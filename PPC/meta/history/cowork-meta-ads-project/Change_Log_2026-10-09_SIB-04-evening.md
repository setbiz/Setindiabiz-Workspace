# Change Log — SIB-04, 9 Oct 2026 evening (18:00–18:30 IST)

Continues `Meta Ads/Change_Log_2026-10-09_SIB-04.md` (last entry C29). Sanjeev, 17:59: "lets complete remaining things so that we move to ads".
AskUserQuestion answers (18:0x): **Publish V3** · **Rename the webhook-named workflow** · **Add 'Advt - WhatsApp' to the Setindiabiz Ops scheduled task**. 18:12: "is zoho_bot1 in use if yes then migrate else lets delete it".
Browser: Claude in Chrome ("SK Big HP"). Nothing in Meta changed.

## Read-only findings

| # | Item | Finding | Method |
|---|---|---|---|
| R22 | SalesIQ data workflow named with the Flow webhook URL (61466000026041027) | Brand Setindiabiz Inquiries, event conversation.missed, action = webhook to Zoho Flow 667631050. It is the hook Zoho Flow created for the realtime SalesIQ trigger "Conversation missed" of Flow **"Missed Chat - Team Alert and Task"** (Conversation missed → Send Email to Sanjeev; created 04-07-2026, same day as the hook). Flow ran 25 times in the last 7 days, last on 08 Oct — matches the hook's last-triggered date. **Keep it**: deleting it stops the missed-chat email. | SalesIQ workflow detail + Flow summary/builder (view only) |
| R23 | SalesIQ connection `zoho_bot1` ("Zoho Bot", service Zoho OAuth, scope ZohoCRM/crmapi, deprecated, "Expiring Soon") | Not referenced in the code of any of the 18 SalesIQ plugs or the 2 data workflows (scanned each script for every connection name). Usage found instead: live plug `sib_wa_lead_1791383468657` → `zohocrm1` (10) + `sib_crm_cb` (3); ChatGPT paid lead attribution → `sib_crm_cb` (2); `sib_client_check` → `sib_crm` (1); `sib_owner` → `sib_crm` (2). The 3 Zobots are codeless and use plugs. → unused, nothing to migrate. | Plug/script editors read via CodeMirror (view only, nothing saved) |
| R24 | Daily watchdog | Not among the account's cloud scheduled tasks (6 listed); it is a Cowork desktop-local task, not reachable from this session. The cloud task "Setindiabiz Ops — Tiya + Desk + CRM" (every 3 h) treated only 'Self - Web Chat' and 'Social - WhatsApp' as chat leads; "Weekly paid-channel measurement report" breaks leads down by Lead_Source generically (no list to change). | list_triggers |

## Changes

| # | Item | Change | Before | After | Verified |
|---|---|---|---|---|---|
| C30 | Cloud scheduled task **"Setindiabiz Ops — Tiya + Desk + CRM"** (trig_01U416h6TEbAxotzjPHtmGEA) | Prompt edited in 3 places only: FIXED FACTS and PART B STEP 1 `Lead_Source in ('Self - Web Chat','Social - WhatsApp')` → `…,'Advt - WhatsApp')`, plus one clarifying sentence ("'Advt - WhatsApp' = SIB-04 click-to-WhatsApp ad chats, claimed by the SalesIQ plug sib_wa_lead_1791383468657 - added 9 Oct 2026; never change their Lead_Source"); PART C-2 misattribution check now also accepts 'Advt - WhatsApp'. Schedule, model, everything else unchanged. | 30,140 chars | 30,356 chars | Yes — saved prompt read back and compared character-for-character with the intended text: identical. |
| C31 | SalesIQ connection **`zoho_bot1`** | Deleted by Sanjeev (18:23) after R23 | 6 connections | **5**: zohocrm, zohocrm1, sib_siq, sib_crm, sib_crm_cb | Yes — screenshot |
| C32 | Zobot **"Tiya - Annual Filings"** (61466000026786012) | **Published V3** by Claude (~18:25), carrying C6 (A04 Pvt Ltd `answers` = `Entity: %q_entity% \| Year: %q_fy_co%`) | DRAFT, last modified 11:25 AM, V2 live | **V3 · PUBLISHED**, "Published a few seconds ago" | Yes — screenshot viewed (saving it to disk was refused by the session safety check) |
| C33 | Rename of the webhook-named workflow (R22) | **Not done — stopped safely.** The Edit form for this Flow-managed hook loads with Name and Module blank; saving it would rebuild the hook from a half-empty form and could break the missed-chat email. Closed without saving; list still shows it unchanged (updated 04 Jul). | — | Unchanged | Yes — list re-read |

Rollback: C30 — re-apply the previous prompt (the 3 edits are listed above). C31 — re-create a connection only if something needs it (nothing did). C32 — publish V2 again from the bot's version history.

## Open after this session
- Webhook-named workflow keeps showing the Flow key to SalesIQ admins (low risk). Safe ways to fix later: re-save the trigger in the Flow (Zoho re-creates the hook) and check the new hook's name, or accept as is.
- Desktop watchdog (Cowork desktop-local): add `Advt - WhatsApp` to paid-Meta Lead_Source lists and count empty Lead_Status as unworked — needs a desktop session.
- Project instructions define the paid-Meta segment as Lead_Source = "PPC Meta Insta" only; SIB-04 CTWA leads will be "Advt - WhatsApp" (and Instant Form leads via LeadChain as configured) — include them in scorecards when the ads go live.
- LeadChain SIB-04 chain can only be set up once the SIB-04 Instant Form exists (ads step).
- Desk test contact "Amod Testing" (optional delete). [phone redacted] not reaching SalesIQ since 8 Oct (unexplained, test number).
