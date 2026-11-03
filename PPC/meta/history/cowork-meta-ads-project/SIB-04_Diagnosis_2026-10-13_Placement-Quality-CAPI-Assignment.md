# SIB-04 diagnosis — 13 Oct 2026 (read-only, nothing changed)

Scope: campaign SIB-04 Annual Filings (120246968311680449), live since 9 Oct 21:35 IST. Spend to date ₹20,473 (Form ad set ₹7,770 · CTWA ad set ₹12,703). Data pulled 13 Oct ~12:00 IST from the Meta connector and Zoho CRM (COQL, timelines, notes). Cost figures are account/campaign level.

## 1. Placements vs #IND4 CCFS

CCFS ad set "C4 Adset - Director CCFS + Form" (manual placements): Facebook Feed, Stories, Reels · Instagram Feed, Stories, Reels · mobile + desktop.

| Ad set | Placement setting | Positions outside CCFS | Spend outside CCFS | Results outside CCFS |
|---|---|---|---|---|
| SIB-04 \| ACR \| CTWA \| IN (120246968316940449) | Advantage+ (no publisher_platforms set) | Audience Network classic + rewarded video, WhatsApp Status, Threads, FB in-stream, Marketplace, Search, Notifications, Reels overlay, profile feed, IG Explore, IG profile feed | ₹3,098 (24.4%) | 56 of 115 conversations (48.7%) |
| SIB-04 \| ACR \| Form \| IN (120246968737470449) | FB + IG selected, positions automatic | FB in-stream, Marketplace, Search, Notifications, Reels overlay, profile feed, biz discovery feed, IG Explore, IG profile feed, IG search | ₹220 (2.8%) | 0 of 22 leads |

Audience Network alone: ₹1,878 (14.8% of CTWA spend) bought 45 "conversations" (39%) at ₹42; AN classic CTR 6.9% vs FB Feed 2.1% — accidental-tap signature. Tagged WhatsApp losses: 4 of 7 "Inquired by Mistake"; Siddharth Das (1123581000946586516) told Sudip he tapped by mistake.

Matching CCFS exactly = set publisher_platforms [facebook, instagram], facebook_positions [feed, story, facebook_reels], instagram_positions [stream, story, reels], device_platforms [mobile, desktop]. Not applied: needs Sanjeev's approval; resets learning; API route force-pauses the ad set and re-activation via API is off-limits (hard rule) → do it in Ads Manager.

Not placements but also different from CCFS: CCFS = male only, age 21–55 suggestion, 19 cities (25 mi), English locales, 6 Director lists, Advantage audience OFF. SIB-04 = all India, 18–65, 15 lists incl. LLP + LAL, Advantage audience ON.

## 2. Lead quality (CRM, created 9–13 Oct)

| Path | CRM records | Valid | Proposal sent | Lost | Establishing Contact | Untouched |
|---|---|---|---|---|---|---|
| Form (Advt - Facebook / Instagram) | 20 (Meta 22) | 4 | 0 | 0 | 9 | 7 |
| WhatsApp tagged "Advt - WhatsApp" | 38 | 12 | 3 | 7 | 18 | 1 |
| WhatsApp NOT tagged (still "Self - Web Chat", has a "Tiya - Annual Filings" chat) | 83 | 12 | 0 | 17 | 43 | 11 |

~121 new WhatsApp chat records vs Meta's 115 conversations started — the counts reconcile, but 69% of them are not in the paid segment. Campaign-level: 141 CRM records, 28 valid → ₹731 per valid (early; 70+ still unworked/establishing).

## 3. CRM → Meta conversion flow

- Dataset 1242417817083521: server last fired 13 Oct 10:57 IST; Purchase events daily (deal path healthy); EMQ 4.6 (email+phone 100%, no fbc).
- Form leads: 3 of 4 valid SIB-04 form leads sent ValidLead (Meta_CAPI_Sent true: Ashish, Adil, James Jacob Thayil). CA Shailesh Gupta (IG, 1123581000946613248, valid 12 Oct 10:35) not yet sent; re-modified 13 Oct 12:11 so the next sweep should take it. 7 valid FB/IG leads modified since 9 Oct are unsent — the sweep's "100 most recently modified" window leaks.
- WhatsApp: 0 of 24 valid WhatsApp leads sent. Causes: (a) sib_capisweep srcSet and Rule 1 criteria accept only Advt - Facebook / Advt - Instagram; (b) 83 of 121 aren't tagged at all; (c) CTWA_Click_ID empty on all — the plug's clid input is unmapped in the bot. Meta's CAPI for business messaging needs action_source business_messaging, messaging_channel whatsapp and ctwa_clid (Meta developer docs, "Conversions API for Business Messaging").
- The CTWA ad set optimises for CONVERSATIONS, so Meta currently rewards AN accidental taps.

## 4. Lead owner vs chat owner — mechanism

1. SalesIQ's native CRM push creates every WhatsApp chat lead the moment the chat opens: Lead_Source "Chat" → "Self - Web Chat", owner = attender, or Pavneet Kaur for bot/missed chats.
2. The plug sib_wa_lead (claims the lead: Advt - WhatsApp, FB-ACR, product, LG-11 rule) is called only at Zobot card A04, after the Entity and Year answers. Visitors who don't answer are never claimed → 83 leads never reach the LG-11 rule.
3. Pavneet later sets Lead Assignment = Auto → workflow "Lead Assignemnt - Edits" → AssignOwner (general round robin), which does not know who holds the chat. Examples: Sarfaraz Shaikh 1123581000946442225 (chat Priyanka 13:50, lead → Tarun Kumar 14:10); Siddharth Das 1123581000946586516 (chat Sudip 21:19, lead → Tarun next morning); NAYAN DEWANGAN 1123581000946586254 (tagged; LG-11 default Pavneet off-hours, chat missed, AssignOwner → Priyam).
4. ~60 of ~130 SIB-04 chat records logged a missed chat (13 inside chat hours). Missed chats are picked up by Customer Support by design → chat with CS, lead with an RM.
5. Detect Duplicate Lead moves duplicates to Sanjeev's admin account: 7 SIB-04 records there (form: Asokanramakrishnan, Virendra Sharma, Jaswinder Ram; WhatsApp: SRIDHAR KUMAR KAMIDI, nayudu345, IIFA, Jaswinder Ram). Jaswinder Ram's form AND WhatsApp leads both sit on the admin account → nobody owns him.

Measured: of ~70 SIB-04 chats where a "X added a note in Zoho SalesIQ" note names the handler, 12 have a different lead owner (Sudip Manna 5, Priyanka 4, others 3). Missed chats with no note are not countable.

## 5. Proposed fixes (none applied — each needs Sanjeev's go)

1. Placement: CTWA ad set to CCFS placements (Ads Manager). Form ad set optional (2.8% outside). Stop-loss: revert if 3-day cost per CRM valid rises >25% vs pre-change.
2. Claim at chat start: call the plug on the bot's first card with adcode ACR (7 Oct decision: every chat on the ACR number is an ad chat), before the Entity question; hourly backstop claims any "Self - Web Chat" lead with a "Tiya - Annual Filings" note < 2 h old. Backfill the 83 to Advt - WhatsApp with trigger [].
3. One owner authority: pick (a) chat follows the LG-11 lead owner, or (b) lead follows the operator who answered. Stop AssignOwner re-runs on chat leads that already have a handler.
4. Duplicates: keep the first owner (don't move to admin) for Advt-* leads; merge form+WhatsApp pairs.
5. CAPI: add Advt - WhatsApp to sweep + Rule 1; switch the sweep to a search on Meta_CAPI_Sent = false instead of the 100-most-recent window; map ctwa_clid in the bot and send WhatsApp events as business_messaging.
6. Add Advt - WhatsApp to the watchdog/scorecard paid-segment filters.
