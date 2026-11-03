# SIB-04 read-only verification — 7 Oct 2026, 19:25–19:44 IST

Run from `SIB-04_Verify_and_Resume_Prompt_2026-10-07.md`. **No change was made anywhere** (Zoho CRM, SalesIQ, Zoho One, Meta). CRM and Meta were read through their connectors; SalesIQ and the CRM rule screen through Claude in Chrome on SKSMALLHP. Every editor opened was closed with Cancel / X, nothing saved.

## Results

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | Assignment rule "PPC - SIB-04 Annual Filings - LG-11" (1123581000945354238) | **OK** | API: rule present, default Sanjeev Kumar, modified 7 Oct 16:42:59 (same after this check). Entry editor (opened, Cancel): Product Cat IS Annual Filing **OR** Tag IS FB-ACR, pattern (1 or 2); Category › Users, round robin; users = Pragya Agrawal, Rishika Singh, Tarun Kumar, Mahima Sehrawat, Anish Singh, Amit Kumar 3, Priyam Tiwari, Gaurav Pandey, Suman Khowal, Praveen Singh (10, matched by email); **Online status ticked**, Shift timing not ticked. None met → Sanjeev Kumar. |
| 2 | TEST leads 1123581000945064083 and 1123581000945155075 | **NOT OK** (still present) | COQL: both exist — "TEST SIB-04 plug - delete" (owner Pragya Agrawal) and "TEST SIB-04 plug 2 - delete" (owner Tarun Kumar). |
| 3 | Products 1123581000000185017 and 1123581000080093673 | **OK** | "ACR - Company Annual Return" and "LLP Annual Return (ACR)" — both active, Product_Category Annual Filing. |
| 4 | Leads since 7 Oct with Tag FB-ACR or Lead_Source "Advt - WhatsApp" (also Meta_Campaign SIB-04* / Social - WhatsApp) | **OK — only the 2 TEST leads** | 1123581000945155075: owner Tarun Kumar, Product_Category Annual Filing, Reporting_Manager Suman Khowal. 1123581000945064083: owner Pragya Agrawal, Product_Category **Miscellaneous**, Reporting_Manager Suman Khowal (first test, before the productid fix). No real lead yet, so it cannot yet be shown that the LeadChain SIB-04 chain uses the rule (no SIB-04 Meta campaign exists — see 12). |
| 5 | Plug `sib_wa_lead` (61466000026793006) published; code = `sib_wa_lead.deluge.txt` | **OK** | Editor header "Published 07:06 PM", Publish button greyed (no pending edits). Editor code: 258 lines, 7,574 chars, SHA-256 identical to the project file (ignoring its trailing newline). Line 20 = `for each  k in keys` (two spaces). Editor closed with X, not saved. Plugs list: last updated 07:06 PM, never triggered. |
| 6 | Connections `sib_crm_cb` and `zohocrm1` | **OK** | Connections page: 6 connections, all green (Connected): zoho_bot1, zohocrm, zohocrm1, sib_siq, sib_crm, sib_crm_cb. Side note: `zoho_bot1` shows **"Expiring Soon"** (not used by `sib_wa_lead`). |
| 7 | 20 lead handlers enabled, role "Sales Agents" only | **OK** | Operators (35). All 20 are enabled and **Sales Agents** — the 4 wrong roles of 7 Oct (Tarun Supervisor; Jitendra, Pragya, Rishika Associate) have been fixed. |
| 8 | Department memberships per staff plan | **OK for Sales - CACS ACR; others by count only** | Sales - CACS ACR (29): full list read — all 15 planned members present, incl. all 10 SIB-04 owners (also Support Agents, Durgesh, Himanshu ×2, Sanjeev, Jitendra, Foziya, Karishma, Rama — wider, accepted). General Inquery 31, Licenses 30, IPR 29, CACS ACR 29 — same counts as the 7 Oct verification (Sales - FDI row was below the fold, not read); their member lists could not be re-read (the operator pop-up stopped loading). |
| 9 | Brand "Compliance & ACR" (61466000023310359) | **OK, with one observation** | Brands list: 2 departments = Customer Support, Sales - CACS ACR; last updated 07:07 PM. WhatsApp: +919266601455 on this brand, WABA "Setindiabiz - Salesiq", 1.5K WhatsApp users. **Balance 10 credits** (unchanged). Observation: the WhatsApp channel page shows **Associated department = Customer Support** only (a channel-level setting, separate from the brand's Flow Controls). |
| 10 | Zobot "Setindiabiz Compliance" on Compliance & ACR (draft) | **NOT OK — not imported** | Zobot list shows 2 bots only (Tiya ×2, both Setindiabiz Inquiries). The import has not been done. Builder checks (23 cards, A04/A05/A06/A07) not possible. |
| 11 | No duplicate `sib_wa_lead` | **OK** | Plugs (18); search "wa_lead" returns one plug. |
| 12 | No SIB-04 campaign active (account 152154124583473) | **OK** | Meta connector: 7 campaigns, all PAUSED (#IND6, #IND5, #IND4, #IND3, #IND2 LLP ACR, #IND 1, #IND 2 Website). Drafts: none. **No SIB-04 / CTWA campaign exists yet, in any state.** |
| 13 | Docs agree with findings | **Mostly — 4 gaps** | See "Doc updates needed" below. |

## What needs fixing

| # | Item | Proposed fix | Who |
|---|---|---|---|
| A | Bot not imported (check 10) | Zobot › Add › Via import; pick `C:\Users\sanje\Claude\SIB-04_Zobot_Import.zip`; brand Compliance & ACR; description "SIB-04 Annual Filings - WhatsApp [phone redacted]"; leave unpublished. Then Claude reviews the builder read-only. | **Sanjeev** (upload); Claude checks after |
| B | 2 TEST leads still in CRM (check 2) | Delete 1123581000945064083 and 1123581000945155075 (or tell Claude "go delete the 2 TEST leads"). | **Sanjeev** |
| C | WhatsApp channel department = Customer Support only (check 9) | No change now. In the phone test, confirm the bot's forward to a named operator and to Sales - CACS ACR actually reaches them. If it lands only in Customer Support, change Settings › WhatsApp › Compliance & ACR › Associated department (or rely on the bot forwards) — needs a go. | Claude tests; Sanjeev decides |
| D | LeadChain SIB-04 chain → rule (check 4) | Can't be confirmed until a SIB-04 form exists. When the chain is set up: rule "PPC - SIB-04 Annual Filings - LG-11", static Tag FB-ACR, Product Cat Annual Filing. | **Sanjeev** |
| E | Departments other than CACS ACR only verified by count (check 8) | Optional: re-read General Inquery / Licenses / IPR / FDI lists in the next session. Not on the SIB-04 critical path. | Claude |
| F | `zoho_bot1` connection "Expiring Soon" | Not used by SIB-04. Check which bot uses it (likely Tiya) and reconnect before it expires. | Sanjeev (authorisation) |

## Doc updates needed (check 13)
1. `SalesIQ_Staff_Plan_2026-10-07.md` › Role check: the 4 roles are now Sales Agents — the table is out of date.
2. `SIB-04_Zobot_Flow_2026-10-07.md` › Steps: steps 1 (publish plug) and 2 (add CACS ACR to brand) are done (19:06 / 19:07); step 3 (import) still open.
3. Change log: the "C4 (plug)" row says "saved, NOT published" — superseded by the 19:06 entry (no edit needed, history), but the WhatsApp channel's own department setting (Customer Support) is not mentioned anywhere.
4. Handoff step 8 (Meta DRAFT/PAUSED SIB-04 campaign) — not started; docs are consistent with that.

I have not edited any of these docs; the resume prompt carries them forward.
