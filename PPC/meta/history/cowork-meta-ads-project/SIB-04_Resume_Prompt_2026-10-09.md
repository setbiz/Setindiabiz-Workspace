# Prompt for the next session — SIB-04 ads build (updated 9 Oct 2026 ~18:30 IST, after C30–C33)

Paste everything below the line into a new session in the "Meta Ads - Optimisation" project.

---

You are continuing the Setindiabiz Meta relaunch for **SIB-04 Company Annual Filings**. The SalesIQ/CRM side is finished and cleaned up; the next step is the **Meta ads build (DRAFT/PAUSED only)**.

## Read first (project docs)
- `Meta Ads/Change_Log_2026-10-09_SIB-04-evening.md` — latest (R22–R24, C30–C33).
- `Meta Ads/Change_Log_2026-10-09_SIB-04.md` — the day's roll-back and clean-up (C5–C29).
- `Meta Ads/Meta_CTWA_Relaunch_Plan_2026-10-06.md`, `Meta Ads/Relaunch_Decisions_Log_2026-10-06.md`, `Meta Ads/Competitor_Creative_Scan_2026-10-06.md`, `Meta Ads/SetIndiaBiz_Meta_Ads_Operator_Instructions.md`.

## State on 9 Oct ~18:30
- WhatsApp [phone redacted] on SalesIQ brand Compliance & ACR (app 61466000023310359). Bot **"Tiya - Annual Filings"** (61466000026786012) **V3 PUBLISHED** (A04 now sends the real entity answer).
- Chat flow: WhatsApp chat → bot (`q_entity`, `q_fy_co`) → SalesIQ creates the lead ("Chat" → "Self - Web Chat") → plug `sib_wa_lead_1791383468657` claims it (**Lead_Source "Advt - WhatsApp"**, Meta_Ad_Code ACR, Tag FB-ACR, Product Cat Annual Filing, campaign "SIB-04 Annual Filings") → LG-11 round-robin owner → bot forwards to owner → unpicked chats stay in SalesIQ › Missed for Customer Support (no CRM task, no status automation — Sanjeev's model; **do not propose rebuilding any of the deleted automation**).
- Chat leads arrive with **empty Lead_Status** until the owner sets one — count empty as "never worked" in any speed-to-lead check.
- SalesIQ connections (5): zohocrm, zohocrm1, sib_siq, sib_crm, sib_crm_cb. Data workflows (2): ChatGPT paid lead attribution; the Flow hook for "Missed Chat - Team Alert and Task" (keep — it sends the missed-chat email; don't edit it in SalesIQ, the form loads blank).
- Cloud scheduled task "Setindiabiz Ops" now treats 'Advt - WhatsApp' as a chat source (C30).
- Meta 152154124583473: all 7 campaigns PAUSED; **no SIB-04 campaign yet**, live or draft.
- No test records left in CRM or Desk.

## Work, in order (each change needs Sanjeev's go)
1. **Re-check the law and MCA fees before writing any ad copy** (Companies Act 2013 s.92(4) MGT-7/7A within 60 days of AGM, s.137(1) AOC-4 within 30 days of AGM, s.403 additional fee; Companies (Registration Offices and Fees) Rules 2014 — ₹100/day per form; LLP Rules 2009 r.24(8) Form 8 by 30 Oct, Form 11 by 30 May). Use mca.gov.in / government sources and confirm the current version; no guaranteed outcomes, no invented timelines, no misstatement of government fees.
2. **Build SIB-04 in Meta as DRAFT/PAUSED** in 152154124583473: CTWA (to [phone redacted]) vs Instant Form A/B; ads ACR-C1/C2/C5 from Canva "PPC 2026"; naming with ACR codes. **Do not activate.** Show Sanjeev previews before anything is published.
3. Once the SIB-04 Instant Form exists: Sanjeev sets up the **LeadChain SIB-04 chain** → rule "PPC - SIB-04 Annual Filings - LG-11", static Tag FB-ACR, Product Cat Annual Filing.
4. Reporting: include `Advt - WhatsApp` (CTWA) and the SIB-04 Instant Form leads in the Meta scorecard (the project instructions currently name only "PPC Meta Insta").
5. WhatsApp template for Instant Form leads from [phone redacted] — after Sanjeev tops up credits (balance 10).
6. Desktop watchdog (Cowork desktop-local): add `Advt - WhatsApp` + empty-Lead_Status rule — needs a desktop session.

## Hard rules
- Every change needs Sanjeev's explicit go naming the specific change, one at a time, before/after screenshot, logged. Read-only needs no go. If the session permission check blocks a click, leave the screen ready and hand the click to Sanjeev; never work around it. After handing over a tab, don't reload/navigate it until Sanjeev says he is done; screenshot it as left first.
- Never activate a Meta campaign, never move money, never top up credits, never enter passwords.
- Don't delete CRM records with the CRM connector (described as permanent) — use the CRM UI (Recycle Bin).
- Browser: Claude in Chrome; send the Connect prompt and let Sanjeev pick "SK Big HP". Open your own tab; closing the last tab removes the tab group (create a new one). Don't click "Join this chat"/"Whisper" or the Cliq bar. The extension can't read support.setindiabiz.com (Desk) — use the Desk connector.
- Zoho CRM is crm.zoho.com (US DC), /crm/setindiabiz/. COQL Owner returns surname only — resolve ids via the `zoho-sales-owner-ids` memory.

## Sanjeev's own steps still open
- LeadChain SIB-04 chain (after the Instant Form exists).
- Optional: delete Desk test contact "Amod Testing" (293676000530151006).
- Unexplained: [phone redacted] stopped reaching SalesIQ after 4:43 PM on 8 Oct (test number).

## Output
End with a short report (done / open / who), log every change in a dated change log, and write the prompt for the session after.
