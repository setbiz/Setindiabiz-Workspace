# Prompt for a fresh session — SIB-04 verification, then a resume prompt (7 Oct 2026, 19:21 IST)

Paste everything below the line into a new session in the "Meta Ads - Optimisation" project.

---

You are continuing the Setindiabiz Meta relaunch for **SIB-04 Company Annual Filings** only. This session is a **read-only health check** of everything built on 7 Oct 2026. At the end you must write me the prompt for the session after this one.

## Read first (project docs)
- `Meta Ads/SIB-04_Session_Handoff_2026-10-07.md` (rules and background)
- `Meta Ads/Change_Log_2026-10-07_SIB-04-CRM.md` (every change made, with times)
- `Meta Ads/SIB-04_Zobot_Flow_2026-10-07.md` (bot design and go-live steps)
- `Meta Ads/SalesIQ_Staff_Plan_2026-10-07.md` (20 lead handlers, departments, verification)
- `Meta Ads/sib_wa_lead.deluge.txt` (the plug code as it should be in SalesIQ)

## Hard rules for this session
- **Read only.** Make no change in Zoho CRM, SalesIQ, Zoho One or Meta. If something is wrong, report it and propose the fix; do not fix it.
- Never enter passwords. Sanjeev signs in himself. Never move money or make payments (that includes WhatsApp credit top-ups).
- Use Claude in Chrome on Sanjeev's laptop "sksmallhp" (open a new tab). SalesIQ blocks page-text reading, so use screenshots and javascript_tool for reading lists.
- No file downloads without asking first. Team Sheet: read only the "Lead Handler Group" tab, never other tabs.
- Do not change roles, app access or plug connections. Do not move plug calls to `sib_crm_cb`.

## Checklist (report each as OK / NOT OK / CAN'T CHECK, with evidence)
**Zoho CRM (use the Zoho CRM connector)**
1. Assignment rule "PPC - SIB-04 Annual Filings - LG-11" (id 1123581000945354238): entry criteria Product Category = Annual Filing OR Tag = FB-ACR; round robin over Pragya Agrawal, Rishika Singh, Tarun Kumar, Mahima Sehrawat, Anish Singh, Amit Kumar 3, Priyam Tiwari, Gaurav Pandey, Suman Khowal, Praveen Singh; online status on; default Sanjeev Kumar.
2. Test leads 1123581000945064083 and 1123581000945155075: still present or deleted (Sanjeev said he would delete them).
3. Products exist: "ACR - Company Annual Return" 1123581000000185017 and "LLP Annual Return (ACR)" 1123581000080093673.
4. Any Leads created since 7 Oct with Tag FB-ACR or Lead_Source "Advt - WhatsApp": list them (owner, Product_Category, Reporting_Manager). This shows whether the LeadChain SIB-04 chain now uses the rule (Sanjeev's step).

**SalesIQ (portal wwwsetindiabizcom, Chrome)**
5. Plug `sib_wa_lead` (61466000026793006): Published (was published 7 Oct 19:06). Code in the editor matches `sib_wa_lead.deluge.txt` (line 20 reads `for each  k in keys` with two spaces). Close the editor without saving.
6. Connections `sib_crm_cb` and `zohocrm1` are still connected (plug works only with both).
7. Operators: all 20 lead handlers enabled; every one has role "Sales Agents" only. On 7 Oct, Tarun Kumar (Supervisor) and Jitendra Singh, Pragya Agrawal, Rishika Singh (Associate) were wrong; Sanjeev said he would change them.
8. Departments: each person is in the departments the staff plan lists (wider membership is accepted).
9. Brand "Compliance & ACR" (61466000023310359): Flow Controls › Departments responsible for chats = Customer Support + Sales - CACS ACR. WhatsApp settings: +919266601455 is on this brand. Note the WhatsApp credit balance (was 10).
10. Zobot: is there a bot "Setindiabiz Compliance" (description "SIB-04 Annual Filings - WhatsApp [phone redacted]") on Compliance & ACR? It should be a DRAFT, not published. If it isn't there, Sanjeev hasn't finished the import (file is at C:\Users\sanje\Claude\SIB-04_Zobot_Import.zip). If it is there, open the builder (no saving) and check: 23 cards; the 3 "A04 CRM lead" cards are attached to `sib_wa_lead` with the inputs from the flow doc; "A05 Route to CRM owner" has 10 owner rules + the Contact rule; the 10 "A06 Forward to <name>" cards (still pointing at Sales - CACS ACR or already switched to the operator?); A07 forwards go to Sales - CACS ACR and Customer Support.
11. Plugs list: no duplicate `sib_wa_lead`.

**Meta (Meta Ads connector, account 152154124583473)**
12. No SIB-04 campaign is active. List any SIB-04 / CTWA draft or paused campaigns.

**Project docs**
13. The change log, flow doc and staff plan agree with what you found.

## Output
1. Send me a short verification report: a table of the 13 checks, then a list of what needs fixing, each with the proposed fix and who does it (me or you). Save it to the project as `Meta Ads/SIB-04_Verification_<date>.md` and add one line to the change log.
2. Then write the **prompt for the next session** and save it as `Meta Ads/SIB-04_Resume_Prompt_<date>.md`. Base it on what you found, and keep the same hard rules. Remaining work, in order (drop whatever is already done):
   a. Finish the bot import if missing (Sanjeev uploads the zip; the Chrome extension can't upload files).
   b. In the builder: re-attach `sib_wa_lead` on the 3 plug cards if needed; switch the 10 "A06" cards to their operators (Pragya, Rishika, Tarun, Mahima, Anish, Amit Kumar 3, Priyam, Gaurav, Suman, Praveen); fallbacks unchanged.
   c. Review the bot with Sanjeev in preview.
   d. Phone test on [phone redacted] with a test number that isn't a real client, then check the CRM lead (owner, Product_Category "Annual Filing", Tag FB-ACR, Reporting_Manager) and the routing.
   e. Publish the bot only on Sanjeev's explicit go.
   f. Next items from the handoff: WhatsApp template for form leads from [phone redacted] (needs credits — Sanjeev tops up); Chat_Attended_By; the Meta DRAFT/PAUSED SIB-04 campaign (CTWA vs Instant Form) — every Meta change needs Sanjeev's go; nothing goes live without an explicit go.
   g. Open items: where 1-minute no-pickup re-routing lives; daily watchdog edits; optional backfill of ~745 Accounts; delete duplicate function `stamp_account_firsttouch1` (needs go).
   h. Sanjeev's own steps if still open: LeadChain SIB-04 chain → rule "PPC - SIB-04 Annual Filings - LG-11" with static Tag FB-ACR and Product Cat Annual Filing; delete the 2 TEST leads; fix the 4 SalesIQ roles.
