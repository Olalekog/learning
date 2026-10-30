"""Answer questions copied from a chat (Teams, Zoom, Slack...) with Ctrl+C.

The server watches the Windows clipboard. When new text is copied, it removes the chat's
name/time lines, checks that it looks like an interview question and hands it over to be answered.
Text that looks like a password, link, file path, code or a long document is ignored.
"""

import ctypes
import re
import sys
import threading
import time

from bank import QUESTION_START

MODES = ("questions", "any", "off")

TIME = r"\d{1,2}[:.]\d{2}(?::\d{2})?\s?(?:[ap]\.?m\.?)?"
TIME_RE = re.compile(TIME, re.I)
# lines a chat app adds around a message when it's copied
META_LINE = re.compile(
    r"^(?:edited|like|reply|seen( by.*)?|today|yesterday|new messages?|\d+ (?:replies|reactions?)|"
    r"(?:mon|tues|wednes|thurs|fri|satur|sun)day|has context menu)$", re.I)
TEAMS_PREFIX = re.compile(r"^\[" + TIME + r"[^\]]*\]\s*", re.I)                    # [10:32 AM] Jane Doe
ZOOM_PREFIX = re.compile(r"^(?:" + TIME + r"\s+)?from\s+.{1,60}?\s+to\s+.{1,40}?\s?:\s*", re.I)
SMALL_TALK = re.compile(
    r"\b(can|could) you (hear|see) (me|us|my screen)|\b(are|r) you (there|still there|able to hear)|"
    r"\bmy (audio|mic|video|camera)\b|\b(give|bear with) (me|us) a (sec|second|minute|moment)|"
    r"\b(join|joining|dial) (the|this) (call|meeting|link)|\bhow are you( doing)?( today)?\?*$", re.I)
EXTRA_START = re.compile(r"^(let's|lets|design|build|write|implement|assume|consider|say|next question)\b", re.I)


def looks_like_name(line):
    words = line.split()
    return 1 <= len(words) <= 5 and "?" not in line and all(w[:1].isupper() or w.startswith("(") for w in words)


def clean_chat_text(text):
    """Strip the sender/time lines a chat app adds and return the message on one line."""
    lines = []
    for raw in (text or "").replace("\r", "").split("\n"):
        line = ZOOM_PREFIX.sub("", TEAMS_PREFIX.sub("", raw.strip())).strip()
        if not line or META_LINE.match(line) or TIME_RE.fullmatch(line):
            continue
        has_time = TIME_RE.search(line)
        if has_time and len(line) < 60 and "?" not in line:
            rest = TIME_RE.sub("", line).strip(" ,-|·")
            if not rest or looks_like_name(rest):
                continue  # "Jane Doe 10:32 AM"
        lines.append(line)
    if len(lines) > 1 and looks_like_name(lines[0]) and not QUESTION_START.match(lines[0]):
        lines = lines[1:]  # sender name on its own line
    return re.sub(r"\s+", " ", " ".join(lines)).strip()


def check(text, mode="questions"):
    """Return (question, None) to answer it, or (None, reason) to ignore it."""
    raw = (text or "").strip()
    if not raw:
        return None, "empty"
    if len(raw) > 1500:
        return None, "too long to be a chat question"
    q = clean_chat_text(raw)
    if len(q) < 10 or len(q.split()) < 3:
        return None, "too short"
    if re.fullmatch(r"\S+", q) or re.match(r"^(https?://|www\.)\S+$", q, re.I):
        return None, "looks like a link or password"
    if re.match(r"^([a-z]:\\|\\\\|/)\S*$", q, re.I) or re.fullmatch(r"\S+@\S+\.\S+", q):
        return None, "looks like a path or email"
    if sum(q.count(c) for c in "{};=<>$") > max(4, len(q) // 25):
        return None, "looks like code"
    if SMALL_TALK.search(q) and len(q.split()) < 12:
        return None, "small talk"
    if mode == "questions":
        sentences = re.split(r"(?<=[.!?:])\s+", q)
        if "?" not in q and not any(QUESTION_START.match(s) or EXTRA_START.match(s) for s in sentences):
            return None, "doesn't look like a question"
    return q[:600], None


class ClipboardWatcher(threading.Thread):
    """Calls on_text(text) whenever new text is copied on this Windows PC."""

    def __init__(self, on_text, interval=0.35):
        super().__init__(daemon=True)
        self.on_text, self.interval = on_text, interval

    @staticmethod
    def available():
        return sys.platform == "win32"

    def run(self):
        user32, kernel32 = ctypes.windll.user32, ctypes.windll.kernel32
        user32.GetClipboardSequenceNumber.restype = ctypes.c_uint32
        user32.OpenClipboard.argtypes = [ctypes.c_void_p]
        user32.GetClipboardData.argtypes = [ctypes.c_uint]
        user32.GetClipboardData.restype = ctypes.c_void_p
        kernel32.GlobalLock.argtypes = [ctypes.c_void_p]
        kernel32.GlobalLock.restype = ctypes.c_void_p
        kernel32.GlobalUnlock.argtypes = [ctypes.c_void_p]
        CF_UNICODETEXT = 13

        def read():
            for _ in range(5):  # another app may be holding the clipboard for a moment
                if user32.OpenClipboard(None):
                    break
                time.sleep(0.05)
            else:
                return None
            try:
                if not user32.IsClipboardFormatAvailable(CF_UNICODETEXT):
                    return None
                handle = user32.GetClipboardData(CF_UNICODETEXT)
                if not handle:
                    return None
                ptr = kernel32.GlobalLock(handle)
                if not ptr:
                    return None
                try:
                    return ctypes.wstring_at(ptr)
                finally:
                    kernel32.GlobalUnlock(handle)
            finally:
                user32.CloseClipboard()

        last = user32.GetClipboardSequenceNumber()  # ignore whatever was copied before the server started
        while True:
            time.sleep(self.interval)
            seq = user32.GetClipboardSequenceNumber()
            if seq == last:
                continue
            last = seq
            try:
                text = read()
                if text:
                    self.on_text(text)
            except Exception as exc:  # never let one bad copy stop the watcher
                print("Chat copy watcher:", exc)
