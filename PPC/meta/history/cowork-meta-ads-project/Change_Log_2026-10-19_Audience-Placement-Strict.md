# Change log: 19 Oct 2026, strict audience and placement rework

**Ask (Sanjeev, 13:31):** "rework on audience and plateforms … very strict … so that the money is not wasted on junk."
**Audit:** `Meta Ads/Audience_Placement_Audit_2026-10-19.md` (read-only evidence, scores, options).

## Decisions (Sanjeev, ~14:10 IST, AskUserQuestion)

| # | Question | Answer |
|---|---|---|
| D32 | SIB-05 audience model | **A: Advantage+ audience OFF, job titles hard** |
| D33 | SIB-05 countries | **Keep all 7** (US, AE, SG, KR, JP, AU, CA), location type **home only** |
| D34 | SIB-05 gender | **All genders** |
| D35 | What to stage now | **SIB-05 strict spec (all 3 ad sets) only.** SIB-02 Copy placements, exclusion X1 and X3–X5 planning were NOT approved today → not done |

## Staged (drafts only; nothing published; no live object changed)

Same targeting on all three SIB-05 ad sets (campaign 120247067847480449), via connector `ads_update_entity`:

| Field | Before | After (staged) |
|---|---|---|
| Advantage+ audience | 1, `targeting_optimization: expansion_all`, individual_setting age 1 / gender 1 | **0**; no expansion_all |
| Location | 7 countries; home + recent (live) / + frequently_in (drafts) | 7 countries; **home only** |
| Age / gender | 25–65; gender suggestion | 25–65 hard; all genders |
| Languages | 6, 24, 11, 12 | unchanged |
| Detailed targeting | One OR-group of suggestions: CEO, Chairman, Owner, CFO, **Co Owner**, Owner and Founder, MD; BDM; SBO; Page admins; International business | **Hard, two groups (AND):** (1) Founder, Owner and Founder, CEO, MD, CFO, Owner, Partner, Managing Partner, Chairman, VP; **AND** (2) Small business owners OR Facebook Page admins OR Business Decision Makers. Co Owner and "International business" removed |
| Placements | Advantage+ (effective list incl. Audience Network, Marketplace, in-stream, search, notifications, profile feed, Explore) | **facebook + instagram only; FB feed, story, reels; IG stream, story, reels** |
| Device | mobile + desktop | unchanged |

Not changed: regulated-category entries (SINGAPORE_UNIVERSAL, AUSTRALIA_UNIVERSAL), CBO ₹4,000, forms, ads, schedule.

India Desk titles (Country Manager, Head of International, General Counsel, Finance Director, Head of Legal) were **not** added: the connector has no targeting-search tool to get their IDs. Sanjeev can add them by name in Ads Manager (group 1) before publishing.

## Read-back (connector, object_state=draft, ~14:15 IST)

| Ad set | Targeting stored | Validation |
|---|---|---|
| India Entry 120247067863750449 (live PAUSED, modify draft) | ✔ exact | **VALIDATED, 0 errors** |
| Subsidiary 120247068431610449 (add draft) | ✔ exact | **HAS_ERRORS: 1815089 "Terms of Service Not Accepted"** |
| Branch-Liaison 120247068705380449 (add draft) | ✔ exact | **HAS_ERRORS: 1815089** |

The 1815089 flag appeared **after my API edit**; both drafts were VALIDATED before it. It is the same API-only lead-terms quirk seen since July (Ads Manager UI writes do not raise it; the Page shows "Accepted" at /ads/leadgen/tos). **Fix before publish (Sanjeev, Ads Manager):** open each of the two ad sets, check the audience shows the values above, click into any field and save, so Ads Manager re-validates under your session. Do not retry through the API.

## Stop-losses (SIB-05, logged before launch)

- Capture stop: 2 spend days with 0 CRM leads → pause (spec §8, unchanged).
- **Under-delivery:** spend < 50% of the ₹4,000 CBO on 2 consecutive days → recommend removing detailed-targeting group 2 (keep titles hard). Reason: titles AND decision-maker behaviours across 7 countries may be a small audience.
- Junk > 40% of worked over 3 days → pause; ≤ 25% → keep.
- Day 7: country split (watch AE, JP, KR separately); day 30 go/no-go (D31).

## Automation updated

Scheduled task "Meta lead-quality watch (daily)" (trig_01DPT99ZCoF8rictq4EsC2bP, 09:40 IST) step 3 replaced with the **strict guardrail audit**: locales, age_min, location type / geo expansion, Advantage+ audience and expansion_all reversion check, placement whitelist + 7-day off-whitelist spend % (FLAG > 2%, BREACH on Audience Network / Marketplace / Threads), exclusion status; plus the SIB-05 stop-losses above. Ad set IDs refreshed (SIB-02 Copy, SIB-05).

## Ads Manager pass, Chrome on the HP laptop (~14:30–14:50 IST; Sanjeev: "take chrome control … do the needful")

**Done**
- Subsidiary 120247068431610449 and Branch-Liaison 120247068705380449: re-selected the same Page (Setindiabiz Private Limited 627814417091714) in Conversion → **error 1815089 cleared on both**, "All edits saved". The UI also states "You've accepted Meta's Lead Ads Terms for this Page."
- Ad S1 (120247068431620449): opening it cleared its "incomplete" mark. Lead-nurturing **Chat on Messenger unticked** (spec D22).

**Not done / needs Sanjeev**
- S1 **Chat on Instagram is still ticked** (spec D22 = untick). My click was blocked by a permission check; untick it by hand.
- After the Page re-select, **S2, B1, B2 show "This ad is incomplete – 2 fields"**. Opening S1 cleared it there, so it is likely the editor re-loading the creative. Open each of S2, B1, B2, wait for "All edits saved", and check: media present (4:5 + 9:16), form = SIB-05 India Entry Form v2, follow-up channels = WhatsApp only, AI disclosure as D30. E1/E2 untouched.
- India Desk titles not added (stopped before any ad-set audience edit; see finding 1).

**Findings that change the SIB-05 plan (from Meta's own editor)**
1. **Detailed targeting cannot be hard on this campaign.** The editor states: "Detailed targeting inclusions are always suggestions with the campaign settings you've selected." It shows the titles block as "Your suggestion". So D32 (titles hard) is **not achievable** with Instant forms + Maximise leads; the titles AND decision-maker groups will steer, not limit. Real hard levers left: countries, age 25+ (shown hard: "Use as a suggestion" unticked), languages (EN-US, EN-UK, JA, KO), placements, and custom-audience exclusions.
2. **"Home only" is not kept.** The editor notice: duplicate ad sets "will be updated to reach people living in or recently in the locations you select. The other location targeting options have been removed." Expect location type to come back as home + recent after publish.
3. **Ad-set placement exclusions are being withdrawn.** Placements show Advantage+ off (manual FB/IG Feed, Stories, Reels — as staged), but Meta notes "Excluding placements or platforms will no longer be available for your ad sets", pointing to placement value rules, per-placement creative and **account-level placement controls**. Long-term placement strictness has to live in Account controls.
4. Audience estimate shown on Subsidiary: 1.1–1.3 M ("broad"), so under-delivery risk from the second group is low.

## Incident 14:00 IST: Subsidiary + S1 published with wrong targeting and an empty ad

- **Cause (my action):** re-selecting the Page on Subsidiary and Branch-Liaison (to clear 1815089) **reset the creatives of their child ads.** S2 120247068431630449, B1 120247068705360449 and B2 120247068705370449 are drafts with an empty creative (Page + Instagram only, CTA "Sign up", no text, image or form; error 3390001 "Missing Lead Form"). S1 was in the same state.
- **Publish at 14:00:59 IST** (from the S1 editor's Publish button; not clicked by Claude) sent live:
  - Ad set Subsidiary 120247068431610449: PAUSED, ₹0, **targeting country = IN only** (the 7 countries were lost), regional SG/AU declarations dropped. Placements, A+A 0, titles, locales were kept.
  - Ad S1 120247068431620449: PAUSED, PENDING_REVIEW, ₹0, **creative 1130585629367155 is empty** (body "", title " ", CTA SIGN_UP, no image, no form).
- **Fixed (draft, connector, 14:10):** Subsidiary targeting back to US, AE, SG, KR, JP, AU, CA (home + recent), strict spec otherwise unchanged; regional_regulated_categories SINGAPORE_UNIVERSAL + AUSTRALIA_UNIVERSAL and SG identities re-added. Read back: 0 errors.
- **Still broken:** S1, S2, B1, B2 creatives must be rebuilt (copy word for word from G12 build sheet §4, images p3–p6 4:5 + 9:16, form v2 1741840353557832, CTA Get quote, enhancements off, AI disclosure on, follow-up WhatsApp only). E1 and E2 are intact.
- **Do not click "Review and publish (11)"**: it would publish the 3 empty ads, plus the TM-C1 and INC-C1 click-to-WhatsApp draft ads (toggles ON).
- Lesson: never change the Page on an ad set that has ads; it wipes the ads' creatives.

## Creative rebuild in Chrome (Sanjeev: "yes", ~14:20–14:42 IST; unpublished editor edits)

- S1, S2, B1 rebuilt (text per G12 build sheet §4, form v2, Get quote, WhatsApp-only follow-up, enhancements/translation off, related media and AI versions removed, AI disclosure on). S2 has 4:5 only (no 9:16 exists).
- B2: placements/follow-up/form v2 set; creative not yet saved. Session stopped at Sanjeev's request ("start a new session"). Resume: `Meta Ads/SIB-05_Creative_Rebuild_Resume_Prompt_2026-10-19.md`.
- Nothing published by Claude.

## Still open (need Sanjeev's go)

1. SIB-02 Copy: placements → FB/IG Feed, Stories, Reels (then geo expansion off). Stop-loss in audit §6.
2. Exclusion audience X1 (instant-form submitters 180d, no upload) → attach to form ad sets.
3. X3–X5 CRM upload lists (leads 180d, customers 540d, staff + junk numbers): DPDP Act 2023 check (ss.5, 6, 8) first; decide whether SIB-04 excludes existing clients.
4. Before SIB-05 publish: fix the two drafts (above), fund the account (≈ ₹15.8k left ≈ 1.3 days with SIB-05 on), set 30-day end date, then read back targeting after publish.
