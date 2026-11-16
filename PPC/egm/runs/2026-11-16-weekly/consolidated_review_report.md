# Consolidated Goldfish review: weekly review w/e 15 Nov 2026

**Reviewers (isolated, read-only):** ppc-performance-critic (1 Blocker, 9 Major, 3 Nit), measurement-skeptic (1 B, 6 M, 3 N), budget-cfo (2 B, 7 M, 3 N), egm-zoom-out (0 B, 4 M, 6 N). Compliance reviewer and customer lens were not run (no ad copy or audience change proposed). **All arithmetic re-checked by three reviewers with no errors.**
**Elephant follow-ups done in this run** (data.md T10): SIB-04 CRM split by path; SIB-05 direct pull (residual confirmed); ChatGPT by day (restart 14 Nov; P = ₹0 confirmed); ChatGPT relabel check; form-lead reconciliation. Factual fixes made in `weekly_review.md`: headline, §3 forms and ChatGPT, §5 SIB-04 verdict (fails the October target; the "₹422" was ad-level, ad-set level was ₹515), SIB-05 source.

## 🔴 Blockers (deduplicated)
| # | Finding | Raised by | Elephant recommendation |
|---|---|---|---|
| B1 | **Action 2 (SIB-01 −50%) rests on immature data.** 11 of 14 W leads are unworked. On the matured P cohort SIB-01 is ₹806/QL vs SIB-02 ₹611 (1.3×, not 2.5×), and QL among worked leads is similar | critic 1, skeptic 2, zoom-out 2 | **Accept: don't cut on this week's data.** The strong evidence is the 90-day CRM figure: 7 won / 687 leads, ₹30,368 on ₹1,20,202 = 0.25× (2 Nov changelog). CFO says pause; critic says −25%. **Decision moves to 19 Nov**, after the backlog is worked (A2): if SIB-01's QL rate among worked leads stays below SIB-02's, **pause SIB-01** (CFO F3: halving keeps the cost and still won't produce a readable test) |
| B2 | **Action 3 (pause SIB-04 WhatsApp) rests on 2 Meta conversations**, while WhatsApp→CRM doesn't reconcile | skeptic 1 (critic 2, zoom-out 3: Major) | **Partly accept.** The CRM pull (T10a) adds evidence: 2 weeks ₹8,811 → 5 CRM leads, 1 QL, 4 unworked; ₹734 per Meta conversation vs ₹336 in October (2.2×). CFO projects 0.52–1.05× ROAS at October rates and supports the pause. Still small n, peak season, and the WhatsApp leads lack `Meta_Ad_Set`. **Replace the pause with a −25% step (₹2,000 → ₹1,500)**, then decide on 19 Nov after the 4 leads are worked |
| B3 | **No per-service break-even**, so "workable ₹/QL" has no benchmark. Gross margin and per-service AOV are unknown | CFO F1 | **Accept, as estimates.** CFO break-even CPL proxies at an assumed 50% margin: SIB-01 ≈ ₹22 (W ₹361); SIB-02 ≈ ₹135 at FB average AOV, or ₹46 at a ₹2,500 trademark AOV (W ₹271); SIB-04 Form ≈ ₹284 (CRM ₹637); SIB-04 WhatsApp ≈ ₹506 per lead (CRM ₹1,762); ChatGPT ₹0 (0 won / 54). **Owner inputs needed:** gross margin, trademark AOV, whether deal `Amount` includes govt fees |
| B4 | **The top-up has no ceiling and no kill rules.** Expected contribution loss ≈ ₹30k for the proposed week at historical conversion (estimate) | CFO F2 | **Accept.** Funding becomes A1 with a November ceiling and kill rules (A4). Same as Blocker B2 in PR #1, still open |

## 🟡 Majors (deduplicated)
| # | Finding | Raised by | Recommendation |
|---|---|---|---|
| M1 | Funding is the precondition for everything but was ranked 4th; one-week top-ups keep failing | all four | **Accept.** A1, funded continuously (no stop-start), sized to sales capacity (M2) |
| M2 | Buying leads faster than sales can work them: 47 unworked, a funded week ≈ 157 leads | CFO F7, zoom-out 1 | **Accept.** A1 is gated on A2 (unworked share < 20%), or budgets are sized to what the team can call within 24 h |
| M3 | Cost per QL compares services with very different AOVs. On October revenue rates, SIB-04 Form (1.08×) beats SIB-02 | CFO F4 | **Accept.** Add an "expected revenue per ₹" column next run. Protect SIB-04 Form through the 31 Dec AOC-4 window. State the SIB-02 hypothesis: Lists/layer-2 leads must close at ≥ 7.4% lead→won |
| M4 | Money is cut but not moved; SIB-02 Lists is the best ₹/QL | critic 4 | **Not now.** Concentration and compliance risk: Lists is 78% of SIB-02 spend, and the list basis is unresolved (CFO F8; IT Act 2000 s. 43A + SPDI Rules 2011 r. 4–5 now; DPDP Act 2023 from ≈13 May 2027). No scaling until the list basis is recorded and frequency and duplicates are checked (next run). Savings stay in reserve |
| M5 | Better quality levers than budget cuts: Higher Intent form type; send CRM QL back to Meta | critic 8 | **Accept as an option.** A6: Higher Intent form test on SIB-01 if the owner keeps it after 19 Nov. CRM-stage CAPI already exists (Cowork, Oct); check its event health next run |
| M6 | §5 SIB-04 verdict contradicted its own target; "₹422" didn't reproduce | critic 5, skeptic 6 | **Accept, fixed.** Both paths fail the October target |
| M7 | No learnings action | critic 6, zoom-out 9 | **Accept.** A7 drafts `learnings.md` rows |
| M8 | Diagnosis lacks ad, placement, age, frequency and form-type drivers | critic 7 | **Accept → next run** (pull per ad set) |
| M9 | ChatGPT measurement overclaimed; kill rule too loose; restart unlogged | skeptic 4, critic 9, CFO F6 | **Accept, partly resolved** (T10c–d). A5: log the restart and budgets; ceiling ₹7,115 cumulative [2,114.58 + 5,000]; kill if < 4 QL by then, counted only once the leads are worked |
| M10 | "Forms → CRM OK" mixed WhatsApp in; 3 form leads missing; Pixel/CAPI not stated | skeptic 3, critic 10 | **Accept, fixed** in §3. CAPI health → next run |
| M11 | W vs P confounds (stop-start delivery, unlogged 12 Nov change, GC05 market-wide urgency drop, 5 stacked changes) | skeptic 5 | **Accept.** All W-vs-P "worse" claims are directional |
| M12 | SIB-05 figures were residuals | skeptic 7, CFO F11 | **Resolved**: direct pull matches (T10b) |
| M13 | India-Entry draft would draw on the same prepaid pool | CFO F9 | **Accept.** Ring-fence an India-Entry line in `budget-plan.md` before PR #2's draft goes live |
| M14 | Builds on unmerged PR #1 | zoom-out 4 | **Accept.** Resolving PR #1 is a precondition (A3); its A1–A8 are superseded by this list where they overlap |

## 🟢 Nits (accepted)
"Savings" is really a mix shift in a prepaid account; add a 10% buffer for Meta's daily overspend (critic 11). Log the owner's 4 Nov SIB-01 restore and identify the 2 extra SIB-04 ads (critic 12). Add pull times and a rolling 30-day won/CPA (critic 13, skeptic 10). Show P columns and ROAS (skeptic 10). Name the CRM ad-set field (`Meta_Ad_Set`) and flag list leads that are existing contacts (skeptic 8). GST on top-ups is recoverable as ITC if the GSTIN is on Meta invoices (CGST Act 2017 s. 16, s. 17(5); verify current text). Show cash vs net (CFO F10). Budget the 5 idle platforms at ₹0 (CFO F12). Footnote SIB-05 and use one decision metric (zoom-out 5–6). Make "no change to SIB-02" a hold note (zoom-out 8). Trim §7 (zoom-out 10).

## Traceability
| Finding | Reviewers | Final action |
|---|---|---|
| B4, M1, M2, M13 | CFO, all | A1, A4 |
| B1, M5 | critic, skeptic, zoom-out, CFO | A2 → 19 Nov decision; A6 |
| B2 | skeptic, critic, zoom-out, CFO | A8 |
| B3, M3 | CFO | A4 (owner inputs) |
| M9 | skeptic, critic, CFO | A5 |
| M14, critic 12 | zoom-out, critic | A3 |
| M7 | critic, zoom-out | A7 |
| M4, M8, M10 (CAPI) | critic, CFO, skeptic | Next weekly run |
| M6, M10, M11, M12 | | Fixed in review / data |

## Final recommended action list (execution order; nothing applied)
| # | Owner | Action | Approve? |
|---|---|---|---|
| A1 | Owner (money, human only) | **Fund continuously, within a ceiling.** Enter a November Meta ceiling in `budget-plan.md` (spend to date ₹63,559 [calc, 2–15 Nov] + a stated maximum), plus a separate India-Entry line. Top up through the next review (≈7 days at the chosen budget + 10% buffer). Release the full week only once A2 brings unworked leads below 20% | ☐ |
| A2 | Sales TLs | Work the **47 unworked paid leads** (SIB-01 15, SIB-04 14 incl. 4 WhatsApp, SIB-02 17, SIB-05 1) and the 4 ChatGPT leads by **19 Nov**. The 19 Nov re-read decides SIB-01 (pause if its worked-lead QL rate stays below SIB-02's) and SIB-04 WhatsApp (A8) | ☐ |
| A3 | Owner + Claude | Resolve PR #1, then log in the changelogs: the 4 Nov SIB-01 restore, the 12 Nov 06:46 SIB-04 status change (and which session made it), the 14 Nov ChatGPT restart with its budgets | ☐ |
| A4 | Owner | Supply **gross margin %, trademark AOV, and whether deal Amount includes govt fees**. Approve kill rules (CFO F2): SIB-02 Interest pause if ₹/QL > ₹700 after ₹7,000; SIB-04 Form pause if CRM ₹/lead > ₹568 after ₹17,500; SIB-02 → ₹2,000/day if the 2–15 Nov cohort has 0 won by 7 Dec | ☐ |
| A5 | Owner | ChatGPT Ads: hard ceiling ₹7,115 cumulative from 14 Nov. Pause both campaigns if < 4 QL by then (counted on worked leads), or if 0 won by 31 Dec | ☐ |
| A6 | Owner (option) | If SIB-01 survives 19 Nov: switch its Instant Form to **Higher Intent** (one change, reversible) instead of a budget cut | ☐ |
| A7 | Claude | Add to `shared/learnings.md`: the SIB-01 cut was not tested (reverted 4 Nov); the SIB-04 relaunch package failed the October cost target with confounded causes; SIB-02 Lists beat Interest on ₹/QL (₹493 vs ₹679, directional, list-basis caveat); ChatGPT had 0 won from 62 leads (54 + 8) [check] | ☐ |
| A8 | Owner | SIB-04 WhatsApp ad set 120247072309210449: **₹2,000 → ₹1,500/day** (−25%) now; decide pause or keep on 19 Nov after its 4 leads are worked | ☐ |

**Deferred to the next run:** expected-revenue-per-₹ column; ad, placement, age, frequency and form-type drivers; CAPI event health; SIB-02 Lists frequency and duplicate check; ₹0 budget lines for idle platforms.
