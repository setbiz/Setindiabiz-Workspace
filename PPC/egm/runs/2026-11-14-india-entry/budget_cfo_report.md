# Goldfish Review: Budget CFO, India Entry (FDI) US plan, DRAFT v1

_Reviewer: `ppc-budget-cfo` (isolated). Target: `design_draft.md`. Context read: `shared/budget-plan.md`, `shared/kpis.md`, `shared/business-context.md`, `reports/cross-platform/2026-11-14-india-entry-diagnosis.md`. Read-only: no ad-platform or CRM tool was called. Severity scale: Blocker / Major / Minor (the persona's "Nit" = Minor). `[calc]` = my arithmetic; `[est]` = my estimate, labelled as such._

## Recheck of every [calc] in the plan

| Plan figure | Recheck | Verdict |
|---|---|---|
| §2 Meta US ₹4,454 per QL | 13,361.78 ÷ 3 = ₹4,453.93 | OK. Blended SIB-05 was ₹13,741 per QL (41,223.41 ÷ 3); the plan quotes only the US cut |
| §2 FDI AOV ≈ ₹86,300 | 14,67,582 ÷ 17 = ₹86,328 | OK (all India-entry: 16,31,480 ÷ 20 = ₹81,574) |
| §2 Google CPC ₹374.6 | 28,092 ÷ 75 = ₹374.56 | OK |
| §2 ≈600–700 high-intent US searches/month | Sum of listed non-informational terms = 620; with "doing business in india" 710 | OK |
| §4 Margin per won deal ₹51,780 | 86,300 × 0.60 | OK |
| §4 Break-even CPQL ₹7,767 | 51,780 × 0.15 | OK, but depends wholly on the 15% [est] (F3) |
| §4 Target ₹6,000 ≈ 77% of break-even | 6,000 ÷ 7,767 = 77.2% | OK |
| §5 Shares and total | 1,20,000 + 45,000 + 75,000 + 25,000 + 20,000 + 15,000 = 3,00,000; shares 40 / 15 / 25 / 8.33 / 6.67 / 5 | OK |
| §5 Daily total ₹10,550 | 4,000 + 1,500 + 2,500 + 800 + 1,000 + 750 | OK |
| §5/§7 Realistic max loss ₹1,05,000 | 20,000 + 15,000 × 5 = 95,000; + "K0 ≈ ₹10,000" | Arithmetic OK; K0 ₹10,000 is an unlabelled estimate, and the conclusion is wrong (F1) |
| §9.3 Stories + IG Feed "₹8,056 for 0 leads" | 4,643.37 + 1,836.81 + 1,769.37 = **₹8,249.55** | **Wrong** (F10) |

---

## Findings

### F1. Maximum loss is overstated as capped; kill rules let spend run above break-even
1. **Severity**: Blocker
2. **Affected Scope**: §5 "Maximum loss month 1"; §7 K1, K2, total line
3. **Economic Rationale**:
   - K1 fires only at **exactly 0 QL**. One QL on a platform disarms it, and then only K2 is left, on day 30, when the full cap is already spent. Scenario: each of 6 platforms gets 1 QL and 0 wins → spend = **₹3,00,000**, not ₹1,05,000. The ₹1,05,000 is the loss in only one scenario (0 QL everywhere).
   - K2 pauses at CPQL **> ₹12,000**, which is 12,000 ÷ 7,767 = **1.55× break-even**. A platform can run all month at ₹7,768–₹12,000 per QL, losing money on the plan's own economics. ₹12,000 CPQL needs QL→won ≥ 12,000 ÷ 51,780 = **23.2%** to break even [calc], against the 15% assumed.
   - Between S1 (≤ ₹6,000) and K2 (> ₹12,000) there's a ₹6,000-wide "hold" band, and most of it (₹7,767–₹12,000) is loss-making.
   - Reddit: K1 threshold ₹15,000 = its whole cap, so K1 never protects it. ChatGPT: K1 = 75% of cap.
   - K1 is judged on CRM Lead_Status, which lags lead creation (diagnosis §2a: 4 of 8 SIB-05 leads unworked). At LinkedIn's ₹2,500/day, a 4-day status lag adds ₹10,000 past the ₹15,000 trigger [calc].
4. **Recommendation (cap)**:
   - Replace K1 with a CPQL kill that keeps working after the first QL: "pause when spend ≥ ₹15,000 (Google ₹20,000) **and** spend ÷ (QL + 1) > ₹7,767", checked twice a week.
   - Set K2 at the break-even (**CPQL > ₹7,767** at day 30), not ₹12,000. Drop the "open proposal ≥ ₹50,000" exception, or limit it to a 7-day extension capped at ₹10,000.
   - Measure K1/K2 on leads that are at least 3 working days old. Add an SLA rule: no platform is judged while unworked leads are more than 25%.
   - Restate max loss as "₹3,00,000 ceiling (committed caps); expected loss under kill rules ₹X", with the derivation, and label K0 as [est] (2 days × that platform's daily budget, i.e. ≤ ₹21,100 if all platforms fail together [calc]).

### F2. Hard-cap mechanics left to the implementer, and partly unworkable
1. **Severity**: Blocker (standard: "a build sheet that leaves a decision to whoever implements it")
2. **Affected Scope**: §5 "Hard caps"; §5 "Meta prepaid balance"; §9.2
3. **Economic Rationale**:
   - Google: "monthly account budget of ₹1,20,000 (account-level budget order **or** campaign end date)" is a choice left to the implementer. An end date doesn't cap spend: Google can spend up to 2× the daily budget on a day, with a monthly limit of 30.4× daily (≈ ₹1,21,600 at ₹4,000 [calc]). An account budget caps the **whole account**, so any other campaign in 1859576856 would share the ₹1,20,000.
   - Microsoft: "campaign monthly budget ₹25,000". Microsoft Advertising campaigns run on daily budgets; monthly campaign budgets are not offered for new campaigns (verify in the UI at build). ₹800 × 30 = ₹24,000, not ₹25,000.
   - Meta: one ad account has one prepaid balance. You can't fund the India-Entry campaign "separately from SIB-01/02/04" inside account 152154124583473. Either campaign can drain the balance the other needs. Only the campaign spending limit (₹45,000) is a real cap.
4. **Recommendation (cap)**: Name one mechanism per platform in §9:
   - Google: a campaign-level end date plus a weekly spend check, or an account budget only if this is the sole active campaign. State which.
   - Microsoft: daily ₹800, an end date of start + 30 days, and a manual stop at ₹24,000.
   - Meta: campaign spending limit ₹45,000, plus an account spending limit raised by exactly ₹45,000 over current committed spend.
   - Delete the "funded separately" sentence, or ask the owner for a separate ad account.

### F3. Break-even rests on one unsourced assumption, and the target fails if it is off by a third
1. **Severity**: Major
2. **Affected Scope**: §4 (QL→won 15% [est], margin 60%, AOV)
3. **Economic Rationale**:
   - Break-even CPQL by QL→won rate (margin ₹51,780) [calc]: 5% → ₹2,589 · 10% → ₹5,178 · 15% → ₹7,767 · 20% → ₹10,356. The ₹6,000 target is above break-even whenever QL→won < 6,000 ÷ 51,780 = **11.6%**. No measured paid QL→won rate exists (diagnosis §1: `Converted__s` false on all 92 FDI leads).
   - AOV is drawn from mostly organic, Indian-addressed deals (18 of 20 "India"). The plan will advertise "From USD 499" (≈ ₹43,900 at an assumed ₹88/USD [est]). If paid US buyers close near the advertised price, margin per deal = 43,900 × 0.6 = ₹26,340, and break-even CPQL at 15% = **₹3,951** [calc], which is below the target.
   - `business-context.md` flags that deal Amount may include government fees. Applying 60% to a gross figure overstates margin. The 60% is a verbal owner figure; `kpis.md` still shows 50% (TODO).
4. **Recommendation (proceed with conditions)**:
   - Add a sensitivity table to §4, and set the target CPQL from the 10% case (≤ ₹5,000) until real data arrives.
   - Confirm with finance whether FDI deal Amount includes govt fees and GST, and recompute AOV net of them.
   - At day 60, replace 15% with the measured rate and re-set K2/S1.

### F4. Google gets 40% of the budget for demand that can't absorb it
1. **Severity**: Major
2. **Affected Scope**: §2 demand bullet; §5 Google row; §7 K1 (Google ₹20,000); §9.1
3. **Economic Rationale**:
   - ≈620 high-intent US searches/month [calc]. Even at 100% impression share and 10% CTR [est] → 62 clicks × ₹374.6 historic CPC = **₹23,225**, or at most 62 × ₹700 max CPC = **₹43,400** [calc].
   - Spending ₹1,20,000 at ₹374.6 needs 320 clicks/month, i.e. 52% of every listed search clicked [calc]. That isn't possible on exact/phrase intent. The only way the cap gets spent is phrase-match drift into off-target queries, which is the Dec-25 failure mode.
   - The plan itself says demand is narrow (§2, §8 "Google budget may not spend"), yet it still books 40% to Google. K1 at ₹20,000 may not be reached within 30 days, so Google may never get a kill decision.
4. **Recommendation (cap / reallocate)**:
   - Cap Google month 1 at **₹40,000** (₹1,350/day). Hold the other ₹80,000 as **unallocated reserve**, not moved automatically.
   - Lower Google K1 to ₹12,000 so a decision lands inside the window.
   - Pull the Dec-25 search-term report (diagnosis §3 lists it as a pending next step) before finalising the keywords.

### F5. Month-1 budget size isn't justified by the line's economics
1. **Severity**: Major
2. **Affected Scope**: §5 (₹3,00,000 ceiling), §1, §4
3. **Economic Rationale**:
   - To break even, ₹3,00,000 ÷ ₹51,780 = **5.8 incremental won FDI deals per month** [calc]. The whole India-entry line won 20 deals in 12 months (1.7/month).
   - At 15% QL→won that needs **38.6 QLs/month** [calc]. The line's total FDI lead volume from all sources is 92 ÷ 12 = **7.7 leads/month** [calc]. So paid must produce about 5× the line's current total lead flow, as qualified leads, in its first month.
   - Annualised, ₹3L/month = ₹36L, against ≈ ₹9.8L annual margin from the whole line (16,31,480 × 0.6) [calc].
   - The owner's ₹3L is a ceiling, not a target. Nothing obliges the test to spend it.
4. **Recommendation (cut)**: Run month 1 as a capped test of about **₹1.9L committed**: Google ₹40k, Meta US ₹60k (₹2,000/day, the only channel with US QLs), LinkedIn ₹75k, Microsoft ₹15k after UET is verified. Keep about ₹1.1L in reserve, released only by S1/S3 with owner approval. Record the decision in `shared/budget-plan.md`.

### F6. Spread too thin: 6 platforms, about 10 campaigns/ad sets, none can exit learning
1. **Severity**: Major
2. **Affected Scope**: §3 table, §5, §9.3 (2 ad sets on ₹1,500/day CBO), §9.4, §9.5, §9.6
3. **Economic Rationale**:
   - Meta: ₹1,500/day = ₹10,500/week ÷ ₹4,454 per QL ≈ **2.4 QL/week** [calc], split across 2 ad sets and 4 ads. Learning needs about 50 optimisation events per ad set per week. At the US CPM of ₹8,420, ₹1,500 buys ≈ **178 impressions/day** [calc].
   - Expected QLs per platform over 30 days at the ₹6,000 target [calc]: Google (realistic ₹23–43k spend) ≈ 4–7 · Meta 7.5 · LinkedIn 12.5 · Microsoft ≈ 4 · ChatGPT 3.3 · Reddit 2.5. Day-30 decisions would rest on n = 2–7 per platform. S1 scales on n ≥ 3.
   - Effort: 3 new LPs, about 9 new creatives (F1, R1, R2, L1, L2, ChatGPT text, 3 RSA sets), 6 tracking integrations (§6.3), a Zoho classifier change, a new Meta form v2, and a late shift to 23:00 IST. No team-hours estimate is given.
   - The plan has no forecast CPL/CPQL for LinkedIn, Microsoft, ChatGPT or Reddit to compare against break-even. Reviewer's indicative LinkedIn estimate (US senior B2B, CPC ₹700–1,300, 10% form CVR, 50% qualify) [est]: CPQL ₹14,000–26,000, above break-even.
4. **Recommendation (cut)**:
   - Phase 1 = Google (capped), Meta (one ad set: company expansion, B2 + F1), LinkedIn, and Microsoft only once UET is verified.
   - Move Meta "Returning founders" to a day-30 test.
   - Add a forecast CPQL with stated assumptions for each funded platform. Fund LinkedIn only if its forecast is ≤ ₹7,767, or treat it as a capped ₹40k learning budget with K1 at ₹15k.

### F7. ChatGPT Ads and Reddit fail the "capped test with kill rule" check
1. **Severity**: Major
2. **Affected Scope**: §3 P5/P6, §5, §6.3 item 7, §7 K1, §9.5, §9.6
3. **Economic Rationale**:
   - ChatGPT: prior `Advt - ChatGPT` 54 leads / 0 won (business-context). Conversion tracking is "confirm at onboarding" and the CGPTA connector isn't connected, so CPQL can't be reconciled. The Zoho classifier would currently log paid clicks as organic "AI - ChatGPT" (§6.2).
   - Reddit: K1 threshold = full ₹15,000 cap, so there is no stop rule before the money is gone. Expected QLs at target = 2.5 [calc], too few to decide.
   - Both are ₹35,000 combined (11.7%) with the weakest measurement.
4. **Recommendation (cut)**: Take both out of month 1. Re-enter at day 30 only if (a) phase-1 CPQL ≤ ₹7,767 on at least one platform, (b) conversion tracking and Zoho source mapping pass a test click, and (c) K1 is set at ≤ 50% of the cap.

### F8. Test duration conflicts with caps
1. **Severity**: Minor
2. **Affected Scope**: §5 ("30-day test from first delivery") vs ChatGPT and Reddit rows
3. **Economic Rationale**: ChatGPT ₹1,000 × 30 = ₹30,000 against a ₹20,000 cap, so the cap is hit on day 20. Reddit ₹750 × 30 = ₹22,500 against ₹15,000, so the cap is hit on day 20. Staggered starts (weeks 2 and 3) push "month-1" spend into December, which blurs the ₹3L monthly ceiling.
4. **Recommendation (cap)**: Set daily = cap ÷ 30 (₹667, ₹500), or shorten the stated duration. Define month-1 as a calendar window with one end date for every platform.

### F9. GST treatment of the ceiling isn't confirmed
1. **Severity**: Minor
2. **Affected Scope**: §5 header ("excl. GST unless stated")
3. **Economic Rationale**: At 18% GST, cash outlay on ₹3,00,000 = **₹3,54,000** [calc]. Ad services billed by Indian entities (Google India, Meta India, LinkedIn India) carry GST under CGST Act 2017 s.9 / IGST Act 2017 s.5(1). Services from non-taxable-territory suppliers (for example, Reddit or OpenAI billed from abroad) to a registered business attract reverse charge under IGST Act s.5(3) read with Notification 10/2017-Integrated Tax (Rate), entry 1. Input tax credit may be available under CGST Act s.16. Prepaid Meta top-ups include GST upfront. _Verify current rates and notifications on cbic-gst.gov.in before finalising._
4. **Recommendation (proceed)**: Get the owner to confirm whether ₹3L is gross or net of GST, and state the cash figure in §5.

### F10. Placement-waste figure is miscalculated
1. **Severity**: Minor
2. **Affected Scope**: §9.3 ad set 1 ("₹8,056 for 0 leads")
3. **Economic Rationale**: IG Feed 4,643.37 + FB Stories 1,836.81 + IG Stories 1,769.37 = **₹8,249.55** [calc] (diagnosis §2d). Also note that the retained Facebook Feed produced 1 lead for ₹9,274.76, which is no better.
4. **Recommendation (proceed)**: Correct the figure to ₹8,250. Consider Facebook Reels + Instagram Reels only for the first 7 days, and add Facebook Feed only if CPL ≤ ₹4,500.

### F11. Shared budget and KPI files contradict the plan
1. **Severity**: Minor
2. **Affected Scope**: §4, §5 vs `shared/kpis.md`, `shared/budget-plan.md`
3. **Economic Rationale**: `kpis.md` still uses ₹8,750 AOV and 50% margin (domestic CPL ≈ ₹130–135). `budget-plan.md` has an empty 2026-11 row and TODO test rules. The weekly cycle reads these files, so it would judge India-entry against the wrong CPL.
4. **Recommendation (proceed)**: When the plan is approved, add an "India Entry (US)" KPI row (break-even CPQL, target, QL→won assumption) and the 2026-11/12 budget row with caps to both files.

---

## Verdict
Not approvable as drafted: **2 Blockers** (F1 kill rules / max loss, F2 cap mechanics), **5 Major** (F3–F7), **4 Minor** (F8–F11). The main fix is to cut month 1 to about ₹1.9L across 4 platforms, cap Google to its demand, and set kills at the break-even of ₹7,767. That brings the worst-case loss down to about ₹1.9L, with an expected loss well below that.
