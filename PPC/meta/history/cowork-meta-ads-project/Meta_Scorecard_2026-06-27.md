# SetIndiaBiz — Meta Ads Daily Scorecard

**Reporting day:** Saturday, 27 Jun 2026 · **Generated:** Sun 28 Jun 2026, 08:30 IST
**Account:** SETINDIABIZ (152154124583473, INR) · **Paid segment:** Lead_Source = "PPC Meta Insta"
**Mode:** Read-only watchdog. All cost metrics are **account-level** (per-campaign attribution awaits LeadChain fix).

---

## 1. 🚦 Delivery — GREEN (blackout recovered)

| Metric | 27 Jun |
|---|---|
| Spend | **₹25,423.73** |
| Impressions | 84,436 |
| Clicks | 742 |
| CTR | 0.88% |
| CPC | ₹34.26 |

Delivery is healthy and **above the typical ~₹17k/day**. The 26–27 Jun blackout has cleared — **26 Jun confirmed fully dark (0 leads)**, 27 Jun is back online.

## 2. Lead inflow — 83 leads (SURGE, +141% vs avg)

| | Value |
|---|---|
| Leads yesterday (27 Jun) | **83** |
| Trailing 7-day avg (20–26 Jun) | 34.4/day |
| Blackout-adjusted avg (excl. dark 26 Jun) | 40.2/day |
| Variance | **+141%** vs 7-day · +106% adj. |

No drop flag. Spike is a genuine post-blackout recovery on strong spend, not a sync artifact (duplicates only 3 of 83). Watch whether it normalises over 29–30 Jun.

## 3. Quality & funnel (27 Jun cohort, n=83)

| Stage | Count | Rate | Account cost |
|---|---|---|---|
| Valid leads | **25** | 30.1% | ₹1,017 / valid |
| Progressed (Negotiation + Proposal Sent) | **12** | 14.5% | ₹2,119 / progressed |
| Committed (Payment Wait) | 0 | — | — |
| **Won deal (W-Login)** | **1** | 1.2% | ₹25,424 / won* |
| Lost | 9 | 10.8% | — |
| Establishing Contact | 43 | 51.8% | — |
| Untriaged (blank status) | 8 | 9.6% | — |

\*One **same-day** Meta lead→win is a strong signal; cost-per-won will fall as the cohort matures (12 progressed + 11 proposals still open). Daily cost-per-won is not a mature metric — track the cohort in Zoho Analytics.

## 4. Speed-to-lead exceptions (status + age proxy)

51 leads sit untriaged/Establishing Contact. **8 never triaged** (blank status), aged overnight 12–22h. Top 10 (untriaged first, then oldest Establishing Contact):

| # | Name | Phone | Owner | Age | Status |
|---|---|---|---|---|---|
| 1 | BK Nayak | [phone redacted] | Kumar | 21.6h | ⚠ Untriaged |
| 2 | Raajeev | [phone redacted] | Kumar | 21.2h | ⚠ Untriaged |
| 3 | Pankaj Sharma | [phone redacted] | Tyagi | 21.1h | ⚠ Untriaged |
| 4 | Subodh Kumar | [phone redacted] | Kumar | 21.0h | ⚠ Untriaged |
| 5 | Pramod Pathe | [phone redacted] | Kumar | 20.1h | ⚠ Untriaged |
| 6 | Venugopal | [phone redacted] | Tyagi | 17.7h | ⚠ Untriaged |
| 7 | Pratik Ambilwade | [phone redacted] | Banerjee | 17.4h | ⚠ Untriaged |
| 8 | Hilash Nandilath | [phone redacted] | Pandey | 12.5h | ⚠ Untriaged |
| 9 | Rahul Ingole | [phone redacted] | Gupta | 22.9h | Establishing Contact |
| 10 | subhash | [phone redacted] | Kumar 3 | 22.5h | Establishing Contact |

> ⚠ True first-contact latency is **not instrumented** (completed calls log to Deals/Contacts, not back to the Lead). This is a status+age proxy. The 8 blank-status leads are the real red flag — never triaged, sitting overnight (Sat→Sun; weekend staffing likely a factor).

## 5. Loss buckets (9 losses)

| Why_Disqualified | n | Bucket |
|---|---|---|
| Duplicate Record | 3 | Natural attrition / data |
| Inquired by Mistake | 2 | Targeting / junk click |
| Other CA | 1 | Pricing / competition |
| Pricing | 1 | Pricing / competition |
| No Product Offering | 1 | Offer / serviceability |
| Language Issue | 1 | Geo / serviceability |

vs baseline (sales-process 51% · pricing/comp 32% · targeting 11%):
- **Sales-process losses: 0** — but the cohort is <24h old, so "Avoiding Call" leaks haven't had time to form. Not yet a real win.
- **"Avoiding Call" volume: 0** yesterday (the #1 historical leak — absent so far).
- Pricing/competition 2/9 (~22%), below the 32% baseline.
- With only 9 losses, bucket %s are noisy — treat as directional.

## 6. Recommendations (≤2)

**A. Sales-process (human, no Meta change, no approval needed) — triage the 8 blank-status leads this morning.**
They've aged 12–22h. Reassign/call within SLA before they decay into "Avoiding Call" losses.
*Confirms by:* untriaged count → 0 by EOD today; tomorrow's exception list shrinks; none of these 8 turn up as losses.

**B. Meta budget — HOLD, do not scale on one post-blackout day (needs approval if/when triggered).**
Yesterday's surge may be pent-up/catch-up demand after the blackout. Do **not** raise budget yet.
*Trigger to revisit:* if leads ≥60/day **and** valid% ≥28% hold for 29–30 Jun, then a **+15% budget test** (one variable, before/after screenshot, stop-loss at CPL > ₹450) is justified.
*Confirms by:* 3-day sustained valid-lead volume.

---
*Read-only run. No budgets, audiences, statuses, or bids were changed. No money moved.*
