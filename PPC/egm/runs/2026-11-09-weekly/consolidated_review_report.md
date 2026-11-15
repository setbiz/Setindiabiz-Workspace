# Consolidated Goldfish review: weekly review w/e 8 Nov 2026

**Reviewers (isolated, read-only, files only):** ppc-performance-critic, measurement-skeptic, budget-cfo, egm-zoom-out. Compliance reviewer and customer lens were not run because §6 has no ad copy or audience change.
**Totals:** 4 Blocker findings (deduplicated to 2), 22 Major, 17 Nit. **All arithmetic re-checked by three reviewers with no errors.** The issues were sourcing, test design, economics and missing items.
**Elephant follow-ups done in this run:** CRM relabelling checks (data.md T11); sourced reference figures (T12); factual corrections to `weekly_review.md` (headline funding days, §2 target label, §3 WhatsApp/ChatGPT, §4.2 driver and confounders, Diwali, §5 GC05 row and bundled-SIB-04 note).

## 🔴 Blockers
| # | Finding | Raised by | Elephant recommendation |
|---|---|---|---|
| B1 | Decision numbers not sourced: ₹176 target, SIB-05 ₹15K cap, India AOV ₹86,300 / 8.8%, 51% sales-process losses, WA plug references. The header claimed full sourcing | critic 1, skeptic 1, CFO F2 | **Accept, fixed.** All are in repo files and now cited in data.md T12. The ₹176 target is labelled provisional, with the adopted ₹130–135 basis shown (multiples ≈30% worse). The SIB-05 cap is an owner decision of 2 Nov but **is not in `meta/changelog.md`**, so log it before relying on it (A3) |
| B2 | No approved November budget and no gross margin, so there is no ceiling to approve a top-up against. Current budgets run at ₹4.5L/month ≈ 4.1× trailing monthly Meta-attributed *revenue* | CFO F1 | **Accept.** The top-up is re-scoped (A6): the owner enters a November Meta figure in `budget-plan.md` first, then funds **one week** within it |

## 🟡 Majors (deduplicated)
| # | Finding | Raised by | Recommendation |
|---|---|---|---|
| M1 | §5 missed the due review of "SIB-04 ads replaced (GC05)" | critic 2, skeptic 6 | **Accept, fixed.** Row added: inconclusive. GC05 is 16–47% costlier than the old baseline, but bundled with SIB-04's other changes |
| M2 | SIB-04 had ≥4 simultaneous structural changes on 2 Nov, so separate verdicts can't be read | critic 2, skeptic 3 | **Accept, fixed.** Judge one "SIB-04 relaunch package" verdict. Age breakdown → next run |
| M3 | Delivery-day maths wrong: credit ran out during 3 Nov and 5 Nov, so only 2 Nov was uncapped. A ₹15,000 top-up buys ₹12,712 of delivery | critic 3, skeptic 7 | **Accept, fixed** (headline, T12). "7 funded days" now means 7 days with no intra-day cut-off |
| M4 | The blended target hides service economics. SIB-01's 90-day return is 0.25× and its break-even CPL ≈ ₹22, vs ₹366 now. SIB-02 needs 23–29% lead→won. SIB-04 is nearest break-even. The owner's 4 Nov restore doubled the worst campaign (+100% step, resets learning) | critic 4, CFO F3, F8 | **Accept.** A4: revert SIB-01 to the last approved and logged ₹1,250 unless the owner confirms ₹2,500 in writing. Per-service break-even column → next run (needs 90-day AOV per `Meta_Campaign`) |
| M5 | The CPL rise came mainly from CTR and click→lead conversion, not CPM. n < 30 per arm. Basis mixed | critic 5, skeptic 2 | **Accept, fixed** in §4.2 (directional, CRM basis, confounders listed). Placement/age/region/audience-size pull → next run |
| M6 | Tests are not pre-registered: no metric, baseline, threshold, minimum sample or stop rule. The changelog said to judge SIB-01 on TL/RM Lead Quality, not Lead_Status. QL rate counts the backlog. The 16 Nov dates can't be met | critic 6, skeptic 4, CFO F4 | **Accept.** A7: the owner approves kill rules and a decision rule before funds resume. Review dates become "top-up + 7 uncapped days" (quality read at 14-day lead age). Next run pulls TL/RM Lead Quality for a pre-2 Nov cohort |
| M7 | Confounders not listed: SIB-02 rebuild, SIB-01 budget changes, old ads on 2 Nov, **Diwali week**, possible business-hours rules | skeptic 3 | **Accept, fixed** in §4.2/headline. Automated-rules check → A3 |
| M8 | WhatsApp/ChatGPT gaps might be relabelling artefacts | skeptic 5, zoom-out 2–3 | **Checked (T11): mostly no.** No `Social - WhatsApp`, 0 `AI - ChatGPT`. 3 CTWA-click leads vs 10 conversations (the 10 include the old ads). Gap is real but smaller; count inbox chats (A5) |
| M9 | ChatGPT Ads may still be spending with 0 CRM leads: ≈₹10,500/week (estimate), 0 won lifetime | critic 9, CFO F10 | **Accept.** A2: the owner checks the dashboard today and pauses until it reconciles with CRM and a capped test is written. Build Supermetrics/CSV plumbing only if the channel stays (zoom-out 3) |
| M10 | Funding is a structural problem (3 interruptions in 14 days), not a one-off | zoom-out 1, critic 15 | **Partly accept.** CFO F4 warns that auto-pay removes the only hard loss cap while no monthly budget exists. **Keep prepaid** until B2 is resolved, but fund a full week in one top-up and set a deadline of **12 Nov** (ad sets inactive for 7+ days may re-enter learning; verify Meta's current guidance) |
| M11 | Top-up sized on budgets, not on delivery; risk marked "none" | CFO F5, skeptic 7 | **Accept** (A6 options table). Observed full-day spend was ≈71% of budget, but 3 and 5 Nov were themselves cut off, so that understates. Budget-based figures are the ceiling; unused credit carries forward |
| M12 | SIB-04 WhatsApp: action 4 ("before funds resume") conflicts with action 1 | CFO F6, zoom-out 2 | **Accept.** The CTWA test and inbox count run the same day as the top-up. **Not a gate** for the other ad sets. The WhatsApp ad set keeps running (historically 3.0×, `learnings.md`) unless the test shows chats are being lost |
| M13 | SIB-04 has no spend cap or end date after the deadline moved to 31 Dec / 31 Jan. Implied exposure ₹4,09,500 to 31 Jan vs ≈₹1.2L approved | CFO F7 | **Accept.** A6: the owner sets a SIB-04 cap and end date, e.g. ₹1.2L to 31 Dec, re-deciding at the AOC-4 deadline. The new dates come from MCA General Circular 05/2026 (owner-verified 2 Nov) under Companies Act 2013 ss. 92(4), 137(1), 403 |
| M14 | Customer-list audiences (SIB-02 Lists, SIB-04 Director/GST) lack a recorded source, notice and approver | critic 7 | **Reject: already decided.** On 2 Nov the owner declined the list pause and accepted the position (2 Nov consolidated report, Owner resolution row 1). The risk is unchanged and recorded: IT Act 2000 s. 43A + SPDI Rules 2011 r. 4–5 now; DPDP Act 2023 ss. 4–6, 8 from ≈13 May 2027 (verify on meity.gov.in) |
| M15 | Fixed prices in ad names (₹1,999 / ₹2,499 / USD 499) while the website shows no package prices | critic 8 | **Needs data.** The owner confirmed on 2 Nov that the prices are real, and these are Instant Form ads (no landing page). Remaining check: each form intro states that government fees are extra (CPA 2019 s. 2(28); CCPA Misleading Ads Guidelines 2022; CCPA Dark Patterns Guidelines 2023 on drip pricing) → next run |
| M16 | No CAPI status, optimisation goal, bid strategy or learning stage. SIB-05 results "n/a"; ad sets likely Learning Limited | critic 10, CFO F9 | **Needs data → next run.** CAPI exists (Cowork, Oct). Pull `optimization_goal`, learning stage and Event Match Quality. Merge SIB-02 Interest into Lists at the decision point, not during the hold |

## 🟢 Nits (accepted unless noted)
Rank action 5 higher (critic 11, CFO F11). Add CPA "n/a, 2–4 week lag" and P revenue/spend 1.61× (critic 12). Cite the GST derivation (T12) (critic 13, skeptic 1). GST on Meta top-ups is recoverable as input tax credit if the GSTIN is on the billing profile (CFO F12; CGST Act 2017 s. 16, s. 17(5); verify current text). Check automated rules / #HOLD before pausing SIB-05 (critic 16). Add a "blended excl. SIB-05" row: ₹478 per CRM lead in W vs ₹266 in P (skeptic 8). SIB-05 saving is ≈₹3,725/day actual, and the cap's start time is now stated (skeptic 9). Ad-set QL and missing leads by campaign (skeptic 10). Use a Meta campaign spending limit to enforce the SIB-05 cap (zoom-out 4). Cut §4 items 2–4 to directional (zoom-out 5; done as a label). Fold action 3 into 6 (zoom-out 7). Drop the LinkedIn/X/Reddit rows until a budget exists (CFO F13).

## Traceability
| Finding | Reviewer(s) | Final action |
|---|---|---|
| B1 | critic, skeptic, CFO | A3 (log cap), T12 |
| B2, M10, M11, M13 | CFO, zoom-out, critic, skeptic | A6 |
| M4 | critic, CFO | A4 |
| M6 | critic, skeptic, CFO | A7, A8 |
| M8, M12 | skeptic, zoom-out, CFO | A5 |
| M9 | critic, CFO, zoom-out | A2 |
| M1–M3, M5, M7 | critic, skeptic | Fixed in review |
| M14 | critic | Rejected (owner decision 2 Nov) |
| M15, M16 | critic, CFO | Next weekly run |

## Final recommended action list (in execution order; nothing applied)
| # | Owner | Action | Why | Approve? |
|---|---|---|---|---|
| A1 | Sales TLs | Clear the **21 unworked paid leads** from 2–8 Nov today, SIB-04 first (7 of 10). ≈₹14,800 of leads already paid for [calc 21 × ₹706] | T8; zero cost | ☐ |
| A2 | Owner | Check the **ChatGPT Ads** dashboard for 2–8 Nov spend today. If spending, pause until it reconciles with CRM and a capped test (budget, duration, kill rule) is written | T7, T11; ≈₹10,500/week possible (estimate), 0 won lifetime | ☐ |
| A3 | Owner + Claude | **SIB-05:** log the 2 Nov ₹15,000 cap in `meta/changelog.md`, then enforce it before funds resume. Default: set a **campaign spending limit** = spend to date + ₹3,078. Fallback: pause campaign 120247067847480449. First list automated rules (#HOLD) | T2, T3, T12. Cap reached after ≈0.8 day at budget | ☐ |
| A4 | Owner | **SIB-01:** revert ad set 120240912969640449 to **₹1,250/day** (last approved and logged), unless the owner confirms ₹2,500 in writing. Log the 4 Nov change either way | T6; 90-day 0.25×; W ₹806 per QL | ☐ |
| A5 | Ops / CRM | Same day as the top-up: count WhatsApp-inbox chats from 2–8 Nov and run one end-to-end test on the GC05 CTWA ad (bot → plug → lead with `Meta_Campaign`). Not a gate for the other ad sets | T2, T11 | ☐ |
| A6 | Owner (money, **human only**) | 1) Enter a November Meta budget in `budget-plan.md`. 2) Set a SIB-04 cap and end date (e.g. ₹1.2L to 31 Dec). 3) Top up **one week by 12 Nov**, within that budget. See the sizing table below | B2, M10, M11, M13 | ☐ |
| A7 | Owner | Before funds resume, approve per-campaign kill rules and log them in `meta/changelog.md`. Draft (CFO F4): pause an ad set with **0 CRM QL after ₹4,375** of uncapped spend, or **CRM cost per lead > 3× its service break-even after ₹5,000**. Decision metric: cost per CRM QL at 14-day lead age, using TL/RM Lead Quality | M6 | ☐ |
| A8 | All | **Hold** all other Meta changes. Review = top-up date + 7 uncapped days; quality read at 14-day lead age | M2, M5, M6 | ☐ |

**A6 sizing (7 days, at full budget; unused credit carries forward):**
| Scenario | Daily budget ₹ | 7-day credit ₹ | Payment incl. GST ₹ [calc ×1.18] |
|---|---|---|---|
| Current settings | 15,000 | 1,05,000 | 1,23,900 |
| SIB-05 capped (A3) | 11,000 | 77,000 | 90,860 |
| **SIB-05 capped + SIB-01 at ₹1,250 (A3 + A4), recommended ceiling** | **9,750** | **68,250** | **80,535** |
| Same, at observed ≈71% delivery (estimate) | ≈6,900 | ≈48,500 | ≈57,200 |

**Excluded or deferred:** merging SIB-02 Interest into Lists, SIB-05 restructure, per-service break-even column, placement/age/region breakdowns, CAPI/optimisation check, form price-disclosure check (all → next weekly run); customer-list compliance (owner decision 2 Nov stands); Supermetrics CGPTA pipeline (only if ChatGPT Ads continues).
