# Prompt for the next session: SIB-04 rule order, test lead 4, funds, first live lead (written 10 Oct 2026 10:40 IST)

Paste everything below the line into a new session in the "Meta Ads - Optimisation" project.

---

You are continuing the Setindiabiz Meta relaunch for **SIB-04 Company Annual Filings**. Campaign 120246968311680449, both ad sets and all 8 ads are published and ACTIVE, 0 errors, ₹0 spent (no funds). LeadChain chain "FB SIB-04 ACR v1" (form 2635626386872789) is Active and delivers test leads to CRM in about 9 seconds.

## Read first
- `Meta Ads/Change_Log_2026-10-10_SIB-04-TestLead.md` (R44–R58, C66–C69).
- `Meta Ads/sib04_form_tidy.deluge.txt` (deployed).

## State on 10 Oct, 10:40
- Rule "PPC - SIB-04 Annual Filings - LG-11" (1123581000945354238): default user **Pavneet Kaur** (1123581000757738001); Online-status check kept.
- Function `sib04_form_tidy(int leadId)` + workflow "SIB-04 Form Tidy" (Leads, Create, Meta Lead Form is "SIB-04 ACR Form v1"): sets Description "<entity>, <years>", Product Name (LLP → "LLP Annual Return (ACR)" 1123581000080093673, else "ACR - Company Annual Return" 1123581000000185017) if blank, Product Cat "Annual Filing". It sits **last** in the Leads workflow list.
- **Test lead 3 (1123581000946520006, 10:32):** rule assigned **Pragya Agrawal** (routing works); "Detect Duplicate Lead" then moved it to Sanjeev because it matched test lead 2 (same test@meta.com). Tidy set Product Name, but "2 Pull Product Info" had read the lead first and wrote Product Cat back to null (race). Product Name is set, so the first RM edit restores "Annual Filing".

## Next, in order
1. Confirm Sanjeev has (a) moved "SIB-04 Form Tidy" to the top of the Leads workflow list (Reorder Rules) and (b) deleted test leads 1123581000946463005 and 1123581000946520006 in CRM. Claude's drag in Reorder Rules did not register; don't retry it, ask Sanjeev.
2. **Test lead 4** (Sanjeev: testing tool › Delete lead › Create lead). Check: `select id, Owner, Created_Time, Product_Name, Product_Category, Description, Lead_Source, WhatsApp_Opt_In, Duplicate_Status from Leads where Meta_Lead_Form = 'SIB-04 ACR Form v1' order by Created_Time desc`, then getTimelines. Pass = owner an LG-11 user (or Pavneet Kaur if none online) and not changed by "Detect Duplicate Lead"; Product_Category "Annual Filing" stays; Product_Name "ACR - Company Annual Return". If Product Cat is still blanked, fallback: add a fixed "Product Name" row to the LeadChain chain "FB SIB-04 ACR v1" (our chain only, via its pencil) so Product Name exists at creation; re-verify on the chain view, then test again. COQL Owner returns surname only; resolve IDs with the memory map (zoho-sales-owner-ids).
3. **Funds**: Sanjeev adds them (₹6,000/day + 18% GST). Owner routing is proven; the Product Cat gap self-heals on first edit, so funds need not wait for step 2. Claude never moves money.
4. **First live lead**: Lead Source Advt - Facebook/Instagram; six Meta_* fields; owner; Product Name/Cat; Description "<entity>, <years>" (first real check of the separator). Then daily CRM vs Meta lead counts; phone test of the form's WhatsApp completion button.
5. Remind Sanjeev to tell Pavneet Kaur she receives SIB-04 leads that arrive while no LG-11 person is online.
6. Carried: Messenger/Instagram buttons on live Form ads (Ads Manager or phone preview); flags (ACR-C5 CTWA AI label, "Chat on WhatsApp" pill, 9:16 safe zone, age-25 floor, video warning icon); **MCA circular watch** for FY 2025-26 AOC-4/MGT-7 additional-fee relaxation (none as of 10 Oct; latest 2026 circular found is GC 04/2026 of 31 Aug extending CCFS-2026 to 15 Sep). If one appears, pause the company "₹100 a day" ads. **MGT-7-only creative by 28 Oct**; on 31 Oct pause ads quoting 30 Oct (C1, C5, LLP-C1); website fixes (LLP late-fee page; roc-filing CCFS text, as CCFS-2026 appears to have closed 15 Sep); WhatsApp template for form leads. Side note: Leads workflow "1 Lead Source" shows disabled (not touched).

## Hard rules
- Never activate or publish a Meta campaign, never move money, never top up, never enter passwords, never call ads_activate_entity.
- Don't edit the 11 older LeadChain chains. Don't delete CRM records with the connector.
- No LLP ad may quote ₹100 a day as the filing fee; only as the Sec. 34(5) penalty with "can be" and the caps.
- Zoho CRM is crm.zoho.com (US DC). Meta tool calls: client_model "claude-opus-5-5".
- If the browser permission check refuses a Setup page, hand the step to Sanjeev rather than working around it.

## Output
Short report (done / open / who), a new dated change log, and the prompt for the session after.
