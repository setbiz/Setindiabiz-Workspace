# Re-analysis, 12 Nov 2026 14:20 IST (owner asked "reanalyse")

Sources: Meta Ads connector (account 152154124583473) and Zoho CRM COQL, pulled 12 Nov 14:15–14:20 IST. Aggregates only. Read-only: nothing was changed.

## What happened since the 9 Nov review
| When (IST) | Event | Source |
|---|---|---|
| 6–10 Nov | Account dark (₹0 spend every day) | Meta daily insights |
| 11 Nov 10:18 | ₹10,000 added (UPI) = ₹8,474.58 credit [calc ÷1.18] | Activity log |
| 11 Nov | Spent **₹8,474.57**, credit used to the paisa, so dark again | Daily insights |
| 12 Nov 06:46–06:47 | **"ads MCP server" (an AI session under Sanjeev's login)** changed status on all 10 SIB-04 ads: GC05 Form + CTWA → Active; old ACR-C1/C2/C5 stay Inactive. **Not in `meta/changelog.md`**; the session is not identified | Activity log |
| 12 Nov 14:06 | ₹25,000 added (UPI) = ₹21,186 credit [calc] | Activity log |
| 12 Nov 14:17 | No delivery errors; ads are delivering again | `ads_get_errors` = [] |

None of the 9 Nov actions (A1–A8) have been applied: SIB-01 is still at ₹2,500/day and SIB-05 has no cap.

## 11 Nov (one partial day, from 10:18 until the credit ran out), by ad set
| Ad set | Budget ₹/day | Spend ₹ | Clicks | CTR | Meta results | Cost/result ₹ |
|---|---|---|---|---|---|---|
| SIB-02 TM Lists | 3,000 | 1,876.11 | 34 | 0.59% | 5 leads | 375 |
| SIB-02 TM Interest | 1,000 | 592.35 | 16 | 0.67% | 4 leads | **148** |
| SIB-04 Form | 2,500 | 1,517.03 | 54 | 1.06% | 4 leads | 379 |
| SIB-04 WhatsApp | 2,000 | 1,171.81 | 43 | 0.49% | 1 conversation | 1,172 |
| SIB-05 (3 ad sets, CBO ₹4,000) | 4,000 | 1,908.36 [calc] | 5 | — | 0 | — |
| SIB-01 INC | 2,500 | 1,408.91 | 47 | 0.70% | 4 leads | 352 |
| **Total** | 15,000 | **8,474.57** | 199 | 0.68% | 17 leads + 1 conv. | 499 per lead [calc] |
Directional only (one partial day).

## Running totals since the 2 Nov changes (2–11 Nov)
- Meta spend **₹42,372.86** [calc 33,898.29 + 8,474.57]; Meta leads 67 (account `lead`).
- CRM paid-Meta leads created 2–12 Nov: **67** (SIB-02 34, SIB-04 16, SIB-01 15, SIB-05 2). Meta and CRM match.
- Cost per CRM lead **₹632** [calc]. Qualified (Valid Lead + Proposal Sent) **27** → **₹1,569 per QL** [calc] (SIB-02 16, SIB-04 6, SIB-01 5, SIB-05 1).
- **Not yet worked (Establishing Contact or empty): 32 of 67 = 48%** [calc], up from 21 on 9 Nov. SIB-02 13, SIB-01 9, SIB-04 9, SIB-05 1. A1 (clear the backlog) has not happened.
- Won deals (paid Meta, closed 2–12 Nov): **2, ₹4,500**. The SIB-02 ₹2,500 deal counted as W-Login on 9 Nov is now "Qualified" (stage reversed in Zoho), so the 9 Nov figure of 3 / ₹7,000 is superseded.

## Urgent, in order
1. **SIB-05 reaches the owner's ₹15,000 cap tonight.** Spend since 2 Nov is ₹13,829.87 [calc 11,921.51 + 1,908.36], so **₹1,170 remains**. At the ₹4,000/day budget that is ≈7 hours of delivery, around 21:00 IST today (estimate). Decide now: campaign spending limit, pause, or raise the cap. 9 Nov action A3.
2. **The new ₹25,000 runs out around tomorrow evening.** ₹21,186 credit ÷ ₹15,000/day ≈ 1.4 days [calc]. With A3 + A4 (SIB-05 capped, SIB-01 at ₹1,250) it is ÷ ₹9,750 ≈ 2.2 days [calc], which reaches into Saturday. As it stands the weekend will be dark again. Since 2 Nov the account has delivered on only 5 of 11 days.
3. **Lead backlog grew to 32.** The sales team needs to work these before more spend is added. SIB-04 is deadline-season: AOC-4 is due by 31 Dec 2026 without additional fee (MCA GC 05/2026).
4. **An unlogged AI change on 12 Nov 06:46.** Find which Claude session ("ads MCP server") changed the SIB-04 ads. The daily Cowork lead-quality watch is meant to be read-only. Add the change to `meta/changelog.md`.

## Early signals (directional, small n)
- SIB-02 Interest is the cheapest lead source on both reads (₹263 on 2–8 Nov, ₹148 on 11 Nov) vs Lists at ₹288 and ₹375. That supports merging Lists into Interest, not the other way round as the 9 Nov CFO note suggested, at the post-hold decision point.
- SIB-04 WhatsApp got 1 conversation for ₹1,172 on 11 Nov (10 for ₹4,949 on 2–8 Nov). It is weakening while the CRM capture question (A5) is still open.
- SIB-05: ₹1,908 for 0 leads on 11 Nov. Total since 2 Nov: ₹13,830 → 2 CRM leads, 1 valid.
