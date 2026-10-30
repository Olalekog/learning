"""Interview Copilot - local server.

Serves the web page and streams Claude's suggested answers.
Your API key stays here on the server and never reaches the browser.

Run:  python server.py     then open http://localhost:8765

For phone access, set ACCESS_CODE so only people with the code can use your API
credit (start-mobile.bat does this for you).
"""

import hmac
import io
import json
import os
import queue
import re
import sys
import threading
import time
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlsplit

import anthropic

import bank
import chatwatch
import refs

PORT = int(os.environ.get("PORT", "8765"))
HOST = os.environ.get("HOST", "127.0.0.1")  # 0.0.0.0 = reachable from other devices on your Wi-Fi
ACCESS_CODE = os.environ.get("ACCESS_CODE", "").strip()
MODEL = os.environ.get("COPILOT_MODEL", "claude-opus-5-5")
EFFORT = os.environ.get("COPILOT_EFFORT", "low")  # low = fastest live answers
STORY_EFFORT = os.environ.get("COPILOT_STORY_EFFORT", "medium")  # story bank is built once, so take more care
MAX_UPLOAD = 5 * 1024 * 1024
HERE = Path(__file__).parent
# Folder of resumes the page can load from. Default: the "Resume" folder next to this app's folder.
RESUME_DIR = Path(os.environ.get("RESUME_DIR", HERE.parent / "Resume"))
RESUME_TYPES = (".docx", ".pdf", ".md", ".txt")
# Study notes searched for technical answers. Default: the folder this app sits in (your learning folder).
REFERENCE_DIR = Path(os.environ.get("REFERENCE_DIR", HERE.parent))
REFERENCE_SKIP = refs.DEFAULT_SKIP | {x.strip() for x in os.environ.get("REFERENCE_SKIP", "").split(",") if x.strip()}
LIBRARY = refs.Library(REFERENCE_DIR, REFERENCE_SKIP)
BANK = bank.Bank(HERE / "data" / "bank.json")  # question bank: asked + notes + your own
# Official documentation Claude may search live (subdomains included, e.g. docs.aws.amazon.com).
OFFICIAL_DOCS = [d.strip() for d in os.environ.get("OFFICIAL_DOCS_DOMAINS", ",".join([
    "aws.amazon.com",                    # AWS docs, whitepapers, FAQs
    "learn.microsoft.com/en-us/azure",   # Azure docs
    "azure.microsoft.com",
    "cloud.google.com",                  # Google Cloud docs
    "linux.org",                         # Linux
    "kernel.org",                        # Linux kernel docs (docs.kernel.org)
    "man7.org",                          # Linux man pages
    "linuxfoundation.org",
])).split(",") if d.strip()]
SEARCH_PRICE = 0.01  # USD per web search ($10 per 1,000)
DOCS_MODES = ("auto", "always", "off")
# Resume, target role and story bank, shared by every device (kept out of git).
PROFILE_FILE = HERE / "data" / "profile.json"
PROFILE_FIELDS = ("profile", "role", "stories")

ANSWER_PROMPT = """You help a job candidate during a live interview. You receive a speech-to-text \
transcript of what the interviewer just said. The candidate's resume, target role and STAR story \
bank follow below. Latency-sensitive; begin your visible answer immediately.

Everything you write is something the candidate will say out loud: first person, natural spoken \
English, confident and honest. The transcript may contain recognition errors; infer the intended question.

## Behavioral, leadership and STAR questions
These include "tell me about a time...", "give me an example...", "describe a situation...", \
"how do you handle...", "what would your team say...", and anything about leadership, conflict, \
failure, mistakes, pressure, deadlines, ambiguity, influence, mentoring, disagreement, ownership, \
change or achievements.

Answer with ONE real story from the story bank, or straight from the resume if the bank is empty. \
Pick the story that best fits what the question is really testing. Avoid a story already used \
earlier in this interview when another one fits. Use this exact format:

**Story:** <story title> (<company>)
**Situation:** 1-2 sentences of context.
**Task:** 1 sentence: what you were responsible for.
**Action:**
- 2-4 bullets of what *you* did, starting with "I". For leadership questions show how you led \
people: set direction, aligned stakeholders, delegated, coached, made the call.
**Result:** the outcome, using the real numbers from the resume or story bank.
**Lesson:** one short sentence (only for leadership, failure, mistake or conflict questions).

Facts rule: use only companies, roles, projects, tools and numbers that appear in the resume or \
story bank. Never invent them. If a detail is missing, leave a visible placeholder such as \
[fill in: who disagreed] so the candidate can supply it. If no story truly fits, start with \
**Closest story:** instead of **Story:** and use the nearest one. Aim for about 180 words.

## Technical, architecture and scenario questions
Start with a one-sentence direct answer, then 3-5 short bullets: how it works or how I would do it, \
the key trade-off or best practice, and a real example from my resume or notes when one fits. \
Include a tiny code or CLI snippet only if it helps. Aim for about 170 words.

## Reference notes
The candidate's own study notes may be attached as <reference_notes>. They were picked by keyword \
search, so some may not fit the question. When a note is relevant:
- Build the answer from it first: reuse its facts, numbers, service names, design patterns, \
commands and the candidate's own phrasing and examples. Fill gaps with accurate general knowledge.
- If a note holds a prepared answer to this same question, keep its structure and key points, \
tightened for speaking.
- If a note is wrong or outdated, give the correct answer instead.
Ignore notes that don't fit. Never mention "notes", "documents" or "sources" in the spoken answer.

## Saved answers
If a <saved_answer> is attached, it is the candidate's own polished answer to this question from their \
question bank. Follow it closely (same story, points and numbers), tightened for speaking. It takes \
priority over reference notes.

## Official documentation search
When the web_search tool is available, it searches only official AWS, Azure, Google Cloud and \
Linux documentation. Use it for technical questions the notes don't cover well, or to confirm exact \
limits, defaults, quotas, commands or recent changes. Search at most twice with short, specific \
queries. Don't search for behavioral, personal or simple questions. Write nothing before searching. \
Never read URLs aloud or mention searching in the spoken answer.

## All other questions
- Start with a one-sentence direct answer, then 2-4 short bullets, grounded in the resume where relevant.
- "Tell me about yourself": a 4-5 sentence pitch from the resume, ending with why this target role.
- If the speech is not a question (small talk, instructions), reply with one short line suggesting how to respond.
- Keep it under about 150 words unless the question truly needs more.

Use simple Markdown (bold, bullets, `code`). No preamble like "Here's an answer"."""

STORY_PROMPT = """You turn a candidate's resume into a STAR story bank for behavioral and \
leadership interview questions.

Write 8 to 12 stories. Together they should cover as many of these themes as the resume \
supports: leadership, leading without authority, conflict, failure or mistake, tight deadline \
or pressure, ambiguity, mentoring or developing others, stakeholder or customer management, \
process improvement or automation, disagreeing with a manager, biggest achievement, learning \
something new fast. Prefer recent roles and stories with measurable results. If a target role \
is given, favour stories that matter most for it.

Format every story exactly like this, in first person:

### <number>. <Short title> - <Company>, <Role>, <Years>
**Themes:** <2-4 themes from the list>
- **Situation:** 1-2 sentences.
- **Task:** 1 sentence.
- **Action:** 2-3 sentences of what I did.
- **Result:** the outcome with numbers from the resume.

Facts rule: use only facts in the resume. Resumes rarely say who disagreed, what went wrong or \
how a conflict was resolved; where a story needs a detail like that, write a placeholder such as \
[fill in: what the disagreement was about] instead of inventing it.

After the stories, add a line "**Gaps:**" listing themes the resume gives no story for, so the \
candidate can prepare one. Output only the story bank."""


def clean_api_key():
    """Strip spaces and quotes that often sneak in when a key is pasted."""
    raw = os.environ.get("ANTHROPIC_API_KEY", "")
    key = raw.strip().strip('"').strip("'").strip()
    if key != raw:
        os.environ["ANTHROPIC_API_KEY"] = key
    return key, key != raw


def check_api_key():
    """Free call that tells us if the key works. Returns 'ok', 'missing', 'rejected' or 'unknown'."""
    if not have_key():
        return "missing"
    try:
        get_client().models.list(limit=1)
        return "ok"
    except anthropic.AuthenticationError:
        return "rejected"
    except anthropic.APIError:
        return "unknown"  # offline or temporary problem; answers may still work later


def have_key():
    return bool(os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("ANTHROPIC_AUTH_TOKEN"))


KEY_STATUS = "unknown"
client = None


def get_client():
    global client
    if client is None:
        client = anthropic.Anthropic()
    return client


extract_resume_text = refs.extract_text  # .docx / .pdf / .txt / .md -> text

def list_resumes():
    """Resume files in RESUME_DIR (skips Word's ~$ lock files)."""
    if not RESUME_DIR.is_dir():
        return []
    return sorted(p.name for p in RESUME_DIR.iterdir()
                  if p.is_file() and p.suffix.lower() in RESUME_TYPES and not p.name.startswith("~$"))


def candidate_context(profile, role, stories):
    parts = []
    if profile.strip():
        parts.append(f"<resume>\n{profile.strip()}\n</resume>")
    if role.strip():
        parts.append(f"<target_role>\n{role.strip()}\n</target_role>")
    if stories.strip():
        parts.append(f"<story_bank>\n{stories.strip()}\n</story_bank>")
    return "\n\n".join(parts) or "<resume>\n(The candidate has not added a resume yet.)\n</resume>"


def answer_request(question, profile, history, notes=None, saved=None):
    """System prompt + candidate context (cached between questions), then the live question."""
    system = [
        {"type": "text", "text": ANSWER_PROMPT},
        {
            "type": "text",
            "text": candidate_context(profile.get("profile", ""), profile.get("role", ""),
                                      profile.get("stories", "")),
            "cache_control": {"type": "ephemeral"},  # same for every question -> cheaper, faster
        },
    ]
    context = []
    if history:
        lines = [f"Q: {h['q']}\nA: {h['a']}" for h in history[-4:]]
        context.append("<earlier_in_this_interview>\n" + "\n\n".join(lines) + "\n</earlier_in_this_interview>")
    if saved:
        context.append(f'<saved_answer question="{saved["question"]}">\n{saved["answer"]}\n</saved_answer>')
    if notes:
        body = "\n\n".join(f'<note source="{n["file"]} › {n["label"]}">\n{n["text"]}\n</note>' for n in notes)
        context.append(f"<reference_notes>\n{body}\n</reference_notes>")
    context.append(f"<interviewer_said>\n{question.strip()}\n</interviewer_said>")
    return system, [{"role": "user", "content": "\n\n".join(context)}]


def load_profile():
    try:
        data = json.loads(PROFILE_FILE.read_text(encoding="utf-8"))
        return {k: str(data.get(k, "")) for k in PROFILE_FIELDS}
    except (OSError, ValueError):
        return {k: "" for k in PROFILE_FIELDS}


# ---------------------------------------------------------------- usage metrics

# Estimated USD per million tokens: input, output, cache read, cache write (5-minute cache).
# Check https://www.anthropic.com/pricing if prices change.
PRICES = {
    "claude-opus-5-5": (4.00, 20.00, 0.20, 5.00),
    "claude-sonnet-5-5": (2.00, 10.00, 0.20, 2.50),
    "claude-haiku-5-5": (0.10, 0.50, 0.01, 0.125),
    "claude-opus-5": (5.00, 25.00, 0.50, 6.25),
    "claude-opus-4-8": (5.00, 25.00, 0.50, 6.25),
    "claude-fable-5-1": (10.00, 50.00, 0.25, 12.50),
}
USAGE_FILE = HERE / "data" / "usage.jsonl"
SETTINGS_FILE = HERE / "data" / "settings.json"


def price_for(model):
    if model in PRICES:
        return PRICES[model]
    for name in sorted(PRICES, key=len, reverse=True):
        if model.startswith(name):
            return PRICES[name]
    return PRICES["claude-opus-5-5"]


class Metrics:
    """Token use, cost, speed and rate limits for every call, saved in data/usage.jsonl."""

    def __init__(self):
        self.lock = threading.Lock()
        self.records = []
        self.limits = {}      # latest rate-limit headers from the API
        self.limits_at = None
        try:
            for line in USAGE_FILE.read_text(encoding="utf-8").splitlines():
                if line.strip():
                    self.records.append(json.loads(line))
        except (OSError, ValueError):
            pass
        try:
            self.settings = json.loads(SETTINGS_FILE.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            self.settings = {}
        if "budget" not in self.settings:
            self.settings["budget"] = float(os.environ.get("COPILOT_BUDGET_USD", "0") or 0)

    def set_budget(self, budget):
        self.update_settings(budget=max(0.0, float(budget)))

    def update_settings(self, **changes):
        with self.lock:
            self.settings.update(changes)
            SETTINGS_FILE.parent.mkdir(exist_ok=True)
            SETTINGS_FILE.write_text(json.dumps(self.settings), encoding="utf-8")

    def update_limits(self, headers):
        found = {}
        for k, v in (headers or {}).items():
            k = k.lower()
            if k.startswith("anthropic-ratelimit-"):
                found[k[len("anthropic-ratelimit-"):]] = v
        if found:
            with self.lock:
                self.limits, self.limits_at = found, time.time()

    def record(self, kind, label, model, u, ttft, total, status, interview=None):
        u = {k: u.get(k, 0) for k in ("input", "output", "cache_read", "cache_write", "searches")}
        p = price_for(model)
        cost = (u["input"] * p[0] + u["output"] * p[1] + u["cache_read"] * p[2] + u["cache_write"] * p[3]) / 1e6
        cost += u["searches"] * SEARCH_PRICE
        rec = {"ts": round(time.time(), 1), "kind": kind, "label": label[:120], "model": model, **u,
               "cost": round(cost, 6), "saved": round(u["cache_read"] * (p[0] - p[2]) / 1e6, 6),
               "ttft": round(ttft, 2) if ttft is not None else None, "total": round(total, 2), "status": status,
               "interview": interview}
        with self.lock:
            self.records.append(rec)
            USAGE_FILE.parent.mkdir(exist_ok=True)
            with USAGE_FILE.open("a", encoding="utf-8") as f:
                f.write(json.dumps(rec) + "\n")
        return rec

    def stats(self, interview_id):
        now = time.localtime()
        today = time.mktime((now.tm_year, now.tm_mon, now.tm_mday, 0, 0, 0, 0, 0, -1))
        month = time.mktime((now.tm_year, now.tm_mon, 1, 0, 0, 0, 0, 0, -1))
        with self.lock:
            records = list(self.records)
            limits, limits_at, budget = dict(self.limits), self.limits_at, self.settings.get("budget", 0)

        def summary(since=0, interview=None):
            rs = [r for r in records if r["ts"] >= since and (interview is None or r.get("interview") == interview)]
            answers = [r for r in rs if r["kind"] == "answer"]
            tin = sum(r["input"] + r["cache_read"] + r["cache_write"] for r in rs)
            ttfts = [r["ttft"] for r in answers if r.get("ttft") is not None]
            totals = [r["total"] for r in answers if r["status"] == "ok"]
            return {
                "answers": len(answers),
                "stories": sum(1 for r in rs if r["kind"] == "stories"),
                "input": tin, "output": sum(r["output"] for r in rs),
                "cache_read": sum(r["cache_read"] for r in rs),
                "searches": sum(r.get("searches", 0) for r in rs),
                "cost": round(sum(r["cost"] for r in rs), 4),
                "saved": round(sum(r.get("saved", 0) for r in rs), 4),
                "avg_ttft": round(sum(ttfts) / len(ttfts), 2) if ttfts else None,
                "avg_total": round(sum(totals) / len(totals), 2) if totals else None,
                "avg_cost": round(sum(r["cost"] for r in answers) / len(answers), 5) if answers else None,
            }

        periods = {"interview": summary(interview=interview_id or "-"), "today": summary(today),
                   "month": summary(month), "all": summary(0)}
        spent = periods["month"]["cost"]
        recent = [{"ts": r["ts"], "label": r["label"], "in": r["input"] + r["cache_read"] + r["cache_write"],
                   "out": r["output"], "cost": r["cost"], "ttft": r.get("ttft"), "total": r["total"],
                   "kind": r["kind"], "status": r["status"], "searches": r.get("searches", 0)}
                  for r in records[-20:]]
        return {"periods": periods, "budget": budget, "month_spent": spent,
                "budget_left": round(budget - spent, 4) if budget else None,
                "limits": limits, "limits_at": limits_at, "recent": recent, "model": MODEL,
                "use_refs": self.settings.get("use_refs", True),
                "docs_mode": self.settings.get("docs_mode", "auto"),
                "chat_watch": self.settings.get("chat_watch", "questions"),
                "chat_available": chatwatch.ClipboardWatcher.available()}


METRICS = Metrics()


def usage_dict(usage):
    stu = getattr(usage, "server_tool_use", None)
    return {
        "input": getattr(usage, "input_tokens", 0) or 0,
        "output": getattr(usage, "output_tokens", 0) or 0,
        "cache_read": getattr(usage, "cache_read_input_tokens", 0) or 0,
        "cache_write": getattr(usage, "cache_creation_input_tokens", 0) or 0,
        "searches": (getattr(stu, "web_search_requests", 0) or 0) if stu else 0,
    }


def add_usage(a, b):
    return {k: a.get(k, 0) + b.get(k, 0) for k in set(a) | set(b)}


def docs_tool():
    """Server-side web search limited to official documentation sites."""
    return {"type": "web_search_20260209", "name": "web_search", "max_uses": 2, "allowed_domains": OFFICIAL_DOCS}


def doc_links(content):
    """Pages the answer cited; if it cited none, the top search results."""
    cited, found = [], []
    for block in content:
        btype = getattr(block, "type", "")
        if btype == "text":
            for c in getattr(block, "citations", None) or []:
                url = getattr(c, "url", None)
                if url:
                    cited.append({"url": url, "title": getattr(c, "title", "") or url})
        elif btype == "web_search_tool_result" and isinstance(getattr(block, "content", None), list):
            for r in block.content:
                url = getattr(r, "url", None)
                if url:
                    found.append({"url": url, "title": getattr(r, "title", "") or url})
    out, seen = [], set()
    for link in cited or found[:3]:
        if link["url"] not in seen:
            seen.add(link["url"])
            out.append(link)
    return out[:5]


def stream_claude(system, messages, effort, max_tokens, emit, cancelled=lambda: False,
                  kind="answer", label="", tools=None, on_search=None, interview=None, fmt=None):
    """Stream Claude's text to emit(); errors are emitted as readable text.
    Returns the usage record for this call (None if the call never ran); record["links"] lists doc pages used."""
    started, first, total, served, status = time.time(), None, {}, MODEL, "ok"
    links, convo = [], list(messages)
    try:
        for _ in range(4):  # first request + up to 3 resumes if a search turn pauses
            kw = dict(model=MODEL, max_tokens=max_tokens, system=system,
                      output_config={"effort": effort, **({"format": fmt} if fmt else {})},
                      betas=["server-side-fallback-2026-07-01"], fallbacks="default", messages=convo)
            if tools:
                kw["tools"] = tools
            with get_client().beta.messages.stream(**kw) as stream:
                try:
                    METRICS.update_limits(stream.response.headers)
                except Exception:
                    pass
                for event in stream:
                    if cancelled():
                        status = "cancelled"  # a newer question arrived; keep what was used so far
                        try:
                            total = add_usage(total, usage_dict(stream.current_message_snapshot.usage))
                        except Exception:
                            pass
                        break  # leaving the block closes the connection to the API
                    if event.type == "content_block_start" and \
                            getattr(event.content_block, "type", "") == "server_tool_use":
                        if on_search:
                            on_search()
                    elif event.type == "text":
                        if first is None:
                            first = time.time()
                        emit(event.text)
                if status != "ok":
                    break
                final = stream.get_final_message()
            total = add_usage(total, usage_dict(final.usage))
            served = final.model or MODEL
            links += [l for l in doc_links(final.content) if l["url"] not in {x["url"] for x in links}]
            if final.stop_reason == "pause_turn":  # long search turn: resume where it stopped
                convo = convo + [{"role": "assistant", "content": final.content}]
                continue
            if final.stop_reason == "refusal":
                emit("\n\n_(Claude declined to answer this one.)_")
            break
    except anthropic.AuthenticationError:
        emit("**Error:** Claude rejected your API key. Create a new key at console.anthropic.com "
             "(Settings → API Keys), copy all of it, then close the server window and start it again.")
    except anthropic.RateLimitError as e:
        METRICS.update_limits(getattr(e.response, "headers", {}))
        emit("**Error:** rate limited by the API. Wait a few seconds and try again.")
    except anthropic.BadRequestError as e:
        if tools and first is None:
            # e.g. web search is turned off for this Anthropic organization: answer without it
            rec = stream_claude(system, messages, effort, max_tokens, emit, cancelled, kind, label,
                                interview=interview)
            emit("\n\n_(Official docs search isn't available for your API account, so this answer "
                 "doesn't use it. An admin can turn on web search in the Anthropic Console.)_")
            return rec
        emit(f"**Error from the API ({e.status_code}):** {e.message}")
    except anthropic.APIStatusError as e:
        emit(f"**Error from the API ({e.status_code}):** {e.message}")
    except anthropic.APIConnectionError:
        emit("**Error:** could not reach the Claude API. Check your internet connection.")
    if not total:
        return None
    rec = METRICS.record(kind, label, served, total,
                         (first - started) if first else None, time.time() - started, status, interview)
    return {**rec, "links": links}

INTERVIEWS_DIR = HERE / "data" / "interviews"
RECORDINGS_DIR = HERE / "data" / "recordings"   # screen recordings, one folder per interview


def interview_markdown(iv):
    """A saved interview as a readable Markdown document."""
    def when(ts):
        return time.strftime("%a %d %b %Y, %H:%M", time.localtime(ts)) if ts else "-"

    lines = [f"# {iv['name']}", ""]
    lines.append(f"- **Started:** {when(iv.get('started_at'))}")
    lines.append(f"- **Ended:** {when(iv.get('stopped_at'))}")
    if iv.get("started_at") and iv.get("stopped_at"):
        lines.append(f"- **Length:** {round((iv['stopped_at'] - iv['started_at']) / 60)} min")
    items = [it for it in iv["items"] if it.get("a")]
    cost = sum((it.get("usage") or {}).get("cost", 0) for it in items)
    lines.append(f"- **Questions:** {len(items)}  ·  **Estimated cost:** ${cost:.2f}")
    lines.append("")
    for n, it in enumerate(items, 1):
        lines += ["---", "", f"## Q{n}. {it['q']}", ""] + (["*Asked in the chat*", ""] if it.get("via") == "chat" else [])
        if it.get("ts"):
            lines += [f"_{time.strftime('%H:%M', time.localtime(it['ts']))}_", ""]
        lines += ["**Suggested answer:**", "", it["a"].strip(), ""]
        if (it.get("mine") or {}).get("text"):
            lines += ["**What I said:**", "", it["mine"]["text"].strip(), ""]
        if it.get("sources"):
            lines.append("**From your notes:** " + "; ".join(f"{s['label']} (`{s['file']}`)" for s in it["sources"]))
            lines.append("")
        if it.get("docs"):
            lines.append("**From official docs:** " + "; ".join(f"[{d['title']}]({d['url']})" for d in it["docs"]))
            lines.append("")
    a = iv.get("analysis")
    if a:
        o = a["overall"]
        lines += ["---", "", "# Analysis", "",
                  f"**Overall {o['overall']}/10** · Correctness {o['correctness']} · Behavioral {o['behavioral']} · "
                  f"Composure {o['composure']} · Communication {o['communication']}", "", a["summary"], "",
                  "**Strengths**", ""] + [f"- {x}" for x in a["strengths"]] + ["", "**Improve**", ""] + \
                 [f"- {x}" for x in a["improvements"]] + ["",
                  f"**Interviewer focus ({a['interviewer']['difficulty']}):** {a['interviewer']['focus']}", ""]
        for q in a["questions"]:
            head = f"### Q{q['number']}. {q.get('question', '')}"
            score = (f"Overall {q['overall']}/10 · Correctness {q['correctness']} · Behavioral {q['behavioral']} · "
                     f"Composure {q['composure']} · Communication {q['communication']}") if q["captured"] else "Answer not captured"
            lines += [head, "", f"_{score}_", "", q["feedback"], "", "**Stronger answer:** " + q["better_answer"], ""]
    return "\n".join(lines)


class Session:
    """Saved interviews (one tab each). One interview is live at a time; every device sees the same data."""

    def __init__(self):
        self.lock = threading.RLock()
        self.subscribers = set()
        self.profile = load_profile()
        self.interviews = {}     # id -> {id, name, status: ready|live|ended, created, started_at, stopped_at, items}
        self.cancel = None       # stops the answer being written when a newer question arrives
        self.writing = None      # (interview id, item) being written
        INTERVIEWS_DIR.mkdir(parents=True, exist_ok=True)
        for f in INTERVIEWS_DIR.glob("*.json"):
            try:
                iv = json.loads(f.read_text(encoding="utf-8"))
                for it in iv["items"]:
                    it["done"] = True  # anything unfinished when the server stopped is final now
                if iv.get("analysis_status") == "running":
                    iv["analysis_status"] = "error"
                for rec in iv.get("recordings", []):
                    if rec["status"] == "recording":
                        rec["status"] = "saved"  # the server stopped mid-recording; keep what arrived
                self.interviews[iv["id"]] = iv
            except (OSError, ValueError, KeyError):
                pass
        live = sorted((iv for iv in self.interviews.values() if iv["status"] == "live"),
                      key=lambda iv: iv.get("started_at") or 0)
        for iv in live[:-1]:  # only one can be live
            iv["status"] = "ended"
        self.active = live[-1]["id"] if live else None

    # ------------------------------------------------------------ helpers
    def broadcast(self, event):
        with self.lock:
            subs = list(self.subscribers)
        for q in subs:
            q.put(event)

    def _save(self, iv):
        tmp = INTERVIEWS_DIR / f"{iv['id']}.tmp"
        tmp.write_text(json.dumps(iv, ensure_ascii=False, indent=1), encoding="utf-8")
        tmp.replace(INTERVIEWS_DIR / f"{iv['id']}.json")

    def _meta(self, iv):
        done = [it for it in iv["items"] if it.get("a")]
        return {"id": iv["id"], "name": iv["name"], "status": iv["status"], "created": iv["created"],
                "started_at": iv.get("started_at"), "stopped_at": iv.get("stopped_at"), "count": len(done),
                "cost": round(sum((it.get("usage") or {}).get("cost", 0) for it in done), 4),
                "recordings": [dict(r) for r in iv.get("recordings", [])]}

    def list_meta(self):
        with self.lock:
            return sorted((self._meta(iv) for iv in self.interviews.values()), key=lambda m: -m["created"])

    def _announce(self):
        self.broadcast({"type": "interviews", "list": self.list_meta(), "active": self.active})

    def stats_focus(self):
        """Interview the usage panel's "This interview" refers to: the live one, else the newest."""
        with self.lock:
            if self.active:
                return self.active
            newest = max(self.interviews.values(), key=lambda iv: iv["created"], default=None)
            return newest["id"] if newest else None

    def get(self, iid):
        with self.lock:
            iv = self.interviews.get(iid)
            return json.loads(json.dumps(iv)) if iv else None  # a copy

    def snapshot(self):
        snap = {"type": "snapshot", "list": self.list_meta(), "active": self.active}
        snap["stats"] = METRICS.stats(self.stats_focus())
        snap["refs"] = LIBRARY.status()
        return snap

    # ------------------------------------------------------------ interview lifecycle
    def create(self, name=""):
        with self.lock:
            now = time.time()
            iv = {"id": uuid.uuid4().hex[:10],
                  "name": (name or "").strip()[:80] or "Interview " + time.strftime("%d %b %H:%M", time.localtime(now)),
                  "status": "ready", "created": now, "started_at": None, "stopped_at": None, "items": []}
            self.interviews[iv["id"]] = iv
            self._save(iv)
        self._announce()
        return iv["id"]

    def _stop_locked(self, iv):
        if self.writing and self.writing[0] == iv["id"] and self.cancel:
            self.cancel.set()
        iv["status"], iv["stopped_at"] = "ended", time.time()
        if self.active == iv["id"]:
            self.active = None
        self._save(iv)

    def start(self, iid):
        with self.lock:
            iv = self.interviews.get(iid)
            if not iv:
                return False
            for other in self.interviews.values():
                if other["status"] == "live" and other["id"] != iid:
                    self._stop_locked(other)
            iv["status"] = "live"
            iv["started_at"] = iv.get("started_at") or time.time()
            iv["stopped_at"] = None
            self.active = iid
            self._save(iv)
        self._announce()
        self.broadcast_stats()
        return True

    def stop(self, iid):
        with self.lock:
            iv = self.interviews.get(iid)
            if not iv:
                return False
            if iv["status"] == "live":
                self._stop_locked(iv)
        self.broadcast({"type": "stopped", "interview": iid})
        self._announce()
        return True

    def rename(self, iid, name):
        with self.lock:
            iv = self.interviews.get(iid)
            if not iv or not name.strip():
                return False
            iv["name"] = name.strip()[:80]
            self._save(iv)
        self._announce()
        return True

    def delete(self, iid):
        with self.lock:
            iv = self.interviews.pop(iid, None)
            if not iv:
                return False
            if self.writing and self.writing[0] == iid and self.cancel:
                self.cancel.set()
            if self.active == iid:
                self.active = None
            try:
                (INTERVIEWS_DIR / f"{iid}.json").unlink()
            except OSError:
                pass
            folder = RECORDINGS_DIR / iid
            for f in folder.glob("*.webm") if folder.is_dir() else []:
                try:
                    f.unlink()
                except OSError:
                    pass
            try:
                folder.rmdir()
            except OSError:
                pass
        self._announce()
        return True

    # ------------------------------------------------------------ what I actually said + analysis
    def save_mine(self, iid, item_id, text, seconds=None, pauses=None):
        with self.lock:
            iv = self.interviews.get(iid)
            item = next((it for it in iv["items"] if it["id"] == item_id), None) if iv else None
            if not item:
                return None
            text = text.strip()
            item["mine"] = {"text": text, "metrics": speech_metrics(text, seconds, pauses), "ts": time.time()} if text else None
            self._save(iv)
            mine = item["mine"]
        self.broadcast({"type": "mine", "interview": iid, "id": item_id, "mine": mine})
        return mine or {}

    def analyze(self, iid):
        with self.lock:
            iv = self.interviews.get(iid)
            if not iv or iv.get("analysis_status") == "running":
                return False
            iv["analysis_status"] = "running"
            snapshot, profile = json.loads(json.dumps(iv)), dict(self.profile)
        self.broadcast({"type": "analysis", "interview": iid, "status": "running"})
        threading.Thread(target=self._run_analysis, args=(iid, snapshot, profile), daemon=True).start()
        return True

    def _run_analysis(self, iid, iv, profile):
        system, messages, items = analysis_request(iv, profile)
        out = []
        rec = stream_claude(system, messages, ANALYSIS_EFFORT, 16000, out.append, kind="analysis",
                            label="Analysis: " + iv["name"], interview=iid, fmt={"type": "json_schema", "schema": ANALYSIS_SCHEMA})
        text, result, error = "".join(out), None, None
        try:
            result = json.loads(text)
            clamp = lambda v: max(1, min(10, int(v)))  # scored answers are always 1-10
            for q in result["questions"]:
                for k in SCORES:
                    q[k] = clamp(q[k]) if q.get("captured") else 0
                if 1 <= q["number"] <= len(items):  # attach the question text and item id
                    q["question"], q["item"] = items[q["number"] - 1]["q"], items[q["number"] - 1]["id"]
            rated = [q for q in result["questions"] if q.get("captured")]
            for k in SCORES:  # overall = average of the captured answers, so it always matches the details
                result["overall"][k] = round(sum(q[k] for q in rated) / len(rated)) if rated else 0
            result.update(created=time.time(), model=MODEL, captured=len(rated), total=len(result["questions"]),
                          cost=rec["cost"] if rec else None)
        except (ValueError, KeyError, TypeError):
            error = text.strip()[:400] if text.strip().startswith("**Error") else \
                "The analysis didn't come back in the expected form. Please try again."
        with self.lock:
            live = self.interviews.get(iid)
            if live:
                live["analysis_status"] = "error" if error else "done"
                if result and not error:
                    live["analysis"] = result
                self._save(live)
        self.broadcast({"type": "analysis", "interview": iid, "status": "error" if error else "done",
                        "analysis": None if error else result, "error": error})
        if rec:
            self.broadcast_stats()

    # ------------------------------------------------------------ screen recordings
    def recording_path(self, iid, rid):
        if not (iid.isalnum() and rid.isalnum()):
            return None  # ids are generated by us; anything else is not a file we made
        return RECORDINGS_DIR / iid / f"{rid}.webm"

    def find_recording(self, iid, rid):
        iv = self.interviews.get(iid)
        return next((r for r in iv.get("recordings", []) if r["id"] == rid), None) if iv else None

    def start_recording(self, iid, mime):
        with self.lock:
            iv = self.interviews.get(iid)
            if not iv:
                return None
            rid = uuid.uuid4().hex[:10]
            path = self.recording_path(iid, rid)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(b"")
            iv.setdefault("recordings", []).append({
                "id": rid, "status": "recording", "started": time.time(), "ended": None,
                "seconds": 0, "bytes": 0, "mime": mime[:60] or "video/webm"})
            self._save(iv)
        self._announce()
        return rid

    def add_chunk(self, iid, rid, data):
        with self.lock:
            rec = self.find_recording(iid, rid)
            path = self.recording_path(iid, rid)
            if not rec or not path or rec["status"] != "recording":
                return False
            with path.open("ab") as f:
                f.write(data)
            rec["bytes"] += len(data)
            rec["seconds"] = round(time.time() - rec["started"])
        return True

    def finish_recording(self, iid, rid):
        with self.lock:
            rec = self.find_recording(iid, rid)
            if not rec:
                return False
            rec["status"], rec["ended"] = "saved", time.time()
            rec["seconds"] = round(rec["ended"] - rec["started"])
            self._save(self.interviews[iid])
        self._announce()
        return True

    def delete_recording(self, iid, rid):
        with self.lock:
            iv = self.interviews.get(iid)
            rec = self.find_recording(iid, rid)
            if not rec:
                return False
            iv["recordings"].remove(rec)
            try:
                self.recording_path(iid, rid).unlink()
            except OSError:
                pass
            self._save(iv)
        self._announce()
        return True

    # ------------------------------------------------------------ questions and answers
    def ask(self, question, origin, iid, via=None):
        """Answer in interview iid (started automatically if it isn't live). via="chat": copied from a chat."""
        with self.lock:
            iv = self.interviews.get(iid)
        if not iv:
            return None
        if iv["status"] != "live":
            self.start(iid)
        with self.lock:
            if self.cancel:
                self.cancel.set()
            earlier = [{"q": it["q"], "a": it["a"]} for it in iv["items"] if it.get("a")][-4:]
            notes = []
            if METRICS.settings.get("use_refs", True):
                notes = LIBRARY.search(question)
                if not notes and earlier and len(question.split()) < 7:
                    # vague follow-up ("why is that?"): borrow the topic of the last question
                    notes = LIBRARY.search(question + " " + earlier[-1]["q"])
            sources = [{"file": n["file"], "label": n["label"]} for n in notes]
            saved = BANK.best_saved_answer(question)
            if saved:
                sources.insert(0, {"file": "Question bank", "label": saved["question"]})
            item = {"id": uuid.uuid4().hex[:12], "q": question, "a": "", "done": False, "ts": time.time(),
                    "sources": sources}
            if via:
                item["via"] = via
            iv["items"].append(item)
            self.cancel, self.writing = threading.Event(), (iid, item)
            cancel, profile = self.cancel, dict(self.profile)
        self.broadcast({"type": "question", "interview": iid, "id": item["id"], "q": question,
                        "origin": origin, "sources": sources, "via": via})
        threading.Thread(target=self._write_answer, args=(iv, item, cancel, profile, earlier, notes, saved),
                         daemon=True).start()
        return item["id"]

    def _write_answer(self, iv, item, cancel, profile, earlier, notes, saved=None):
        iid = iv["id"]

        def emit(text):
            with self.lock:
                item["a"] += text
            self.broadcast({"type": "delta", "interview": iid, "id": item["id"], "text": text})

        system, messages = answer_request(item["q"], profile, earlier, notes, saved)
        mode = METRICS.settings.get("docs_mode", "auto")
        tools = [docs_tool()] if mode == "always" or (mode == "auto" and not notes) else None
        rec = stream_claude(system, messages, EFFORT, 4000, emit, cancel.is_set, kind="answer", label=item["q"],
                            tools=tools, interview=iid,
                            on_search=lambda: self.broadcast({"type": "searching", "interview": iid, "id": item["id"]}))
        summary = None
        if rec:
            summary = {"in": rec["input"] + rec["cache_read"] + rec["cache_write"], "cached": rec["cache_read"],
                       "written": rec["cache_write"], "searches": rec["searches"],
                       "out": rec["output"], "cost": rec["cost"], "ttft": rec["ttft"], "total": rec["total"]}
        docs = rec["links"] if rec else []
        with self.lock:
            item.update(done=True, usage=summary, docs=docs)
            if not item["a"].strip() and item in iv["items"]:
                iv["items"].remove(item)  # cancelled before any words: nothing worth keeping
            if self.writing and self.writing[1] is item:
                self.writing = None
            if iid in self.interviews:
                self._save(iv)  # saved after every answer
        # full text included so a device that joined mid-answer ends up with exactly the saved answer
        self.broadcast({"type": "done", "interview": iid, "id": item["id"], "a": item["a"],
                        "usage": summary, "docs": docs})
        self._announce()
        if item["a"].strip() and rec and rec["status"] == "ok" and iid in self.interviews:
            BANK.add_asked(item["q"], item["a"], iid, iv["name"], item["id"], item["ts"])
            self.broadcast({"type": "bank"})
        if rec:
            self.broadcast_stats()

    def from_chat(self, text):
        """Text copied on this PC: answer it if it's an interview question and an interview is live."""
        mode = METRICS.settings.get("chat_watch", "questions")
        with self.lock:
            iv = self.interviews.get(self.active) if self.active else None
            if mode == "off" or not iv:
                return
            recent = iv["items"][-30:]
        question, reason = chatwatch.check(text, mode)
        if question:
            key = bank.norm_text(question)
            if any(bank.norm_text(it["q"]) == key for it in recent[-5:]):
                reason, question = "already answered", None
            elif any(key in bank.norm_text(it.get("a", "")) for it in recent) or BANK.has_answer_text(question):
                reason, question = "copied from an answer", None
        if not question:
            # the copied text itself is never sent: it could be a password
            self.broadcast({"type": "chat", "status": "ignored", "reason": reason})
            return
        if not have_key():
            self.broadcast({"type": "chat", "status": "ignored", "reason": "no API key set"})
            return
        self.ask(question, "chat", iv["id"], via="chat")

    def broadcast_stats(self):
        self.broadcast({"type": "stats", "stats": METRICS.stats(self.stats_focus())})

    def save_profile(self, fields, origin):
        with self.lock:
            for k in PROFILE_FIELDS:
                if k in fields:
                    self.profile[k] = str(fields[k])
            PROFILE_FILE.parent.mkdir(exist_ok=True)
            tmp = PROFILE_FILE.with_suffix(".tmp")
            tmp.write_text(json.dumps(self.profile, ensure_ascii=False, indent=1), encoding="utf-8")
            tmp.replace(PROFILE_FILE)
            changed = {k: self.profile[k] for k in PROFILE_FIELDS if k in fields}
        self.broadcast({"type": "profile", "origin": origin, **changed})


SESSION = Session()


def reindex_library():
    def run():
        SESSION.broadcast({"type": "refs", "refs": {**LIBRARY.status(), "building": True}})
        LIBRARY.build()
        st = LIBRARY.status()
        print(f"Reference notes: {st['files']} documents, {st['sections']} sections indexed "
              f"in {st['build_seconds']} s from {st['folder']}", flush=True)
        n = BANK.load_notes(LIBRARY)
        print(f"Question bank: {n} questions from your notes", flush=True)
        SESSION.broadcast({"type": "refs", "refs": st})
        SESSION.broadcast({"type": "bank"})
    threading.Thread(target=run, daemon=True).start()


def backfill_bank():
    """Put questions from interviews saved before the bank existed into it (safe to repeat)."""
    with SESSION.lock:
        ivs = [json.loads(json.dumps(iv)) for iv in SESSION.interviews.values()]
    for iv in ivs:
        for it in iv["items"]:
            if it.get("a", "").strip():
                BANK.add_asked(it["q"], it["a"], iv["id"], iv["name"], it["id"], it.get("ts") or iv["created"])


ANALYSIS_EFFORT = os.environ.get("COPILOT_ANALYSIS_EFFORT", "medium")

ANALYSIS_PROMPT = """You are an experienced hiring manager and interview coach reviewing a real interview. \
You get each question the interviewer asked and, when it was captured, what the candidate actually said, \
with speech measurements. The candidate's resume, target role and story bank are attached.

Rate every captured answer from 1 to 10 on four dimensions:
- correctness: technical accuracy and completeness; for behavioral questions, whether the story really \
answers what was asked and is credible.
- behavioral: STAR structure (situation, task, action, result), ownership ("I" not only "we"), concrete \
results with numbers, relevance. For technical questions, rate how well they used real experience as evidence.
- composure: calm, confident, steady delivery. Use the measurements: comfortable pace is about 120-160 \
words per minute; more than 3 filler words per 100 words, several long pauses or many restarts lower the \
score. Speech recognition drops some fillers, so don't penalise what you can't see.
- communication: clarity, structure, conciseness, answering the question directly, no rambling.
Also give "overall" (1-10) for the answer.

Scale: 1-3 poor, 4-5 below the bar, 6-7 meets the bar, 8-9 strong, 10 exceptional. Be honest and \
specific; quote short phrases from the answer when useful. Don't inflate scores.

For each question also give: feedback (2-4 sentences: what worked, what to fix) and better_answer (a \
stronger answer the candidate could say, about 120 words, first person, using only facts from their \
resume or story bank; for gaps write [fill in: ...]).

If an answer was not captured, set captured to false and all scores to 0, and still give feedback on how \
to approach the question and a better_answer.

Then the whole interview: overall scores (average of captured answers, rounded), a 2-3 sentence summary, \
3-5 strengths, 3-5 improvements (most important first), and what the interviewer focused on: main themes, \
what they seemed to probe for, and the difficulty (easy, moderate, hard)."""

SCORE = {"type": "integer", "description": "1 (poor) to 10 (exceptional); 0 if the answer wasn't captured"}
SCORES = {k: SCORE for k in ("correctness", "behavioral", "composure", "communication", "overall")}
ANALYSIS_SCHEMA = {
    "type": "object",
    "properties": {
        "overall": {"type": "object", "properties": SCORES, "required": list(SCORES), "additionalProperties": False},
        "summary": {"type": "string"},
        "strengths": {"type": "array", "items": {"type": "string"}},
        "improvements": {"type": "array", "items": {"type": "string"}},
        "interviewer": {
            "type": "object",
            "properties": {"themes": {"type": "array", "items": {"type": "string"}},
                           "focus": {"type": "string"},
                           "difficulty": {"type": "string", "enum": ["easy", "moderate", "hard"]}},
            "required": ["themes", "focus", "difficulty"], "additionalProperties": False},
        "questions": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {"number": {"type": "integer"},
                               "type": {"type": "string", "enum": ["technical", "behavioral", "leadership", "other"]},
                               "captured": {"type": "boolean"},
                               **SCORES,
                               "feedback": {"type": "string"},
                               "better_answer": {"type": "string"}},
                "required": ["number", "type", "captured", *SCORES, "feedback", "better_answer"],
                "additionalProperties": False}},
    },
    "required": ["overall", "summary", "strengths", "improvements", "interviewer", "questions"],
    "additionalProperties": False,
}

FILLERS = re.compile(r"\b(um+|uh+|erm+|er|ah+|hmm+|you know|i mean|basically|actually|kind of|sort of|literally|so yeah)\b", re.I)


def speech_metrics(text, seconds=None, pauses=None):
    """Simple delivery measurements from what was said."""
    words = re.findall(r"[A-Za-z0-9']+", text)
    n = len(words)
    fillers = [m.group(0).lower() for m in FILLERS.finditer(text)]
    lower = [w.lower() for w in words]
    restarts = sum(1 for a, b in zip(lower, lower[1:]) if a == b and a not in ("very", "really", "that", "had"))
    m = {"words": n, "fillers": len(fillers), "filler_words": sorted(set(fillers)),
         "fillers_per_100": round(100 * len(fillers) / n, 1) if n else 0, "restarts": restarts}
    if seconds:
        m["seconds"] = round(seconds)
        m["wpm"] = round(n / (seconds / 60)) if seconds > 5 else None
    if pauses is not None:
        m["long_pauses"] = int(pauses)
    return m


def analysis_request(iv, profile):
    items = [it for it in iv["items"] if it.get("a") or it.get("mine")]
    parts = [f"Interview: {iv['name']}"]
    for n, it in enumerate(items, 1):
        mine = it.get("mine") or {}
        said = (mine.get("text") or "").strip()
        block = [f"### Question {n}", f"Interviewer: {it['q']}"]
        if said:
            block.append(f"Candidate said: {said}")
            met = mine.get("metrics") or {}
            facts = [f"{met.get('words', 0)} words"]
            if met.get("wpm"):
                facts.append(f"{met['wpm']} words/min over {met.get('seconds')} s")
            facts.append(f"{met.get('fillers', 0)} filler words ({met.get('fillers_per_100', 0)} per 100 words)")
            if met.get("long_pauses") is not None:
                facts.append(f"{met['long_pauses']} pauses longer than 3 s")
            facts.append(f"{met.get('restarts', 0)} repeated-word restarts")
            block.append("Measurements: " + ", ".join(facts))
        else:
            block.append("Candidate said: (not captured)")
        parts.append("\n".join(block))
    system = [
        {"type": "text", "text": ANALYSIS_PROMPT},
        {"type": "text", "text": candidate_context(profile.get("profile", ""), profile.get("role", ""),
                                                   profile.get("stories", ""))},
    ]
    return system, [{"role": "user", "content": "\n\n".join(parts)}], items


def story_request(data):
    content = f"<resume>\n{str(data.get('profile', '')).strip()}\n</resume>"
    role = str(data.get("role", "")).strip()
    if role:
        content += f"\n\n<target_role>\n{role}\n</target_role>"
    return STORY_PROMPT, [{"role": "user", "content": content}]


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"  # needed for chunked streaming

    def log_message(self, fmt, *args):
        if "/events" not in (args[0] if args else ""):  # the live feed would flood the log
            sys.stderr.write("[server] " + (fmt % args) + "\n")

    def _authorized(self):
        """True when no access code is configured, or the request carries the right one."""
        if not ACCESS_CODE:
            return True
        sent = self.headers.get("X-Access-Code", "").strip()
        if not sent:  # the live feed can't send headers, so it passes ?code=
            sent = (parse_qs(urlsplit(self.path).query).get("code") or [""])[0].strip()
        if hmac.compare_digest(sent.encode(), ACCESS_CODE.encode()):
            return True
        time.sleep(1)  # slows down anyone guessing codes
        self.close_connection = True  # any unread request body is discarded with the connection
        self._json(401, {"error": "Wrong or missing access code."})
        return False

    def do_GET(self):
        url = urlsplit(self.path)
        if url.path in ("/", "/index.html"):
            body = (HERE / "index.html").read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-cache")
            self.end_headers()
            self.wfile.write(body)
            return
        if not self._authorized():
            return
        if url.path == "/status":
            self._json(200, {"model": MODEL, "effort": EFFORT, "key_configured": have_key(),
                             "key_status": KEY_STATUS})
        elif url.path == "/events":
            self._events()
        elif url.path == "/profile":
            with SESSION.lock:
                self._json(200, dict(SESSION.profile))
        elif url.path == "/stats":
            self._json(200, METRICS.stats(SESSION.stats_focus()))
        elif url.path == "/interviews":
            self._json(200, {"list": SESSION.list_meta(), "active": SESSION.active})
        elif url.path.startswith("/interviews/"):
            parts = url.path.split("/")  # ['', 'interviews', id] or [..., id, 'export']
            iv = SESSION.get(parts[2]) if len(parts) >= 3 else None
            if not iv:
                self._json(404, {"error": "That interview doesn't exist any more."})
            elif len(parts) == 4 and parts[3] == "export":
                self._download(interview_markdown(iv), iv["name"])
            elif len(parts) == 5 and parts[3] == "recordings":
                rec = next((r for r in iv.get("recordings", []) if r["id"] == parts[4]), None)
                path = SESSION.recording_path(iv["id"], parts[4])
                if not rec or not path or not path.is_file():
                    self._json(404, {"error": "Recording not found."})
                else:
                    stamp = time.strftime("%Y-%m-%d %H%M", time.localtime(rec["started"]))
                    self._send_file(path, rec.get("mime", "video/webm").split(";")[0],
                                    f"{iv['name']} {stamp}.webm" if "download" in url.query else None)
            else:
                self._json(200, iv)
        elif url.path == "/bank":
            q = parse_qs(url.query)
            arg = lambda k, d="": (q.get(k) or [d])[0]
            self._json(200, BANK.search(arg("q"), arg("cat"), arg("src"), arg("star") == "1", arg("iv"),
                                        int(arg("offset", "0") or 0), min(int(arg("limit", "50") or 50), 200)))
        elif url.path == "/bank/export":
            q = parse_qs(url.query)
            arg = lambda k, d="": (q.get(k) or [d])[0]
            res = BANK.search(arg("q"), arg("cat"), arg("src"), arg("star") == "1", arg("iv"), 0, 100000)
            self._download(BANK.markdown(res["results"]), "Interview question bank")
        elif url.path == "/refs":
            self._json(200, LIBRARY.status())
        elif url.path == "/resumes":
            self._json(200, {"folder": str(RESUME_DIR), "files": list_resumes()})
        elif url.path == "/resume":
            name = unquote((parse_qs(url.query).get("name") or [""])[0])
            if name not in list_resumes():  # only files from the listing, never arbitrary paths
                self._json(404, {"error": "Resume not found."})
                return
            try:
                text = extract_resume_text(name, (RESUME_DIR / name).read_bytes())
            except Exception as e:
                self._json(400, {"error": f"Couldn't read {name}: {e}"})
                return
            self._json(200, {"text": text})
        else:
            self._json(404, {"error": "Not found"})

    def _events(self):
        """Live feed (Server-Sent Events): every device gets each question and answer as it's written."""
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream; charset=utf-8")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Transfer-Encoding", "chunked")
        self.end_headers()
        q = queue.Queue()
        with SESSION.lock:
            SESSION.subscribers.add(q)
            first = SESSION.snapshot()
        try:
            self._chunk("retry: 2000\n\n")
            self._chunk("data: " + json.dumps(first) + "\n\n")
            while True:
                try:
                    event = q.get(timeout=15)
                    self._chunk("data: " + json.dumps(event) + "\n\n")
                except queue.Empty:
                    self._chunk(": ping\n\n")  # keeps phone/tunnel connections open
        except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError, OSError):
            pass
        finally:
            with SESSION.lock:
                SESSION.subscribers.discard(q)
            self.close_connection = True

    def do_POST(self):
        path = urlsplit(self.path).path
        if path not in ("/answer", "/stories", "/extract", "/profile", "/settings", "/refs/reindex", "/interviews") \
                and not path.startswith("/interviews/") and path != "/bank" and not path.startswith("/bank/"):
            self._json(404, {"error": "Not found"})
            return
        if not self._authorized():
            return
        length = int(self.headers.get("Content-Length", "0") or 0)
        if length > MAX_UPLOAD:
            self.close_connection = True
            self._json(413, {"error": "That file is too big (5 MB max)."})
            return
        raw = self.rfile.read(length)

        parts = path.split("/")
        if len(parts) == 6 and parts[1] == "interviews" and parts[3] == "recordings" and parts[5] == "chunk":
            if SESSION.add_chunk(parts[2], parts[4], raw):
                self._json(200, {"ok": True})
            else:
                self._json(409, {"error": "This recording has already finished."})
            return

        if path == "/extract":
            try:
                text = extract_resume_text(self.headers.get("X-Filename", ""), raw)
            except ValueError as e:
                self._json(400, {"error": str(e)})
                return
            except Exception:
                self._json(400, {"error": "Couldn't read that file. Try saving it as .docx or .pdf again."})
                return
            self._json(200, {"text": text})
            return

        try:
            data = json.loads(raw or b"{}")
        except (ValueError, json.JSONDecodeError):
            self._json(400, {"error": "Request body must be JSON."})
            return
        origin = str(data.get("origin", ""))

        if path == "/profile":
            SESSION.save_profile({k: data[k] for k in PROFILE_FIELDS if k in data}, origin)
            self._json(200, {"ok": True})
            return
        if path == "/interviews":
            self._json(200, {"id": SESSION.create(str(data.get("name", "")))})
            return
        if path.startswith("/interviews/") and "/items/" in path:
            parts = path.split("/")  # ['', 'interviews', iid, 'items', item, 'mine']
            if len(parts) == 6 and parts[5] == "mine":
                mine = SESSION.save_mine(parts[2], parts[4], str(data.get("text", "")),
                                         data.get("seconds"), data.get("pauses"))
                self._json(200, {"mine": mine}) if mine is not None else self._json(404, {"error": "Question not found."})
            else:
                self._json(404, {"error": "Not found"})
            return
        if path.startswith("/interviews/") and path.endswith("/analyze"):
            if not have_key():
                self._json(500, {"error": "No API key set. Set ANTHROPIC_API_KEY and restart the server."})
            elif SESSION.analyze(path.split("/")[2]):
                self._json(202, {"ok": True})
            else:
                self._json(409, {"error": "This interview is already being analysed, or doesn't exist."})
            return
        if path.startswith("/interviews/") and "/recordings" in path:
            parts = path.split("/")  # ['', 'interviews', iid, 'recordings'(, rid, action)]
            iid = parts[2]
            if len(parts) == 4:
                rid = SESSION.start_recording(iid, str(data.get("mime", "")))
                self._json(200, {"id": rid}) if rid else self._json(404, {"error": "That interview doesn't exist any more."})
                return
            if len(parts) == 6 and parts[5] in ("finish", "delete"):
                ok = (SESSION.finish_recording if parts[5] == "finish" else SESSION.delete_recording)(iid, parts[4])
                self._json(200, {"ok": True}) if ok else self._json(404, {"error": "Recording not found."})
                return
            self._json(404, {"error": "Not found"})
            return
        if path.startswith("/interviews/"):
            parts = path.split("/")
            if len(parts) != 4:
                self._json(404, {"error": "Not found"})
                return
            iid, action = parts[2], parts[3]
            actions = {"start": lambda: SESSION.start(iid), "stop": lambda: SESSION.stop(iid),
                       "rename": lambda: SESSION.rename(iid, str(data.get("name", ""))),
                       "delete": lambda: SESSION.delete(iid)}
            if action not in actions:
                self._json(404, {"error": "Not found"})
            elif actions[action]():
                self._json(200, {"ok": True})
            else:
                self._json(404, {"error": "That interview doesn't exist any more."})
            return
        if path == "/bank":
            eid = BANK.add_mine(str(data.get("question", "")), str(data.get("answer", "")), data.get("category"))
            if eid:
                SESSION.broadcast({"type": "bank"})
                self._json(200, {"id": eid})
            else:
                self._json(400, {"error": "Type a question first."})
            return
        if path.startswith("/bank/"):
            parts = path.split("/")  # ['', 'bank', id, action]
            if len(parts) == 4 and parts[3] in ("update", "delete"):
                ok = BANK.update(parts[2], data) if parts[3] == "update" else BANK.delete(parts[2])
                if ok:
                    SESSION.broadcast({"type": "bank"})
                    self._json(200, {"ok": True, "entry": BANK.get(parts[2])})
                else:
                    self._json(404, {"error": "That question isn't in the bank any more."})
            else:
                self._json(404, {"error": "Not found"})
            return
        if path == "/refs/reindex":
            reindex_library()
            self._json(202, {"ok": True})
            return
        if path == "/settings":
            try:
                if "budget" in data:
                    METRICS.set_budget(data["budget"])
                if "use_refs" in data:
                    METRICS.update_settings(use_refs=bool(data["use_refs"]))
                if data.get("docs_mode") in DOCS_MODES:
                    METRICS.update_settings(docs_mode=data["docs_mode"])
                if data.get("chat_watch") in chatwatch.MODES:
                    METRICS.update_settings(chat_watch=data["chat_watch"])
            except (TypeError, ValueError):
                self._json(400, {"error": "Budget must be a number, e.g. 10"})
                return
            SESSION.broadcast_stats()
            self._json(200, {"ok": True})
            return

        if not have_key():
            self._json(500, {"error": "No API key set. Set ANTHROPIC_API_KEY and restart the server."})
            return

        if path == "/answer":
            question = str(data.get("question", "")).strip()
            if not question:
                self._json(400, {"error": "No question was sent."})
                return
            iid = str(data.get("interview", "")) or SESSION.active or SESSION.create()
            item_id = SESSION.ask(question, origin, iid)
            if item_id is None:
                self._json(404, {"error": "That interview doesn't exist any more. Pick another tab."})
                return
            self._json(202, {"id": item_id, "interview": iid})  # the answer arrives on /events
            return

        # /stories: streamed back to the device that asked
        if not str(data.get("profile", "")).strip():
            self._json(400, {"error": "Add your resume first."})
            return
        system, messages = story_request(data)
        self.send_response(200)
        # event-stream type stops tunnels/proxies from buffering; the page reads it as plain text
        self.send_header("Content-Type", "text/event-stream; charset=utf-8")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Transfer-Encoding", "chunked")
        self.end_headers()
        stopped = threading.Event()

        def send(text):
            try:
                self._chunk(text)
            except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError):
                stopped.set()  # the page pressed Stop

        rec = stream_claude(system, messages, STORY_EFFORT, 16000, send, stopped.is_set,
                            kind="stories", label="Story bank")
        if rec:
            SESSION.broadcast_stats()
        if not stopped.is_set():
            try:
                self.wfile.write(b"0\r\n\r\n")
            except OSError:
                pass

    def _chunk(self, text):
        b = text.encode("utf-8")
        if b:
            self.wfile.write(f"{len(b):X}\r\n".encode() + b + b"\r\n")
            self.wfile.flush()

    def _send_file(self, path, mime, download_name=None):
        size = path.stat().st_size
        start, end = 0, size - 1
        rng = self.headers.get("Range", "")
        m = re.match(r"bytes=(\d*)-(\d*)", rng)
        if m and size:
            if m.group(1):
                start = int(m.group(1))
                end = int(m.group(2)) if m.group(2) else end
            elif m.group(2):  # last N bytes
                start = max(0, size - int(m.group(2)))
            end = min(end, size - 1)
            if start > end:
                self.send_response(416)
                self.send_header("Content-Range", f"bytes */{size}")
                self.send_header("Content-Length", "0")
                self.end_headers()
                return
            self.send_response(206)
            self.send_header("Content-Range", f"bytes {start}-{end}/{size}")
        else:
            self.send_response(200)
        self.send_header("Content-Type", mime)
        self.send_header("Accept-Ranges", "bytes")
        self.send_header("Content-Length", str(end - start + 1 if size else 0))
        if download_name:
            safe = "".join(ch if ch.isalnum() or ch in " -_." else "_" for ch in download_name)
            self.send_header("Content-Disposition", f'attachment; filename="{safe}"')
        self.end_headers()
        if not size:
            return
        try:
            with path.open("rb") as f:
                f.seek(start)
                left = end - start + 1
                while left > 0:
                    block = f.read(min(1024 * 1024, left))
                    if not block:
                        break
                    self.wfile.write(block)
                    left -= len(block)
        except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError):
            pass  # the player stopped reading (seek or close)

    def _download(self, text, name):
        safe = "".join(ch if ch.isalnum() or ch in " -_" else "_" for ch in name).strip() or "interview"
        body = text.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/markdown; charset=utf-8")
        self.send_header("Content-Disposition", f'attachment; filename="{safe}.md"')
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _json(self, code, obj):
        body = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    key, cleaned = clean_api_key()
    if cleaned:
        print("Note: removed extra spaces/quotes from the pasted API key.")
    print("Checking your API key...")
    KEY_STATUS = check_api_key()
    if KEY_STATUS == "ok":
        print("API key works.")
    elif KEY_STATUS == "missing":
        print("Warning: ANTHROPIC_API_KEY is not set - answers will fail until you set it.")
    elif KEY_STATUS == "rejected":
        looks = "starts with sk-ant-" if key.startswith("sk-ant-") else "does NOT start with sk-ant- (likely the wrong text was pasted)"
        print("=" * 64)
        print("PROBLEM: Claude rejected this API key.")
        print(f"  The key you entered is {len(key)} characters long and {looks}.")
        print("  Real keys start with sk-ant- and are usually 100+ characters.")
        print("  Fix: create a new key at console.anthropic.com > Settings > API Keys,")
        print("  copy the whole key, close this window and start again.")
        print("=" * 64)
    else:
        print("Couldn't check the API key right now (no internet?). Answers will try anyway.")
    if HOST != "127.0.0.1" and not ACCESS_CODE:
        print("Warning: the server is reachable from other devices but ACCESS_CODE is not set.")
    print(f"Interview Copilot running at http://localhost:{PORT}  (model: {MODEL}, effort: {EFFORT})")
    if ACCESS_CODE:
        print(f"Access code: {ACCESS_CODE}")
    backfill_bank()
    if chatwatch.ClipboardWatcher.available():
        chatwatch.ClipboardWatcher(SESSION.from_chat).start()
        print("Chat questions: copy an interviewer's question (Ctrl+C) during a live interview to answer it.")
    print(f"Indexing reference notes in {REFERENCE_DIR} ...")
    reindex_library()
    ThreadingHTTPServer((HOST, PORT), Handler).serve_forever()
