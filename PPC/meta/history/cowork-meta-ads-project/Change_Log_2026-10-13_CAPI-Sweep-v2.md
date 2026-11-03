# Change log — 13 Oct 2026 — CRM → Meta CAPI sweep v2 (WhatsApp + leak fix)

**Approval:** Sanjeev, 16:5x, AskUserQuestion answer "Yes, apply all".

The change:
- the sweep also sends WhatsApp ad leads;
- it scans the 600 most recently modified leads (was 100);
- it labels each event with its lead source.

To clear the backlog, the waiting leads were re-saved once with no workflows, and the sweep was run twice by hand.

Source of the problem: the diagnosis `SIB-04_Diagnosis_2026-10-13_Placement-Quality-CAPI-Assignment.md` §3.

**Schedule correction (found 17:20):** the schedule "SIB CAPI Sweep - Hourly" actually runs **every 2 hours** (frequency hourly, repeating_period 2; runs at even hours; last 16:00, next 18:00). It has run this way since 9 Jul, although the description and older notes say "hourly". Not changed.

## Before

- `sib_capisweep` (id 1123581000915255380) sent only `Advt - Facebook` / `Advt - Instagram`. Code v1 (9 Jul 2026) is saved as `Meta Ads/sib_capisweep_v1_2026-07-09.deluge.txt`.
- The sweep read only the 100 most recently modified leads, which leaked: 121 leads were modified between 12:11 and 13:00 today, and 232 between 15:00 and 16:00. Runs are 2 hours apart, so a graded lead was usually pushed out of the window before the next run.
- **Backlog at 16:55 IST** (paid leads created since 6 Oct, valid or progressed, Meta_CAPI_Sent = false): 34 in total:
  - 32 Advt - WhatsApp;
  - 1 Advt - Facebook (Vinod Kumar …517382);
  - 1 Advt - Instagram (CA Shailesh Gupta …613248).

## Changes

| # | Time (IST) | Item | Change | Verified |
|---|---|---|---|---|
| K1 | 16:59 | `sib_capisweep` code → **v2** (file `Meta Ads/sib_capisweep_v2_2026-10-13.deluge.txt`) | (a) srcSet adds **"Advt - WhatsApp"**. (b) The scan reads up to 3 pages × 200, sorted Modified_Time desc, so **600 leads** (was 1 × 100). (c) Each event carries `custom_data.lead_source` = the lead's Lead_Source. Unchanged: event logic (QualifiedLead / ValidLead), match keys (lead_id + hashed em/ph), event_id `<leadId>-<event>`, cap of 20 events per run, marking Meta_CAPI_Sent with trigger []. Integration calls per run ≤ 24 (1 org variable + ≤ 3 getRecords + ≤ 20 updateRecord). Commit message "v2 13 Oct: add Advt - WhatsApp, scan 600 recent leads, lead_source in custom_data". | IDE: saved, 0 errors, "Last modified … just now". The CodeMirror value equalled the v2 file exactly before saving (3,549 chars). |
| K2 | 17:00:33 – 17:00:44 | Backlog touch | 34 leads re-saved with `Meta_CAPI_Sent = false` and **trigger []**, so their Modified_Time moved into the sweep window. No field values changed and no workflows ran. One test record first (…564125), then 33. | All 34 returned SUCCESS; Modified_Time 17:00:33 / 17:00:44 |
| K3 | 17:01 | Manual run 1 | Scanned 600; sent 20 → `events_received: 20`, messages [] (custom_data accepted without warnings), fbtrace ApWKOcewjgGwH7xPN55j3Ek; 20 marked sent | IDE console |
| K4 | 17:02 | Manual run 2 | Scanned 600; sent 16 → `events_received: 16`, messages [], fbtrace AXF9wLYfdrrk6NYqMgzwNw4; 16 marked sent | IDE console |

**Result:** 36 leads marked Meta_CAPI_Sent = true at 17:01–17:02.

| Lead source | Count | Notes |
|---|---|---|
| Advt - WhatsApp | 32 | |
| Advt - Facebook | 3 | Vinod Kumar, plus 2 older unsent valid leads that were in the 600 window: Ishu Parashar Mishra …662051 (created 30 May, Proposal Sent) and Gkmahesh Gk …123062 (created 22 Sep) |
| Advt - Instagram | 1 | |

Events sent: 31 ValidLead and 5 QualifiedLead. The QualifiedLead (Proposal Sent) leads were Ishu, ASHISHGOYAL, Chandra Prakash Singh, Shrinivas Chitmilwar and NAYAN DEWANGAN. The re-check query for the backlog (since 6 Oct) now returns **0**.

## Deliberately not changed

- **Rule 1 "Meta CAPI - ValidLead"** (criteria Advt - Facebook / Advt - Instagram) was left as is. Its function does not mark Meta_CAPI_Sent. Adding WhatsApp to it could double-send events that the sweep also sends.
- **WhatsApp "business_messaging" events with ctwa_clid:** not possible yet. CTWA_Click_ID is empty on all WhatsApp leads because SalesIQ does not pass the click ID to the bot. So WhatsApp events go as `system_generated`, matched on hashed phone (and email when present). They count in the dataset (1242417817083521) for measurement and future optimisation. The CTWA ad set itself still optimises for conversations.
- **The schedule** stays at every 2 hours.

## Rollback

Open `sib_capisweep` in the IDE, then either:
- Revisions → restore the 9 Jul version, or
- paste `sib_capisweep_v1_2026-07-09.deluge.txt` and Save.

Leads already marked sent stay marked. Meta de-duplicates repeats by event_id.

## Watch

- The 18:00 scheduled run is the first unattended v2 run. It should log "scanning 600" and send only newly graded leads.
- Coverage: runs are 2 hours apart and a run sees the 600 most recently modified leads. At about 120–230 lead edits per hour, 600 covers the gap with some margin. If edits pass about 300 per hour, a grading could still drop out of the window. If that happens, either:
  - set the schedule to every hour, or
  - raise the scan to 4 pages and lower the cap to 19.
- Dataset stats are privacy-rounded and can lag by about 30 minutes. Read ValidLead and QualifiedLead with plain `aggregation:event`; the SERVER_ONLY filter is unreliable (see the operator memory).
