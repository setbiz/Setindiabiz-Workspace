# Change log: SIB-05 G3c and G10, SIB-04 first live days (12 Oct 2026, 13:20–13:55 IST)

Follows `Change_Log_2026-10-10_SIB-05-Form.md` (R95–R104, C77–C80). Spec: `Meta Ads/SIB-05_India_Entry_Build_Spec_2026-10-10.md` (v4). G10 text: `Meta Ads/SIB-05_G10_Email_Draft_2026-10-10.md`.

## Sanjeev's decisions (12 Oct, ~13:25)

| Question | His answer | Effect |
|---|---|---|
| G3c route for …508 WhatsApp | "A: General Inquery + rule" | C82–C84 |
| G10 template and workflow, exact text shown in chat | "Yes, save as shown" | C85–C87 |
| SIB-04 record fixes | "Fix source on 946586197" only | C81. 946567286 not reassigned; 946543271 left as is |

Routing type for the C84 rule was not asked. Claude set **Least loaded**, which the 10 Oct handoff named as closest to the CRM round robin. One click to change (Settings › Chat Routing › rule › Edit).

## Read-only checks

| # | Item | Finding | Method |
|---|---|---|---|
| R105 | SIB-04 delivery, 10–12 Oct (12 Oct to ~13:25) | Campaign 120246968311680449 ACTIVE. Spend ₹6,461.74 / ₹5,895.79 / ₹3,036.22. Form ad set (120246968737470449) ₹6,207.65, 20 Meta leads (7/9/4). CTWA ad set (120246968316940449) ₹9,186.10. | Meta connector, campaign and ad-set level, daily |
| R106 | SIB-04 CRM leads (Meta_Campaign "SIB-04 Annual Filings") | 45 leads: 18 form ("SIB-04 ACR Form v1") + 27 WhatsApp ("Advt - WhatsApp"). Valid Lead or Proposal Sent: form 3/18 (17%), WhatsApp 11/27 (41%); 3 Proposal Sent, all WhatsApp; 2 Lost (WhatsApp). Cost per valid: form ₹2,069, WhatsApp ₹835, all ₹1,100. Lead_Status blank on 15 (9 form, 6 WhatsApp). | COQL |
| R107 | Meta vs CRM form leads by ad (10–12 Oct) | LLP-C1 7/7, ACR-C2 4/4, ACR-C5 1/1, **ACR-C1 8 vs 6**: both missing leads are on ACR-C1 and fall on 10 Oct. The Leads deleted list shows two leads sent to the Recycle Bin on 10 Oct by Sanjeev's login: "Aniket Srivastava" (18:11:59) and "Hemang Tiwari" (19:41:42). Not confirmed that these are the two form leads. Also deleted 10–12 Oct: about 20 staff test records (Rishika Test, Mahima, Pavneet, Anish, employee names). | Meta connector, ad level; CRM `/Leads/deleted` from the page |
| R108 | Speed-to-lead at 13:25 (blank Lead_Status, 4+ hours old) | 12 leads: Pavneet Kaur 3 (form, Sun 21:01–23:13); Sudip Manna 2 (form, Sat 20:20 and 20:33, 41 h); Praveen Singh 2 (WhatsApp Sat 15:44, 46 h; form Sun 21:08); Sanjeev's admin account 2 (see R109); Priyam Tiwari 1 (WhatsApp Sun 18:00); Gaurav Pandey 1 (WhatsApp Sun 22:32); Mahima Sehrawat 1 (WhatsApp today 08:02). A further 14 sit at "Establishing Contact". First_Contact_Time is blank on all 45. | COQL; owner IDs resolved with getSingleUser |
| R109 | "Detect Duplicate Lead" moves duplicates to the admin account | 946543271 (Sun 23:15) and 946567286 (Mon 00:15): assigned to Pavneet by the SIB-04 rule, then moved to Sanjeev Kumar (…006825001) with Duplicate_Status Yes. 946543271 matches WhatsApp lead 946561225 (Amit Kumar 3, Establishing Contact). 946567286 matches old lead 1123581000721772108 and Contact 1123581000584769650, so it is a returning customer with no active owner. | getTimelines |
| R110 | Lead 946586197 (Hafeez) | Created by SalesIQ (Tiya - Annual Filings chat) at 20:58 on 10 Oct; form lead 946549221 merged into it on 11 Oct at 14:49 (crm_ui). The survivor kept Lead Source "Self - Web Chat" and Channel "Self", so it was out of the paid segment and the CAPI ValidLead rule. Tiya forwarded the chat twice and no operator answered (Desk tickets #1414789, #1414796). Anish called on 11 Oct 15:14: "call rejected, WhatsApp message dropped". | getTimelines |
| R111 | Lead 946517382 | Anish Singh changed Product to "Incorporation - OPC" at 12:32 on 12 Oct; note "wants to incorporate OPC, Uttar Pradesh". Correct reclassification: the OPC answer on the annual-filing form can bring incorporation enquiries. | getTimelines |
| R112 | Owners outside the original map | Sudip Manna (…057363001) is Head - Customer Support, role Sales - TL Roles; 946575232 was moved to him from Pavneet on 11 Oct 10:40 from Sanjeev's login (crm_ui). Praveen Singh (…005632013) is Sales - Gold Team. "Gupta" (…893487006) not resolved. | getSingleUser; getTimelines |
| R113 | SIB-04 assignment rule | "PPC - SIB-04 Annual Filings - LG-11" modified 11 Oct 14:14 by Sanjeev's login. Default still Pavneet Kaur. The user list was not read. | getAssignmentRules |
| R114 | MCA circular watch | No relaxation of additional fees for FY 2025-26 AOC-4/MGT-7 found. The latest found are GC 06/2025 (17 Oct 2025) and GC 08/2025 (30 Dec 2025), both for FY 2024-25 up to 31 Jan 2026. The "₹100 a day" company ads stay. | Web (taxmann, taxguru, mbgcorp) |
| R115 | SIB-05 form leads | 0 leads for "SIB-05 India Entry Form v1" (no ads, no tests yet). | COQL |
| R116 | Email template merge fields | Templates store `${!Leads.Last_Name}` / `${!Leads.Owner}`, but the editor rejects that syntax when pasted ("unsupported merge fields"). The label form `${Leads.Last Name}` / `${Leads.Lead Owner}` is accepted and saved as the `!` form. | Templates API; template editor |

## Changes

| # | Time (IST) | Change | Before | After | Evidence |
|---|---|---|---|---|---|
| C81 | 13:27:31 | Lead **1123581000946586197** (Hafeez): Lead_Source and Lead_Channel | "Self - Web Chat" / "Self" | **"Advt - Facebook" / "Advt"** | updateRecord with `trigger: []` and assignment rules skipped, so no workflow ran. COQL read-back: owner Anish Singh and status "Establishing Contact" unchanged. |
| C82 | ~13:30 | SalesIQ brand **India Entry Services** (61466000023310225) › Flow Controls › Departments responsible for chats | Customer Support + Sales - FDI | **Customer Support + Sales - FDI + Sales - General Inquery** | "Changes saved successfully" |
| C83 | ~13:31 | SalesIQ › WhatsApp › [phone redacted] › Associated department | Customer Support | **Sales - General Inquery** | "Updated successfully"; page shows the new department |
| C84 | 13:33 | SalesIQ › Chat routing › new rule **"FDI WhatsApp - India Entry Services to FDI team"** (id 61466000026794114) | No rules | Brand India Entry Services; audience Channels is WhatsApp; Route to Specific operators: **Foziya, Gaurav Pandey, Karishma, Rishika Singh, Shubendu** (5, read back before Save); routing type **Least loaded**; enabled | Overview page after Save; list shows 1 rule, toggle on, "Yet to be routed" |
| C85 | ~13:45 | CRM email template **"SIB-05 India Entry - Free consultation link"** (id **1123581000946398903**), folder **S - FDI**, Leads | None | Subject and body exactly as approved (G10 draft section 1); merge fields stored as `${!Leads.Last_Name}`, `${!Leads.Owner}` ×2 | Templates API read-back (name, folder, subject, merge fields, full text) |
| C86 | 13:49:10 | Email notification **"SIB-05 India Entry - booking email to lead"** (id **1123581000946398906**) | None | To `${!Leads.Email}`; template 1123581000946398903; From and Reply-to `${!Record.Owner.Email}`; not bulk | Email Notifications API read-back |
| C87 | 13:49:54 | Workflow rule **"SIB-05 India Entry - booking email"** (id **1123581000946398910**), Leads | None | Execute on **Create**; criteria `(Meta_Lead_Form = "SIB-05 India Entry Form v1" AND Email not empty) AND Email_Opt_Out = false`; instant action C86; no scheduled action; **active** | Workflow Rules API read-back |

For about two minutes between C83 and C84, …508 chats would have gone to all of Sales - General Inquery. The number has 0 WhatsApp users and no ad points to it yet.

While building C85, a first paste with the `!` syntax was flagged; the three fields were replaced with the label form before saving (R116). One "#" typed in the body to open the merge picker was removed before saving.

No Meta campaign, ad set or ad was created or changed. No money was moved. No CRM record was deleted. No LeadChain chain, assignment rule or function was edited.

## Open

| # | Item | Who |
|---|---|---|
| 1 | **G9 test leads** on form 4073050519663550 (Lead Ads Testing Tool): "Subsidiary (Indian company)" + United States; "Branch office" + Japan; "Not sure yet" + Other. Claude then checks owner (five handlers or Pavneet), Tag FB-FDI, Lead Channel, Lead Source, Product and Product Cat after ~2 min, Description, Select_Country ("Other"), Meta_* fields, and that the C87 email went out with the owner's name. Testing-tool leads get Lead Source "Direct" (normal). Also tap the thank-you WhatsApp button once on a phone and confirm the chat reaches one of the five handlers (C84). Sanjeev deletes the test leads afterwards. | Sanjeev runs, Claude checks |
| 2 | Tell **Pavneet Kaur** she is the default owner for SIB-04 and SIB-05 leads that arrive when no handler is online; she has 3 untouched form leads from Sunday night. | Sanjeev |
| 3 | **Sudip Manna**: 2 form leads untouched for 41 h (moved to him on 11 Oct 10:40). **Praveen Singh**: 2 untouched. | Sanjeev |
| 4 | **946567286** (returning customer) sits on your admin account with no active owner. You chose not to reassign it; someone still has to call. | Sanjeev |
| 5 | **Duplicate handling.** "Detect Duplicate Lead" parks every new duplicate on the admin account. For paid leads, consider keeping the duplicate with the assigned rep (or the original's owner) and only flagging it. Needs a code change shown before save. | Sanjeev decides, Claude drafts |
| 6 | **Merges.** When a form lead and a chat lead are merged, choose the form lead as master (or keep its Lead Source and Channel), or the lead drops out of the paid segment and CAPI (R110). | Sanjeev / ops |
| 7 | **2 missing ACR-C1 form leads (10 Oct).** Check the Recycle Bin entries "Aniket Srivastava" (10 Oct 18:11) and "Hemang Tiwari" (10 Oct 19:41); restore if they are SIB-04 form leads. | Sanjeev |
| 8 | Chat routing type: Least loaded set by Claude; switch to "Route one by one" or another if preferred. | Sanjeev |
| 9 | Job title → Designation ("Title") not on the Leads layout; unmapped. | Sanjeev |
| 10 | G11 creatives with claims review; G12 campaign (3 ad sets, 7 non-EU/UK countries) switched off; G13 publish. | Per spec |
| 11 | SIB-04: daily CRM vs Meta counts; speed-to-lead; MGT-7 creative by 28 Oct; on 31 Oct propose pausing the ads that quote 30 Oct (C1, C5, LLP-C1); MCA watch; website fixes. | Claude / Sanjeev |
| 12 | Raise when there is time: privacy policy s.16 ("once established"); s.4 "contractual necessity" vs Sec. 7 DPDP Act; the "Register Your Indian Subsidiary in 15–21 Days" page; Bookings service text written for Indian everyday services and staffed by support. | Sanjeev |
