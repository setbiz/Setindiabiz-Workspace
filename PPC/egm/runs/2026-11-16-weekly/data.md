# Data: weekly cycle, week ending 15 Nov 2026

W = Mon 9 – Sun 15 Nov 2026; P = 2–8 Nov 2026. IST. Pulled 16 Nov 2026 ≈10:20–10:45 IST by the scheduled run. Aggregates only, no personal data. Previous run: PR setbiz/Setindiabiz-Workspace#1 (`PPC/egm/runs/2026-11-09-weekly/`, not yet merged).

## T1. Meta daily account totals, W (Meta Ads connector, account 152154124583473, INR)
| Date | Spend ₹ | Impr. | Clicks | Meta leads |
|---|---|---|---|---|
| 9 Nov | 0 | 0 | 0 | — |
| 10 Nov | 0 | 0 | 0 | — |
| 11 Nov | 8,474.57 | 29,322 | 199 | 17 |
| 12 Nov | 16,571.93 | 61,159 | 396 | 34 |
| 13 Nov | 4,614.53 | 15,861 | 107 | 6 |
| 14 Nov | 0 | 0 | 0 | — |
| 15 Nov | 0 | 0 | 0 | — |
| **W total** | **29,661.03** | **106,342** | **702** | **57** |
P total (from PR #1 data.md T1): ₹33,898.29, 65,361 impr., 609 clicks, 50 form leads + 10 WhatsApp conversations.

## T2. Meta ad sets, W
| Ad set | Status 16 Nov | Budget ₹/day | Spend ₹ | Impr. | Clicks | CTR | CPM ₹ | Results | Cost/result ₹ |
|---|---|---|---|---|---|---|---|---|---|
| SIB-02 \| TM \| Lists \| Form \| 8C | Active | 3,000 | 6,582.10 | 23,135 | 157 | 0.68% | 284.51 | 24 leads | 274.25 |
| SIB-02 \| TM \| Interest \| Form \| 8C | Active | 1,000 | 1,815.43 | 8,332 | 59 | 0.71% | 217.89 | 8 leads | 226.93 |
| SIB-04 \| ACR \| … \| WhatsApp \| 19C | Active | 2,000 | 3,861.47 | 29,658 | 132 | 0.45% | 130.20 | 2 conversations | 1,930.74 |
| SIB-04 \| ACR \| … \| Form \| 19C | Active | 2,500 | 5,806.61 | 21,267 | 183 | 0.86% | 273.03 | 11 leads | 527.87 |
| SIB-01 \| INC \| Interest \| Form \| 18C | Active | 2,500 | 5,053.80 | 22,001 | 161 | 0.73% | 229.71 | 14 leads | 360.99 |
| SIB-05 Branch-Liaison / Subsidiary / India Entry (3) | Campaign paused 14 Nov | CBO 4,000 | 6,541.62 [calc] | 1,949 | 10 | — | ≈3,356 [calc] | 0 | — |
Daily budgets of active ad sets: **₹11,000** [calc 3,000+1,000+2,000+2,500+2,500].

## T3. Meta account status and log, 12 Nov 14:00 → 16 Nov
- `ads_get_errors` (16 Nov): **"Your ads have been paused because your prepaid funds are empty."**
- 12 Nov 14:06 ₹25,000 added (UPI) = ₹21,186.46 credit [calc ÷1.18] = 12 Nov + 13 Nov spend [calc]. Billed 13 Nov 06:58 ₹16,571.93; 14 Nov 06:41 ₹4,614.53.
- 11 Nov 10:18 ₹10,000 added = ₹8,474.58 credit = 11 Nov spend.
- 12 Nov 06:46–06:47: "ads MCP server" (Sanjeev's login) changed status on all 10 SIB-04 ads (GC05 Form/CTWA → Active; old ACR ads stay Inactive). Not in `meta/changelog.md` on main.
- 14 Nov 13:39: SIB-05 India Entry campaign → Inactive (paused) via "ads MCP server". Logged by the India-Entry session on branch `ppc/india-entry-2026-11-14` (PR #2), approver: owner.
- India-Entry session also staged a **draft** campaign `META_Leads_IndiaEntry_US_Founders_202612` (not live), per PR #2.

## T4. Zoho CRM paid-Meta leads created in W, by campaign × Lead_Status (COQL)
| Campaign | Valid Lead | Proposal Sent | Postponed | Lost | Establishing Contact | (empty) | Total |
|---|---|---|---|---|---|---|---|
| SIB-02 Trademark | 15 | 3 | 1 | 2 | 2 | 8 | 31 |
| SIB-01 Incorporation | 2 | 0 | 1 | 0 | 8 | 3 | 14 |
| SIB-04 Annual Filings | 2 | 0 | 1 | 1 | 4 | 5 | 13 |
| SIB-05 India Entry | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Total** | 19 | 3 | 3 | 3 | 14 | 16 | **58** |
By source: Advt - Facebook 20, Advt - Instagram 34, Advt - WhatsApp 4 (all W `Advt - FB/IG/WA` leads carry Meta_Campaign). QL (Valid + Proposal) = **22** [calc]; unworked (Establishing Contact + empty) = **30 = 52%** [calc].

## T5. Same for the P cohort (created 2–8 Nov), status as of 16 Nov (leads now 8–14 days old)
| Campaign | Valid | Proposal | Postponed | Lost | Est. Contact | (empty) | Total | QL | Unworked |
|---|---|---|---|---|---|---|---|---|---|
| SIB-02 | 7 | 5 | 1 | 5 | 3 | 4 | 25 | 12 | 7 |
| SIB-01 | 3 | 2 | 1 | 1 | 2 | 2 | 11 | 5 | 4 |
| SIB-04 | 4 | 1 | 0 | 0 | 4 | 1 | 10 | 5 | 5 |
| SIB-05 | 1 | 0 | 0 | 0 | 0 | 1 | 2 | 1 | 1 |
| **Total** | 15 | 8 | 2 | 6 | 9 | 8 | 48 | **23** | **17 (35%)** |
On 9 Nov the same cohort showed QL 22 and unworked 21 (PR #1 T8).

## T6. SIB-02 by ad set, leads created 2–15 Nov (CRM) vs spend 2–15 Nov (Meta)
| Ad set | Spend ₹ | CRM leads | QL | QL rate | ₹/CRM lead | ₹/QL | Lost |
|---|---|---|---|---|---|---|---|
| Lists | 12,336.97 | 42 | 25 | 60% | 294 | **493** | 5 |
| Interest | 3,393.42 | 14 | 5 | 36% | 242 | **679** | 2 |
[calc]. Spend = W (T2) + P (PR #1 T2).

## T7. Won deals, paid Meta (`Stage like W-*`, by Closing_Date)
| Window | Deals | ₹ |
|---|---|---|
| W (9–15 Nov) | 1 (#IND4 CCFS, old campaign) | 1,000 |
| 2–12 Nov (pulled 12 Nov) | 2 | 4,500 (a SIB-02 ₹2,500 deal moved from W-Login back to Qualified) |

## T8. ChatGPT Ads (Supermetrics CGPTA, account adacct_6a4a…5e57 "Setindiabiz Private Limited", INR) — newly authenticated
| Campaign | Status | Impr. | Clicks | Spend ₹ | Platform conv. |
|---|---|---|---|---|---|
| CFO Services | active | 6,305 | 159 | 1,544.64 | 1 |
| GST Filing | active | 4,304 | 95 | 569.94 | 1 |
| **Total W** | | 10,609 | 254 | **2,114.58** | 2 |
Querying 2–15 Nov returns identical rows, so **P spend was ₹0** (explains 0 ChatGPT CRM leads in P). Branch & Liaison campaign returns no rows.
CRM: `Advt - ChatGPT` leads created in W = **5** (Lead_Status: 4 empty, 1 Lost). Deals with `Lead_Source = Advt - ChatGPT` created since 1 Sep 2026: **none**.

## T9. Other platforms (Supermetrics, W)
| Platform | Result |
|---|---|
| Google Ads AW (1859576856) | No rows (no activity) |
| Microsoft Ads AC (150488150, 150329248) | No rows (no activity) |
| LinkedIn LIA, X TA, Reddit RDA | Not authenticated (missing) |
