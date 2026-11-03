# Claude export import (3 Nov 2026)

Export `d1f730d1…`, created 03 Nov 2026 02:51 UTC. Three of the eight ZIPs are relevant: `projects-000`, `claude_code_cloud-000` and `conversations-000`.
Personal data was redacted before commit: customer phone numbers, customer names and personal (gmail etc.) addresses. The company WhatsApp numbers and staff work emails were kept.

| ZIP | Status | What went where |
|---|---|---|
| `projects-000.zip` (44 projects) | **Imported** | See below |
| `claude_code_cloud-000.zip` | **Imported** | Holds scheduled tasks and their runs only, no session transcripts. The 23 PPC-related tasks are in `routines-ppc.md` |
| `conversations-000.zip` (105 MB) | **Pending.** Too large to upload to the chat | The chats themselves, including those inside the "Google Ads", "Twitter Ads", "FDI Clients - Leads" and "Meta Ads - Optimisation" projects |

## Projects
| Project | Imported to | Notes |
|---|---|---|
| **Meta Ads - Optimisation** (176 files + instructions) | `PPC/meta/history/cowork-meta-ads-project/` | The full Cowork history Jun–Nov 2026: change logs, scorecards, daily lead-quality watch logs, CAPI/LeadChain/CTWA Deluge code, SIB-04 and SIB-05 build specs. `.docx` files are text extracts (`*.docx-text.md`) |
| **Lead Source** (instructions only) | `PPC/shared/lead-source-attribution-runbook.md` | The 38-value prefixed Lead_Source taxonomy and the classifier workflow |
| Google Ads, Twitter Ads, FDI Clients - Leads | — | No files or instructions. Their chats are in `conversations-000.zip` |
| All others (SEO, blogs, video, CRM, HR, ops) | Not imported | Outside PPC scope. Candidates for the future `SEO-YouTube/`, `OPS/` areas |

## Scheduled tasks that overlap with this repo (all ON)
| Task | Runs | Relationship to the EGM tasks |
|---|---|---|
| Meta lead-quality watch (daily) | 09:40 IST daily, Cowork | Writes `Lead_Quality_Watch_Log_*.md`. The EGM weekly review should read these logs rather than repeat them |
| Weekly paid-channel measurement report | Mon 09:00 IST | Overlaps the EGM weekly review (Mon 10:17 IST). Candidate to retire once the EGM cycle has run twice |
| Monthly LeadChain phone reconciliation | 1st of month 10:00 IST | Complements the EGM monthly review (2nd) |
