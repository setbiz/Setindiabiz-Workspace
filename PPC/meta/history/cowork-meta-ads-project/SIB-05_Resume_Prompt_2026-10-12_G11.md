You are continuing two Setindiabiz Meta jobs:
- **SIB-04 Company Annual Filings** is live.
- **SIB-05 India Entry (FDI Services)** is being built.

Zoho CRM is crm.zoho.com (US DC). The Meta account is 152154124583473. Meta tool calls use client_model "claude-opus-5-5".

Read these project docs first:
- Meta Ads/Change_Log_2026-10-12_SIB-05-G11-review.md: R117–R128, open items.
- Meta Ads/SIB-05_G11_Creative_Copy_and_Claims_Review_2026-10-12.md: decisions A–E, revised copy for the six ads, designer brief, substantiation list.
- Meta Ads/Change_Log_2026-10-12_SIB-05-G3c-G10.md: C81–C87 and open items 2–9.
- Meta Ads/SIB-05_India_Entry_Build_Spec_2026-10-10.md (v4): D1–D20, G1–G13, section 3 campaign structure, section 4 form and LeadChain map.
- Meta Ads/SIB-04_Resume_Prompt_2026-10-10_ppcformtidy.md: SIB-04 steps 3–7 still apply.

## State at 12 Oct, 14:15 IST

**SIB-05, built:** Tag FB-FDI; assignment rule "PPC - SIB-05 India Entry - PG-02" (round robin over five handlers, default Pavneet Kaur); PPC Form Tidy CONFIG block; privacy policy s.18 live; Instant Form "SIB-05 India Entry Form v1" (4073050519663550, Active); LeadChain chain "FB SIB-05 FDI v1" (Active, Job title unmapped); G3c SalesIQ routing (C82–C84); G10 booking email template, notification and workflow (C85–C87).

**SIB-05, in progress:**
- **G9:** 0 leads on the form at 14:11. Sanjeev was asked at 14:05 to submit the three test leads.
- **G11:** copy reviewed and revised; waiting for Sanjeev's decisions A–E. Nothing changed in Canva.
- G12 and G13 not started.

**Legal points verified 12 Oct (rbi.org.in):** FC-GPR within 30 days of each issue (Reg. 4(1), FEMA 395/2019-RB, amended to 13 Jun 2026); BO 5 years/USD 100k and LO 3 years/USD 50k (Master Direction 10/2015-16, updated 18 May 2021); LO definition, Reg. 2(5) FEMA 22(R)/2016-RB. Still secondary only: Press Note 2 (2026) (10 Mar 2026), NDI amendments S.O. 2174(E) 1 May, S.O. 2186(E) 2 May and **S.O. 3030(E) 12 Jun 2026** (third amendment, land-border control triggers, not yet in the spec); Sec. 149(3).

**SIB-04 (10 Oct 13:35 – 12 Oct ~14:10):** ₹15,608.65 spend (form ₹6,258.62, CTWA ₹9,350.03). 46 CRM leads (18 form, 28 WhatsApp). Valid or Proposal Sent: form 3/18, WhatsApp 11/28. Cost per valid: form ₹2,086, WhatsApp ₹850. Meta 20 form leads vs CRM 18 (gap 2 on ACR-C1, 10 Oct). Not worked (blank or Establishing Contact) 30/46; 12 blank for 4+ h (Pavneet 3 form, Sudip Manna 2 form + 1 WhatsApp, admin 2, Praveen Singh, Priyam Tiwari, Gaurav Pandey, Mahima Sehrawat 1 WhatsApp each). "Gupta" = Krishna Gupta (…893487006, Sales RM).

## Next, in Order

1. **G9** as soon as Sanjeev says the test leads are in (subsidiary + United States; branch office + Japan; not sure yet + Other). COQL on `Meta_Lead_Form = 'SIB-05 India Entry Form v1'`, then getRecord and getTimelines for each. Check:
   - owner is Foziya Ansari 1123581000033869514, Gaurav Pandey 1123581000900792006, Karishma Singh 1123581000458244001, Rishika Singh 1123581000754062001, Shubendu Banerjee 1123581000037468001 or Pavneet Kaur 1123581000757738001, and "Detect Duplicate Lead" did not move it to the admin account (…006825001);
   - Tag FB-FDI; Lead Channel "Advt"; Lead Source "Direct" (normal for testing-tool leads);
   - Product and Product Cat after ~2 minutes (subsidiary / not sure → FDI - Subsidiary Incorporation / FDI; branch → Branch Office Registration of Foreign Company / BO-LO-PO);
   - Description "<Q1>, <Q3>"; Select_Country (record what "Other" does); Meta_* fields;
   - timeline shows workflow "SIB-05 India Entry - booking email" sent; Sanjeev confirms the email arrived with the owner's name.
   Then the WhatsApp-button phone test (chat must reach one of the five handlers), and Sanjeev deletes the test leads.
2. **G11:** apply Sanjeev's answers to decisions A–E in the claims review, update the doc, and hand the brief to the designer. When images arrive, read them in Canva and review every on-image claim before G12. Try again to open Press Note 2 (2026) and S.O. 2174(E) / 3030(E) on dpiit.gov.in or egazette.gov.in; add S.O. 3030(E) to spec section 1 and the section 8 legal stop.
3. **G12** on Sanjeev's go: campaign "SIB-05 India Entry" switched off, three ad sets (spec section 3; 7 non-EU/UK countries), then the six ads; preview pack. **G13** Sanjeev publishes.
4. **SIB-04 daily:** Meta form leads by ad vs CRM by day; spend split form vs CTWA; valid rate and cost per valid by channel; speed-to-lead list by owner (blank or Establishing Contact = not worked). Do not propose a budget shift between the form and CTWA ad sets until the 8 untouched form leads have been worked. Remind Sanjeev of open items in the two 12 Oct logs. MGT-7 creative by 28 Oct; on 31 Oct propose pausing the ads quoting 30 Oct (C1, C5, LLP-C1); MCA circular watch.
5. **Raise when there is time:** privacy policy s.16 and s.4; the "15–21 Days" subsidiary page; Bookings service text.

## Hard Rules

- Never activate or publish a Meta campaign. Never move money, never top up, never enter passwords, never call ads_activate_entity. Any pause, budget or creative change needs Sanjeev's explicit approval, one variable at a time.
- Publishing website content needs Sanjeev's explicit OK on the exact text. Ad copy and on-image text need his OK on the exact text too.
- Show code, a diff or the exact text before saving any production function, template or workflow.
- Don't edit the 11 older LeadChain chains. Don't delete CRM records with the connector. Don't delete sib04_form_tidy unless Sanjeev asks.
- When editing a CRM record with the connector, pass `trigger: []` and skip assignment rules.
- SIB-05 ads never say "100% FDI allowed", "no approval needed", "set up in X days" or "no need to visit India". No LLP ad may quote ₹100 a day as the filing fee.
- If the browser permission check refuses a Setup page, hand the step to Sanjeev.

## Browser Notes

- The built-in browser is signed in to Facebook, Zoho CRM, SalesIQ and WordPress. For CRM Setup pages set the viewport to 1366×900 with resize_window and reset afterwards.
- SalesIQ settings load reliably only from /settings/home.
- CRM APIs from the page: X-CRM-ORG = window.crmZgid and X-ZCSRF-TOKEN = 'crmcsrfparam=' + the crmcsr cookie.
- Email template editor: paste merge fields in label form, `${Leads.Last Name}`.
- dpiit.gov.in returns an empty page to WebFetch; try the built-in browser, or egazette.gov.in by S.O. number.
- Canva relaunch creatives: "SIB Relaunch Oct 2026 – 1:1 working set" (DAHXTezZ4Nk); older pool "INDIA ENTRY" (DAHHddJfPOU).

## Output

End with a short report (done / open / who) and a new dated change log, then write the prompt for the session after.
