You are continuing the Setindiabiz Meta relaunch for SIB-04 Company Annual Filings. Campaign 120246968311680449, both ad sets and all 8 ads are published and ACTIVE, 0 errors, ₹0 spent until Sanjeev adds funds. LeadChain chain "FB SIB-04 ACR v1" (form 2635626386872789) is Active (13 rows) and delivers leads to CRM in about 9 seconds.

Read first (project docs):
- Meta Ads/Change_Log_2026-10-10_SIB-04-TestLead5.md (R69–R77; no changes)
- Meta Ads/Change_Log_2026-10-10_SIB-04-ProductCat.md (C70–C71)
- Meta Ads/sib04_form_tidy.deluge.txt (v2, deployed)

State at 10 Oct, 12:14:
- CRM routing for SIB-04 form leads is proven end to end. Test lead 5 (1123581000946400031, created 12:09:40): owner Tarun Kumar (LG-11) from rule "PPC - SIB-04 Annual Filings - LG-11" (1123581000945354238); Duplicate_Status No, owner untouched; Product Name "ACR - Company Annual Return"; Product Cat blanked by "2 Pull Product Info" at 12:09:42 and restored to "Annual Filing" by the scheduled SIB-04 Form Tidy run at 12:11:54. The Product Cat fix works; no further change needed.
- Normal at creation, not faults: Report_Cat null (filled as "Compliance" on the first RM edit) and Lead_Status null (set by the RM). Test leads show Lead_Source "Direct" because the testing tool sends no URL fields; live leads should get "Advt - Facebook" or "Advt - Instagram" from "Auto Classify Lead Source from URL fields - Leads".
- Default owner when no LG-11 user is online: Pavneet Kaur (1123581000757738001). Not yet exercised.

Next, in order:
1. Confirm test lead 5 is deleted: COQL `select id from Leads where Meta_Lead_Form = 'SIB-04 ACR Form v1'`. If it is still there, ask Sanjeev to delete it; don't delete it yourself.
2. Funds: read the campaign with the Meta connector (effective_status, amount_spent, impressions, lead; date_preset today and maximum). If spend is still nil, remind Sanjeev (₹6,000/day + 18% GST). Claude never moves money.
3. First live lead (as soon as one exists): COQL `select id, Owner, Created_Time, Lead_Source, Lead_Channel, Product_Name, Product_Category, Report_Cat, Description, Duplicate_Status, Lead_Status, Tag, WhatsApp_Opt_In from Leads where Meta_Lead_Form = 'SIB-04 ACR Form v1' order by Created_Time desc`, then getRecord for every Meta_* field, then getTimelines. Pass = Lead Source "Advt - Facebook" or "Advt - Instagram" ("Direct" on a live lead is a fault: it also keeps the lead out of the "Meta CAPI - ValidLead" rule); Lead Channel "Advt"; all Meta_* fields filled; owner an LG-11 user or Pavneet Kaur; Duplicate_Status set and owner unchanged by "Detect Duplicate Lead"; Product Name matches the entity answer (LLP → "LLP Annual Return (ACR)", otherwise "ACR - Company Annual Return"); Product Cat "Annual Filing" within about 2 minutes; Description "<entity>, <years>" with the comma separator (first real check). COQL Owner returns the surname only; resolve IDs with the memory map (zoho-sales-owner-ids).
4. From the first live day: CRM vs Meta lead counts for the SIB-04 form, daily. Speed-to-lead for SIB-04 counts Lead_Status null (and "Establishing Contact") as not yet worked. Phone test of the form's WhatsApp completion button (Sanjeev, on a phone).
5. Remind Sanjeev to tell Pavneet Kaur she receives SIB-04 leads that arrive while no LG-11 person is online.
6. Offer, don't build: Tidy v3 could also write Report_Cat "Compliance" only if blank. Build only if Sanjeev says yes.
7. Carried: Messenger/Instagram buttons on live Form ads; flags (ACR-C5 CTWA AI label, "Chat on WhatsApp" pill, 9:16 safe zone, age-25 floor, video warning icon); MCA circular watch for any FY 2025-26 AOC-4/MGT-7 additional-fee relaxation (none as of 10 Oct; latest 2026 circular found is GC 04/2026 of 31 Aug extending CCFS-2026 to 15 Sep): if one appears, propose pausing the company "₹100 a day" ads; MGT-7-only creative by 28 Oct; on 31 Oct propose pausing the ads quoting 30 Oct (C1, C5, LLP-C1); website fixes (LLP late-fee page; roc-filing CCFS text); WhatsApp template for form leads. Side note: Leads workflow "1 Lead Source" shows disabled (not touched).

Browser notes: the built-in browser is not signed in to Facebook, so the Lead Ads Testing Tool (developers.facebook.com/tools/lead-ads-testing) needs Sanjeev to sign in, or he can use his own Chrome. LeadChain lives in an iframe at crm.zoho.com/crm/setindiabiz/settings/extensions/leadchain-extensions/leadchain?network=Facebook (the iframe URL alone renders blank). The chain's pencil editor pre-fills a Lead Source = "Meta Ads" row that is not on the saved chain: remove it before any Save, or exit without saving. The function IDE is CodeMirror 5 (document.querySelector('.CodeMirror').CodeMirror).

Hard rules:
- Never activate or publish a Meta campaign, never move money, never top up, never enter passwords, never call ads_activate_entity. Any pause, budget or creative change needs Sanjeev's explicit approval, one variable at a time.
- Don't edit the 11 older LeadChain chains. Don't delete CRM records with the connector.
- No LLP ad may quote ₹100 a day as the filing fee; only as the Sec. 34(5) penalty with "can be" and the caps.
- Zoho CRM is crm.zoho.com (US DC). Meta tool calls: client_model "claude-opus-5-5".
- If the browser permission check refuses a Setup page, hand the step to Sanjeev rather than working around it.

Output: short report (done / open / who), a new dated change log, and the prompt for the session after.
