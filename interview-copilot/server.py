"""Interview Copilot - local server.

Serves the web page and streams Claude's suggested answers.
Your API key stays here on the server and never reaches the browser.

Run:  python server.py     then open http://localhost:8765

For phone access, set ACCESS_CODE so only people with the code can use your API
credit (start-mobile.bat does this for you).
"""

import hmac
import json
import os
import sys
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import anthropic

PORT = int(os.environ.get("PORT", "8765"))
HOST = os.environ.get("HOST", "127.0.0.1")  # 0.0.0.0 = reachable from other devices on your Wi-Fi
ACCESS_CODE = os.environ.get("ACCESS_CODE", "").strip()
MODEL = os.environ.get("COPILOT_MODEL", "claude-opus-5-5")
EFFORT = os.environ.get("COPILOT_EFFORT", "low")  # low = fastest answers
HERE = Path(__file__).parent

SYSTEM_PROMPT = """You help a job candidate during a live interview. You receive a \
speech-to-text transcript of what the interviewer just said, plus the candidate's \
background. Latency-sensitive; begin your visible answer immediately.

Write a suggested answer the candidate can say out loud:
- First person, natural spoken English, confident and honest.
- Start with a one-sentence direct answer, then 2-4 short bullet points of supporting detail.
- Behavioral questions ("tell me about a time..."): use STAR (Situation, Task, Action, Result) \
and draw on the candidate's background when it fits. Never invent employers, titles or numbers \
that contradict the background; if you need an example the background doesn't cover, mark it \
[adapt this].
- Technical questions: give the correct answer clearly; include a tiny code snippet only if it helps.
- Keep it under about 150 words unless the question truly needs more.
- The transcript may contain recognition errors; infer the intended question.
- If the speech is not a question (small talk, instructions), reply with one short line \
suggesting how to respond.
Use simple Markdown (bold, bullets, `code`). No preamble like "Here's an answer"."""

client = None


def get_client():
    global client
    if client is None:
        client = anthropic.Anthropic()
    return client


def build_messages(question, profile, history):
    context = []
    if profile.strip():
        context.append(f"<candidate_background>\n{profile.strip()}\n</candidate_background>")
    if history:
        lines = [f"Q: {h.get('q', '')}\nA: {h.get('a', '')}" for h in history[-4:]]
        context.append("<earlier_in_this_interview>\n" + "\n\n".join(lines) + "\n</earlier_in_this_interview>")
    context.append(f"<interviewer_said>\n{question.strip()}\n</interviewer_said>")
    return [{"role": "user", "content": "\n\n".join(context)}]


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"  # needed for chunked streaming

    def log_message(self, fmt, *args):
        sys.stderr.write("[server] " + (fmt % args) + "\n")

    def _authorized(self):
        """True when no access code is configured, or the request carries the right one."""
        if not ACCESS_CODE:
            return True
        sent = self.headers.get("X-Access-Code", "").strip()
        if hmac.compare_digest(sent.encode(), ACCESS_CODE.encode()):
            return True
        time.sleep(1)  # slows down anyone guessing codes
        self.close_connection = True  # any unread request body is discarded with the connection
        self._json(401, {"error": "Wrong or missing access code."})
        return False

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            body = (HERE / "index.html").read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        elif self.path == "/status":
            if not self._authorized():
                return
            ok =bool(os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("ANTHROPIC_AUTH_TOKEN"))
            self._json(200, {"model": MODEL, "effort": EFFORT, "key_configured": ok})
        else:
            self._json(404, {"error": "Not found"})

    def do_POST(self):
        if self.path != "/answer":
            self._json(404, {"error": "Not found"})
            return
        if not self._authorized():
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            data = json.loads(self.rfile.read(length) or b"{}")
        except (ValueError, json.JSONDecodeError):
            self._json(400, {"error": "Request body must be JSON."})
            return

        question = str(data.get("question", ""))
        if not question.strip():
            self._json(400, {"error": "No question was sent."})
            return
        if not (os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("ANTHROPIC_AUTH_TOKEN")):
            self._json(500, {"error": "No API key set. Set ANTHROPIC_API_KEY and restart the server."})
            return

        # Stream plain text back to the page as Claude writes it.
        self.send_response(200)
        # event-stream type stops tunnels/proxies from buffering; the page reads it as plain text
        self.send_header("Content-Type", "text/event-stream; charset=utf-8")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Transfer-Encoding", "chunked")
        self.end_headers()

        try:
            with get_client().beta.messages.stream(
                model=MODEL,
                max_tokens=4000,
                system=SYSTEM_PROMPT,
                output_config={"effort": EFFORT},
                betas=["server-side-fallback-2026-07-01"],
                fallbacks="default",
                messages=build_messages(question, str(data.get("profile", "")), data.get("history") or []),
            ) as stream:
                for text in stream.text_stream:
                    self._chunk(text)
                final = stream.get_final_message()
                if final.stop_reason == "refusal":
                    self._chunk("\n\n_(Claude declined to answer this one.)_")
        except anthropic.AuthenticationError:
            self._chunk("**Error:** your API key was rejected. Check ANTHROPIC_API_KEY and restart the server.")
        except anthropic.RateLimitError:
            self._chunk("**Error:** rate limited by the API. Wait a few seconds and try again.")
        except anthropic.APIStatusError as e:
            self._chunk(f"**Error from the API ({e.status_code}):** {e.message}")
        except anthropic.APIConnectionError:
            self._chunk("**Error:** could not reach the Claude API. Check your internet connection.")
        except (BrokenPipeError, ConnectionResetError):
            return  # the page cancelled this answer
        except Exception as e:  # e.g. no API key configured
            self._chunk(f"**Error:** {e}")
        try:
            self.wfile.write(b"0\r\n\r\n")
        except (BrokenPipeError, ConnectionResetError):
            pass

    def _chunk(self, text):
        b = text.encode("utf-8")
        if b:
            self.wfile.write(f"{len(b):X}\r\n".encode() + b + b"\r\n")
            self.wfile.flush()

    def _json(self, code, obj):
        body = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    if not (os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("ANTHROPIC_AUTH_TOKEN")):
        print("Warning: ANTHROPIC_API_KEY is not set - answers will fail until you set it.")
    if HOST != "127.0.0.1" and not ACCESS_CODE:
        print("Warning: the server is reachable from other devices but ACCESS_CODE is not set.")
    print(f"Interview Copilot running at http://localhost:{PORT}  (model: {MODEL}, effort: {EFFORT})")
    if ACCESS_CODE:
        print(f"Access code: {ACCESS_CODE}")
    ThreadingHTTPServer((HOST, PORT), Handler).serve_forever()
