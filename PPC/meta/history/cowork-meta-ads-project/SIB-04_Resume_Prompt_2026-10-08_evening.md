# Prompt for the next session — SIB-04 (written 8 Oct 2026 evening, updated 9 Oct after clean-up)

Paste everything below the line into a new session in the "Meta Ads - Optimisation" project.

---

You are continuing the Setindiabiz Meta relaunch for **SIB-04 Company Annual Filings** (WhatsApp [phone redacted], brand Compliance & ACR = SalesIQ app 61466000023310359, bot "Tiya - Annual Filings" V2 published 12:58 PM 8 Oct).

## Read first (project docs)
- `Meta Ads/Change_Log_2026-10-08_SIB-04-evening.md` — latest (findings R1–R11, changes C1–C4, observation O1, proposals list). Append changes there or start a new dated log and say so.
- `Meta Ads/Change_Log_2026-10-08_SIB-04-fallback.md` and `Change_Log_2026-10-07_SIB-04-CRM.md` — history.
- `SIB-04_Zobot_Flow_2026-10-07.md`, `sib_wa_lead.deluge.txt`.

## State on 9 Oct (see change log R1–R11, C1–C4, O1)
- Working: WhatsApp chat → bot (entity `q_entity`, year `q_fy_co`) → plug claims the SalesIQ lead (Advt - WhatsApp, ACR, Annual Filing, FB-ACR) → LG-11 round robin owner → bot forwards to owner.
- Decision (Sanjeev, 8 Oct 17:44): unpicked chats stay missed; Customer Support watches missed chats.
- Abandoned fallback is **fully switched off**: Flow "SIB-04 chat fallback" OFF (C1); SalesIQ workflows 61466000026786113 and 61466000026786132 both Disabled (C3); CRM function `sib04_siq_transfer` API key OFF (C4, 9 Oct). Nothing deleted — deletion is optional and needs a go.
- New SalesIQ data workflow **"SIB-04 missed chat - callback task" (61466000026803029)** created (brand Compliance & ACR, conversation.missed, no rule — Sales - CACS ACR is not offered by the rule picker; Sanjeev chose brand-only). Sanjeev saved it 06:49 PM; **phone test passed 19:24** (C2e): chat #61318 → lead 1123581000945624169 (Gaurav Pandey) → task "Callback: SIB-04 missed chat #61318 - [customer name redacted]", High, due today, owner Gaurav Pandey.
- Plug-created SIB-04 leads arrive with **Lead_Status empty** (O1) — the speed-to-lead check (`Establishing Contact`) would miss them.
- Before 2A, nothing alerted on a missed SIB-04 chat: Flow "Missed Chat - Team Alert and Task" is scoped to app 61466000023074073 (Setindiabiz Inquiries) and emails only sanjeev@setindiabiz.com; SalesIQ workflow "Missed chat - callback task" (61466000026746193) is scoped to Setindiabiz Inquiries + Department Customer Support.
- A04 plug `answers` = "Entity: Private Limited | Year: %q_fy_co%" (hard-coded). A04 shows "Update parameters for the latest version (v2)".
- Test leads 1123581000945620151 and 1123581000945723027 (Lead_Status Lost) and 1123581000945624169 "[customer name redacted]" + its task 1123581000945706112 still in CRM — Sanjeev to delete.
- Meta 152154124583473: all 7 campaigns PAUSED; no SIB-04 campaign live or draft.

## Hard rules
- Every change needs Sanjeev's explicit go naming the specific change, one at a time, before/after screenshot, logged. Read-only needs no go. If the session permission check blocks a click, leave the screen ready and hand the click to Sanjeev; never work around it.
- Never enter passwords, never move money or top up WhatsApp credits (balance 10 credits).
- Browser: Claude in Chrome; names reset — send the Connect prompt and let Sanjeev pick (he uses "SK Big HP", the Big HP laptop). Open your own tab. Don't click "Join this chat"/"Whisper" on monitored chats, or the bottom-left Cliq bar in SalesIQ. In the Zobot builder, close card panels with Cancel (the Save button turns active on the A04 plug card just from opening it). Don't save screenshots that show API keys.
- Zoho CRM is crm.zoho.com (US DC), /crm/setindiabiz/. COQL Owner returns surname only — resolve ids via `zoho-sales-owner-ids` memory.
- Ad claims must stay defensible (Companies Act 2013 s.92(4), s.137(1), s.403 + Companies (Registration Offices and Fees) Rules 2014; LLP Rules 2009 r.24(8)) — re-check MCA fee rules before any ad copy is published.

## Work, in order (each change needs a go)
1. Clean-up: done except optional deletion of the disabled workflows (…113, …132) and the switched-off Flow — only on Sanjeev's go.
2. Support watch: 2A done. 2B (optional): add app 61466000023310359 + the Support mailbox to the missed-chat email Flow — needs the mailbox address.
3. A04 `answers` → `Entity: %q_entity% | Year: %q_fy_co%`; publish V3 only on a separate go.
4. `Chat_Attended_By` — design + go.
5. WhatsApp template for form leads (after Sanjeev tops up credits).
6. Meta: SIB-04 as DRAFT/PAUSED in 152154124583473 (CTWA vs Instant Form A/B; ads ACR-C1/C2/C5 from Canva "PPC 2026"). Do not activate.
7. Watchdog: add `Advt - WhatsApp` to the paid-Meta Lead_Source lists (Cowork desktop-local task — needs a desktop session).
8. Lead_Status "Establishing Contact" on plug-created SIB-04 leads (O1) — design + go.

## Sanjeev's own steps still open
- Delete the 3 test leads and the test task above.
- Delete original plug `sib_wa_lead` (61466000026793006); delete unconnected connections `sib_crm_cb1`, `zohocrm11`; reconnect `zoho_bot1`.
- LeadChain SIB-04 chain → rule "PPC - SIB-04 Annual Filings - LG-11", static Tag FB-ACR, Product Cat Annual Filing.
- Rename the SalesIQ data workflow whose name is the full Flow webhook URL (contains the key).
- Unexplained: [phone redacted] stopped reaching SalesIQ after 4:43 PM on 8 Oct.

## Output
End with a short report (done / open / who), append every change to the change log, and write the prompt for the session after.
