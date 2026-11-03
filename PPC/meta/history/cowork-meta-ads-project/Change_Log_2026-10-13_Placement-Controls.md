# Change log — 13 Oct 2026 — account-level placement exclusions

Approved by Sanjeev in chat (12:23 IST): "Yes change whatsapp as set to ccfs placement and form ad set too". He chose the option "Account-level exclusions".
Executed by Claude in Ads Manager › Advertising settings › Placement controls, ad account SETINDIABIZ 152154124583473, about 12:30 IST.

## What changed

| | Before | After |
|---|---|---|
| Account placement controls | Toggle off ("Not defined") | 4 exclusions saved ("Defined") |
| Audience Network native, banner, interstitial | allowed | excluded |
| Audience Network rewarded videos | allowed | excluded |
| Facebook Marketplace | allowed | excluded |
| Facebook right column | allowed | excluded |

**Scope.** This is an account-wide setting. It applies to every current and future campaign in 152154124583473, including SIB-05 when it launches and any paused campaign that is reactivated.

Ad set targeting specs are unchanged: no budget, audience, creative, status or bid edits were made. No learning reset was triggered by an ad-set edit.

## Why

From 9 to 13 Oct, the CTWA ad set spent ₹1,878 (14.8%) on Audience Network. That spend bought 45 "conversations" at ₹42 each. AN classic CTR was 6.9%, against 2.1% on FB Feed, which is the signature of accidental taps. Four of the 7 tagged WhatsApp losses were "Inquired by Mistake". Full analysis: `SIB-04_Diagnosis_2026-10-13_Placement-Quality-CAPI-Assignment.md` §1.

## Read-back (13 Oct 12:34 IST, Meta connector)

- Both ad sets are ACTIVE, and `ads_get_errors` shows no delivery errors on the campaign or either ad set.
- The ad set targeting still lists `audience_network` and `marketplace` in its effective positions. This is expected: account controls are applied at delivery, not written into the ad set spec. Meta says changes reach running campaigns within minutes, up to 48 h.
- Proof will come from delivery data. Snapshot of today's spend up to 12:34, almost all of it before the change:

| Placement | CTWA spend today | Form spend today |
|---|---|---|
| Audience Network, classic | ₹389.71 | — |
| Audience Network, rewarded video | ₹21.49 | — |
| FB Marketplace | ₹1.22 | — |
| Total ad set spend today | ₹1,195.32 (AN 34.4%) | ₹391.56 |

**Pass test:** AN and Marketplace spend for today should stop growing past ₹411.20 and ₹1.22. From 14 Oct onward, AN and Marketplace should show ₹0.

## Propagation check (13 Oct 18:31 IST, scheduled task, read-only)

Source: Meta connector, today's spend by publisher_platform + platform_position for both ad sets.

| CTWA ad set, today | 12:34 snapshot | 18:31 | Change |
|---|---|---|---|
| Audience Network, classic | ₹389.71 | ₹401.44 | +₹11.73 |
| Audience Network, rewarded video | ₹21.49 | ₹21.48 | ₹0 |
| **Audience Network total** | **₹411.20** | **₹422.92** | **+₹11.72** |
| FB Marketplace | ₹1.22 | ₹1.22 | ₹0 |
| Ad set total | ₹1,195.32 | ₹2,357.18 | +₹1,161.86 |

**Result: mostly passed, but not clean.**
- Marketplace stopped.
- Audience Network took ₹11.72 of the ₹1,161.86 spent since 12:34. That is 1.0% of new spend, against 34.4% before the change.
- The connector returns nothing for a platform × hour breakdown, so the timing of the ₹11.72 can't be shown. The most likely cause is propagation lag (Meta says minutes up to 48 h).

**Other checks**
- Form ad set: no Audience Network or Marketplace spend today (total ₹1,437.44).
- Both ad sets are ACTIVE; `ads_get_errors` returns no errors.
- Other non-CCFS spend in CTWA today: ₹292.70 (12.4%). This is mainly FB in-stream (₹195.83) and Reels overlay (₹87.78), plus Search, Notifications, profile feed, Threads and WhatsApp Status. These are expected (see below).

**Next**
- Full-day 14 Oct: Audience Network and Marketplace should be ₹0.
- If Audience Network is above ₹0 on 14 Oct, open Advertising settings › Placement controls and confirm the 4 exclusions still show "Defined". No other change.

**Process note:** the first breakdown call was blocked by the session's permission check (it carried the original change request as its label). It was retried once as a read-only lookup and ran. No Meta changes were made.

## Still outside CCFS (no available control can exclude these)

**CTWA ad set:** WhatsApp Status, Threads, FB in-stream video, Reels overlay, Search, Notifications, FB profile feed, IG Explore and IG profile feed.
- Today these took ₹174.35 (14.6%), mostly in-stream: ₹129.52, 1,721 impressions, CTR 0.64%.

**Form ad set:** in-stream, Search, Notifications, Reels overlay, profile feed, biz discovery, IG Explore, IG profile feed and IG search. These were 2.8% of spend from 9 to 13 Oct.

**Options to close the gap**, not to be applied until the 3-day read is in:
- **(a) Placement value rules.** These can down-weight positions but cannot exclude them. The existing rule set "Website 20% up form 30% down rule" is attached to 0 active ad sets.
- **(b) API targeting update to exact CCFS positions.** This sets FB feed/story/reels and IG stream/story/reels on mobile and desktop.
  - The API pauses the ad set, and the hard rule is that only Sanjeev reactivates it, in Ads Manager.
  - It also resets learning.

## Stop-loss

**Window:** 14–16 Oct (3 full days). Review on 17 Oct morning.

**Measure:** cost per CRM valid lead for each ad set. Spend comes from the connector. Valid leads come from Zoho:
- CTWA: count both "Advt - WhatsApp" and untagged "Self - Web Chat" leads that have a "Tiya - Annual Filings" chat, the same method as the baseline.
- Form: count "Advt - Facebook" and "Advt - Instagram" leads tagged FB-ACR.

**Baseline (9–13 Oct, early, 70+ leads still unworked):**

| Ad set | Spend | Valid leads | Cost per valid | Revert threshold (+25%) |
|---|---|---|---|---|
| CTWA | ₹12,703 | 24 | ₹529 | ₹662 |
| Form | ₹7,770 | 4 | ₹1,943 | ₹2,428 |
| Campaign | ₹20,473 | 28 | ₹731 | ₹914 |

**Revert:** turn Placement controls back off (toggle) in Advertising settings if the 3-day CTWA or campaign cost per valid lead exceeds its threshold.

**Expected and not a trigger:** Meta's cost per conversation will rise, because ₹42 AN conversations are gone. Judge on CRM valid leads, never on Meta conversations.

## Related decisions taken in the same session (not yet executed)

**LG-11 assignment fix.** Sanjeev said "LG11 would work" and approved "Yes, build it". The build waits until he has added 4 agents: Sudip Manna, Foziya Ansari, Himanshu Singh and Shubendu Banerjee.

Each new agent must be added in two places:
- the CRM rule "PPC - SIB-04 Annual Filings - LG-11" (1123581000945354238);
- the SalesIQ department "Sales - CACS ACR" (61466000026678128).

Build scope:
1. Move the sib_wa_lead plug call to the first card of Zobot "Tiya - Annual Filings", with adcode ACR.
2. Stop the "Lead Assignment = Auto" → AssignOwner re-run on chat leads.
3. Backfill the 83 untagged leads to Advt - WhatsApp with trigger [], after a dry-run and Sanjeev's approval.
4. Test on one chat before switching on.

**Still proposed (not approved):**
- Stop the duplicate detector from parking leads on the admin account.
- CAPI fixes: add WhatsApp to the sweep and Rule 1, search on Meta_CAPI_Sent = false, and map ctwa_clid.
- Add Advt - WhatsApp to the watchdog and scorecard filters.
