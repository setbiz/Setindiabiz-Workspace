# Data — Meta audit 2026-11-02

All figures pulled 2026-11-02 (IST). Labels: [Meta] = Meta Ads connector, [Zoho] = Zoho CRM COQL, [calc] = computed from those numbers.

## Accounts [Meta]
10 ad accounts visible. Only **SETINDIABIZ (152154124583473, INR)** spent in the last 90 days: ₹4,50,928.67. The other 7 Setindiabiz accounts spent ₹0. "Setindiabiz - Salesiq" is not enabled for the connector. "KPS Corp" is not Setindiabiz.

## Campaigns with spend, last 90 days (≈4 Aug – 2 Nov 2026) [Meta]
| Campaign | ID | Status (2 Nov) | Spend ₹ | Impr. | Clicks (all) | CTR (all) | CPM ₹ | Freq. | Leads | CPL ₹ |
|---|---|---|---|---|---|---|---|---|---|---|
| #IND4 - CCFS | 120244101705120449 | Deleted 2 Nov | 1,72,140.77 | 994,964 | 5,906 | 0.59% | — | — | 396 | 434.70 |
| SIB-01 Incorporation | 120240912969660449 | ACTIVE | 1,20,201.98 | 532,038 | 5,280 | 0.99% | 225.93 | 2.21 | 687 | 174.97 |
| SIB-04 Annual Filings | 120246968311680449 | PAUSED 2 Nov (via ads MCP) | 80,521.16 | 339,996 | 3,872 | 1.14% | 236.83 | 2.11 | 140 | 575.15 |
| #IND3 - Trademark | 120243118117990449 | Deleted 2 Nov | 44,622.48 | 249,378 | 2,272 | 0.91% | — | — | 346 | 128.97 |
| SIB-05 India Entry | 120247067847480449 | ACTIVE, ₹4,000/day, "Highest volume" | 22,760.28 | 7,319 | 84 | 1.15% | 3,109.75 | 3.04 | 6 | 3,793.38 |
| SIB-02 Trademark (new) | 120247094837400449 | ACTIVE | 7,408.29 | 35,968 | 448 | 1.25% | 205.97 | 1.74 | 87 | 85.15 |
| SIB-02 Trademark (old) | 120247048085410449 | Archived | 3,273.71 | 15,224 | 185 | 1.22% | — | — | 28 | 116.92 |
| **Total** | | | **4,50,928.67** | | | | | | **1,690** | **266.82 [calc]** |

## Zoho CRM, same window (created 4 Aug – 2 Nov 2026) [Zoho]
Leads: Advt - Facebook 892, Advt - Instagram 623, Advt - WhatsApp 336, so **1,851** in total. Meta reported 1,690 platform leads.

Deals created in the window, by won stage (assumption: `W-*` stages = won):
| Source | Won deals | Won ₹ |
|---|---|---|
| Advt - Facebook | 37 (W-SKV 12, W-Login 12, W-Finance 7, W-SPI 5, W-CSD 1) | 4,00,371 |
| Advt - Instagram | 21 (W-SKV 9, W-Finance 6, W-Login 4, W-SPI 2) | 1,98,043 |
| Advt - WhatsApp | 3 (W-Login) | 52,625 |
| **Total** | **61** | **6,51,039** |
Also: Qualified (open) 7, Refunded 1.

[calc]: revenue/spend = **1.44×**; cost per won deal ₹7,392; AOV ₹10,673; lead→won 3.3% (61/1,851). Break-even needs a gross margin of ≥69.3% on the `Amount` field. `Amount` may include govt fees (unconfirmed). Pipeline lag means late-October leads may still close, so this understates the outcome.
**Gap:** Zoho has no campaign-level attribution, so won deals can't be tied to SIB-01 / SIB-02 / SIB-04 / SIB-05.

## Meta Opportunity Score [Meta]: 61/100
Top recommendations by points: Advantage+ creative enhancements bundle (9 pts, "3% lower cost per result"); **fragmentation in SIB-05's 3 ad sets** (5 pts); **Conversions API for CRM** (4 pts, "24% lower cost per quality lead"); auto-music (3 pts); AI images, Reels 9:16, mixed formats (1–2 pts each); messaging events (1 pt).

## Performance trend (ad set, Meta fixed 28-day comparison) [Meta]
- SIB-02 | TM | Interest | Form | 8C: CPR improved 6.16%, CVR +25.18%, CTR +7.67%, CPM worse (+18.41%).
- SIB-01 | INC | Interest | Form | 18C: CPR improved 48.39%, CVR +78.69%, CTR +24.81%; ROAS flagged worse (−62.32%).

## Activity log, 21 Oct – 2 Nov 2026 (150 most recent entries) [Meta]
- **Customer-list custom audiences created** 31 Oct–2 Nov: "Meta_GST_All_Contacts.csv", "GST - Company/LLP/Firm/Proprietorship.csv", "LLP 2026-27". Existing lists include "Company Director 2022-23 … 2024-25" and "LLP 2021-22 … 2024-25". These are used in SIB-04 ACR ad sets (Directors + GST Co) and were **added today to "SIB-02 | TM | Lists | Form | 8C"**.
- 2 Nov: #IND3, #IND4, #IND5 deleted (Power Editor). SIB-04 set to inactive by "ads MCP server", i.e. another AI-assistant session.
- 2 Nov: SIB-02 TM Interest ad set budget changed (old ₹1,200; new value truncated in log) and targeting/locations changed.
- 21 Oct: SIB-05 ads activated by "ads MCP server", including "S1 | From USD 499".
- No automated-rule events in this window, so business-hours rules / #HOLD can't be verified from the log.

## ADDENDUM (after Goldfish round 1): campaign-level CRM backfill [Zoho `Meta_Campaign` field on Deals]
Deals created 4 Aug–2 Nov 2026, Lead_Source Advt-FB/IG/WA, won = `W-*` stages. Sum = ₹6,51,039, matching the total above.
| Zoho Meta_Campaign | Won deals | Won ₹ | Meta spend ₹ (90d) | Revenue/spend [calc] | Cost/won ₹ [calc] | AOV ₹ [calc] |
|---|---|---|---|---|---|---|
| #IND4 - CCFS | 18 | 4,34,619 | 1,72,141 | **2.52×** | 9,563 | 24,145 |
| SIB-04 Annual Filings | 6 (+1 Qualified) | 86,125 | 80,521 | 1.07× (launched 9 Oct; pipeline open) | 13,420 | 14,354 |
| #IND3 - Trademark | 18 | 37,533 | 44,622 | 0.84× | 2,479 | 2,085 |
| SIB-02 Trademark (+ "- Copy") | 3 | 6,500 | 10,682 | 0.61× (early) | 3,561 | 2,167 |
| #IND 1 — Incorporation (**assumed = SIB-01**, renamed; confirm) | 7 | 30,368 | 1,20,202 | **0.25×** | 17,172 | 4,338 |
| #IND 1 — Business Registration - Lead | 2 | 3,500 | (not in 90d spend) | — | — | — |
| #IND5 - DPIIT | 3 | 28,698 | 0 in window (older leads) | — | — | — |
| #IND2 — Annual Returm - Lead | 1 | 5,000 | 0 in window | — | — | — |
| (blank, likely WhatsApp) | 3 | 18,696 | — | — | — | — |
| SIB-05 India Entry | 0 | 0 | 22,760 | 0× | — | — |
SIB-01 lead→won ≈ 7/687 = 1.0% [calc, Meta leads].

By Zoho `Product_Category`, won ₹: Annual Filing 15 deals ₹4,52,192; Striking Off 7 ₹91,348; TM Filing in India 20 ₹40,233 (AOV ≈₹2,012); Start Company 6 ₹29,565; DPIIT 1 ₹4,999; others small.
**Reading:** compliance and deadline work (CCFS, annual filing, striking off) drives ~84% of Meta-attributed revenue. Incorporation and trademark have low AOV and lose money at current CPLs, even before margin.

## ADDENDUM: live ad copy (Meta creatives, ACTIVE) [Meta]
- Annual filing creatives (created 1 Nov, for SIB-04): "Annual filing pack ₹7,499 + GST … Government fees at actuals … Setindiabiz is a private firm, not affiliated with MCA". Deadlines cite Companies Act 2013 ss. 137(1), 92(4), 403. **Claim "Setindiabiz has served 25,000+ businesses"** conflicts with the website's "18K+ clients".
- India entry (SIB-05): branch office / liaison office copy states RBI eligibility (USD 100k / 50k net worth). "Indian subsidiary from USD 499 … Government fees, stamp duty and DSC extra, at actual cost". Transparent wording; price must be honoured in quotes.
- Active ad names: "INC-F1 | Rs2499 + GST | Form" (SIB-01, ₹30,109 last 30d, CPL ₹175), "TM-F1 | Rs1999 + GST | Form | Interest" (SIB-02), "TM-F1 | … | Lists" (₹0 spend so far, uses customer lists).
