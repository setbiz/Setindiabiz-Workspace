# CRM → Meta signals: gaps and fix plan — 14 Oct 2026

Sanjeev, 14 Oct 19:47: "Yes we should send all relevant signals to Meta."

Status: **APPLIED 14 Oct 2026, 19:58–20:13 IST** (Sanjeev: "Apply all"). See `Change_Log_2026-10-14_CAPI-All-Signals.md`.

## 1. What reaches Meta today

| Signal | Form leads (Advt - Facebook / Instagram) | WhatsApp leads (Advt - WhatsApp) |
|---|---|---|
| ValidLead or QualifiedLead, first grading (`sib_capisweep` v2) | Sent | Sent since 13 Oct, matched on hashed phone |
| QualifiedLead after an earlier ValidLead | **Not sent** (the sweep sends one event per lead) | **Not sent** |
| Committed and Purchase from Deals (`sib_sendMetaCAPI1`, Rule 2) | Sent, but **repeated at every won stage** | **Not sent** (source not in the function's list) |
| Click-attributed WhatsApp events (`business_messaging` + `ctwa_clid`) | n/a | **Not possible yet** (no click ID in CRM) |

## 2. Findings

**F1. The first WhatsApp sale was not reported.**
- Deal P101453, ONWEBSYS DIGITRANS LLP (contact Rakesh Roshan), LLP Annual Return, ₹7,660.
- Stage history: Qualified 16:22 → Payment Wait 16:55 → Won 17:08 → W-ACR Login → W-Login.
- The contact's Lead_Source is `Advt - WhatsApp`. The deal function's source list is `{Advt - Facebook, Advt - Instagram, PPC Meta Insta}` (code read in the IDE today, last modified 6 Jul), so it returned without sending.

**F2. One sale is reported as three or more Purchases.**
- Rule 2 fires on every Stage edit. The function has no "already sent" check and no `event_id`.
- Typical deal path: Qualified → Won → W-Login → W-Finance. Stage histories checked:
  - Cynovate P100996: Won 25 Sep, W-Login 29 Sep, W-Finance 12 Oct;
  - Trinexa DSC P101012: Won, W-Login, W-Finance 10 Oct;
  - Crown Manpower P100924: Won, W-Login, W-Finance 7 Oct.
- Each of those edits sent a full-value Purchase, so a deal moving to W-Finance two weeks after the sale is reported as a new sale on that day.
- **Scale, last 3 weeks:**
  - 25 new Meta-sourced won deals;
  - 159 Meta-sourced won deals modified;
  - about 223 Purchase events in dataset 1242417817083521, including a spike of 52 on 5 Oct (some may be website-pixel Purchases).
- **Effect:** Meta's purchase count and value are inflated several-fold. No active ad set optimises on Purchase today (SIB-04 optimises on leads and conversations), so nothing is being bid on this yet. It would mislead any future Purchase or value optimisation.

**F3. The QualifiedLead upgrade is lost.**
- The sweep marks `Meta_CAPI_Sent` after the first event, so a lead sent as ValidLead never sends QualifiedLead when it reaches Proposal Sent.
- That is the progressed-lead signal in our objective hierarchy.

**F4. WhatsApp ads can't receive click-attributed events yet.**
- Meta's Conversions API for Business Messaging requires `action_source: business_messaging`, `messaging_channel: whatsapp`, `user_data.whatsapp_business_account_id` and `user_data.ctwa_clid` (developers.facebook.com/docs/marketing-api/conversions-api/business-messaging).
- The same page lists the allowed event names: Purchase, LeadSubmitted, QualifiedLead and others. A custom event such as ValidLead is not on the list.
- Meta documents purchase optimisation for click-to-WhatsApp ads through this route.
- What blocks it:
  - `CTWA_Click_ID` is empty on all 174 WhatsApp leads; the bot leaves the plug's `clid` input empty;
  - it is not confirmed that SalesIQ exposes the click ID (`referral.ctwa_clid`) to the bot. The question to Zoho support was drafted on 6 Oct; no reply is on file.

## 3. Proposed changes, in order (each needs a go)

| # | Change | Records touched | Rollback |
|---|---|---|---|
| S1 | Create text field **Meta CAPI Event** (`Meta_CAPI_Event`, length 30) on Leads and on Deals. | Schema, 2 fields | Delete the fields. |
| S2 | **Deals backfill** with trigger []: Meta-sourced deals already in a won stage → `Meta_CAPI_Event = Purchase` (585: Won 7, W-Login 84, W-SPI 118, W-SKV 290, W-Finance 71, W-CSD 15). The one Payment Wait deal → `Committed`. WhatsApp deal P101453 left blank so it can be sent in S4. | 586 deals | Clear the field. |
| S3 | **Leads backfill** with trigger []: paid leads created since 9 Oct with `Meta_CAPI_Sent = true`. Proposal Sent → `QualifiedLead` (5); all others → `ValidLead` (41: Facebook 6, Instagram 3, WhatsApp 32, of which 7 are now Lost). | 46 leads | Clear the field. |
| S4 | **Sender v2**, same body in both copies (`sib_sendMetaCAPI` for Leads, `sib_sendMetaCAPI1` for Deals). Adds `Advt - WhatsApp` to the source list. Sends each event once per record: ValidLead < QualifiedLead < Committed < Purchase, recorded in `Meta_CAPI_Event`. Adds `event_id` and `custom_data.lead_source`. Then one manual Run for P101453 → Purchase ₹7,660. | 2 functions, 1 event | IDE → Revisions → 6 Jul version. |
| S5 | **Sweep v3**: also sends QualifiedLead once for a lead previously sent as ValidLead. | 1 function | Revisions → 13 Oct v2 (`sib_capisweep_v2_2026-10-13.deluge.txt`). |

Code: `sib_sendMetaCAPI_v2_2026-10-14.deluge.txt`, `sib_capisweep_v3_2026-10-14.deluge.txt`.

**Expected after S4:**
- Daily Purchase events drop to about the number of new Meta-sourced sales (about 1–2 a day). This is the correction, not an outage.
- The daily server-channel check should compare against that baseline, not the old one.

**Verify:**
- S4: the console for P101453 shows `events_received: 1`, and the deal's `Meta_CAPI_Event` = Purchase.
- S4: move one test deal from W-Login to W-Finance and confirm the log says "not above last sent Purchase - skipped".
- S5: first scheduled run log; a lead at Proposal Sent with `Meta_CAPI_Event = ValidLead` flips to QualifiedLead.

## 4. Handoff to the SalesIQ project (they own the bot and plug)

1. Find out whether SalesIQ passes the click-to-WhatsApp `referral` (`ctwa_clid`, `source_id`) to a Zobot or plug. The Zoho ticket from 6 Oct needs a reply.
2. If it does, map it into the existing `clid` input of `sib_wa_lead_1791383468657` on the claim card. The plug already writes `CTWA_Click_ID`.
3. Then, in this project:
   - get the WABA ID for +919266601455 (and the other numbers);
   - link dataset 1242417817083521 to the WABA (`POST /{WABA_ID}/dataset` returns the existing link);
   - confirm the token has `whatsapp_business_manage_events`;
   - send WhatsApp-lead events as `business_messaging` with `ctwa_clid`: ValidLead → LeadSubmitted, QualifiedLead, Purchase.
