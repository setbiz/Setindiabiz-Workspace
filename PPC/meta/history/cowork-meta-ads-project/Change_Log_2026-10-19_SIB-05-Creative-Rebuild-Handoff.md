# Change log: 19 Oct 2026 (session 2, ~14:47–16:30 IST), SIB-05 B2 rebuild, draft repairs, publish, end date

Continues `Meta Ads/Change_Log_2026-10-19_Audience-Placement-Strict.md` (read its Incident section first). Resume prompt used: `Meta Ads/SIB-05_Creative_Rebuild_Resume_Prompt_2026-10-19.md`. **Nothing published by Claude; Sanjeev published.**

## Done (Ads Manager in Sanjeev's Chrome unless noted)

| Object | What changed | Read-back (connector, object_state=draft) |
|---|---|---|
| Ad B2 120247068705370449 | Creative built: 4:5 `42bae5474a58a69980aea4acd19c632f` + uploaded 9:16 `353f3468d7e2276c84ffcf6b556b9754`; B2 text word for word (G12 build sheet §4); CTA Get quote; form v2 1741840353557832; enhancements and translation off; related media removed; AI vertical/square versions removed (square = plain padding); AI disclosure ticked (D30). Rebuilding the creative re-ticked Messenger + Instagram follow-up → **unticked** (WhatsApp only, D22) | ✔ exact, 0 errors (later overwritten, see below) |
| Ad set Branch-Liaison 120247068705380449 | **Was staged as India only** (the Page re-select had wiped its 7 countries too; not in the resume note). Restored US, AE, SG, KR, JP, AU, CA one by one (bulk add matched extra territories, abandoned before saving). Singapore advertiser re-selected (field had emptied) | ✔ 7 countries, home + recent; SG identities 629080835992237; VALIDATED |
| Ad set India Entry 120247067863750449 | Publish error **1870194**: Meta no longer accepts "home only" and the editor has no location-type control. **Sanjeev approved one connector edit (AskUserQuestion, ~15:20)**: `location_types` → home + recent; every other targeting field carried unchanged. Editor reloaded after the API write (to avoid saving stale values), then Singapore advertiser re-selected (emptied by the location edits) | ✔ 7 countries, home + recent; SG identities; VALIDATED, **no 1815089** |
| S1, S2, B1 | Not touched this session | ✔ exact copy, form v2, GET_QUOTE, WhatsApp only, AI label, 0 errors |
| E1 120247067863760449 / E2 120247068331330449 | E1 opened only (editor: form v2, WhatsApp only) | 0 errors |

**D33 superseded:** "home only" is no longer a valid Meta option. All three SIB-05 ad sets are now home + recent.

## 15:34 IST: B2 overwritten again, rebuilt at 15:45

- Sanjeev asked "check, and why don't you use laptop hp big chrome". Check found SIB-05 **not yet published** (campaign PAUSED; all 9 items still drafts) and **B2 overwritten at 15:34 IST**: text, headline, description, CTA (back to Sign up), AI label and enhancement opt-outs gone; related media back; only images + form v2 kept. Cause unknown: Claude was on the campaigns table at the time. Possible causes: the ad set editor reload saving a stale copy of B2, or another open editor tab.
- Browser: Sanjeev used switch_browser and connected **"SK Big HP"**. It is the same Chrome Claude had been using all session ("Browser 1", deviceId 12ab3f67-c6a1-4115-8f56-85376adb99d1). "Browser 2" (621920c4…) is a different Windows Chrome connected since ~11:10 IST.
- Rebuilt B2 in SK Big HP via Change selections: text word for word, Get quote, form v2, enhancements 0/5 + 0/3, translation off, related media removed, AI vertical/square removed, AI disclosure ticked, Messenger + Instagram unticked.
- Read-back 15:45 IST: B2 VALIDATED, 0 errors, copy exact, GET_QUOTE, WhatsApp only, AI label OPT_IN. **Gap:** the uploaded 9:16 (`353f…`, clustered_variant) is **opt_out**. Stories/Reels fall back to the 4:5 with padding. In Customize media the vertical slot shows only the AI version, a crop and "Default padding applied" (checkbox locked), and "+" did nothing. Left as is.

## 15:55 IST check: partial publish

Campaign 120247067847480449 ACTIVE; ad sets India Entry and Subsidiary published ACTIVE (targeting correct); ads E1/S1 live but PAUSED with old creatives; Branch-Liaison + E2, S2, B1, B2 still drafts. No spend risk (all live ads paused).

## 16:00 IST check ("chech now"): SIB-05 fully published

Connector, live:

| Object | Live state |
|---|---|
| Campaign SIB-05 India Entry 120247067847480449 | ACTIVE |
| Ad sets India Entry 120247067863750449, Subsidiary 120247068431610449, Branch-Liaison 120247068705380449 | All ACTIVE. Each: US, JP, CA, SG, KR, AE, AU, home + recent; 25–65; locales 6/11/12/24; titles group AND decision-maker group; Advantage+ audience 0; FB feed/story/reels + IG stream/story/reels only; mobile + desktop. No end date at 16:00 (see next section) |
| Ads (all status PAUSED, effective IN_PROCESS = in review) | E1 creative 1724357761994854; E2 1663411985572031; S1 3934649513358828; S2 1704743077655068; B1 2144337016154094; B2 2146456619410623 |

- Live creatives read back (`ads_get_creatives`): body, title and description of all six match G12 build sheet §4 **word for word**; CTA GET_QUOTE on all six; 4:5 image hashes correct (E1 e1aa…, E2 eac8…, S1 7075…, S2 b92e…, B1 bca6…, B2 42ba…). S1's empty creative is replaced.
- Drafts left in the account: only SIB-02 TM WhatsApp ad set + TM-C1, and C1-INC WhatsApp ad set + INC-C1 (correctly not published; their ad toggles are ON).
- Spend: none yet (all SIB-05 ads paused and in review).

## ~16:30 IST: end date staged (Sanjeev: "end date 31 dec 2026 / i will topup this evening")

**D31 changed:** end date is **31 Dec 2026, 11:59 PM IST** (not 18 Nov). Set in the Ads Manager UI, one ad set at a time; nothing else edited.

| Ad set | Draft read-back (connector, object_state=draft) |
|---|---|
| India Entry 120247067863750449 | end_time null → 2026-12-31T23:59:00+0530; VALIDATED; 0 errors |
| Subsidiary 120247068431610449 | same; VALIDATED; 0 errors |
| Branch-Liaison 120247068705380449 | same; VALIDATED; 0 errors |

- The only change in each draft is end_time. Targeting, budget (CBO ₹4,000/day) and the ads are untouched.
- **Waiting on Sanjeev:** Review and publish → keep only these 3 SIB-05 ad-set edits, untick TM WhatsApp ad set + TM-C1 and C1-INC WhatsApp ad set + INC-C1. Claude then reads back live end_time.
- **Funding:** Sanjeev tops up this evening (human only). Ads stay PAUSED until funding is in and review clears.
- Stop-loss: if the end date causes any delivery error after publish, remove the end date (one edit) and re-read.

## 16:06 IST: end date published (Sanjeev)

- Live read-back: all three ad sets ACTIVE, end_time 2026-12-31T18:29:00Z (= 31 Dec 2026, 11:59 PM IST).
- All six SIB-05 ads: effective_status PAUSED (no longer IN_PROCESS, so review has finished; none disapproved).
- Drafts left: only TM WhatsApp ad set + TM-C1 and C1-INC WhatsApp ad set + INC-C1 (correctly not published).

## Still open

1. ~~Publish the 3 end-date edits~~ done 16:06.
2. **Funding:** ≈ ₹15.8k left ≈ 1.3 days with SIB-05 on. Sanjeev tops up this evening.
3. **Switch ads on** after review clears and funding is in (Sanjeev, or Claude with explicit approval). Watch first leads against the G9 checklist.
4. B2 9:16: add SIB-05_B2_9x16 to the vertical slot by hand, or accept padded 4:5 for Stories/Reels.
5. E1 has no "shared_messages" chat greeting (the other five ads have it). Low impact.
6. S2 has no 9:16 image (4:5 only).
7. Unchanged from the earlier log: SIB-02 Copy placements; exclusion X1; X3–X5 lists (DPDP Act 2023 ss.5, 6, 8 check first).

## Lessons

- Any location edit in the editor can blank the Singapore advertiser/payer declaration; re-check Ad transparency after.
- After a connector edit, reload the editor before touching the same ad set, or the stale page can save old values back.
- Rebuilding a creative resets lead-nurture channels to all-on; untick Messenger/Instagram every time.
- Never change the Page on an ad set that has ads (wipes creatives) — confirmed again: it also wiped Branch-Liaison's countries.
- Re-read every SIB-05 ad through the connector immediately before publishing; a draft can change between the last check and Publish.
- Publishing from the campaign row can publish the campaign and ad sets without their ads; check "Review and publish" lists every child item.
- The end-time field is segmented (hour / minute / AM-PM); typing the date alone leaves 12:00 AM, so set each segment and zoom to confirm.
