# Budget CFO review: design_draft.md (Google Ads relaunch, TM + Annual Filing)

Reviewer: ppc-budget-cfo (Goldfish, read-only). Inputs: target plan, `egm/standards/campaign-plan-standard.md`, `shared/kpis.md`, `shared/budget-plan.md`, `shared/business-context.md`, `shared/learnings.md`, `google-ads/changelog.md`, `google-ads/reports/2026-11-22-account-audit.md`, `google-ads/history/2026-11-22-session-handoff.md`.

**Arithmetic check:** §4 break-even CPA and CPL ranges are computed correctly from their inputs (e.g. 5,953 × 50% = 2,977; 2,977 × 8% = 238; 7,324 × 3% = 220). The AF total of ₹99,000 (6 × 1,000 + 62 × 1,500) and the grand total of ₹1,41,000 are correct as stated. The problems are in the inputs and in how the targets and rules relate to the break-even figures.

**Verdict:** not approvable for D1 as drafted. There are 3 Blockers.

---

### CFO-1 · Blocker · §4 Unit economics (AOV basis)
**Issue:** The AOV upper bounds most likely include pass-through government fees and GST, which are not margin. That inflates every break-even figure.
**Evidence [calc]:** TM organic AOV ₹5,953 and all-source AOV ₹6,568 are close to professional fee ₹1,999 + govt fee ₹4,500 = ₹6,499 (Trade Marks Rules 2017, First Schedule, as cited in §8). The paid-social AOV ₹2,300 is close to ₹1,999 + 18% GST = ₹2,359. The plan's own caveat says Amount "may include government fees". For AF, the ad price points are ₹4,599 / ₹5,999 / ₹7,999 + GST & ROC fee (§8), but the CRM AOV of ₹12,780–15,265 is 1.6–3.3× those, which fits the bundle caveat. A searcher who clicks a "₹4,599" ad is unlikely to produce a ₹14,647 AOV.
**Impact:** TM break-even CPA on a ₹1,999 fee at 50% margin is ≈ ₹1,000, not ₹2,977. The target of ₹1,500 is 1.5× break-even and the day-28 kill line of ₹3,000 is 3×. For AF at ₹4,599–7,999, break-even CPA is ≈ ₹2,300–4,000, so the target of ₹4,000 sits at or above break-even.
**Fix:** Recompute AOV as professional fee net of govt fees and GST. Use a Zoho fee split, or audit a sample of about 30 won deals per service. For paid search, use the advertised package mix as the base case. Reset the target CPA, target CPL and kill lines from that figure.

### CFO-2 · Blocker · §4 Unit economics (margin)
**Issue:** Gross margin is an unconfirmed 50% [est] (`kpis.md`: "TODO: set after margin confirmed"). Every break-even figure scales with it, and the CFO mandate treats a missing break-even input as a Blocker for a budget decision.
**Evidence:** §4 line 35; `kpis.md` rows 1–2; `business-context.md` "TODO: gross margin %".
**Fix:** The owner states the contribution margin on professional fees for TM and AF before D1. Show the break-even at both that margin and ±10 pts.

### CFO-3 · Blocker · §4 Targets vs §4 assumptions
**Issue:** The target CPL and target CPA contradict the plan's own lead→won range.
**Evidence [calc]:** TM ₹150 / ₹1,500 and AF ₹400 / ₹4,000 both imply a **10%** lead→won rate. The plan's range is 3–8%, and the only paid baseline is Facebook at 3.7%. At 3.7%, TM ₹150 CPL gives ₹4,054 per won deal, above even the inflated ₹2,977 break-even. AF ₹400 CPL gives ₹10,811 per won deal, above the ₹7,324 break-even.
**Fix:** Set target CPL = target CPA × assumed lead→won rate (3.7% base). On the corrected CFO-1 AOV, that is roughly TM ≤ ₹37–55 and AF ≤ ₹85–150 [calc]. State plainly whether those are reachable.

### CFO-4 · Major · §4 / §2 (missing funnel step)
**Issue:** The plan has no click→lead assumption, and the only account data points the other way.
**Evidence [calc from §2 + learnings.md]:** Dec-25 spent ₹99,927 for 4,430 clicks and 84 CRM leads. That is a 1.9% click→lead rate and a **₹1,190 CRM CPL**. To reach a ₹150 CPL at the §4 CPC range of ₹16–60 needs a 10.7–40% click→lead rate, which is 5–20× the history.
**Fix:** Add a click→lead row labelled [est] with a justification for the improvement (intent-only keywords, priced copy). Show the CPL at a realistic rate such as 3–6%. If TM cannot clear break-even on that, cut TM or run it at ₹1,000/day (D2).

### CFO-5 · Major · §5 Budget and cap
**Issue:** The "maximum loss" is not a hard cap.
**Evidence:** §5 itself notes Google can spend up to 2× the daily budget on a given day. "Launch day + 28 days" is 29 days, so TM is ₹43,500, not ₹42,000. With a 25 Nov launch, the month-by-month total is Nov ₹15,000 + Dec ₹81,000 + Jan ₹46,500 = ₹1,42,500 [calc]. Daily overdelivery can bring spend forward and exhaust the prepaid balance early.
**Fix:** Make the prepaid funding the hard cap: fund in tranches tied to the checkpoints, for example ₹40k at launch and the rest only after day 14 passes. Set an end date on TM. Restate the maximum loss as "≤ funded amount".

### CFO-6 · Major · §7 Annual Filing rules
**Issue:** There is no economic kill rule after day 14. About ₹81,000 (₹99,000 − ₹18,000) runs to 31 Jan with only a copy pause on 31 Dec. January (₹46,500) is entirely after the AOC-4 no-fee window and is not judged separately.
**Fix:** Add a 31 Dec checkpoint: pause if cost per won exceeds the corrected break-even, or if won < spend ÷ break-even CPA. January spend needs a fresh owner OK, based on MGT-7-only demand.

### CFO-7 · Major · §7 thresholds vs §4 break-even
**Issue:** The pause thresholds sit above break-even, so a losing campaign survives every checkpoint.
**Evidence:** TM day-14 pause is CPL > ₹300, against a maximum break-even CPL of ₹238. AF day-14 pause is CPL > ₹800, against a maximum of ₹586. The day-7 rules (TM < 10 leads on ₹10k; AF < 8 on ₹8k) tolerate a ₹1,000 CPL. The TM day-28 "continue at ₹1,500–3,000" band is above the paid-AOV break-even of ₹1,150 and has no new cap or end date.
**Fix:** Tie each pause line to the break-even CPL (after CFO-1 and CFO-2). Allow "Continue" only with a new capped amount and a dated review.

### CFO-8 · Major · §7 day-28 decision
**Issue:** The won-deal kill rule is undefined at 0 won, and it ignores the time from lead to close.
**Evidence:** "Kill if cost per won > ₹3,000" has no value when won = 0. `business-context.md` notes that the lead and deal cohorts don't match (Created_Time vs Closing_Date). There is no data on TM sales-cycle length.
**Fix:** State the rule as "kill if won < ⌈spend ÷ threshold⌉" (14 won at ₹42k / ₹3,000). Pull the median lead→close days for TM and AF from Zoho. If the median is over 14 days, use a QL-based proxy at day 28 and confirm on won deals at day 45.

### CFO-9 · Major · §3 / §5 Opportunity cost and portfolio
**Issue:** ₹1.41L goes to a channel with 0 won deals in 12 months, with no comparison to the next-best use of the money.
**Evidence:** Facebook + Instagram produce ≈ 96% of ad-attributed won ₹ (`learnings.md`). Meta WhatsApp for annual filings returned 3.0× [data, n=3]. `budget-plan.md` is empty and `kpis.md` has "Monthly total budget ₹ TODO".
**Fix:** Fill in the November–January `budget-plan.md` row first. Show the ₹1.41L as a share of the total and compare it with Meta AF/TM marginal cost per won deal. Consider AF-only first, with TM deferred or at ₹1,000/day.

### CFO-10 · Major · §8 Cannibalisation and §6 attribution
**Issue:** Organic Google already wins 320 TM and 532 AF deals a year. Paid search with last-touch UTM attribution will claim some of these, so paid economics will look better than the true incremental result. The mitigation ("watch week on week") has no number. Launching without GCLID (D4) leaves UTM-only matching; only 6 of 84 past Google leads had a gclid.
**Fix:** Record the 8-week baseline of weekly `SEO - Google` leads per service before launch. Pre-register a rule: if organic falls by more than X% while paid rises, cut paid on overlapping terms. Discount paid won deals by the measured overlap.

### CFO-11 · Minor · §5 Funds needed / G2
**Issue:** The 2-week funding figure is understated.
**Evidence [calc]:** For 25 Nov–8 Dec: TM 14 × ₹1,500 = ₹21,000; AF 6 × ₹1,000 + 8 × ₹1,500 = ₹18,000. That is **₹39,000**, not ₹30,000–35,000, and up to about 2× on overdelivery days. The current balance is ≈ ₹4,630.
**Fix:** Set G2 to "balance ≥ ₹39,000" (or the CFO-5 tranche amount).

### CFO-12 · Minor · Open decisions D1 / §7 scale rule
**Issue:** D1 calls ₹1.41L a "monthly cap", but it is the total over about 10 weeks. The December peak alone is ≈ ₹81,000. The TM scale condition "≤ ₹1,500 with ≥ 5 won" is redundant: ≤ ₹1,500 per won on ₹42k already means ≥ 28 won. The ₹1,500 line is also above the paid-AOV break-even.
**Fix:** Reword D1 as total and monthly figures (Nov ₹15k / Dec ₹81k / Jan ₹46.5k). Set the scale threshold below the corrected break-even, with a minimum-won count that actually binds.
