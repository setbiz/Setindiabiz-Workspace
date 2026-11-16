# budget_cfo report: weekly review w/e 2026-11-15

Raw output of the isolated Goldfish subagent (read-only), 16 Nov 2026.

CFO REVIEW: `PPC/egm/runs/2026-11-16-weekly/weekly_review.md` (Mode: REVIEW)
Inputs read: target, standard, `data.md`, `shared/` (kpis, budget-plan, business-context, learnings, brand-voice, landing-pages, plus a grep of the runbook and the import file), `meta/README.md` and `meta/changelog.md`, `chatgpt-ads/README.md` and `chatgpt-ads/changelog.md`. Arithmetic check: every scorecard, §4, §5 and §6 figure recomputes correctly from data.md. The findings below are about economics, not arithmetic.

---

### F1
1. **Severity:** Blocker
2. **Affected scope:** All budget decisions (actions 2–6, §7.1). The headline claim that "SIB-02 is near a workable cost per QL".
3. **Economic rationale:** The review never works out a break-even per service. It uses one blanket ₹130–135 target, and it has no break-even per QL at all, so "workable" has no benchmark. Gross margin is still TODO (`kpis.md`, `business-context.md`). The best per-service proxies available in context, at the assumed 50% margin:

| Service | Basis (in context) | Lead→won | AOV ₹ | Rev/lead ₹ | Break-even CPL ₹ | W ₹/lead | Multiple over break-even |
|---|---|---|---|---|---|---|---|
| SIB-01 Incorp. | meta/changelog: 90d, 7 won / 687 leads, ₹30,368 | 1.02% | 4,338 | 44 | **22** | 361 | **16.4×** |
| SIB-02 Trademark | no service history; FB account average | 3.7% | 7,284 | 271 | **135** | 271 | **2.0×** |
| SIB-04 Form | learnings Oct: 3 won / 59, ₹33,500 | 5.1% | 11,167 | 568 | **284** | 528 (Meta) | **1.9×** |
| SIB-04 WhatsApp | learnings Oct: 3 won / 52, ₹52,625 | 5.8% | 17,542 | 1,012 | **506** | 1,931 (Meta) / 965 (CRM 4) | **3.8× / 1.9×** |
| ChatGPT Ads | business-context: 0 won / 54 | 0% | — | 0 | **0** | 423 | ∞ |

Every live campaign is above break-even. SIB-02's ₹271 per CRM lead equals the FB revenue per lead (₹271), so it only breaks even at 100% margin. At 50% it needs lead→won of 7.4% [271 ÷ (7,284 × 0.5)], double the historical rate. The only SIB-02 deal in context is ₹2,500 (T7, and it reverted). If that is typical, break-even CPL is ₹46 [2,500 × 0.5 × 3.7%] and SIB-02 is 5.9× over. Paid-Meta won revenue in November is at most ₹5,500 (T7) against ₹63,559 of Meta spend on 2–15 Nov [33,898.29 + 29,661.03]. The 2–4 week lag is acknowledged.
4. **Recommendation:** **Cap.** Do not approve action 4 as an open-ended top-up until the review adds a per-service break-even table like the one above, labelled as estimates. Also add to §7: (a) gross margin %; (b) trademark AOV from CRM won deals, and whether deal `Amount` includes statutory filing fees (Trade Marks Rules 2017, First Schedule; check the current amended schedule); (c) QL→won rate, so that ₹/QL can be compared with a break-even ₹/QL.

### F2
1. **Severity:** Blocker
2. **Affected scope:** Action 4 (one-week Meta top-up of ₹54,250 credit, ₹64,015 cash) and actions 2, 3, 6 (each says "review after 7 funded days" with no pass or fail threshold).
3. **Economic rationale:** `budget-plan.md` is empty: no monthly cap and no test-budget %. The new spend has a duration (7 days) and an amount, but no kill rule on any ad set. The expected result of the proposed week, using F1 proxies [estimate]:
- SIB-02: ₹28,000 → about 103 leads × ₹271 = ₹28,000 revenue, so about ₹14,000 contribution.
- SIB-01: ₹8,750 → 24 leads × ₹44 = ₹1,071 revenue, so about ₹535.
- SIB-04 Form: ₹17,500 → 33 leads × ₹568 = ₹18,850 revenue, so about ₹9,425.

That totals about ₹47.9k revenue (ROAS 0.88×) and about ₹24.0k contribution on ₹54,250 of spend. **Expected contribution loss is about ₹30.3k for the week** unless lead→won rises well above historical rates.
4. **Recommendation:** **Cap.** Write into `budget-plan.md` a November Meta ceiling: spend to date plus a stated maximum loss. Fund the week as a capped test with these kill rules:
- SIB-02 Interest: pause if ₹/QL is above ₹700 after ₹7,000.
- SIB-04 Form: pause if CRM ₹/lead is above ₹568 (revenue ROAS below 1× at the October conversion rate) after ₹17,500.
- SIB-02 overall: by 7 Dec, the 2–15 Nov cohort must show at least 1 won deal, or SIB-02 drops to ₹2,000/day.
- Account level: no further top-up until won ₹ from the 2–15 Nov cohorts is reported.

### F3
1. **Severity:** Major
2. **Affected scope:** Action 2: SIB-01 ad set 120240912969640449, ₹2,500 → ₹1,250 a day.
3. **Economic rationale:** SIB-01's own 90-day history (meta/changelog) is 0.25× ROAS, ₹44 revenue per lead, and a break-even CPL of about ₹22 at 50% margin. W cost was ₹361 per lead (16.4× over) and ₹2,527 per QL. Halving the budget still spends ₹8,750 a week for an expected ₹535 contribution, an expected loss of about ₹8,200 a week [estimate]. At ₹1,250 a day it produces about 24 results a week (8,750 ÷ 360.99), so it stays learning-limited and the halved test can't be read (see F5). Halving keeps the cost and still won't give a readable result.
4. **Recommendation:** **Cut.** Pause SIB-01, because the owner restored it on 4 Nov and the case against it is now stronger. If the owner keeps it, cap it with a hard stop at ₹8,750 cumulative from the change date, and pause it if the 2–22 Nov cohort has 0 won by 7 Dec. Pausing instead of halving lowers the week's expected loss from about ₹30.3k to about ₹22.1k. Keep the ₹1,250 a day in reserve rather than moving it elsewhere.

### F4
1. **Severity:** Major
2. **Affected scope:** The ranking logic in the headline, §4 and actions 2, 3 and 6. Cost per QL is compared across services with different AOVs.
3. **Economic rationale:** QL is a sales label, not revenue. The only revenue evidence in context reverses the review's ranking:
- SIB-04 has the best history: October ROAS was 1.55× (Form) and 3.0× (WhatsApp), and CCFS was 2.52× (meta/changelog), with an AOV of ₹11–17.5k.
- SIB-02 has no revenue history since the 2 Nov rebuild.
- SIB-01 was 0.25×.

Projected W ROAS at October conversion rates: SIB-04 Form 1.08× [567.8 ÷ 527.87] and WhatsApp 0.52× [1,012 ÷ 1,931]. On revenue per ₹, SIB-04 Form beats SIB-02, even though SIB-02 looks better on ₹/QL (₹467 vs ₹4,834). The `budget-plan.md` rule "move budget toward lowest cost per qualified lead" only works if AOV and QL→won are similar across services, and here they aren't.
4. **Recommendation:** **Reallocate the analysis, not the money yet.** Add an "expected revenue per ₹" column (₹/lead vs revenue per lead for each service) next to ₹/QL. Write the SIB-02 hypothesis explicitly: "layer-2 / Lists leads close at ≥7.4% lead→won", with a test date. Protect SIB-04 Form through the 31 Dec AOC-4 window. Action 3 (pause SIB-04 WhatsApp): **proceed**. W runs at 0.52× projected ROAS, and it's still only 1.05× if CRM's 4 WhatsApp leads are the true count, which is below break-even at any margin under 100%.

### F5
1. **Severity:** Major
2. **Affected scope:** Thin spread across Meta ad sets after actions 2, 3 and 6.
3. **Economic rationale:** Meta's learning phase needs about 50 optimisation events in 7 days (Meta Business Help Center, "About the learning phase"). Weekly results at the proposed budgets, using W cost per result:

| Ad set | Calculation | Results/week | Exits learning? |
|---|---|---|---|
| SIB-02 Lists | 21,000 ÷ 274.25 | 77 | Yes |
| SIB-02 Interest | 7,000 ÷ 226.93 | 31 | No |
| SIB-04 Form | 17,500 ÷ 527.87 | 33 | No |
| SIB-01 at ₹1,250 | 8,750 ÷ 360.99 | 24 | No |
| SIB-04 WhatsApp if kept | 14,000 ÷ 1,930.74 | 7 | No |

That leaves 4 of 5 ad sets learning-limited. On top of that, funding cuts delivered only 3 of 7 days in W, with 4 interruptions since 27 Oct. No ad set gets a clean 7-day window.
4. **Recommendation:** **Cut the number of ad sets.** Pause SIB-01 (F3) and SIB-04 WhatsApp (action 3). For SIB-02 Interest at ₹1,000 a day, the owner should choose between merging it into fewer ad sets and accepting it as permanently learning-limited. Either way, the review should say so rather than reading weekly swings in its ₹/QL as signal. Fund continuously for 7 days or not at all, because a stop-start top-up wastes learning.

### F6
1. **Severity:** Major
2. **Affected scope:** Action 5: the ChatGPT Ads kill rule. `chatgpt-ads/changelog.md` is empty.
3. **Economic rationale:**
- **The bar is too low.** At ₹423 per lead, ₹5,000 buys about 11.8 leads, and a single QL passes the rule. That allows up to ₹5,000 per QL, while the review cuts SIB-01 at ₹1,298 per QL.
- **The history is ignored.** There are 0 won from 54 CRM leads since October. At a 3.7% lead→won rate, 2.0 wins were expected, and the chance of 0 is 0.963^54 ≈ 13%. ChatGPT's break-even CPL in context is ₹0.
- **The duration isn't capped.** "2–3 weeks" assumes ₹302 a day of observed spend [2,114.58 ÷ 7]. The configured budgets aren't recorded anywhere. In October they were ₹500 a day per campaign, and the README notes a reported minimum of about ₹725 a day. At ₹1,000 a day, ₹5,000 runs out in 5 days.
4. **Recommendation:** **Cap, then proceed.**
- Record both campaign daily budgets in `chatgpt-ads/changelog.md`.
- Set a hard cumulative ceiling of ₹7,115 [2,114.58 + 5,000] until the first won deal.
- Kill both campaigns if fewer than 4 QL arrive by that ceiling (₹/QL above ₹1,300, the SIB-01 level the review itself treats as too expensive), or by a fixed date, whichever comes first.
- Work the 4 unworked ChatGPT leads before any further spend.

### F7
1. **Severity:** Major
2. **Affected scope:** Effort vs return: action 4 vs action 1 (sales backlog).
3. **Economic rationale:** W produced 58 CRM leads in 3 funded days, and 30 (52%) are unworked. The P cohort still has 17 unworked after 8–14 days. A full funded week at ₹7,750 a day buys about 157 CRM leads [estimate: 71 + 29 + 33 + 24], 2.7× W volume. At the current sales throughput, most of those purchased leads would go unworked. The 47 unworked leads already represent about ₹18–19k of sunk spend [estimate: 47 × ~₹400 blended per lead].
4. **Recommendation:** **Cap.** Tie the top-up to sales capacity. For example, fund only as many ₹/day as the team can work within 24 hours, or release the full week only once the unworked share is below 20%. Rank action 1 explicitly as the condition for action 4.

### F8
1. **Severity:** Major
2. **Affected scope:** Concentration risk in SIB-02 Lists (action 6, "keep Lists ₹3,000").
3. **Economic rationale:** Lists took 78% of SIB-02 spend on 2–15 Nov [12,336.97 ÷ 15,730.39] and produced 83% of its QL (25 of 30). The workspace guardrail (`PPC/CLAUDE.md`) records that the website form notice ("used only to respond to your enquiry") does not cover ad targeting. It cites IT Act 2000 s. 43A with the SPDI Rules 2011 (r. 4, r. 5) now, and the DPDP Act 2023 ss. 4–6 and 8 from about 13 May 2027 under the DPDP Rules 2025 phased commencement (verify on meity.gov.in). If the list basis has to be withdrawn, SIB-02 falls back to Interest at ₹679 per QL, 38% worse than Lists' ₹493, and the review's best performer weakens.
4. **Recommendation:** **Proceed, with a contingency.** In §7, state that SIB-02's economics depend on the customer-list basis being resolved. Show the fallback ₹/QL, and don't scale Lists above ₹3,000 a day until the source, notice, purpose and approver are recorded.

### F9
1. **Severity:** Major
2. **Affected scope:** SIB-05 India Entry and the staged draft `META_Leads_IndiaEntry_US_Founders_202612` (PR #2), which draw on the same prepaid Meta pool.
3. **Economic rationale:** SIB-05 cost ₹18,464 for 1 QL across P and W [11,922 + 6,542] before it was paused. The review excludes India Entry from its actions, but the draft would spend from the same unbudgeted prepaid funds. The old campaign had a ₹4,000 CBO, which is 52% on top of the proposed ₹7,750 a day. The top-up maths in action 4 assumes it stays off.
4. **Recommendation:** **Cap.** Ring-fence a separate India-Entry line in `budget-plan.md`, with a capped test budget, a duration and a kill rule, before the draft can go live. Say in §7 that activating it would drain the action-4 top-up early.

### F10
1. **Severity:** Nit
2. **Affected scope:** Action 4 cost basis (₹64,015 "incl. 18% GST").
3. **Economic rationale:** GST on Meta advertising is normally recoverable as input tax credit under CGST Act 2017 s. 16(1), subject to the s. 16(2) conditions. Advertising isn't in the s. 17(5) blocked list (check that the current Act text is unchanged). If the company GSTIN is on the Meta billing profile, the P&L cost is ₹54,250. The extra ₹9,765 is a timing item in working capital, not a cost.
4. **Recommendation:** **Proceed.** Show both cash (₹64,015) and net cost (₹54,250), and confirm the GSTIN is on the Meta invoices.

### F11
1. **Severity:** Nit
2. **Affected scope:** SIB-05 W row (₹6,541.62, CPM ≈ ₹3,356), and the blended figures ₹504 per lead and ₹1,444 per QL.
3. **Economic rationale:** The SIB-05 spend, impressions and clicks are all residuals: the account total minus the 5 listed ad sets [29,661.03 − 23,119.41]. That accounts for 22% of W Meta spend, and its CPM is 12–26× the other ad sets (₹130–285). If any other entity spent in W, it is attributed to SIB-05. Blended per-lead cost moves from ₹401 to ₹504 depending on this row.
4. **Recommendation:** **Proceed**, but pull SIB-05 insights directly next run and footnote the method. No current decision depends on it, because the campaign is paused.

### F12
1. **Severity:** Nit
2. **Affected scope:** Channel count: Google, Microsoft, LinkedIn, X and Reddit.
3. **Economic rationale:** Only 2 of the 7 platforms spent money (Meta ₹29,661, ChatGPT ₹2,115). Google and Microsoft show ₹0. LinkedIn, X and Reddit aren't authenticated, and the review lists them as "no live campaigns known", which is an assumption, not a check. Each week the review spends effort on 5 idle channels. Google's history in learnings is ₹99,927 spent for 0 won.
4. **Recommendation:** **Cut.** Put ₹0 lines for these 5 platforms in the November `budget-plan.md`. Do a one-time billing check to confirm they have no spend, then report them as "₹0, budgeted off" instead of "Missing". Concentrating on Meta and capping ChatGPT Ads is the right call: fewer channels, each funded properly.

---
**Summary:** 2 Blockers (no per-service break-even; the top-up has no kill rule and an expected loss of about ₹30k a week), 7 Major, 3 Nit. Proceed: action 1 (work the backlog, ranked first, as the review does), action 3 (pause SIB-04 WhatsApp), action 7. Cut instead of halve: SIB-01. Cap before approving: action 4 (Meta top-up) and action 5 (ChatGPT kill rule).