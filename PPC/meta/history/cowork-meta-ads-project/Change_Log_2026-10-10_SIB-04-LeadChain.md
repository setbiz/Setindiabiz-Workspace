# Change log: SIB-04 publish check and LeadChain chain (10 Oct 2026, 07:50–09:10 IST)

Follows `Change_Log_2026-10-09_SIB-04-late.md` (C62). Account 152154124583473, campaign "SIB-04 Annual Filings" 120246968311680449.

## Read-only checks
| # | Item | Finding | Method |
|---|---|---|---|
| R38 | Publish state | Both ad sets (A CTWA 120246968316940449, B Form 120246968737470449) and all 8 ads **ACTIVE (live)**. Ads Manager draft for the campaign is **empty**. `ads_get_errors` on campaign + both ad sets: **0 errors**. Spend ₹0 (no funds). Sanjeev finished the publish after the late log; the CTWA "Select a Page" error is gone. | Meta connector, live + draft read |
| R39 | MCA additional-fee relaxation, FY 2025-26 AOC-4/MGT-7 | **None found** as of 10 Oct. Latest 2026 circular seen: GC 02/2026 (19 Jun 2026, DPT-3 fee waiver to 31 Jul 2026). Last year's annual-filing waiver was GC 06/2025 (17 Oct 2025), extended by GC 08/2025 to 31 Jan 2026. Company "₹100 a day" ads stand. Re-check daily until ~20 Oct. | Web search |
| R40 | CRM prerequisites | Tag **FB-ACR** exists (id 1123581000740044520). Product_Category value **"Annual Filing"** in use (2,180 leads in 2026). Assignment rule **"PPC - SIB-04 Annual Filings - LG-11"** (1123581000945354238) exists. | Zoho CRM connector |
| R41 | How existing chains set Lead Source | Lead 1123581000940496275 (Incorporation V2, 24 Sep) timeline: created via crm_api with **Lead_Source null**; 1 s later the function **"Auto Classify Lead Source from URL fields - Leads"** (workflow "Auto-set Lead Source from URL") set **"Advt - Facebook"**. | getTimelines |
| R42 | LeadChain behaviour found while mapping | (a) A row accepts text pieces + form answers, but **a text label next to two answers triggers "Field limit reached"**; two answers with no text works, and LeadChain joins them with **", "** (view shows "What type …, Which years…"). (b) LeadChain lists **two "Description" rows**: the first is Leads.Description (the only Description on Leads); the second is in the **Product Matrix subform** — never map it. (c) True/false fields (WhatsApp Opt In) have **no fixed-value option**. (d) New chains pre-fill Lead Source = "Meta Ads" (excluded value) and Full Name = Full name. (e) The chain is stored as a **Draft as soon as you click "Proceed to Field Mapping"**. (f) The chain **view page lists every saved row, including fixed values** — use it to verify. (g) A draft whose subform row was mapped then cleared crashed on Save (LeadAjax.js `restv2Ajax` called with undefined, 21×, nothing sent). | LeadChain wizard, console |
| R43 | Live Form ads: Messenger/Instagram follow-up buttons | **Not checkable via connector**. Still open; check in Ads Manager or a phone preview. | Meta connector |

## Sanjeev's decisions this block
- Years answer → "entity type and years should be entered into description. try only fields without any text input in description"
- WhatsApp Opt In → "Fixed 'true'" (not possible in LeadChain; proposed CRM workflow instead, awaiting go)
- Repeat leads → new lead each time ("Update or Add Leads" off)
- Save → "Yes, save and set Active"
- "you can also use Account Name for Entity Type" → **not applied** (Account Name becomes the Account name on conversion; existing chains leave it blank). Offered.

## Changes
| # | Time (IST) | Change | State | Evidence |
|---|---|---|---|---|
| C63 | 07:55–08:25 | First build of chain **"FB SIB-04 ACR v1"** in the wizard. | Claude's Save click blocked by the permission check; Sanjeev's Save at 08:30 **crashed in LeadChain's script** (R42g). Draft discarded (exit confirmed) at ~08:40. | Console log, screenshots |
| C64 | ~08:45 | Same chain (already stored as Draft at 07:55 with the step-1 settings) was **saved Active with only 4 rows** (Email, Last Name←Full name, Social Lead ID←Lead Id, **Lead Source = "Meta Ads"**) — a Save landed while Claude was mid-rebuild. No leads possible (no funds). | Corrected by C65 | Chain view screenshot |
| C65 | 08:50–09:04 | Edited "FB SIB-04 ACR v1" (pencil): removed Lead Source "Meta Ads"; added Phone←Phone number; **Description←[What type of entity is it?], [Which years are pending?]**; Meta Campaign←Campaign Name; Meta Ad Set←Adset Name; Meta Lead Form←Form Name; Meta Ad Name←Advert Name; Meta Ad ID←Advert Id; Meta Ad Type←Platform; **Product Cat = Annual Filing**; **Lead Channel = Advt**. Subform Description untouched. **Sanjeev clicked Save and Publish (~09:04): "You have successfully updated a chain."** | **Active, verified** on the chain view: 14 rows exactly as listed, no Lead Source row. Step-1 settings (unchanged since 07:55 draft): FB account Sanjeev Kumar › ad account SETINDIABIZ 152154124583473 › Page 627814417091714 › form SIB-04 ACR Form v1 2635626386872789 → Leads, layout Standard, **Tag FB-ACR**, **rule PPC - SIB-04 Annual Filings - LG-11**, Update or Add Leads off. Email notifications off. 0 leads synced. | Chain view screenshots |

No Meta changes. No money moved. No other LeadChain chain touched (12 chains: the 11 old ones + this).

## Open / next
1. **Test lead before funds** (Sanjeev: Meta Lead Ads Testing Tool on form 2635626386872789, name "TEST Claude ignore"). Then COQL: Owner in LG-11, Lead_Source "Advt - Facebook/Instagram", Lead_Channel Advt, Product_Category Annual Filing, Tag FB-ACR, Description "<entity>, <years>", six Meta_* fields, leadchain0__Social_Lead_ID. Sanjeev deletes the test lead.
2. Proposed (needs go): CRM workflow on Lead create, condition Meta_Lead_Form = "SIB-04 ACR Form v1" → WhatsApp_Opt_In = true (+ Opt_In_Time). Consent covers contact about this enquiry only.
3. Then Sanjeev adds funds (₹6,000/day + 18% GST).
4. Carried: Messenger/Instagram buttons on live Form ads (R43); flags (C5 CTWA AI label, "Chat on WhatsApp" pill, 9:16 safe zone, age-25 floor, video warning icon); MGT-7-only creative by 28 Oct; pause the 30-Oct-date ads on 31 Oct; MCA circular watch.
