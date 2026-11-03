# Prompt for the next session — SIB-04 (written 8 Oct 2026, 17:50 IST)

Paste everything below the line into a new session in the "Meta Ads - Optimisation" project.

---

You are continuing the Setindiabiz Meta relaunch for **SIB-04 Company Annual Filings** (WhatsApp [phone redacted], brand Compliance & ACR, bot "Tiya - Annual Filings" V2 published).

## Read first (project docs)
- `Meta Ads/Change_Log_2026-10-08_SIB-04-fallback.md` — latest; append every change here (or start a new dated log and say so).
- `Meta Ads/Change_Log_2026-10-07_SIB-04-CRM.md` — full history to 8 Oct 15:45.
- `Meta Ads/SIB-04_Session_Handoff_2026-10-07.md`, `SIB-04_Zobot_Flow_2026-10-07.md`, `sib_wa_lead.deluge.txt` (plug v2).

## Where things stand (8 Oct 17:50)
- **Working end to end:** WhatsApp chat → bot asks entity + year → plug claims the SalesIQ-created lead (Advt - WhatsApp, Meta_Ad_Code ACR, Product Annual Filing, Tag FB-ACR) → SIB-04 LG-11 round robin sets the owner → bot forwards the chat to that owner (tested with Mahima Sehrawat and Anish Singh).
- **Owner-miss fallback: abandoned.** SalesIQ's API will not move a chat the bot holds: transfer → 6139 "Given user doesn't have permission to transfer", pickup → 6015 "Already pickup the chat" (Sanjeev is Owner and in all 9 departments — irrelevant). **Decision 17:44 (Sanjeev): unpicked chats stay "missed"; Customer Support watches all missed chats.** SalesIQ marks the chat missed ~2–3 min after the forward; CRM lead gets a "Zoho SalesIQ chat missed" note.
- Fallback pieces still in place unless Sanjeev has switched them off (check read-only): Zoho Flow "SIB-04 chat fallback - 1 min to Customer Support" (ON), SalesIQ data workflow "SIB-04 bot transfer - 1 min fallback" 61466000026786113 (Enabled), Flow function `sib04ChatFallback` v1.4, CRM function `sib04_siq_transfer` v2 (id 1123581000945603370, **REST API key enabled**), CRM connection `sib_siq_transfer`, disabled SalesIQ workflow 61466000026786132. All harmless (they read the chat and stop) but useless. Proposed clean-up (needs go / Sanjeev's clicks): Flow OFF; disable 61466000026786113; turn OFF the API key on `sib04_siq_transfer`; optionally delete 61466000026786132.

## Hard rules
- Every change needs Sanjeev's explicit go naming the specific change, one at a time, before/after screenshot, logged. Read-only needs no go. The session permission check has blocked Claude's clicks on Flow ON/Confirm/Apply and builder edits before — when blocked, leave the screen ready and hand the click to Sanjeev; never work around it.
- Never enter passwords, never move money or top up WhatsApp credits (balance 10 credits).
- Browser: Claude in Chrome. Names reset ("Browser 1/2"); on 8 Oct afternoon Sanjeev used **"SK Big HP"**. If unsure, send the Connect prompt and let him pick. Open your own tab. Don't click "Join this chat"/"Whisper" on monitored chats or the bottom-left Cliq bar in SalesIQ.
- Zoho CRM is crm.zoho.com (US DC), org path /crm/setindiabiz/. COQL Owner returns surname only — resolve ids via `zoho-sales-owner-ids` memory.
- Ad claims must stay defensible (Companies Act 2013 s.92(4), s.137(1), s.403 + Companies (Registration Offices and Fees) Rules 2014; LLP Rules r.24(8)) — re-check MCA fee rules before any ad copy is published.

## Work, in order (each change needs a go)
1. Read-only: confirm whether the fallback pieces were switched off; propose the clean-up above if not.
2. Support watch on missed chats: optional help — a saved SalesIQ view/filter for missed chats on Compliance & ACR / Sales - CACS ACR; remind that WhatsApp free-form replies are possible only within 24 h of the visitor's last message (after that a paid template is needed).
3. A04 (Pvt Ltd) card `answers` hard-codes "Entity: Private Limited" even for OPC → propose "Entity: %q_entity% | Year: %q_fy_co%" (confirm the variable name in the builder first).
4. `Chat_Attended_By` (write the attending operator to the lead) — design + go.
5. WhatsApp template for form leads from [phone redacted] (Sanjeev tops up credits).
6. Meta: create SIB-04 as **DRAFT/PAUSED** in 152154124583473 (CTWA vs Instant Form A/B; ads ACR-C1/C2/C5). None exists. Do not activate.
7. Daily watchdog: add `Advt - WhatsApp` to the paid-Meta Lead_Source lists (Cowork desktop-local task).

## Sanjeev's own steps still open
- Delete test leads **1123581000945620151** ("Pavneet", [phone redacted], owner Anish Singh) and **1123581000945723027** ("dhoundiyalswati7", [phone redacted], owner Mahima Sehrawat) — both Advt - WhatsApp and would distort campaign numbers.
- Tidy-up: delete original plug `sib_wa_lead` (61466000026793006, never triggered) and unconnected connections `sib_crm_cb1`, `zohocrm11`; reconnect `zoho_bot1` ("Expiring Soon") — not re-checked 8 Oct.
- LeadChain SIB-04 chain → rule "PPC - SIB-04 Annual Filings - LG-11", static Tag FB-ACR, Product Cat Annual Filing.
- Unexplained: [phone redacted] stopped reaching SalesIQ after 4:43 PM on 8 Oct (nothing blocked on the SalesIQ side).

## Output
End with a short report (done / open / who), append every change to the change log, and write the prompt for the session after.
