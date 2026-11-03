# SIB-04 Company Annual Return – Session Handoff (revised 7 Oct 2026, 13:45 IST)

Paste the prompt at the bottom of this file as the first message of a new session in this Project.

## Scope
ONE campaign only: **SIB-04 Company Annual Filings** (Pvt Ltd / OPC annual return; LLP Form 8 note). All other campaigns (SIB-01/02/03/05) wait until SIB-04 is live. Later campaigns reuse the same pattern: own Canva pair, own PPC assignment entry, own Zobot.

## Read first
1. This file.
2. Doc "SIB-04 CRM Changes – Analysis & Proposal" — https://claude.ai/code/artifact/8e6f65ac-f332-4688-a224-2afa68819df4 (Claude Docs connector: project id 8e6f65ac-f332-4688-a224-2afa68819df4, tab 81896803-d866, body node c5cd7087-06d8). Read it and its comments before acting; Sanjeev's edits there override this file.
3. `Meta Ads/Change_Log_2026-10-07_SIB-04-CRM.md` — what has already been executed. Append every new change there.
4. `Meta Ads/Meta_CTWA_Relaunch_Plan_2026-10-06.md` (§6 bot + mapping, §7 CRM) and `Meta Ads/Relaunch_Decisions_Log_2026-10-06.md` (budget CTWA ₹3,500 + Form ₹2,500/day = ₹6,000; stop-loss ceiling ACR ₹500; run until 29 Nov 2026).
5. `Meta Ads/Stamp_Account_FirstTouch.txt`, `Meta Ads/Inherit_Deal_Attribution.txt`.

## Decisions settled (7 Oct)
- C1–C9 in the doc: all **Approved**.
- Organic WhatsApp chats → `Social - WhatsApp`; legacy `WhatsApp - SETINDIABIZ` retired.
- Ad codes in pre-filled WhatsApp message: ACR-C2 (cost of delay, Canva p1), ACR-C1 (deadline, p2), ACR-C5 (hybrid, p3).
- C6: add the current Lead_Source values to the old picklists Accounts.First_Touch_Lead_Source and Deals.First_Touch_Source (keep old values).
- Form leads get an automatic WhatsApp template from [phone redacted] within ~2 minutes (needs an approved template).
- Owner vs chat attender: the CRM owner stays; mismatches go on the daily list; no auto-reassignment.
- **SIB-04 pool = all 10 people in column L (LG-11) of sheet "Team Sheet (Use Responsibly)" › tab "Lead Handler Group"** (Drive id 1tBrTkEdvZ8mu3MFa397JP5Ifm8IxZlR2G8FXoidW9-g). Read ONLY that tab — other tabs hold passwords. CRM user IDs:
  - Pragya Agrawal 1123581000744835001 (sheet spells "Agarwal")
  - Rishika Singh 1123581000754062001
  - Tarun Kumar 1123581000898222001
  - Mahima Sehrawat 1123581000899805001
  - Anish Singh 1123581000904230019
  - Amit Kumar 3 1123581000900455002
  - Priyam Tiwari 1123581000900978001
  - Gaurav Pandey 1123581000900792006
  - Suman Khowal 1123581000012023007 (TL)
  - Praveen Singh 1123581000005632013 (Gold Team)
- No pickup within **1 minute** → next person in the round robin. Chat hours **Mon–Sat 09:30–19:30**; bot handles other times.
- **One PPC assignment per product.** SIB-04 first: `PPC – SIB-04 Annual Filings (LG-11)`; criteria Lead_Source in (Advt - Facebook, Advt - Instagram, Advt - WhatsApp) AND Meta_Campaign starts with `SIB-04` → round robin over the 10. Zoho applies ONE assignment rule per incoming record (chosen by web form / import / API `lar_id`). All Meta and chat leads are created via API under Sanjeev's user. So first find which rule LeadChain and SalesIQ pass today. If only one rule can be named, build per-product entries inside one `PPC – Meta 2026` rule. Show Sanjeev before saving.

## Already done (verified)
- C2/C3 fields created via API (7 Oct ~13:15):
  - Leads: `WhatsApp_Opt_In`, `Opt_In_Time`, `Meta_Ad_Code`, `Chat_Attended_By`
  - Contacts: `WhatsApp_Opt_In`, `Opt_In_Time`
  - Deals: `Meta_Ad_Code`
  - Not yet on page layouts; conversion mapping not yet set.
- The 6 legacy leads relabelled to `Social - WhatsApp` (workflows not triggered).
- **C1 done 7 Oct ~13:40:** `Advt - WhatsApp` added to the Lead_Source global set; 41 values on Leads, Contacts, Deals, Accounts (API-verified).
- Creatives: Canva folder "PPC 2026" (FAHXTwdMxJ4) holds "SIB-04 Annual Filings – 1:1 Feed" (DAHXThVtclk) and "– 9:16 Stories/Reels" (DAHXT5r2Ex8). The designer is editing them; do not touch until Sanjeev says done, then export PNGs.

## CRM facts (read-only check 7 Oct)
- **Zoho CRM is on the US data centre: https://crm.zoho.com/crm/setindiabiz/** (not crm.zoho.in). Global Sets: Setup › Modules and Fields › Global Sets tab (`/settings/global_picklists`).
- Lead_Source is a global set (id 1123581000914084595) shared by Leads/Contacts/Deals/Accounts.
- Existing fields to reuse: CTWA_Click_ID, WhatsApp_Number, Meta_Ad_Type (has `WhatsApp` option; LeadChain writes fb/ig), Meta_Ad_ID/Name/Campaign, UTM_*.
- First-touch picklists hold 27 old values: 745 of 758 accounts since 1 Jul are blank, and only 6 are Meta_Sourced. Stamp_Account_FirstTouch only matches `PPC Meta*`/`PPC Insta*`.
- Existing Lead assignment rules: `Lead - General 2026` (default Sanjeev) + 5 dialer rules.

## Next steps, in order (one at a time; before/after screenshot; log each)
Zoho CRM is crm.zoho.com (US DC), and Sanjeev is signed in to it in the built-in browser.
1. ~~C1 — add `Advt - WhatsApp` to Lead_Source.~~ Done 7 Oct.
2. C2 — add the new fields to layouts. Lead conversion mapping: WhatsApp_Opt_In/Opt_In_Time → Contacts; Meta_Ad_Code → Deals.
3. C6 — add the current values to both first-touch picklists; map Lead_Source → First_Touch_Lead_Source on conversion.
4. C7 — update Stamp_Account_FirstTouch to a list check: {"Advt - Facebook","Advt - Instagram","Advt - WhatsApp","PPC Meta Insta","PPC Insta"}.contains(src).
5. C8 — add all three `Advt -` Meta values to WF1 "Stamp Account Meta Sourced", the watchdog, scheduled tasks and the Zoho Analytics scorecard. C9 — verify that CAPI Rule 1 and `sib_capisweep` exclude WhatsApp (no edit).
6. C5 — find the assignment rule LeadChain and SalesIQ use, then build the SIB-04 PPC entry (pool above).
7. C4 + Zobot — in SalesIQ, build the SIB-04 bot:
   - Q1 entity (Pvt Ltd / OPC / LLP), Q2 year (FY 2025-26 only / older), Q3 AGM held?
   - Webhook Deluge: search Leads then Contacts by the last 10 digits of the phone → update or create.
     - New lead: Lead_Source `Advt - WhatsApp` if an ad code is present, else `Social - WhatsApp`; Meta_Ad_Type `WhatsApp`; CTWA_Click_ID, Meta_Ad_Code, Meta_Campaign `SIB-04…`, opt-in + time.
     - Existing lead: never overwrite Lead_Source.
   - Route the chat to the CRM owner; no pickup in 1 min → next in the round robin; write the attender into Chat_Attended_By.
   - Form-lead WhatsApp template from [phone redacted].
8. Meta: create SIB-04 as DRAFT/PAUSED in account 152154124583473, with a CTWA vs Instant Form A/B test. Ads named with ACR codes. Do not activate.
9. End-to-end test from Sanjeev's phone: check the CRM record, owner, source, ad code and Chat_Attended_By.
10. Publish only on Sanjeev's explicit go. Then add SIB-04 to the daily watchdog: owner≠attender, duplicate phones, owners outside the pool, cost per valid/progressed/won.

## Rules
- Zoho CRM outcomes are the source of truth. Optimise in this order: cost per won → committed → progressed → valid lead.
- Every Meta or CRM mutation needs explicit approval (the doc's Decision column counts), one change at a time, screenshot before/after, logged.
- Never move money or make payments. Never enter passwords — Sanjeev signs in himself.
- Ad claims must be defensible under:
  - s.403 Companies Act 2013 + Companies (Registration Offices and Fees) Rules 2014 (₹100/day per form, no cap)
  - s.137(1) (AOC-4 within 30 days of AGM)
  - s.92(4) (MGT-7/7A within 60 days)
  - LLP Rules r.24(8) (Form 8 by 30 Oct)
  - Re-check MCA fee rules before publishing.
- Deluge has no `!` operator; use `.contains(...) == false`. COQL returns owner surname only; map by user ID.

---

## PROMPT (paste this into the new session)

Continue the Setindiabiz Meta relaunch for SIB-04 Company Annual Filings only. First read the Project doc `Meta Ads/SIB-04_Session_Handoff_2026-10-07.md` and follow it exactly. Then read my doc "SIB-04 CRM Changes – Analysis & Proposal" (https://claude.ai/code/artifact/8e6f65ac-f332-4688-a224-2afa68819df4) including its comments, and `Meta Ads/Change_Log_2026-10-07_SIB-04-CRM.md`. C1–C9 are approved; C1, C2 field creation and C3 are done. Continue from the next open step in Zoho CRM (crm.zoho.com, US DC) using the built-in browser, where I'm already signed in. Do one change at a time with before/after screenshots, log each in the change log, and pause for my go before C5 (assignment), the Zobot, and anything in Meta.
