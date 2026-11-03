# Change log: SIB-04 test leads, default owner, form tidy (10 Oct 2026, 09:25–10:40 IST)

Follows `Change_Log_2026-10-10_SIB-04-LeadChain.md` (C65). Campaign "SIB-04 Annual Filings" 120246968311680449, form "SIB-04 ACR Form v1" 2635626386872789, chain "FB SIB-04 ACR v1".

## Read-only checks
| # | Item | Finding | Method |
|---|---|---|---|
| R44 | Test lead 1 | Lead **1123581000946538001** (L483274), created 09:16:16 via crm_api, Social Lead ID 1649346473565668, Email test@meta.com. **Pass:** Tag FB-ACR, Lead_Channel Advt, Meta_Lead_Form, Social Lead ID, Email. **Fail:** Owner, Product Cat, Description (R53, R46, R47). Meta_* campaign/ad fields and Phone blank, as expected for a testing-tool lead. Since deleted by Sanjeev. | COQL, getRecord |
| R45 | Owner (first view) | Rule **"PPC - SIB-04 Annual Filings - LG-11"** fired at 09:16:16 but assigned **Sanjeev Kumar (admin, …006825001)**, the rule's **default assignee**, although Product Cat matched. First hypothesis (shift start 09:30) **disproved by R52; cause in R53**. | getTimelines, getAssignmentRules |
| R46 | Product Cat | LeadChain set "Annual Filing"; ~2 s later **"Pull Product, Report Category and Reporting Manager"** (workflow "2 Pull Product Info") set it to **null** because **Product_Name is blank**. That function rebuilds Product Cat from Product Name. On older chain leads the RM sets Product Name by hand (e.g. lead 1123581000940496275, Mahima Sehrawat, 24 Sep), so the gap never showed. The SalesIQ plug avoids it by passing productid 1123581000000185017. Fix attempt C67–C68; race in R58. | getTimelines |
| R47 | Description | Stored as `<test…entity><test…years>`: **no separator**. The ", " on the chain view is display only. A real lead would read "LLPNot sure". Fix: C67–C68 (not yet seen on a real lead). | getRecord |
| R48 | WhatsApp Opt In | Workflow **"SIB-04 Form Opt In"** (1123581000946537009), created by Sanjeev, **fired on all three test leads**: WhatsApp_Opt_In true, Opt_In_Time stamped. Form consent: required custom-disclaimer checkbox per build spec §5. | getTimelines |
| R49 | Lead Source | "Direct", set by "Auto Classify Lead Source from URL fields". Expected for a testing-tool lead (no Platform). Real chain leads carry Meta_Ad_Type fb/ig and got "Advt - Facebook" on 24 Sep. Verify on the first live lead. | getTimelines |
| R50 | Meta | `ads_get_errors` on campaign + both ad sets: **0 errors**. No funds yet. | Meta connector |
| R51 | MCA circular watch | **No FY 2025-26 AOC-4/MGT-7 additional-fee relaxation** found. 2026 circulars: GC 01/2026 (24 Feb, CCFS-2026), GC 02/2026 (19 Jun, DPT-3 to 31 Jul), **GC 03/2026 (8 Jul, CCFS-2026 to 31 Aug)**, **GC 04/2026 (31 Aug, CCFS-2026 to 15 Sep)**. No GC 05/2026 found. CCFS-2026 therefore appears to have closed on 15 Sep 2026: relevant to the open website fix (roc-filing CCFS text). Company "₹100 a day" ads stand. | Web search |
| R52 | Test lead 2 | Meta testing tool: leadgen 3432893276919158 sent 09:31:55, delivery to app 191062257579887 "Success". CRM lead **1123581000946463005** created **09:32:04 (9 s sync)**. Owner again **Sanjeev (default)** via the SIB-04 rule; Product Cat wiped again; opt-in fired; Duplicate_Status Yes against test lead 1. | COQL, getTimelines, screenshot |
| R53 | **Owner cause** | Not shift. The rule entry has **"Check availability: Online status" ticked** (Shift timing not ticked), per `Change_Log_2026-10-07_SIB-04-CRM.md` (C5) and `SIB-04_Verification_2026-10-07.md`. The round robin picks only LG-11 users online in CRM; none was online at 09:16 or 09:32 Saturday, so both leads went to the default. Applies to form leads and plug WhatsApp leads (same rule via lar_id). | Project logs + timelines |
| R54 | Opt-in rule trigger | Workflow list shows "SIB-04 Form Opt In" = **Create** only, so Opt In Time is not re-stamped on later edits. | Workflow Rules list (browser) |
| R55 | Side observation | Leads workflow rule **"1 Lead Source"** (Create or Edit, 9 actions) shows as **disabled**. Not touched; noted only. | Workflow Rules list |
| R56 | Test lead 3 | Lead **1123581000946520006**, created **10:32:27**, Social Lead ID 1767451427824747. **"SIB-04 Form Tidy" fired** and set Product_Name "ACR - Company Annual Return". Opt-in fired (10:32). Reporting_Manager Suman Khowal. | COQL, getTimelines |
| R57 | **Owner routing works** | The SIB-04 rule assigned **Pragya Agrawal** (LG-11, online at 10:32). One second later the function **"Detect Duplicate Lead"** set Duplicate_Status Yes (match: test lead 2, same test@meta.com) and **changed Owner Pragya Agrawal → Sanjeev Kumar**, the owner of the matching lead. So a duplicate is handed to the existing record's owner (inferred from this one case; function code not read). Test-only clash; delete earlier test leads before the next test. Pavneet default not exercised (an LG-11 user was online). | getTimelines |
| R58 | **Product Cat race** | At 10:32:28 "2 Pull Product Info" started, read the lead while Product_Name was still empty, and wrote Product_Category null **after** "SIB-04 Form Tidy" had set Product_Name (Tidy's history shows only Product_Name changing; Product Cat was still "Annual Filing" then). Both functions ran in the same second; the Tidy rule sits last in the Leads list. Product_Name is now present, so the next edit by an RM re-runs Pull Product and restores "Annual Filing": the gap lasts only until first edit. | getTimelines |

## Sanjeev's decisions (09:38)
- Default owner of the SIB-04 rule → **Pavneet Kaur** (option B: keep "Online status").
- "ok to function" → deploy `sib04_form_tidy` as drafted (LLP → "LLP Annual Return (ACR)").

## Changes
| # | Time (IST) | Change | State | Evidence |
|---|---|---|---|---|
| C66 | 09:42 | Rule **"PPC - SIB-04 Annual Filings - LG-11"** (1123581000945354238): **default user Sanjeev Kumar → Pavneet Kaur** (1123581000757738001, Support Team, "Sales - Executive Pre Sales"). Rule entry unchanged (Product Cat Annual Filing OR Tag FB-ACR → round robin over LG-11, Online status ticked). | Live | getAssignmentRules: default_assignee Pavneet Kaur, modified 2026-10-10 09:42:07 |
| C67 | 09:46–09:50 | New CRM function **`sib04_form_tidy`** (display "SIB-04 Form Tidy", Deluge, category automation), argument **leadId (int) = Leads › Lead Id**. Body = `Meta Ads/sib04_form_tidy.deluge.txt`. Saved, 0 errors. **Test-run** on test lead 1123581000946463005: getRecordById 200, updateRecord 200; result Product_Name "ACR - Company Annual Return", Product_Category "Annual Filing". | Live | Function editor console; COQL |
| C68 | 09:51 | New workflow rule **"SIB-04 Form Tidy"** (Leads; When: Record action **Create**; Condition: Meta Lead Form **is** "SIB-04 ACR Form v1"; Instant action: Function SIB-04 Form Tidy). Saved and active. **Not reordered**: sits last in the Leads list; drag in "Reorder Rules" did not register (mouse drag and scripted drag), reorder mode cancelled with no change. R58 shows the order matters. | Live | "SIB-04 Form Tidy Rule has been saved." |
| C69 | 09:53 | Test lead **1123581000946463005** edited via connector (no workflows triggered): Description → "LLPNot sure", Product_Name → empty, to test the separator path. The planned editor run was blocked (session permission check refused navigation to Setup › Functions). | Test data only | updateRecord SUCCESS 09:53:46 |

No Meta changes. No money moved. No LeadChain chain touched.

## Open
1. **Sanjeev: reorder** "SIB-04 Form Tidy" to the **top** of the Leads workflow list (Setup › Workflow Rules › filter Leads › Reorder Rules › drag it above "1 Lead Source" / "2 Pull Product Info" › Save). Claude's drag did not register.
2. **Sanjeev: delete test leads** 1123581000946463005 and 1123581000946520006 in CRM (and test lead 3 in the testing tool), so the duplicate detector does not reassign the next test lead.
3. **Test lead 4** after 1–2. Pass = owner an LG-11 user (or Pavneet if none online); Product_Category "Annual Filing" stays; Product_Name "ACR - Company Annual Return". If Product Cat is still blanked after the reorder, fall back to setting Product Name at creation: try a fixed "Product Name" row in the LeadChain chain (our chain only), then retest.
4. **Funds** (₹6,000/day + 18% GST): owner routing is now proven (R57). Product Cat is a data-quality gap that self-heals on first edit, so funds need not wait for item 3 if Sanjeev prefers. Claude never moves money.
5. First live lead check: Lead Source Advt - Facebook/Instagram, six Meta_* fields, owner, Product Name/Cat, Description "<entity>, <years>".
6. Tell Pavneet Kaur she now receives SIB-04 form and WhatsApp leads that arrive while no LG-11 person is online (nights, Sundays, early mornings).
