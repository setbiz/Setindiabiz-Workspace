# Prompt for the next session: SIB-04 test lead, opt-in workflow, funds (written 10 Oct 2026 ~09:10 IST, after C65)

Paste everything below the line into a new session in the "Meta Ads - Optimisation" project.

---

You are continuing the Setindiabiz Meta relaunch for **SIB-04 Company Annual Filings**. G1–G11 are done: campaign 120246968311680449, both ad sets and all 8 ads are **published and ACTIVE**, no draft, no errors, ₹0 spent (no funds yet). The LeadChain chain **"FB SIB-04 ACR v1"** is **saved, Active and verified** (C65, 10 Oct ~09:04) with 14 rows; 0 leads synced so far.

## Read first (project docs)
- `Meta Ads/Change_Log_2026-10-10_SIB-04-LeadChain.md`: R38–R43, C63–C65 (full chain config), LeadChain behaviour, open items.
- `Meta Ads/SIB-04_Ads_Build_Spec_2026-10-09.md` (v2) for background.

## Chain as saved (verify on the chain view if in doubt — it lists every row)
Email←Email; Last Name←Full name; Social Lead ID←Lead Id; Phone←Phone number; Description←"What type of entity is it?", "Which years are pending?" (joined with ", "); Meta Campaign←Campaign Name; Meta Ad Set←Adset Name; Meta Lead Form←Form Name; Meta Ad Name←Advert Name; Meta Ad ID←Advert Id; Meta Ad Type←Platform; Product Cat = Annual Filing; Lead Channel = Advt. **No Lead Source row** (the CRM function "Auto Classify Lead Source from URL fields - Leads" sets Advt - Facebook/Instagram). Step 1: FB account Sanjeev Kumar › ad account 152154124583473 › Page 627814417091714 › form 2635626386872789 → Leads, layout Standard, Tag FB-ACR, rule "PPC - SIB-04 Annual Filings - LG-11", Update or Add Leads off.

## Work, in order (each change needs Sanjeev's go naming it)
1. **Test lead before funds.** Sanjeev runs Meta's Lead Ads Testing Tool on form 2635626386872789 (name "TEST Claude ignore"). Within ~10 min run COQL: `select id, Last_Name, Owner, Lead_Source, Lead_Channel, Product_Category, Tag, Description, Meta_Campaign, Meta_Ad_Set, Meta_Lead_Form, Meta_Ad_Name, Meta_Ad_ID, Meta_Ad_Type, leadchain0__Social_Lead_ID, Created_Time from Leads where Meta_Lead_Form = 'SIB-04 ACR Form v1'`. Pass = Owner in LG-11 (check the timeline shows rule "PPC - SIB-04 Annual Filings - LG-11"), Lead_Source "Advt - Facebook/Instagram", Lead_Channel Advt, Product Cat Annual Filing, Tag FB-ACR, Description "<entity>, <years>". Test-tool leads may carry no campaign/ad fields — that's expected. Sanjeev deletes the test lead himself (never delete via connector). If it fails, fix via the chain's pencil (our chain only) and re-verify on the view page.
2. **WhatsApp Opt In (proposal, needs go):** LeadChain can't set a fixed true. Proposed CRM workflow on Lead create, condition Meta_Lead_Form = "SIB-04 ACR Form v1" → WhatsApp_Opt_In = true (+ Opt_In_Time via a small function). Consent box on the form is required; scope is contact about this enquiry only — not for broadcasts.
3. **Funds:** Sanjeev adds them (₹6,000/day + 18% GST) only after step 1 passes. Claude never moves money.
4. After launch: daily CRM vs Meta lead counts (`onsite_conversion_lead_grouped` vs COQL count); phone test of the form's WhatsApp button (tap at once and after ~10 min) to see whether the chat reaches the LeadChain owner or creates a second lead.
5. Carried: Messenger/Instagram follow-up buttons on live Form ads (connector can't show; check in Ads Manager/phone preview); flags (ACR-C5 CTWA AI label, "Chat on WhatsApp" pill on Form creatives, 9:16 safe zone, age-25 floor, video warning icon); **MCA circular watch** for FY 2025-26 AOC-4/MGT-7 additional-fee relaxation (none as of 10 Oct; last year's came 17 Oct) — if one appears, pause the company "₹100 a day" ads; **MGT-7-only creative by 28 Oct**; on 31 Oct pause ads quoting 30 Oct (C1, C5, LLP-C1); website fixes (LLP late-fee page, roc-filing CCFS text); WhatsApp template for form leads. Sanjeev's optional idea: entity type into Account Name — not applied (becomes the Account name on conversion); raise only if he asks.

## LeadChain know-how
- Chains are form-scoped; a form with no chain never reaches CRM.
- The LeadChain screens are a cross-origin iframe: use screenshots + coordinates; zoom 1:1 to hit the small × on mapped pieces. Console errors are readable with read_console_messages.
- A chain is stored as a Draft as soon as you click "Proceed to Field Mapping"; reopen the draft rather than creating a duplicate.
- One row = form answers + text pieces, but a text label next to two answers triggers "Field limit reached"; two answers alone are joined with ", ".
- The second "Description" in the field list is the Product Matrix subform — never map it (a map-then-clear of it broke a draft's Save).
- CRM field metadata is reachable from the CRM tab via `fetch('/crm/v2.2/settings/fields?module=Leads', {headers:{'X-ZCSRF-TOKEN':'crmcsrfparam='+<crmcsr cookie>, 'X-CRM-ORG':'setindiabiz'}})` (read-only).

## Hard rules
- Never activate or publish a Meta campaign yourself, never move money, never top up credits, never enter passwords. Never call ads_activate_entity.
- If the session permission check blocks a click, leave the screen ready and hand it to Sanjeev; tell him not to click Save while you're still editing.
- Don't edit the 11 older LeadChain chains. Don't delete CRM records with the connector.
- No LLP ad may quote ₹100 a day as the filing fee; only as the Sec. 34(5) penalty with "can be" and the caps.
- Zoho CRM is crm.zoho.com (US DC); COQL Owner returns surname only. Meta tool calls: client_model "claude-opus-5-5".

## Output
End with a short report (done / open / who), log every change in a new dated change log, and write the prompt for the session after.
