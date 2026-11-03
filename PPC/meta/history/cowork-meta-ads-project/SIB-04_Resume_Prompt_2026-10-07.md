# Prompt for the next session — SIB-04 bot builder, test (updated 8 Oct 2026, 15:45 IST — see item f "Owner-miss fallback — CURRENT")

Paste everything below the line into a new session in the "Meta Ads - Optimisation" project.

---

You are continuing the Setindiabiz Meta relaunch for **SIB-04 Company Annual Filings** only. State at 7 Oct 20:25: CRM rule, products, operator roles and the Compliance & ACR brand are in order (read-only check 19:25–19:44). **The bot is imported** as **"Tiya for Compliance"** (Zobot id 61466000026786012), DRAFT, on Compliance & ACR, 23 cards. The 2 TEST leads are still in CRM and no SIB-04 Meta campaign exists.

## Read first (project docs)
- `Meta Ads/Change_Log_2026-10-07_SIB-04-CRM.md` — read the bottom entries (19:44 onward) first; append every change
- `Meta Ads/SIB-04_Verification_2026-10-07.md` (13-point check)
- `Meta Ads/SIB-04_Session_Handoff_2026-10-07.md` (rules and background)
- `Meta Ads/SIB-04_Zobot_Flow_2026-10-07.md` (bot design; its steps 1–3 are done)
- `Meta Ads/SalesIQ_Staff_Plan_2026-10-07.md` (20 lead handlers; its role table is out of date — all 20 are Sales Agents now)
- `Meta Ads/sib_wa_lead.deluge.txt` (plug code; both plugs below match it exactly)

## Facts from the import (7 Oct ~20:00)
- The import created a **copy of the plug: `sib_wa_lead_1791383468657`** (id 61466000026786016, published 08:01 PM, identical code). **Decision 20:21 (Sanjeev): keep the copy.** The 3 "A04 CRM lead" cards use it, with all inputs and the 6 outputs (wa_*) correctly mapped. Do not re-point them: switching a card's plug wipes all its mappings.
- The import also created 2 **unconnected** connections, `sib_crm_cb1` and `zohocrm11` (Connections 6 → 8). The copy's code still calls `sib_crm_cb` and `zohocrm1`.
- A05 has the 10 owner rules + `wa_matched == contact`. The 10 "A06 Forward to <name>" cards point at Sales - CACS ACR, "Transfer to all available operators"; each has a "Transfer to selected operators" option.
- Bot settings were copied from Tiya: **"Bot works on: During business hours, when all the operators are offline…"**, hand-off Off. SIB-04 needs the bot on every chat.
- On 7 Oct this session's permission check blocked Claude from editing the bot builder (Modify Shared Resources) and earlier from browser access once. Expect builder edits may have to be done by Sanjeev, with Claude giving exact values and checking read-only afterwards.

## Hard rules
- **Every change needs Sanjeev's explicit go**, one change at a time, before/after screenshot, logged in the change log. Read-only work needs no go.
- Never enter passwords. Sanjeev signs in himself. Never move money or make payments (that includes WhatsApp credit top-ups).
- Use Claude in Chrome on Sanjeev's laptop **"SKSMALLHP"** (two Chromes are connected and the names can reset — if unsure, use the Connect prompt and let Sanjeev pick). Open a new tab. SalesIQ blocks `document.body.innerText`: use screenshots, `find`, and javascript_tool on leaf elements. Keep JS loops short. The bottom-left of SalesIQ pages has the Cliq "Chats" bar — don't click there by mistake.
- No file downloads without asking first. Team Sheet: read only the "Lead Handler Group" tab, never other tabs.
- Do not change roles, app access or plug connections. Do not move plug calls to `sib_crm_cb`.
- Nothing goes live without an explicit go. Ad claims must stay defensible (s.403 Companies Act 2013 + Companies (Registration Offices and Fees) Rules 2014; s.137(1); s.92(4); LLP Rules r.24(8)) — re-check MCA fee rules before any ad copy is published.

## Work, in order
a. ~~Dry run on the plug copy~~ **PASSED 7 Oct 20:30** (phone [phone redacted], dryrun yes → matched lead 1123581000940464311, owner aditya.bisht@; no write). Both connections work from the copy.
b. **Tidy-up (approved 20:30; Sanjeev clicks the deletions himself — check whether done):** delete the ORIGINAL plug `sib_wa_lead` (61466000026793006, now unused) and the unconnected connections `sib_crm_cb1`, `zohocrm11`. Check first that nothing else uses them.
c. ~~Bot settings~~ **No change needed (checked 20:31):** all 4 working-hour boxes are ticked; the overview text was truncated.
d. ~~A06 cards~~ **DONE 20:32–20:40:** all 10 set to "Transfer to selected operators" with the named person (department Sales - CACS ACR). Fallbacks unchanged.
d2. **Rename to "Tiya - Annual Filings" (Sanjeev 20:32)** — the Bot Profile name change did not persist on the draft (still "Tiya for Compliance"). Set it at publish time (Bot Profile step before Publish) and confirm in the Zobot list.
e. ~~Review in preview~~ done. **8 Oct: AGM question removed for all entities (V2 published 12:58);** bot asks two questions (entity, year). Bot departments = Customer Support + Sales - CACS ACR (8 Oct 12:28; the earlier Sales-only setting stopped the bot from seeing any WhatsApp chat). Bot to be renamed "Tiya - Annual Filings" (Sanjeev 20:32) — see d2.
f. **Phone test** on [phone redacted] from a test number that isn't a real client. Check the CRM lead: owner from the LG-11 pool, Product_Category "Annual Filing", Tag FB-ACR, Reporting_Manager, Lead_Source Advt - WhatsApp, Meta_Ad_Code ACR. **Watch the routing:** the WhatsApp channel's own "Associated department" is **Customer Support** (Settings › WhatsApp › Compliance & ACR). Confirm the forward reaches the named owner and, as fallback, Sales - CACS ACR. If not, propose the fix and wait for a go.
   **8 Oct 13:00 test result:** SalesIQ's native CRM integration created the lead first (Self - Web Chat, owner Pavneet), so the plug only added a note. **Fix A (Sanjeev 13:05): plug v2 published 13:10** — it claims a matched Lead that is Self - Web Chat, has no Meta_Ad_Code, an ad code is present and was created within 1 h: sets Advt - WhatsApp / product / tag fields and re-runs rule 1123581000945354238 via `lar_id` on update. Dry run passed. **Live test 13:14 PASSED** (chat #61314): lead 1123581000945723027 claimed — Advt - WhatsApp, ACR, SIB-04, product ACR, Annual Filing, Tag FB-ACR, owner Pavneet → **Mahima Sehrawat** (rule re-ran), Reporting_Manager Suman Khowal; bot forwarded the chat to Mahima. Open: A04 (Pvt Ltd) `answers` hard-codes "Entity: Private Limited" even for OPC — proposed "Entity: %q_entity% | Year: %q_fy_co%" (needs go); Lead_Assigned_on / Lead_Status blank on claimed leads (check against form leads).
   **Owner-miss fallback — CURRENT (8 Oct 15:45): CRM function bridge, built, NOT live yet.** Route: SalesIQ webhook workflow "SIB-04 bot transfer - 1 min fallback" (61466000026786113; Compliance & ACR; conversation.transfer.initiated → Flow webhook) → Zoho Flow "SIB-04 chat fallback - 1 min to Customer Support" (Webhook → Delay 1 min → `sib04ChatFallback` v3, project file `sib04ChatFallback.deluge.txt`, key redacted) → POST to CRM standalone function `sib04_siq_transfer` (REST API key; project file `sib04_siq_transfer.crm.deluge.txt`; CRM connection `sib_siq_transfer` with SalesIQ.conversations.READ + UPDATE, Connected) → if no human picked the chat, transfer to Customer Support (61466000018349043). Auth checked with dummy id (6045 Invalid Conversation Id = scope OK). **To go live (Sanjeev — Claude's toggle was blocked):** Flow ON (Apply changes if asked); SalesIQ workflow 61466000026786113 Enable; optionally Disable 61466000026786132. Then phone test with the owner ignoring the chat; read Flow › History (output "status") and the chat (should show Customer Support).
   *(Superseded 15:16)* SalesIQ Deluge workflow "SIB-04 owner miss - to Customer Support" (61466000026786132; events conversation.missed + conversation.transfer.rejected) — **never fires** for WhatsApp bot hand-offs (test #61315: Last Triggered "-", no logs).
   *(History)* **1-minute fallback (Sanjeev 13:18–13:33; 45 s not possible — Flow delays are whole minutes):** LIVE 8 Oct 14:08–14:48. SalesIQ data workflow "SIB-04 bot transfer - 1 min fallback" (61466000026786113; Compliance & ACR; conversation.transfer.initiated → webhook) → Zoho Flow "SIB-04 chat fallback - 1 min to Customer Support" (Webhook → Delay 1 min → function `sib04ChatFallback`, project file `sib04ChatFallback.deluge.txt`, connection `sib_siq_conv`) → if no human picked the chat, transfer to Customer Support (dept 61466000018349043). **Unproven:** `sib_siq_conv` has no SalesIQ.conversations.UPDATE scope; verify with a phone test where the owner does not pick, then read Flow › History. If refused: a Zoho API Console client with that scope (Sanjeev creates it) or another route — propose, don't do. Without the fallback SalesIQ marks a forwarded chat missed after ~3 min.
g. ~~Publish the bot~~ done (V2 published 8 Oct 12:58).
h. Next items from the handoff, each needing a go:
   - WhatsApp template for form leads from [phone redacted] — balance is **10 credits**; Sanjeev tops up.
   - `Chat_Attended_By` (write the attending operator to the lead).
   - Meta: create SIB-04 as DRAFT/PAUSED in 152154124583473 (CTWA vs Instant Form A/B; ads named ACR-C1/C2/C5). **None exists yet.** Do not activate.
i. Open items: where 1-minute no-pickup re-routing lives (not possible in a CRM rule); daily watchdog edits (add Advt - WhatsApp — Cowork desktop-local task); optional backfill of ~745 Accounts' first touch; delete duplicate function `stamp_account_firsttouch1` (needs go).
j. **Sanjeev's own steps still open:**
   - Delete the 2 TEST leads 1123581000945064083 and 1123581000945155075.
   - LeadChain SIB-04 chain → rule "PPC - SIB-04 Annual Filings - LG-11", static Tag FB-ACR, Product Cat Annual Filing.
   - Reconnect SalesIQ connection `zoho_bot1` — "Expiring Soon".

## Also tidy (read-only check, then propose)
- Optionally re-read member lists of Sales - General Inquery / Licenses / IPR / FDI (counts only on 7 Oct: 31 / 30 / 29 / not read).
- Update the staff plan's role table and the flow doc's steps (plug copy, bot name, import done) once Sanjeev agrees.

## Output
End with a short report (what was done, what is open, who does it), append every change to the change log, and write the prompt for the session after.
