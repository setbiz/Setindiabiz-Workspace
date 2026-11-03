# Change log — 14 Oct 2026 — CRM → Meta signals: WhatsApp sale, one event per record, QualifiedLead upgrade

**Approval:** Sanjeev, 14 Oct, 19:47 ("Yes we should send all relevant signals to Meta"), then the AskUserQuestion answer "Apply all (Recommended)".
**Plan and findings:** `Meta Ads/CAPI_All_Signals_Plan_2026-10-14.md`.
**Code:**
- `Meta Ads/sib_sendMetaCAPI_v2_2026-10-14.deluge.txt` (live);
- `Meta Ads/sib_capisweep_v3_2026-10-14.deluge.txt` (live);
- previous sender: `Meta Ads/sib_sendMetaCAPI_v1_2026-07-06.deluge.txt`.

## Changes

| # | Time (IST) | Item | Change | Verified |
|---|---|---|---|---|
| S1 | 19:58 | New text field **Meta CAPI Event** (`Meta_CAPI_Event`, length 30) | Leads (field id 1123581000947950003) and Deals (1123581000948000003), each with an info-icon tooltip. | COQL selects the field on both modules |
| S2 | 19:59–20:02 | **Deals backfill**, trigger [] | 585 Meta-sourced deals already in a won stage (contact Lead_Source Advt - Facebook / Instagram) → `Purchase`. Deal 1123581000920227149 (Payment Wait, Individual ITR Hemat Kumar Pant) → `Committed`. 6 calls of ≤100, all SUCCESS. | Re-query: 0 won Meta deals left blank, except P101453 (kept blank for S4) |
| S3 | 20:02 | **Leads backfill**, trigger [] | 49 paid leads created since 9 Oct with `Meta_CAPI_Sent = true`: 6 at Proposal Sent → `QualifiedLead`; 43 → `ValidLead`. The count grew from 46 (plan) to 49 because sweep runs added leads. | 49 SUCCESS |
| S4a | 20:05 | `sib_sendMetaCAPI1` (Deals copy, function id 1123581000911677606) → **v2** | Source list adds `Advt - WhatsApp`. Once-per-record guard on `Meta_CAPI_Event` (ValidLead 1 < QualifiedLead 2 < Committed 3 < Purchase 4). Adds `event_id` = recordId-event and `custom_data.lead_source`. Marks the event with trigger [] after `events_received` > 0. | IDE: "Function saved successfully"; length 5,236 |
| S4b | 20:07 | Manual Run, Deals / **P101453** (1123581000947712654, ONWEBSYS DIGITRANS LLP, LLP Annual Return, ₹7,660, contact Rakesh Roshan, `Advt - WhatsApp`) | **Purchase sent: `events_received: 1`**, fbtrace A3TtULpSL4MV75JGZaCH3H; deal marked Purchase. **First WhatsApp-ad sale reported to Meta.** | Console + COQL (`Meta_CAPI_Event` = Purchase) |
| S4c | 20:08 | Guard test: Run again on P101453 | "Purchase not above last sent Purchase - skipped". No POST. | Console |
| S4d | 20:10 | `sib_sendMetaCAPI` (Leads copy, 1123581000911606421) → v2 | Same body; only the first line differs. Before the change, both copies had identical bodies (checked in the browser). | Saved; length 5,235 |
| S4e | 20:11 | Guard test, Leads / 1123581000946345208 (`ValidLead`) | "ValidLead not above last sent ValidLead - skipped". | Console |
| S5 | 20:13 | `sib_capisweep` (1123581000915255380) → **v3** | Also sends QualifiedLead once when a lead marked `ValidLead` reaches Proposal Sent / Negotiation / Payment Pending. Records `Meta_CAPI_Event` on every send. Leads sent before v3 with a blank event are not re-sent. Unchanged: sources, 600-lead scan, cap 20, match keys, event_id. | Saved; manual run: "scanning 600 recently-modified leads", "0 events to send" (nothing pending) |

## Why

1. The deal sender's source list `{Advt - Facebook, Advt - Instagram, PPC Meta Insta}` excluded WhatsApp, so the first WhatsApp sale (P101453) was not reported.
2. The deal sender had no "already sent" check and no event_id. Rule 2 fires on every Stage edit, so each won-stage move sent another full-value Purchase:
   - stage histories show Won → W-Login → W-Finance (and W-SKV / W-SPI) for one deal;
   - last 3 weeks: 25 new Meta-sourced won deals, but about 223 Purchase events in the dataset, with a 52-event spike on 5 Oct (some may be website-pixel Purchases).
3. The sweep marked a lead sent after its first event, so ValidLead → Proposal Sent never sent QualifiedLead.

## Expect

- **Daily Purchase events will fall** to about the number of new Meta-sourced sales (about 1–2 a day). This is the correction, not an outage. Any watchdog check on Purchase volume must use the new baseline.
- WhatsApp-sourced deals now send QualifiedLead / Committed / Purchase once each, matched on the contact's hashed email and phone (no click ID yet).
- **Rule 1 "Meta CAPI - ValidLead"** is unchanged (criteria Advt - Facebook / Instagram). It now shares the same guard as the sweep, so the two paths cannot double-send.

## Rollback

- Functions: open each in the IDE → Revisions → restore the 6 Jul (sender) / 13 Oct (sweep) version. Or paste the v1 / v2 files and Save.
- Fields: clear `Meta_CAPI_Event` (mass update, trigger []), or delete the two fields **after** restoring the old code, because v2 / v3 read them.

## Still open

- **WhatsApp click ID (`ctwa_clid`).** It is needed to send `business_messaging` events that Meta can attribute to the click-to-WhatsApp ads and use for optimisation. It depends on SalesIQ passing the referral to the bot; the SalesIQ project owns this. See §4 of the plan.
- **Daily watchdog** (desktop-local Cowork task). Not reachable from the cloud session. Update its paid-Meta source list to the three values, and its Purchase baseline.
- **Watch:** the next real lead upgrade (ValidLead → Proposal Sent) should show "1 events to send" and the lead flips to `QualifiedLead`. Not testable today without editing a live lead.
