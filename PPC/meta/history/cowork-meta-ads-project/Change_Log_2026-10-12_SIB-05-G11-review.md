# Change log: SIB-05 G11 claims review, SIB-04 day-3 check (12 Oct 2026, 14:04–14:15 IST)

Follows `Change_Log_2026-10-12_SIB-05-G3c-G10.md` (R105–R116, C81–C87). G11 deliverable: `Meta Ads/SIB-05_G11_Creative_Copy_and_Claims_Review_2026-10-12.md`.

## Read-only checks

| # | Item | Finding | Method |
|---|---|---|---|
| R117 | SIB-05 form leads | 0 for "SIB-05 India Entry Form v1" at 14:05 and again at 14:11. G9 not yet run. Sanjeev asked at 14:05 to submit the three test leads. | COQL |
| R118 | SIB-04 Meta, 10–12 Oct (12 Oct to ~14:10) | Spend ₹15,608.65: form ads ₹6,258.62, CTWA ads ₹9,350.03; 12 Oct so far ₹3,250.15. Meta form leads 20: ACR-C1 8 (5/1/2), LLP-C1 7 (1/6/0), ACR-C2 4 (1/1/2), ACR-C5 1 (0/1/0). All 8 ads ACTIVE; LLP-C1 CTWA and ACR-C5 CTWA show no spend. | Meta connector, ad level, daily |
| R119 | SIB-04 CRM vs Meta by day (form) | 10 Oct 5 vs 7; 11 Oct 9 vs 9; 12 Oct 4 vs 4. Gap still 2, on 10 Oct (ACR-C1); see open item 7 of the 12 Oct G3c/G10 log. | COQL on Meta_Campaign "SIB-04 Annual Filings" |
| R120 | SIB-04 CRM totals | 46 leads (18 form, 28 WhatsApp); new since 13:25: WhatsApp lead 946493495 (14:02, Praveen Singh). Valid Lead or Proposal Sent: form 3/18 (17%), WhatsApp 11/28 (39%). 3 Proposal Sent, all WhatsApp; 2 Lost, both WhatsApp. Cost per valid (ad-set spend): form ₹2,086, WhatsApp ₹850, all ₹1,115. Cost per CRM lead: form ₹348, WhatsApp ₹334. | COQL; Python tally |
| R121 | Speed-to-lead at 14:10 | Blank status 15 (8 form, 7 WhatsApp); Establishing Contact 15. Not worked 30/46 (65%). Blank and 4+ h old (12): Praveen Singh 946538212 (WA, 46 h); Sudip Manna 946575232, 946586161 (form, ~42 h); Priyam Tiwari 946561179 (WA, 20 h); Pavneet Kaur 946488294, 946463322, 946538331 (form, 15–17 h); Gaurav Pandey 946400318 (WA, 16 h); admin account 946543271, 946567286 (form, 14–15 h); Mahima Sehrawat 946420324 (WA, 6 h); Sudip Manna 946532320 (WA, 4 h). Since 13:25: Praveen's form lead 946520482 moved to Establishing Contact. | COQL |
| R122 | Owner "Gupta" (…893487006) | Krishna Gupta, Sales RM Roles, active, reports to Suman Khowal. Closes the gap in R112. | getSingleUser |
| R123 | FC-GPR timing | Reg. 4(1), FEMA 395/2019-RB (17 Oct 2019, amended up to 13 Jun 2026): FC-GPR "not later than thirty days from the date of issue of equity instruments", where the issue is reckoned as FDI. S2 line verified. | rbi.org.in, BS_FemaNotifications Id=11723 and Master Direction page |
| R124 | BO/LO rules | RBI Master Direction 10/2015-16 still "updated as on 18 May 2021": BO five years' profit record and USD 100,000; LO three years and USD 50,000; LO generally valid three years; Form FNC to an AD Category-I bank the applicant chooses; prior RBI approval list unchanged. | rbi.org.in |
| R125 | LO definition | Reg. 2(5), FEMA 22(R)/2016-RB: no commercial, trading or industrial activity; funded by inward remittances. The words "earn income" do not appear, so the copy was reworded. | rbi.org.in, Id=10327 |
| R126 | Press Note 2 (2026) and NDI amendments | dpiit.gov.in press-note page did not render; no Gazette copy opened. Secondary: PN2 dated 10 Mar 2026; NDI (Amendment) Rules S.O. 2174(E) of 1 May 2026 and S.O. 2186(E) of 2 May 2026; **Third Amendment S.O. 3030(E) of 12 Jun 2026** adds land-border control triggers in rules 12 and 13 (not in the build spec). | Web (K S & K, TaxGuru) |
| R127 | Sec. 149(3) | indiacode.nic.in returned a server error. Not used in any ad. | Web |
| R128 | Canva "SIB Relaunch Oct 2026 – 1:1 working set" (DAHXTezZ4Nk) | India-entry pages: S1 small print says land-border investors "need prior Government approval" (outdated); "End to End" headline conflicts with the USD 499 scope; "CS & CA Experts" needs confirming; E1 has typo "FIDI" and CTA "Get the India-entry checklist" with no checklist behind it. | Canva read-design |

## Changes

None. No Meta campaign, ad set, ad, form or budget was created or changed. No money was moved. No CRM record, rule, template, workflow, function or LeadChain chain was edited. Nothing in Canva or WordPress was changed.

One project doc written: the G11 copy and claims review.

## Open

| # | Item | Who |
|---|---|---|
| 1 | **G9 test leads** on form 4073050519663550 (subsidiary + US; branch + Japan; not sure + Other), then the WhatsApp-button phone test. Claude checks per the G9 list; Sanjeev deletes the test leads. | Sanjeev runs, Claude checks |
| 2 | **G11 decisions A–E** in the claims review (approve copy; S1 scope line; footer wording; "CS & CA Experts"; E1 checklist CTA). | Sanjeev |
| 3 | Designer builds 12 images after approval; Claude reviews the images before G12. | Designer, Claude |
| 4 | Open Press Note 2 (2026) and S.O. 2174(E) / 3030(E) from a government site; add S.O. 3030(E) to spec section 1 and the legal stop in section 8. | Claude |
| 5 | **SIB-04 unworked leads:** Pavneet 3 form (15–17 h), Sudip Manna 2 form (42 h) + 1 WhatsApp, Praveen Singh 1 WhatsApp (46 h), admin account 2. Form quality cannot be judged while 8 of 18 form leads are untouched. | Sanjeev |
| 6 | Carried from the G3c/G10 log: items 2–9 (tell Pavneet; Sudip and Praveen; 946567286 on admin; duplicate handling; merges; two missing ACR-C1 leads in the Recycle Bin; routing type; Job title mapping). | Sanjeev |
| 7 | SIB-04: daily counts and speed-to-lead; MGT-7 creative by 28 Oct; 31 Oct pause proposal for C1, C5, LLP-C1 (30 Oct dates); MCA circular watch. | Claude / Sanjeev |
| 8 | Raise when there is time: privacy policy s.16 and s.4; the "15–21 Days" subsidiary page; Bookings service text. | Sanjeev |
