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

## Interview sessions

At the top of the Interview page, the **Interview** dropdown lists every saved interview with its
state ("● Live", "Not started", or ended), date and number of questions. Choose one to open it.

- **+ New interview** (next to the dropdown) creates one. Click its name to rename it, e.g.
  "Capital One – Cloud Engineer".
- **Start interview** makes it live and turns on listening on that device. **Stop interview** ends it on
  every device. Only one interview is live at a time: starting another ends the current one.
  An ended interview can be resumed.
- Every question and answer is **saved on your PC** as it happens (`data/interviews/`), with the notes
  and official docs used and its cost, so nothing is lost if the server restarts.
- Choose any past interview in the dropdown to read it. **Export (.md)** downloads it as a Markdown
  document. **Delete** (tap twice) removes it.
- Asking a question in an interview that isn't live starts it. Phone and laptop follow the live
  interview automatically, and the Usage tab's "This interview" is the live one (or the newest).

## Questions typed in the chat (Teams, Zoom, Slack)

When the interviewer types a question in the meeting chat, select their message on the PC running the app and press
**Ctrl+C**. The answer appears right away on the laptop and the phone. You don't need to paste anything or switch windows.

- It only works while an interview is **live** and only on the Windows PC running the server. Copying on your phone
  does nothing.
- The chat app's name and time lines ("Jane Doe 10:32 AM", "From Jane to Everyone:") are removed.
- **Questions in the chat** (Listening panel):
  - **Answer questions I copy** (default): only text that reads like a question ("…?", "Tell me…",
    "Explain…", "Design…").
  - **Answer any text I copy**, e.g. a topic like "Kubernetes ingress vs service mesh".
  - **Off**.
- These copies are ignored: passwords, links, file paths, emails, code, long documents, small talk ("Can you hear
  me?"), the question you just asked, and text copied from an answer or the question bank. The panel says
  why it ignored a copy. The copied text itself is never shown or saved.
- Chat questions are marked "Question (from chat)" and "*Asked in the chat*" in the export.

## Interview analysis (scores 1–10)

Open the **Analysis** tab at the top (or press **Analysis** in an interview), pick the interview and press
**Analyze this interview**. Claude reviews
every question with what you actually said, then gives:

- **Scores from 1 to 10** for each answer and overall: **correctness** (accuracy, completeness),
  **behavioral** (STAR structure, ownership, results with numbers), **composure** (pace, fillers, pauses,
  restarts) and **communication** (clarity, structure, directness). 1–3 poor, 4–5 below the bar,
  6–7 meets it, 8–9 strong, 10 exceptional.
- **Feedback** and a **stronger answer** for every question, built from your resume and story bank.
- **Strengths**, **what to improve**, and **what the interviewer focused on** (themes, difficulty).

To score your answers, the app needs what you said:

- **Capture my answers** (in the Listening panel, on by default): after a suggested answer appears, the
  app records what you say as *your answer* and stops auto-answering. Press **Space** (or **My answer is
  done**) when you finish and it listens for the next question again.
- Or use **Add what I said / Edit** under any question to type or paste your answer, for example from the
  recording.

Composure uses measurements of each captured answer: words per minute, filler words ("um", "you know",
"basically"), pauses over 3 seconds and restarts. Answers you didn't capture get advice but no score.
The analysis is saved with the interview, synced to every device and included in **Export (.md)**.
One analysis costs roughly $0.03–0.10 depending on length.

## Question bank

Press **Question bank** at the top to open your knowledge base of interview questions and answers.
It has three sources:

- **Asked in interviews:** every answered question is added automatically, with the company/interview
  and date. Repeat questions are merged and counted ("Asked 3× · Capital One, United Airlines").
  Questions stay in the bank even if you delete the interview.
- **From my notes:** about 1,200 prepared Q&A found in your notes (answer banks, company guides, AWS,
  Terraform, Kubernetes…). These refresh when you press **Re-index**.
- **Added by me:** press **+ Add question** to write your own.

Search finds questions and answers by keyword, including company names. Filter by category
(Behavioral, Leadership, AWS, Kubernetes, Terraform / IaC, Security, Networking…), source, ★ Starred or
interview. Click a question to see its answer, then **Edit answer**, **Copy**, ★ star it, or
**Delete**. Deleting a notes entry only hides it in the bank; your files aren't touched.
**Export (.md)** saves the current list grouped by category.

**Your polished answers come back live:** when an interview question closely matches one you edited,
starred or added, that answer is given to Claude to follow, and "Question bank" appears in the answer's
sources. Stored in `data/bank.json` (not in git).

## Screen recording

Each interview tab has **● Record screen** (desktop Chrome or Edge; phone browsers can't record the screen).

- When the browser asks what to share, pick the meeting tab or your whole screen and tick
  **Share tab audio** / **Share system audio**, so the interviewer's voice is recorded. Your microphone is
  mixed in automatically. If the shared audio is missing, the app tells you.
- Tick **Record when I start the interview** to start recording with **Start interview**.
  **Stop interview** (or "Stop sharing" in the browser bar) ends the recording.
- The video is sent to your PC every 4 seconds into `data/recordings/` (not in git), so a crash loses
  at most a few seconds. About 7–8 MB per minute (≈ 300–350 MB for 45 minutes).
- Recordings are listed under their interview with **Play**, **Download** (.webm, plays in Chrome, Edge
  or VLC) and **Delete**. Deleting an interview deletes its recordings.

**Get permission first.** Recording a call usually needs everyone's consent (required by law in some
places), and some employers don't allow it. The app reminds you before your first recording.

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

## Technical answers from your own notes

The app indexes your study notes (`.md`, `.pdf`, `.docx`, `.txt`) in the folder it sits in, your
`learning` folder, when the server starts. It skips hidden folders such as `.git` and `.trunk`,
plus `Resume`, `coverage`, `node_modules` and this app.

For every question it finds the best-matching sections in a few milliseconds and sends them with the
question. Technical answers then follow your notes: your service names, numbers, architectures,
commands and prepared answers, with general knowledge filling any gaps. The files used are listed under
each answer ("From your notes").

- **4. Reference notes** in the resume panel shows how many documents are indexed, has a switch to turn
  this off, and a **Re-index** button for after you add or edit notes.
- Short follow-ups ("Why is that better?") reuse the previous question's topic.
- Only the few matching sections are sent, never whole folders.
- Use another folder with `REFERENCE_DIR=C:\path\to\notes`; skip extra folders with
  `REFERENCE_SKIP=Folder1,Folder2`.

## Official documentation (AWS, Azure, Google Cloud, Linux)

Claude can also search official documentation live, limited to these sites (subdomains included):
`aws.amazon.com` (docs.aws.amazon.com), `learn.microsoft.com/en-us/azure`, `azure.microsoft.com`,
`cloud.google.com`, `linux.org`, `kernel.org`, `man7.org` (Linux man pages) and `linuxfoundation.org`.
The pages used are linked under the answer ("From official docs").

Choose how often in **4. Reference notes → Official docs**:

- **Only when my notes don't cover it** (default): answers your notes cover stay fast; others check the docs.
- **Always check:** best for preparation, to confirm exact limits, defaults and recent changes.
- **Off.**

A search adds a few seconds before the answer starts and costs about 1¢ plus the tokens of the pages
read (typically ≈$0.05 per searched answer). At most 2 searches per answer. If web search is turned off
for your Anthropic organization, answers still work without it and say so. An admin can turn it on in
the Anthropic Console. Change the sites with `OFFICIAL_DOCS_DOMAINS=site1.com,site2.com/path`.

## Usage and cost

The **Usage** tab at the top shows, for this interview, today, this month or all time:

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
