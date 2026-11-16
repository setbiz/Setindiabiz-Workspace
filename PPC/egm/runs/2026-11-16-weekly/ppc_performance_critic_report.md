# ppc_performance_critic report: weekly review w/e 2026-11-15

Raw output of the isolated Goldfish subagent (read-only), 16 Nov 2026.

## PPC Performance Critic: REVIEW of `PPC/egm/runs/2026-11-16-weekly/weekly_review.md`

Against the standard `PPC/egm/standards/weekly-review-standard.md`. I re-checked every scorecard figure against `data.md` (T1–T9) and they reconcile: ad-set sums, CTR, CPC, ₹/CRM lead, ₹/QL, the blended rows and the top-up maths are all correct. The problems are in the conclusions drawn from those numbers.

---

### 1
1. **Severity**: Blocker
2. **Affected Scope**: §6 Action 2 (SIB-01 ad set 120240912969640449, ₹2,500 → ₹1,250), §4.3, headline
3. **Finding**: The review's own data does not support this action.
   - **The W cohort hasn't been worked.** "SIB-01 is deteriorating" rests on W leads where 11 of 14 have not been contacted (T4). Of the 3 that were worked, 2 are QL. §4.5 says quality "can't be judged on leads nobody has called", and Action 1 exists to fix exactly that. Action 2 then cuts budget on that unreadable data.
   - **The matured gap is small.** On the matured P cohort, SIB-01 is ₹806 per QL against SIB-02's ₹611, about 1.3×. The 2.5× gap only appears once immature W leads are mixed in.
   - **The same test condemns SIB-04 Form, which is left untouched.** SIB-04 matured P is ₹2,123 per QL, 2.6× SIB-01. Over 2 weeks SIB-04 is ₹20,283 ÷ 7 QL = ₹2,898 per QL [calc], against SIB-01's ₹1,298. Yet the SIB-04 Form ad set keeps its full ₹2,500/day.
   - **The cut is too large.** It is a 50% budget change, beyond the ~20–30% step that avoids resetting learning. At 14 leads a week the ad set is far below Meta's ~50 optimisation events a week, so it is already in Learning Limited.
4. **Recommended Fix**:
   - Hold the decision until the 19 Nov backlog review (Action 1).
   - If the cut must go ahead now, justify it with the evidence that actually supports it: the 90-day CRM figure of 0.25× ROAS (7 won from 687 leads, ₹30,368 on ₹1,20,202, `meta/changelog.md` 2 Nov). Step it by −25% (₹2,500 → ₹1,875), not −50%.
   - Apply the same ₹/QL test to SIB-04 Form. Pull the SIB-04 CRM split by `Meta_Ad_Set`, as T6 does for SIB-02, and rank the two consistently.

### 2
1. **Severity**: Major
2. **Affected Scope**: §6 Action 3 (pause SIB-04 WhatsApp ad set 120247072309210449), §4.4, §3 WhatsApp bullet
3. **Finding**: The ₹1,931 per conversation figure has four problems.
   - **Tiny, non-authoritative sample.** It is n = 2 Meta conversations over 3 delivery days, and Meta is the non-authoritative system here. CRM is the source of truth (`kpis.md`) and shows 4 `Advt - WhatsApp` leads, which would be about ₹965 per lead if all came from this ad set. The review admits the two systems don't reconcile (W 2 vs 4; P 10 vs 1) and then decides on the Meta number anyway.
   - **The CRM count method may be broken.** The 38-value taxonomy in `shared/lead-source-attribution-runbook.md` §2 has no `Advt - WhatsApp` value. CTWA clicks fall through to `Advt - Facebook` (§5 rule 7). So counting WhatsApp leads by `Lead_Source` is probably wrong.
   - **The week is confounded.** The unlogged 12 Nov 06:46 status change on all 10 SIB-04 ads (T3) happened in the middle of a 3-day delivery week. The review flags the change in §3 but never connects it to the WhatsApp reading.
   - **It pauses the best revenue path at the worst time.** In October, WhatsApp was the best SIB-04 path on won revenue (3.0× vs Form 1.55×, `learnings.md`). AOC-4 is due 31 Dec, so this is peak season.
4. **Recommended Fix**:
   - Count SIB-04 WhatsApp CRM leads by `CTWA_Click_ID` / `Meta_Ad_Set`, not by `Lead_Source`, for both P and W.
   - Read P + W together: about ₹8,811 for 12 Meta conversations [calc ₹494.92×10 + ₹3,861.47] ≈ ₹734 each. Set that against CRM leads and won deals.
   - Replace the pause with a −25% budget step (₹2,000 → ₹1,500), plus a creative swap back to a real statutory-deadline hook, citing the GC 05/2026 dates. Re-read after 7 funded days.

### 3
1. **Severity**: Major
2. **Affected Scope**: §6 ranking (Action 4 funding ranked #4), §4.1
3. **Finding**:
   - **Funding is the biggest lever but is ranked fourth.** The account delivered on 3 of 7 days and has been dark since 13 Nov. ₹50,000 of top-ups each lasted ≈1.5 days. Zero delivery costs more than anything in Actions 2, 3, 5 or 6, yet the section is supposed to be ranked by expected impact.
   - **The stop-start damage is never mentioned.** Four interruptions since 27 Oct mean repeated stop-start pacing on every ad set. That learning-phase damage is missing from the diagnosis.
4. **Recommended Fix**:
   - Rank funding #1.
   - Fix the funding model, not only the amount: an automatic payment method or threshold billing if the INR account is eligible, otherwise one top-up sized to 7 days of active budgets.
   - Don't make budget or status edits on the same day the account restarts, so each reset is isolated.

### 4
1. **Severity**: Major
2. **Affected Scope**: §6 Action 6 (no change to SIB-02), Actions 2 and 3
3. **Finding**: Money is cut but never moved.
   - **It breaks the budget rule.** `budget-plan.md` says "Move budget toward the lowest cost per qualified lead". The review cuts ₹3,250/day and moves none of it to the best entity in the account: SIB-02 Lists, ₹493 per QL and a 60% QL rate (T6).
   - **Two numbers that decide the Lists question are missing.** There is no frequency figure, and Lists has the highest CPM of any active ad set at ₹284.51, which suggests saturation. There is also no check on whether Lists QLs are existing clients who would have bought anyway. That is an incrementality question.
4. **Recommended Fix**:
   - Report frequency for both SIB-02 ad sets.
   - De-duplicate Lists QLs against Zoho Contacts/Accounts.
   - If frequency is below about 3 per week and most QLs are new, step Lists up +20% (₹3,000 → ₹3,600), funded from the SIB-01 / SIB-04 WhatsApp steps.
   - Correct the risk column ("None"). A customer-list ad set carries the open list-basis compliance question (PPC/CLAUDE.md: the website notice doesn't cover ad targeting). Route any increase through §7.

### 5
1. **Severity**: Major
2. **Affected Scope**: §5 row 2 (SIB-04 relaunch package verdict)
3. **Finding**:
   - **The verdict contradicts its own test.** The expected result was "Annual-filing leads at ≤ the October cost". October Form cost was ₹21,559 ÷ 59 = ₹365 per lead [calc, `learnings.md`]. P was ₹422 and W was ₹528, so both fail, yet the verdict reads "Form acceptable".
   - **The cause can't be isolated.** The package bundled 5 simultaneous changes (reactivation, layer-2, age 25–55, GC05 creative, GST-Company list), so nothing can be attributed. Even so, §4.4 singles out GC05 as the hypothesis, with no age split to rule out the 46–55 expansion.
4. **Recommended Fix**:
   - Restate the verdict as "Form fails the cost target (+45% vs October); WhatsApp fails".
   - Pull an age breakdown (25–45 vs 46–55) and an ad-level breakdown for both SIB-04 ad sets before naming a cause.

### 6
1. **Severity**: Major
2. **Affected Scope**: §5 "Learning recorded?" column
3. **Finding**: Rows 1 and 2 say "Proposed below", but none of Actions 1–7 proposes a `shared/learnings.md` entry. The standard (§5) requires outcomes to be moved into learnings.
4. **Recommended Fix**: Add an action with draft learnings rows for:
   - SIB-01: the budget cut was not tested (reverted 4 Nov).
   - The SIB-04 relaunch package: fails the cost target, causes confounded.
   - SIB-02: Lists beat Interest on ₹/QL (₹493 vs ₹679, n = 42 vs 14, directional).

### 7
1. **Severity**: Major
2. **Affected Scope**: §4 What changed and why (whole section)
3. **Finding**: The diagnosis stays at ad-set level. The standard (§4) asks for actual drivers: placements, audiences, creatives and auction metrics. None are given:
   - no ad or creative breakdown (10 SIB-04 ads, multiple SIB-02 ads)
   - no placement or age breakdown
   - no frequency
   - no Instant Form type
   - Meta CTR of 0.62–0.73% across every campaign is never examined
4. **Recommended Fix**: Pull an ad-level table, plus placement, age and frequency breakdowns per active ad set, for the 3 delivery days. State the form type (More Volume vs Higher Intent) per ad set.

### 8
1. **Severity**: Major
2. **Affected Scope**: §6 (bigger lever ignored), SIB-01 / SIB-04 lead quality
3. **Finding**: Both "quality" problems are answered with budget cuts. The cheaper quality levers are missing:
   - switch SIB-01 / SIB-04 forms to the Higher Intent type, or add one qualifying question
   - send the CRM QL stage back to Meta (conversion-leads optimisation) so the algorithm learns from qualified leads, not raw form fills. At the current cohort size (22 QL/week), the account is optimising on the wrong event.
4. **Recommended Fix**:
   - Propose a Higher Intent form test on SIB-01 in place of the budget cut. It is one change, reversible, and leaves budget alone.
   - Propose a scoped plan to return CRM stages to Meta via CAPI. This is a personal-data upload, so it needs a recorded basis under IT Act 2000 s. 43A + SPDI Rules 2011 r. 5 (the DPDP Act 2023 phases in from ≈13 May 2027; verify on meity.gov.in). It goes in §7.

### 9
1. **Severity**: Major
2. **Affected Scope**: §3 ChatGPT bullet, §6 Action 5 (kill rule), §1 provenance
3. **Finding**: The ChatGPT numbers aren't yet good enough to run a kill rule on.
   - **The CRM bucket may be wrong.** The live classifier sends `utm_source=chatgpt` / chatgpt.com traffic to `AI - ChatGPT` (runbook §5 rule 4), and the runbook taxonomy has no `Advt - ChatGPT` value. That conflicts with `business-context.md`. So the "5 CRM leads" and the kill rule may be measuring a bucket the workflow doesn't populate.
   - **"Now measurable" is an overclaim.** There are 2 platform conversions against 5 CRM leads, and conversion tracking is still TODO in `chatgpt-ads/README.md`.
   - **The reactivation is unlogged.** `chatgpt-ads/changelog.md` is empty, yet the review flags only the Meta unlogged change.
   - **Budget and status are missing.** No daily budgets or status dates are given. ₹302/day sits below the reported ≈₹725/day minimum and the ₹500/day per campaign used in October, which suggests a partial-week start.
   - **The rule can trip for the wrong reason.** "0 CRM QL" depends on sales working 4 unworked leads, so it can fire because nobody called them.
   - **Won deals are ignored.** The 12-month history is 54 leads and 0 won, so won deals should anchor the rule, not QL alone.
4. **Recommended Fix**:
   - Count both `AI - ChatGPT` and `Advt - ChatGPT` leads in W, split by `UTM_Campaign`.
   - Log the reactivation date, operator and budgets in `chatgpt-ads/changelog.md`.
   - Reword the rule: pause if 0 QL once at least 10 ChatGPT leads have been worked, or after a further ₹5,000, whichever comes later; and pause regardless if there are 0 won deals by a set date.

### 10
1. **Severity**: Major
2. **Affected Scope**: §3 "Meta forms → CRM: OK"
3. **Finding**:
   - **The reconciliation mixes channels.** It compares 57 Meta leads with 58 CRM leads, but the CRM figure includes WhatsApp. Form against form, Meta shows 57 (24+8+11+14, T2) and CRM shows 54 (`Advt - Facebook` + `Advt - Instagram`, T4): 3 form leads are missing. SIB-02 alone is 32 vs 31.
   - **Tracking status is absent.** There is no Pixel/CAPI status (standard §3; `meta/README.md` still TODO).
   - **The SIB-05 anomaly isn't flagged.** SIB-05 ran at a CPM of ≈₹3,356 and a CPC of ₹654, 12–26× the rest of the account (T2).
4. **Recommended Fix**:
   - Reconcile per campaign and per channel (form vs CTWA) and name the gap.
   - Add Pixel/CAPI status from `ads_get_dataset_quality`, or mark it "not checked".
   - Confirm the SIB-05 spend from its three ad sets directly, or label the anomaly.

### 11
1. **Severity**: Nit
2. **Affected Scope**: §6 Actions 2–4, "Expected impact"
3. **Finding**: "Saves ₹8,750/week" and "₹14,000/week" are not savings in a prepaid, top-up-limited account. They change the spend mix and how long a top-up lasts. Meta can also overspend the daily budget: on 12 Nov it spent ₹16,571.93 against about ₹15,000 of active budgets including SIB-05 [calc]. A top-up of exactly 7× the daily budget can therefore run out unevenly.
4. **Recommended Fix**: Reword the impact as "₹/QL mix shift" and add a 10% buffer to the top-up figure.

### 12
1. **Severity**: Nit
2. **Affected Scope**: §3 unlogged change, §5 row 1, Action 7
3. **Finding**:
   - The owner's 4 Nov SIB-01 restore to ₹2,500 is also missing from `meta/changelog.md` on main, which still shows ₹1,250 "published".
   - T3 says "all 10 SIB-04 ads", but the changelog accounts for 8 (6 old + 2 GC05). Two ads are unaccounted for.
4. **Recommended Fix**: Extend Action 7 to log the 4 Nov restore and to identify the 2 extra SIB-04 ads.

### 13
1. **Severity**: Nit
2. **Affected Scope**: §1 provenance, §2 scorecard
3. **Finding**:
   - The ChatGPT, Google and Microsoft rows have no pull time.
   - CPA and ROAS are "n/a" with no rolling view. `learnings.md` says to judge every channel on CRM won deals, and T7 shows a SIB-02 ₹2,500 deal moved back from W-Login to Qualified, so SIB-02 may have 0 confirmed wins in November.
4. **Recommended Fix**:
   - Add pull times to every row.
   - Add a rolling 30-day won-deal count, ₹ and CPA per campaign (by `Meta_Campaign`) to the scorecard, labelled directional.

---

**Summary:** 1 Blocker (Action 2 has no data justification and contradicts SIB-04's treatment), 9 Major, 3 Nit.

The arithmetic is clean. The faults are in what the actions rest on:
- **The wrong metric:** immature QL, and Meta counts instead of CRM.
- **The wrong order:** funding is ranked fourth.
- **The wrong lever:** budget cuts are used where form type, CRM feedback or reallocation to SIB-02 Lists would do more.

Reviewed read-only: nothing was edited and no ad-platform or CRM tool was called.

Files reviewed (all under `/home/user/setindiabiz-workspace/PPC/`):
- `egm/runs/2026-11-16-weekly/weekly_review.md` and `data.md`
- `egm/standards/weekly-review-standard.md`
- `shared/` (all files)
- `meta/README.md`, `meta/changelog.md`
- `chatgpt-ads/README.md`, `chatgpt-ads/changelog.md`