# Migration Checklist — bringing past work into this repo

## A. ChatGPT → repo (export first, delete last)

Deleting a ChatGPT chat is permanent, and a chat can't be exported after it's deleted. Follow the steps in order.

1. ☐ **Export.** ChatGPT → profile icon → **Settings → Data controls → Export data → Confirm export**. A download link is emailed to you. It can take a few minutes up to about 24 hours, and the link expires, so download promptly.
2. ☐ **Keep the original ZIP** somewhere safe outside this repo (for example a private Google Drive folder) as a backup.
3. ☐ **Bring the ZIP into Claude Code.** Upload it to the session or put it in `imports/chatgpt/raw/`. That folder is git-ignored, so the full export never gets committed.
4. ☐ **Run the importer:**
   ```bash
   python3 -I scripts/import_chatgpt_export.py imports/chatgpt/raw/<your-export>.zip
   ```
   Options: `--min-hits 2` (looser filter), `--all` (import everything), `--extra-keywords "gst,trademark,llp"`.
5. ☐ **Review `imports/chatgpt/INDEX.md`** to confirm the right chats were picked up.
6. ☐ **Distil.** Ask Claude: *"Read imports/chatgpt/conversations and move decisions, ad copy, keyword lists and results into the right platform folders and shared/learnings.md."*
7. ☐ **Commit and push** the repo so the work is saved.
8. ☐ **Delete in ChatGPT.** Use INDEX.md as the tick-list and delete those chats one by one (open chat → ⋯ → Delete). *Settings → Data controls → Delete all chats* exists, but it removes **every** chat, including non-PPC ones. Only use it if that's what you want.

> OpenAI's data-controls help page states how long deleted chats stay on its systems before final removal. Check the current text at help.openai.com.
> Claude can't sign in to your ChatGPT account, so it can't export or delete chats for you. Steps 1 and 8 have to be done by you.

## B. Claude Cowork → repo

For each past Cowork session, paste this prompt into that session:

> Summarise this session as Markdown for my PPC repo: (1) platform, (2) date range, (3) what we analysed, (4) every change made in the ad account (with date), (5) results/metrics observed, (6) decisions and reasoning, (7) open items / next steps, (8) reusable learnings. Do not invent numbers.

Save each output as `imports/cowork/YYYY-MM-DD-<platform>-<topic>.md`, then ask Claude to distil them (same as step A6).

## C. Fill in the shared context
☐ `shared/business-context.md` ☐ `shared/kpis.md` ☐ `shared/budget-plan.md` ☐ `shared/landing-pages.md` ☐ `shared/brand-voice.md` ☐ each platform's `README.md`
