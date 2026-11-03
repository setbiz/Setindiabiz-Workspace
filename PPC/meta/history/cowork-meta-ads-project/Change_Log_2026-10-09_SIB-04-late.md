# Change log: SIB-04 publish attempt and LeadChain start (9 Oct 2026, 21:35–21:50 IST)

Follows `Change_Log_2026-10-09_SIB-04-night.md` (C34–C61). Account 152154124583473, campaign "SIB-04 Annual Filings" 120246968311680449.

## Sanjeev's instructions this block
- 21:35 "i wil login into crm and you setup lead chain and also ensure that all information is captured."
- 21:35 "published"
- 21:37 "fix problem, then publish, then do leadchain as some time is taken in approvals also and i have not added funds yet"
- 21:44 "will resume later"

## What Sanjeev published (his clicks in Ads Manager)
| Time (IST) | Object | State after |
|---|---|---|
| ~21:35 | Campaign 120246968311680449, ad set B "SIB-04 \| ACR \| Form \| IN" 120246968737470449, ad ACR-C2 \| Cost of delay \| Form 120246969544800449 | ACR-C2 Form IN_PROCESS at 21:36, **ACTIVE (approved) by ~21:48** |
| ~21:46 | ACR-C1 \| Deadline \| Form 120246969553500449 | IN_PROCESS (in review) |

All objects were switched On by Sanjeev before publishing (status ACTIVE). No funds on the account yet, so nothing can spend.

Still in draft ("Review and publish (7)"): ad set A "SIB-04 \| ACR \| CTWA \| IN" 120246968316940449, the 4 CTWA ads (ACR-C1 120246968790550449, ACR-C2 120246968981980449, ACR-C5 120246969045870449, LLP-C1 120246969168420449), LLP-C1 \| Form 120246969555870449, ACR-C5 \| Form 120246969554880449.

## The problem: CTWA ads can't publish
- "Review draft items" shows **Fix error** on all 4 CTWA ads. The ad editor says: "Select a Page for your ad set. For this ad, you must select a Page to represent your business for your ad set."
- Ad set A already has Page Setindiabiz Private Limited (draft promoted_object page_id 627814417091714, WhatsApp [phone redacted], page_whatsapp_number_id 1277691388770677). The connector's draft read shows 0 errors on every object.
- Likely cause: the campaign is live while ad set A is still a draft. Suggested fix (Sanjeev's clicks): in Review draft items, untick the 4 CTWA ads, publish ad set A (plus the 2 remaining Form ads), then reopen a CTWA ad; if the error is gone, publish the 4 CTWA ads.

## Changes and attempts
| # | Change | Before | After | Evidence |
|---|---|---|---|---|
| C62 | Ad set A › Conversion › Facebook Page: re-selected "Setindiabiz Private Limited" (same value) to try to clear the CTWA error | Setindiabiz selected | Setindiabiz selected ("All edits saved"); CTWA error unchanged | Screenshots of the selector and of the ad editor afterwards |
| — | Claude's click on **Publish** in the editor | — | **Blocked by the session permission check** (real-world transactions). Screen left ready; handed to Sanjeev at 21:41 | Tool denial |

## Checks done before publishing (read-only)
- **Media placements, all 8 ads: correct.** 1:1 image and video in Feeds, in-stream and Search; 9:16 image and video in Stories and Reels only.
- **Correction to earlier notes:** the ACR-C1 video IDs were swapped in the build notes and resume prompt. Video titles confirm **ACR-C1 1x1 = 1645062090557187** and **ACR-C1 9x16 = 1129840180007679**. The ads themselves were built correctly.
- **AI features:** none opted in except the AI-label self-disclosure on ACR-C5 \| Form (as decided). `generative_asset_spec` entries on each creative are Meta's processing records for the uploaded videos; image animation, standard enhancements, text optimisations and Advantage+ creative are all OPT_OUT.
- **Lead nurture:** the draft data for ACR-C1 \| Form and LLP-C1 \| Form still lists `b2p_messaging` (Messenger) and `chat_on_instagram` channels next to WhatsApp; ACR-C5 \| Form lists WhatsApp only. The editor shows "Instant form additional action(s) — Current action(s): Chat on WhatsApp" for ACR-C1 \| Form. **Check the live ACR-C1 \| Form and ACR-C2 \| Form** (form ending screen / messaging after submit) for Messenger or Instagram buttons.

## LeadChain (not started)
- CRM is logged in (Sanjeev Kumar) in tab "Setup Page - Zoho CRM". LeadChain is reached via **Setup › Marketplace › All › LeadChain** (direct URLs like /settings/marketplace give "Invalid URL").
- Pattern on recent LeadChain leads (COQL, 24 Sep): Lead_Source "Advt - Facebook"/"Advt - Instagram" by platform; Lead_Channel "Advt"; Tag per chain (FB-INCORP, FB-TMF); Product_Category per chain ("Start Company", "TM Filing in India"); Description holds the answer only (no question label); City only when the form asks; WhatsApp_Opt_In false and Opt_In_Time empty on all; Meta_Ad_Code empty.
- **Risk:** ACR-C2 \| Form is approved. Once funds are added, form leads will not reach Zoho until the SIB-04 chain exists (they stay in Meta's Leads Center). Create the chain before adding funds.

## Awaiting Sanjeev
1. Publish ad set A and the remaining ads (steps above); report whether the CTWA error clears.
2. Resume LeadChain with Claude before adding funds.
3. Flags still open from the night log: C5 CTWA AI label, "Chat on WhatsApp" pill on Form creatives, 9:16 safe zone, age-25 floor, video warning icon.
