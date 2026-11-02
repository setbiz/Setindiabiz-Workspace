# ChatGPT (Business workspace) → PPC repo, via Claude in Chrome

ChatGPT Business workspaces have no "Export data" option (OpenAI Help: ChatGPT Business FAQ).
So the chats are moved using the Claude side panel in Chrome, with a Google Doc as the hand-off.

## Step 1 — paste this into the Claude side panel (with chatgpt.com open)

```
Task: migrate my PPC/advertising chats out of ChatGPT. READ ONLY — do not delete, archive, rename or send anything in ChatGPT.

1. In ChatGPT, open the project "Chatgpt Ads", then use ChatGPT search (magnifier icon) for each of:
   Google Ads, Meta, Facebook ads, Instagram ads, LinkedIn ads, Microsoft Ads, Bing, Reddit ads,
   X ads, Twitter ads, ChatGPT ads, PPC, CPC, CPL, campaign, keywords, ad copy, landing page, budget.
   Build a de-duplicated list of matching chats (title + date + URL).
2. Show me the list and wait for my OK before continuing.
3. For each approved chat, open it, scroll to load the whole conversation, and record:
   - Title, date, URL, platform(s)
   - Summary (3–5 lines)
   - Decisions made and why
   - Changes made in ad accounts (with dates if mentioned)
   - Metrics/results mentioned (exact numbers only — never estimate)
   - Ad copy, headlines, keyword lists, negative keywords, audiences — copied VERBATIM
   - Open items / next steps
4. Create ONE Google Doc in my Google Drive named "PPC-ChatGPT-Import-2026-11" and write each chat
   as its own section under a "## <Title> (<date>)" heading, in the structure above.
5. At the end of the doc add an index table: Title | Date | URL.
6. Tell me when done and how many chats were captured.
```

## Step 2 — back in Claude Code
Say: "Import the Google Doc PPC-ChatGPT-Import-2026-11 into the repo."
Claude reads the doc via the Drive connector, files content into platform folders and `shared/learnings.md`, and commits.

## Step 3 — remove from ChatGPT (only after Step 2 is committed and pushed)
Prefer **Archive** first (chat ⋯ → Archive): it's reversible. Delete only the chats in the doc's index table.
Deleted chats cannot be recovered.
