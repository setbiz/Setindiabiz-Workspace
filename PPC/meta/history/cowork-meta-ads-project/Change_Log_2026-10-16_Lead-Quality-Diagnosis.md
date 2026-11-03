# Change log — 16 Oct 2026, ~22:15–23:15 IST — lead-quality (junk) fix

Diagnosis: `Meta Ads/Lead_Quality_Junk_Diagnosis_2026-10-16.md`.

**Sanjeev's answers (chat, ~22:35 IST):** pause SIB-04 WhatsApp now — yes; directors only, male; age 25–60 plus graduate+ education; 19 CCFS cities.

## Change A — LIVE: SIB-04 WhatsApp ad set paused

- Ad set 120246968316940449 "SIB-04 | ACR | CTWA | IN", via connector `ads_update_entity` {"status":"PAUSED"}; `is_draft: false`.
- **Before:** ACTIVE, ₹3,500/day; spend today ₹3,357.38, 72 chats (Meta).
- **After (read-back):** status PAUSED, effective_status PAUSED, updated 16 Oct 22:37:09 IST; spend frozen at ₹3,357.38. Its 4 ads show ADSET_PAUSED.
- Nothing else touched. The SIB-04 Form ad set 120246968737470449 is still ACTIVE (₹2,500/day) until Change B is published.
- Supersedes: the 22 Oct quality read of the 16 Oct English + age-25 change and its staged Change 2 (city limit). The scheduled task itself was not edited — when it runs on 22 Oct it should report the ad set as paused.
- Revert: not planned. WhatsApp returns only as the directors-only ad set below.

## Change B — DRAFTS ONLY (not published, nothing spending)

Built in campaign 120246968311680449 "SIB-04 Annual Filings". Both ad sets are **PAUSED inside the draft**, so an accidental publish will not spend.

| | Form | WhatsApp |
|---|---|---|
| Ad set id | **120247072301790449** "SIB-04 \| ACR \| Directors \| Form \| 19C" | **120247072309210449** "SIB-04 \| ACR \| Directors \| WhatsApp \| 19C" |
| Optimisation | LEAD_GENERATION, on-ad form 2635626386872789 | CONVERSATIONS, WhatsApp [phone redacted], 1-day click attribution (Meta rejected 7-day for this goal) |
| Budget | ₹2,500/day | ₹2,000/day |
| Ads (same creatives as the live ads) | 120247072323670449 ACR-C1 Deadline · 120247072324940449 ACR-C2 Cost of delay · 120247072326340449 ACR-C5 Dates and price | 120247072327710449 ACR-C1 · 120247072328200449 ACR-C2 · 120247072330100449 ACR-C5 (coded pre-filled messages carried over) |
| LLP-C1 Form 8 ad | left out (no LLP lists in the audience) | left out |

**Audience (both, all hard limits):**
- Advantage+ audience **off**; `targeting_relaxation_types` lookalike 0, custom_audience 0; no lookalikes.
- Custom audiences: Company Director 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26 (7 lists). Director 2026-27 excluded.
- Male; age 25–60; English (US, UK).
- Education (flexible_spec): college graduate, in / some grad school, master's, professional degree, doctorate — enum [3, 7, 8, 9, 10, 11].
- 19 CCFS cities, 25 mi, living in or recently in.
- Placements: Facebook + Instagram Feed, Stories, Reels.

**Read-back (draft, ~23:10 IST):** all of the above confirmed on both ad sets. WhatsApp ad set and its 3 ads: no errors. Form ad set and its 3 ads: Meta flags **error 1815089 "Lead Generation Terms of Service not accepted"** — the long-standing API-side ToS mismatch (the Page shows "Accepted" in the UI, and the live Form ad set was created in Ads Manager).

## Update 22:55 IST — education dropped (Sanjeev: "we can drop education")

- With education [3,7,8,9,10,11] Ads Manager estimated **79,100–93,000** people and flagged the audience as "quite narrow".
- Education removed from both drafts via connector (draft edits, still unpublished and PAUSED); all other settings unchanged.
- New estimate (WhatsApp draft, Ads Manager): **356,500–419,400** people.
- Form draft still shows error 1815089 (Lead Gen ToS) in Ads Manager, although the same panel says the terms are accepted for the Page. Billing page asked for Sanjeev's passkey, so the balance was not checked.
- Stop-loss widening order is now: all-India location first, then (only with Sanjeev's say) all genders.

## Update ~23:05 IST — PUBLISHED AND LIVE (Sanjeev: "yes, publish")

Done by Claude in Sanjeev's Chrome (Ads Manager) plus the connector:
1. **Review draft items:** ticked only the 2 Directors ad sets and their 6 ads, with "Try to publish items with errors" (the Lead Gen ToS flag turned out to be spurious). Result: "2 ad sets and 6 ads were published". The other 14 drafts (SIB-05 India Entry, TM and INC WhatsApp, the two "DISCARD" INC ads) were **not** published and are still drafts.
2. **Read-back found a problem:** Ads Manager published the WhatsApp ad set with **all-India location and Advantage+ placements** (incl. Audience Network, Marketplace, WhatsApp Status, Threads) instead of the draft spec — it overwrote the draft on publish, like the 16 Oct INC incident. The Form ad set was correct.
3. **Fixed before switch-on:** connector targeting update on 120247072309210449 (staged as draft), then published only that ad set ("Updated: Audience"). Read-back: 19 cities, FB + IG Feed / Stories / Reels, male, 25–60, English, 7 Director lists, A+A off, relaxation 0/0. Note: Meta re-adds "frequently_in" to location types — harmless.
4. **Switched on** both Directors ad sets (Ads Manager toggles) — read-back ACTIVE, updated 23:01 IST. Their 6 ads are in Meta review (PENDING_REVIEW / IN_PROCESS).
5. **Switched off old Form ad set** 120246968737470449: the Ads Manager toggle did not take, so paused via connector (`status: PAUSED`, is_draft false). Read-back: ADSET_PAUSED on its 4 ads.
6. One stray click hit **Duplicate** earlier (toolbar shifted); the dialog was cancelled, nothing duplicated.

**Live ad sets after the change (connector, ~23:05 IST):**

| Ad set | Budget/day |
|---|---|
| SIB-04 \| ACR \| Directors \| Form \| 19C (120247072301790449) | ₹2,500 |
| SIB-04 \| ACR \| Directors \| WhatsApp \| 19C (120247072309210449) | ₹2,000 |
| #IND1 C1 - 24Hr INSA | ₹2,500 |
| SIB-02 \| TM \| Form \| IN | ₹1,000 |
| **Total** | **₹8,000** |

Paused: SIB-04 \| ACR \| CTWA \| IN (22:37) and SIB-04 \| ACR \| Form \| IN (~23:04).

**Stop-loss clock:** starts on the first full delivery day after Meta approves the ads (expected 17 Oct, if funds allow). 3 full days; read on day 6 in CRM (rejected ≤25% and valid ≥35% of worked = keep; rejected >40% = pause; <50% budget spent 3 days running = widen to all-India first).

**Watch:** after any future edit opened in Ads Manager, re-read the live targeting through the connector — Ads Manager has now twice rewritten a draft on its own.

## Update ~23:20 IST — #IND3 Trademark "Director - TMF" restart (Sanjeev: "restart Director-TMF")

Why: best historical quality of any ad set (Jul–Aug CRM: 172 leads, 56% Valid - RM Working, 3% junk). TMF-SA 408 / 55% / 5%; Daytime INSA 251 / 51% / 8%; 24Hr INSA 179 / 50% / 12%.

- The original ad set 120243249506380449 cannot be edited: Meta error 2446289 (a placement variant of one of its ads references a deleted reel). Its end-date draft (15 → 31 Oct) is staged with that error — **do not publish it; discard it**.
- Built instead (drafts, PAUSED): **"C3 Adset - Director - TMF - Web + Form | Restart Oct" 120247072947130449** in #IND3 - Trademark — identical historical targeting (A+A on, male suggestion, 28 cities, English, Director/LLP/GST lists as suggestions, small-business-owner / Page-admin behaviours and education as suggestions), OFFSITE_CONVERSIONS on dataset Lead, Website + Lead form, lifetime ₹12,000 to 31 Oct (~₹800/day; campaign requires lifetime budgets).
- Ads (draft) reusing the historical creatives: Ad 3 120247072971100449, Ad 4 120247072973570449, Ad 5 120247072975380449, Ad 6 120247072976120449, Ad 7 120247072979500449. All show only the spurious Lead Gen ToS flag.
- **Ad 2 (120247072969850449) to be left unpublished:** its copy says "Government fees: ₹4,500"; under the Trade Marks Rules 2017 First Schedule ₹4,500 applies to individuals / startups / small enterprises, companies pay ₹9,000. Director-targeted audience → misstatement risk.
- Campaign #IND3 stop_time 15 → 31 Oct staged as a draft (no errors).
- **Publishing was refused by the browser permission check** → Sanjeev to publish (steps given in chat), then Claude reads back.
- Stop-loss: 3 full days after delivery starts, read in CRM (Meta_Ad_Set name contains "Restart Oct"): keep if rejected ≤20% of worked; pause if rejected >30% or 0 CRM leads after ₹2,000 spend.

## Update ~23:30 IST — Director-TMF: OLD ad set restarted (Sanjeev: "Keep the old one")

- **What Sanjeev's publish did (read-back 23:25 IST, connector):** published at 23:19 IST:
  - the #IND3 campaign stop_time is now 31 Oct; the campaign is still PAUSED;
  - the **old** ad set 120243249506380449 took the end-date edit despite error 2446289: status ACTIVE, end 31 Oct, lifetime ₹60,000 with **₹11,831.42 remaining** (≈ ₹790/day over 15 days); targeting unchanged (A+A on, 28 cities, 19 lists as suggestions);
  - the new "| Restart Oct" ad set 120247072947130449 went live with **no ads** and is PAUSED;
  - the five "| Restart" ads and the restart Ad 2 are still drafts.
- **Decision (Sanjeev, chat):** run the old ad set, which keeps its learning history. The empty restart ad set stays off. Its 6 draft ads stay unpublished; discard them later.
- **Change:** the old ad set's **#C3B TM Ad 2** (120243249506430449, "Government fees: ₹4,500" line) was switched **off**.
  - The connector pause was refused with the spurious Lead Gen ToS error 1815089, so it was done with the Ads Manager toggle in Sanjeev's Chrome.
  - Read-back: PAUSED, updated 23:28 IST.
- **Old ad set ads now:** Ads 3, 4, 5, 6 and 7 are ACTIVE, waiting only on the campaign (CAMPAIGN_PAUSED); Ad 1 and Ad 2 are PAUSED.
- **Still needed:** Sanjeev switches the **#IND3 - Trademark** campaign On. Activation stays human; Claude then reads back.
- The TMF-SA ad set (120243118118000449) ended on 15 Oct and does not restart with the campaign.
- **Stop-loss:** 3 full days after delivery starts, read in CRM where Meta_Ad_Set = "C3 Adset - Director - TMF - Web + Form".
  - Keep if rejected ≤20% of worked leads.
  - Pause if rejected >30%, or 0 CRM leads after ₹2,000 spend.
  - Baseline (Jul–Aug): 56% Valid - RM Working, 3% junk.

## Publish steps for Sanjeev (Ads Manager) — superseded, kept for reference

1. Open Ads Manager → SIB-04 Annual Filings. You will see the two new "Directors … 19C" ad sets as drafts.
2. In each, check the audience panel says the estimated audience size, and that "Use as a suggestion" is not ticked anywhere. If the estimate is very small (Meta warns "too narrow"), tell Claude before publishing — the first thing to drop is education.
3. Publish (Review and publish). If the Form ad set is blocked by the Lead Gen terms, accept them at facebook.com/legal/leadgen/tos for the Setindiabiz Private Limited page and publish again. Leave the TM / INC WhatsApp drafts unpublished — untick them if they appear in the publish list.
4. Switch both new ad sets **On**, and switch the old **SIB-04 | ACR | Form | IN** **Off** in the same sitting.
5. Tell Claude; Claude reads back the live specs and spend.
6. Funding must be topped up first, or nothing will deliver.

## Stop-loss (Change B)

- Window: the first 3 full days after switch-on; read on day 6 so leads are worked.
- **Keep** if rejected (junk + not a buyer) ≤25% of worked leads and valid ≥35% of worked.
- **Pause and review** if rejected >40%.
- **Too small:** if either ad set spends <50% of its budget on all 3 days, widen in this order: drop education → all-India location → (only with Sanjeev's say) all genders.
- Judge in CRM only (Meta_Campaign "SIB-04 Annual Filings", Lead_Source Advt - Facebook / Instagram / WhatsApp, created in the window).

## 23 Oct 2026, ~10:20 IST — Directors stop-loss read, window 18–20 Oct (scheduled task trig_01WunWG2jVXrsXmmMK8vEsWL; read-only)

**Verdict: KEEP both Directors ad sets.** Nothing was changed in Meta or CRM.

**Definitions** (project standard, from `Lead_Quality_Junk_Diagnosis_2026-10-16.md`):
- **Rejected** = junk + not a buyer.
  - Junk = Inquired by Mistake, Job Seeker, Bot Created/Spam, Wrong Info, or an Invalid quality field.
  - Not a buyer = No Product Offering, Not Eligible, Non-Compliant, Language Issue.
- **Worked** = status is not blank or Establishing Contact.
- **Valid** = Valid Lead, Negotiation, Proposal Sent or Payment Pending. A Lost lead with a "Valid" quality field counts as Lost.
- CRM read on 23 Oct at about 10:15 IST.

**Spend against budget (connector):**

| Ad set | Budget/day | 18 Oct | 19 Oct | 20 Oct | Total |
|---|---|---|---|---|---|
| Directors Form 120247072301790449 | ₹2,500 | ₹3,788.65 (152%) | ₹2,519.14 (101%) | ₹1,943.85 (78%) | ₹8,251.64 |
| Directors WhatsApp 120247072309210449 | ₹2,000 | ₹1,828.97 (91%) | ₹2,296.79 (115%) | ₹2,103.24 (105%) | ₹6,229.00 |

Both ad sets spent at least 50% of budget on every day, so no widening is needed.

**CRM leads created 18–20 Oct:**

| Path | Leads | Worked | Rejected (of worked) | Valid (of worked) | Other Lost | Unworked | ₹ per valid | Rule |
|---|---|---|---|---|---|---|---|---|
| Form (Advt - FB / IG) | 19 | 12 | 1 (8%) | 9 (75%), incl. 4 Proposal Sent | 2 (Other CA, Not Interested) | 7 (37%) | ₹917 | KEEP |
| WhatsApp (Advt - WhatsApp) | 5 | 5 | 1 (20%) | 2 (40%) | 2 (Duplicate Record, Pricing) | 0 | ₹3,115 | KEEP (n = 5) |
| Both | 24 | 17 | 2 (12%) | 11 (65%) | 4 | 7 (29%) | ₹1,316 | KEEP |

**"Inquired by Mistake" check (2 leads): no mislabel found.**
- …948929729 (Form, 18 Oct): the RM's note says a friend enquired by mistake and the caller was abusive. Genuine.
- …949665003 (WhatsApp, 18 Oct): the only message was Meta's default greeting, and the RM's note says "Not a valid lead, have no idea about the enquiry". Genuine.

**WhatsApp capture:** Meta counts 16 conversations (5 / 7 / 4), and CRM keeps 5 WhatsApp leads.
- The 21 Oct watch saw 5 WhatsApp leads for 20 Oct, 4 of them with "Duplicate Record" notes. Those 4 are no longer in CRM; they were merged into the same person's Form lead.
- So much of the WhatsApp volume is the same directors who also send the form. These are not lost leads.

**Cost:** the Form costs 3.4× less per valid lead than WhatsApp. Under the 16 Oct quality-first principle cost is not a trigger; it is noted here for the budget split.

**Today:** both ad sets are delivering (Form ₹710.11, WhatsApp ₹361.17 by about 10:15 IST).

**Recommendation (not executed; needs Sanjeev's go):**
- Optional, one variable: move ₹400/day from Directors WhatsApp (₹2,000 → ₹1,600, −20%) to Directors Form (₹2,500 → ₹2,900, +16%).
- Confirm with: over the next 3 days, Form valid stays at least 35% of worked with rejected at most 25%, and WhatsApp still spends at least 50% of its budget.
- Stop-loss: revert if Form rejected goes above 25% over 3 days.

**For the TLs:** 7 Form leads from 18–20 Oct are still blank or Establishing Contact, 3–5 days after they came in.
