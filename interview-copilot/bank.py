"""Question bank: every interview question in one searchable place.

Three kinds of entries:
- "asked": questions asked in your interviews (added automatically, repeats merged and counted)
- "notes": prepared Q&A found in your study notes (rebuilt whenever the notes are re-indexed)
- "mine":  questions you add yourself
Your edits, stars and deletions are saved in data/bank.json.
"""

import hashlib
import json
import math
import re
import threading
import time
import uuid
from collections import Counter, defaultdict

import refs

QUESTION_START = re.compile(
    r"^(what|what's|whats|how|why|when|where|which|who|describe|explain|tell|give|walk|compare|contrast|"
    r"can|could|do|does|did|is|are|have|has|would|should|will|define|list|name|discuss|share|talk|"
    r"imagine|suppose|if you|in your|as a|outline|differentiate|summarize|provide)\b", re.I)
NUMBERING = re.compile(r"^\s*(?:q(?:uestion)?\s*\d+\s*[.:)\-]?|\d+\s*[.:)\-]|[a-z]\d+\s*[.:)\-]?)\s*", re.I)

# (category, pattern) in priority order; an entry gets every matching tag, the first is its category
CATEGORIES = [
    ("Behavioral", r"tell me about (a|yourself)|describe a (time|situation)|give (me )?an example|a time (when|you)|"
                   r"(?<!merge )conflicts?\b(?! (between|in) (versions|dependencies|files))|disagree|mistake|failure|failed|weakness|strength|feedback|under pressure|tight deadline|"
                   r"difficult|proud|why (do you want|are you interested|should we hire|this (role|company))|"
                   r"introduce yourself|yourself|motivat|co-?workers?|teammates?|work style|prefer to communicate"),
    ("Leadership", r"\blead(er|ership|ing)?\b|mentor|coach|influenc|delegat|ownership|direct reports?|"
                   r"manage (a |the )?team|build(ing)? a team|vision|stakeholder"),
    ("AI / RAG", r"\brag\b|\bllm|genai|generative|embedding|vector|prompt|bedrock|openai|machine learning|\bml\b"),
    ("Kubernetes", r"kubernetes|\bk8s\b|\bpods?\b|helm|statefulset|daemonset|ingress|kubectl|\beks\b|\baks\b|\bgke\b|argo"),
    ("Terraform / IaC", r"terraform|\biac\b|infrastructure as code|cloudformation|bicep|pulumi|ansible|state (file|lock)"),
    ("CI/CD & DevOps", r"ci/?cd|pipeline|jenkins|github actions|gitlab|azure devops|release|rollback|blue.?green|canary|gitops|devops|\bgit\b|merge|branch"),
    ("Security", r"secur|encrypt|\bkms\b|secret|zero trust|complian|vulnerab|devsecops|crypto|\biam\b|least privilege|guardduty|waf"),
    ("Networking", r"network|\bvpc\b|subnet|\bdns\b|route ?53|load balanc|\balb\b|\bnlb\b|cidr|peering|transit gateway|firewall|\bvpn\b|privatelink|endpoint"),
    ("Linux", r"linux|\bbash\b|shell|systemd|kernel|chmod|\bgrep\b|cron|ssh"),
    ("Data & Databases", r"database|\bsql\b|\brds\b|dynamodb|postgres|mysql|aurora|data lake|\bemr\b|spark|kafka|glue|athena|redshift"),
    ("Observability & SRE", r"monitor|observab|logging|cloudwatch|prometheus|grafana|alert|\bsre\b|incident|\bslo\b|on-?call|troubleshoot"),
    ("Architecture", r"design|architect|scal|high(ly)? availab|disaster|multi-?region|microservice|resilien|fault"),
    ("AWS", r"\baws\b|\bec2\b|\bs3\b|lambda|\becs\b|fargate|cloudfront|\bsns\b|\bsqs\b|organizations|control tower|landing zone"),
    ("Azure", r"azure|entra|\barm\b"),
    ("Google Cloud", r"\bgcp\b|google cloud|bigquery|cloud run"),
]
CATEGORY_RES = [(name, re.compile(pat, re.I)) for name, pat in CATEGORIES]
CATEGORY_NAMES = [name for name, _ in CATEGORIES] + ["General"]


def clean_question(text):
    text = re.sub(r"<[^>]+>", "", text or "")
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = text.replace("**", "").strip().strip("#").strip()
    text = NUMBERING.sub("", text).strip()
    text = re.sub(r"^(question|q)\s*[:.\-]\s*", "", text, flags=re.I)  # "Question: How do you..."
    return text.rstrip("…").strip()


def is_question(text):
    q = clean_question(text)
    return 12 <= len(q) <= 300 and (q.endswith("?") or bool(QUESTION_START.match(q)))


def categorize(question, answer=""):
    tags = [name for name, rx in CATEGORY_RES if rx.search(question)]
    if not tags and answer:
        tags = [name for name, rx in CATEGORY_RES if rx.search(answer[:400])][:2]
    return (tags[0] if tags else "General"), tags


def qtokens(text):
    return set(refs.tokenize(clean_question(text)))


def similar(a_tokens, b_tokens):
    return len(a_tokens & b_tokens) / max(len(a_tokens | b_tokens), 1)


def stable_id(*parts):
    return hashlib.sha1("|".join(parts).encode("utf-8")).hexdigest()[:12]


def question_of(chunk):
    """The full question a notes section answers, or None."""
    candidates = []
    if chunk["section"]:
        candidates.append(chunk["section"].split(" › ")[-1])
    for line in chunk["text"].splitlines()[:3]:
        if line.strip():
            candidates.append(line)
    for c in candidates:
        if is_question(c):
            return clean_question(c)
    return None


def answer_of(chunk, question):
    """Section text without its own question line."""
    lines = chunk["text"].splitlines()
    while lines and (not lines[0].strip() or clean_question(lines[0]) == question):
        lines.pop(0)
    return "\n".join(lines).strip()


class Bank:
    def __init__(self, path):
        self.path = path
        self.lock = threading.RLock()
        self.entries = {}     # asked + mine, by id
        self.overrides = {}   # notes id -> {answer, starred, hidden, category}
        self.notes = {}       # notes entries, rebuilt from the library
        self.index = None     # search index, rebuilt when something changes
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            self.entries = data.get("entries", {})
            self.overrides = data.get("overrides", {})
        except (OSError, ValueError):
            pass

    # ------------------------------------------------------------ storage
    def _save(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.path.with_suffix(".tmp")
        tmp.write_text(json.dumps({"entries": self.entries, "overrides": self.overrides},
                                  ensure_ascii=False, indent=1), encoding="utf-8")
        tmp.replace(self.path)
        self.index = None

    # ------------------------------------------------------------ building from notes
    def load_notes(self, library):
        """Collect prepared Q&A from the reference notes (duplicates across .md/.docx copies merged)."""
        with library.lock:
            chunks = list(library.chunks)
        notes, seen = {}, {}
        for c in chunks:
            q = question_of(c)
            if not q:
                continue
            answer = answer_of(c, q)
            if len(answer) < 40:
                continue
            key = " ".join(sorted(qtokens(q)))
            if key in seen:  # same question in another copy: keep the longer answer
                prev = notes[seen[key]]
                if len(answer) > len(prev["answer"]):
                    prev.update(answer=answer, file=c["file"], section=c["section"])
                continue
            nid = stable_id("notes", c["file"], q)
            cat, tags = categorize(q, answer)
            notes[nid] = {"id": nid, "source": "notes", "question": q, "answer": answer, "category": cat,
                          "tags": tags, "file": c["file"], "section": c["section"], "times_asked": 0,
                          "origins": [], "starred": False, "edited": False, "created": 0}
            seen[key] = nid
        with self.lock:
            self.notes = notes
            self.index = None
        return len(notes)

    def _all(self):
        """Every visible entry with your edits applied."""
        out = []
        for e in self.notes.values():
            o = self.overrides.get(e["id"], {})
            if o.get("hidden"):
                continue
            out.append({**e, **{k: v for k, v in o.items() if k != "hidden"}})
        out.extend(self.entries.values())
        return out

    # ------------------------------------------------------------ adding
    def add_asked(self, question, answer, interview_id, interview_name, item_id, ts):
        """Record a question from an interview; a repeat of an earlier question is merged and counted."""
        question = question.strip()
        if not question or not answer.strip():
            return None
        toks = qtokens(question)
        with self.lock:
            for e in self.entries.values():
                if any(o.get("item") == item_id for o in e["origins"]):
                    return e["id"]  # already recorded
            match = None
            for e in self.entries.values():
                if similar(toks, qtokens(e["question"])) >= 0.75:
                    match = e
                    break
            origin = {"interview": interview_id, "name": interview_name, "item": item_id, "ts": ts}
            if match:
                match["origins"].append(origin)
                match["times_asked"] = len(match["origins"])
                match["last_asked"] = max(ts, match.get("last_asked") or 0)
                if not match.get("edited"):
                    match["answer"] = answer  # keep your own edits; otherwise show the latest answer
                eid = match["id"]
            else:
                eid = uuid.uuid4().hex[:12]
                cat, tags = categorize(question, answer)
                self.entries[eid] = {"id": eid, "source": "asked", "question": question, "answer": answer,
                                     "category": cat, "tags": tags, "origins": [origin], "times_asked": 1,
                                     "last_asked": ts, "starred": False, "edited": False, "created": ts}
            self._save()
        return eid

    def add_mine(self, question, answer, category=None):
        question = question.strip()
        if not question:
            return None
        cat, tags = categorize(question, answer)
        if category in CATEGORY_NAMES:
            cat = category
            tags = [category] + [t for t in tags if t != category]
        with self.lock:
            eid = uuid.uuid4().hex[:12]
            now = time.time()
            self.entries[eid] = {"id": eid, "source": "mine", "question": question, "answer": answer.strip(),
                                 "category": cat, "tags": tags, "origins": [], "times_asked": 0,
                                 "last_asked": None, "starred": False, "edited": True, "created": now}
            self._save()
        return eid

    # ------------------------------------------------------------ editing
    def update(self, eid, changes):
        allowed = {k: v for k, v in changes.items() if k in ("answer", "question", "starred", "category")}
        if "category" in allowed and allowed["category"] not in CATEGORY_NAMES:
            allowed.pop("category")
        if "answer" in allowed or "question" in allowed:
            allowed["edited"] = True
        with self.lock:
            if eid in self.entries:
                self.entries[eid].update(allowed)
            elif eid in self.notes:
                self.overrides.setdefault(eid, {}).update(allowed)
            else:
                return False
            self._save()
        return True

    def delete(self, eid):
        with self.lock:
            if eid in self.entries:
                del self.entries[eid]
            elif eid in self.notes:
                self.overrides.setdefault(eid, {})["hidden"] = True  # notes stay untouched on disk
            else:
                return False
            self._save()
        return True

    # ------------------------------------------------------------ search
    def _build_index(self):
        docs = self._all()
        postings, lens = defaultdict(list), []
        for i, e in enumerate(docs):
            origin_words = " ".join(o.get("name", "") for o in e.get("origins", []))
            terms = Counter(refs.tokenize(e["question"]) * 3 + refs.tokenize(e["answer"][:3000]) +
                            refs.tokenize(" ".join(e.get("tags", []))) + refs.tokenize(origin_words) * 2 +
                            refs.tokenize(e.get("file", "").replace("/", " ").replace("_", " ")))
            lens.append(max(sum(terms.values()), 1))
            for t, tf in terms.items():
                postings[t].append((i, tf))
        n = max(len(docs), 1)
        idf = {t: math.log(1 + (n - len(p) + 0.5) / (len(p) + 0.5)) for t, p in postings.items()}
        self.index = {"docs": docs, "postings": postings, "idf": idf, "lens": lens,
                      "avg": sum(lens) / n if lens else 1}

    def _scores(self, query):
        if self.index is None:
            self._build_index()
        ix = self.index
        q = refs.tokenize(query)
        weights = {t: 2.0 for t in q}
        for t in q:
            for syn in refs.SYNONYMS.get(t, []):
                weights.setdefault(syn, 0.6)
        scores = defaultdict(float)
        for t, w in weights.items():
            for i, tf in ix["postings"].get(t, ()):
                L = ix["lens"][i]
                scores[i] += w * ix["idf"][t] * tf * 2.4 / (tf + 1.4 * (0.25 + 0.75 * L / ix["avg"]))
        return scores

    def search(self, query="", category="", source="", starred=False, interview="", offset=0, limit=50):
        with self.lock:
            if self.index is None:
                self._build_index()
            docs = self.index["docs"]
            if query.strip():
                scores = self._scores(query)
                top = max(scores.values(), default=0)
                order = [i for i, sc in sorted(scores.items(), key=lambda x: -x[1]) if sc >= top * 0.3]
            else:
                rank = {"asked": 0, "mine": 1, "notes": 2}
                order = sorted(range(len(docs)), key=lambda i: (
                    not docs[i].get("starred"), rank.get(docs[i]["source"], 3),
                    -(docs[i].get("last_asked") or docs[i].get("created") or 0), docs[i]["question"].lower()))

            def keep(e):
                return ((not category or e["category"] == category or category in e.get("tags", [])) and
                        (not source or e["source"] == source) and (not starred or e.get("starred")) and
                        (not interview or any(o.get("interview") == interview for o in e.get("origins", []))))

            matched = [docs[i] for i in order if keep(docs[i])]
            cats, srcs, ivs = Counter(), Counter(), {}
            for e in docs:
                cats[e["category"]] += 1
                srcs[e["source"]] += 1
                for o in e.get("origins", []):
                    ivs[o.get("interview")] = o.get("name") or "Interview"
            return {"total": len(matched), "results": matched[offset:offset + limit],
                    "categories": {c: cats.get(c, 0) for c in CATEGORY_NAMES if cats.get(c)},
                    "sources": dict(srcs), "interviews": [{"id": k, "name": v} for k, v in ivs.items()],
                    "all": len(docs)}

    def best_saved_answer(self, question):
        """Your own polished answer to (nearly) this question: an edited, starred or self-added entry."""
        toks = qtokens(question)
        if len(toks) < 2:
            return None
        with self.lock:
            best, best_sim = None, 0.0
            for e in self._all():
                if not (e.get("edited") or e.get("starred") or e["source"] == "mine") or not e["answer"].strip():
                    continue
                sim = similar(toks, qtokens(e["question"]))
                if sim > best_sim:
                    best, best_sim = e, sim
            return best if best_sim >= 0.6 else None

    def get(self, eid):
        with self.lock:
            return next((e for e in self._all() if e["id"] == eid), None)

    def markdown(self, results):
        lines = ["# Interview question bank", "", f"_{len(results)} questions · exported "
                 f"{time.strftime('%d %b %Y %H:%M')}_", ""]
        by_cat = defaultdict(list)
        for e in results:
            by_cat[e["category"]].append(e)
        for cat in CATEGORY_NAMES:
            if not by_cat.get(cat):
                continue
            lines += [f"## {cat}", ""]
            for e in by_cat[cat]:
                star = "★ " if e.get("starred") else ""
                lines += [f"### {star}{e['question']}", ""]
                if e["source"] == "asked":
                    names = ", ".join(sorted({o.get("name", "") for o in e["origins"]}))
                    lines += [f"_Asked {e['times_asked']}× · {names}_", ""]
                elif e["source"] == "notes":
                    lines += [f"_From notes: `{e.get('file', '')}`_", ""]
                lines += [e["answer"].strip(), ""]
        return "\n".join(lines)
