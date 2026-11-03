# Change log: SIB-04 test lead 4 and Product Cat fix (10 Oct 2026, 10:40–11:08 IST)

Follows `Change_Log_2026-10-10_SIB-04-TestLead.md` (C69). Campaign "SIB-04 Annual Filings" 120246968311680449, form "SIB-04 ACR Form v1" 2635626386872789, chain "FB SIB-04 ACR v1". Paused by Sanjeev at 11:08.

## Read-only checks
| # | Item | Finding | Method |
|---|---|---|---|
| R59 | Old test leads | 1123581000946463005 and 1123581000946520006 **deleted** by Sanjeev (still present at 10:36, gone at 10:42). Sanjeev also confirmed the Reorder Rules move of "SIB-04 Form Tidy" ("done"). | COQL |
| R60 | **Test lead 4** | Lead **1123581000946520042** (L483302), created **10:41:21**, Social Lead ID 2256110258654052. **Owner: pass**: rule "PPC - SIB-04 Annual Filings - LG-11" assigned **Rishika Singh** (LG-11); "Detect Duplicate Lead" set Duplicate_Status **No** and left the owner alone. **Product Name: pass** ("ACR - Company Annual Return", set by Form Tidy). **Product Cat: fail**: "Pull Product, Report Category and Reporting Manager" wrote null over "Annual Filing" in the same second; Tidy's own write recorded only Product_Name, so Pull Product's null landed last. Opt-in fired; Lead Source "Direct"; Reporting Manager Suman Khowal. | COQL, getTimelines |
| R61 | Reorder had no effect | Both rules start functions that run side by side. Rule order sets which starts first, not which write finishes last. | R60 vs R58 |
| R62 | Product category of the two ACR products | "ACR - Company Annual Return" (1123581000000185017) and "LLP Annual Return (ACR)" (1123581000080093673) both map to **Annual Filing**. | COQL Products |
| R63 | **LeadChain cannot set Product Name** | In the chain editor, the Product Name row (a lookup) shows "Select a value" and offers only Facebook form fields; there is **no fixed-value option** (text fields show "Enter your text or Select a value"). The planned chain-row fallback is not possible. | Chain editor (built-in browser) |
| R64 | **Pencil editor gotcha** | Opening "FB SIB-04 ACR v1" with the pencil pre-fills a **Lead Source = "Meta Ads"** row that is not on the saved chain. Any Save from that editor must remove this row first. Editor exited **without saving**; chain view afterwards: Active, 13 rows, no Lead Source row, 4 leads synced. | Chain editor, chain view |
| R65 | Scheduled actions | Zoho workflow scheduled actions accept a **Minute(s)** unit relative to Rule Trigger Time (also Business hour, Hour, Business day, Day, Week, Year). | Zoho FAQ; rule editor |
| R66 | Self-heal confirmed | Sanjeev edited test lead 4 at **10:57** (Lead Status Lost, Why Disqualified "Wrong Info"). Pull Product re-ran: Product_Category "Annual Filing", Report_Cat "Compliance". | getRecord |
| R67 | **Lead Channel watch** | After that edit, test lead 4's **Lead_Channel reads "SEO"** (the chain sets "Advt"; test lead 1 showed Advt at creation). Likely derived from Lead Source "Direct" by an edit-time rule. Real leads should get Lead Source "Advt - Facebook/Instagram"; check Lead Channel on the first live lead. | getRecord |
| R68 | Setup access | This session's built-in browser opened Setup › Functions and Setup › Workflow Rules without a permission refusal (unlike C69). LeadChain runs in an iframe at `crm.zoho.com/crm/setindiabiz/settings/extensions/leadchain-extensions/leadchain?network=Facebook`; the iframe URL opened alone renders blank. | Built-in browser |

## Sanjeev's decisions
- ~10:45: "Chain row + Tidy edit" (fixed Product Name in the chain; Tidy switches LLP answers to the LLP product). Abandoned after R63.
- ~10:55: **"Delayed re-run"**: guard Product Cat in the function (only if blank) and add a scheduled action that runs the function again a few minutes after creation.

## Changes
| # | Time (IST) | Change | State | Evidence |
|---|---|---|---|---|
| C70 | ~11:00 | Function **`sib04_form_tidy`** (id 1123581000946541004) **v2**: Product_Category written **only if blank**; update sent only if there is something to change (else logs "nothing to change"). Description and Product Name logic unchanged. Commit message "v2: Product Cat only if blank, for scheduled re-run (Claude, 10 Oct)". Code copy: `Meta Ads/sib04_form_tidy.deluge.txt`. | Live | Saved, 0 errors, "Last modified … just now". Test run on test lead 4: **Success, 0.48 s, "nothing to change"** (correct: Product Cat already restored by the 10:57 edit, R66). |
| C71 | ~11:05 | Workflow rule **"SIB-04 Form Tidy"** (1123581000946541013): added **Scheduled Action "Execute 2 Minute(s) After Rule Trigger Time" → Function SIB-04 Form Tidy**. Instant action unchanged. | Live, **not yet exercised** | Rule saved; re-opened after reload: "This rule is active", scheduled action present. |

No Meta changes. No money moved. LeadChain chain not changed (editor exited unsaved). No other chain touched. No CRM records deleted by Claude.

## Open
1. **Sanjeev:** delete test lead 4 (**1123581000946520042**, L483302, owner Rishika Singh) in CRM, so the duplicate detector does not hand test lead 5 to her.
2. **Test lead 5** (Sanjeev runs the testing tool: Delete lead, then Create lead). Claude checks at once and again 3+ minutes later. Pass = owner an LG-11 user (or Pavneet Kaur if none online), Duplicate_Status No, owner not changed by "Detect Duplicate Lead"; Product_Name "ACR - Company Annual Return"; **Product_Category blank at creation, then "Annual Filing" about 2 minutes later**; timeline shows the scheduled SIB-04 Form Tidy run. Then Sanjeev deletes test lead 5.
3. **Funds** (₹6,000/day + 18% GST): Sanjeev. Not blocked by item 2. Claude never moves money.
4. **First live lead:** Lead Source "Advt - Facebook/Instagram", **Lead Channel "Advt"** (R67), six Meta_* fields, owner, Product Name (LLP answer → "LLP Annual Return (ACR)"), Product Cat "Annual Filing" within ~2 min, Description "<entity>, <years>" (first real check of the separator). Then daily CRM vs Meta lead counts; phone test of the form's WhatsApp completion button.
5. **Sanjeev:** tell Pavneet Kaur she receives SIB-04 form and WhatsApp leads that arrive while no LG-11 person is online.
6. Carried (unchanged): Messenger/Instagram buttons on live Form ads; flags (ACR-C5 CTWA AI label, "Chat on WhatsApp" pill, 9:16 safe zone, age-25 floor, video warning icon); MCA circular watch for FY 2025-26 AOC-4/MGT-7 additional-fee relaxation (none found as of 10 Oct; latest 2026 circular found is GC 04/2026 of 31 Aug extending CCFS-2026 to 15 Sep); if one appears, pause the company "₹100 a day" ads; MGT-7-only creative by 28 Oct; on 31 Oct pause ads quoting 30 Oct (C1, C5, LLP-C1); website fixes (LLP late-fee page; roc-filing CCFS text); WhatsApp template for form leads. Side note: Leads workflow "1 Lead Source" shows disabled (not touched).
