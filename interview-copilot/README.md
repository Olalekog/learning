# Interview Copilot

Listens to interview questions through your microphone and shows a suggested answer from Claude as it streams in. Works on your PC and on your phone.

## Run it on your PC (Windows)

1. Get an API key at https://console.anthropic.com (Settings → API Keys).
2. Double-click `start.bat`. It asks for the key, sets up Python the first time and opens the page.
3. Use **Chrome or Edge** and allow the microphone.

Manual start:

```
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
set ANTHROPIC_API_KEY=sk-ant-...
.venv\Scripts\python server.py
```

(The app uses its own `.venv` because an older compression library in some Anaconda installs breaks the Anthropic SDK.)

## Run it on your phone

The server still runs on your PC; your phone opens it through a secure link.

1. Double-click `start-mobile.bat` on your PC. The first time, it installs Cloudflare's free `cloudflared` tool with winget.
2. Wait for a line like `https://something.trycloudflare.com` and open it on your phone
   (Chrome on Android, Safari on iPhone). Tip: open the link on your PC and send it to yourself.
3. Enter the **access code** shown in the window. The phone remembers it.

Notes:
- The access code is created once and kept in `access-code.txt`. Delete that file to get a new code.
- The link changes each time you run `start-mobile.bat`. Your PC must stay on and awake.
- Phones only allow the microphone on `https://` pages, which is why the tunnel is used.
  Without it (same Wi-Fi, `HOST=0.0.0.0`), tap the keyboard's mic and dictate into "Type a question".
- iPhone listening is less reliable than Android; tap **Answer now** if auto-answer doesn't fire.
- In a real interview: keep the call on your laptop and put the phone near the laptop speaker.

## Using it

- Paste your resume summary and the job into **Your background** so answers sound like you.
- Press **Start listening**. When the interviewer pauses (1.8 s by default), the answer appears.
- Press **Answer now** (or **Space** on a PC) to answer immediately, or type a question.
- On a video call, the mic must hear the interviewer: use speakers, not headphones.

## Settings (environment variables)

- `COPILOT_MODEL` (default `claude-opus-5-5`). For faster, cheaper answers try `claude-sonnet-5-5` or `claude-haiku-5-5`.
- `COPILOT_EFFORT` (default `low`, fastest). `medium` or `high` gives more careful answers but slower.
- `ACCESS_CODE`: when set, the page asks for this code. `start-mobile.bat` sets it for you.
- `HOST` (default `127.0.0.1`, this PC only). `0.0.0.0` makes it reachable on your Wi-Fi; always set `ACCESS_CODE` too.
- `PORT` (default `8765`).
