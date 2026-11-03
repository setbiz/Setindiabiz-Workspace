You are continuing two Setindiabiz Meta jobs:
- **SIB-04 Company Annual Filings** is live.
- **SIB-05 India Entry (FDI Services)** is being built.

Zoho CRM is crm.zoho.com (US DC). The Meta account is 152154124583473. Meta tool calls use client_model "claude-opus-5-5".

Read these project docs first:
- Meta Ads/Change_Log_2026-10-12_SIB-05-G3c-G10.md: R105–R116, C81–C87, open items.
- Meta Ads/SIB-05_India_Entry_Build_Spec_2026-10-10.md (v4): decisions D1–D20, go list G1–G13, section 4 form and LeadChain map, section 6 creatives.
- Meta Ads/SIB-04_Resume_Prompt_2026-10-10_ppcformtidy.md: SIB-04 steps 3–7 still apply.

## State at 12 Oct, 13:55 IST

**SIB-05, built:**
- Tag FB-FDI; assignment rule "PPC - SIB-05 India Entry - PG-02" (round robin over the five handlers, default Pavneet Kaur); PPC Form Tidy CONFIG block.
- Privacy policy s.18 EU/UK notice, live since 10 Oct 14:40.
- Instant Form "SIB-05 India Entry Form v1", ID 4073050519663550, Active, 0 leads.
- LeadChain chain "FB SIB-05 FDI v1": Active, Job title unmapped.
- **G3c done (C82–C84):** brand India Entry Services has Customer Support + Sales - FDI + Sales - General Inquery; the …508 WhatsApp channel is on Sales - General Inquery; chat-routing rule "FDI WhatsApp - India Entry Services to FDI team" (61466000026794114): Channels is WhatsApp → Foziya, Gaurav Pandey, Karishma, Rishika Singh, Shubendu; Least loaded; enabled.
- **G10 done (C85–C87):** template "SIB-05 India Entry - Free consultation link" (1123581000946398903, folder S - FDI); email notification 1123581000946398906 (To lead Email; From and Reply-to Record Owner's Email); workflow rule "SIB-05 India Entry - booking email" (1123581000946398910), Leads, on Create, `(Meta_Lead_Form = "SIB-05 India Entry Form v1" AND Email not empty) AND Email_Opt_Out = false`, active.

**SIB-05, not done:** G9 test leads; G11–G13.

**SIB-04 (10 Oct 13:35 – 12 Oct 13:25):** ₹15,394 spend; 45 CRM leads (18 form, 27 WhatsApp); valid 3/18 form vs 11/27 WhatsApp; 3 Proposal Sent (WhatsApp). Meta 20 form leads vs CRM 18; the gap is 2 on ACR-C1 on 10 Oct (possibly the Recycle Bin entries "Aniket Srivastava" and "Hemang Tiwari"). 12 leads had a blank status after 4+ hours (Pavneet 3, Sudip Manna 2, Praveen Singh 2, admin account 2, others 1 each). Lead 946586197's source was fixed to "Advt - Facebook" (C81).

## Next, in Order

1. **G9** when Sanjeev says the three test leads are in (Lead Ads Testing Tool, form 4073050519663550):
   - "Subsidiary (Indian company)" + United States; "Branch office" + Japan; "Not sure yet" + Other.
   - For each, COQL on `Meta_Lead_Form = 'SIB-05 India Entry Form v1'`, then getRecord and getTimelines. Check:
     - owner is one of the five handlers (Foziya Ansari 1123581000033869514, Gaurav Pandey 1123581000900792006, Karishma Singh 1123581000458244001, Rishika Singh 1123581000754062001, Shubendu Banerjee 1123581000037468001) or Pavneet Kaur 1123581000757738001, and that "Detect Duplicate Lead" did not move it to the admin account;
     - Tag FB-FDI; Lead Channel "Advt"; Lead Source "Direct" is normal for testing-tool leads;
     - Product and Product Cat after about 2 minutes (subsidiary/not sure → FDI - Subsidiary Incorporation / FDI; branch → Branch Office Registration of Foreign Company / BO-LO-PO);
     - Description "<Q1>, <Q3>"; Select_Country (record what "Other" does); Meta_* fields;
     - the timeline shows workflow "SIB-05 India Entry - booking email" sent the email; ask Sanjeev to confirm it arrived with the owner's name.
   - Ask Sanjeev to tap the thank-you WhatsApp button on a phone and confirm the chat reaches one of the five handlers.
   - Sanjeev deletes the test leads.
2. **G11:** draft the six creatives' copy from spec section 6 for the designer; run `product-legal:marketing-claims-review` on each; open the primary texts still pending (Press Note 2 (2026) on dpiit.gov.in, Sec. 149(3) on indiacode.nic.in, FEMA 395/2019-RB on rbi.org.in) and verify the FC-GPR 30-day line before S2 is approved.
3. **G12:** on Sanjeev's go, create campaign "SIB-05 India Entry" switched off with the three ad sets (spec section 3; 7 non-EU/UK countries), then the ads; preview pack. **G13** Sanjeev publishes.
4. **SIB-04 daily:** CRM vs Meta counts by ad; speed-to-lead (blank status or "Establishing Contact" = not worked); remind Sanjeev of open items 2–7 in the 12 Oct change log; MGT-7 creative by 28 Oct; on 31 Oct propose pausing the ads quoting 30 Oct (C1, C5, LLP-C1); MCA circular watch.
5. **Raise when there is time:** privacy policy s.16 and s.4; the "15–21 Days" subsidiary page; Bookings service text.

## Hard Rules

- Never activate or publish a Meta campaign. Never move money, never top up, never enter passwords, never call ads_activate_entity. Any pause, budget or creative change needs Sanjeev's explicit approval, one variable at a time.
- Publishing website content needs Sanjeev's explicit OK on the exact text.
- Show code, a diff or the exact text before saving any production function, template or workflow.
- Don't edit the 11 older LeadChain chains. Don't delete CRM records with the connector. Don't delete sib04_form_tidy unless Sanjeev asks.
- When editing a CRM record with the connector, pass `trigger: []` and skip assignment rules, or the "Lead Assignemnt - Edits" workflow can change the owner.
- SIB-05 ads never say "100% FDI allowed", "no approval needed", "set up in X days" or "no need to visit India". No LLP ad may quote ₹100 a day as the filing fee.
- If the browser permission check refuses a Setup page, hand the step to Sanjeev rather than working around it.

## Browser Notes

- The built-in browser is signed in to Facebook, Zoho CRM, SalesIQ (salesiq.zoho.com/wwwsetindiabizcom) and WordPress. The pane is narrow (~755 px): for CRM Setup pages set the tab viewport to 1366×900 with resize_window and reset it to "desktop" afterwards.
- SalesIQ settings load reliably only from /settings/home; click through from there.
- CRM APIs from the page: X-CRM-ORG = window.crmZgid and X-ZCSRF-TOKEN = 'crmcsrfparam=' + the crmcsr cookie. Useful read-backs: /crm/v8/settings/email_templates/{id}, /crm/v8/settings/automation/workflow_rules/{id}, /crm/v8/settings/automation/email_notifications/{id}, /crm/v8/Leads/deleted.
- Zoho lyte dropdown items open reliably with a ref click on the button, then `item.click()` from JavaScript on the visible lyte-drop-item.
- Email template editor: paste merge fields as `${Leads.Last Name}` / `${Leads.Lead Owner}` (label form); the `${!Leads.Last_Name}` form is rejected when pasted.

## Output

End with a short report (done / open / who) and a new dated change log, then write the prompt for the session after.
