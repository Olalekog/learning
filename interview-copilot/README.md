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
- The phone and laptop stay in sync: a question asked on either one shows up, with its answer, on
  every device that has the page open ("● Synced" at the top). History, resume, job and story bank
  are shared too (saved in `data/profile.json` on your PC). **New interview** clears history everywhere.
- The access code is created once and kept in `access-code.txt`. Delete that file to get a new code.
- The link changes each time you run `start-mobile.bat`. Your PC must stay on and awake.
- Phones only allow the microphone on `https://` pages, which is why the tunnel is used.
  Without it (same Wi-Fi, `HOST=0.0.0.0`), tap the keyboard's mic and dictate into "Type a question".
- iPhone listening is less reliable than Android; tap **Answer now** if auto-answer doesn't fire.
- In a real interview: keep the call on your laptop and put the phone near the laptop speaker.

## Before the interview: resume and STAR stories

In the **Your resume & stories** panel:

1. **Resume:** pick a file from your `Resume` folder (the folder next to this app) and press **Load**,
   or **Upload file** (.docx, .pdf, .txt). Choose the tailored version for the job (e.g. `_SA`, `_FinOps`).
2. **Job you're interviewing for:** paste the title, company and key parts of the job description.
3. **Build story bank from resume:** Claude writes 8-12 STAR stories from your real experience,
   tagged by theme (leadership, conflict, failure, deadlines...) and lists themes your resume has no story for.
   Read it once and replace every `[fill in: ...]` with your real details. Rebuild after changing resume.

During the interview, behavioral and leadership questions ("Tell me about a time...", "How do you lead...")
are answered with one of these stories as **Story / Situation / Task / Action / Result / Lesson**,
using only companies, projects and numbers from your resume. Other questions get a short direct answer.

Use another folder of resumes with `RESUME_DIR=C:\path\to\folder`.

## Using it

- Load your resume and build your story bank first (see above).
- Press **Start listening**. When the interviewer pauses (1.8 s by default), the answer appears.
- Press **Answer now** (or **Space** on a PC) to answer immediately, or type a question.
- On a video call, the mic must hear the interviewer: use speakers, not headphones.

## Usage and cost

The **Usage** panel shows, for this interview, today, this month or all time:

- **Cost (estimated)** and average cost per answer, from Anthropic's published prices.
- **Tokens used** (input and output), number of answers and story banks built.
- **Speed:** average time to the first words and to the full answer.
- **Monthly budget:** set a limit and see how much is left (the bar turns amber at 80%, red when over).
- **API rate limit left:** tokens and requests per minute Anthropic still allows, read from the latest answer.
- **Cache:** how much of your resume/story bank was reused and the money it saved.
- **Last 20 calls:** a bar chart of tokens per call (hover a bar for details).

Each answer also shows its own line, e.g. `3,720 in (3,400 from cache) · 240 out · first words 0.6 s · ≈$0.0068`.

Your exact credit balance isn't available to the app (the API doesn't expose it); check it at
console.anthropic.com → Settings → Billing. Usage is saved in `data/usage.jsonl` on your PC.

## Settings (environment variables)

- `COPILOT_MODEL` (default `claude-opus-5-5`). For faster, cheaper answers try `claude-sonnet-5-5` or `claude-haiku-5-5`.
- `COPILOT_EFFORT` (default `low`, fastest). `medium` or `high` gives more careful answers but slower.
- `COPILOT_STORY_EFFORT` (default `medium`) for building the story bank.
- `RESUME_DIR` (default: the `Resume` folder next to this app).
- `COPILOT_BUDGET_USD`: starting monthly budget (you can also set it in the Usage panel).
- `ACCESS_CODE`: when set, the page asks for this code. `start-mobile.bat` sets it for you.
- `HOST` (default `127.0.0.1`, this PC only). `0.0.0.0` makes it reachable on your Wi-Fi; always set `ACCESS_CODE` too.
- `PORT` (default `8765`).
