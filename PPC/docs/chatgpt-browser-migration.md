# ChatGPT → PPC repo → delete (Business workspace, via Claude in Chrome)

The scope is **PPC / advertising chats only**. Non-PPC chats are left untouched in ChatGPT.
ChatGPT Business workspaces have no "Export data" option (OpenAI Help: ChatGPT Business FAQ),
so chats are moved using the Claude side panel in Chrome, with a Google Doc as the hand-off.

Deletion is **permanent** and happens only after the import is committed and pushed to GitHub.

---

## Phase 1 — Identify & capture (READ-ONLY). Paste into the Claude side panel with chatgpt.com open

```
Task: find EVERY advertising/PPC-related item in my ChatGPT account and copy its content to a Google Doc.
READ ONLY in ChatGPT — do not delete, archive, rename, move or send anything.

A. IDENTIFY — check ALL of these places (both the "Chat" and "Work" tabs at the top):
   1. Recents in the left sidebar — scroll to the very bottom so the full history loads.
   2. Every Project — click "Show more" to reveal all projects; open each one and list its chats.
      (Start with "Chatgpt Ads", but check every project.)
   3. Pinned chats.
   4. Archived chats — Settings → Data controls → Archived chats → Manage.
   5. Codex — chatgpt.com/codex (all tasks, including archived).
   6. ChatGPT search (magnifier) for each term:
      Google Ads, AdWords, Performance Max, Meta ads, Facebook ads, Instagram ads, LinkedIn ads,
      Microsoft Ads, Bing ads, Reddit ads, X ads, Twitter ads, ChatGPT ads, PPC, CPC, CPL, CPA, ROAS,
      campaign, ad copy, keywords, negative keywords, landing page, pixel, conversion, retargeting,
      lookalike, audience, ad budget, Supermetrics.
   An item is in scope if its main topic is paid advertising, ad tracking, ad landing pages or ad budgets.
   Organic SEO, YouTube SEO, operations, patents, investments, etc. are OUT of scope.

B. Show me ONE de-duplicated table: # | Title | Tab (Chat/Work/Codex) | Location (Project/Recents/Archived) | Date | URL | Why in scope.
   Also list "borderline" items separately. WAIT for my OK and any corrections.

C. CAPTURE — for each approved item, open it, scroll top-to-bottom so everything loads, and record:
   - Title, date, URL, tab, location, platform(s)
   - Summary (3–5 lines)
   - Decisions made and why
   - Changes made in ad accounts (with dates if mentioned)
   - Metrics/results — exact numbers only, never estimate
   - Ad copy, headlines, descriptions, keyword lists, negative keywords, audiences, scripts/code — VERBATIM
   - For Codex tasks: repo, branch/PR link, what was changed
   - Open items / next steps

D. Write everything into ONE Google Doc in my Google Drive named "PPC-ChatGPT-Import-2026-11":
   one section per item, heading "## <#>. <Title> (<date>)". At the end add the index table from step B
   (# | Title | Tab | Location | URL). If the doc gets very long, continue in "...-part2".

E. Report: number of items found, number captured, and any item you could not fully read.
```

## Phase 2 — Import (in Claude Code)
Say: **"Import the Google Doc PPC-ChatGPT-Import-2026-11."**
Claude reads it through the Drive connector, files the content into the platform folders, `shared/learnings.md` and the changelogs, saves the index as `PPC/imports/chatgpt/INDEX.md`, then commits and **pushes to GitHub**.
Claude then gives you the Phase 3 prompt with the exact list of items that are confirmed imported.

## Phase 3 — Delete (only after Phase 2 is pushed)
Claude Code generates this prompt. It lists the exact chat URLs, and the side panel deletes only those.
- Chat/Work chats: open chat → ⋯ → Delete → confirm.
- Archived chats: Settings → Data controls → Archived chats → delete the listed ones only.
- Codex tasks: delete if that option exists, otherwise archive. Their code stays in GitHub either way.
- **Never** use "Delete all chats" (it would remove the non-PPC chats too).
