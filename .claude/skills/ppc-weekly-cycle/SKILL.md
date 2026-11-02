---
name: ppc-weekly-cycle
description: Weekly Setindiabiz PPC evaluate-and-improve cycle using the Elephant-Goldfish Model. Pulls data from every platform, drafts the weekly review and proposed actions (Elephant), has them reviewed by isolated PPC Goldfish reviewers, consolidates findings, and opens a draft PR for human approval. Never changes ad accounts. Safe to run unattended from a scheduled task.
---

# PPC Weekly Cycle (Elephant → Goldfish → human gate)

You are the **Elephant**: the agent holding full context. Read `CLAUDE.md`, `PPC/CLAUDE.md` and everything in `PPC/shared/` first.

**Hard rules**
- READ-ONLY on ad platforms. Do not create, edit, pause, activate or change budgets in this skill. Execution happens only in a later, human-approved session.
- Never invent numbers. A platform without data is marked "missing", not estimated.
- If running unattended, do not stop to ask questions. Record open questions in section 7 of the review.

Let RUN = `PPC/egm/runs/<today YYYY-MM-DD>-weekly/`.

## Step 1 — Pull data (last 7 complete days vs the previous 7)
- **Meta**: Meta Ads connector (`ads_get_ad_accounts`, `ads_get_ad_entities` with insights). Also check `ads_insights_anomaly_signal`.
- **Supermetrics connector** (`data_source_discovery` → `accounts_discovery` → `field_discovery` → `data_query` → `get_async_query_results`). Source IDs: Google Ads `AW`, Microsoft Advertising `AC`, LinkedIn Ads `LIA`, X Ads `TA`, Reddit Ads `RDA`, ChatGPT Ads `CGPTA` (early access), Facebook Ads `FA` (cross-check for Meta). Query only the sources that show `AUTHENTICATED`. Any that aren't are listed as "missing — needs Supermetrics login".
- **ChatGPT Ads fallback**: if `CGPTA` is unavailable, use the newest CSV in `PPC/chatgpt-ads/reports/raw/`.
- **CRM qualified leads**: Zoho CRM connector or Supermetrics `ZOHO`. Use lead counts by source/UTM and stage for the same dates, as aggregates only.
- Save the pulled tables as `RUN/data.md`, with the source and timestamp for each table. No personal data: aggregate counts only.

## Step 2 — Elephant draft
- Write `RUN/weekly_review.md` from `PPC/egm/templates/weekly-review-template.md`, meeting `PPC/egm/standards/weekly-review-standard.md`.
- Section 5: scan every `PPC/*/changelog.md` for "Review on" dates that have passed and evaluate those changes.
- Section 6: propose actions ranked by expected impact. Any ad copy goes in verbatim.

## Step 3 — Goldfish review (isolated, in parallel)
Spawn one fresh subagent per reviewer with the Agent tool (general-purpose). Send them all in a single message so they run in parallel. Give each one only this prompt, with no summary of your own reasoning:

> Read your persona file `<persona>` first and follow it exactly. Mode: REVIEW. TargetFile: `RUN/weekly_review.md`. Standard: `<standard>`. GoldfishContext: `RUN/data.md`, `PPC/shared/`, `PPC/<platform>/README.md` and `changelog.md` for each platform mentioned. Return findings in the persona's output format.

| Persona file | Standard |
|---|---|
| `PPC/egm/reviewers/ppc_performance_critic.md` | weekly-review-standard |
| `PPC/egm/reviewers/measurement_skeptic.md` | weekly-review-standard |
| `PPC/egm/reviewers/budget_cfo.md` | weekly-review-standard |
| `PPC/egm/reviewers/compliance_reviewer.md` | ad-copy-standard (only if section 6 contains ad copy or audience changes) |
| `PPC/egm/reviewers/customer_lens.md` | ad-copy-standard (only if section 6 contains ad copy) |

If the EGM plugin is installed, also spawn the `egm-zoom-out` subagent on the full file. If there are no subagents available, stop and say so: a same-context review is not a Goldfish review.

Write each reviewer's raw output to `RUN/<persona>_report.md`.

## Step 4 — Consolidate (Elephant pre-resolution, nothing applied)
Write `RUN/consolidated_review_report.md` containing:
- the findings deduplicated and grouped 🔴 Blocker / 🟡 Major / 🟢 Nit, with a traceability matrix (finding → reviewer → action #);
- for each finding, the Elephant's recommendation (accept / reject / needs data) with a one-line reason;
- the **final action list** you recommend after the review. Actions blocked by a 🔴 finding are excluded.

Then edit `RUN/weekly_review.md` only for factual corrections. Leave decisions to the human.

## Step 5 — Hand-off for approval
1. Commit on branch `ppc/weekly-<date>` and push. Open a **draft PR** titled `PPC weekly review — week ending <date>` whose body contains the scorecard, the top 5 actions and the Blockers.
2. Send a short notification if a notification tool is available.
3. Stop. The human then runs `/egm:egm-resolve` on `RUN/consolidated_review_report.md` (or comments on the PR) and says "apply approved actions". Only in that later session may changes be made, following `PPC/CLAUDE.md`: approved items only, new entities PAUSED, and each change logged in the platform's `changelog.md` with a "Review on" date.
