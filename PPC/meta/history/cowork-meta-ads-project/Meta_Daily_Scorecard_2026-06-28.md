# SetIndiaBiz — Meta Ads Daily Watchdog

**Reporting day:** Sunday, 28 June 2026 · **Run:** Mon 29 Jun 2026, 08:04 IST · **Segment:** Lead_Source = "PPC Meta Insta" · **Mode:** read-only

---

## 1. 🟢 Delivery status — GREEN

Campaigns delivered normally yesterday (no blackout).

| Metric | 28 Jun |
|---|---|
| Spend | ₹8,474.58 |
| Impressions | 25,770 |
| Clicks | 221 |
| CTR | 0.86% |

Spend was ~58% of the 7-day daily average (₹14,528/day) — a Sunday pullback, not a fault.

## 2. Lead inflow vs baseline

| | Value |
|---|---|
| Leads 28 Jun | 22 |
| 7-day daily avg (21–27 Jun) | 35.1/day |
| Variance | −37% |

Below average but **not** a hard flag (threshold −50%). Leads (63% of avg) track spend (58% of avg) almost exactly — day-of-week budget effect, not a delivery or LeadChain sync break (spend > 0 **and** CRM leads > 0).

## 3. Quality & funnel — 28 Jun cohort (n = 22)

Same-day snapshot. 14 of 22 (64%) are still "Establishing Contact" (being triaged), so valid%/progressed% will mature upward.

| Outcome | Count | % | Account-level cost (spend ÷ count) |
|---|---|---|---|
| Valid | 5 | 23% | ₹1,694.92 / valid |
| Progressed | 4 | 18% | ₹2,118.65 / progressed |
| Won | 0 | — | building (same-day cohort) |

Status split: Establishing Contact 14 · Valid Lead 1 · Negotiation 2 · Proposal Sent 1 · Payment Pending 1 · Lost 1 · blank 2.

## 3b. Campaign cost-per-quality scorecard — last 7 days (22–28 Jun)

Spend = Supermetrics (Facebook Ads). Quality = Zoho by Meta_Campaign. Cost/Lead uses **CRM** leads, not Meta's on-FB leads. Virtual CFO variants merged. Leads with null Meta_Campaign (11 returning/dedup) excluded from the split. Cost/Committed & Cost/Won by campaign still **building**.

| Campaign | Spend ₹ | CRM Leads | Cost/Lead | Valid | Cost/Valid | Progressed | Cost/Progressed |
|---|---:|---:|---:|---:|---:|---:|---:|
| #IND1 — Business Registration | 49,679 | 109 | ₹456 | 39 | ₹1,274 | 22 | ₹2,258 |
| #IND4 — CCFS | 21,715 | 67 | ₹324 | 24 | ₹905 | 16 | ₹1,357 |
| #IND6 — Virtual CFO (merged) | 12,768 | 19 | ₹672 | 8 | ₹1,596 | 1 | ₹12,768 |
| #IND5 — DPIIT | 11,861 | 35 | ₹339 | 11 | ₹1,078 | 10 | ₹1,186 |
| #IND3 — Trademark | 5,672 | 27 | ₹210 | 13 | ₹436 | 7 | ₹810 |
| **TOTAL** | **1,01,695** | **257** | **₹396** | **95** | **₹1,070** | **56** | **₹1,816** |

- **Best Cost/Valid:** #IND3 Trademark — ₹436 (also cheapest Cost/Lead and healthy progression).
- **Worst Cost/Valid:** #IND6 Virtual CFO — ₹1,596.
- **🔴 Key leak:** Virtual CFO converts valid→progressed at just **1 of 8** (₹12,768/progressed, ~7× the next worst). High spend (3rd highest) is producing valids that stall. DPIIT is the opposite — 10 progressed from 35 leads at ₹1,186/progressed.

## 4. Speed-to-lead exceptions (last 48h, untriaged first)

Proxy = status + age (true first-contact latency not yet instrumented). 6 leads sit at **blank** status, 4 of them ~41–45h old.

| # | Name | Phone | Owner | Age | Status |
|---|---|---|---|---|---|
| 1 | Raajeev | +917039000952 | Kumar | ~45h | blank |
| 2 | Pankaj Sharma | +919039132015 | Tyagi | ~45h | blank |
| 3 | Venugopal | +919866231601 | Tyagi | ~41h | blank |
| 4 | Pratik Ambilwade | +919604046422 | Banerjee | ~41h | blank |
| 5 | Syed Shakeer | +918125853204 | Kumar | ~18h | blank |
| 6 | Vaseem Akram | +919844161837 | Kumar | ~16h | blank |
| 7 | Rahul Ingole | +918600871306 | Gupta | ~46h | Establishing Contact |
| 8 | subhash | +919922600365 | Kumar 3 | ~46h | Establishing Contact |
| 9 | Girish Kumar | +919989987780 | Sehrawat | ~46h | Establishing Contact |
| 10 | Hiren | +919537992616 | Gupta | ~46h | Establishing Contact |

## 5. Loss buckets — 28 Jun

Only 1 loss yesterday: **"Other CA"** (offer/pricing/competition bucket — prospect already has a CA). Sample too small to compare to baseline (sales-process 51% / pricing-competition 32% / targeting 11%). **No "Avoiding Call" losses** yesterday — the #1 historical leak was clean (tiny sample).

## 6. Recommended changes — for Sanjeev's approval (never auto-executed)

**Rec 1 (ad-side, needs approval — one variable, before/after screenshot, stop-loss):**
Shift ~15–20% of daily budget (~₹2,000–2,500/day) **from #IND6 Virtual CFO → #IND3 Trademark**. Rationale: Virtual CFO is worst Cost/Valid (₹1,596) with near-zero progression (1 of 8 valids); Trademark is best Cost/Valid (₹436) with healthy progression and headroom.
- *Confirming metric:* 7-day blended Cost/Progressed falls below ₹1,816; Trademark Cost/Valid stays under ₹700.
- *Stop-loss:* revert if Trademark Cost/Valid exceeds ₹700 or Virtual CFO progression recovers on its own.

**Rec 2 (sales-process, not an ad change — diagnostic):**
Virtual CFO's 8-valid → 1-progressed gap points to qualification/pricing/follow-up, not targeting. Have the RM team review Virtual CFO valids and pull Why_Disqualified before any deeper ad cut. Triage the 6 blank-status leads above today (owners: Kumar ×3, Tyagi ×2, Banerjee).

---
*Caveats: account-level costs in §3 are same-day cohort snapshots and will improve as leads mature. §3b spend window (Supermetrics last_7_days) and CRM window (≥22 Jun) differ at the edges by hours. Speed-to-lead is a status+age proxy.*
