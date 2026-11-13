# budget_cfo report: weekly review w/e 2026-11-08

Raw output from the isolated Goldfish subagent (read-only), 9 Nov 2026.

**Budget CFO review: `PPC/egm/runs/2026-11-09-weekly/weekly_review.md`**
Mode: REVIEW. Context used: target, data.md, `PPC/shared/*`, `PPC/meta/README.md`, `PPC/meta/changelog.md`. Read-only; nothing changed. `[calc]` = my arithmetic from those sources. "Estimate" = depends on an assumption, which is named.

---

### F1
1. **Severity:** Blocker
2. **Affected Scope:** Action 1 (top-up of ₹1,23,900 gross), §7.1, every "vs target" cell
3. **Economic Rationale:** The two inputs needed to approve money are missing:
   - Gross margin % is still TODO (`business-context.md`, `kpis.md`).
   - The 2026-11 row in `budget-plan.md` is blank, and the monthly budget in `kpis.md` is "₹ TODO".

   So there is no ceiling to approve the top-up against.
   - Run-rate at current budgets: ₹15,000/day × 30 = **₹4,50,000/month** [calc].
   - Last 12 months of Meta-attributed won revenue (FB + IG + WA, `business-context.md`): ₹9,83,330 + ₹2,67,688 + ₹52,625 = ₹13,03,643, which is **≈₹1,08,637/month** [calc].
   - The proposed run-rate is therefore **≈4.1×** [calc] the trailing monthly ad-attributed *revenue*, before margin.
   - November cash so far: ₹33,898.29 net spend × 1.18 = **≈₹40,000** [calc] (T4, T6). Action 1 would take it to ≈₹1.64L by 15 Nov, with no approved monthly figure.
4. **Recommendation:** **Cap.** Before any top-up, the owner enters a November Meta budget in `budget-plan.md` and confirms gross margin. Until then, fund one week only, sized as in F5.

### F2
1. **Severity:** Blocker (standard: "an invented or unsourced number")
2. **Affected Scope:** §2 target of ₹176, §4.5 and §7.2 (SIB-05 ₹15,000 cap, AOV ₹86,300, "lead→won ≥ 8.8%"), §4.7 ("≈51% of lost deals"), and the review's own claim that "Every number is in `data.md`"
3. **Economic Rationale:** None of these numbers is in data.md or the GoldfishContext. They are credited to a "2 Nov audit / owner resolution" with no file or section.
   - ₹176 at 50% margin implies revenue per lead of ₹352. `business-context.md` gives ₹269 for FB + IG together [calc: ₹12,51,018 / 4,650], or ₹261 including WA [calc]. The ₹176 basis is therefore **31% looser** [calc] than the only basis on file.
   - The 8.8% cannot be reproduced. ₹86,300 at 50% margin is ₹43,150 per won deal:
     - against the P CRM CPL of ₹2,619 it needs 6.1%;
     - against the W CRM CPL of ₹5,961 it needs 13.8%;
     - on a revenue-only basis (no margin) at ₹5,961 it needs 6.9%.
   - Re-based on the `kpis.md` target of ₹135, the scorecard multiples are worse than shown:

     | Campaign | Review (vs ₹176) | Re-based (vs ₹135) [calc] |
     |---|---|---|
     | SIB-02 | 1.7× | **2.2×** |
     | SIB-01 | 2.1× | **2.7×** |
     | SIB-04 | 6.0× | **7.9×** |
     | Blended | 4.0× | **5.2×** |
4. **Recommendation:** **Cap until sourced.** Either cite the file and section for each number and copy them into data.md, or show both bases (₹135 file basis and ₹176 audit basis) and label ₹176 as unverified. Record the SIB-05 cap in `meta/changelog.md`; it is not there today.

### F3
1. **Severity:** Major
2. **Affected Scope:** Unit-economics gap for SIB-01, SIB-02, SIB-04 and SIB-05. The single blended target hides a 0.98×–16.6× spread across services.
3. **Economic Rationale:** Break-even CPL per service, using the context data and an assumed 50% margin. All figures are directional, with small n.

   | Service | Basis (source) | Break-even CPL | W actual | Multiple | Lead→won needed at W CPL |
   |---|---|---|---|---|---|
   | SIB-01 Incorporation | 90-day: ₹30,368 won / 687 leads = ₹44.2 per lead (changelog) | **₹22** | ₹366 CRM | **16.6×** | 14.1% at T9 AOV ₹5,185; 29.3% at ₹2,499 ad price. 90-day actual: 1.0% |
   | SIB-02 Trademark | Ad price ₹1,999 × 50% × FB 3.7% lead→won; T9 AOV ₹2,250 [₹13,500 / 6] | **₹37–42** | ₹293 CRM | **7–8×** | 26–29% |
   | SIB-04 Form | 30 days: ₹33,500 / 59 leads = ₹568 per lead (learnings) | **₹284** | ₹630 CRM form [₹5,665.79 / 9]; ₹422 Meta ad-level | 2.2× / 1.5× | — |
   | SIB-04 WhatsApp | 30 days: ₹52,625 / 52 chats = ₹1,012 per chat | **₹506 per chat** | ₹495 per chat (T2) | **0.98×** | CRM captures only 1 of 10 chats |
   | SIB-05 India Entry | AOV not in context | not computable | ₹5,961 | — | — |

   SIB-04 is the only service near break-even. SIB-01 is the worst by an order of magnitude: its 90-day return is 0.25× (changelog), yet the owner restored its budget (F8).
4. **Recommendation:** **Reallocate.**
   - Put the week's money first into SIB-04 (seasonal, nearest break-even).
   - Return SIB-01 to ₹1,250 or pause it.
   - Hold SIB-02 at its current budget under a kill rule (F4).
   - Add a per-service break-even column to the scorecard, and in §6 state the lead→won rate that each campaign needs to hit.

### F4
1. **Severity:** Major
2. **Affected Scope:** Uncapped risk in Action 1 ("Risk: none on performance"), Action 6 (hold everything), and the line "Consider a payment method that avoids repeated dark days"
3. **Economic Rationale:**
   - Downside if W economics repeat for a funded week: ₹1,05,000 / ₹706 = 148.7 CRM leads [calc].
     - On the file basis: × ₹269 × 50% ≈ ₹20,000 gross profit, so **≈₹85,000 net loss** (estimate; revenue lags 2–4 weeks).
     - On the ₹176 basis: ≈₹26,200 gross profit, so ≈₹78,800 loss.
   - Prepaid credit is currently the **only** hard loss cap. No campaign has a ₹ stop rule.
   - The 2 Nov layer-2 test has a duration (7 funded days) but no pass/fail ₹ threshold and no kill rule.
   - Switching to a threshold or auto-pay method would remove that cap while there is no monthly budget (F1).
4. **Recommendation:** **Cap.**
   - Keep prepaid funding until F1 is resolved.
   - Write per-campaign kill rules into the changelog before funds resume. Example: pause if there are 0 CRM QLs after ₹4,375 of spend (one `kpis.md` break-even CPA), or if CRM CPL is above 3× the service break-even after ₹5,000.
   - Change Action 1's risk cell to state the ₹ downside.

### F5
1. **Severity:** Major
2. **Affected Scope:** Action 1 top-up sizing
3. **Economic Rationale:** The top-up is sized on budgets, not on observed delivery.
   - Full-day spend averaged ₹10,662 (2, 3 and 5 Nov) [calc], against ₹15,000 of budgets. That is about 71%, so the narrowed audiences are under-delivering.
   - Without SIB-05: ₹21,976.78 / ≈3.2 days ≈ **₹6,868/day** [calc]. That is ₹48,076 net or ₹56,730 gross for 7 days, against the review's ₹90,860. The top-up is **oversized by ≈₹34,000** (estimate). Excluding the one-off ₹2,091 of old ACR spend makes the gap larger.
   - The review's 18% gross-up is supported by the data: the ₹15,000 UPI payment funded exactly ₹1,893.14 + ₹10,818.72 = ₹12,711.86 of billing, which is ₹15,000 / 1.18 [calc]. Its reading that the top-up "lasted ≈1 day at ₹15,000/day" leaves out that GST took ₹2,288.
4. **Recommendation:** **Cap.** Size the top-up to observed delivery plus a buffer: about ₹55,000 net (≈₹65,000 gross), timed to the 16 Nov review. Any credit left over carries forward; an oversized top-up is spend the owner has not decided on.

### F6
1. **Severity:** Major
2. **Affected Scope:** SIB-04 WhatsApp ad set (₹2,000/day). Action 1 and Action 4 conflict on timing.
3. **Economic Rationale:**
   - Action 4 says "Before funds resume", but Action 1 restores this ad set at current settings.
   - W: ₹4,949 bought 10 chats, but the CRM recorded 1 lead.
   - A funded week means ₹14,000 net (₹16,520 gross) [calc] of spend that cannot be measured.
   - This is also historically the best-returning asset (3.0× in the last 30 days, learnings), so cutting it blind is costly too.
4. **Recommendation:** **Proceed, conditionally.** Run the end-to-end CTWA test on the same day, before the top-up. If capture is not fixed, keep the WhatsApp ad set paused while the rest is funded. Either way, write the dependency into §7.

### F7
1. **Severity:** Major
2. **Affected Scope:** SIB-04 Annual Filings has no spend cap or end date.
3. **Economic Rationale:**
   - The 2 Nov reactivation was capped at "≈₹1.2L to 29 Nov" [check: ₹4,500 × 27 days = ₹1,21,500].
   - The GC05 replacement (changelog: MCA General Circular 05/2026 of 24 Oct 2026, as recorded and not independently verified) moves the hook to AOC-4 on 31 Dec 2026 and MGT-7/7A on 31 Jan 2027, with no additional fee.
   - The underlying law: Companies Act 2013 s. 137(1) (AOC-4 within 30 days of the AGM), s. 92(4) (MGT-7 within 60 days of the AGM) and s. 403 (additional fee). Verify the circular's current text on mca.gov.in.
   - At ₹4,500/day from 2 Nov to 31 Jan (91 days), the implied exposure is **₹4,09,500** [calc], against the ₹1.2L that was approved. Removing the late fee also weakens the urgency hook, so the old conversion assumptions may not hold.
4. **Recommendation:** **Cap.** The owner sets a new SIB-04 ₹ cap and end date in the changelog, for example ₹1.2L through 31 Dec with a re-decision at the AOC-4 deadline.

### F8
1. **Severity:** Major
2. **Affected Scope:** SIB-01 Incorporation, Action 3 and §7.3
3. **Economic Rationale:**
   - The owner's unlogged 4 Nov restore (T6) doubled spend on the campaign with the worst economics: 0.25× over 90 days, a break-even CPL of ₹22 against W ₹366 (F3), and a W cost per QL of ₹806.
   - Action 3 already assumes the ₹2,500 test (₹17,500/week) while §7.3 is still asking the owner to decide.
   - The last approved and logged state is ₹1,250 (₹8,750/week). The difference is ₹8,750/week of downside [calc].
4. **Recommendation:** **Cut.** Go back to ₹1,250 unless the owner confirms ₹2,500 in writing, and log it either way. Rewrite Action 3 so it does not depend on that answer.

### F9
1. **Severity:** Major
2. **Affected Scope:** Thin spread across 8 ad sets (5 after SIB-05 is paused)
3. **Economic Rationale:** Meta's guidance is about 50 optimisation events in 7 days to exit the learning phase. Events per funded week at W cost per result and current budgets [calc, estimate]:

   | Ad set | Events per week |
   |---|---|
   | SIB-02 Lists | 73 at budget; ≈44 at observed ₹1,798/day |
   | SIB-02 Interest | 26.6 |
   | SIB-01 | 47.8 |
   | SIB-04 Form | 41.5 |
   | SIB-04 WhatsApp | 28.3 |
   | SIB-05 (CBO across 3 ad sets) | ≈4.7 (≈₹17,160 over 2 weeks, 4 CRM leads, 0 won [calc]) |

   - SIB-02 Interest (CPL ₹263) and Lists (CPL ₹288) cost about the same, so the second ad set splits signal without adding information.
   - SIB-05 can never exit learning on lead optimisation at ₹4,000/day.
   - On the SIB-05 cap: ₹3,078 lasts 0.77 day at ₹4,000/day [calc]. The pause must come before the top-up, as the review already says.
4. **Recommendation:** **Proceed** with the SIB-05 pause (Action 2). At the 16 Nov decision point, not during the hold, merge SIB-02 Interest into Lists. Any SIB-05 relaunch should be one ad set with a logged ₹ cap and kill rule.

### F10
1. **Severity:** Major
2. **Affected Scope:** ChatGPT Ads (Action 7)
3. **Economic Rationale:**
   - This is a paid channel with **unknown spend**. It is missing from the "blended" total, so total paid spend for the week is unknown.
   - The CRM shows 54 leads and 0 won over its life (`business-context.md`, learnings), so revenue per lead is ₹0 and the break-even CPL is ₹0.
   - If the three ₹500/day campaigns from learnings are still live, that is ≈₹45,000/month (estimate) with no cap, duration or kill rule.
   - Action 7 only restores visibility.
4. **Recommendation:** **Cut.** The owner confirms the status and pauses the channel until a capped test is written: budget, duration, and a kill rule such as "0 won from N leads". Spend the effort on connecting CGPTA only if the channel stays.

### F11
1. **Severity:** Nit
2. **Affected Scope:** Action ranking and order (§6)
3. **Economic Rationale:**
   - Action 1, ranked first, spends ₹1.24L with risk marked "none".
   - Action 5 costs nothing and works on ₹14,830 of leads already paid for (21 × ₹706 [calc]).
   - Actions 2, 4 and the SIB-01 decision must logically come before Action 1.
4. **Recommendation:** **Reorder:** 5 (in parallel) → 2 → 4 → SIB-01 decision → 1 (sized per F5) → 6 → 7.

### F12
1. **Severity:** Nit
2. **Affected Scope:** Action 1 cost framing
3. **Economic Rationale:** The economic cost of Action 1 is ₹1,05,000. The ₹18,900 of GST is cash flow and is recoverable as input tax credit if Setindiabiz's GSTIN is on the Meta billing profile and the invoices are B2B (CGST Act 2017 s. 16, conditions in s. 16(2); advertising is not listed as a blocked credit in s. 17(5); verify the current text).
4. **Recommendation:** **Proceed.** Report spend ex-GST and cash separately, and confirm the GSTIN is on the billing profile.

### F13
1. **Severity:** Nit
2. **Affected Scope:** Effort vs return of weekly reporting
3. **Economic Rationale:** Provenance tracks 7 platforms. Five have no activity or are not authenticated, and Meta carries ≈99.9% of ad-attributed won revenue (`business-context.md`).
4. **Recommendation:** **Cut** the reporting rows for LinkedIn, X and Reddit until a budget exists. Record ₹0 for them in `budget-plan.md` (YAGNI for channels).

---

**Arithmetic check:** I recomputed every [calc] in §2–§6 and all match within rounding: the cost per CRM lead and per QL figures, the P comparisons, +100% spend, 0.21× revenue/spend, 94% form match, 44% unworked, 79% for B2, ₹3,078, ₹1,23,900, ₹90,860, 14.6% and 13%. The won-deal totals (₹7,000 / ₹27,369) also check. The errors are in sourcing and economics (F1, F2), not in arithmetic.