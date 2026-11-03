# Lead Quality Watch Log — Meta Ads (SETINDIABIZ 152154124583473)

Daily read-only watch (scheduled 09:40 IST). CRM = source of truth. Definitions: see the scheduled-task prompt (junk / valid / unworked; % of all leads in cohort).

## 2026-10-17 (Sat) — run 09:41 IST

**FUNDING (first):** all 4 active ad sets show delivery OFF, sub-status `account_spend_limit_reached`; only ₹215 spent today by 09:41. Last top-up ₹25,000 on 15 Oct 10:24; billed since ₹9,270.79 (16 Oct) + ₹11,700.57 (17 Oct) = ₹20,971 → ≤ ~₹3.8k left on paper, < 0.5 day at ₹8,000/day budgets. Top-up is human-only.
**Delivery 16 Oct:** account ₹11,576 (FB 8,226 / IG 3,350 / Threads 0.02). No Audience Network, no Marketplace spend. `ads_get_errors` empty.
- #IND1 24Hr INSA ₹4,228 / 19 leads (budget ₹2,500 — 169% day, within Meta's daily overspend allowance) · SIB-02 Form ₹983 / 10 · old SIB-04 Form ₹2,840 / 19 (paused ~23:05) · old SIB-04 CTWA ₹3,402 / 77 convos (paused 22:37) · new Directors Form ₹83 · Directors WhatsApp ₹40 (live late evening only).
**Source guard:** 0 leads with Meta_Campaign set and wrong Lead_Source (10-day window, 415 leads). 6 leads have the right source but Lead_Channel empty (SIB-02 ×5, #IND1 ×1: …948904162, …948958262, …948989001, …949000280, …949025272, …949065236).

**Scorecard** (junk / valid / unworked, % of all leads; cost per valid = ad-set spend ÷ valid)

| Campaign × path | Yday n | junk | valid | unw | 7d n | junk | valid | ₹/valid 7d | Matured (7–13) n | junk | valid | ₹/valid |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SIB-04 WhatsApp | 87 | 29% | 3% | 64% | 313 | 30% | 13% | 572 | 129 | 26% | 28% | 422 |
| SIB-04 Form | 19 | 11% | 16% | 68% | 57 | 11% | 26% | 1,174 | 23 | 0% | 48% | 936 |
| #IND1 Form | 19 | 0% | 42% | 68% | 26 | 0% | 38% | 735 | — (relaunched 15 Oct) | | | |
| SIB-02 Form | 10 | 0% | 40% | 60% | 13 | 0% | 46% | 275 | — (launched 15 Oct) | | | |

- Top Why_Disqualified, SIB-04 WA 7d: Inquired by Mistake 71, Wrong Info 12, No Product Offering 8. SIB-04 Form 7d: Inquired by Mistake 5, No Product Offering 2.
- Trend vs 16 Oct baseline (WA 9–15 Oct: 27% junk, 18% valid): **worse** (30% / 13%), but 16 Oct is the old open-audience ad set's last day. Directors ad sets have not had a delivery day yet → no read possible. Meta_Ad_Set is not stamped on WhatsApp leads, so old vs Directors WA cannot be split in CRM.
**Guardrail audit:** all 4 ACTIVE ad sets have locales [6,24], age_min 25 and a city list (Directors ×2: 19 CCFS cities, male 25–60, A+A off; SIB-02: 30 cities; #IND1: 18 cities). PASS.
**WhatsApp signals (16 Oct, 87 Advt-WhatsApp leads, all have a Tiya note):** 52 coded ([ACR-C5] 46, [ACR-C1] 3, [LLP-C1] 3), 15 Meta standard English greeting, 6 in Indian script (Hindi), 14 other (incl. 1 competitor pitch, junk text). No Social-WhatsApp leads yesterday → no misfiled ad chats.
**Speed:** 162 paid leads > 24 h still unworked (SIB-04 ~145). Top owners: Anish Singh 18, Praveen Singh 15, Tarun Kumar 15, "[customer name redacted] Lost Records" bucket 14, Sudip Manna 13, Amit Kumar 3 12, Krishna Gupta 11, Rishika Singh 11, Priyam Tiwari 9, Dipanshu Saini 7.
**Recommendations (not executed):** (1) Top up / clear spend limit so Directors ad sets get their first full day; stop-loss clock starts on that day — confirm with Directors WA junk ≤ 15%. (2) Stamp Meta_Ad_Set on WhatsApp leads (W6 click capture) so Directors vs old WA quality can be measured — confirm with Meta_Ad_Set non-null on ≥ 90% of new WA leads.

## 2026-10-17 (Sat), 13:50–14:00 IST: junk-control audit (asked by Sanjeev: "re-ensure spam and junk is avoided"; read-only)

**Funding:** ₹20,000 added at 13:48 IST (UPI). Assuming it includes GST, that is about ₹16.9k of ad credit, roughly 2 days at about ₹8k/day. The stop-loss clock for the Directors ad sets moves to **18–20 Oct**, read on 23 Oct (scheduled task trig_01WunWG2jVXrsXmmMK8vEsWL).

| Control | Directors WhatsApp | Directors Form | #IND1 24Hr INSA | SIB-02 TM Form |
|---|---|---|---|---|
| Audience (live read) | A+A off; 7 Company Director lists only, no lookalikes, relaxation 0/0 | same | A+A on (interests are suggestions) | A+A on |
| Hard limits | Male 25–60 · English · 19 cities | same | English · 25+ · 18 cities | English · 25+ · 30 cities |
| Location leakage (15–17 Oct region delivery) | — (new) | — (new) | Only states of the listed cities (HP ₹26 = Chandigarh radius) | 0.4% (₹7 HP / Uttarakhand, radius spill). The `geo: 1` flag does **not** widen beyond the cities in practice |
| Placements | FB + IG feed, stories, reels only | same | Advantage+ minus account exclusions | same |
| Audience Network / Marketplace / WhatsApp Status, 14–16 Oct | ₹0 (account exclusions holding) | ₹0 | ₹0 | ₹0 |
| Instant form | — (pre-filled codes ACR-C1/C2/C5) | SIB-04 ACR Form v1 2635626386872789: **Higher intent**, 2 qualifying questions, consent tick, untargeted leads off | Incorporation V2 1697003818298811: **Higher intent**, 1 question, untargeted off | Trademark V2 1079618781060482: **Higher intent**, 1 question + City, untargeted off |

**Verdict:** every control that stops junk at Meta's end is in place on all 4 live ad sets. The one remaining junk-prone path is WhatsApp one-tap. It is now limited to the 7 Director lists and is guarded by the Directors stop-loss: rejected >40% → pause; ≤25% → keep.

**Early Directors leads (16 Oct 23:00 – 17 Oct 13:50, 5 leads):**
- 1 Valid Lead (Form, Pvt Ltd, FY 2025-26 and earlier).
- 1 Lost "Wrong Info" (Form, OPC).
- 1 Lost "**Inquired by Mistake**" (WhatsApp …948913248). Its chat summary shows a real OPC enquiry for FY 2025-26: the chat was missed at 08:52, before chat hours. **This looks like an RM mislabel, not junk.**
- 2 in progress.

**Found, not junk, for Sanjeev to decide:**
- **Incorporation V2 form intro still says "Start Your Pvt Ltd/LLP in Just 7 Days!" and "Register … in 7 days".** The live ad text was corrected on 15 Oct to "typically 5–7 working days … subject to MCA processing". An instant form that has collected leads can't be edited, so the fix is a new form version plus a new LeadChain chain.
- The Trademark V2 form says "Trusted by 25,000+ businesses over 18+ years". The "18+ years" claim needs substantiation (company incorporated 2015).
- RMs marking real enquiries as "Inquired by Mistake" inflates junk numbers. Ask the TLs to re-check that reason on missed-chat leads.

## 2026-10-17 (Sat), 14:06 IST: post-top-up check (scheduled task trig_01Jkg9n38i7Hh5bjHqs7RmUx; read-only)

- **Top-up confirmed:** activity log "Money added to balance" at 13:48 IST, ₹20,000.00, UPI, fee 0.
- **Delivery:** all 4 ad sets now show delivery **active**. The 09:41 read showed `account_spend_limit_reached`. Directors WA and #IND1 are "active"; Directors Form and SIB-02 are "in learning phase".
- **Spend today:** still ₹53.12 / ₹118.64 / ₹20.80 / ₹22.52 (₹215.08), unchanged from 13:40. This is probably insights reporting lag 18 minutes after the top-up. **Not yet a PASS on "spend rising"**; a one-off re-read is scheduled for 15:08 IST (trig_01FVV1f49ps6hCmSvvX6JPB3).
- **Directors WhatsApp targeting read-back: PASS.**
  - Male, 25–60, locales [6, 24].
  - The same 19 cities at 25 mi.
  - 7 Company Director lists (2019-20 to 2025-26).
  - Relaxation lookalike 0 / custom audience 0; Advantage+ audience 0.
  - FB feed, story and reels; IG stream, story and reels. No Audience Network, Messenger or Threads.
  - Location types include the legacy "frequently_in" alongside home and recent. This matters little with a 25 mi city radius; noted only.
- No changes made.
- **15:08 IST re-read: PASS.** Spend today is rising on all 4 ad sets (₹215 → ₹1,063): Directors WA ₹309.71 (2 conversations), Directors Form ₹352.14 (1 lead), #IND1 ₹304.76 (2 leads), SIB-02 ₹96.21 (1 lead). All show delivery active. No changes made.

## 2026-10-18 (Sun) — run 09:42 IST

**FUNDING (first):** last top-ups ₹25,000 (15 Oct 10:24) + ₹20,000 (17 Oct 13:48). Billed since: ₹9,270.79 (16 Oct) + ₹11,700.57 (17 Oct) + ₹9,499.45 (18 Oct 06:42) = ₹30,470.81. Today's unbilled spend by 09:41 ₹3,201. Left on paper ≈ **₹11.3k (~1.4 days at ₹8,000/day budgets)**; if top-ups include 18% GST ≈ **₹4.5k (< 0.6 day)**. The 17 Oct spend-limit stop happened with ~₹3.8k left on paper, which points to the GST reading → likely runs dry tonight. Top-up is human-only. All 4 ad sets delivering now.
**Delivery 17 Oct:** account ₹9,511 (FB 5,761 / IG 3,750; no Audience Network / Marketplace / Threads). `ads_get_errors` empty. No ₹0 ad sets.
- Directors WA ₹2,044 / 8 convos · Directors Form ₹2,522 / 4 · #IND1 24Hr INSA ₹4,253 / 21 · SIB-02 Form ₹692 / 5.
**Source guard:** 0 leads with Meta_Campaign set and wrong Lead_Source (457 leads, 8–18 Oct). **Lead_Channel empty is growing: 28 leads (was 6)** — 19 of 25 #IND1/SIB-02 leads on 17 Oct and all 8 today. CAPI sweep keys on Lead_Source only, so CAPI is not blocked; reporting hygiene / likely LeadChain regression.

| Campaign × path | Yday n | junk | valid | unw | 7d n | junk | valid | unw | ₹/valid 7d | Matured (8–14) n | junk | valid | ₹/valid |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SIB-04 WhatsApp | 6 | 17% | 17% | 67% | 298 | 37% | 12% | 45% | 602 | 171 | 33% | 23% | 447 |
| SIB-04 Form | 5 | 20% | 0% | 80% | 57 | 18% | 23% | 47% | 1,344 | 27 | 4% | 44% | 1,021 |
| #IND1 Form | 20 | 0% | 10% | 90% | 46 | 0% | 30% | 76% | 829 | — | | | |
| SIB-02 Form | 5 | 0% | 0% | 100% | 18 | 6% | 39% | 56% | 334 | — | | | |

- 17 Oct = first full day of Directors-only SIB-04 (old open ad sets paused 16 Oct night). Top Why_Disqualified 7d WA: Inquired by Mistake 82, Wrong Info 17, No Product Offering 8. Form 7d: Inquired by Mistake 6, Avoiding Call 4, Wrong Info 3.
- Trend: **junk improving** on SIB-04 WA (16 Oct old audience 38/87 = 44% → 17 Oct Directors 1/6), but n is tiny and volume fell 87 → 6 leads (CRM ₹341/lead). The one WA junk (…948913248, "Inquired by Mistake") is the real OPC enquiry flagged 17 Oct as an RM mislabel. Valid % flat-to-down on #IND1 (38% → 30% 7d) because 18/20 of yesterday's leads are still unworked (Saturday), not because of junk (0%).
**Guardrail audit:** all 4 ACTIVE ad sets have locales [6,24], age_min 25, a city list (Directors 19, SIB-02 30, #IND1 18). PASS.
**WhatsApp signals (17 Oct, 6 Advt-WhatsApp leads, all with Tiya notes):** 1 coded [ACR-C5]; 3 WhatsApp-form messages ("I filled in your form…" with entity + pending years — new qualified opener); 2 Meta standard greeting; 0 Indian script. 0 Social-WhatsApp leads → no misfiled ad chats. 1 file-only chat.
**Speed:** **185** paid leads > 24 h unworked (was 162): SIB-04 162, #IND1 17, SIB-02 6. Owners: Anish Singh 21, Praveen Singh 17, [customer name redacted] Lost Records 17, Amit Kumar 3 16, Tarun Kumar 15, Sudip Manna 15, Krishna Gupta 13, Priyam Tiwari 13, Dipanshu Saini 9, Rishika Singh 8.
**Recommendations (not executed):** (1) Top up before tonight so the Directors stop-loss window (18–20 Oct) gets full days — confirm: no `account_spend_limit_reached` at tomorrow's run and 18 Oct spend ≥ ₹7.5k. (2) TLs to work #IND1 + Directors leads first (₹829 and ₹2,000+ per valid; can't judge their quality while 76–90% unworked) — confirm: #IND1 unworked > 24 h ≤ 5 tomorrow. Also: fix Lead_Channel stamping in the #IND1 / SIB-02 LeadChain chains (confirm: 0 new empties).

## 2026-10-18 (Sun), 21:50 IST: evening re-run (extra firing of the daily task; delta only, read-only)

**FUNDING (first): balance exhausted, all ads stopped.** All 4 ACTIVE ad sets show delivery OFF, `account_spend_limit_reached`. No top-up since 17 Oct 13:48 (budget activity log). Today's spend ₹7,635 + billed ₹30,471 = ₹38,106 ≈ ₹45,000 ÷ 1.18 (₹38,136). That confirms the GST reading: top-ups carry 18% GST, so ₹1 of ad credit costs ₹1.18. ₹8k/day of budget needs about ₹9.5k/day of top-up. Last CRM lead arrived at 19:06, so delivery likely stopped around then. Top-up is human-only. The Directors stop-loss window (18–20 Oct) loses tonight.
**Delivery today (to stop):** Directors WA ₹1,691 / 5 convos · Directors Form ₹3,154 / 9 · #IND1 ₹1,932 / 8 · SIB-02 ₹859 / 9. Guardrails unchanged: all 4 have English, age 25+ and a city list. PASS.
**Source guard:** 28 paid leads today. All have the correct Lead_Source and **Lead_Channel 'Advt' (0 empties)**, so the stamping issue from the morning looks fixed or backfilled.

| Today 18 Oct (partial) | n | junk | valid | unw | ₹/valid |
|---|---|---|---|---|---|
| SIB-04 WhatsApp (Directors) | 4 | 25% | 25% | 0% | 1,691 |
| SIB-04 Form (Directors) | 7 | 14% | 14% | 71% | 3,154 |
| #IND1 Form | 8 | 0% | 50% | 50% | 483 |
| SIB-02 Form | 9 | 0% | 33% | 67% | 286 |

- Quality is good: 2 junk out of 28 (7%) and 9 valid (32%), with 3 proposals sent already. The two junk leads are both "Inquired by Mistake" on SIB-04. Other WhatsApp losses are Pricing and Duplicate, not junk.
- **Recommendation (not executed):** top up now, about ₹19k for 2 days. Confirm with: no `account_spend_limit_reached` at the 19 Oct 09:40 run, and 19 Oct spend of at least ₹7.5k.

## 2026-10-19 (Mon) — run 09:41 IST

**Funding:** Sanjeev added ₹25,000 at 22:12 on 18 Oct (UPI). Total top-ups since 15 Oct are ₹70,000, which is ₹59,322 of ad credit after 18% GST. Billed since then: ₹39,490.76 (latest bill ₹9,019.95 on 19 Oct at 06:42). Unbilled spend today by 09:41: ₹2,414. **About ₹17.4k is left, or 2.1 days at ₹8,200/day of budgets.** That runs out around 21 Oct. It is above the 1.5-day threshold, so no warning yet.
**Delivery on 18 Oct:** account ₹9,012 (Facebook ₹5,497, Instagram ₹3,514). No spend on Audience Network, Marketplace or Threads. `ads_get_errors` is empty.
- Directors WhatsApp ₹1,829 / 5 conversations · Directors Form ₹3,787 / 14 leads · #IND1 ₹2,465 / 12 · SIB-02 (original) ₹932 / 10.
**Account changes, 18 Oct 22:03–23:43 (Sanjeev):**
- SIB-02 budget raised from ₹1,000 to ₹1,200.
- At 23:16 the original **SIB-02 Trademark campaign was deleted**, along with old inactive objects (SIB-04 old CTWA and Form, #IND2, #IND6, LLP ACR).
- At 23:41 it was relaunched as "SIB-02 Trademark - Copy" (campaign 120247094837400449, ad set 120247094867020449, ₹1,200/day). Targeting is the same: Male, English, 25+, 30 cities, Advantage+ audience on. Its learning phase restarts. Its ad started delivering at 03:06, and 2 CRM leads have arrived so far.
- The new Meta_Campaign value is **'SIB-02 Trademark - Copy'**.
**Source guard:** 0 leads with Meta_Campaign set and the wrong Lead_Source (498 leads, 9–19 Oct). **Lead_Channel is empty again: 22 leads, 11 of them today.** That is every #IND1 and SIB-02 lead created overnight, and 4 #IND1 + 1 SIB-02 from late 18 Oct. SIB-04 leads are fine. The Conversions API sweep keys on Lead_Source, so it is not blocked; this is a LeadChain stamping regression in the #IND1/SIB-02 chains.

| Campaign × path | Yday n | junk | valid | unw | 7d n | junk | valid | unw | ₹/valid 7d | Matured (9–15) n | junk | valid | ₹/valid |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SIB-04 WhatsApp | 7 | 14% | 14% | 43% | 274 | 42% | 10% | 39% | 732 | 226 | 36% | 18% | 515 |
| SIB-04 Form | 10 | 10% | 10% | 80% | 59 | 20% | 22% | 44% | 1,458 | 38 | 16% | 34% | 1,130 |
| #IND1 Form | 12 | 0% | 33% | 67% | 58 | 0% | 43% | 62% | 563 | 7 | 0% | 43% | 1,040 |
| SIB-02 Form | 10 | 0% | 30% | 70% | 28 | 4% | 39% | 57% | 298 | 3 | 33% | 67% | 333 |

- **Directors-only SIB-04, 17–18 Oct:** 26 leads, 4 junk (15%), 4 valid (15%), 16 unworked (62%). The WhatsApp half has 12 leads with 2 junk; the Form half has 14 leads with 2 junk.
  - Junk is at target. Valid can't be judged while 10 of 14 Form leads are unworked.
  - The 7-day SIB-04 WhatsApp junk rate of 42% is still carried by the old open-audience days (12–16 Oct).
- Top Why_Disqualified, 7d: SIB-04 WhatsApp: Inquired by Mistake 85, Wrong Info 21, Avoiding Call 8. SIB-04 Form: Inquired by Mistake 7, Avoiding Call 4, Wrong Info 4. Yesterday's SIB-04 WhatsApp losses were 1 Duplicate, 1 Pricing and 1 Inquired by Mistake.
- **Trend:** improving.
  - #IND1 7d valid rose from 30% to 43%, with 0% junk.
  - SIB-04 junk on the live ad sets fell (WhatsApp 17% → 14%, Form 20% → 10%).
  - SIB-02 is flat (39% valid).
  - Cost per valid on SIB-04 Directors is high (₹1.8k–3.8k a day) because most leads are not worked yet.
**Guardrail audit:** all 4 ACTIVE ad sets have locales [6,24], age_min 25 and a city list (Directors ×2: 19 cities; #IND1: 18; SIB-02 Copy: 30). PASS.
**WhatsApp signals (18 Oct, 7 Advt-WhatsApp leads, all with Tiya notes):**
- 6 chats opened with the WhatsApp-form message "I filled in your form…" (Pvt Ltd or OPC + pending years). 1 opened with Meta's standard greeting; the RM marked it "not a valid lead".
- 0 coded openers, 0 chats in an Indian script. 0 Social-WhatsApp leads, so no ad chats misfiled as organic.
- 6 of 7 carry a "Duplicate Record" note: they repeat another lead, so WhatsApp and Form counts overlap.
- 3 chats between 22:39 and 23:31 were missed (no operator online).
**Speed:** **189** paid leads older than 24 h are unworked (was 185): SIB-04 146, #IND1 30, SIB-02 13. By owner: Tarun Kumar 19, Praveen Singh 18, [customer name redacted] Lost Records 17, Amit Kumar 3 16, Krishna Gupta 15, Sudip Manna 15, Anish Singh 12, Priyam Tiwari 9, Dipanshu Saini 9, Rishika Singh 8.
**Recommendations (not executed):**
1. TLs should work the 17–18 Oct Directors leads (16 unworked) and the 3 missed late-night WhatsApp chats today. The Directors stop-loss read on 23 Oct needs worked leads. Confirm: Directors 17–18 Oct unworked ≤ 20% at tomorrow's run.
2. Fix Lead_Channel = 'Advt' in the #IND1 and SIB-02 LeadChain chains, and make sure 'SIB-02 Trademark - Copy' maps the same way. Confirm: 0 new leads with empty Lead_Channel tomorrow.

## 2026-10-20 (Tue) — run 09:41 IST

**FUNDING (first): about ₹9.0k of ad credit left, ~1.1 days at ₹8,200/day of budgets. Below the 1.5-day threshold.** There has been no top-up since ₹25,000 on 18 Oct at 22:12. Credit since 15 Oct: ₹70,000 ÷ 1.18 = ₹59,322. Billed: ₹48,468 (latest bill ₹8,977.46 on 20 Oct at 06:42). Unbilled spend today by 09:41: ₹1,846. At this pace delivery stops around midnight or early on 21 Oct. Topping up is human-only.
**Delivery on 19 Oct:** account ₹8,968. `ads_get_errors` is empty.
- Directors WhatsApp ₹2,291 / 7 conversations · Directors Form ₹2,515 / 5 leads · #IND1 ₹2,905 / 29 · SIB-02 Copy ₹1,258 / 16.
- The 3 SIB-05 ad sets are ACTIVE but have all ads off (`multi_all_ads_off`) and ₹0 spend. They are not published yet, so the capture stop-loss has not started.
**Source guard:** 0 leads with Meta_Campaign set and the wrong Lead_Source (531 leads, 10–20 Oct).
- **Lead_Channel is still empty: 23 leads.** That is all 14 #IND1/SIB-02 leads from 19 Oct and 7 from today. The 19 Oct fix has not landed.
- New: lead …950440001 (20 Oct 08:47, Advt - Instagram) has **no Meta_Campaign**.

| Campaign × path | Yday n | junk | valid | unw | ₹/valid | 7d n | junk | valid | unw | ₹/valid 7d | Matured (10–16) n | junk | valid | ₹/valid |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SIB-04 WhatsApp | 1 | 0% | 0% | 100% | — | 221 | 48% | 11% | 31% | 776 | 312 | 44% | 16% | 471 |
| SIB-04 Form | 3 | 0% | 0% | 100% | — | 57 | 28% | 25% | 32% | 1,360 | 57 | 26% | 33% | 927 |
| #IND1 Form | 26 | 0% | 35% | 65% | 323 | 83 | 1% | 48% | 55% | 425 | 26 | 4% | 58% | 490 |
| SIB-02 Form (orig + Copy) | 15 | 0% | 27% | 67% | 314 | 43 | 2% | 49% | 44% | 216 | 13 | 8% | 69% | 183 |

- Top Why_Disqualified, 7d: SIB-04 WhatsApp: Inquired by Mistake 73, Wrong Info 22, No Product Offering 8. SIB-04 Form: Inquired by Mistake 10, Avoiding Call 5, Wrong Info 4. #IND1 and SIB-02: 1 each at most.
- **Trend: improving on #IND1 and SIB-02.** #IND1 7d valid rose from 43% to 48%, with matured valid at 58%. SIB-02 7d valid rose from 39% to 49%, with matured valid at 69%. Junk on both is 2% or less.
- SIB-04 7d junk rose (WhatsApp 42% → 48%, Form 20% → 28%). The cause is that RMs are now working the old open-audience leads from 13–16 Oct; it is not the Directors ad sets.
- **Directors-only SIB-04, 17–19 Oct:** 26 leads, 4 junk (15%), 6 valid (23%), 12 unworked.
  - Of the 14 worked leads, 8 are Lost: 3 Inquired by Mistake (one already flagged as an RM mislabel), 1 Wrong Info, 2 Pricing, 1 Duplicate, 1 No Product Offering.
  - Junk-type rejects are 4/14 (29%), in the 25–40% watch zone. All Lost are 57%. The stop-loss read is on 23 Oct.
- **SIB-04 volume and capture:** ₹4,806 on 19 Oct produced only 4 CRM leads (₹1,201 each). From 17 to 19 Oct, Meta reported 20 WhatsApp conversations but CRM has 10 WhatsApp leads. Meta reported 21 form leads; CRM has 16.
**Guardrail audit:** Directors Form PASS (home + recent).
- Directors WhatsApp: FLAG. Location types include `frequently_in` (known). Everything else passes: Advantage+ audience off, 7 Director lists, relaxation 0/0, placements limited to FB/IG feed, stories and reels, 0% of spend outside them.
- #IND1: FLAG for `frequently_in`. Off-placement spend is 0.6% (₹101 of ₹17.0k). Threads is enabled but has ₹0 spend.
- SIB-02 Copy: FLAG. `geo: 1` location expansion is still on (known, pending approval), plus `frequently_in`. Threads and Marketplace/search are enabled but have ₹0 spend. Off-placement spend is 0.2%.
- SIB-05 ×3: PASS. Exactly the 7 countries, locales [6, 11, 12, 24], age 25+, Advantage+ audience off, both flexible_spec groups present, FB/IG feed, stories and reels only. These ad sets are not live.
- No ad set has a custom-audience exclusion. There was no Audience Network, Marketplace or Threads spend in the last 7 days.
**WhatsApp signals (19 Oct):** 1 Advt-WhatsApp lead.
- It opened with the WhatsApp-form message (Pvt Ltd, FY 2025-26 only). It duplicates the same person's Form lead …949819235, and the chat was missed at 21:35.
- 0 coded openers, 0 chats in an Indian script, 0 Social-WhatsApp leads.
**Speed:** **162** paid leads older than 24 h are unworked (was 189): SIB-04 121, #IND1 32, SIB-02 9.
- By owner: Tarun Kumar 20, Praveen Singh 18, [customer name redacted] Lost Records 17, Krishna Gupta 16, Amit Kumar 3 15, Anish Singh 14, Priyam Tiwari 8, Dipanshu Saini 8.
- 17–18 Oct Directors leads: 8 of 22 are still unworked (36%), which misses the ≤ 20% target.
**Recommendations (not executed):**
1. Top up about ₹19.4k today (2 days × ₹8,200 × 1.18). Confirm: no `account_spend_limit_reached` at the 21 Oct run, and 20 Oct spend ≥ ₹7.5k.
2. Before the 23 Oct Directors read, TLs should clear the 12 unworked Directors leads and re-check the 3 "Inquired by Mistake" labels. Sanjeev or the tech owner should also check why Meta's WhatsApp conversations (20) are double the CRM WhatsApp leads (10). Confirm: Directors unworked ≤ 20% and CRM leads ≥ 80% of Meta results on 21 Oct.

## 2026-10-21 (Wed) — run 09:41 IST

**FUNDING (first): about ₹0.9k of ad credit left, roughly 0.1 day. Ads will likely stop by late morning.** There has been no top-up since ₹25,000 on 18 Oct at 22:12. Credit: ₹70,000 ÷ 1.18 = ₹59,322. Billed: ₹56,451 (latest bill ₹7,982.80 on 21 Oct at 06:42). Unbilled spend today by 09:41: ₹1,929. Push alert sent at 09:42. Topping up is human-only.
**Delivery on 20 Oct:** account ₹7,945. `ads_get_errors` is empty and no active ad set had ₹0 spend, apart from the unpublished SIB-05 ads.
- Directors WhatsApp ₹2,102 / 4 conversations · Directors Form ₹1,938 / 7 leads · #IND1 ₹2,575 / 9 · SIB-02 Copy ₹1,330 / 13.
- Capture is fine: CRM got 5 WhatsApp, 7 SIB-04 Form, 9 #IND1 and 12 SIB-02 leads, plus 1 with no campaign. SIB-05 ×3: still `multi_all_ads_off` with ₹0 spend. The capture stop-loss has not started.
**Source guard:** 0 leads with Meta_Campaign set and the wrong Lead_Source (538 leads, 11–21 Oct).
- **Lead_Channel is still empty on 45 leads.** This includes every #IND1 and SIB-02 lead since 19 Oct (20 Oct: 9 + 11; today: 9), so the fix has not landed.
- Lead …950440001 (Advt - Instagram, 20 Oct) still has no Meta_Campaign.

| Campaign × path | Yday n | junk | valid | unw | 7d n | junk | valid | unw | ₹/valid 7d | Matured (11–17) n | junk | valid | ₹/valid |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SIB-04 WhatsApp | 5 | 0% | 0% | 100% | 198 | 50% | 8% | 32% | 1,354* | 296 | 44% | 14% | 685* |
| SIB-04 Form | 7 | 0% | 0% | 100% | 57 | 28% | 18% | 42% | (*campaign) | 56 | 27% | 30% | (*campaign) |
| #IND1 Form | 9 | 0% | 0% | 100% | 92 | 1% | 43% | 60% | 489 | 45 | 2% | 56% | 465 |
| SIB-02 Form (orig + Copy) | 12 | 0% | 0% | 100% | 55 | 2% | 38% | 56% | ~248† | 18 | 6% | 67% | ~140† |

\* SIB-04 cost is at campaign level (WhatsApp and Form combined), because the old ad sets were deleted. † Original SIB-02 spend is taken from the log for 16–18 Oct; 15 Oct is not available, so these figures are understated.
- **None of the 34 paid leads from 20 Oct has been worked.** The 5 WhatsApp chats were all missed after the bot handoff, and 4 of them came in during the day (10:54–15:34).
- Top Why_Disqualified, 7d: SIB-04 WhatsApp: Inquired by Mistake 70, Wrong Info 19, Language Issue 8. SIB-04 Form: Inquired by Mistake 10, Avoiding Call 4, Wrong Info 4.
- **Trend: flat.** #IND1 7d valid is 43% (was 48%) and SIB-02 is 38% (was 49%). The dip comes from 20 unworked leads in the denominator; junk on both is still 2% or less. Matured valid is above target: #IND1 56%, SIB-02 67%.
- SIB-04 7d junk is 50% and still carries the old open-audience days.
- **Directors-only SIB-04, 17–20 Oct:** 38 leads, 4 junk (11%), 6 valid, 24 unworked (63%). ₹19,041 spent, so cost per valid is ₹3,173.
  - Worked leads are still 14, the same as yesterday. Junk-type rejects are 4/14 (29%), in the watch zone. The 17–18 Oct leads are still 8 of 22 unworked (36%).
**Guardrail audit:**
- Directors Form: PASS.
- Directors WhatsApp: FLAG for `frequently_in` (known). Everything else passes, with 0% off-placement spend.
- #IND1: FLAG for `frequently_in`. Off-placement spend is 0.55% (₹108 of ₹19.6k).
- SIB-02 Copy: FLAG for `geo: 1` (pending approval) and `frequently_in`. Off-placement spend is 0.27%.
- SIB-05 ×3: PASS (7 countries, locales [6, 11, 12, 24], age 25+, Advantage+ audience off, both flexible_spec groups, FB/IG feed, stories and reels only).
- No custom-audience exclusions. No Audience Network, Marketplace or Threads spend in the last 7 days.
**WhatsApp signals (20 Oct):** 5 Advt-WhatsApp leads, and all 5 opened with the WhatsApp-form message (Pvt Ltd, FY 2025-26 only). 0 coded openers, 0 chats in an Indian script, 0 Social-WhatsApp leads.
- 4 of 5 carry a "Duplicate Record" note.
- All 5 chats were missed (operators did not pick up the bot forward).
**Speed:** **193** paid leads older than 24 h are unworked (was 162): SIB-04 119, #IND1 49, SIB-02 24.
- By owner: Pavneet Kaur 21, Tarun Kumar 20, Praveen Singh 19, Krishna Gupta 18, [customer name redacted] Lost Records 17, Amit Kumar 3 15, Anish Singh 14, Dipanshu Saini 8, Mahima Sehrawat 8.
**Recommendations (not executed):**
1. Top up about ₹19.4k now. Confirm: no `account_spend_limit_reached` at the 22 Oct run, and 21 Oct spend ≥ ₹7.5k.
2. The sales team should work the 34 leads from 20 Oct and the 24 unworked Directors leads before the 23 Oct read, and staff the SalesIQ WhatsApp handoff during the day. Confirm: unworked > 24 h ≤ 100 and Directors unworked ≤ 20% at tomorrow's run. Do not judge the ads on this until the leads are worked: this is a sales-process gap, not targeting.

## 2026-10-22 (Thu) — run 09:45 IST

**FUNDING (first): about ₹3.2k of ad credit left, ~0.3 day at ₹12,200/day of budgets (SIB-05 now on). Below the 1.5-day threshold; likely stops around midday.** Top-ups since 15 Oct ₹90,000 (incl. ₹20,000 on 21 Oct 11:17) ÷ 1.18 = ₹76,271. Billed ₹69,056 (latest ₹12,605.18 on 22 Oct 06:50). Unbilled today by 09:45: ₹4,021. Push sent 09:46. Top-up is human-only; 2 days ≈ ₹28.8k.
**Delivery on 21 Oct:** account ₹12,582. `ads_get_errors` empty; no active ad set at ₹0.
- Directors WA ₹1,787 / 6 convos · Directors Form ₹2,508 / 6 leads · #IND1 ₹2,401 / 15 · SIB-02 Copy ₹1,121 / 16 · **SIB-05 ₹4,764 / 0 leads** (Branch-Liaison 3,117, Subsidiary 934, India Entry 713).
- **SIB-05 capture:** 21 Oct 11:17 → 22 Oct 09:45: ₹6,797, 2,235 impressions, 12 link clicks, **0 Meta form leads, 0 CRM leads**. Ad B2 Branch office took ₹4,518 (1,453 impr, CPM ~₹3.1k). Today it has already spent ₹2,028 of the ₹4,000 CBO. The ₹8k / 0-lead stop and the 2-spend-day capture stop both trigger today.
**Source guard:** 0 leads with Meta_Campaign set and the wrong Lead_Source (531 leads, 12–22 Oct). Lead …950440001 no longer appears without a campaign.
- Lead_Channel empty: 18 (was 45, older ones backfilled). Still every new #IND1/SIB-02 lead: 21 Oct 11 of 30, 22 Oct 6 of 6. Fix not landed in the LeadChain chains.

| Campaign × path | Yday n | junk | valid | unw | 7d (15–21) n | junk | valid | unw | ₹/valid 7d | Matured (12–18) n | junk | valid | ₹/valid |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SIB-04 WhatsApp | 2 | 0% | 50% | 50% | 153 | 56% | 10% | 24% | 1,139* | 270 | 52% | 12% | 789* |
| SIB-04 Form | 4 | 0% | 50% | 50% | 57 | 26% | 28% | 33% | (*campaign) | 58 | 28% | 29% | (*campaign) |
| #IND1 Form | 15 | 0% | 20% | 80% | 107 | 4% | 47% | 52% | 440 | 57 | 5% | 51% | 486 |
| SIB-02 Form (orig + Copy) | 15 | 0% | 47% | 53% | 69 | 1% | 52% | 42% | ~176† | 27 | 4% | 59% | ~163† |
| SIB-05 Form | 0 | — | — | — | 0 | | | | ∞ (₹4,764) | — | | | |

\* SIB-04 campaign spend (WA + Form). † Original SIB-02 spend from this log (16–18 Oct); 15 Oct missing → understated.
- Top Why_Disqualified 7d: SIB-04 WA Inquired by Mistake 63, Wrong Info 17, Avoiding Call 7. SIB-04 Form Inquired by Mistake 9, Avoiding Call 4, Wrong Info 4. #IND1 Wrong Info 2, Inquired by Mistake 2.
- **Trend: improving.** 7d valid: #IND1 43% → 47%, SIB-02 38% → 52%, SIB-04 Form 18% → 28%. Junk on #IND1/SIB-02 ≤ 4%. SIB-04 WA 7d junk 56% is still the old open audience (12–16 Oct) being worked.
- **Directors-only SIB-04, 17–21 Oct:** 39 leads, 5 junk (13%), **17 valid (44%)**, 13 unworked (33%). Worked 26 (was 14): 12 Valid, 4 Proposal Sent, 10 Lost (Inquired by Mistake 4, Pricing 2, Wrong Info 1, Duplicate 1, No Product Offering 1, Other CA 1). Junk-type rejects 5/26 = 19% (keep zone ≤ 25%); all Lost 38%. Spend ₹23,343 → ₹1,373 per valid (was ₹3,173). 17–18 Oct unworked 6/22 (27%, was 36%).
**Guardrail audit (fresh read):**
- Directors Form: PASS. Directors WA: FLAG `frequently_in` (known); A+ audience 0, 7 Director lists, relaxation 0/0, FB/IG feed/story/reels, 0% off-placement.
- #IND1: FLAG `frequently_in`; off-placement 0.59% (₹131 of ₹22.0k). SIB-02 Copy: FLAG `geo: 1` (pending approval) + `frequently_in`; off-placement 0.30%.
- SIB-05 ×3: PASS (exactly US/AE/SG/KR/JP/AU/CA, home + recent, locales [6,11,12,24], 25+, A+ audience 0, both flexible_spec groups, FB/IG feed/story/reels only, 0% off-placement).
- No custom-audience exclusions. No Audience Network, Marketplace or Threads spend in 7 days.
**WhatsApp signals (21 Oct):** 2 Advt-WhatsApp leads, both opened with the WhatsApp-form message (Pvt Ltd; one prefixed with an fb.me link, still Advt-sourced). 0 coded, 0 Indian script, 0 Social-WhatsApp. 1 carries a Duplicate Record note. Both chats missed (no live handoff; one at 09:47, one at 21:40).
**Speed:** **153** paid leads > 24 h unworked (was 193): SIB-04 82, #IND1 48, SIB-02 23. Owners: Krishna Gupta 20, Tarun Kumar 18, [customer name redacted] Lost Records 16, Praveen Singh 15, Amit Kumar 3 12, Anish Singh 10, Mahima Sehrawat 8, Anshu Yadav 8, Sudip Manna 7.
**Recommendations (not executed):**
1. Pause SIB-05 India Entry (or at least ad B2) before topping up: ₹6.8k, 12 clicks, 0 leads; both logged stop-losses trigger today. Review form/CTA and the 7-country CPM before relaunch. Confirm: SIB-05 spend ₹0 tomorrow, and the India ad sets get full-day spend.
2. Top up about ₹19.4k (2 days × ₹8,200 India budgets × 1.18) once SIB-05 is paused; ₹28.8k if it stays on. Confirm: no `account_spend_limit_reached` at the 23 Oct run.

## 2026-10-23 (Fri) — run 09:45 IST

**FUNDING (first): about ₹10.1k of ad credit left, ~0.8 day at ₹12,200/day (SIB-05 still on). Below the 1.5-day threshold; likely stops overnight or early 24 Oct.** Top-ups since 15 Oct ₹115,000 (incl. ₹25,000 on 22 Oct 16:01) ÷ 1.18 = ₹97,458. Billed ₹82,729 (latest ₹13,672.57 on 23 Oct 06:50). Unbilled today by 09:45 ₹4,642. 2 days ≈ ₹28.8k with SIB-05, ₹19.4k without. Top-up is human-only.
**Delivery on 22 Oct:** account ₹13,668. `ads_get_errors` empty; no active ad set at ₹0. No pause/targeting/budget changes in the activity log since 22 Oct 09:00 (only Meta auto-audience updates) → SIB-05 was not paused.
- Directors WA ₹2,053 / 8 convos · Directors Form ₹2,440 / 6 · #IND1 ₹2,239 / 18 · SIB-02 Copy ₹1,175 / 14 · SIB-05 ₹5,761 / 1 (Branch-Liaison ₹4,842 / 1, Subsidiary ₹669, India Entry ₹250).
- **SIB-05 captured its first CRM leads:** …951284102 (22 Oct 15:00, already Valid Lead) and …951221124 (today 09:10). Spend 21–23 Oct ≈ ₹13.2k → ~₹6.6k per CRM lead, ₹13.2k per valid. Capture stop cleared; under-delivery stop not hit (₹4,765 and ₹5,761 vs ₹2,000 floor). Branch-Liaison takes ~76% of spend.
**Source guard:** 0 leads with Meta_Campaign set and wrong Lead_Source (519 leads, 13–23 Oct). 0 paid leads without Meta_Campaign. **Lead_Channel empty: 27 (was 18)** — 22 Oct #IND1 8 + SIB-02 7, 23 Oct 6 + 5 (all of today's), 1 old. LeadChain fix still not landed.

| Campaign × path | Yday n | junk | valid | unw | 7d (16–22) n | junk | valid | unw | ₹/valid 7d | Matured (13–19) n | junk | valid | ₹/valid |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SIB-04 WhatsApp | 3 | 0% | 33% | 67% | 101 | 54% | 15% | 21% | 978* | 220 | 55% | 11% | 966* |
| SIB-04 Form | 6 | 0% | 67% | 33% | 50 | 24% | 40% | 28% | (*campaign) | 57 | 30% | 26% | (*campaign) |
| #IND1 Form | 18 | 0% | 28% | 72% | 117 | 4% | 43% | 51% | 422 | 83 | 5% | 48% | 425 |
| SIB-02 Form (orig + Copy) | 14 | 0% | 21% | 79% | 80 | 0% | 51% | 44% | ~183† | 42 | 2% | 60% | ~155† |
| SIB-05 Form | 1 | 0% | 100% | 0% | 1 | 0% | 100% | 0% | 10,526 | — | | | |

\* SIB-04 campaign spend (WA + Form). † Original SIB-02 spend from this log (16–18 Oct); 15 Oct missing → understated.
- Top Why_Disqualified 7d: SIB-04 WA Inquired by Mistake 39, Wrong Info 11, Language Issue 6. SIB-04 Form Inquired by Mistake 8, Wrong Info 3, Language Issue 2. #IND1 Wrong Info 3, Other CA 3, Not Interested 2. SIB-02 Other CA 3, Avoiding Call 2.
- **Trend: improving on SIB-04, flat on #IND1/SIB-02.** SIB-04 Form 7d valid 28% → 40%, WA 10% → 15% as the old open-audience days roll out. #IND1 47% → 43% and SIB-02 52% → 51% (unworked 51%/44% in the denominator); junk ≤ 4%. Matured valid above 40% target on #IND1 (48%) and SIB-02 (60%).
- **Directors stop-loss read (due today): KEEP.** SIB-04 17–22 Oct: 45 leads, 5 junk (11%), 22 valid (49%), 13 unworked. Worked 32: 15 Valid, 6 Proposal Sent, 11 Lost (Inquired by Mistake 4, Pricing 2, Wrong Info 1, Duplicate 1, No Product Offering 1, Other CA 1, Not Interested 1). Junk-type rejects 5/32 = 16% (≤ 25% keep); all Lost 34% (< 40%). Spend ₹27,848 → ₹1,266 per valid (was ₹1,373). 17–18 Oct unworked 6/22 (27%, unchanged).
**Guardrail audit (fresh read):**
- Directors Form: PASS. Directors WA: FLAG `frequently_in` (known); A+ audience 0, 7 Director lists, relaxation 0/0, FB/IG feed/story/reels, 0% off-placement.
- #IND1: FLAG `frequently_in`; off-placement 0.62% (₹131 of ₹21.1k). SIB-02 Copy: FLAG `geo: 1` (pending approval) + `frequently_in`; off-placement 0.29% (₹14 of ₹4.9k).
- SIB-05 ×3: PASS (exactly US/AE/SG/KR/JP/AU/CA, home + recent, locales [6,11,12,24], 25+, A+ audience 0, both flexible_spec groups, FB/IG feed/story/reels only, 0% off-placement).
- No custom-audience exclusions. No Audience Network, Marketplace or Threads spend in 7 days.
**WhatsApp signals (22 Oct):** 3 Advt-WhatsApp leads: 2 WhatsApp-form openers (OPC "not sure"; Pvt Ltd FY 2025-26 only), 1 coded [ACR-C5]; two were prefixed with an instagram.com/p/ link but are correctly Advt-sourced. 0 Indian script, 0 Social-WhatsApp. 2 of 3 carry a Duplicate Record note. Handoff: 1 closed "client not responding", 1 missed at 23:36, 1 SYNC GAP (SalesIQ chat #61858 not ended).
**Speed:** **142** paid leads > 24 h unworked (was 153; window 13–22 Oct): SIB-04 63, #IND1 52, SIB-02 27. Owners: Tarun Kumar 19, Krishna Gupta 18, [customer name redacted] Lost Records 14, Praveen Singh 12, Anish Singh 10, Anshu Yadav 10, Amit Kumar 3 9, Sudip Manna 8, Mahima Sehrawat 6.
**Recommendations (not executed):**
1. Top up today: ≈ ₹28.8k for 2 days with SIB-05, or ≈ ₹19.4k if SIB-05 is paused. Confirm: no `account_spend_limit_reached` at the 24 Oct run and 23 Oct spend ≥ ₹11k.
2. Keep SIB-04 Directors as is (stop-loss passed). SIB-05: capture stop cleared, but at ₹13.2k per valid; if funds are short, pause SIB-05 before any India ad set. Next read 25 Oct: junk > 40% of worked over 3 days → pause; day 7 (27 Oct) split by country. Confirm: SIB-05 CRM leads ≥ 1/day at ≤ ₹4k each.

## 2026-10-24 (Sat) — run 09:41 IST

**FUNDING (first): balance exhausted, all 7 ACTIVE ad sets delivery OFF (`account_spend_limit_reached`).** Today's spend ₹764 by 09:41. Top-ups since 15 Oct ₹115,000 (last ₹25,000 on 22 Oct 16:01) ÷ 1.18 = ₹97,458. Billed ₹96,697 (latest ₹13,968.21 on 24 Oct 06:50) + ₹764 unbilled → ≈ ₹0 left. Push sent 09:45. Top-up is human-only: 2 days ≈ ₹28.8k with SIB-05, ₹19.4k without.
**Delivery on 23 Oct:** account ₹13,901. `ads_get_errors` empty; no ad set at ₹0.
- Directors WA ₹1,733 / 6 convos · Directors Form ₹2,117 / 9 · #IND1 ₹2,375 / 17 · SIB-02 Copy ₹1,165 / 11 · SIB-05 ₹6,512 / 3 (Branch-Liaison ₹4,772 / 3, Subsidiary ₹965, India Entry ₹775).
- Capture good: CRM got 6 WA + 9 SIB-04 Form, 17 #IND1, 11 SIB-02, 3 SIB-05.
**Source guard:** 0 leads with Meta_Campaign set and wrong Lead_Source (515 leads, 14–24 Oct). 0 paid leads without Meta_Campaign. **Lead_Channel empty: 16 (was 27)** — 23 Oct #IND1 6/17, SIB-02 6/11; 22 Oct 4. Older ones backfilled; still ~half of new #IND1/SIB-02 leads miss it.

| Campaign × path | Yday n | junk | valid | unw | 7d (17–23) n | junk | valid | unw | ₹/valid 7d | Matured (14–20) n | junk | valid | ₹/valid |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SIB-04 WhatsApp | 6 | 0% | 33% | 67% | 20 | 15% | 40% | 35% | 1,321* | 193 | 59% | 9% | 1,100* |
| SIB-04 Form | 9 | 0% | 0% | 100% | 39 | 5% | 41% | 44% | (*campaign) | 57 | 30% | 26% | (*campaign) |
| #IND1 Form | 17 | 0% | 29% | 71% | 115 | 3% | 46% | 45% | 364 | 92 | 5% | 51% | 417 |
| SIB-02 Form (orig + Copy) | 11 | 0% | 27% | 73% | 80 | 0% | 51% | 45% | 148 | 54 | 2% | 57% | ~168† |
| SIB-05 Form | 3 | 0% | 33% | 67% | 4 | 0% | 50% | 50% | 8,525 | — | | | |

\* SIB-04 campaign spend (WA + Form). † Copy ₹2,604 + original 16–18 Oct from this log; 14–15 Oct missing → understated.
- Top Why_Disqualified 7d: SIB-04 WA Inquired by Mistake 3, Duplicate 1, No Product Offering 1. SIB-04 Form Other CA 2, Pricing 1, Inquired by Mistake 1. #IND1 Avoiding Call 3, Not Interested 3, Other CA 3. SIB-02 Avoiding Call 3, Other CA 2.
- **Trend: improving.** The 7d window is now Directors-only for SIB-04: WA valid 15% → 40%, junk 54% → 15%; Form 40% → 41%, junk 24% → 5%. #IND1 43% → 46%, SIB-02 51% flat; junk ≤ 3%. Matured valid above 40% on #IND1 (51%) and SIB-02 (57%); SIB-04 matured still carries the old open audience (14–16 Oct).
- **Directors SIB-04, 17–23 Oct:** 59 leads, 5 junk (8%), 24 valid (41%), 24 unworked. Worked 35: 15 Valid, 7 Proposal Sent, 1 Negotiation, 12 Lost. Junk-type rejects 5/35 = 14%, all Lost 34% → KEEP holds. ₹31,702 → ₹1,321 per valid. 17–18 Oct unworked 5/22 (23%, was 27%).
- **SIB-05:** 4 CRM leads (22 Oct 1, 23 Oct 3), 2 Valid, 0 junk. 23 Oct ₹6,512 / 3 leads = ₹2,171 per lead (≤ ₹4k target met). 7d ₹17,051 → ₹4.3k/lead, ₹8.5k/valid. Branch-Liaison 73% of spend. Junk read 25 Oct; country split 27 Oct.
**Guardrail audit (fresh read):** Directors Form PASS. Directors WA FLAG `frequently_in` (known); A+ audience 0, 7 Director lists, relaxation 0/0, FB/IG feed/story/reels, 0% off-placement. #IND1 FLAG `frequently_in`; off-placement 0.61% (₹117 of ₹19.3k). SIB-02 Copy FLAG `geo: 1` (pending approval) + `frequently_in`; off-placement 0.35% (₹21 of ₹6.1k). SIB-05 ×3 PASS (7 countries, home + recent, locales [6,11,12,24], 25+, A+ audience 0, both flexible_spec groups, FB/IG feed/story/reels, 0% off-placement). No custom-audience exclusions. No Audience Network, Marketplace or Threads spend in 7 days.
**WhatsApp signals (23 Oct):** 6 Advt-WhatsApp leads, all opened with the WhatsApp-form message (Pvt Ltd ×6; FY 2025-26 only ×4, earlier years ×1, not sure ×1); 5 prefixed with an instagram.com/p/ link, 1 with fb.me, all correctly Advt-sourced. 0 coded, 0 Indian script, 0 Social-WhatsApp. 3 carry a Duplicate Record note. 2 SYNC GAP flags (SalesIQ #61870, #61871 not ended); 2 already worked (proposal sent for 2 companies; callback).
**Speed:** **138** paid leads > 24 h unworked (was 142): #IND1 54, SIB-04 51, SIB-02 32, SIB-05 1. Owners: Krishna Gupta 17, Tarun Kumar 16, [customer name redacted] Lost Records 14, Sudip Manna 14, Praveen Singh 12, Amit Kumar 3 10, Anish Singh 9, Anshu Yadav 8, Rama Dwivedi 6, Mahima Sehrawat 6.
**Recommendations (not executed):**
1. Top up now: ≈ ₹28.8k for 2 days with SIB-05, or ≈ ₹19.4k if SIB-05 is paused (pause SIB-05 before any India ad set if funds are short). Confirm: no `account_spend_limit_reached` at the 25 Oct run and 24 Oct spend ≥ ₹7.5k.
2. TLs to clear the 54 unworked #IND1 leads (largest backlog; ₹364 per valid, best-quality campaign after SIB-02). Confirm: #IND1 unworked > 24 h ≤ 25 tomorrow.

## 2026-10-25 (Sun) — run 09:45 IST

**FUNDING (first): still exhausted, 2nd day. All 7 ACTIVE ad sets delivery OFF (`account_spend_limit_reached`).** No top-up since ₹25,000 on 22 Oct 16:01. Credit since 15 Oct ₹115,000 ÷ 1.18 = ₹97,458; billed ₹97,461 (latest ₹764.23 on 25 Oct 06:50) → ≈ ₹0. Push sent 09:46. Top-up is human-only: 2 days ≈ ₹28.8k with SIB-05, ₹19.4k without.
**Delivery on 24 Oct:** account ₹764 (all before the stop). Directors WA ₹58 / 1 convo · Directors Form ₹161 / 1 · #IND1 ₹48 · SIB-02 Copy ₹26 · SIB-05 ₹471 (Branch-Liaison ₹390, Subsidiary ₹71, India Entry ₹9). `ads_get_errors` empty. Every ad set ~₹0 because of funding, not a delivery fault.
**Source guard:** 0 leads with Meta_Campaign set and wrong Lead_Source (514 leads, 14–24 Oct). 0 paid leads without Meta_Campaign. Lead_Channel empty: 12 (was 16): 22 Oct 4, 23 Oct 8 (#IND1/SIB-02). No new ones (only 2 SIB-04 leads yesterday).

| Campaign × path | Yday n | junk | valid | unw | 7d (18–24) n | junk | valid | unw | ₹/valid 7d | Matured (15–21) n | junk | valid | ₹/valid |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SIB-04 WhatsApp | 1 | 0% | 0% | 100% | 16 | 6% | 38% | 44% | 1,189* | 152 | 58% | 10% | 1,140* |
| SIB-04 Form | 1 | 0% | 0% | 100% | 34 | 3% | 50% | 29% | (*campaign) | 54 | 30% | 30% | (*campaign) |
| #IND1 Form | 0 | — | — | — | 96 | 4% | 52% | 32% | 301 | 106 | 5% | 52% | 400 |
| SIB-02 Form (orig + Copy) | 0 | — | — | — | 75 | 0% | 56% | 37% | 167 | 69 | 1% | 64% | ~144† |
| SIB-05 Form | 0 | — | — | — | 4 | 0% | 50% | 50% | 8,761 | — | | | |

\* SIB-04 campaign spend (WA + Form). † Original SIB-02 spend 16–18 Oct from this log; 15 Oct missing → understated.
- Top Why_Disqualified 7d: SIB-04 WA Duplicate 1, Pricing 1, Inquired by Mistake 1. SIB-04 Form Other CA 2, Inquired by Mistake 1, Not Interested 1. #IND1 Avoiding Call 4, Other CA 4, Inquired by Mistake 3. SIB-02 Avoiding Call 3, Other CA 3.
- **Trend: improving** (leads already in CRM being worked; no new volume). 7d valid: #IND1 46% → 52%, SIB-02 51% → 56%, SIB-04 Form 41% → 50%, WA 40% → 38%; junk ≤ 6% everywhere in 7d. Matured valid ≥ 40% on #IND1 (52%) and SIB-02 (64%); SIB-04 matured still carries the old open audience (15–16 Oct).
- **Directors SIB-04, 17–24 Oct:** 59 leads, 5 junk (8%), 25 valid (42%), 19 unworked. Worked 40: 17 Valid, 6 Proposal Sent, 1 Negotiation, 2 Postponed, 14 Lost. Junk-type rejects 5/40 = 13%, all Lost 35% → KEEP holds. ₹31,921 → ₹1,277 per valid.
- **SIB-05 junk read (due today): no trigger.** 4 CRM leads, 2 worked (both Valid), 0 junk. ₹17,522 → ₹4.4k/lead, ₹8.8k/valid. Day-7 country split on 27 Oct (needs delivery to resume).
**Guardrail audit (fresh read):** Directors Form PASS. Directors WA FLAG `frequently_in` (known); A+ audience 0, 7 Director lists, relaxation 0/0, FB/IG feed/story/reels, 0% off-placement. #IND1 FLAG `frequently_in`; off-placement 0.62% (₹93 of ₹15.1k). SIB-02 Copy FLAG `geo: 1` (pending approval) + `frequently_in`; off-placement 0.35% (₹21 of ₹6.1k). SIB-05 ×3 PASS (7 countries, home + recent, locales [6,11,12,24], 25+, A+ audience 0, both flexible_spec groups, FB/IG feed/story/reels, 0% off-placement). No custom-audience exclusions. No Audience Network, Marketplace or Threads spend in 7 days.
**WhatsApp signals (24 Oct):** 1 Advt-WhatsApp lead (…951690432, 23:15): WhatsApp-form opener (Pvt Ltd, FY 2025-26 only) prefixed with fb.me, correctly Advt-sourced. 0 coded, 0 Indian script, 0 Social-WhatsApp. Duplicate Record note (matches Form lead …951756335). Chat MISSED: "Operators are not responded to the bot forward request".
**Speed:** **135** paid leads > 24 h unworked (was 138): SIB-04 54, #IND1 47, SIB-02 32, SIB-05 2. Owners: Krishna Gupta 16, [customer name redacted] Lost Records 14, Sudip Manna 14, Shubendu Banerjee 13, Tarun Kumar 12, Praveen Singh 11, Amit Kumar 3 10, Anish Singh 8, Rama Dwivedi 6.
**Recommendations (not executed):**
1. Top up now: ≈ ₹28.8k for 2 days with SIB-05, or ≈ ₹19.4k if SIB-05 is paused first (₹8.8k/valid vs ₹167–1,277 on India campaigns). Confirm: no `account_spend_limit_reached` at the 26 Oct run and 25 Oct spend ≥ ₹7.5k.
2. Use the no-delivery days to clear the 135-lead backlog (#IND1 47 first, best ₹/valid after SIB-02) and staff the WhatsApp bot handoff. Confirm: unworked > 24 h ≤ 100 tomorrow.

## 2026-10-26 (Mon) — run 09:41 IST

**FUNDING (first): still exhausted, 3rd day running. All 7 ACTIVE ad sets delivery OFF (`account_spend_limit_reached`); `ads_get_errors` now shows an account-level error: "prepaid funds are empty".** No top-up since ₹25,000 on 22 Oct 16:01 (no new budget-log entries since the ₹764.23 bill on 25 Oct 06:50). Credit ₹97,458 vs billed ₹97,461 → ≈ ₹0. Top-up is human-only: 2 days ≈ ₹28.8k with SIB-05, ₹19.4k without.
**Delivery on 25 Oct:** ₹0 on every ad set (funding, not a delivery fault). No CRM paid lead since 24 Oct 23:15.
**Source guard:** 0 leads with Meta_Campaign set and wrong Lead_Source (515 leads, 14–24 Oct). 0 paid leads without Meta_Campaign. Lead_Channel empty: 12 (unchanged: 22 Oct 4, 23 Oct 8, #IND1/SIB-02).

| Campaign × path | Yday n | 7d (19–25) n | junk | valid | unw | ₹/valid 7d | Matured (16–22) n | junk | valid | ₹/valid |
|---|---|---|---|---|---|---|---|---|---|---|
| SIB-04 WhatsApp | 0 | 12 | 0% | 42% | 58% | 1,144* | 101 | 55% | 15% | 978* |
| SIB-04 Form | 0 | 26 | 0% | 54% | 35% | (*campaign) | 48 | 25% | 42% | (*campaign) |
| #IND1 Form | 0 | 84 | 2% | 52% | 33% | 286 | 117 | 5% | 53% | 341 |
| SIB-02 Form (orig + Copy) | 0 | 66 | 0% | 58% | 36% | 161 | 79 | 0% | 59% | ~160† |
| SIB-05 Form | 0 | 4 | 0% | 50% | 50% | 8,761 | 1 | 0% | 100% | 10,539 |

\* SIB-04 campaign spend (WA + Form). † Copy + original 16–18 Oct from this log.
- Top Why_Disqualified 7d: #IND1 Avoiding Call 4, Other CA 4, Not Interested 3. SIB-02 Other CA 3, Avoiding Call 2. SIB-04 Form Not Interested 1, Avoiding Call 1; WA none. Matured SIB-04 WA Inquired by Mistake 40, Wrong Info 11, Language Issue 6 (16 Oct old open audience).
- **Trend: flat-to-improving, no new volume.** 7d window moved to 19–25 Oct, so 7d junk is now 0–2% on every campaign and valid 42–58%. Matured valid ≥ 40% on #IND1 (53%), SIB-02 (59%) and now SIB-04 Form (42%); SIB-04 WA matured still has 16 Oct in it.
- **Directors SIB-04, 17–25 Oct:** unchanged from 25 Oct: 59 leads, 5 junk, 25 valid, 19 unworked; worked 40, junk-type rejects 13%, all Lost 35% → KEEP. **No RM work on these leads in 24 h.**
- **SIB-05:** 4 leads, 2 Valid, 1 Establishing Contact, 1 untouched (…951683222). Day-7 country split (27 Oct) can't run: only ~2.2 spend days.
**Guardrail audit (fresh read):** unchanged. Directors Form PASS. Directors WA FLAG `frequently_in` (known); A+ audience 0, 7 Director lists, relaxation 0/0, FB/IG feed/story/reels, 0% off-placement. #IND1 FLAG `frequently_in`; off-placement 0.63% (₹79 of ₹12.6k). SIB-02 Copy FLAG `geo: 1` (pending approval) + `frequently_in`; off-placement 0.35% (₹21 of ₹6.1k). SIB-05 ×3 PASS. No custom-audience exclusions. No Audience Network, Marketplace or Threads spend in 7 days.
**WhatsApp signals (25 Oct):** 0 Advt-WhatsApp / Social-WhatsApp leads (no delivery).
**Speed:** **137** paid leads > 24 h unworked (was 135; +2 from 24 Oct): SIB-04 56, #IND1 47, SIB-02 32, SIB-05 2. Owners: Krishna Gupta 16, [customer name redacted] Lost Records 14, Sudip Manna 14, Shubendu Banerjee 13, Tarun Kumar 12, Praveen Singh 11, Amit Kumar 3 10, Anish Singh 8, Rama Dwivedi 6. The backlog did not move over the weekend.
**Recommendations (not executed):**
1. Top up today: ≈ ₹19.4k if SIB-05 is paused first (₹8.8k/valid vs ₹161–1,144 on India campaigns), ≈ ₹28.8k if it stays on. Confirm: no `account_spend_limit_reached` at the 27 Oct run and 26 Oct spend ≥ ₹7.5k. Expect a short re-learning dip after 3 dark days; judge on CRM quality, not first-day CPL.
2. Monday: TLs to clear the 137-lead backlog (#IND1 47 and SIB-02 32 first, lowest ₹/valid) and the 19 unworked Directors leads. Confirm: unworked > 24 h ≤ 100 at tomorrow's run.
