You are continuing two Setindiabiz Meta jobs:
- **SIB-04 Company Annual Filings** is live.
- **SIB-05 India Entry (FDI Services)** is being built.

Zoho CRM is crm.zoho.com (US DC). The Meta account is 152154124583473. Meta tool calls use client_model "claude-opus-5-5".

Read these project docs first:
- Meta Ads/Change_Log_2026-10-10_SIB-05-Form.md: R95–R104, C77–C80, open items.
- Meta Ads/SIB-05_India_Entry_Build_Spec_2026-10-10.md (v4): decisions D1–D20, go list G1–G13, section 4 form and LeadChain map, section 5 CRM and SalesIQ.
- Meta Ads/SIB-05_G10_Email_Draft_2026-10-10.md: the email template and workflow waiting for approval.
- Meta Ads/Change_Log_2026-10-10_SIB-05-CRM.md: R86–R94, C74–C76.
- Meta Ads/SIB-04_Resume_Prompt_2026-10-10_ppcformtidy.md: SIB-04 steps 3–7 still apply.

## State at 10 Oct, 15:15 IST

**SIB-05, built:**
- Tag FB-FDI.
- Assignment rule "PPC - SIB-05 India Entry - PG-02": round robin over the five handlers, default Pavneet Kaur.
- PPC Form Tidy CONFIG block.
- Privacy policy s.18 EU/UK notice, live since 14:40:21.
- Instant Form "SIB-05 India Entry Form v1", ID 4073050519663550, Active.
- LeadChain chain "FB SIB-05 FDI v1": Active since 14:42, 0 leads, Job title unmapped.
- SalesIQ brand India Entry Services departments are Customer Support + Sales - FDI.

**SIB-05, not built:**
- **G3c WhatsApp routing.** The …508 chats still go to Customer Support. A chat-routing rule's operator picker offers only the 9 Customer Support members, so the rule was cancelled unsaved. Sanjeev must choose:
  - **A:** add Sales - General Inquery (Public; it has all five handlers and Pavneet) to the brand, set the …508 channel to it, then save the rule "FDI WhatsApp - India Entry Services to FDI team" (Brand India Entry Services; Channels is WhatsApp; Specific operators = the five handlers).
  - **B:** a new Public department "India Entry - WhatsApp" with the five handlers and Pavneet, linked only to this brand and set on the channel.
  - **C:** leave it as it is.
- **G10.** The template and workflow draft waits for Sanjeev's OK. It uses the "Free Consultation" link https://setindiabiz.zohobookings.com/3882293000006990272, which is staffed by support.
- **G9.** Test leads have not been run.
- **G11–G13.** Not started.

**SIB-04:**
- Campaign 120246968311680449 is ACTIVE.
- The first live lead is 1123581000946520260 (L483411, 14:28:28):
  - all checks passed; owner Priyam Tiwari;
  - Lead_Status "Establishing Contact" at 14:51:45, 23 minutes after creation;
  - First_Contact_Time blank.

## Next, in Order

1. **G3c, on Sanjeev's choice:**
   - **Option A:** in SalesIQ, Settings › Brands › India Entry Services › Flow Controls, add Sales - General Inquery. Then Settings › WhatsApp, set …508 Change Department to Sales - General Inquery. Then Settings › Chat Routing › Add, build the rule above with routing type as Sanjeev picks (Least loaded is the closest to the CRM round robin). Save, and confirm the five names in the picker before saving.
   - **Option B:** create the department, add it to the brand, then set the channel.
   - Record before and after. If the permission check refuses a page, hand the step to Sanjeev.
2. **G10, on Sanjeev's OK of the exact text:**
   - In CRM Setup › Templates › Email, create "SIB-05 India Entry - Free consultation link" in folder S - FDI.
   - Then Setup › Workflow Rules: Leads, on Create; condition Meta_Lead_Form = "SIB-05 India Entry Form v1" AND Email not empty AND Email Opt Out = false.
   - The action is an email notification to the lead, From and Reply-to = Record Owner.
3. **G9:** Sanjeev runs three leads in the Lead Ads Testing Tool on form 4073050519663550:
   - "Subsidiary (Indian company)" + United States;
   - "Branch office" + Japan;
   - "Not sure yet" + Other.

   For each, check:
   - the owner is one of the five handlers, or Pavneet;
   - Tag FB-FDI; Lead Channel "Advt"; Lead Source "Advt - Facebook" or "Advt - Instagram";
   - Product and Product Cat after about 2 minutes (branch → BO-LO-PO);
   - Description "<Q1>, <Q3>"; Select_Country (and what "Other" does); Meta_* fields;
   - the G10 email arrives with the owner's name filled in.

   Sanjeev deletes the test leads afterwards.
4. **G11–G13:** creatives with the marketing-claims review; the campaign with 3 ad sets switched off on the 7 non-EU/UK countries; Sanjeev publishes.
5. **SIB-04:**
   - daily CRM vs Meta counts;
   - speed-to-lead on each live lead;
   - remind Sanjeev to tell Pavneet Kaur she is the default owner for SIB-04 and SIB-05;
   - MGT-7 creative by 28 Oct; on 31 Oct, propose pausing the ads that quote 30 Oct (C1, C5, LLP-C1);
   - MCA circular watch; website fixes.
6. **Raise with Sanjeev when there is time:**
   - privacy policy s.16 says the Data Protection Board will act "once established", although it has been in force since 13 Nov 2025;
   - s.4 lists "contractual necessity" as a DPDP legitimate use, which Sec. 7 of the DPDP Act does not contain;
   - a page titled "Register Your Indian Subsidiary in 15–21 Days" makes a timeline claim;
   - the Bookings service text is written for Indian everyday services.

## Hard Rules

- Never activate or publish a Meta campaign. Never move money, never top up, never enter passwords, and never call ads_activate_entity. Any pause, budget or creative change needs Sanjeev's explicit approval, one variable at a time.
- Publishing website content needs Sanjeev's explicit OK on the exact text.
- Show code, a diff or the exact text before saving any production function, template or workflow.
- Don't edit the 11 older LeadChain chains. Don't delete CRM records with the connector. Don't delete sib04_form_tidy unless Sanjeev asks.
- SIB-05 ads never say "100% FDI allowed", "no approval needed", "set up in X days" or "no need to visit India". No LLP ad may quote ₹100 a day as the filing fee.
- If the browser permission check refuses a Setup page, hand the step to Sanjeev rather than working around it.

## Browser Notes

- The built-in browser is signed in to Facebook, Zoho CRM, SalesIQ (salesiq.zoho.com/wwwsetindiabizcom) and WordPress.
- SalesIQ settings pages load reliably only from the Settings home menu (/settings/home). Direct URLs such as /settings/departments/ can hang on a spinner.
- CRM APIs from the page: send X-CRM-ORG = window.crmZgid and X-ZCSRF-TOKEN = 'crmcsrfparam=' + the crmcsr cookie.
- After a WordPress page update, purge the WP Rocket cache for the post before reading it back.

## Output

End with a short report (done / open / who) and a new dated change log, then write the prompt for the session after.
