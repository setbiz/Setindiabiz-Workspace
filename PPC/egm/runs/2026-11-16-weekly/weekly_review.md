# Weekly PPC Review — week ending 2026-11-15

Elephant draft, scheduled run of 16 Nov 2026. Read-only: no ad account was changed. Numbers come from `data.md` (T#). `[calc]` = computed here. India Entry (SIB-05) is now run by a dedicated session (PRs setbiz/Setindiabiz-Workspace#2 and #3). It is reported here for completeness only, with no actions.

**Headline:** the Meta account delivered on **3 days (11–13 Nov)** and has been **dark since 13 Nov: prepaid funds are empty** (T1, T3). Every top-up this month has run out within 1.5 days. Despite that, the second matured week confirms the ranking: **SIB-02 Trademark is the only campaign near a workable cost per qualified lead. SIB-01 and SIB-04 are getting worse.** ChatGPT Ads is live again and visible in Supermetrics for the first time.

## 1. Data provenance
| Platform | Source | Date range | Compared with | Pulled at | Missing? |
|---|---|---|---|---|---|
| Meta | Meta Ads connector, 152154124583473 | 9–15 Nov | 2–8 Nov (PR #1) | 16 Nov ≈10:20 IST | No. 3 delivery days |
| CRM | Zoho COQL | Leads created 9–15 Nov; P cohort re-read; deals closed 9–15 Nov | P cohort at 8–14 days | 16 Nov ≈10:35 IST | W leads are 1–7 days old (immature) |
| ChatGPT Ads | Supermetrics CGPTA (newly authenticated) | 9–15 Nov | 2–15 Nov query (P = ₹0) | 16 Nov | No |
| Google / Microsoft | Supermetrics AW / AC | 9–15 Nov | — | 16 Nov | No activity |
| LinkedIn, X, Reddit | Supermetrics LIA / TA / RDA | — | — | — | **Missing**: not authenticated (no live campaigns known) |

## 2. Scorecard
QL = CRM "Valid Lead" + "Proposal Sent". Target cost per CRM lead: **₹130–135** (adopted, `kpis.md`). ₹176 is provisional (PR #1 T12). Margin unconfirmed. W QL is immature, so the matured P figures (T5) are the fairer comparison.

| Platform / campaign | Spend ₹ | Clicks | CTR | CPC ₹ | Platform conv. | CRM leads | ₹/CRM lead | QL | ₹/QL | P matured ₹/QL |
|---|---|---|---|---|---|---|---|---|---|---|
| Meta: SIB-02 Trademark | 8,397.53 | 216 | 0.69% | 38.88 | 32 leads | 31 | 271 | 18 | **467** | 611 |
| Meta: SIB-01 Incorporation | 5,053.80 | 161 | 0.73% | 31.39 | 14 leads | 14 | 361 | 2 | 2,527 | 806 |
| Meta: SIB-04 Annual Filings | 9,668.08 | 315 | 0.62% | 30.69 | 11 form + 2 WA conv. | 13 | 744 | 2 | 4,834 | 2,123 |
| Meta: SIB-05 India Entry (paused 14 Nov) | 6,541.62 | 10 | 0.51% | 654 | 0 | 0 | — | 0 | — | 11,922 |
| ChatGPT Ads (CFO + GST) | 2,114.58 | 254 | 2.39% | 8.33 | 2 | 5 | 423 | 0 | — | (P spend ₹0) |
| Google / Microsoft | 0 | — | — | — | — | 0 | — | — | — | — |
| **Blended (Meta + ChatGPT)** | **31,775.61** | 956 | 0.82% | 33.24 | | **63** | **504** | **22** | **1,444** | P Meta 1,474 |
| Blended excl. SIB-05 | 25,233.99 | 946 | | | | 63 | 401 | 22 | 1,147 | |
All [calc] from T2, T4, T5, T8. P matured ₹/QL uses P spend (PR #1 T1) ÷ P QL now (T5). vs target: blended ₹504 ≈ 3.7–3.9× the ₹130–135 target [calc]. Won (paid Meta, closed in W): 1 deal, ₹1,000, from an old CCFS campaign (T7). CPA n/a (2–4 week lag).

## 3. Tracking health
- **Meta forms → CRM: OK.** 57 Meta leads (incl. form leads) vs 58 CRM leads (FB 20, IG 34, WA 4), all carrying `Meta_Campaign` (T1, T4).
- **WhatsApp:** Meta reports 2 conversations in W; CRM has 4 `Advt - WhatsApp` leads in W. Counts are now the other way round from P (10 vs 1), so the two systems still don't reconcile. The 9 Nov capture test (A5) has not been reported.
- **ChatGPT Ads: now measurable.** ₹2,114.58 spend, 2 platform conversions, 5 CRM leads (T8). P had ₹0 spend, which explains 0 CRM leads in P. No ChatGPT-sourced deal exists since September.
- **Funding:** 4 interruptions since 27 Oct. ₹50,000 added in November across 3 top-ups (₹15,000, ₹10,000, ₹25,000), each used up within ≈1.5 days (T3, PR #1 T6/T12).
- **Unlogged change:** the 12 Nov 06:46 status change on 10 SIB-04 ads by an "ads MCP server" session is not in `meta/changelog.md` on main (T3).

## 4. What changed and why
1. **Delivery was again set by funding**: 3 days, ≈₹29.7k (T1).
2. **SIB-02 holds up on the matured cohort and the new week:** ₹611 per QL (P, matured) and ₹467 (W, immature) (T5, scorecard). **Within SIB-02 the customer-list ad set beats the interest ad set on quality:** 60% vs 36% QL rate, ₹493 vs ₹679 per QL over 2–15 Nov, even though its CPL is higher (₹294 vs ₹242) (T6). That reverses the CPL-only reading in the 12 Nov re-analysis. n = 42 vs 14 leads, so directional.
3. **SIB-01 is deteriorating:** 2 QL out of 14 W leads, and **11 of 14 are not yet worked** (T4). The matured P cohort was 5 of 11 QL. Combined spend 2–15 Nov is ₹9,082.76 for 7 QL = ₹1,298 per QL [calc], 2.5× SIB-02's ₹524 [calc 15,730.39 ÷ 30]. The ₹2,500/day budget (owner restore on 4 Nov) is still in place.
4. **SIB-04 WhatsApp has collapsed:** ₹1,930.74 per conversation in W (₹494.92 in P; ₹336 per chat in the October baseline, `learnings.md`). CPM is the cheapest in the account (₹130) but CTR is 0.45% (T2). *Hypothesis:* the GC05 "fee relief" message lowered urgency for chat-starters. The form ad set is steadier at ₹528 per lead. SIB-04 overall: ₹20,283 over 2 weeks → 23 CRM leads → 7 QL (P 5 matured) [calc].
5. **The sales backlog moved only slightly:** the P cohort went from 21 to 17 unworked in a week; W adds 30 unworked out of 58 (52%) (T4, T5). Lead quality can't be judged on leads nobody has called.
6. **SIB-05** spent ₹6,541.62 for 0 leads before the India-Entry session paused it on 14 Nov with owner approval (T2, T3).

## 5. Due reviews (from changelogs on main)
| Platform | Change (date) | Expected | Actual | Verdict | Learning recorded? |
|---|---|---|---|---|---|
| Meta | SIB-01 budget ₹2,500 → ₹1,250 (2 Nov), review 16 Nov | Lower spend, judge lead quality | Ran ≈2 days; owner restored ₹2,500 on 4 Nov (PR #1 T6). At ₹2,500: ₹1,298 per QL over 2–15 Nov | **Test not run** (reverted). Data since then favours the cut | Proposed below |
| Meta | 2 Nov SIB-04 relaunch package (reactivation, layer-2, age 25–55, GC05 creative, GST-Company list), reviews due 9 Nov | Annual-filing leads at ≤ the October cost | 2 weeks: Form ₹422 → ₹528 per lead; WhatsApp ₹495 → ₹1,931 per conversation; 7 QL from ₹20,283 | **Mixed: Form acceptable, WhatsApp failing.** Won deals still lagging | Proposed below |
| Meta | Layer-2 targeting on all ad sets (2 Nov), review 9 Nov | Higher quality, lower volume | Matured P QL rates: SIB-02 48%, SIB-01 45%, SIB-04 50% (T5). No pre-2-Nov cohort at the same lead age has been pulled | **Inconclusive: no baseline.** SIB-02 works under layer-2; SIB-01 doesn't | Not yet |

## 6. Proposed actions (ranked by expected impact)
| # | Platform | Exact change | Evidence | Expected impact | Risk / reversible? | Review on |
|---|---|---|---|---|---|---|
| 1 | Sales (no ad change) | Work the **47 unworked paid leads** (P 17 + W 30), SIB-01 (15) and SIB-04 (14) first, plus the 4 unworked ChatGPT leads | T4, T5, T8 | Converts leads already paid for. Makes quality readable | None | 2026-11-19 |
| 2 | Meta | **SIB-01 ad set 120240912969640449: daily budget ₹2,500 → ₹1,250** (one change; same as the approved 2 Nov cut) | §4.3, §5 row 1: ₹1,298 per QL vs SIB-02 ₹524 | Saves ₹1,250/day ≈ ₹8,750/week [calc] | Reversible; resets learning on one ad set | 7 funded days after the change |
| 3 | Meta | **Pause SIB-04 WhatsApp ad set 120247072309210449** (status only). Keep the SIB-04 Form ad set running | §4.4: ₹1,931 per conversation in W, CTR 0.45%; WhatsApp→CRM still unreconciled | Saves ₹2,000/day [calc ₹14,000/week] | Reversible. Risk: WhatsApp was the best SIB-04 path in October (3.0×, `learnings.md`) | 7 funded days |
| 4 | Meta (billing, human only) | Set a November Meta budget in `budget-plan.md`, then top up **one week**. After #2 and #3, active budgets = ₹7,750/day → 7 days ≈ ₹54,250 credit ≈ **₹64,015 incl. 18% GST** [calc]. At current settings (₹11,000/day): ₹77,000 credit ≈ ₹90,860 | T2, T3 | First full funded week since October | No performance risk; sets the cash exposure | 2026-11-23 |
| 5 | ChatGPT Ads | No change this week. Write a kill rule into `chatgpt-ads/changelog.md`: **pause both campaigns if 0 CRM QL after a further ₹5,000** | T8: ₹2,115 → 5 leads (4 unworked), 0 deals since September | Caps the downside at ≈2–3 weeks of spend at ₹302/day [calc] | None | When the ₹5,000 is spent |
| 6 | Meta | **No change to SIB-02**: keep Lists (₹3,000) and Interest (₹1,000) as they are | T6: Lists ₹493 per QL, Interest ₹679 | Protects the best performer | None | 2026-11-23 |
| 7 | Process | Log the 12 Nov 06:46 SIB-04 status change in `meta/changelog.md`, name the session that made it, and resolve PR #1 so the 9 Nov decisions (A1–A8) are closed | T3 | Keeps one source of truth | None | Before the next weekly run |

## 7. Needs human decision
1. **November Meta budget and top-up** (action 4). Money movement is human-only. This was open in PR #1 too (Blocker B2 there).
2. **SIB-01 budget cut** (action 2). It reverses your 4 Nov restore.
3. **Pausing SIB-04 WhatsApp** (action 3). It touches the seasonal campaign. AOC-4 for FY 2025-26 is due by 31 Dec 2026 without additional fee under MCA General Circular 05/2026 (owner-verified 2 Nov; Companies Act 2013 ss. 137(1), 403).
4. **ChatGPT Ads kill rule** (action 5).
5. Still open from earlier: gross margin %; whether to adopt ₹176 or keep ₹130–135; customer-list basis (owner decision of 2 Nov stands); the website "18K+" vs ads "25,000+".
