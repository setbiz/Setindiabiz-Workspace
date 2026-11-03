# Change log: one form-tidy function for every Meta lead form (10 Oct 2026, 12:19–12:53 IST)

Follows `Change_Log_2026-10-10_SIB-04-TestLead5.md` (R69–R77). Campaign "SIB-04 Annual Filings" 120246968311680449, form "SIB-04 ACR Form v1" 2635626386872789. Code copy: `Meta Ads/ppc_form_tidy.deluge.txt`.

## Sanjeev's decisions
- 12:19: Product Cat is refreshed on every manual edit by the assignment-side function, so a separate Report Cat fill is not needed, but there is no harm provided the value is pulled from the Products module. With more campaigns coming, **one function should handle Product Name and Product Cat for all of them**.
- 12:24: "ok" to deploy the generic function and repoint the existing rule, with the condition **Meta Lead Form is not empty**.

## Read-only checks
| # | Item | Finding | Method |
|---|---|---|---|
| R78 | Products module | Product 1123581000000185017 "ACR - Company Annual Return" carries Product_Category "Annual Filing" and Report_Cat "Compliance", so both can be read from the product record. | getRecord |
| R79 | Gap on older forms | Of the Meta form leads since 1 Jan 2026, 64 across ten older forms (Incorporation V2 23, Trademark V2 14, CCFS2026 V2 10, DPIIT V2 6, the two C1 forms 4, CCFS 3, DPIIT 2, LLP ACR 1, Virtual CFO V2 1) still have a blank Product Name. The race is not SIB-04-only. None of these forms is in CONFIG yet. | COQL group by Meta_Lead_Form, Product_Name |
| R80 | WhatsApp leads | Plug `sib_wa_lead` passes `productid` and sets Product_Name when it creates the lead, so "2 Pull Product Info" fills Product Cat itself. CTWA leads need no tidy function. | Project file `sib_wa_lead.deluge.txt` |
| R81 | Test lead 5 | Deleted by Sanjeev before 12:24 (COQL returned no SIB-04 lead). | COQL |
| R82 | Skip path | IDE run of `ppc_form_tidy` on Trademark V2 lead 1123581000940494254: Success, 0.34 s, one GET (200), log "form 'Trademark V2' not in CONFIG, nothing done". No write. | Function IDE console |
| R83 | **Test lead 6: PASS** | Lead **1123581000946429088**, created **12:48:44**. Owner **Mahima Sehrawat** (LG-11) by rule "PPC - SIB-04 Annual Filings - LG-11"; Duplicate_Status No. **12:48:45** instant run of PPC Form Tidy set Product_Name "ACR - Company Annual Return" and **Report_Cat "Compliance"**. In the same second "Pull Product" changed Product_Category from "Annual Filing" to null (known race) and did not touch Report_Cat. **12:50:23** scheduled run set **Product_Category "Annual Filing"**. Both category values came from the Products record. At 12:52 COQL showed Product Cat "Annual Filing", Report Cat "Compliance", owner unchanged. | COQL, getTimelines |
| R84 | Timing | The "2 minutes after" scheduled run fired 1 min 39 s after creation. It still lands well after "Pull Product" (1 s after creation). | getTimelines |
| R85 | Rule editor behaviour | Changing a rule's criteria resets that rule's usage-report counts (Zoho warning; only today's test runs were lost). A scheduled-action group takes one function only; removing its function left the empty 2-minute group in place, so the new function was added to the same group. | Rule editor |

## Changes
| # | Time (IST) | Change | State | Evidence |
|---|---|---|---|---|
| C72 | ~12:30 | New CRM function **"PPC Form Tidy"** (API `ppc_form_tidy`, Deluge record id **1123581000946601707**, category automation, argument `int leadId`). CONFIG holds one block: "SIB-04 ACR Form v1" with default product "ACR - Company Annual Return", entity options OPC / Private Limited / LLP, and LLP mapped to "LLP Annual Return (ACR)". For a listed form it adds the Description comma, sets Product Name if blank, and copies Product Cat and Report Cat from the Products record if blank. Updates fire no workflow. | Live | Saved, 0 errors; IDE run R82; test lead 6 R83 |
| C73 | ~12:35–12:40 | Workflow rule **1123581000946541013** edited: name "SIB-04 Form Tidy" → **"PPC Form Tidy"**; description rewritten; condition "Meta Lead Form is SIB-04 ACR Form v1" → **"Meta Lead Form is not empty"**; instant action and the 2-minute scheduled action both switched from SIB-04 Form Tidy to **PPC Form Tidy** with leadId = Leads › Lead Id. Trigger unchanged (Create). | Live | Rule reloaded after save: active, condition, both actions and new name shown; test lead 6 timeline names rule "PPC Form Tidy" |

`sib04_form_tidy` (1123581000946541004) is no longer attached to any rule. It was not deleted. No Meta change, no money moved, no LeadChain chain opened, no CRM record edited or deleted by Claude.

## Open
1. **Sanjeev:** delete test lead 6 (**1123581000946429088**, owner Mahima Sehrawat, created 12:48:44).
2. **Funds** (₹6,000/day + 18% GST): Sanjeev. Claude never moves money.
3. **First live lead** (Claude checks): Lead Source "Advt - Facebook" or "Advt - Instagram" (R77); Lead Channel "Advt"; every Meta_* field filled; owner an LG-11 user, or Pavneet Kaur if none was online; Product Name, with an LLP answer giving "LLP Annual Return (ACR)"; **Report Cat "Compliance" at creation and Product Cat "Annual Filing" within about 2 minutes** (R83); Description "<entity>, <years>" (first real check of the separator, which the testing tool cannot exercise); Lead Status blank until the RM works it (R76). Then daily CRM vs Meta lead counts, and a phone test of the form's WhatsApp completion button.
4. **Sanjeev:** tell Pavneet Kaur she receives SIB-04 form and WhatsApp leads that arrive while no LG-11 person is online.
5. **Each new campaign form:** add one CONFIG block to `ppc_form_tidy` (form name exactly as LeadChain writes Meta_Lead_Form, default product id, first-question options, optional answer → product id) when the form is built, then test with the testing tool. The ten older forms in R79 get a block only if their campaigns are relaunched.
6. **Sanjeev, optional:** delete the unattached `sib04_form_tidy` when convenient. Claude has left it in place.
7. Carried (unchanged): Messenger/Instagram buttons on live Form ads; flags (ACR-C5 CTWA AI label, "Chat on WhatsApp" pill, 9:16 safe zone, age-25 floor, video warning icon); MCA circular watch for any FY 2025-26 AOC-4/MGT-7 additional-fee relaxation (none found as of 10 Oct; latest 2026 circular found is GC 04/2026 of 31 Aug extending CCFS-2026 to 15 Sep); if one appears, propose pausing the company "₹100 a day" ads; MGT-7-only creative by 28 Oct; on 31 Oct propose pausing the ads quoting 30 Oct (C1, C5, LLP-C1); website fixes (LLP late-fee page; roc-filing CCFS text); WhatsApp template for form leads. Side note: Leads workflow "1 Lead Source" shows disabled (not touched).
