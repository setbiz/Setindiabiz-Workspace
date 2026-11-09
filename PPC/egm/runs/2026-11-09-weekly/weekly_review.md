# Weekly PPC Review — week ending 2026-11-08

Elephant draft, scheduled run of 9 Nov 2026. Read-only: **no ad account was changed.** Every number is in `data.md` (table reference in brackets). `[calc]` = computed here from sourced numbers.

**Headline:** the Meta account has been **dark since 6 Nov 06:52 IST because prepaid funds are empty** (T4, T5). The week had about 3.2 days of full delivery (2, 3, 5 Nov plus ₹1.9k on 4 Nov). The previous week had about 1.75 days (dark from 27 Oct evening to 2 Nov). Neither week supports a performance verdict on the 2 Nov changes.

## 1. Data provenance
| Platform | Source | Date range | Compared with | Pulled at | Missing? |
|---|---|---|---|---|---|
| Meta (FB+IG+WhatsApp) | Meta Ads connector, account 152154124583473 | 2–8 Nov 2026 | 26 Oct–1 Nov 2026 | 9 Nov ≈10:20 IST | No. Partial delivery in both weeks (funding) |
| CRM | Zoho CRM connector (COQL, aggregates) | Leads created 2–8 Nov; deals closed 2–8 Nov | Same, 26 Oct–1 Nov | 9 Nov ≈10:35 IST | Lead status is immature (leads 1–7 days old) |
| Google Ads | Supermetrics AW | 26 Oct–8 Nov | — | 9 Nov | No activity |
| Microsoft Ads | Supermetrics AC | 26 Oct–8 Nov | — | 9 Nov | No activity |
| ChatGPT Ads | Supermetrics CGPTA / CSV | — | — | — | **Missing** (not authenticated, no CSV). CRM: 0 ChatGPT leads (P: 8) |
| LinkedIn, X, Reddit | Supermetrics LIA / TA / RDA | — | — | — | **Missing**: not authenticated (no known live campaigns) |

## 2. Scorecard
Qualified lead (QL) = CRM Lead_Status "Valid Lead" or "Proposal Sent" (T8). Target: break-even cost per CRM lead ≈ **₹176** (90-day CRM basis, 2 Nov audit, 50% margin assumed; `kpis.md` still shows the older ₹130–135).

| Platform | Spend ₹ | Clicks | CTR | CPC ₹ | Conv. (Meta) | Cost/CRM lead ₹ | QL (CRM) | Cost/QL ₹ | vs target | vs prev |
|---|---|---|---|---|---|---|---|---|---|---|
| Meta: SIB-02 Trademark | 7,332.86 | 187 | 0.89% | 39.21 | 26 leads | 293 [calc] (25 CRM) | 13 | 564 [calc] | 1.7× | P ₹93/CRM lead (14) [calc] |
| Meta: SIB-01 Incorporation | 4,028.96 | 116 | 0.89% | 34.73 | 11 leads | 366 [calc] (11) | 5 | 806 [calc] | 2.1× | P ₹143 (24) [calc] |
| Meta: SIB-04 Annual Filings | 10,614.96 | 260 | 0.92% | 40.83 | 11 form leads + 10 WA conv. | 1,062 [calc] (10) | 3 | 3,538 [calc] | 6.0× | P ₹1,161 (6) [calc] |
| Meta: SIB-05 India Entry | 11,921.51 | 46 | 1.48% | 259.16 | 2 leads | 5,961 [calc] (2) | 1 | 11,922 [calc] | n/a (high-AOV, see §4) | P ₹2,619 (2) [calc] |
| Google / Microsoft | 0 | 0 | — | — | — | — | — | — | — | 0 |
| ChatGPT Ads | missing | | | | | — (0 CRM leads) | 0 | | | P 8 CRM leads |
| **Blended (Meta)** | **33,898.29** | **609** | **0.93%** | **55.66** | 50 form leads + 10 WA conv. | **706** [calc] (48) | **22** | **1,541** [calc] | **4.0×** [calc] | P ₹368 (46) [calc]; spend +100% on more delivery days |

Won deals closed this week (paid Meta): 3, ₹7,000 (P: 6, ₹27,369) (T9). These come from October leads, so the week's revenue/spend (0.21× [calc]) is not a verdict on this week's spend.

## 3. Tracking health
- **Meta forms → CRM: OK.** 50 Meta form leads vs 47 CRM form leads (FB+IG) [T3, T7] = 94% [calc]. All W `Advt%` leads carry `Meta_Campaign`.
- **WhatsApp → CRM: broken or lagging.** The SIB-04 WhatsApp ad set reports **10 conversations started** (₹4,949) but the CRM has **1** `Advt - WhatsApp` lead in W (T2, T7). P had 3. Either chats are not being turned into leads (agent/bot path) or they land under another source. Hypothesis: the `sib_wa_lead` plug or CTWA click capture (Cowork change logs 7–15 Oct) is not firing for the new GC05 ad.
- **ChatGPT Ads:** 0 CRM leads in W vs 8 in P, with no platform data. Hypothesis: campaigns stopped or budget exhausted. Unverified.
- **Funding:** 3 interruptions in 14 days: 27 Oct evening–2 Nov, 4 Nov (₹1.9k day), 6 Nov onward (T4, T6). The ₹15,000 top-up on 4 Nov 18:06 lasted ≈1 day at ₹15,000/day of budgets.
- Meta anomaly check: none flagged (T5).

## 4. What changed and why
1. **Delivery was set by funding, not performance.** Spend doubled vs P only because the account ran ≈3.2 days instead of ≈1.75 (T4).
2. **Costs per lead rose sharply after the 2 Nov targeting change.** SIB-01 CPC ₹23.55 → ₹34.73 and Meta CPL ₹143 → ₹366. SIB-02 CPC ₹18.16 → ₹39.21 and CPL ₹77 → ₹282 (T1, T1-P). CTR fell on both (1.16% → 0.89%, 1.26% → 0.89%). *Hypothesis:* the narrower layer-2 audience (behaviour AND education, age cap, Advantage+ off) raised CPMs and cut volume. That is the intended trade-off if lead quality rises. Quality is not yet readable: SIB-02 52% QL [calc 13/25] and SIB-01 45% QL [calc 5/11], on 1–7-day-old leads.
3. **SIB-02 now runs mostly on the customer-list ad set.** Lists ₹5,755 → 20 leads at ₹288. Interest ₹1,578 → 6 leads at ₹263 (T2). The two are comparable on cost. The Lists ad set has run ≈3 delivery days, so its 7-day read is not complete.
4. **SIB-04:** the new GC05 Form ad delivered from 2 Nov 20:42 (11 leads, ₹422/lead). The old ACR ads still spent ₹2,091 on 2 Nov before the pause (T3). 7 of 10 SIB-04 CRM leads are not yet worked (T8).
5. **SIB-05:** ₹11,922 for 2 CRM leads (1 valid). One ad, B2 Branch office, took ₹9,450 = 79% [calc] of the campaign for 1 lead (T3). CPM ≈ ₹3,600–3,900 (T2). The owner's 2 Nov rule allows ₹15,000 of further spend. **₹3,078 [calc] remains**, under one day at the ₹4,000 budget.
6. **Unlogged change:** the SIB-01 budget went back from ₹1,250 to ₹2,500/day on 4 Nov 18:14 (owner, Power Editor) (T6). The approved 50% cut ran ≈2 days and isn't recorded in `meta/changelog.md`.
7. **Speed-to-lead:** 21 of 48 W leads (44%) [calc] are still "Establishing Contact" or empty (T8). The Cowork baseline attributes ≈51% of lost deals to the sales process.

## 5. Due reviews (from changelogs)
| Platform | Change (date) | Expected | Actual | Verdict | Learning recorded? |
|---|---|---|---|---|---|
| Meta | Layer-2 targeting on all 8 ad sets (2 Nov) | Higher quality, lower volume | ≈3.2 delivery days. CPL up 2.5–3.7× on SIB-01/SIB-02. QL rate 45–52% on immature leads | **Inconclusive**. Extend to 7 funded days after the top-up | Not yet: pending |
| Meta | SIB-04 age 25–45 → 25–55 (2 Nov) | More delivery on director lists | SIB-04 spent ₹10,615 in ≈3.2 days. Age breakdown not pulled | **Inconclusive**. Extend | Not yet |
| Meta | SIB-04 reactivated (2 Nov) | Annual-filing leads and won deals through the fee-relief window | 10 CRM leads, 3 QL, 0 won so far | **Inconclusive**. Won deals lag 2–4 weeks | Not yet |
No other changelog has a due "Review on" date.

## 6. Proposed actions (ranked)
| # | Platform | Exact change | Evidence | Expected impact | Risk / reversible? | Review on |
|---|---|---|---|---|---|---|
| 1 | Meta (billing, **human only**) | Add prepaid funds. At current budgets (₹15,000/day) 7 days = ₹1,05,000 of credit ≈ **₹1,23,900 payment incl. 18% GST** [calc]. If action 2 is approved (SIB-05 off), ₹11,000/day → ≈₹90,860 [calc]. Consider a payment method that avoids repeated dark days | T4, T5, T6: dark since 6 Nov; 3 interruptions in 14 days | Restores delivery; gives the first clean 7-day read of the 2 Nov changes | None on performance. Spend resumes at current settings | 2026-11-16 |
| 2 | Meta | Enforce the owner's 2 Nov SIB-05 cap: **pause campaign "SIB-05 India Entry" (120247067847480449) before funds are added**, unless the owner raises the cap. Only ₹3,078 of the ₹15,000 cap is left | T2, T3, T7, T8: ₹11,922 → 2 CRM leads, 1 valid; B2 took 79% for 1 lead | Saves ₹4,000/day. Stops spend past the agreed cap | Reversible (status only). Restarting means re-learning | 2026-11-16 |
| 3 | Meta (process) | No budget change. Record the 4 Nov SIB-01 budget restore (₹1,250 → ₹2,500) in `meta/changelog.md` and restart the SIB-01 quality read: 7 funded days at ₹2,500 | T6 | Keeps one variable per campaign and gives an honest test | None | 2026-11-16 |
| 4 | CRM (no ad change) | Check why SIB-04 WhatsApp chats don't become CRM leads: 10 conversations vs 1 `Advt - WhatsApp` lead. Test one chat on the GC05 CTWA ad end to end (bot → plug → lead with `Meta_Campaign`) | T2, T7; Cowork SIB-04 CRM change logs | Recovers attribution for the WhatsApp ad set: ₹4,949 = 14.6% of W spend [calc]; ₹2,000 of ₹15,000 daily budget = 13% [calc] | None | Before funds resume |
| 5 | Sales process (no ad change) | TLs clear the 21 unworked paid leads from 2–8 Nov, SIB-04 first (7 of 10, deadline-season service) | T8 | Converts leads already paid for (≈₹706 each [calc]) | None | 2026-11-11 |
| 6 | All Meta | **Hold** all other targeting, creative and ad-set changes (SIB-02 Lists, SIB-04 GC05 ads, layer-2 targeting) until 7 funded days have passed | §4: ≈3.2 delivery days; several changes started 2 Nov | Avoids confounding the read | None | 2026-11-16 |
| 7 | ChatGPT Ads | Owner checks in the ChatGPT Ads dashboard whether campaigns are live or out of budget. Connect CGPTA in Supermetrics (early access), or drop a weekly CSV in `chatgpt-ads/reports/raw/` | T7, T10: 0 CRM leads vs 8 | Restores visibility of a paid channel | None | 2026-11-16 |

## 7. Needs human decision
1. **Top-up amount and payment method** (action 1). Money movement is human-only.
2. **SIB-05:** enforce the ₹15,000 cap (pause), or raise it. India-entry AOV ≈ ₹86,300 needs lead→won ≥ 8.8% to break even at the 2 Nov CPL (2 Nov owner resolution). Current: 1 valid lead from ₹11,922 this week.
3. **SIB-01:** confirm the 4 Nov budget restore to ₹2,500 was intended. If so, action 3 restarts the test. If not, revert to ₹1,250 (one change only).
4. Update `kpis.md` target CPL from ₹130–135 to the audit's ₹176 basis? It still needs the gross-margin figure (open since 2 Nov).
5. Open since 2 Nov: gross margin %; website "18K+" vs ads "25,000+".
