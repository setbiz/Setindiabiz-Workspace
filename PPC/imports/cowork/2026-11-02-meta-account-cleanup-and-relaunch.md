# Meta Ads session log: 2 Nov 2026

> **Provenance: reconstruction, not a transcript.** The chat where this work happened could not be opened. This file is built from:
>
> - **[LOG]** Meta activity log, account 152154124583473, 31 Oct 2026 00:00 to 2 Nov 2026 17:45 IST. All times are IST.
> - **[LIVE]** Live read of the account on 2 Nov 2026, after 17:45 IST.
> - **[NOTES]** Saved project notes, last updated 2 Nov 2026 at 11:37 IST, and the weekly paid-channel report notes.
> - **[REPO]** `setbiz/Setindiabiz-Workspace` at commit 3452bd1: `PPC/meta/changelog.md`, `PPC/meta/quality-lead-settings-playbook.md` and `PPC/egm/runs/2026-11-02-meta-audit/`.
>
> Nothing here comes from the conversation itself. Reasons come from [NOTES] and [REPO], and anything they don't explain is marked as not recorded.

## 1. Platform

Meta Ads (Facebook and Instagram). Account "SETINDIABIZ", ID 152154124583473, billed in INR on prepaid balance.

## 2. Date range

- **Changes covered:** 31 Oct 2026 to 2 Nov 2026 (main work on 2 Nov, 10:43 to 17:44 IST)
- **Performance baseline:** 26 Oct to 1 Nov 2026
- **Partial-day metrics:** 2 Nov 2026

## 3. What we analysed

The notes and log show work on these areas. The depth of any analysis is not recorded.

- Trademark audience setup: interest ad set versus a list-based ad set
- Unused campaigns, ad sets and ads to remove
- Outdated custom audiences against the marketing data in `G:\Shared drives\1. SKAC - Marketing Data\Raw Data`
- SIB-04 Annual Filings audience
- Naming across campaigns, ad sets and ads
- Weekly paid-channel performance for 26 Oct to 1 Nov
- Meta audit with CRM backfill, about 4 Aug to 2 Nov 2026 [REPO]. Won-deal figures by campaign are in that run's `data.md` and are not repeated here

## 4. Every change made in the ad account

"Tool" is the log's application name. All user changes are logged under Sanjeev Kumar. Meta's automatic review events are summarised, not listed one by one. The log also has system billing events: `Account refunded` on 1 Nov at 08:57 and 10:55, and `Account billed` three times on 2 Nov at 06:21. Their logged amounts (1 or 2) cannot be read reliably as rupees, so they are not listed as changes.

### 31 Oct 2026: GST custom audiences created

| Time | Audience (final name) | Created as | Rows received |
|---|---|---|---:|
| 13:55 to 14:00 | GST - Other Business Types | Meta_GST_All_Contacts.csv | 7,075,148 |
| 14:08 to 14:09 | GST - Company | GST - Company.csv | 784,822 |
| 14:11 | GST - LLP | GST - LLP.csv | 203,591 |
| 14:12 | GST - Firm | GST - Firm.csv | 50,354 |
| 14:15 to 14:16 | GST Proprietorship | GST - Proprietorship.csv | 464,718 |

Renamed to their final names between 14:00 and 14:25. Tool: Power Editor.

### 2 Nov 2026: budget and Trademark rebuild

| Time | Object | Change | Tool |
|---|---|---|---|
| 08:26 | Account balance | ₹25,000 added by UPI | Meta log |
| 10:43 | SIB-02 \| TM \| Lists \| Form (ad set) | Created at ₹3,000/day, performance goal Conversions, automatic bidding | Power Editor |
| 10:43 | TM-F1 \| Rs1999 + GST \| Form \| Lists (ad) | Created | Power Editor |
| 10:43 | SIB-02 \| TM \| Form \| IN - Copy (ad set) | Budget ₹1,200 → ₹1,000/day | Power Editor |
| 10:43 | Same ad set | Cities 30 → 8; Optimize locations On → Off; age 25-55 → 25-45; Advantage+ audience On → Off; Advantage+ lookalike Off | Power Editor |
| 10:45 | Both TM ads | Approved by Meta | Meta |
| 12:35 | TM-F1 \| Rs1999 + GST \| Form \| Lists | Started delivery | Meta |

### 2 Nov 2026: deletions, 10:57 to 11:03 (Power Editor)

**Campaigns (3):** `#IND3 - Trademark`, `#IND4 - CCFS`, `#IND5 - DPIIT`

**Ad sets (8):**

- `C1 - 24Hr LAL1% Director - Company INC`
- `C1 - Daytime INSA Company INC`
- `C1 - Daytime - LAL1% Director - Company INC`
- `C3 Adset - TMF - SA - Web + Form`
- `C3 Adset - Director - TMF - Web + Form`
- `C3 Adset - Director - TMF - Web + Form | Restart Oct`
- `C4 Adset - Director CCFS + Form`
- `C4 Adset - Director DPIIT + Form`

**Ads (22):**

- `#C5 DPIIT 1`, `2`, `3`, `4`
- `#C4 CCFS - 1`, `2`, `3`, `4`
- `#C3A TM Ad 1` to `7`
- `#C3B TM Ad 1`, `2`
- `Ad-1 Lead - Company Registration` (4 separate ads)
- `Ad-1 Lead - Company Registration - Copy`

### 2 Nov 2026: pause, renames and SIB-04 audience

| Time | Object | Change | Tool |
|---|---|---|---|
| 11:35 | SIB-04 Annual Filings (campaign) | Active → Inactive | ads MCP server |
| 12:51 | Campaign | `#IND 1 — Incorporation` → `SIB-01 Incorporation` | Power Editor |
| 12:51 | Campaign | `SIB-02 Trademark - Copy` → `SIB-02 Trademark` | Power Editor |
| 12:51 | Ad set | `C1 - 24Hr INSA Company INC` → `SIB-01 \| INC \| Interest \| Form \| 18C` | Power Editor |
| 12:51 | Ad set | `SIB-02 \| TM \| Form \| IN - Copy` → `SIB-02 \| TM \| Interest \| Form \| 8C` | Power Editor |
| 12:51 | Ad set | `SIB-02 \| TM \| Lists \| Form` → `SIB-02 \| TM \| Lists \| Form \| 8C` | Power Editor |
| 12:51 | Ad set | `SIB-04 \| ACR \| Directors \| Form \| 19C` → `SIB-04 \| ACR \| Directors + GST Co \| Form \| 19C` | Power Editor |
| 12:51 | Ad set | `SIB-04 \| ACR \| Directors \| WhatsApp \| 19C` → `SIB-04 \| ACR \| Directors + GST Co \| WhatsApp \| 19C` | Power Editor |
| 12:51 | Both SIB-04 ad sets | Custom audience `GST - Company` added | Power Editor |
| 12:52 | Ad | `Ad-2 Lead - Company Registration` → `INC-F1 \| Rs2499 + GST \| Form` | Power Editor |
| 12:52 | Ad | `TM-F1 \| Rs1999 + GST \| Form - Copy` → `TM-F1 \| Rs1999 + GST \| Form \| Interest` | Power Editor |

### 2 Nov 2026: custom audience refresh (Power Editor)

All entries are logged as `operation: add`. Rows received is not the match count.

| Time | Audience | Rows received |
|---|---|---:|
| 13:08 to 13:09 | LLP 2026-27 (**created**) | 71,434 |
| 15:41 | Company Director 2026-27 | 126,940 |
| 15:42 | Company Director 2019-20 | 102,050 |
| 15:43 | Company Director 2020-21 | 138,403 |
| 15:44 | Company Director 2021-22 | 170,452 |
| 15:45 | LLP 2021-22 | 80,803 |
| 15:46 | LLP 2019-20 | 74,136 |
| 15:48 | LLP 2020-21 | 96,398 |
| 15:49 | Company Director 2022-23 | 233,527 |
| 15:51 | LLP 2022-23 | 76,601 |
| 15:52 | Company Director 2023-24 | 557,303 |
| 15:53 | LLP 2023-24 | 130,711 |
| 15:55 | Company Director 2024-25 | 615,036 |
| 15:56 | LLP 2024-25 | 144,708 |
| 15:57 | Company Director 2025-26 | 459,351 |
| 15:58 | LLP 2025-26 | 199,132 |
| 16:00 to 16:04 | GST 2025-26 (5 batches: 500,001 × 4, then 437,578) | 2,437,582 |
| 16:05 to 16:07 | GST 2026-27 (3 batches: 500,001 × 2, then 289,319) | 1,289,321 |

### 2 Nov 2026: reactivation and evening targeting batch (ads MCP server)

| Time | Object | Change |
|---|---|---|
| 17:16 | SIB-04 Annual Filings (campaign) | Inactive → Active |
| 17:37 | SIB-01 \| INC \| Interest \| Form \| 18C | Budget ₹2,500 → ₹1,250/day |
| 17:37 | Same ad set | Placements cut to feed, Stories and Reels; narrowing now behaviours AND education, `Industry: Business Decision Makers` removed from narrowing; `Minimum age: 25` line removed, age stays 25-45; Advantage+ audience On → Off; Advantage+ lookalike Off |
| 17:37 | SIB-02 \| TM \| Interest \| Form \| 8C | Placements cut to feed, Stories and Reels |
| 17:37 | SIB-02 \| TM \| Lists \| Form \| 8C | Added behaviours AND education narrowing; Advantage+ lookalike Off |
| 17:37 | SIB-05 India Entry, Subsidiary and Branch-Liaison ad sets | Age 25-65+ → 25-45; languages `English (US), Japanese, Korean or English (UK)` → `English (US) or English (UK)`; removed `Lead Gen Multi Submit Ads on Instagram`; narrowing `Industry: Business Decision Makers` replaced with education |
| 17:37 | Both SIB-04 ad sets | Age 25-60 → 25-45; added behaviours AND education narrowing; removed `Lead Gen Multi Submit Ads on Instagram` from the Form ad set |
| 17:40 | Both SIB-04 ad sets | Age 25-45 → 25-55 |

Affected ads went back through review. By 17:44 Meta had approved all of them except `ACR-C2 | Cost of delay | CTWA | Dir`, which [LIVE] still shows as `PENDING_REVIEW`.

## 5. Results and metrics observed

### Week 26 Oct to 1 Nov 2026 [NOTES]

Meta delivered 2 of 7 days, on 27 and 28 Oct, then ran out of prepaid balance.

| Metric | Value |
|---|---:|
| Spend | ₹16,949.19 |
| Impressions | 41,369 |
| CRM leads | 47 (₹361 each) |
| Valid leads | 19 (₹892 each) |
| Leads not yet quality-scored | 36% |
| Platform results vs CRM leads | 53 vs 47 (11% gap, no flag) |

₹892 is a ceiling because 36% of leads were unscored.

| Campaign (name then) | Spend | CRM leads | Valid | ₹ per valid |
|---|---:|---:|---:|---:|
| SIB-02 Trademark - Copy | ₹1,307.62 | 15 | 6 | ₹218 |
| #IND 1 Incorporation | ₹3,438.70 | 24 | 10 | ₹344 |
| SIB-04 Annual Filings | ₹6,964.69 | 6 | 2 | ₹3,482 |
| SIB-05 India Entry | ₹5,238.18 | 2 | 1 | ₹5,238 |

Previous week, 19 to 25 Oct: ₹57,940.48 spend, 187 CRM leads, 64 valid, ₹310 per lead, ₹905 per valid.

### 2 Nov 2026, partial day [LIVE]

These are platform figures, not CRM outcomes, so they are not a performance verdict. Most of this spend came before the 17:37 changes. WhatsApp conversations were not pulled, so blank leads on the WhatsApp ad set do not mean no chats.

| Ad set | Daily budget | Spend | Impressions | Leads (Meta) |
|---|---:|---:|---:|---:|
| SIB-01 \| INC \| Interest \| Form \| 18C | ₹1,250 | ₹1,495.18 | 5,084 | 1 |
| SIB-02 \| TM \| Lists \| Form \| 8C | ₹3,000 | ₹896.19 | 2,647 | 6 |
| SIB-02 \| TM \| Interest \| Form \| 8C | ₹1,000 | ₹309.63 | 1,112 | none |
| SIB-04 \| ACR \| Directors + GST Co \| Form \| 19C | ₹2,500 | ₹468.12 | 629 | none |
| SIB-04 \| ACR \| Directors + GST Co \| WhatsApp \| 19C | ₹2,000 | ₹609.75 | 1,613 | none |
| SIB-05 \| India Entry \| Form \| INTL | shared | ₹257.05 | 56 | none |
| SIB-05 \| Subsidiary \| Form \| INTL | shared | ₹485.19 | 132 | 1 |
| SIB-05 \| Branch-Liaison \| Form \| INTL | shared | ₹1,784.67 | 409 | 1 |
| **Total** | **₹13,750** | **₹6,305.78** | **11,682** | **9** |

SIB-05 uses a ₹4,000/day campaign budget, counted once in the total. Only four campaigns now show as active or paused, and all four are active. The Ads Manager draft read returned no drafts for this user.

## 6. Decisions and reasoning

Reasons are shown only where the notes record one.

| Decision (2 Nov unless dated) | Recorded reasoning |
|---|---|
| Fix Trademark first, then the other campaigns | Not recorded |
| Trademark audience: saved audience of all company directors and LLP partners, plus all GST saved audiences | Not recorded |
| Run a list-based ad set alongside the interest ad set, at ₹3,000 and ₹1,000/day | Not recorded. The notes say budgets were briefly ₹500/₹2,500, but [LOG] shows no such change |
| Both TM ad sets: male, 25-45, 8 cities, Advantage+ off | Not recorded |
| Trademark runs 24x7 | No Sunday or 8 PM-9 AM delivery was considered first. Sanjeev says his experience with 24x7 has not been encouraging because of connectivity |
| Delete, not archive, marked unused campaigns, ad sets and ads, plus the unpublished Trademark and Incorporation WhatsApp ad drafts | He wanted abandoned or unused objects removed |
| Pause SIB-04, add `GST - Company`, resume later | Sanjeev's own decision; reason not recorded [NOTES] |
| Reactivate SIB-04 at 17:16 | MGT-7/7A season. CRM, 90 days: CCFS 2.52×, Annual Filing product ₹4.52L won [REPO]. Now affected by item 1 in section 7 |
| Name campaigns, ad sets and ads properly | Not recorded |
| Refresh outdated custom audiences from Drive | Audiences were outdated |
| 17:37 layer-2 targeting on all 8 ad sets | Owner's playbook of "settings that helped get quality leads"; expected higher quality and lower volume [REPO] |
| SIB-01 budget ₹2,500 → ₹1,250/day | Owner-approved 50% cut. CRM, 90 days: 7 won from 687 leads, ₹30,368 on ₹1,20,202 (0.25×) [REPO] |
| SIB-04 age 25-45 → 25-55 | Owner request, to keep older directors in the audience for the MGT-7 deadline [REPO] |
| Keep customer-list audiences live | Owner accepted the data-protection position for now and declined the audit's pause [REPO] |
| Keep SIB-05 running with a further ₹15K cap | India-entry deal value about ₹86,300; judge on CRM-qualified leads [REPO] |
| Standing principle, 16 Oct | "we must work towards good quality consistently over time, cost will come down" |

## 7. Open items and next steps

### Fix first

1. **All six SIB-04 ads need rewriting.** MCA General Circular No. 05/2026 dated 24 Oct 2026 allows FY 2025-26 AOC-4 forms to be filed by 31 Dec 2026 and MGT-7/7A by 31 Jan 2027 with no additional fee. It does not extend AGM timelines. Secondary summaries say additional fees after those windows run from the original due dates under Secs. 137(1) and 92(4), Companies Act, 2013.
   - `ACR-C1` and `ACR-C5` (Form and CTWA) state 30 October and 29 November. `ACR-C5` adds "After that, ₹100 a day per form".
   - `ACR-C2` (Form and CTWA) says late filing costs ₹100 a day and does not mention the relief.
   - A wrong deadline or fee claim is a risk under Consumer Protection Act, 2019 s. 2(28). The 29 Nov reasoning and the review plan in `PPC/meta/changelog.md` also need updating.
   - **Source check:** the circular's number appears on mca.gov.in, but its PDF could not be opened. Dates are from secondary summaries, so confirm them against the original first.
2. **Prepaid balance.** Current budgets total ₹13,750/day. ₹25,000 covers about 1.8 days, and ₹6,305.78 has already been spent today. The notes call 26 Oct to 1 Nov the sixth straight week of prepaid exhaustion.
3. **LLP 2026-27 is missing from `SIB-02 | TM | Lists | Form | 8C`.** It was created today but is not in the ad set's audience list.
4. **`ACR-C2 | Cost of delay | CTWA | Dir` is still in review.** Confirm it clears.

### Check

5. **CRM attribution after renames.** Meta leads are attributed through the Zoho `Meta_Campaign` field (LeadChain). Check whether old and new names now split across reports, and whether the Product Name and Product Cat function depends on campaign or ad names.
6. **SIB-05 Japan and South Korea.** Both are still targeted, but Japanese and Korean were removed from languages. Confirm that English-only there is intended.
7. **SIB-05 countries.** Seven are live: US, JP, CA, SG, KR, AE, AU. The 10 Oct decision covered 10 countries and kept Germany, Netherlands and UK after a privacy policy check. Confirm whether those three are still planned.
8. **Trademark headline.** Sanjeev's earlier instruction was to lead on credentials, not low fee. The live headline is `Trademark Filing @ ₹1,999 + GST`.
9. **SIB-04 spend limit.** The audit proposed a ₹25,000 total cap and a kill rule of CPL above ₹600 after ₹8,000. The changelog records only a maximum of about ₹1.2L. Confirm which applies.
10. **Budget intent.** Earlier notes put domestic at ₹6,500/day, annual return at ₹6,000/day and FDI at ₹4,000/day. Live budgets are different, and SIB-01 was halved today. Confirm the current plan.
11. **Changelog gaps.** `PPC/meta/changelog.md` does not yet cover the Trademark rebuild, deletions, renames, the `GST - Company` addition, the 11:35 pause or the audience refresh. `PPC/CLAUDE.md` also requires a recorded source, notice, purpose and approver for list uploads.
12. **Naming.** Live names follow the `SIB-NN` pattern below, not the `<Platform>_<Objective>_<Service>_<Geo>_<Audience>_<YYYYMM>` convention in `PPC/CLAUDE.md`. Decide which one stands.

### Audit questions this answers

- `#IND 1 — Incorporation` is SIB-01. [LOG] shows campaign 120240912969660449 renamed at 12:51.
- SIB-04 was paused on Sanjeev's decision, carried out through the ads MCP server at 11:35 [LOG, NOTES].

### Next

13. Judge the new setup on CRM valid leads in the weekly report, not on Meta leads.
14. Include the renamed campaigns and the deleted `#IND3`, `#IND4` and `#IND5` objects when reconciling windows that overlap their delivery.

## 8. Reusable learnings

- **Check dates in the copy before reactivating.** A paused campaign can come back with a deadline that has already passed.
- **Check MCA circulars before using a statutory date in ads.** Circular 05/2026 changed the no-fee windows 9 days before SIB-04 was reactivated.
- **Batch targeting edits.** Each edit sent ads back through review. ACR ads were reviewed up to three times today, at about 12:52, 17:38 and 17:41.
- **Treat notes as intent and the activity log as fact.** Today's notes and log disagree on at least one budget, and some decisions came after the last note.
- **Compare prepaid balance with the sum of daily budgets** before each top-up or launch.
- **Check new audiences are attached.** Creating an audience does not add it to existing list-based ad sets.
- **Read large list uploads as batches.** The GST lists appear in the log as batches of 500,001 rows. Rows received is not the matched audience size.
- **Naming pattern now in use:** `SIB-NN | Product | Audience | Destination | nC`, where `nC` is the city count. Ad names follow `PRODUCT-Variant | Angle | Destination | Audience`.
- **Check what depends on names** before bulk-renaming campaigns or ads.

---

## Appendix A: live audience settings, verbatim

Meta has no keywords, so interests, job titles and behaviours are listed instead. Settings are from [LOG] final values, and location types are from [LIVE].

### Common placements

SIB-01 and SIB-02 (location types: `frequently_in`, `home`, `recent`):

```text
on pages: Feed on desktop computers, Instagram feed, Instagram Stories, Instagram Reels, Instagram Web Feed, Instagram Web Stories, Instagram Msite Stories, Feed on mobile devices, Facebook Stories on mobile devices or Facebook Reels
```

SIB-04 and SIB-05 (location types: `home`, `recent`, except the SIB-04 WhatsApp ad set, which also has `frequently_in`):

```text
on pages: Feed on desktop computers, Instagram feed, Instagram Stories, Instagram Reels, Feed on mobile devices, Facebook Stories on mobile devices or Facebook Reels
```

Common narrowing on all eight ad sets:

```text
And must also match: Behaviors: Small business owners or Facebook Page admins
And must also match: Education level: College grad, Master's degree, Professional degree or Doctorate degree
Language: English (US) or English (UK)
Advantage+ audience: Off
```

### SIB-02 | TM | Lists | Form | 8C

₹3,000/day. Goal `OFFSITE_CONVERSIONS`, destination `WEBSITE_AND_LEAD_FORM`.

```text
Custom audience: LLP 2024-25, LLP 2023-24, LLP 2022-23, LLP 2021-22, Company Director 2024-25, Company Director 2023-24, Company Director 2022-23, Company Director 2021-22, GST 2025-26, LLP 2025-26, LLP 2020-21, LLP 2019-20, Company Director 2019-20, Company Director 2020-21, Company Director 2025-26, Company Director 2026-27, GST 2026-27, GST - Other Business Types, GST - Company, GST - LLP, GST - Firm or GST Proprietorship
Location: India: Delhi (+25 mi) Delhi; Ahmedabad (+25 mi) Gujarat; Gurugram (+25 mi) Haryana; Mumbai (+25 mi), Pune (+25 mi) Maharashtra; Bangalore (+25 mi) Karnataka; Noida (+25 mi) Uttar Pradesh; Hyderabad (+25 mi) Telangana
Optimize locations: Off
Age: 25 - 45
Gender: Male
Advantage+ lookalike: Off
```

### SIB-02 | TM | Interest | Form | 8C

₹1,000/day. Goal `OFFSITE_CONVERSIONS`, destination `WEBSITE_AND_LEAD_FORM`. Location, age, gender and Optimize locations as above.

```text
People who match:
Interests: Small business, Amazon.com, Brand management, Senior management, Online marketplace, Graphic design, Drop shipping, Product design, E-commerce, Shopify, LinkedIn, Jewelry, Fashion design, Marketing, Venture capital, Board of directors, Private equity, Startup company, Initial public offering, Fashion accessories, Flipkart, Entrepreneurship, Brand, Investment, Social media marketing, Business, Packaging and labeling, Trade, Advertising, Retail or Marketing services and organizations
Field of study: Corporate Finance
Job title: Chief executive officer, Chief marketing officer, Designer, Creative director, Chairman, Partner, Angel investor, Owner, Vice President, Chief financial officer, Proprietor, Managing Partner, Co-Founder/Producer, Founder or Managing Director
Industry: Business Decision Makers
Advantage+ lookalike: Off
```

### SIB-01 | INC | Interest | Form | 18C

₹1,250/day. Goal `OFFSITE_CONVERSIONS`, destination `WEBSITE_AND_LEAD_FORM`.

```text
Location: India: Visakhapatnam (+25 mi) Andhra Pradesh; Chandigarh (+25 mi) Chandigarh; Delhi (+25 mi) Delhi; Ahmedabad (+25 mi), Surat (+25 mi) Gujarat; Gurugram (+25 mi) Haryana; Kochi (+25 mi) Kerala; Mumbai (+25 mi), Nagpur (+25 mi), Pune (+25 mi) Maharashtra; Bangalore (+25 mi) Karnataka; Bhubaneswar (+25 mi) Odisha; Jaipur (+25 mi) Rajasthan; Coimbatore (+25 mi) Tamil Nadu; Indore (+25 mi) Madhya Pradesh; Lucknow (+25 mi), Noida (+25 mi) Uttar Pradesh; Hyderabad (+25 mi) Telangana
Optimize locations: Off
Age: 25 - 45
People who match:
Interests: Small business, Shark Tank, Business school, Amazon.com, Drop shipping, Digital marketing, Self-employment, E-commerce, Shopify, Web development, Startup company, Flipkart, Entrepreneurship, Freelancer, Sole proprietorship, Engineering and polytechnic schools or Consulting
Behaviors: Small business owners
Job title: Proprietor or Founder
Advantage+ lookalike: Off
```

### SIB-04 | ACR | Directors + GST Co | Form | 19C and WhatsApp | 19C

Form: ₹2,500/day, goal `LEAD_GENERATION`, destination `ON_AD`. WhatsApp: ₹2,000/day, goal `CONVERSATIONS`, destination `WHATSAPP`. Audience settings are identical apart from the location types noted above.

```text
Custom audience: Company Director 2024-25, Company Director 2023-24, Company Director 2022-23, Company Director 2021-22, Company Director 2019-20, Company Director 2020-21, Company Director 2025-26 or GST - Company
Location: India: Delhi (+25 mi) Delhi; Ahmedabad (+25 mi), Surat (+25 mi), Vadodara (+25 mi) Gujarat; Faridabad (+25 mi), Gurugram (+25 mi) Haryana; Mumbai (+25 mi), Nagpur (+25 mi), Pune (+25 mi) Maharashtra; Bangalore (+25 mi) Karnataka; Ludhiana, Punjab (+25 mi) Punjab region; Jaipur (+25 mi) Rajasthan; Kolkata (+25 mi) West Bengal; Indore (+25 mi) Madhya Pradesh; Ghaziabad (+25 mi), Kanpur (+25 mi), Lucknow (+25 mi), Noida (+25 mi) Uttar Pradesh; Hyderabad (+25 mi) Telangana
Optimize locations: Off
Age: 25 - 55
Gender: Male
```

### SIB-05 India Entry: India Entry, Subsidiary and Branch-Liaison ad sets

₹4,000/day at campaign level. Goal `LEAD_GENERATION`, destination `ON_AD`. Audience settings are identical.

```text
Location: United Arab Emirates, Australia, Canada, Japan, South Korea, Singapore, United States
Age: 25 - 45
People who match:
Job title: Chief executive officer, Chairman, Partner, Owner, Vice President, Chief financial officer, Owner and Founder, Managing Partner, Founder or Managing Director
```

---

## Appendix B: live ad copy, verbatim

Headline is Meta's `title` field. Primary text is `body`. Text and emoji are unchanged.

### TM-F1 | Rs1999 + GST | Form | Lists and | Interest

Creative 1414111734270603, shared by both ads. CTA `GET_QUOTE`. Display link `setindiabiz.com/trademark-registration`.

**Headline:** Trademark Filing @ ₹1,999 + GST
**Description:** Free TM Search Included

```text
🏷️ Trademark filing in India — professional fee ₹1,999 + GST.
✅ Government fee ₹4,500 per class for individuals, startups and small enterprises (₹9,000 for others), at actuals
✅ Free trademark search before filing
✅ Filed within 24 hours of receiving complete documents
✅ Use ™ once filed; ® only after registration
✅ 14,000+ trademark applications filed
Reply to an examination report is quoted separately.
Amazon, Flipkart and Meesho are trademarks of their respective owners; Setindiabiz is not affiliated with or endorsed by them. Setindiabiz is a private professional services firm, not affiliated with IP India.
```

### INC-F1 | Rs2499 + GST | Form

Creative 2219613962304030. CTA `GET_QUOTE`. Display link `setindiabiz.com/company-registration`.

**Headline:** Pvt Ltd Registration @ ₹2,499 + GST
**Description:** Register Your Own Pvt Ltd Company

```text
Register your Private Limited company for a professional fee of ₹2,499 + GST. Covers DSC and DIN, MOA & AOA drafting, SPICe+ filing, PAN and TAN, up to the Certificate of Incorporation. Typically 5–7 working days after complete documents, subject to MCA processing. Government fees, stamp duty (state-wise) and DSC at actuals; post-incorporation services quoted separately. 25,000+ businesses served. 👉 Get a free 15-min call to confirm your company name and structure.
Setindiabiz is a private professional services firm, not affiliated with MCA.
```

### ACR-C1 | Deadline | Form | Dir

Creative 2650225295380459. CTA `GET_QUOTE`.

**Headline:** Avoid late fee: AOC-4 by 30 Oct, MGT-7 by 29 Nov
**Description:** Annual filing pack ₹7,499 + GST

```text
AGM held on 30 September 2026? AOC-4 is due by 30 October and MGT-7/MGT-7A by 29 November (Secs. 137(1) and 92(4), Companies Act, 2013). File late and MCA charges an additional fee of ₹100 a day for each form, with no upper limit.

Our annual filing pack for companies with turnover up to ₹5 lakh covers AGM documents, audit support, AOC-4, MGT-7/7A and the company's ITR-6 for ₹7,499 + GST. Government fees at actuals.

Tap Get quote and answer two short questions. Our team will call or WhatsApp you.
```

### ACR-C1 | Deadline | CTWA | Dir

Creative 1635700458207120. CTA `WHATSAPP_MESSAGE`.

**Headline:** Avoid late fee: AOC-4 by 30 Oct, MGT-7 by 29 Nov
**Description:** Annual filing pack ₹7,499 + GST

```text
AGM held on 30 September 2026? AOC-4 is due by 30 October and MGT-7/MGT-7A by 29 November (Secs. 137(1) and 92(4), Companies Act, 2013). File late and MCA charges an additional fee of ₹100 a day for each form, with no upper limit.

Our annual filing pack for companies with turnover up to ₹5 lakh covers AGM documents, audit support, AOC-4, MGT-7/7A and the company's ITR-6 for ₹7,499 + GST. Government fees at actuals.

Tap Chat on WhatsApp and tell us the entity type and the years pending.
```

### ACR-C2 | Cost of delay | Form | Dir

Creative 1790372369064790. CTA `GET_QUOTE`.

**Headline:** Avoid late fee of ₹100 a day per form
**Description:** File AOC-4 and MGT-7 on time

```text
Late ROC filing costs ₹100 a day for each form, with no upper limit. If AOC-4 and MGT-7 are both 90 days late, the additional fee alone is ₹18,000 (Sec. 403, Companies Act, 2013 read with the Companies (Registration Offices and Fees) Rules, 2014).

File FY 2025-26 on time. Pack for companies with turnover up to ₹5 lakh: AGM documents, audit support, AOC-4, MGT-7/7A and ITR-6 for ₹7,499 + GST. Government fees at actuals.

Tap Get quote and answer two short questions. Our team will call or WhatsApp you.
```

### ACR-C2 | Cost of delay | CTWA | Dir

Creative 1784392812714834. CTA `WHATSAPP_MESSAGE`.

**Headline:** Avoid late fee of ₹100 a day per form
**Description:** File AOC-4 and MGT-7 on time

```text
Late ROC filing costs ₹100 a day for each form, with no upper limit. If AOC-4 and MGT-7 are both 90 days late, the additional fee alone is ₹18,000 (Sec. 403, Companies Act, 2013 read with the Companies (Registration Offices and Fees) Rules, 2014).

File FY 2025-26 on time. Pack for companies with turnover up to ₹5 lakh: AGM documents, audit support, AOC-4, MGT-7/7A and ITR-6 for ₹7,499 + GST. Government fees at actuals.

Chat with us on WhatsApp to check your company's due dates.
```

### ACR-C5 | Dates and price | Form | Dir and CTWA | Dir

Creatives 2613055129170585 (Form, CTA `GET_QUOTE`) and 1081755811138834 (CTWA, CTA `WHATSAPP_MESSAGE`). Copy is identical.

**Headline:** Annual filing pack ₹7,499 + GST
**Description:** AGM on 30 Sep? AOC-4 due 30 Oct

```text
Directors of private limited companies: if your AGM was on 30 September 2026, AOC-4 is due by 30 October and MGT-7/7A by 29 November. After that, ₹100 a day per form.

Setindiabiz has served 25,000+ businesses. Annual filing pack for companies with turnover up to ₹5 lakh: AGM documents, audit support, AOC-4, MGT-7/7A and ITR-6 for ₹7,499 + GST. Government fees at actuals.

Setindiabiz is a private firm, not affiliated with MCA.
```

### SIB-05 | E1 | India entry | Form

Creative 1724357761994854. CTA `GET_QUOTE`.

**Headline:** Set up your business in India
**Description:** Subsidiary, branch or liaison office

```text
Planning to set up in India? We help foreign companies choose between an Indian subsidiary, a branch office and a liaison office, then handle the filings with the Registrar of Companies and the reporting under India's foreign exchange rules (FEMA). Setindiabiz has served 25,000+ businesses from offices in Delhi, Noida, Mumbai, Bengaluru and Hyderabad. Answer three short questions and our India-entry team will contact you.
```

### SIB-05 | E2 | Structures | Form

Creative 1663411985572031. CTA `GET_QUOTE`.

**Headline:** Which India structure fits you?
**Description:** Compare the three routes

```text
Subsidiary, branch office or liaison office? A subsidiary is an Indian company. A branch office generally needs a profit-making record over the last five financial years and net worth of at least USD 100,000. A liaison office generally needs a three-year profit-making record and net worth of at least USD 50,000; it cannot carry on business in India and is funded from abroad. Tell us your plans and we will suggest the route that fits.
```

### SIB-05 | S1 | From USD 499 | Form

Creative 3934649513358828. CTA `GET_QUOTE`.

**Headline:** Indian subsidiary from USD 499
**Description:** Government fees extra, at cost

```text
Set up your Indian subsidiary from USD 499. The fee covers consultation and our services up to the Certificate of Incorporation. Government fees, stamp duty and digital signature costs are extra, billed at actual cost. Registered office and a resident director are arranged separately. We check your sector's foreign investment route and conditions first.
```

### SIB-05 | S2 | After incorporation | Form

Creative 1704743077655068. CTA `GET_QUOTE`.

**Headline:** Your India compliance, one contact
**Description:** Incorporation, FEMA and annual filings

```text
Incorporation is the first step. A foreign-owned Indian company reports each issue of shares to its foreign investor on Form FC-GPR within 30 days of the issue, then files its accounts and annual return with the Registrar of Companies every year. Setindiabiz handles incorporation and the compliance that follows, with one point of contact.
```

### SIB-05 | B1 | Liaison office | Form

Creative 2144337016154094. CTA `GET_QUOTE`.

**Headline:** Open a liaison office in India
**Description:** 3 years' profits, USD 50,000 net worth

```text
Want a presence in India before you trade? A liaison office can represent your company and promote trade and technical or financial collaboration with Indian businesses. It cannot carry on business in India and is funded from abroad. Eligibility: generally a profit-making record over the last three financial years and net worth of at least USD 50,000. We prepare the application, which is filed through an authorised bank in India.
```

### SIB-05 | B2 | Branch office | Form

Creative 2146456619410623. CTA `GET_QUOTE`.

**Headline:** Open a branch office in India
**Description:** 5 years' profits, USD 100,000 net worth

```text
A branch office lets your company carry out the activities the RBI permits for branches in India. Eligibility: generally a profit-making record over the last five financial years and net worth of at least USD 100,000. Applicants in some sectors and from some countries need prior RBI approval. We check eligibility and prepare the application.
```
