# SetIndiaBiz — Meta Ads Deep Analysis (read-only) — 6 Oct 2026

**Scope:** Meta account 152154124583473 (INR), 1 Apr – 5 Oct 2026 (last delivery 24 Sep). Zoho CRM paid-Meta leads (`Lead_Source in ('Advt - Facebook','Advt - Instagram')`) created in the same window: **4,260 leads** (4,097 unconverted, pulled with COQL, plus 163 converted, pulled with getRecords because COQL leaves out converted leads). These are joined to **5,837 Deals** created 25 Mar – 5 Oct through `Converted_Deal`.
**Nothing was changed in Meta or Zoho.** All figures are actuals unless marked *estimate*.

## 0. Definitions and caveats (read first)
- **CRM classes** (one per lead): `converted` (has a deal) · `progressed` (Negotiation/Proposal Sent/Payment Pending) · `open_valid` (Valid Lead/Postponed) · `stuck` (Establishing Contact) · `lost_nocontact` (Why_Lost = Avoiding Call, or quality = Invalid-Never Connect) · `lost_junk` (Inquired by Mistake, Job Seeker, Wrong Info, Bot, Duplicate) · `lost_qual` (No Product Offering, Not Eligible, Language, Territory…) · `lost_price_comp` (Other CA, Pricing, Competitor, Self Completed) · `lost_attrition` (Not Interested, Plan Drop, RM Delay).
- **No-contact** = stuck + lost_nocontact. Telephony is not logged in Zoho and `First_Contact_Time` is filled on **0 of 4,260** leads, so this is a proxy based on how RMs set the disposition.
- **Strict valid** = converted + progressed + open_valid + lost_price_comp (a real need was confirmed on contact). **Quality-field valid** = any quality field `Valid*` except "Product Not Ready". ⚠️ This field is unreliable: **`RM_Lead_Quality = 'Valid - RM Working'` sits on 704 leads that were lost as "Avoiding Call"**, so I report strict valid as the main measure.
- **Won** = first deal from the lead in a W-* or Won stage. **Revenue** = that deal's Amount. Repeat or upsell deals (Post-INC, TM objection replies, ACR renewals) are **not** included, so lifetime value is understated, most of all for Incorporation and Trademark.
- **Attribution:** 190 leads have no Meta campaign stamp. 66 of them won ₹3.62L, mostly converted leads from May. For campaign economics I assign these 66+ leads to a campaign from the deal product and creation date (for example, LLP Form 11 deals created 16–30 May → #IND2 LLP ACR). These are labelled **(incl. inferred)**.
- **Maturity:** 44% of September leads are still open (stuck/valid/progressed), and 34% are "Still Evaluating". The median time from lead to conversion is 5.1 days (p90 32 days). Sep figures will improve; Aug is largely settled.
- `Select_State` is blank on 72% of leads and is filled mostly after contact (biased), so geography uses the form `City` field (67% filled).
- Meta auction-ranking and industry-benchmark tools returned **no data** for this account.

## 1. Current state (as of 6 Oct)
- **Why nothing is delivering:** the ad-set delivery sub-status is `account_spend_limit_reached`, meaning the prepaid balance is used up. The last top-up was **₹25,000 by UPI on 21 Sep**, the last billing was on 25 Sep and the last spend was on 24 Sep.
- **Funding has been the binding constraint all along.** The account delivered on only **104 of 150 calendar days** (28 Apr–24 Sep). On **34 days the spend was exactly the top-up ÷ 1.18** (₹8,474.58 = ₹10k, ₹12,711.86 = ₹15k, ₹16,949.15 = ₹20k), so 18% GST is taken out of each UPI top-up. **A ₹10,000/day gross top-up buys about ₹8,475 of media.** Average spend per live day was ₹12,453. Because of the dark days, learning kept restarting.
- **Live (status ACTIVE but unfunded):**
  - #IND1 Incorporation. Ad set *Daytime INSA* has a lifetime budget of ₹2.5L with ₹56.7k left, ends 30 Oct, runs Mon–Sat 07:00–20:00. Ad set *24Hr INSA* runs at ₹2,500/day with no end date.
  - #IND3 Trademark. Both ad sets have lifetime budgets (SA ₹1.5L with ₹24.2k left; Director ₹60k with ₹11.8k left), run Mon–Sat 07:00–19:00, and **the campaign stops 15 Oct**.
  - **If money is added, these resume immediately on their old settings.**
- **Paused:** #IND4 CCFS (ended 8 Sep), #IND5 DPIIT and #IND6 CFO (ended 31 Jul), #IND2 LLP ACR (16–30 May), #IND2 Website (sales objective).
- **Setup on all lead ad sets:** objective OUTCOME_LEADS, optimisation OFFSITE_CONVERSIONS on the pixel LEAD event, destination WEBSITE_AND_LEAD_FORM, attribution 7-day click / 1-day view.
  - Advantage+ audience is **ON** for IND1 INSA and both TM ad sets, so their interests, age and gender are only suggestions.
  - TM, CCFS, DPIIT and CFO specify **male only**. IND1 targets all genders. Women are 5–9% of spend.
  - Geography is 18–30 named cities with a 25-mile radius.
  - Placements are Advantage+ on IND1/IND3, but all spend went to FB/IG feed, reels and stories. Audience Network got ₹0.
- **One Click-to-WhatsApp (CTWA) test already ran:** *C2 LLP ACR – WA*, 23–30 May, ₹26,389 spent, **77 messaging conversations at ₹343 each**, against the sister Instant Form ad set (same audience, same week) at ₹400 per lead. **None of those conversations can be found in CRM** (`CTWA_Click_ID` is filled on 0 leads; only 3 "Social - WhatsApp" leads were created in May), so there is no quality read-out.

## 2. Campaign economics (Apr–Sep)
Meta: spend ₹12.67L (₹12.17L on lead campaigns plus ₹50k on the website campaign) and 4,520 Meta leads. CRM: 4,260 paid-Meta leads.

| Segment | Spend | Meta leads | CRM leads | Cost/CRM lead | No-contact total | Stuck EC | Lost-Avoiding Call | Lost-junk reason | Lost-qual/lang | Strict valid | Quality-field valid | Progressed+conv | Won | Won rev | Cost/strict valid | Cost/progressed | Cost/won | Rev/spend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IND1-Incorp | ₹509,890 | 2199 | 2004 | ₹254 | 43.6% | 4.4% | 39.2% | 7.5% | 3.2% | 31.1% | 54.9% | 13.4% | 13 | ₹45,978 | ₹817 | ₹1,903 | ₹39,222 | 0.09x |
| IND3-TM | ₹174,008 | 1028 | 988 | ₹176 | 44.5% | 7.6% | 36.9% | 3.5% | 2.4% | 29.9% | 58.6% | 8.0% | 25 | ₹55,508 | ₹590 | ₹2,203 | ₹6,960 | 0.32x |
| IND4-CCFS | ₹296,730 | 746 | 687 | ₹432 | 46.9% | 4.8% | 42.1% | 4.4% | 3.8% | 31.3% | 54.0% | 6.7% | 29 | ₹567,991 | ₹1,380 | ₹6,451 | ₹10,232 | 1.91x |
| IND2-LLP-ACR | ₹163,132 | 315 | 219 | ₹745 | 36.1% | 0.0% | 36.1% | 4.6% | 3.2% | 44.7% | 76.3% | 8.7% | 2 | ₹14,912 | ₹1,665 | ₹8,586 | ₹81,566 | 0.09x |
| IND5-DPIIT | ₹48,815 | 147 | 132 | ₹370 | 47.7% | 5.3% | 42.4% | 7.6% | 3.8% | 24.2% | 35.6% | 6.1% | 1 | ₹4,999 | ₹1,525 | ₹6,102 | ₹48,815 | 0.10x |
| IND6-CFO | ₹24,731 | 41 | 40 | ₹618 | 52.5% | 10.0% | 42.5% | 17.5% | 2.5% | 7.5% | 25.0% | 0.0% | 0 | - | ₹8,244 | - | - | 0.00x |
| UNSTAMPED | - | - | 190 | - | 25.8% | 0.0% | 25.8% | 8.9% | 3.2% | 54.2% | 64.2% | 44.7% | 66 | ₹361,832 | - | - | - | - |
| ALL paid Meta | ₹1,217,307 | 4476 | 4260 | ₹286 | 43.4% | 4.9% | 38.5% | 6.1% | 3.1% | 32.2% | 56.2% | 11.9% | 136 | ₹1,051,220 | ₹889 | ₹2,411 | ₹8,951 | 0.86x |

**Including inferred attribution of unstamped converted leads:**

| Campaign | Spend | CRM leads | Won | First-deal revenue | Cost/won | Avg ticket | Rev/spend |
|---|---|---|---|---|---|---|---|
| IND1 Incorporation | ₹5,09,890 | 2,114 | 37 | ₹1,69,610 | ₹13,781 | ₹4,584 | **0.33x** |
| IND3 Trademark | ₹1,74,008 | 998 | 26 | ₹59,084 | ₹6,693 | ₹2,272 | **0.34x** |
| IND4 CCFS (ACR + closure) | ₹2,96,730 | 697 | 30 | ₹5,77,491 | ₹9,891 | ₹19,250 | **1.95x** |
| IND2 LLP ACR (16–30 May) | ₹1,63,132 | 267 | 42 | ₹2,40,036 | ₹3,884 | ₹5,715 | **1.47x** |
| IND5 DPIIT | ₹48,815 | 132 | 1 | ₹4,999 | ₹48,815 | ₹4,999 | 0.10x |
| IND6 Virtual CFO + GST | ₹24,731 | 40 | 0 | – | – | – | 0.00x |
| **Total** | ₹12,17,307 | 4,260 | 136 | ₹10,51,220 | ₹8,951 | ₹7,730 | **0.86x** |

- **What the wins were.**
  - IND1: Incorporation (19), LLP Registration (4), GST Registration (4), TMF (3).
  - IND3: TMF (22).
  - IND4: ACR-CCFS (11, ₹3.83L), Striking Off (8, ₹1.10L), ACR (4).
  - IND2: LLP Annual Return (33) and Form 11 (4).
- **Cross-check:** 159 deals carry a Meta lead source. 148 of them link to a lead above. The other 11 are unlinked (₹1.06L won) and are excluded from these figures.

### Lost reasons by campaign
- **IND1-Incorp** (Lost n=1464): Avoiding Call 54%, Not Interested 13%, Other CA 9%, Plan Drop 6%, Wrong Info 4%, Inquired by Mistake 4%, Job Seeker 2%, Pricing 2%
- **IND3-TM** (Lost n=742): Avoiding Call 49%, Not Interested 16%, Other CA 12%, Plan Drop 10%, Pricing 3%, Wrong Info 2%, Language Issue 2%, Inquired by Mistake 2%
- **UNSTAMPED** (Lost n=99): Avoiding Call 49%, Inquired by Mistake 9%, Not Interested 9%, Other CA 8%, Pricing 4%, Plan Drop 4%, None 3%, Wrong Info 3%
- **IND2-LLP-ACR** (Lost n=194): Avoiding Call 41%, Other CA 27%, Not Interested 12%, Pricing 10%, Language Issue 2%, Wrong Info 2%, Job Seeker 2%, Duplicate Record 1%
- **IND5-DPIIT** (Lost n=111): Avoiding Call 50%, Not Interested 12%, Other CA 11%, Plan Drop 8%, Inquired by Mistake 5%, Wrong Info 4%, Pricing 4%, Not Eligible 3%
- **IND4-CCFS** (Lost n=580): Avoiding Call 50%, Other CA 18%, Not Interested 10%, Plan Drop 6%, Pricing 5%, Inquired by Mistake 2%, Wrong Info 2%, No Product Offering 2%
- **IND6-CFO** (Lost n=35): Avoiding Call 49%, Not Interested 20%, Job Seeker 14%, Self Completed 6%, Non Servinge Territory 3%, Wrong Info 3%, Plan Drop 3%, Inquired by Mistake 3%

### Month × campaign
| Segment | Spend | Meta leads | CRM leads | Cost/CRM lead | No-contact total | Stuck EC | Lost-Avoiding Call | Lost-junk reason | Lost-qual/lang | Strict valid | Quality-field valid | Progressed+conv | Won | Won rev | Cost/strict valid | Cost/progressed | Cost/won | Rev/spend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-04 | ₹18,158 | 128 | 153 | ₹119 | 40.5% | 0.7% | 39.9% | 9.8% | 0.7% | 33.3% | 51.6% | 20.9% | 4 | ₹20,084 | ₹356 | ₹567 | ₹4,540 | 1.11x |
| 2026-05 | ₹322,740 | 1091 | 1040 | ₹310 | 39.6% | 0.7% | 38.9% | 6.1% | 3.1% | 39.0% | 67.2% | 19.9% | 61 | ₹329,493 | ₹795 | ₹1,559 | ₹5,291 | 1.02x |
| 2026-06 | ₹283,898 | 851 | 842 | ₹337 | 47.7% | 3.7% | 44.1% | 7.0% | 2.5% | 28.1% | 51.4% | 11.4% | 17 | ₹99,102 | ₹1,198 | ₹2,957 | ₹16,700 | 0.35x |
| 2026-07 | ₹285,654 | 1149 | 1051 | ₹272 | 44.6% | 3.7% | 40.9% | 6.7% | 3.3% | 24.8% | 52.0% | 4.9% | 29 | ₹256,915 | ₹1,094 | ₹5,601 | ₹9,850 | 0.90x |
| 2026-08 | ₹197,555 | 690 | 646 | ₹306 | 47.4% | 9.0% | 38.4% | 5.3% | 4.3% | 27.2% | 54.5% | 6.7% | 15 | ₹292,156 | ₹1,122 | ₹4,594 | ₹13,170 | 1.48x |
| 2026-09 | ₹109,301 | 567 | 528 | ₹207 | 37.3% | 13.6% | 23.7% | 3.6% | 3.2% | 45.3% | 54.4% | 14.4% | 10 | ₹53,470 | ₹457 | ₹1,438 | ₹10,930 | 0.49x |

| Segment | Spend | Meta leads | CRM leads | Cost/CRM lead | No-contact total | Stuck EC | Lost-Avoiding Call | Lost-junk reason | Lost-qual/lang | Strict valid | Quality-field valid | Progressed+conv | Won | Won rev | Cost/strict valid | Cost/progressed | Cost/won | Rev/spend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IND1-Incorp 2026-04 | ₹18,158 | 128 | 113 | ₹161 | 43.4% | 0.0% | 43.4% | 4.4% | 0.9% | 35.4% | 49.6% | 20.4% | 0 | - | ₹454 | ₹789 | - | 0.00x |
| IND1-Incorp 2026-05 | ₹159,607 | 776 | 700 | ₹228 | 43.1% | 1.0% | 42.1% | 7.0% | 3.0% | 33.3% | 64.3% | 17.9% | 3 | ₹3,499 | ₹685 | ₹1,277 | ₹53,202 | 0.02x |
| IND1-Incorp 2026-06 | ₹166,157 | 487 | 459 | ₹362 | 51.0% | 5.0% | 46.0% | 9.8% | 2.8% | 22.7% | 46.8% | 10.5% | 5 | ₹15,132 | ₹1,598 | ₹3,462 | ₹33,231 | 0.09x |
| IND1-Incorp 2026-07 | ₹75,874 | 293 | 262 | ₹290 | 44.3% | 2.3% | 42.0% | 10.3% | 3.4% | 21.4% | 51.5% | 3.8% | 2 | ₹10,847 | ₹1,355 | ₹7,587 | ₹37,937 | 0.14x |
| IND1-Incorp 2026-08 | ₹34,789 | 217 | 193 | ₹180 | 40.9% | 8.3% | 32.6% | 8.8% | 5.2% | 27.5% | 50.3% | 7.3% | 2 | ₹4,500 | ₹656 | ₹2,485 | ₹17,394 | 0.13x |
| IND1-Incorp 2026-09 | ₹55,304 | 298 | 277 | ₹200 | 33.9% | 13.4% | 20.6% | 2.9% | 4.0% | 49.8% | 53.1% | 17.3% | 1 | ₹12,000 | ₹401 | ₹1,152 | ₹55,304 | 0.22x |
| IND3-TM 2026-04 | - | - | 2 | - | 100.0% | 0.0% | 100.0% | 0.0% | 0.0% | 0.0% | 100.0% | 0.0% | 0 | - | - | - | - | - |
| IND3-TM 2026-05 | - | - | 10 | - | 70.0% | 0.0% | 70.0% | 0.0% | 0.0% | 10.0% | 60.0% | 0.0% | 0 | - | - | - | - | - |
| IND3-TM 2026-06 | ₹58,827 | 210 | 208 | ₹283 | 44.7% | 1.0% | 43.8% | 2.9% | 1.9% | 30.8% | 64.4% | 10.1% | 3 | ₹6,000 | ₹919 | ₹2,801 | ₹19,609 | 0.10x |
| IND3-TM 2026-07 | ₹70,558 | 472 | 438 | ₹161 | 45.2% | 4.6% | 40.6% | 5.0% | 2.7% | 22.8% | 54.1% | 3.9% | 11 | ₹27,500 | ₹706 | ₹4,150 | ₹6,414 | 0.39x |
| IND3-TM 2026-08 | ₹22,701 | 165 | 158 | ₹144 | 44.9% | 17.1% | 27.8% | 1.9% | 3.8% | 33.5% | 63.3% | 11.4% | 6 | ₹13,508 | ₹428 | ₹1,261 | ₹3,784 | 0.60x |
| IND3-TM 2026-09 | ₹21,921 | 181 | 172 | ₹127 | 40.1% | 15.1% | 25.0% | 2.3% | 1.2% | 44.8% | 58.1% | 13.4% | 5 | ₹8,500 | ₹285 | ₹953 | ₹4,384 | 0.39x |
| IND4-CCFS 2026-05 | - | - | 1 | - | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 100.0% | 0.0% | 0.0% | 0 | - | - | - | - | - |
| IND4-CCFS 2026-06 | ₹31,384 | 94 | 92 | ₹341 | 41.3% | 1.1% | 40.2% | 3.3% | 1.1% | 44.6% | 54.3% | 13.0% | 5 | ₹64,000 | ₹765 | ₹2,615 | ₹6,277 | 2.04x |
| IND4-CCFS 2026-07 | ₹93,206 | 256 | 226 | ₹412 | 43.4% | 3.5% | 39.8% | 3.1% | 4.0% | 35.4% | 58.0% | 8.4% | 14 | ₹204,069 | ₹1,165 | ₹4,906 | ₹6,658 | 2.19x |
| IND4-CCFS 2026-08 | ₹140,065 | 308 | 291 | ₹481 | 52.2% | 5.2% | 47.1% | 4.8% | 4.1% | 24.1% | 51.9% | 3.8% | 7 | ₹274,148 | ₹2,001 | ₹12,733 | ₹20,009 | 1.96x |
| IND4-CCFS 2026-09 | ₹32,075 | 88 | 77 | ₹417 | 44.2% | 11.7% | 32.5% | 7.8% | 5.2% | 29.9% | 50.6% | 5.2% | 3 | ₹25,774 | ₹1,395 | ₹8,019 | ₹10,692 | 0.80x |


## 3. Ad set and creative
| Segment | Spend | Meta leads | CRM leads | Cost/CRM lead | No-contact total | Stuck EC | Lost-Avoiding Call | Lost-junk reason | Lost-qual/lang | Strict valid | Quality-field valid | Progressed+conv | Won | Won rev | Cost/strict valid | Cost/progressed | Cost/won | Rev/spend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IND1-Incorp / C1 - Daytime INSA Company INC | ₹193,342 | 895 | 822 | ₹235 | 42.5% | 4.7% | 37.7% | 6.8% | 3.0% | 30.4% | 53.4% | 10.8% | 7 | ₹29,580 | ₹773 | ₹2,172 | ₹27,620 | 0.15x |
| IND1-Incorp / C1 - 24Hr INSA Company INC | ₹151,019 | 810 | 749 | ₹202 | 42.7% | 4.5% | 38.2% | 7.2% | 3.6% | 34.6% | 57.5% | 15.1% | 4 | ₹14,398 | ₹583 | ₹1,336 | ₹37,755 | 0.10x |
| IND1-Incorp / C1 - 24Hr LAL1% Director - Company INC | ₹55,890 | 294 | 258 | ₹217 | 45.3% | 2.7% | 42.6% | 7.8% | 1.9% | 30.2% | 55.0% | 18.6% | 1 | ₹1,000 | ₹717 | ₹1,164 | ₹55,890 | 0.02x |
| IND1-Incorp / C1 - Daytime - LAL1% Director - Company INC | ₹109,638 | 200 | 175 | ₹627 | 50.3% | 5.1% | 45.1% | 12.0% | 4.6% | 21.1% | 50.3% | 10.3% | 1 | ₹1,000 | ₹2,963 | ₹6,091 | ₹109,638 | 0.01x |
| IND2-LLP-ACR / C2 - Daytime - Cust Aud LLP - LLP ACR | ₹99,545 | 220 | 151 | ₹659 | 35.8% | 0.0% | 35.8% | 5.3% | 4.0% | 45.7% | 80.8% | 9.3% | 2 | ₹14,912 | ₹1,443 | ₹7,110 | ₹49,772 | 0.15x |
| IND2-LLP-ACR / C2 - Daytime - Cust Aud LLP - LLP ACR - DW | ₹37,198 | 93 | 68 | ₹547 | 36.8% | 0.0% | 36.8% | 2.9% | 1.5% | 42.6% | 66.2% | 7.4% | 0 | - | ₹1,283 | ₹7,440 | - | 0.00x |
| IND3-TM / C3 Adset - TMF - SA - Web + Form | ₹125,839 | 756 | 726 | ₹173 | 44.8% | 6.1% | 38.7% | 3.7% | 2.2% | 30.3% | 59.4% | 8.5% | 21 | ₹43,000 | ₹572 | ₹2,030 | ₹5,992 | 0.34x |
| IND3-TM / C3 Adset - Director - TMF - Web + Form | ₹48,169 | 272 | 262 | ₹184 | 43.9% | 11.8% | 32.1% | 3.1% | 3.1% | 28.6% | 56.5% | 6.5% | 4 | ₹12,508 | ₹642 | ₹2,833 | ₹12,042 | 0.26x |
| IND4-CCFS / C4 Adset - Director CCFS + Form | ₹296,730 | 746 | 687 | ₹432 | 46.9% | 4.8% | 42.1% | 4.4% | 3.8% | 31.3% | 54.0% | 6.7% | 29 | ₹567,991 | ₹1,380 | ₹6,451 | ₹10,232 | 1.91x |
| IND5-DPIIT / C4 Adset - Director DPIIT + Form | ₹48,815 | 147 | 132 | ₹370 | 47.7% | 5.3% | 42.4% | 7.6% | 3.8% | 24.2% | 35.6% | 6.1% | 1 | ₹4,999 | ₹1,525 | ₹6,102 | ₹48,815 | 0.10x |
| IND6-CFO / C6 Adset - Director and GSTN CFO + Form | ₹24,731 | 41 | 34 | ₹727 | 50.0% | 8.8% | 41.2% | 20.6% | 0.0% | 5.9% | 26.5% | 0.0% | 0 | - | ₹12,366 | - | - | 0.00x |
| UNSTAMPED / None | - | - | 190 | - | 25.8% | 0.0% | 25.8% | 8.9% | 3.2% | 54.2% | 64.2% | 44.7% | 66 | ₹361,832 | - | - | - | - |

- **IND1 ad sets.**
  - *Daytime LAL1% Director* was the worst: CPL ₹548, 12% junk, 21% strict valid, 1 win from ₹1.10L.
  - *24Hr INSA* beat *Daytime INSA*: CPL ₹186 vs ₹216, strict valid 34.6% vs 30.4%, progressed 15.1% vs 10.8%.
  - Day-parting did not improve quality.
- **IND3 ad sets.** The two are equivalent. SA/interests: CPL ₹166, 21 wins. Director custom audience: CPL ₹177, 4 wins.

**Ads.** CRM ad-level data exists only for the 2,353 leads that carry `Meta_Ad_ID`, which is complete only for ads launched after mid-July, so cost columns for older ads are understated.
| Segment | Spend | Meta leads | CRM leads | Cost/CRM lead | No-contact total | Stuck EC | Lost-Avoiding Call | Lost-junk reason | Lost-qual/lang | Strict valid | Quality-field valid | Progressed+conv | Won | Won rev | Cost/strict valid | Cost/progressed | Cost/won | Rev/spend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IND3 / C3 Adset - TMF - SA - Web +  / #C3A TM Ad 2 [980449] | ₹102,715 | 682 | 536 | ₹192 | 44.4% | 7.8% | 36.6% | 3.7% | 2.4% | 31.0% | 57.8% | 7.6% | 17 | ₹35,000 | ₹619 | ₹2,505 | ₹6,042 | 0.34x |
| IND4 / C4 Adset - Director CCFS + F / #C4 CCFS - 2 [410449] | ₹229,660 | 620 | 528 | ₹435 | 48.5% | 5.5% | 43.0% | 4.4% | 3.8% | 29.2% | 54.5% | 5.7% | 22 | ₹461,176 | ₹1,491 | ₹7,655 | ₹10,439 | 2.01x |
| IND1 / C1 - 24Hr INSA Company INC / Ad-2 Lead - Company Registration [760449] | ₹44,977 | 262 | 252 | ₹178 | 37.7% | 11.1% | 26.6% | 3.2% | 4.4% | 46.4% | 52.0% | 16.3% | 2 | ₹4,500 | ₹384 | ₹1,097 | ₹22,488 | 0.10x |
| IND1 / C1 - Daytime INSA Company IN / Ad-1 Lead - Company Registration [000449] | ₹157,422 | 721 | 224 | ₹703 | 46.0% | 1.8% | 44.2% | 7.6% | 3.6% | 20.5% | 51.3% | 3.6% | 2 | ₹10,646 | ₹3,422 | ₹19,678 | ₹78,711 | 0.07x |
| IND1 / C1 - Daytime INSA Company IN / Ad-1 Lead - Company Registration - Copy [720449] | ₹35,921 | 174 | 165 | ₹218 | 35.8% | 12.7% | 23.0% | 4.8% | 3.0% | 40.6% | 51.5% | 12.1% | 2 | ₹12,499 | ₹536 | ₹1,796 | ₹17,960 | 0.35x |
| IND3 / C3 Adset - Director - TMF -  / #C3B TM Ad 2 [430449] | ₹21,352 | 161 | 145 | ₹147 | 44.1% | 15.2% | 29.0% | 3.4% | 4.8% | 32.4% | 58.6% | 9.0% | 3 | ₹10,008 | ₹454 | ₹1,642 | ₹7,117 | 0.47x |
| IND1 / C1 - 24Hr INSA Company INC / Ad-1 Lead - Company Registration [650449] | ₹106,042 | 548 | 129 | ₹822 | 38.0% | 3.1% | 34.9% | 15.5% | 5.4% | 25.6% | 55.8% | 5.4% | 1 | ₹5,799 | ₹3,213 | ₹15,149 | ₹106,042 | 0.05x |
| IND5 / C4 Adset - Director DPIIT +  / #C5 DPIIT 1 [940449] | ₹37,465 | 120 | 85 | ₹441 | 50.6% | 4.7% | 45.9% | 7.1% | 4.7% | 21.2% | 35.3% | 4.7% | 1 | ₹4,999 | ₹2,081 | ₹9,366 | ₹37,465 | 0.13x |
| IND4 / C4 Adset - Director CCFS + F / #C4 CCFS - 1 [670449] | ₹42,259 | 90 | 63 | ₹671 | 41.3% | 3.2% | 38.1% | 6.3% | 6.3% | 30.2% | 54.0% | 7.9% | 4 | ₹56,815 | ₹2,224 | ₹8,452 | ₹10,565 | 1.34x |
| IND3 / C3 Adset - Director - TMF -  / #C3B TM Ad 7 [370449] | ₹9,550 | 57 | 45 | ₹212 | 48.9% | 8.9% | 40.0% | 0.0% | 2.2% | 15.6% | 51.1% | 4.4% | 0 | - | ₹1,364 | ₹4,775 | - | 0.00x |
| IND3 / C3 Adset - Director - TMF -  / #C3B TM Ad 6 [420449] | ₹10,181 | 38 | 34 | ₹299 | 41.2% | 2.9% | 38.2% | 0.0% | 0.0% | 23.5% | 52.9% | 0.0% | 0 | - | ₹1,273 | - | - | 0.00x |
| IND4 / C4 Adset - Director CCFS + F / #C4 CCFS - 4 [300449] | ₹20,013 | 30 | 29 | ₹690 | 55.2% | 3.4% | 51.7% | 3.4% | 3.4% | 24.1% | 51.7% | 3.4% | 0 | - | ₹2,859 | ₹20,013 | - | 0.00x |
| IND1 / C1 - Daytime - LAL1% Directo / Ad-1 Lead - Company Registration [000449] | ₹109,638 | 200 | 21 | ₹5,221 | 57.1% | 19.0% | 38.1% | 23.8% | 0.0% | 9.5% | 23.8% | 4.8% | 0 | - | ₹54,819 | ₹109,638 | - | 0.00x |
| IND6 / C6 Adset - Director and GSTN / #C6 CFO 3 [210449] | ₹12,194 | 16 | 15 | ₹813 | 66.7% | 13.3% | 53.3% | 13.3% | 0.0% | 0.0% | 33.3% | 0.0% | 0 | - | - | - | - | 0.00x |
| IND5 / C4 Adset - Director DPIIT +  / #C5 DPIIT 2 [950449] | ₹6,636 | 17 | 15 | ₹442 | 46.7% | 6.7% | 40.0% | 6.7% | 0.0% | 13.3% | 33.3% | 0.0% | 0 | - | ₹3,318 | - | - | 0.00x |
| IND6 / C6 Adset - Director and GSTN / #C6 CFO 1 [250449] | ₹6,373 | 17 | 11 | ₹579 | 27.3% | 0.0% | 27.3% | 36.4% | 0.0% | 9.1% | 36.4% | 0.0% | 0 | - | ₹6,373 | - | - | 0.00x |
| IND3 / C3 Adset - TMF - SA - Web +  / #C3A TM Ad 7 [930449] | ₹4,881 | 33 | 11 | ₹444 | 36.4% | 9.1% | 27.3% | 18.2% | 9.1% | 18.2% | 9.1% | 9.1% | 1 | ₹2,000 | ₹2,441 | ₹4,881 | ₹4,881 | 0.41x |
| IND1 / C1 - 24Hr LAL1% Director - C / Ad-1 Lead - Company Registration [780449] | ₹55,890 | 294 | 10 | ₹5,589 | 80.0% | 40.0% | 40.0% | 10.0% | 0.0% | 0.0% | 20.0% | 0.0% | 0 | - | - | - | - | 0.00x |
| IND3 / C3 Adset - Director - TMF -  / #C3B TM Ad 4 [400449] | ₹2,346 | 10 | 10 | ₹235 | 60.0% | 30.0% | 30.0% | 0.0% | 0.0% | 20.0% | 40.0% | 10.0% | 1 | ₹2,500 | ₹1,173 | ₹2,346 | ₹2,346 | 1.07x |

**Creatives (copy pulled from Meta):**
- **TM winner, *TM Ad 2*, the same creative in both ad sets:** "Trademark Filing @ ₹1,999 Only", professional fee ₹1,999 + **government fee ₹4,500 shown upfront**, free search, CTA *Get Quote*.
  - Meta CPL ₹151 (SA) and ₹133 (Director).
  - 843 Meta leads = **82% of TM leads**, 20 wins.
- **TM losers (paused):**
  - "Free TM Search India" (Ad 1): CPL ₹953–1,054.
  - "Protect Your Trademark / What can you trademark?" (Ad 6): CPL ₹268–360.
  - "Is your trademark getting copied?" (Ad 7 Director): CPL ₹168 but 15.6% strict valid.
  - **Ads with a clear price beat generic and fear angles by 2–7x on CPL.**
- **IND1:**
  - The old ads (Apr–Jul) were catalog/dynamic (`{{product.name}}`) creatives: CPL ₹190–218.
  - **The new Aug creative "Pvt Ltd in 7 Days – ₹2,499"** (professional fee, govt + DSC at actuals, free 15-minute consult) ran as Ad-2 (24Hr) and Ad-1 Copy (Daytime). CPL ₹172 / ₹206, strict valid 46% / 41%, Avoiding Call 27% / 23%, the best IND1 cohort. The cohort is still maturing (11–13% stuck).
  - ⚠️ **Compliance:** "in 7 days" and "25,000+ companies / 18+ years" must be provable (Companies Act/CPA s.2(28)). An MCA processing delay makes "7 days" a timeline claim you cannot guarantee.
- **IND4 CCFS:** "90% Late Fee Waiver" with a scheme deadline drove ROAS of 2.0x (CCFS-2: ₹2.30L spend, 22 wins, ₹4.61L). **That scheme has ended, so the hook can't be reused.**
- **IND2 LLP ACR:** "File LLP Form 11 before 30 May, plans from ₹1,999" also used a deadline hook.
- **DPIIT** ("Apply for DPIIT Recognition", CTA *Learn More*) and **CFO** were weak.

## 4. Breakdowns
### Meta: age (CPL = spend ÷ Meta leads, Apr–Sep)
| Age | IND1 spend% | IND1 CPL | IND3 spend% | IND3 CPL | IND4 spend% | IND4 CPL | All CPL |
|---|---|---|---|---|---|---|---|
| 18-24 | 0% | - | 5% | ₹154 | 4% | ₹260 | ₹246 |
| 25-34 | 42% | ₹244 | 37% | ₹165 | 24% | ₹439 | ₹265 |
| 35-44 | 51% | ₹226 | 38% | ₹176 | 34% | ₹400 | ₹261 |
| 45-54 | 6% | ₹218 | 16% | ₹164 | 23% | ₹404 | ₹299 |
| 55-64 | 1% | ₹153 | 3% | ₹181 | 11% | ₹381 | ₹343 |
| 65+ | 0% | ₹288 | 1% | ₹246 | 4% | ₹348 | ₹360 |

Ages 25–55 dominate. For IND1, 25–34 is the most expensive band. The CPL difference is small (≤15%), so age is not a strong lever. CRM leads carry no age, so quality by age can't be measured.

### Meta: gender
- Men are 91–95% of spend.
- TM: female CPL ₹171 vs male ₹169.
- IND1: female CPL ₹267 vs male ₹229.
- The data does not justify the male-only restriction on TM/CCFS/DPIIT/CFO. With Advantage+ it barely matters.

### Meta: placement
| Placement | IND1 spend / leads / CPL | IND3 spend / leads / CPL | IND4 spend / leads / CPL | All (excl. website) CPL |
|---|---|---|---|---|
| FA feed | ₹174k / 720 / ₹242 | ₹26k / 148 / ₹176 | ₹81k / 259 / ₹311 | ₹266 |
| FA reels | ₹131k / 664 / ₹197 | ₹67k / 413 / ₹161 | ₹95k / 220 / ₹431 | ₹246 |
| IN feed | ₹113k / 352 / ₹322 | ₹28k / 155 / ₹182 | ₹44k / 92 / ₹473 | ₹345 |
| IN reels | ₹64k / 363 / ₹176 | ₹46k / 272 / ₹170 | ₹69k / 157 / ₹438 | ₹258 |
| IN stories | ₹26k / 94 / ₹276 | ₹7k / 36 / ₹183 | ₹9k / 18 / ₹488 | ₹329 |

Reels on FB and IG are the cheapest everywhere. **IG feed for IND1 is 33% more expensive (CPM ₹465).** Facebook vs Instagram in CRM (fb/ig stamp, Jun–Sep, n = 1,498 / 855): **no-contact is identical at 44.3%**. Instagram has lower junk (2.9% vs 7.1%), higher strict valid (32.2% vs 28.8%) and higher revenue per lead (₹277 vs ₹246).

### Meta: hour of day (account level)
| Hour band (IST) | Spend | Meta leads | CPL | Share of spend |
|---|---|---|---|---|
| 00-06 | ₹46,233 | 220 | ₹210 | 4% |
| 07-09 | ₹119,914 | 465 | ₹258 | 9% |
| 10-14 | ₹555,238 | 1748 | ₹318 | 43% |
| 15-19 | ₹455,861 | 1619 | ₹282 | 35% |
| 20-23 | ₹117,904 | 480 | ₹246 | 9% |

**Leads are cheapest at night and early morning (₹210 in 00–06) and most expensive at 10:00–14:00 (₹318).**

### CRM: quality by hour of lead arrival (IST)
| Segment | CRM leads | No-contact total | Stuck EC | Lost-Avoiding Call | Lost-junk reason | Lost-qual/lang | Strict valid | Progressed+conv | Won | Won rev | Rev/lead |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1) 09-13 | 996 | 45.2% | 5.3% | 39.9% | 6.7% | 2.6% | 29.9% | 12.2% | 34 | ₹213,069 | ₹214 |
| 2) 13-17 | 1558 | 44.6% | 5.9% | 38.7% | 5.9% | 3.2% | 30.9% | 10.6% | 46 | ₹310,430 | ₹199 |
| 3) 17-20 | 752 | 40.8% | 5.1% | 35.8% | 5.3% | 3.3% | 36.7% | 14.4% | 22 | ₹344,841 | ₹459 |
| 4) 20-23 | 417 | 40.0% | 1.2% | 38.8% | 7.9% | 4.3% | 31.2% | 11.5% | 17 | ₹106,815 | ₹256 |
| 5) 23-09 | 537 | 42.6% | 3.7% | 38.9% | 5.2% | 2.8% | 34.3% | 11.5% | 17 | ₹76,065 | ₹142 |

**No-contact is flat across arrival hours (40–45%).** Night leads (23–09) are no worse: 42.6% no-contact and 34.3% strict valid.

### CRM: day of week
| Segment | CRM leads | No-contact total | Stuck EC | Lost-Avoiding Call | Lost-junk reason | Lost-qual/lang | Strict valid | Progressed+conv | Won | Won rev | Rev/lead |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-Mon | 473 | 41.4% | 6.1% | 35.3% | 7.2% | 2.3% | 35.1% | 12.5% | 14 | ₹309,059 | ₹653 |
| 1-Tue | 781 | 45.3% | 5.1% | 40.2% | 5.5% | 3.7% | 29.2% | 11.5% | 17 | ₹124,518 | ₹159 |
| 2-Wed | 689 | 41.8% | 3.2% | 38.6% | 5.8% | 3.3% | 33.1% | 13.4% | 32 | ₹187,467 | ₹272 |
| 3-Thu | 661 | 43.9% | 4.8% | 39.0% | 6.5% | 3.9% | 31.8% | 11.8% | 29 | ₹130,661 | ₹198 |
| 4-Fri | 782 | 43.0% | 5.9% | 37.1% | 5.1% | 3.2% | 33.4% | 12.3% | 15 | ₹89,511 | ₹114 |
| 5-Sat | 579 | 43.4% | 5.7% | 37.7% | 7.9% | 1.7% | 30.2% | 10.9% | 16 | ₹94,369 | ₹163 |
| 6-Sun | 295 | 45.1% | 2.0% | 43.1% | 4.7% | 3.4% | 34.6% | 9.2% | 13 | ₹115,635 | ₹392 |


### CRM: city tier (form City field)
- Metro/NCR (n = 1,055): no-contact 43.9%, junk 5.6%, strict valid 34.2%, won 4.5%.
- Non-metro (n = 1,806): no-contact 42.6%, junk 6.6%, strict valid 31.2%, won 3.2%.
- **Geography does not explain no-contact.** The win rate is modestly higher in metros (small n). See T4_city.csv for the top 30 cities: Mumbai won 7.5%, Bangalore 6.4%, Noida 7.8%, Delhi 3.8%, Pune 2.0%, Jaipur/Ahmedabad 0.
- Meta spend by region is concentrated in Maharashtra (IND1 32%, IND3 32%, IND4 39%), then Delhi/UP/Karnataka/Telangana.

### CRM: Facebook vs Instagram by campaign
| Segment | CRM leads | No-contact total | Stuck EC | Lost-Avoiding Call | Lost-junk reason | Lost-qual/lang | Strict valid | Progressed+conv | Won | Won rev | Rev/lead |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ('IND1-Incorp', 'fb') | 482 | 40.5% | 6.4% | 34.0% | 9.5% | 3.7% | 30.9% | 8.5% | 5 | ₹20,945 | ₹43 |
| ('IND1-Incorp', 'ig') | 319 | 41.1% | 10.7% | 30.4% | 4.1% | 4.1% | 36.4% | 11.3% | 2 | ₹12,499 | ₹39 |
| ('IND3-TM', 'fb') | 495 | 42.8% | 8.7% | 34.1% | 4.8% | 2.8% | 31.5% | 7.3% | 13 | ₹31,208 | ₹63 |
| ('IND3-TM', 'ig') | 294 | 47.3% | 10.2% | 37.1% | 1.7% | 2.7% | 26.2% | 7.5% | 9 | ₹18,300 | ₹62 |
| ('IND4-CCFS', 'fb') | 410 | 50.0% | 5.6% | 44.4% | 5.4% | 4.4% | 25.9% | 4.9% | 17 | ₹312,062 | ₹761 |
| ('IND4-CCFS', 'ig') | 215 | 43.7% | 4.2% | 39.5% | 2.8% | 3.3% | 36.3% | 7.4% | 9 | ₹205,929 | ₹958 |
| ('IND5-DPIIT', 'fb') | 86 | 46.5% | 3.5% | 43.0% | 10.5% | 4.7% | 22.1% | 4.7% | 1 | ₹4,999 | ₹58 |
| ('IND5-DPIIT', 'ig') | 21 | 52.4% | 9.5% | 42.9% | 0.0% | 0.0% | 19.0% | 0.0% | 0 | - | - |
| ('IND6-CFO', 'fb') | 25 | 44.0% | 8.0% | 36.0% | 20.0% | 0.0% | 8.0% | 0.0% | 0 | - | - |


### CRM: form version and before/after 4 Jul (form reduced from 2 questions to 1)
| Segment | CRM leads | No-contact total | Stuck EC | Lost-Avoiding Call | Lost-junk reason | Lost-qual/lang | Strict valid | Progressed+conv | Won | Won rev | Rev/lead |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ('IND1-Incorp', 'C1 Company+LLP Higher Intent v1') | 867 | 46.9% | 2.7% | 44.3% | 7.8% | 2.4% | 28.7% | 16.4% | 6 | ₹12,534 | ₹14 |
| ('IND1-Incorp', 'C1 | Company+LLP | Higher Intent | v1') | 395 | 44.3% | 2.0% | 42.3% | 8.1% | 3.5% | 30.4% | 13.4% | 2 | ₹10,646 | ₹27 |
| ('IND1-Incorp', 'Incorporation V2') | 742 | 39.4% | 7.8% | 31.5% | 6.9% | 4.0% | 34.4% | 9.8% | 5 | ₹22,798 | ₹31 |
| ('IND2-LLP-ACR', 'LLP ACR') | 219 | 36.1% | 0.0% | 36.1% | 4.6% | 3.2% | 44.7% | 8.7% | 2 | ₹14,912 | ₹68 |
| ('IND3-TM', 'FB TMF 2026 V2') | 219 | 45.2% | 1.8% | 43.4% | 2.3% | 1.4% | 31.1% | 10.0% | 5 | ₹10,500 | ₹48 |
| ('IND3-TM', 'Trademark V2') | 763 | 44.3% | 9.3% | 35.0% | 3.8% | 2.8% | 29.6% | 7.3% | 20 | ₹45,008 | ₹59 |
| ('IND4-CCFS', 'CCFS') | 113 | 41.6% | 1.8% | 39.8% | 2.7% | 3.5% | 44.2% | 12.4% | 6 | ₹69,805 | ₹618 |
| ('IND4-CCFS', 'CCFS2026 V2') | 574 | 47.9% | 5.4% | 42.5% | 4.7% | 3.8% | 28.7% | 5.6% | 23 | ₹498,186 | ₹868 |
| ('IND5-DPIIT', 'DPIIT') | 44 | 54.5% | 9.1% | 45.5% | 2.3% | 4.5% | 31.8% | 9.1% | 0 | - | - |
| ('IND5-DPIIT', 'DPIIT V2') | 88 | 44.3% | 3.4% | 40.9% | 10.2% | 3.4% | 20.5% | 4.5% | 1 | ₹4,999 | ₹57 |
| ('IND6-CFO', 'Virtual CFO Lead Form') | 23 | 56.5% | 13.0% | 43.5% | 4.3% | 4.3% | 13.0% | 0.0% | 0 | - | - |
| ('IND6-CFO', 'Virtual CFO V2') | 17 | 47.1% | 5.9% | 41.2% | 35.3% | 0.0% | 0.0% | 0.0% | 0 | - | - |
| ('UNSTAMPED', None) | 190 | 25.8% | 0.0% | 25.8% | 8.9% | 3.2% | 54.2% | 44.7% | 66 | ₹361,832 | ₹1,904 |

| Segment | CRM leads | No-contact total | Stuck EC | Lost-Avoiding Call | Lost-junk reason | Lost-qual/lang | Strict valid | Progressed+conv | Won | Won rev | Rev/lead |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ('IND1-Incorp', 'pre-4Jul') | 1287 | 46.0% | 2.4% | 43.6% | 7.8% | 2.7% | 29.5% | 15.3% | 9 | ₹23,679 | ₹18 |
| ('IND1-Incorp', 'post-4Jul') | 717 | 39.3% | 8.1% | 31.2% | 7.0% | 4.2% | 34.0% | 9.9% | 4 | ₹22,299 | ₹31 |
| ('IND3-TM', 'pre-4Jul') | 236 | 47.0% | 1.7% | 45.3% | 2.5% | 1.7% | 29.2% | 9.7% | 5 | ₹10,500 | ₹44 |
| ('IND3-TM', 'post-4Jul') | 752 | 43.8% | 9.4% | 34.3% | 3.9% | 2.7% | 30.1% | 7.4% | 20 | ₹45,008 | ₹60 |
| ('IND4-CCFS', 'pre-4Jul') | 117 | 41.9% | 1.7% | 40.2% | 2.6% | 3.4% | 44.4% | 12.0% | 6 | ₹67,305 | ₹575 |
| ('IND4-CCFS', 'post-4Jul') | 570 | 47.9% | 5.4% | 42.5% | 4.7% | 3.9% | 28.6% | 5.6% | 23 | ₹500,686 | ₹878 |

After 4 Jul, IND1's Avoiding Call fell from 43.6% to 31.2%, but stuck rose from 2.4% to 8.1% (part of that is maturity), so total no-contact moved from 46.0% to 39.3%. TM went from 47.0% to 43.8%. CCFS got **worse**, from 41.9% to 47.9% (CCFS2026 V2 form). Junk did not rise after the shorter form.

### CRM: by owner (all paid-Meta leads; owner IDs resolved from the project's owner map)
| Segment | CRM leads | No-contact total | Stuck EC | Lost-Avoiding Call | Lost-junk reason | Lost-qual/lang | Strict valid | Progressed+conv | Won | Won rev | Rev/lead |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Gupta…87006 | 348 | 53.4% | 3.4% | 50.0% | 2.9% | 4.0% | 15.5% | 1.4% | 0 | - | - |
| Gaurav Pandey | 319 | 42.9% | 0.0% | 42.9% | 6.3% | 3.1% | 32.9% | 1.6% | 5 | ₹15,090 | ₹47 |
| Amit Kumar 3 | 318 | 57.9% | 0.3% | 57.5% | 2.2% | 1.9% | 24.2% | 2.8% | 5 | ₹63,576 | ₹200 |
| Aditya Bisht | 303 | 41.3% | 2.6% | 38.6% | 3.3% | 2.6% | 34.3% | 15.2% | 13 | ₹235,885 | ₹778 |
| Rishika Singh | 273 | 64.5% | 0.4% | 64.1% | 1.8% | 1.8% | 20.1% | 4.8% | 12 | ₹82,105 | ₹301 |
| Priyam Tiwari | 272 | 25.7% | 2.2% | 23.5% | 5.5% | 4.8% | 36.8% | 4.4% | 7 | ₹21,770 | ₹80 |
| Pragya Agrawal | 257 | 64.2% | 0.0% | 64.2% | 7.4% | 1.9% | 20.6% | 12.1% | 14 | ₹96,719 | ₹376 |
| Anish Singh | 256 | 43.4% | 5.9% | 37.5% | 8.2% | 2.7% | 23.4% | 9.4% | 6 | ₹134,275 | ₹525 |
| Mahima Sehrawat | 249 | 48.6% | 0.0% | 48.6% | 2.0% | 3.6% | 25.7% | 4.0% | 8 | ₹47,266 | ₹190 |
| Tarun Kumar | 243 | 34.6% | 2.1% | 32.5% | 13.2% | 4.9% | 26.3% | 4.9% | 6 | ₹43,444 | ₹179 |
| Santosh Kumar | 236 | 33.1% | 30.5% | 2.5% | 3.0% | 1.3% | 57.6% | 47.9% | 2 | ₹20,597 | ₹87 |
| Anshu Yadav | 236 | 38.6% | 4.2% | 34.3% | 5.5% | 2.5% | 37.7% | 7.2% | 6 | ₹11,944 | ₹51 |
| Singh…32013 | 169 | 29.0% | 24.9% | 4.1% | 1.2% | 3.6% | 63.9% | 53.8% | 0 | - | - |
| ?…28020 | 149 | 34.2% | 2.0% | 32.2% | 8.7% | 6.0% | 43.0% | 9.4% | 0 | - | - |
| ?…44001 | 93 | 50.5% | 18.3% | 32.3% | 2.2% | 6.5% | 22.6% | 9.7% | 0 | - | - |
| Dwivedi…17014 | 80 | 20.0% | 0.0% | 20.0% | 72.5% | 5.0% | 1.2% | 0.0% | 0 | - | - |
| Singh…74041 | 41 | 24.4% | 0.0% | 24.4% | 4.9% | 2.4% | 56.1% | 0.0% | 0 | - | - |

**The same IND1 lead stream, split by owner** (no-contact %):
- Santosh Kumar 20.5%, Singh…32013 23.6%, Priyam Tiwari 26.8%, Aditya Bisht 34.3%, Anshu Yadav 37.5%, Gaurav Pandey 38.4%, Tarun Kumar 39.3%.
- Mahima Sehrawat 45.5%, Gupta…87006 58.1%, Amit Kumar 3 60.3%, **Rishika Singh 67.7%, Pragya Agrawal 67.7%**.

That is a **3x spread on identical leads**. ⚠️ Converted leads are often re-owned by operations after conversion, so **wins by owner are not reliable**. No-contact by owner is reliable.

Routing anomalies:
- Gupta…87006: 364 leads, 0 won.
- Inactive/unknown users …28020 and …44001: 250 leads, 0 won.
- Dwivedi…17014: 80 leads, 100% Lost and 65% marked Job Seeker/Wrong Info, May–Jun.
- Singh…32013 and Santosh Kumar: leads parked in Negotiation/Establishing Contact.

## 5. Contact-failure diagnosis: is no-contact explained by the ad side?
| Dimension | No-contact range | Read |
|---|---|---|
| Campaign | 36% (LLP ACR) – 53% (CFO); IND1 43.6%, TM 44.5%, CCFS 46.9% | uniform |
| FB vs IG | 44.3% vs 44.3% | none |
| Arrival hour band | 40.0% – 45.2% | none |
| Day of week | 41% – 45% | none |
| City tier | 42.6% – 44.0% | none |
| Form version / pre-post 4 Jul | IND1 46 → 39; CCFS 42 → 48 | mixed, small |
| **Owner (same IND1 stream)** | **20% – 68%** | **dominant** |

**Conclusion:** ad-side changes cannot fix no-contact. It is a sales-process and routing problem, which agrees with the 23 Aug diagnosis. A second leak: **277 leads created before Sep remain in Negotiation/Proposal Sent with no deal; 203 of them are IND1.** That is stale pipeline.

### Junk / targeting check
Lost-junk (Inquired by Mistake / Job Seeker / Wrong Info / Bot / Duplicate) as a share of all leads:
- IND1 7.5%, **TM 3.5%**, CCFS 4.4%, LLP ACR 4.6%, DPIIT 7.6%, **CFO 17.5%** (Job Seeker is 14% of CFO's lost leads — "CFO" pulls in job hunters).
- Qualification/language losses: 2–4%.
- The 4.4% junk for CCFS vs 7.5% for IND1 suggests interest-based INSA targeting lets in more noise than director custom audiences. The gap is small either way.

## 6. Chat benchmark (organic chat sources, Apr–Oct; not paid CTWA)
| Source | Leads | Avoiding Call (unconverted) | Converted | Won | Won rate | Avg ticket |
|---|---|---|---|---|---|---|
| Social - WhatsApp | 169 | 15.9% | 31 | 7 | 4.1% | ₹14,462 |
| Self - Web Chat (SalesIQ) | 346 | 2.1% | 66 | 42 | 12.1% | ₹9,967 |
| Paid Meta Instant Forms | 4,260 | 38.5% | 163 | 136 | 3.2% | ₹7,730 |

Chat leads are self-selected (higher intent), so this is an **upper bound** for CTWA. Organic WhatsApp also carries junk: Job Seeker is 6.5% of WhatsApp leads. The direction is clear, though: people who start a conversation can be reached.

## 7. Product economics for the relaunch
Won deals closed 9 Apr – 6 Oct (all sources): 3,882 deals, ₹3.53 Cr.

| Product | Won n (180d) | Avg ticket | Median | Historical Meta CPL | Meta cost/strict valid | Meta cost/won | First-deal break-even CPL* |
|---|---|---|---|---|---|---|---|
| Trademark filing (TMF) | 355 | ₹8,205 | ₹3,000 | ₹169 (best ad ₹133–151) | ₹590 | ₹6,693 | ₹59 (Meta-TM ticket ₹2,272 × 2.6%) |
| TM back-end: Reply to Exam Report | 134 | ₹5,908 | – | – | – | – | LTV lever |
| Incorporation (Pvt/OPC/Public) | 170 | ₹6,994 | ₹5,124 | ₹232 (new ad ₹172) | ₹817 | ₹13,781 | ₹80 (₹4,584 × 1.75%) |
| Post-INC Key Five Docs | 305 | ₹5,754 | – | – | – | – | LTV lever |
| GST Return Filing | 178 | ₹3,751 | ₹2,500 | **no Meta history** (IND6 bundled "GST" with CFO) | – | – | – |
| Virtual CFO (Lite/Std/Premium) | ~105 | Premium renewal ₹24,966, enrolment ₹14,208; Std ₹7–14k | – | ₹603 | ₹8,244 | none won (n=40) | – |
| Company ACR (incl. CCFS) | 581 | ₹18,770 | – | CCFS ₹398 | ₹1,380 | ₹9,891 | **₹829** (₹19,250 × 4.3%) |
| LLP Annual Return | 247 | ₹7,321 | ₹5,200 | ₹518 | ₹1,665 | ₹3,884 | ₹899 (₹5,715 × 15.7%) |
| DPIIT Recognition | 40 (+5 Seed Fund) | ₹6,421 | ₹5,755 | ₹332 | ₹1,525 | ₹48,815 (n=1) | – |

*Break-even CPL = average Meta-sourced first-deal ticket × historical CRM lead→won rate. LTV is excluded, which matters a lot for TM and Incorporation.

*Estimate, not observed:* if no-contact fell from 44% to 20% and reached leads converted at today's rate, wins would rise about 1.4x. That takes IND1 and TM to roughly 0.47–0.5x first-deal revenue/spend. They still need back-end revenue (Post-INC, TM objection replies, ACR renewals) or a higher-priced bundle to break even.

## 8. Verdict on "IND1 and IND3 worked well, targeting worked, only connectivity was the problem"
- **Targeting worked: mostly TRUE.** Junk is low (TM 3.5%, IND1 7.5%) and so is qualification/language loss (2–4%). Clicks were real business owners.
- **Connectivity was a big problem: TRUE.** 44% of leads were never reached. But it is a **sales-process/routing** failure, not a lead or ad failure: it is flat across platform, hour, geography and form, and varies 3x by owner. Changing ads or switching to CTWA alone will not fix it unless replies are captured in CRM and someone answers within minutes.
- **IND1/IND3 "worked well": FALSE on business outcomes.**
  - IND1: ₹5.10L → 37 wins, ₹1.70L first-deal revenue (0.33x), cost/won ₹13.8k on a ₹4.6k ticket.
  - IND3: 0.34x, cost/won ₹6.7k on a ₹2.3k ticket.
  - Even among reached leads, IND1 converts to a win only about 3%. Post-contact losses are Not Interested (13%), Other CA (9%) and Plan Drop (6%), and **203 IND1 leads are stale in Negotiation/Proposal**.
  - **The only campaigns that returned more than their spend on the first deal were the Annual Return ones** (CCFS 1.95x, LLP ACR 1.47x).
- **"Only connectivity": FALSE.** Offer and price (low first-deal tickets), pipeline follow-through and funding-throttled delivery all contributed.

## 9. Relaunch design (recommendations; estimates are labelled)
1. **Budget mechanics.** ₹10k/day gross is about **₹8,475 net media**; ₹5k gross is about ₹4,237. Fund a ≥7-day prepaid balance and control daily spend with campaign or ad-set budgets. Daily ₹10–15k UPI top-ups caused 46 dark days and repeated learning resets. Expect to pay 18% GST on every top-up.
2. **Split** (net ₹/day, *recommendation*):
   - ACR special ₹4,200 (separate campaign).
   - TM ₹3,000 and Incorporation ₹3,000.
   - One rotating 2-week test slot at ₹2,500 for VCFO → DPIIT → GST Return, about 50–70 leads per product per test. At ₹1k/day for each of three products, no ad set would ever leave learning, because each would get only about 15–25 leads a week at a ₹300–600 CPL.
3. **CPL ceilings** (Meta CPL; pause or rework if a 7-day rolling CPL exceeds the ceiling): TM ≤ ₹170 (target ₹140) · Incorporation ≤ ₹220 (target ₹180) · ACR ≤ ₹500 · DPIIT ≤ ₹350 · VCFO ≤ ₹600 with job-seeker share < 10% · GST Return: start at ≤ ₹250 (no history). Judge on **cost per strict-valid lead**: TM ≤ ₹600, INC ≤ ₹800, ACR ≤ ₹1,400.
4. **Expected outcomes at historical rates** (*estimate*):
   - TM ₹3k/day → about 18–20 leads/day, about 0.45 wins/day (~13/month).
   - INC ₹3k/day → about 13–16 leads/day, about 0.25 wins/day (~7/month).
   - ACR ₹4.2k/day → about 10 leads/day, about 0.45 wins/day (~13/month), at ₹10–19k tickets.
5. **Schedule: run 24 hours.** Night leads are 25–35% cheaper and no worse in quality, and 24Hr INSA beat Daytime INSA. Pair this with an instant WhatsApp acknowledgement and a 09:15 first-call rule for night leads.
6. **Audience.**
   - Keep the INSA interest set and Director/LLP custom audiences with Advantage+ audience.
   - **Drop the LAL1% Director/web-visitor ad set** (CPL ₹548, 12% junk).
   - Use director custom audiences for ACR (proven).
   - Remove the male-only restriction; women's CPL matches for TM.
   - Keep the 18–30 metro/tier-2 city lists; geography is not the lever.
   - Ages 25–55; the 25–34 band is the most expensive for INC but not junkier.
7. **Placements.** Keep FB+IG feed and reels and lean into reels (cheapest CPL everywhere). For Incorporation, consider excluding or capping IG feed (CPL ₹322, CPM ₹465). Instagram leads have lower junk and higher revenue per lead, so don't exclude IG entirely.
8. **Creative.**
   - Lead with an explicit, transparent price (TM "₹1,999 + govt fee ₹4,500"; INC "₹2,499 professional fee, govt fees at actuals") plus one concrete deliverable.
   - Kill "free search" and generic or fear angles.
   - For ACR, use a filing-deadline hook (AOC-4 / MGT-7 / LLP Form 8 for FY 2025-26). Verify the exact due dates before running them.
   - Drop "in 7 days" unless it can be honoured or is qualified ("typically", "subject to MCA processing").
9. **CTWA vs Instant Form.** Run CTWA **alongside** forms at equal budget for TM and INC, not instead of them. Measure cost per strict-valid lead and cost per won.
   - The May test: ₹343 per conversation vs ₹400 per form lead in the same audience.
   - Organic chat leads reach Avoiding Call 2–16% vs 38.5% for forms.
   - Before launch, map CTWA to CRM: populate `CTWA_Click_ID`, set `Lead_Source`, and auto-create the lead. The May test was lost because the 77 conversations never reached CRM.
   - Staff WhatsApp replies within 5 minutes during the day.
   - For VCFO, use form-only or CTWA with a screening question. Job seekers make up 17.5% of junk there.
10. **Sales process (bigger lever than the ads).**
    - Route paid-Meta leads only to active Sales-RM users. Remove the Gupta…87006, inactive …28020/…44001 and Gold-Team queues (about 700 leads, 0–2 wins).
    - Require 6 logged attempts before "Avoiding Call", and require a dialer.
    - Run a weekly review of leads in Negotiation/Proposal for more than 14 days (277 stale).
    - Keep `RM_Lead_Quality` from defaulting to "Valid - RM Working".

## 10. Files saved here
`T1_campaign_kpis.csv`, `T1b_campaign_won_inferred.csv`, `T2b_campaign_month.csv`, `T3a_adset.csv`, `T3b_ad.csv`, `T4_state_*.csv`, `T4_city.csv`, `T4_hour.csv`, `T4_owner.csv`, `T7_won_by_product_180d.csv`, `T7_product_groups_180d.csv`, `meta_campaign_monthly.csv`, `meta_ads.csv`, `meta_age_gender.csv`, `meta_placement.csv`, `meta_region_spend.csv`, `meta_hourly.csv`, `meta_daily.csv`, `leads_enriched.json` (lead-level joined dataset), `raw/` (CRM pulls).
