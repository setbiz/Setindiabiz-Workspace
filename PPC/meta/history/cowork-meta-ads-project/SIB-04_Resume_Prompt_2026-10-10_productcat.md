You are continuing the Setindiabiz Meta relaunch for SIB-04 Company Annual Filings. Campaign 120246968311680449, both ad sets and all 8 ads are published and ACTIVE, 0 errors, ₹0 spent (no funds). LeadChain chain "FB SIB-04 ACR v1" (form 2635626386872789) is Active (13 rows) and delivers test leads to CRM in about 9 seconds.

Read first (project docs):
- Meta Ads/Change_Log_2026-10-10_SIB-04-ProductCat.md (R59–R68, C70–C71)
- Meta Ads/sib04_form_tidy.deluge.txt (v2, deployed)

State when paused (10 Oct, 11:08):
- Owner routing proven twice: rule "PPC - SIB-04 Annual Filings - LG-11" (1123581000945354238) assigned Pragya Agrawal (test 3) and Rishika Singh (test 4); default user Pavneet Kaur (1123581000757738001) when no LG-11 user is online; Online-status check kept.
- Product Cat race: "2 Pull Product Info" blanks Product Cat at creation because Product Name is empty when it reads the lead. Rule reorder did not help. LeadChain cannot set the Product Name lookup (form answers only, no fixed value).
- Fix deployed but NOT yet tested: function sib04_form_tidy v2 (id 1123581000946541004) writes Product Cat "Annual Filing" only if blank; workflow rule "SIB-04 Form Tidy" (1123581000946541013, Leads, Create, Meta Lead Form is "SIB-04 ACR Form v1") runs it instantly AND as a Scheduled Action 2 minutes after Rule Trigger Time.
- Test lead 4 (1123581000946520042, L483302, owner Rishika Singh, Lost) still in CRM unless Sanjeev has deleted it.

Next, in order:
1. Ask Sanjeev to confirm test lead 4 is deleted (check with COQL; don't delete it yourself).
2. Test lead 5 (Sanjeev runs the testing tool: Delete lead, then Create lead). COQL at once and again 3+ minutes later: select id, Owner, Created_Time, Product_Name, Product_Category, Description, Lead_Source, Lead_Channel, WhatsApp_Opt_In, Duplicate_Status from Leads where Meta_Lead_Form = 'SIB-04 ACR Form v1' order by Created_Time desc — then getTimelines. Pass = owner an LG-11 user (or Pavneet Kaur if none online), Duplicate_Status No and owner not changed by "Detect Duplicate Lead"; Product_Name "ACR - Company Annual Return"; Product_Category blank at creation and "Annual Filing" about 2 minutes later, with the scheduled SIB-04 Form Tidy run in the timeline. If it stays blank, check the rule's scheduled action and the function's Logs/Failures tab before changing anything. COQL Owner returns surname only; resolve IDs with the memory map (zoho-sales-owner-ids). Then Sanjeev deletes test lead 5.
3. Funds: Sanjeev adds them (₹6,000/day + 18% GST). Not blocked by step 2. Claude never moves money.
4. First live lead: Lead Source "Advt - Facebook/Instagram"; Lead Channel "Advt" (test lead 4 showed "SEO" after an edit while Lead Source was "Direct"); six Meta_* fields; owner; Product Name (LLP answer → "LLP Annual Return (ACR)"); Product Cat "Annual Filing" within ~2 min; Description "<entity>, <years>" (first real check of the separator). Then daily CRM vs Meta lead counts; phone test of the form's WhatsApp completion button.
5. Remind Sanjeev to tell Pavneet Kaur she receives SIB-04 leads that arrive while no LG-11 person is online.
6. Carried: Messenger/Instagram buttons on live Form ads; flags (ACR-C5 CTWA AI label, "Chat on WhatsApp" pill, 9:16 safe zone, age-25 floor, video warning icon); MCA circular watch for FY 2025-26 AOC-4/MGT-7 additional-fee relaxation (none as of 10 Oct; latest 2026 circular found is GC 04/2026 of 31 Aug extending CCFS-2026 to 15 Sep) — if one appears, pause the company "₹100 a day" ads; MGT-7-only creative by 28 Oct; on 31 Oct pause ads quoting 30 Oct (C1, C5, LLP-C1); website fixes (LLP late-fee page; roc-filing CCFS text); WhatsApp template for form leads. Side note: Leads workflow "1 Lead Source" shows disabled (not touched).

Browser notes: LeadChain lives in an iframe at crm.zoho.com/crm/setindiabiz/settings/extensions/leadchain-extensions/leadchain?network=Facebook (the iframe URL alone renders blank). The chain's pencil editor pre-fills a Lead Source = "Meta Ads" row that is not on the saved chain — remove it before any Save, or exit without saving. The function IDE is CodeMirror 5 (document.querySelector('.CodeMirror').CodeMirror).

Hard rules:
- Never activate or publish a Meta campaign, never move money, never top up, never enter passwords, never call ads_activate_entity.
- Don't edit the 11 older LeadChain chains. Don't delete CRM records with the connector.
- No LLP ad may quote ₹100 a day as the filing fee; only as the Sec. 34(5) penalty with "can be" and the caps.
- Zoho CRM is crm.zoho.com (US DC). Meta tool calls: client_model "claude-opus-5-5".
- If the browser permission check refuses a Setup page, hand the step to Sanjeev rather than working around it.

Output: short report (done / open / who), a new dated change log, and the prompt for the session after.
