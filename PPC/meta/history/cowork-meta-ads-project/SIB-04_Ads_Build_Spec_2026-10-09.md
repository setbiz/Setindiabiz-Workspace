# SIB-04 Annual Filings: Meta Ads Build Spec (v2, awaiting Sanjeev's go)

Prepared 9 October 2026; v2 at 19:10 IST after Sanjeev's answers. Nothing has been built or changed in Meta, Canva, SalesIQ or CRM. Meta account 152154124583473 still has 7 paused campaigns and an empty Ads Manager draft.

## Decisions (Sanjeev, 9 October 2026, 18:56 IST)

| # | Question | Decision | Effect on the build |
|---|---|---|---|
| Q1 | Is the statutory audit in the ₹7,499 pack? | Yes, included; marketing wording is "audit support". | Keep "Complete annual filing". Add "audit support" to the inclusions on the images (G2) and in the ad text. |
| Q2 | Which director audiences? | All companies up to 2025-26. | Suggestions: Company Director 2019-20 to 2025-26 and LAL-Director-2024-25 1%; not 2026-27. LLP 2019-20 to 2025-26 added for the LLP ad. |
| Q3 | ACR-C5 photo | AI-generated. | Meta AI disclosure OPT_IN on both ACR-C5 ads. Meta may show an "AI info" label. |
| Q4 | Build route | API plus browser. | Campaign and CTWA ad set through the API; form, form ad set and all ads through Ads Manager. |
| Q5 | Form completion button | WhatsApp button; duplicate or test leads are acceptable. | Completion screen opens WhatsApp to [phone redacted]. |
| Q6 | LLP Form 8 ad | Yes. | New creative LLP-C1 (G3) and a fourth ad in each ad set until 30 October. |

Still with Sanjeev before launch: confirm [phone redacted] is linked to the Page "Setindiabiz Private Limited" (627814417091714) in Meta Business Suite; fund the account or turn on auto-pay (SIB-04 at ₹6,000 a day plus 18% GST is ₹7,080 a day, about ₹49,560 for 7 days).

## 1. Law and Fee Check (as on 9 October 2026)

| Point | Position | Basis |
|---|---|---|
| AGM | Within six months of the financial year end, so 30 September 2026 for FY 2025-26. First AGM within nine months, so 31 December 2026. An OPC holds no AGM. | Sec. 96(1), Companies Act, 2013 |
| AOC-4 | Within 30 days of the AGM: 30 October 2026 for an AGM on 30 September. OPC: within 180 days of the year end, which was 27 September 2026 and has passed. | Sec. 137(1) and its proviso |
| MGT-7 / MGT-7A | Within 60 days of the AGM: 29 November 2026 for an AGM on 30 September. | Sec. 92(4) |
| Day count | Sec. 9, General Clauses Act, 1897 excludes the AGM day, giving 30 October and 29 November. Some competitors print 29 October and 28 November. Copy keeps the condition "AGM held on 30 September". | Settled 6 October (Competitor scan) |
| Additional fee, companies | ₹100 a day for each form (AOC-4 in all variants, MGT-7, MGT-7A), no upper limit, on top of the normal fee. | Sec. 403(1), read with the Annexure to the Companies (Registration Offices and Fees) Rules, 2014 as amended by the Second Amendment Rules, 2018 (from 1 July 2018). The only 2026 amendment, G.S.R. 300(E) of 21 April 2026, replaced item VII (DIR-3 KYC Web fees) and leaves this untouched. |
| MCA relaxation for FY 2025-26 | None found. 2026 circulars so far: GC 01/2026 (CCFS), 02/2026 (DPT-3 to 31 July), 03/2026 and 04/2026 (CCFS to 31 August, then 15 September). | For FY 2024-25 MCA waived the additional fee on 17 October 2025 (GC 06/2025) and extended the waiver to 31 January 2026 (GC 08/2025). A repeat this month would make every "₹100 a day" company ad misleading from that day: see the stop rule in section 8. |
| LLP Form 8 | Within 30 days from the end of six months of the financial year: 30 October 2026. | Sec. 34, LLP Act, 2008 read with Rule 24(4), LLP Rules, 2009. The handover cited Rule 24(8); that sub-rule is the audit threshold, not the filing time. |
| LLP late filing fee | Multiples of the normal fee by delay band since 1 April 2022: Small LLP 1, 2, 4, 6, 10, 15 times; other LLPs 1, 4, 8, 12, 20, 30 times. Beyond 360 days, Form 8 and Form 11 attract 15 times plus ₹10 a day (Small LLP) or 30 times plus ₹20 a day (others). | Annexure A, LLP Rules, 2009, substituted by G.S.R. 109(E) of 11 February 2022 |
| LLP penalty | Separate from the fee: an LLP that fails to comply with Sec. 34(3) is liable to a penalty of ₹100 a day, up to ₹1 lakh for the LLP and up to ₹50,000 for each designated partner. It is imposed by the adjudicating officer, so ad copy says "can be". | Sec. 34(5), LLP Act, as substituted by Sec. 13 of the LLP (Amendment) Act, 2021, in force from 1 April 2022 |
| LLP Form 11 | Within 60 days of the year end (30 May). Not advertised. | Sec. 35, LLP Act read with Rule 25(1) |

Correction to the first version: "₹100 a day" may appear in the LLP ad, but only as the Sec. 34(5) penalty with its caps, never as the filing fee. Our page setindiabiz.com/learning/llp-form-8-filing-late-fee calls ₹100 a day the late fee; that is a content fix for the website team (the late fee is the slab multiple; ₹100 a day is the penalty).

Not opened in this session: MCA's own fee table on mca.gov.in. The ₹100-a-day company rule was read from a copy of the 2018 Second Amendment Rules and the Annexure as reproduced by ICAI branch sites. Confirm once on the MCA fee calculator before publishing.

## 2. Creatives: Canva Folder "PPC 2026"

Two designs, three pages each: "SIB-04 Annual Filings – 1:1 Feed" (DAHXThVtclk) and "SIB-04 Annual Filings – 9:16 Stories/Reels" (DAHXT5r2Ex8). Page 1 is ACR-C2 (cost of delay), page 2 is ACR-C1 (deadline), page 3 is ACR-C5 (dates and price).

What checks out: "₹100 a day, per form, no upper limit" matches the Fees Rules; the bars (₹6,000 at 30 days, ₹18,000 at 90, ₹36,000 at 180) equal ₹100 × days × 2 forms and the footnote says so; dates carry the 30 September AGM condition; every price shows "+ GST"; government fees at actuals; turnover limit of ₹5 lakh; "not affiliated with MCA"; no ADT-1 or DIR-3 KYC.

| # | Page | Now | Change |
|---|---|---|---|
| F1 | 2, both sizes | "AGM HELD ON 30 SEP 2026?, File Annual Returns on time to avoid Late filing costs" (stray "?,") | "AGM held on 30 Sep 2026? File annual returns on time to avoid late filing costs" |
| F2 | 1, 2 and 3, both sizes (footer) | "Pack for companies with turnover up to ₹5 lakh: AGM documents, AOC-4, MGT-7 / 7A and ITR-6." | "Pack for companies with turnover up to ₹5 lakh: AGM documents, audit support, AOC-4, MGT-7 / 7A and ITR-6." |
| F3 | 3, both sizes | AI-generated photo | No change; disclosure OPT_IN on the ads |

New creative LLP-C1 (1:1 and 9:16), built by copying page 2 of each design into a new design "SIB-04 LLP Form 8" in the same folder. On-image text:

| Element | Text |
|---|---|
| Top bar | ATTENTION: DESIGNATED PARTNERS OF LLPs |
| Pill | LLP FORM 8 · FY 2025-26 |
| Headline | File your Statement of Account and Solvency on time |
| Calendar card | OCTOBER 2026 · 30 · Form 8 due |
| Warning line | Miss it: penalty can be ₹100 a day, up to ₹1 lakh for the LLP (Sec. 34(5), LLP Act) |
| Price box | LLP Form 8 from ₹2,499 + GST |
| CTA | Chat on WhatsApp |
| Footer | setindiabiz.com · Professional fee + GST; government fees at actuals. Setindiabiz is a private professional services firm, not affiliated with MCA. |

From 31 October the 30 October date on ACR-C1, ACR-C5 and LLP-C1 is in the past. A MGT-7-only creative ("MGT-7/7A due 29 Nov") is needed from the designer by 28 October.

## 3. Campaign Structure

| Level | Name | Settings |
|---|---|---|
| Campaign | SIB-04 Annual Filings | Objective Leads. Budget at ad-set level (ABO). No special ad category. The name must start with "SIB-04": the CRM assignment rule and the plug both key on it. |
| Ad set A | SIB-04 \| ACR \| CTWA \| IN | Conversion location WhatsApp, number [phone redacted], Page 627814417091714, Instagram setindiabiz_official. Goal: maximise conversations. ₹3,500 a day. Highest-volume bidding. |
| Ad set B | SIB-04 \| ACR \| Form \| IN | Instant Form "SIB-04 ACR Form v1". Goal: maximise leads. ₹2,500 a day. Highest-volume bidding. |
| Both ad sets | | India. Advantage+ audience with age 25+. Audience suggestions: Company Director 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26; LAL-Director-2024-25 1%; LLP 2019-20 to 2025-26. Facebook and Instagram placements (no Audience Network). No dayparting. End 29 November 2026, 23:59 IST. Start when Sanjeev switches on. |
| A/B test | CTWA vs Form | Meta Experiments, 14 days, key metric cost per result. Set up at launch (needs live ad sets). Form leads who tap the WhatsApp completion button will also show as chats; accepted by Sanjeev. |

Audience IDs: Company Director 2019-20 120243249278260449, 2020-21 120243249316070449, 2021-22 120227495253470449, 2022-23 120226471598550449, 2023-24 120226339094810449, 2024-25 120226217224820449, 2025-26 120243249459750449; LAL-Director-2024-25 1% 120239558688100449; LLP 2019-20 120242016865360449, 2020-21 120242016337960449, 2021-22 120224166934370449, 2022-23 120224128668320449, 2023-24 120223743527150449, 2024-25 120223362685870449, 2025-26 120240556758770449.

## 4. Ads and Copy

Four ads in each ad set. Each uses the 1:1 image for feeds and the 9:16 image for Stories and Reels. CTA "Send WhatsApp message" in ad set A, "Get quote" in ad set B. Advantage+ creative enhancements off, including text improvements, so Meta cannot rewrite statutory figures. AI disclosure: OPT_IN on ACR-C5; OPT_OUT on the others unless they also contain AI imagery (Sanjeev to say if so).

Ad names: "ACR-C1 | Deadline | CTWA", "ACR-C2 | Cost of delay | CTWA", "ACR-C5 | Dates and price | CTWA", "LLP-C1 | Form 8 | CTWA", and the same four ending "| Form".

**ACR-C1, deadline (page 2)**

> AGM held on 30 September 2026? AOC-4 is due by 30 October and MGT-7/MGT-7A by 29 November (Secs. 137(1) and 92(4), Companies Act, 2013). File late and MCA charges an additional fee of ₹100 a day for each form, with no upper limit.
>
> Our annual filing pack for companies with turnover up to ₹5 lakh covers AGM documents, audit support, AOC-4, MGT-7/7A and the company's ITR-6 for ₹7,499 + GST. Government fees at actuals.
>
> Tap Chat on WhatsApp and tell us the entity type and the years pending.

Headline: AOC-4 by 30 Oct, MGT-7 by 29 Nov
Description: Annual filing pack ₹7,499 + GST
Pre-filled WhatsApp message: Hi Setindiabiz, I want to file my company's AOC-4 and MGT-7. [ACR-C1]

**ACR-C2, cost of delay (page 1)**

> Late ROC filing costs ₹100 a day for each form, with no upper limit. If AOC-4 and MGT-7 are both 90 days late, the additional fee alone is ₹18,000 (Sec. 403, Companies Act, 2013 read with the Companies (Registration Offices and Fees) Rules, 2014).
>
> File FY 2025-26 on time. Pack for companies with turnover up to ₹5 lakh: AGM documents, audit support, AOC-4, MGT-7/7A and ITR-6 for ₹7,499 + GST. Government fees at actuals.
>
> Chat with us on WhatsApp to check your company's due dates.

Headline: ₹100 a day per form, no upper limit
Description: File AOC-4 and MGT-7 on time
Pre-filled WhatsApp message: Hi Setindiabiz, I want to file my annual returns before late fees start. [ACR-C2]

**ACR-C5, dates and price (page 3)**

> Directors of private limited companies: if your AGM was on 30 September 2026, AOC-4 is due by 30 October and MGT-7/7A by 29 November. After that, ₹100 a day per form.
>
> Setindiabiz has served 25,000+ businesses. Annual filing pack for companies with turnover up to ₹5 lakh: AGM documents, audit support, AOC-4, MGT-7/7A and ITR-6 for ₹7,499 + GST. Government fees at actuals.
>
> Setindiabiz is a private firm, not affiliated with MCA.

Headline: Annual filing pack ₹7,499 + GST
Description: AGM on 30 Sep? AOC-4 due 30 Oct
Pre-filled WhatsApp message: Hi Setindiabiz, please share details of the ₹7,499 annual filing pack. [ACR-C5]

**LLP-C1, Form 8 (new creative)**

> LLP Form 8 (Statement of Account and Solvency) for FY 2025-26 is due by 30 October 2026 (Sec. 34, LLP Act, 2008 read with Rule 24(4), LLP Rules, 2009). Miss it and the LLP can be penalised ₹100 a day up to ₹1 lakh, plus up to ₹50,000 for each designated partner (Sec. 34(5)), over and above a late filing fee that rises with the delay.
>
> LLP Form 8 filing from ₹2,499 + GST. Government fees at actuals.
>
> Tap Chat on WhatsApp and we will check what your LLP has pending.

Headline: LLP Form 8 due 30 Oct 2026
Description: Form 8 filing from ₹2,499 + GST
Pre-filled WhatsApp message: Hi Setindiabiz, I want to file Form 8 for my LLP. [LLP-C1]

In the Form versions, the last line of ACR-C1, ACR-C2 and LLP-C1 reads: "Tap Get quote and answer two short questions. Our team will call or WhatsApp you." ACR-C5 is unchanged.

"25,000+ businesses served" is the settled claim (29,367 CRM accounts, Decisions Log 6 October). LLP Form 8 "from ₹2,499 + GST" is from the same log.

The bot passes the fixed code "ACR" to CRM, so Meta_Ad_Code will not show C1, C2, C5 or LLP-C1. The per-ad split comes from Meta's conversation count by ad; the bracketed code still tells the owner which ad the person came from.

## 5. Instant Form "SIB-04 ACR Form v1"

| Part | Content |
|---|---|
| Type | Higher intent (adds a review step). After the 4 July change from two questions to one, the early read showed valid% falling from 38.8% to 36.1%; at a ₹19,442 average ACR ticket, fewer and better leads is the right trade. |
| Intro | Headline "Annual filing for FY 2025-26". Text: "AGM on 30 September 2026? AOC-4 is due by 30 October and MGT-7/7A by 29 November. LLP Form 8 is due by 30 October. Answer two questions and our team will contact you." |
| Q1 | What type of entity is it? Private Limited / One Person Company (OPC) / LLP |
| Q2 | Which years are pending? FY 2025-26 only / FY 2025-26 and earlier years / Not sure |
| Contact | Full name, phone number, email (prefilled by Meta) |
| Privacy | https://www.setindiabiz.com/privacy-policy (checked live 9 October; updated 4 October 2026) |
| Consent | Custom disclaimer, required checkbox: "I agree to be contacted by Setindiabiz on phone and WhatsApp about this enquiry." |
| Completion | "Thank you. Our team will contact you on the number you shared. To talk now, chat with us on WhatsApp." Button: WhatsApp (native option if Ads Manager offers it for [phone redacted], otherwise a link to https://wa.me/919266601455 with the text "Hi Setindiabiz, I just filled the annual filing form. [IF-ACR]"). |

A form cannot be deleted once created, only archived, so it is built once.

After the form exists, Sanjeev sets the LeadChain SIB-04 chain: rule "PPC - SIB-04 Annual Filings - LG-11", static Tag FB-ACR, Product Cat Annual Filing, and Q1/Q2 into Description.

## 6. Build Route B (chosen)

Through the API: campaign (G4) and CTWA ad set A (G5), both created switched off. Through Ads Manager in Claude in Chrome on "SK Big HP": Instant Form, ad set B and all eight ads, saved unpublished until G11.

Why the split: the connector cannot set a WhatsApp pre-filled message or attach an Instant Form to a creative, and it still reports leadgen_tos_accepted = false for both Pages (627814417091714 and 185807091504036), so a lead-form ad set through the API would be refused. Ads Manager has worked for both since July.

If the session's permission check blocks a click, the screen is left ready and the click is handed to Sanjeev.

## 7. Go List (one at a time; Claude acts only on a go that names the item)

| # | Change | Where |
|---|---|---|
| G1 | F1 typo fix, page 2 of both designs | Canva |
| G2 | F2 "audit support" in the footer, pages 1–3 of both designs | Canva |
| G3 | New design "SIB-04 LLP Form 8" (1:1 and 9:16) per section 2 | Canva |
| G4 | Campaign "SIB-04 Annual Filings": OUTCOME_LEADS, auction, no special category, no campaign budget, PAUSED | API |
| G5 | Ad set "SIB-04 \| ACR \| CTWA \| IN": CONVERSATIONS, destination WhatsApp, promoted object Page 627814417091714 + number [phone redacted], ₹3,500 a day, IMPRESSIONS billing, lowest cost, targeting and audience suggestions per section 3, end 29 Nov 2026 23:59 IST, PAUSED | API |
| G6 | Instant Form "SIB-04 ACR Form v1" per section 5 | Ads Manager |
| G7 | Ad set "SIB-04 \| ACR \| Form \| IN" per section 3 | Ads Manager |
| G8 | Upload the eight PNGs; build ACR-C1, C2, C5, LLP-C1 in ad set A | Ads Manager |
| G9 | Same four ads in ad set B | Ads Manager |
| G10 | Preview pack to Sanjeev: every ad in Feed, Stories and Reels (read-only, no go needed) | Chat |
| G11 | Publish ad set B and all ads with every toggle off | Ads Manager |

Activation, the A/B test start and funding stay with Sanjeev. Exporting PNGs from Canva changes nothing and needs no go.

## 8. Reporting, Stop-Loss and Wind-Down

SIB-04 segment for the scorecard: Leads where Lead_Source is one of 'Advt - Facebook', 'Advt - Instagram', 'Advt - WhatsApp' and Meta_Campaign starts with 'SIB-04'. CTWA half = 'Advt - WhatsApp'; Form half = the other two (form leads who also chat may appear in both; Sanjeev accepted this). An empty Lead_Status counts as never worked. COQL needs binary nesting: `((Lead_Source in (...)) and (Meta_Campaign like 'SIB-04%'))`, then the date range as a third nested condition.

Replacement line for the project instructions (Sanjeev pastes; the current text still names "PPC Meta Insta"): "Paid Meta = Lead_Source 'Advt - Facebook', 'Advt - Instagram' and 'Advt - WhatsApp' (CTWA chats claimed by the SalesIQ plug). Organic 'Social - Facebook', 'Social - Instagram' and 'Social - WhatsApp' are excluded."

| Rule | Trigger | Action |
|---|---|---|
| Cost stop | 3-day cost per conversation or lead above ₹1,000 (twice the ₹500 ceiling) | Propose pausing that ad set |
| Capture stop | 2 spend days with 0 CRM leads from an ad set | Propose pausing it; check the plug or LeadChain chain |
| Legal stop | MCA circular relaxing additional fees for FY 2025-26 company annual filings | Pause every company ad saying "₹100 a day" the same day; swap copy |
| Date switch | 31 October | ACR-C1, ACR-C5 and LLP-C1 off; MGT-7-only creative on |
| End | 29 November 2026, 23:59 IST | Ad sets end |

## 9. Sources Opened on 9 October 2026

- Sec. 403 text: https://www.incometaxindia.gov.in/w/section-403-2 (government)
- G.S.R. 300(E), 21 April 2026: https://egazette.gov.in/WriteReadData/2026/271973.pdf (government)
- GC 03/2026, 8 July 2026: https://www.caalley.com/mca26/circular-20260708.pdf (copy of the circular)
- GC 08/2025, 30 December 2025: https://www.icai.org/post/clcgc-announcement-30122025
- Companies (Registration Offices and Fees) Second Amendment Rules, 2018: https://ca2013.com/wp-content/uploads/2018/05/companies-Registration-offices-and-Fees-Second-Amendment-Rules-2018..pdf (copy)
- LLP Rules Annexure A after G.S.R. 109(E): https://www.taxmanagementindia.com/visitor/detail_act.asp?ID=13295 and https://vasai.icai.org/detail/14248.aspx (reproductions)
- Rule 24(4) LLP Rules (2011 amendment text): https://taxguru.in/?p=45027
- LLP (Amendment) Act, 2021, Secs. 13 and 15: https://prsindia.org/files/bills_acts/acts_parliament/2021/The%20Limited%20Liability%20Partnership%20(Amendment)%20Act,%202021.pdf
- Commencement of Secs. 1–29 of the 2021 Amendment Act from 1 April 2022: https://www.taxmann.com/post/blog/government-notifies-applicability-of-sec-1-to-29-of-llp-amendment-act-2021-w-e-f-01-04-2022/
- Privacy policy: https://www.setindiabiz.com/privacy-policy
