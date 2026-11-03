# SetIndiaBiz Meta Ads — Daily Watchdog + Monday Rollup
**Monday, 10 August 2026** · Account SETINDIABIZ (152154124583473) · Prepared by the Meta Ads optimisation operator · Read-only except Part B (0 writes today)

---

## 🚦 Delivery (yesterday, 9 Aug 2026)

**GREEN — not dark.** Spend ₹8,474.58 · Impressions 28,891 · Clicks 269 · CPC ₹31.5 · CTR 0.93%. This matches the recurring "half-tier" pacing signature (₹8,474.57–58) seen on 8 Aug, 28 Jul, and historically on Sundays/Saturdays — confirmed not weekday-bound.

**⚠️ Correction to the blackout record.** The 14-day spend trend shows the recent outage was **longer and messier than previously logged as "1–5 Aug, 5 days."** Actual pattern:

| Date | Day | Spend | Note |
|---|---|---|---|
| 27 Jul | Mon | ₹0.01 | dark |
| 28 Jul | Tue | ₹8,474.57 | delivered (half-tier) |
| 29 Jul | Wed | ₹0.01 | dark |
| 30 Jul | Thu | $0 (no record) | dark — **not previously logged as a blackout day** |
| 31 Jul | Fri | ₹0.91 | dark |
| 1–5 Aug | Sat–Wed | $0 | dark (the previously-logged 5-day block) |
| 6 Aug | Thu | ₹11,824.74 | recovered |
| 7 Aug | Fri | ₹17,836.28 | recovered, strong (clears the old ₹12,711.86 ceiling) |
| 8 Aug | Sat | ₹8,474.57 | half-tier |
| 9 Aug | Sun | ₹8,474.58 | half-tier |

Net: **28 Jul was the only real delivery day in a 10-day span (27 Jul–5 Aug)** — effectively a 9-day disruption, not 5. Cause still undiagnosed (billing/spending-limit is the standing hypothesis per the recurring 18-Jul/23-Jul pattern) — Sanjeev should check Ads Manager → Billing for what triggered/cleared it. This materially eats into the 150×150 glidepath timeline; treat July's checkpoints as effectively skipped.

---

## Inflow vs baseline

Yesterday: **17 paid CRM leads** (Advt-Facebook + Advt-Instagram). Literal trailing-7-day avg (2–8 Aug, includes 4 blackout zero-days) = 22.1/day — not a meaningful baseline right now. More useful: 3-day post-recovery average (6–8 Aug) = **51.7/day**, so yesterday ran **33% of the recovery pace**. Expected for a half-tier Sunday, not alarming alone — but CPL was the highest of the 4 recovery days: 9 Aug ₹498.5 vs 6 Aug ₹337.8 / 7 Aug ₹225.8 / 8 Aug ₹206.7. Small sample (17 leads); watch, don't act.

---

## Stop-loss / trigger board (3-day window, 7–9 Aug)

| Ad set | 3d spend | Leads | CPL | Valid | Valid% | Status |
|---|---|---|---|---|---|---|
| C3 TMF-SA | ₹5,551.77 | 41 | ₹135 | 21 | 51.2% | ✅ Healthy, well inside ₹250/30% |
| C3 Director-TMF | ₹3,511.18 | 26 | ₹135 | 13 | 50.0% | ✅ Healthy — notable improvement vs its recent near-floor history |
| C1 Daytime INSA | ₹3,399.74 | 22 | ₹155 | 9 | 40.9%¹ | ✅ Clears both gates — **staging-increment candidate** |
| C1 24Hr INSA | ₹3,332.69 | 28 | ₹119 | 7 | 25.0%¹ | ⚠️ CPL excellent, valid% soft even matured — see below |
| C4 CCFS | ₹18,990.05 | 19 | **₹1,000** | 11 | 57.9% | 🚨 Severe cost/valid problem — see below |
| #IND5 DPIIT | — | — | — | — | — | ✅ Confirmed still `CAMPAIGN_PAUSED` (standing pause since 14 Jul) — not re-flagged |

¹ Grading-lag checked: Daytime INSA matures to **58.3% valid** on the 6–7 Aug-only cohort (vs 40.9% blended); 24Hr INSA matures to **31.6%** on 6–7 Aug vs **20.0%** on fresh 8–9 Aug (blended 25.0%) — the dip is real, not just fresh-lead grading lag, though still borderline around the 30% floor.

**Must-stay-paused list** (IND6 campaign, both LAL1% ad sets, DPIIT ads #C5 DPIIT-2 & #C5 DPIIT-4): all confirmed correctly paused. No drift.

**🚨 CCFS (#IND4) — top issue today.** 3-day spend ₹18,990 (≈₹6,330/day) for only 19 leads, cost/valid **₹1,726** — the worst of any campaign, and worse than the ₹6,685/day / ₹1,254 cost/valid already flagged 9 Aug. CCFS is now consuming **59% of this week's total spend for 19% of lead volume**. The connector shows **no explicit daily or lifetime budget cap on "C4 Adset - Director CCFS + Form"** — worth checking directly in Ads Manager, since an uncapped/misconfigured pacing setting would explain the runaway spend.

**⚠️ Unverified change — C1 24Hr INSA daily budget.** Connector now reads **₹2,500/day**; the last approval on record was ₹2,160/day (20 Jul, +20% increment). No change-log entry covers ₹2,160→₹2,500. Please confirm whether this was an authorized further increment — if so I'll log it; if not, flag for review.

**✅ Resolved — C1 Daytime INSA end-date.** This has been an open question since 20 Jul ("will strand ~₹38–48k unless extended"). The ad set now reads **end_time 24 Aug 2026** (lifetime ₹190,500 unchanged) — the extension has happened. No further action needed on this specific item.

---

## Yesterday's quality + form-change watch

9 Aug cohort (17 leads) is too fresh for Lost determinations: Establishing Contact 10, Valid Lead 5, Proposal Sent 1, blank 1 — 0 Lost. Live quality-picklist check across the full 4-day window (172 leads) confirms only **"Valid - RM Working"** and **"Still Evaluating"** are in real use; the other three prefixed valid tiers (Good/Casual/NIL RM Action) did not appear at all, and "Valid - Product Not Ready" appeared once (correctly excluded from valid).

Form-change watch (matured 6–7 Aug cohort, 16 losses): junk share (Inquired by Mistake + Job Seeker) = 4/16 = **25%** — inside the acceptable range, consistent with the 21-Jul "resolved" call. No action needed; the 2nd qualifying question does not need restoring.

---

## 7-day campaign scorecard

Window is nominally 3–9 Aug, but **3–5 Aug were fully dark** — figures below reflect the 4 active days (6–9 Aug).

| Campaign | Spend | CRM Leads | CPL | Valid | Valid% | Cost/Valid | Progressed | Cost/Progressed |
|---|---|---|---|---|---|---|---|---|
| #IND 1 — Incorporation | ₹10,075.83 | 70 | ₹143.9 | 25 | 35.7% | ₹403.0 | 5 | ₹2,015.2 |
| #IND3 - Trademark | ₹9,069.64 | 67 | ₹135.4 | 34 | 50.7% | **₹266.8** (best) | 17 | ₹533.5 |
| #IND4 - CCFS | ₹27,464.70 | 33 | ₹832.3 | 18 | 54.5% | **₹1,525.8** (worst) | 5 | ₹5,492.9 |
| **TOTAL** | **₹46,610.17** | **172**² | — | **77** | **44.8%** | **₹605.3** | **27** | **₹1,726.3** |

² 170 leads carry a named campaign; 2 have null Meta_Campaign (1.2% — healthy, well under the 10% alarm line).

**Glidepath verdict:** blended CPL ₹271 (spend÷172) reads *above* the mid-Aug ₹150–180 checkpoint — but that's entirely CCFS. Excluding CCFS, Trademark + IND1 together run **₹139.7 CPL** on 137 leads — comfortably *inside* the mid-Aug band. Diagnosis: the account's efficiency problem is CCFS-specific, not systemic — Trademark and Incorporation are both tracking ahead of plan.

---

## CAPI channel health — 🟢 GREEN

Server last fired ~12h50m ago (2026-08-09 10:03 PDT). 72h SERVER_ONLY events: **ValidLead 33, Purchase 23** (consistent with the 9-Aug reading of 34/22 — steady). Extrapolated pace ≈77 ValidLead/week if sustained, nearing the ≥50/week readiness gate — but the **P9 quality-optimisation switch (C1 Daytime INSA) has not been executed yet**, so the website-conversion-retest gate (P3) is not fully met. Report progress only, no action.

---

## Speed-to-lead exceptions (last 48h, 8–9 Aug)

**39 stale/untriaged paid leads**, of which only 3 are completely untriaged (blank status) — the rest sit in Establishing Contact/Postponed. Owner concentration: **Singh 11 + Kumar 11 = 22/39 (56%)** of the queue between two owners. This is the same rotating-bottleneck pattern flagged repeatedly (different owner names each time: Kumar 6/15/20 Jul, Kumar+Yadav 9 Aug, now Singh+Kumar) — reinforces that this looks like a missing SLA/alerting process rather than one rep's issue.

| Name | Phone | Owner | Hours old | Status |
|---|---|---|---|---|
| Samyak | +917517722134 | Kumar | ~44.0h | *(untriaged)* |
| Ganesh das Chhangani | +918240413061 | Kumar | ~42.9h | *(untriaged)* |
| Laguri | +917894953837 | Agrawal | ~15.8h | *(untriaged)* |
| Gehlot | +918619825765 | Kumar | ~46.5h | Establishing Contact |
| Ray | +916372652168 | Singh | ~46.1h | Establishing Contact |
| Vipin Sharma | +919891146517 | Yadav | ~46.0h | Establishing Contact |
| Manish Manohar | +917972450289 | Singh | ~46.0h | Establishing Contact |
| Dnyaneshwar N | +917773958283 | Yadav | ~45.9h | Establishing Contact |
| PRAKASH AYAWALE | +919273942485 | Sehrawat | ~45.9h | Establishing Contact |
| Arun tiwari | +919569469023 | Bisht | ~45.7h | Establishing Contact |

*(Status+age proxy — first-contact latency isn't directly instrumented.)*

---

## Loss buckets

Yesterday: 0 losses (cohort too fresh). Matured window (6–7 Aug, 16 losses): Not Interested 5, Inquired by Mistake 3, Other CA 2, Language Issue 2, Plan Drop 1, Not Eligible 1, No Product Offering 1, Job Seeker 1. Directional bucket read: natural attrition ~38%, targeting/qualification ~25%, pricing/competition ~13%, sales-process ~13%, geography/serviceability ~13%. **Zero "Avoiding Call"** in this window — vs the ~44–51% historical baseline. Small sample (16), but a positive signal worth tracking over the next few days.

---

## Pilot monitors

- **P0 WhatsApp auto-follow-up:** not launched — still waiting on Sanjeev (WA provider/number, template sign-off, form opt-in line).
- **P1 TM call ads:** not launched — waiting on a dedicated phone number + answering owner.
- **P2 CTWA (Company Registration):** not launched (gated on P0). `CTWA_Click_ID` is null on 100% of 219 leads sampled across the last two weeks — confirms zero pilot activity.
- **P3 Website-conversion retest:** gated. CAPI pace ~77 ValidLead/week (nearing the ≥50/week bar) but P9 switch not done — report progress only, not ready.

---

## Part B — Lead-source QA sweep: **clean, 0 writes**

- Chat stragglers: 0 · Blank Lead_Source: 0 · Stray labels (last 2 days, all sources): none — all values are valid taxonomy (Advt-Facebook 36, Advt-Instagram 22, Self-Cold Call 157, Self-Web Chat 10, SEO-Google 2, Direct 8, SEO-Zoho Booking 1).
- Stamped-value contradictions: 0 (AI-source utm check, "Zoho Bookings" stray-label recheck both clean).
- Meta placement integrity (ig↔Facebook / fb↔Instagram mismatches): 0 both directions.
- The 9-Jul "Auto-set Lead Source from URL" fix continues to hold.

---

## Part C — Monday weekly rollup

**Caveat up front:** both "this week" (3–9 Aug, 4 active days) and "prior week" (27 Jul–2 Aug, ~1.5 active days) are blackout-contaminated, so a literal week-over-week read is close to meaningless. Figures given for completeness; the last clean pre-blackout baseline (24 Jul watchdog: 17–23 Jul, blended CPL ₹224 @48.2% valid, ~43 leads/day) is the more useful reference point.

**C1/C2 — full funnel, this week vs prior week:**

| | This week (6–9 Aug, 4d) | Prior week (27–28 Jul, ~1.5d) | Δ |
|---|---|---|---|
| Spend | ₹46,610.17 | ₹8,475.50 | +450% (recovery, not growth) |
| Leads | 172 | 47 | +266% |
| Valid (simplified metric)³ | 75 (43.6%) | 23 (48.9%) | -5.3pp |
| CPL | ₹271.0 | ₹180.3 | +50% (CCFS-driven — ex-CCFS this week is ₹139.7, *better* than prior week) |

³ Simplified valid = RM_Lead_Quality='Valid - RM Working' OR Lead_Status='Valid Lead' only (excludes progressed-status-only valids), used here for apples-to-apples; the fuller KPI definition gives this week's valid as 77/44.8% (see scorecard above).

**Deals (committed/won), Modified_Time last 7d, GROUP BY Meta_Campaign:** Committed (Payment Wait) = 32 account-wide, but **0 carry Meta_Campaign or paid-Meta Lead_Source attribution** — this is a known Deal-level attribution gap (campaign field rarely populates on Deals), not necessarily zero real Meta committals in progress. Won-stage touches this week = 1,402 account-wide (mostly ongoing fulfilment-stage movement — W-CSD/W-SPI/W-Login/W-SKV — not discrete new-win events); of those, 44 (Advt-Facebook 40 + Advt-Instagram 4 = 3.1%) carry paid-Meta Lead_Source attribution. Treat all Deal-side Meta figures as directional only.

**C3 — CAPI optimisation readiness:** not yet ready. See CAPI section above — ~77 ValidLead/week pace, P9 switch outstanding.

**C4 — Lead-source distribution (last 2 days, all sources):** Self - Cold Call 157 (66.5%), Advt-Facebook 36 + Advt-Instagram 22 (24.6%), Self - Web Chat 10, SEO-Google 2, Direct 8, SEO-Zoho Booking 1. No non-taxonomy values, no blank-source spike, no cross-tab mismatches.

---

## Recommended for approval (max 2)

1. **CCFS cost-efficiency review.** 3-day cost/valid ₹1,726 vs account blended ₹605 (worst of all campaigns); the ad set shows no visible daily/lifetime budget cap via the connector. Ask: Sanjeev checks "C4 Adset - Director CCFS + Form" pacing/budget settings directly in Ads Manager. **Confirming metric:** 3-day cost/valid back under ₹800 within 3 days of any correction.
2. **C1 Daytime INSA — next +20% staging increment.** Both gates now clear (3d CPL ₹155 vs ₹350 ceiling; valid% 40.9–58.3% vs the ≥40% bar) and the lifetime end-date question is resolved (now 24 Aug). Ask: approve pulling exact lifetime-spent-to-date to size the next tranche (remaining budget ÷ remaining days) and applying it. **Confirming metric:** post-increment 3-day CPL stays <₹350 and valid% ≥40%.

*(Separately, not counted above: please confirm whether the C1 24Hr INSA daily budget increase to ₹2,500 — up from the last-logged ₹2,160 — was an authorized change, so it can be logged.)*

---
*All Meta figures via the Meta Ads connector (account-level attribution until LeadChain fix is fully live). All CRM figures via Zoho COQL, Lead_Source ∈ {Advt - Facebook, Advt - Instagram} only. No Meta mutations executed — ad-level changes still require the browser route per the standing leadgen-ToS block.*
