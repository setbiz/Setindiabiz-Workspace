# measurement_skeptic report: weekly review w/e 2026-11-15

Raw output of the isolated Goldfish subagent (read-only), 16 Nov 2026.

**Measurement Skeptic: REVIEW of `PPC/egm/runs/2026-11-16-weekly/weekly_review.md`**

**What I recomputed and found correct:** The scorecard arithmetic checks out from `data.md`:
- CTR, CPC, ₹/CRM lead and ₹/QL for all four Meta rows, the ChatGPT row, both blended rows and "excl. SIB-05".
- The matured P ₹/QL figures: 611, 806 and 2,123, derived by subtracting W spend from the 2-week totals.
- SIB-02 ₹524 (15,730.39 ÷ 30) and SIB-01 ₹1,298 (9,082.76 ÷ 7).
- T6 Lists vs Interest: 293.7, 242.4, 493.5 and 678.7.
- The top-up credits (÷1.18), the action-4 cash maths (₹54,250 / ₹64,015 / ₹90,860) and the unworked counts (47 = 17 + 30; SIB-01 15, SIB-04 14).

The problems are in how the numbers are interpreted, not in the arithmetic.

---

### 1
1. **Severity:** Blocker
2. **Affected Scope:** §4.4, §6 action 3 (pause the SIB-04 WhatsApp ad set 120247072309210449), §7.3
3. **Finding:** The pause decision rests on **2 Meta-reported conversations** over 3 delivery days. The ₹1,930.74 figure is 3,861.47 ÷ 2.
   - A Poisson 95% interval on 2 events is about 0.24–7.2, so the true cost per conversation could be anywhere from ≈₹536 to ≈₹16,000. This is noise.
   - The CRM, which `kpis.md` names as the source of truth, has **4** `Advt - WhatsApp` leads in W: ₹965 each. In P the platform showed 10 and the CRM 1. The review admits the two "still don't reconcile" and then acts on the platform number anyway.
   - Pooling the two weeks gives P WA spend ≈ 494.92 × 10 = 4,949 plus W 3,861 = ≈₹8,811 for 12 platform conversations (≈₹734 each) or 5 CRM leads (≈₹1,762 each).
   - No QL figure is given for the WA ad set. T4 does not split SIB-04 by ad set.
   - The only downstream evidence on file (`learnings.md`, 2 Nov) shows WhatsApp as the best SIB-04 path: 3.0× vs 1.55× for the form, n = 3.
   - Under the standard, this action is not justified by the data in the document.
4. **Required Evidence or Fix:**
   - Pull SIB-04 CRM leads, QL and Lost by `Meta_Ad_Set` (or `CTWA_Click_ID` not null) for 2–15 Nov.
   - Reconcile the platform WA conversations against the CRM and the CTWA click IDs.
   - Either downgrade the action to "hold and measure", or re-justify it on CRM QL with a stated threshold and enough events.
   - Report the 9 Nov capture test (A5) first.

### 2
1. **Severity:** Major
2. **Affected Scope:** Headline, §4.3, §5 rows 1 and 3, §6 action 2 (SIB-01 ₹2,500 → ₹1,250)
3. **Finding:** "SIB-01 is deteriorating" is driven by the sales backlog, not by evidence about lead quality.
   - 11 of 14 SIB-01 W leads (79%) are unworked. §4.5 of this same review says "Lead quality can't be judged on leads nobody has called".
   - On worked leads, SIB-01 looks like SIB-02:
     - **SIB-01:** W 2 of 3 worked are QL (67%); P 5 of 7 (71%).
     - **SIB-02:** W 18 of 21 (86%); P 12 of 18 (67%).
   - On the matured P cohort, the QL rates are SIB-01 45% (5/11) vs SIB-02 48% (12/25). So §5 row 3's "SIB-02 works under layer-2; SIB-01 doesn't" contradicts the review's own matured numbers.
   - The ₹1,298 figure mixes 5 matured P QL with 2 immature W QL. Its denominator is 7 QL, well under ~30, and it is not labelled directional.
   - Unworked shares differ: SIB-01 has 15 of 25 two-week leads unworked (60%) vs 17 of 56 for SIB-02 (30%). This alone is enough to explain the ₹/QL gap.
   - Action 1 (work SIB-01 leads first, review 19 Nov) and action 2 (cut SIB-01 now) are proposed together, so the cut would be decided before the backlog test that could overturn it.
4. **Required Evidence or Fix:**
   - Compare QL rate among **worked** leads at equal lead age.
   - Sequence action 2 after action 1's 19 Nov re-read, or label it directional with a revert rule (see finding 6).
   - Correct the §5 row 3 wording.

### 3
1. **Severity:** Major
2. **Affected Scope:** §3 "Meta forms → CRM: OK"
3. **Finding:** The 57 vs 58 comparison mixes form leads with WhatsApp leads.
   - The 57 in T1 are form leads only (24 + 8 + 11 + 14 = 57 from T2). The CRM form-equivalent is FB 20 + IG 34 = **54**, so **3 form leads (5%) are missing**.
   - By campaign: SIB-02 has Meta 32 vs CRM 31. SIB-04 has Meta 11 form vs CRM 13 − 4 WA = 9, if all 4 WA leads are SIB-04 (the only WA ad set).
   - Per `shared/lead-source-attribution-runbook.md` §5 and §13, the live classifier has **no `Advt - WhatsApp` value**. CTWA leads (`CTWA_Click_ID`) are written as `Advt - Facebook` (rule 7) or `Social - WhatsApp` (wa.me referrer). The Edit trigger can also overwrite manually set values; the guard protects only `Self -`, `Referral - Clients/Partner/Employee` and `SEO - Zoho Booking`.
   - So the FB/IG/WA split, and with it the WA reconciliation in findings 1 and 4, rests on a labelling path the documentation doesn't describe.
4. **Required Evidence or Fix:**
   - Reconcile by campaign and ad set using `Meta_Ad_ID`, `Meta_Ad_Set` and `CTWA_Click_ID`, not `Lead_Source`.
   - State how `Advt - WhatsApp` gets assigned.
   - Change "OK" to "3 form leads unreconciled" until resolved.

### 4
1. **Severity:** Major
2. **Affected Scope:** §3 ChatGPT bullet, scorecard ChatGPT row, §6 action 5 (kill rule)
3. **Finding:** "ChatGPT Ads: now measurable" overstates what is known.
   - **Classifier:** the runbook's 38-value taxonomy has no `Advt - ChatGPT`. Rule 4 classifies any chatgpt.com / openai.com referrer or `utm_source=chatgpt` as **`AI - ChatGPT`** (organic). Paid ChatGPT clicks are therefore likely to land as organic, and how the 5 `Advt - ChatGPT` leads got that label is unexplained.
   - **Counts:** the platform shows 2 conversions vs 5 CRM leads, unreconciled. `chatgpt-ads/README.md` still has tracking and conversion events as TODO.
   - **P = ₹0:** "P spend ₹0" is inferred from a 2–15 Nov query returning rows identical to W's. That is equally consistent with the early-access source ignoring the date filter.
   - **P CRM count:** "0 ChatGPT CRM leads in P" is not shown as a pulled number anywhere in T8.
   - **Kill rule:** action 5 depends on this measurement.
4. **Required Evidence or Fix:**
   - Pull CGPTA by day.
   - Pull W and P CRM counts for both `Advt - ChatGPT` and `AI - ChatGPT`.
   - Check that the ChatGPT ad URLs carry a UTM that the classifier routes to a paid value.
   - Map the 5 CRM leads to a campaign (CFO vs GST).

### 5
1. **Severity:** Major
2. **Affected Scope:** Headline ("SIB-01 and SIB-04 are getting worse"), §4.3–4.4, §5 row 2
3. **Finding:** The W vs P comparisons are confounded, and none of these is controlled for:
   - **Delivery pattern:** W delivered on 3 weekdays only (Wed–Fri, 11–13 Nov) in a stop-start funding pattern. On 12 Nov, spend of ₹16,572 exceeded the ₹15,000/day combined budget. P had its own funding gaps.
   - **Unlogged change:** at 06:46 on 12 Nov, all 10 SIB-04 ads had their status changed (GC05 Form/CTWA → Active), and the change is not in the changelog. It is unclear what SIB-04 served on 11 Nov.
   - **Deadline relief:** MCA GC 05/2026 moved the deadline and removed the additional fee. That lowers urgency across the whole market, not only in the creative.
   - **Stacked changes:** the 2 Nov package stacked 5 changes on SIB-04: reactivation, layer-2, age band, GC05 creative and the GST-Company list. Nothing measured here can say which one moved the result.
4. **Required Evidence or Fix:**
   - Pull SIB-04 ad-set × ad × day for 9–15 Nov, and the ads' status history.
   - Compare like-for-like delivery days, or state the confounds next to each "worse" claim and label the claims directional.

### 6
1. **Severity:** Major
2. **Affected Scope:** §5 row 2 verdict, §6 actions 2, 3 and 5, headline "workable"
3. **Finding:** Several success measures are undefined, or not applied as pre-registered.
   - **§5 row 2:** the expectation was "≤ the October cost". The October form cost was ₹21,559 ÷ 59 = **₹365 per lead** (`learnings.md`). Form ran ₹422 (P) and ₹528 (W), so it **failed** the threshold in both weeks, yet the verdict is "Form acceptable".
   - **The ₹422 figure doesn't reproduce:** P SIB-04 spend is 20,283 − 9,668.08 = 10,614.92. Less WA P (494.92 × 10 = 4,949.20) leaves form ₹5,665.72, and ÷ 422 gives 13.4 leads, which is not a whole number. One of those P inputs is inconsistent.
   - **"Workable cost per QL"** has no target. `kpis.md` sets only CPL (₹130–135, at an *assumed* 50% margin, TODO) and CPA (≈₹4,375). The review calls the CPL target "adopted", which overstates its status.
   - **Actions 2 and 3:** the review date is "7 funded days", but there is no decision threshold or revert rule.
   - **Action 5 kill rule:** "0 CRM QL after ₹5,000" has no lead-maturity condition. 4 of 5 ChatGPT leads are unworked today.
4. **Required Evidence or Fix:**
   - Restate the row 2 verdict against ₹365.
   - Source the ₹422 figure (the PR #1 table plus the arithmetic).
   - Give each action a primary metric (CRM ₹/QL at ≥ 8 days lead age), a baseline, a threshold and a stop/revert rule.
   - Add "leads ≥ 8 days old and ≥ 80% worked" to the kill rule.

### 7
1. **Severity:** Major
2. **Affected Scope:** §4.6, scorecard SIB-05 row, the "Blended excl. SIB-05" row
3. **Finding:** All SIB-05 W figures are **residuals**: the account total minus the five listed ad sets.
   - Spend: 29,661.03 − 23,119.41 = 6,541.62.
   - Impressions: 106,342 − 104,393 = 1,949.
   - Clicks: 702 − 692 = 10.
   - The implied CPM of ₹3,356 is ≈12× the account average (₹279) and is not plausible for Meta. Any other spending campaign, or a mismatch in attribution date, would be silently booked to SIB-05.
   - The review presents these as measured facts ("spent ₹6,541.62 for 0 leads") without saying how they were derived.
4. **Required Evidence or Fix:** Pull SIB-05 campaign-level insights for 9–15 Nov directly. Until then, label the figures "residual, unverified".

### 8
1. **Severity:** Nit
2. **Affected Scope:** §4.2, §6 action 6 (SIB-02 Lists vs Interest)
3. **Finding:** The comparison is correctly labelled directional (Interest has only 5 QL).
   - The CRM field used to split ad sets isn't named; presumably it is `Meta_Ad_Set`.
   - Unworked shares per ad set aren't shown.
   - Customer-list audiences are existing contacts, so their higher QL rate may be selection rather than incrementality.
4. **Required Evidence or Fix:** Name the field, show unworked leads by ad set, and flag possible CRM duplicates of existing contacts.

### 9
1. **Severity:** Nit
2. **Affected Scope:** §2, §3, §4.4, §5
3. **Finding:** Numbers carried over from PR #1 can't be checked against this run's `data.md` or the GoldfishContext:
   - P WA ₹494.92, form ₹422, the ₹15,000 top-up, "4 interruptions since 27 Oct", P ad-set spends, SIB-05 P ₹11,922, ₹176.
   - The "2–4 week lag" claim behind "CPA n/a" has no source.
4. **Required Evidence or Fix:** Copy the cited PR #1 rows into `data.md` with their table IDs, or cite the file path and table.

### 10
1. **Severity:** Nit
2. **Affected Scope:** §2 scorecard, §1 provenance, §5 "Learning recorded?"
3. **Finding:**
   - The standard requires previous-period figures. The scorecard shows them only for ₹/QL, not for spend, CTR, CPC or CPL.
   - ROAS is omitted. W won ₹1,000 against ₹29,661 Meta spend, and the won-stage definition is itself unstable: T7 shows a deal moved back from W-Login, and the `business-context.md` assumption is still TODO.
   - Google and Microsoft "no rows" is reported as "no activity" without confirming that spend was ₹0.
   - The ChatGPT pull has no timestamp.
   - §5 says "Proposed below" for learnings, but no §6 action writes to `shared/learnings.md`.
4. **Required Evidence or Fix:**
   - Add the P columns and a ROAS line (labelled directional).
   - Confirm ₹0 spend for Google and Microsoft, and add the ChatGPT pull time.
   - Add a §6 action that records the 2 Nov test outcomes in `learnings.md`.

---

**Verdict: FAIL** on one Blocker (finding 1, the WhatsApp pause on n = 2 unreconciled platform events). Findings 2–7 should be fixed before the owner decides on actions 2, 3 and 5.

**Files reviewed:**
- `/home/user/setindiabiz-workspace/PPC/egm/runs/2026-11-16-weekly/weekly_review.md`
- `/home/user/setindiabiz-workspace/PPC/egm/runs/2026-11-16-weekly/data.md`
- `/home/user/setindiabiz-workspace/PPC/egm/standards/weekly-review-standard.md`
- `/home/user/setindiabiz-workspace/PPC/shared/lead-source-attribution-runbook.md`
- `/home/user/setindiabiz-workspace/PPC/shared/kpis.md`
- `/home/user/setindiabiz-workspace/PPC/shared/learnings.md`
- `/home/user/setindiabiz-workspace/PPC/shared/business-context.md`
- `/home/user/setindiabiz-workspace/PPC/meta/changelog.md`
- `/home/user/setindiabiz-workspace/PPC/chatgpt-ads/README.md`