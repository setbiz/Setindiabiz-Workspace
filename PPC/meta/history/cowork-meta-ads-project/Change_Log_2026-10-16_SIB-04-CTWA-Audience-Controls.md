# Change log — 16 Oct 2026 — SIB-04 WhatsApp ad set: English language + minimum age 25

**Approval:** Sanjeev approved in chat at 11:35 IST ("Ok approved all proposed changes, go ahead"). He was approving the recommendations in `SIB-04_Junk_Diagnosis_2026-10-16.md` §6.

**Executed by:** Claude via the Meta connector (`ads_update_entity`) at about 11:45 IST.
- The change was staged as an Ads Manager draft (`is_draft: true`, `status_forced_to_paused: false`). Meta validated it (VALIDATED, no active errors).
- The ad set stayed ACTIVE on the old targeting while the draft waited, so there was no gap in delivery.

**LIVE: published by Sanjeev in Ads Manager on 16 Oct 2026, 11:41:32 IST** (updated_time 06:11:32 UTC).

**Read-back on the Meta connector at about 11:45 IST:**
- The live spec shows `age_min` 25 and `locales` [6, 24].
- All 15 custom audiences are unchanged, and Advantage+ audience is still on.
- Effective status ACTIVE, budget ₹3,500/day, optimisation CONVERSATIONS.
- No pending draft. `ads_get_errors` is empty for the ad set and the campaign.
- The Form ad set 120246968737470449 is unchanged (age_min 18, no locales, last updated 13 Oct) and serves as the control.

**Ad set:** 120246968316940449 "SIB-04 | ACR | CTWA | IN", in campaign 120246968311680449. Nothing else was touched.

## What changed

| Targeting field | Before | After |
|---|---|---|
| `locales` (language, a hard limit) | not set (any language) | **[6, 24] English (US), English (UK)**, the same as #IND1, #IND3, SIB-02 and CCFS |
| `age_min` (a hard limit) | 18 | **25**, the same as #IND1 24Hr INSA, #IND3 TMF-SA and SIB-02 |
| `age_max` | 65 | 65 |
| `geo_locations` | IN, location types frequently_in, home, recent | unchanged |
| `custom_audiences` | 15 lists (8 Director, 6 LLP, 1 Director 1% lookalike) | unchanged, same 15 IDs |
| `targeting_relaxation_types` | lookalike 1, custom_audience 1 | unchanged |
| `targeting_optimization` | expansion_all | unchanged |
| `targeting_automation.advantage_audience` | 1 (on) | unchanged |
| `brand_safety_content_filter_levels` | FACEBOOK_RELAXED, AN_RELAXED | unchanged |
| Placements | automatic (account controls exclude AN, Marketplace and right column) | unchanged |
| Budget, optimisation, schedule | ₹3,500/day, CONVERSATIONS, no end date | unchanged |

**Before snapshot:** spend today up to about 11:40 IST was ₹1,176.81 for 23 conversations.

**Note on Meta's rules:** under Advantage+ audience, `age_min` above 25 is rejected, so 25 is the highest hard minimum available without turning A+A off.

## Why

Full evidence is in `SIB-04_Junk_Diagnosis_2026-10-16.md`. In short:
- WhatsApp leads from 9 to 15 Oct were 27% junk (62 of 229), with half still unworked.
- The Form ad set, which has the same audience but asks questions, had 0 junk in 38 leads.
- 16 chats came in in Hindi, Gujarati or Tamil script, including Meta's greeting translated. Only 1 of them is valid.
- SIB-04 was the only campaign without the English language limit and a minimum age of 25.

## Effect on the 13 Oct placement-controls read

That stop-loss window is 14–16 Oct. This change went live at 11:41 IST on 16 Oct, so the WhatsApp ad set's 16 Oct numbers mix two settings. For the 17 Oct read:
- Judge the WhatsApp ad set on **14–15 Oct**.
- Use the untouched Form ad set for 16 Oct.

On 16 Oct data the campaign's cost per valid lead (9–15 Oct) was ₹665, against the ₹731 baseline and the ₹914 revert threshold. **No revert is indicated.**

## Stop-loss for this change (quality-first, updated 16 Oct ~12:15 IST)

**Operating principle (Sanjeev, 16 Oct):** "we must work towards good quality consistently over time, cost will come down." Judge on CRM quality, not on Meta cost.

- **Window:** **17–19 Oct**, the first three full days after Publish.
- **Decision read:** **22 Oct**, so the cohort has had three days to be worked.
- **Measure:** WhatsApp ad-set spend from the connector, and CRM leads with `Meta_Campaign = 'SIB-04 Annual Filings'`, `Lead_Source = 'Advt - WhatsApp'`, created in the window.
  - **Valid** = status Valid Lead, Negotiation, Proposal Sent or Payment Pending, or a quality field starting "Valid".
  - **Junk** = Why_Disqualified is Inquired by Mistake, Job Seeker, Bot Created/Spam or Wrong Info, or a quality field is Invalid.
- **Baselines:**
  - 9–15 Oct, read 16 Oct: WhatsApp junk **27%**, valid **18%**, cost per valid **₹502**.
  - Same-age comparison: the 10–13 Oct cohort read on 15 Oct was 130 leads, 25% junk.
- **KEEP** the change if junk% is lower than baseline and valid% is not lower, **even if cost per valid has risen**. Higher cost on its own is not a reason to revert.
- **Recommend REVERT** (remove the locales, set age_min back to 18) only if:
  - quality did not improve (junk% not lower **and** valid% lower), or
  - the ad set cannot deliver (it spent under 50% of its ₹3,500 daily budget on all 3 days).
- **Success target:** WhatsApp junk **at or below 15%**. If junk is still above 15%, Change 2 below is staged.
- **Expected and not a trigger:** fewer chats and a higher Meta cost per conversation. Learning restarts after the edit.
- *(Superseded: the earlier cost-only rule "revert if 3-day cost per valid > ₹628".)*

## Scheduled follow-ups

These are scheduled in the Meta Ads session.
- **17 Oct 10:00 IST:** confirm the change is still live, and run the placement-controls read (trigger trig_01H2MNnoWAEHnht4NmEhxySb).
- **22 Oct 10:00 IST:** decision read for this change using the quality-first rules above, plus the Change 2 gate (trigger trig_01MPVr6hm9VZN8k3E8v8H8Dp).
- **Daily 09:40 IST:** lead-quality watch across all campaigns, with source guard and funding warning (trigger trig_01DPT99ZCoF8rictq4EsC2bP).

## Approved follow-on (conditional)

**Change 2:** limit WhatsApp ad-set location to the 19 CCFS cities (25-mile radius) **only if** junk is still above 15% at the 22 Oct read. Stage it as a draft for Sanjeev to publish, as with this change.

**Caution when publishing Change 2:** Ads Manager's Publish can include other pending drafts. The TM and INC WhatsApp ad-set drafts (see `Change_Log_2026-10-16_IND1-Source-Backfill-and-TM-INC-WhatsApp-Drafts.md`) are held PAUSED, so they will not spend if swept up.

## Not done (options only, not approved as defaults)

- **Male only:** needs Advantage+ audience off.
- **Excluding a custom audience of past junk numbers.**

## Handed to the SalesIQ project (not touched here)

See `Tiya_Project_Prompt_ACR-Qualifier-and-Ad-Signal_2026-10-16.md`.

## 17 Oct 2026, 10:00 IST — scheduled check-in (read-only; no changes made)

### 1. Status of this change

**Superseded the same evening.** The English + age-25 change was live from 16 Oct 11:41 IST until **22:37 IST**. At 22:37 Sanjeev had the WhatsApp ad set 120246968316940449 paused (connector, via the ads MCP server). It was replaced by the directors-only ad sets; see `Change_Log_2026-10-16_Lead-Quality-Diagnosis.md`.

The old Form ad set 120246968737470449 was also paused, at about 23:01 IST.

Read-back at 10:00 IST:
- Both old ad sets are PAUSED.
- The WhatsApp spec still shows locales [6, 24] and age_min 25.
- `ads_get_errors` is empty for the campaign and both ad sets.

**Consequence for the 22 Oct read:**
- The 17–19 Oct window for this change will have no delivery, so there is nothing to judge on 22 Oct.
- The 22 Oct task should report "superseded" and **not stage Change 2**. The directors ad sets already use the 19 CCFS cities.

### 2. 13 Oct placement-controls stop-loss read (window 14–16 Oct)

**Placements: PASS.** On both ad sets, all three days:
- Audience Network **₹0**;
- Marketplace **₹0**;
- WhatsApp Status **₹0**.

Threads took ₹0.27. What remains outside the CCFS placements is FB in-stream (₹412 CTWA, ₹134 Form) and Reels overlay (₹261 CTWA).

**CRM** (Meta_Campaign "SIB-04 Annual Filings", read 17 Oct 10:00 IST):

| | Spend | Leads | Valid (status Valid Lead+) | Junk | Unworked (blank or Establishing Contact) | Cost per valid | Revert threshold |
|---|---|---|---|---|---|---|---|
| WhatsApp ad set, 14–15 Oct | ₹5,399.10 | 97 | 1 | 36 (37%) | 50 (52%) | ₹5,399 | ₹662 |
| Form ad set, 14–16 Oct | ₹7,230.28 | 34 | 2 | 6 (18%) | 22 (65%) | ₹3,615 | ₹2,428 |
| Campaign, 14–16 Oct (WhatsApp ₹8,801.29 + Form) | ₹16,031.57 | 218 | 4 | — | — | ₹4,008 | ₹914 |

Notes on the counts:
- **Junk** = Inquired by Mistake, Job Seeker, Bot Created/Spam or Wrong Info. WhatsApp 14–15: 25 + 2 + 2 + 7. Form: 5 Inquired by Mistake + 1 Bot.
- Six leads carry RM quality "Valid - RM Working" but are Lost with "Inquired by Mistake" or "Job Seeker". They are not counted as valid. This field conflict should go to the TLs.
- WhatsApp 16 Oct alone: 87 leads, 1 valid, 30 lost (20 of them Inquired by Mistake), 56 unworked.

**Verdict: KEEP the placement controls.** The cost thresholds are breached, but the breach does not come from the placement change:
- Audience Network was only about 15% of spend before 13 Oct. Removing it cannot explain valid leads falling roughly 10×.
- The drivers are WhatsApp junk (37%, above the 27% baseline) and unworked leads (52–65%, sales-process).
- Turning the controls off would bring back Audience Network's accidental taps. That is against the 16 Oct quality-first principle.
- The cost-only revert rule was written before that principle and is retired here.
- The audience problem is already being addressed by the 16 Oct directors-only rebuild.

**Not changed:** Meta, CRM and the account placement controls.

**Flag for TLs:** 72 of the 131 leads above (55%) are still blank or Establishing Contact after 1–3 days.

## 22 Oct 2026, ~10:05 IST — decision read (scheduled task trig_01MPVr6hm9VZN8k3E8v8H8Dp; read-only)

**Verdict: SUPERSEDED.** There is no KEEP/REVERT decision, and Change 2 was **not staged**.
- Ad set 120246968316940449 is **ARCHIVED**. It was deleted with the old inactive objects on the night of 18 Oct.
- It spent **₹0 on 17, 18 and 19 Oct**. Meta still credits it with 3 + 1 conversations on 17–18 Oct, which come from earlier clicks.
- The Form control 120246968737470449 is also ARCHIVED, with ₹0 spend.
- Change 2 (the 19 CCFS cities) cannot be applied to an archived ad set. Its successor, Directors WhatsApp 120247072309210449, already has the same 19 cities, plus male 25–60, English, the 7 Director lists and Advantage+ audience off.

**Successor read, 17–19 Oct (for information only).** The formal Directors stop-loss read is on 23 Oct, for 18–20 Oct.
- Source: CRM, Meta_Campaign 'SIB-04 Annual Filings', leads created 17–19 Oct, read on 22 Oct at about 10:00 IST.
- Definitions are as in this log. A Lost lead with a "Valid" quality field counts as Lost, not valid.

| Path | Spend (connector) | Leads | Junk | Valid | Unworked | ₹ per valid |
|---|---|---|---|---|---|---|
| Directors WhatsApp | ₹6,170.27 | 9 | 3 (33%) | 2 (22%) | 1 (11%) | ₹3,085 |
| Directors Form (control) | ₹8,830.02 | 16 | 2 (13%) | 5 (31%) | 7 (44%) | ₹1,766 |
| Baseline: WhatsApp, 9–15 Oct (old open audience) | — | 229 | 27% | 18% | — | ₹502 |

- **The 3 WhatsApp junk leads**, all marked "Inquired by Mistake":
  - …948913248 (17 Oct, 08:51–08:52) is the RM mislabel flagged on 17 Oct.
  - …949064205 (17 Oct, 08:51–08:52) also carries RM quality "Valid - RM Working", which conflicts with the Lost reason.
  - …949665003 (18 Oct).
- Without the known mislabel, junk is 2 of 8 (25%).
- The other WhatsApp losses are not junk: Duplicate Record, No Product Offering and Pricing.
- **Reading:** n = 9 is too small to call. Valid is up (18% → 22%); junk at face value is not lower (27% → 33%). Under this log's rules that is neither KEEP nor REVERT. Cost per valid is high, but cost alone is not a trigger.
- **Capture gap:** Meta reports 20 Directors WhatsApp conversations for 17–19 Oct, but CRM has 9 WhatsApp leads. Many chats carry a "Duplicate Record" note because the same person also sent a form.

**SalesIQ ACR qualifier (item 1 of the 16 Oct Tiya prompt): no sign it has shipped.**
- No WhatsApp lead since 16 Oct carries a "Not Eligible" disposition.
- Why_Disqualified values seen on Advt - WhatsApp leads, 16–22 Oct: Inquired by Mistake 39, Wrong Info 10, Language Issue 6, Bot Created/Spam 4, Not Interested 3, Avoiding Call 3, and 1 each of Non-Compliant, Duplicate, No Product Offering and Pricing.
- Since 17 Oct, WhatsApp chats open with Meta's WhatsApp-form message ("I filled in your form…" + entity + pending years). Qualification is coming from the Directors ad's own form, not from the bot, so junk counts are not affected by any bot change.

**Not changed:** Meta, CRM.
