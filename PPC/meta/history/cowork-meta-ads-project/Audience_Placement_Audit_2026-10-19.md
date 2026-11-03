# Audience and placement audit: strict lens (19 Oct 2026, ~14:00 IST)

Account SETINDIABIZ 152154124583473. Read-only audit; **nothing in Meta was changed**. Evidence: Meta connector (targeting read-back, 14-day breakdowns 5–18 Oct by placement, age × gender and region; today 19 Oct for SIB-02 Copy) joined to Zoho CRM (Leads, Lead_Source 'Advt - Facebook' / 'Advt - Instagram', created 5–19 Oct, grouped by Meta_Ad_Set). Ask (Sanjeev, 19 Oct 13:31): be very strict on audience and platforms so money is not wasted on junk.

Definitions (same as the watch log): **junk** = Lost with Why_Disqualified in Inquired by Mistake / Wrong Info / Language Issue / No Product Offering / Not Eligible / Bot Created-Spam. **Valid** = Lead_Status Valid Lead / Proposal Sent / Negotiation / Payment Pending. **Unworked** = Establishing Contact or blank. Percentages are of all CRM leads in the cohort. WhatsApp leads carry no Meta_Ad_Set, so Directors WhatsApp quality comes from the watch log.

## 1. Bottom line

1. **The live ad sets are not where money is leaking now.** CRM junk on the four live ad sets is 1–7% (WhatsApp 17% on 12 leads). Spend outside FB/IG Feed, Stories and Reels is **0.3–0.6%** of spend (₹1–₹77 per ad set over 14 days). Region delivery stays inside the city radii. The junk machine was Advantage+ audience plus one-tap WhatsApp on an open audience; that was switched off on 16 Oct (old open SIB-04 Form: **33% junk, 29% valid** on 58 leads, against 7% / 33% on the Directors rebuild).
2. **The two real gaps are:**
   - **No ad set excludes anyone.** The account has **no exclusion audience at all** (no CRM leads, customers, staff or junk-number list). Exclusions are hard even under Advantage+ audience, so this is the cheapest strictness win. Evidence it costs money: 6 of 7 WhatsApp leads on 18 Oct were flagged "Duplicate Record".
   - **SIB-05 India Entry is the loosest object in the account** and is about to take ₹4,000/day: Advantage+ audience with `expansion_all`, every title a suggestion (incl. the mistaken "Co Owner"), "recently in" + "frequently in" location types, all genders as a suggestion, and Advantage+ placements whose effective list **includes Audience Network and Marketplace** despite the 13 Oct account-level exclusions.
3. **Do not rebuild #IND1 or SIB-02.** They are the cheapest valid-lead sources in the account (#IND1 ≈ ₹414 per valid, SIB-02 ≈ ₹205 per valid, 14 days). Strictness there = small guard-rails, one at a time, with a stop-loss.

## 2. Meta's rules this audit relies on (checked today in Meta's Help Centre via the connector)

| Rule | Source |
|---|---|
| Under Advantage+ audience only **location, minimum age, language and custom-audience exclusions** are controls; age range, gender, detailed targeting and custom-audience inclusions are suggestions. Custom-audience exclusions "are always set as controls even if use as a suggestion is checked". | [Choose audience settings in Advantage+ campaigns](https://www.facebook.com/business/help/25941857932125812) |
| With "Further limit the reach", detailed targeting becomes a hard control if Advantage+ detailed targeting is unticked. **Advantage+ detailed targeting is forced (no opt-out) only for link clicks, landing page views, conversations, conversions, app events/installs and value** — instant-form LEAD_GENERATION is not in that list, so hard detailed targeting is possible for SIB-05. Detailed targeting is not available for click-to-WhatsApp ads. | [Use detailed targeting](https://www.facebook.com/business/help/440167386536513) |
| Manual placements for Leads: untick placements under Placement controls; **"Allow limited spend to excluded placements" lets up to 5% per excluded placement leak — must be OFF.** Excluding any placement turns Advantage+ placements off. | [Choose ad placements](https://www.facebook.com/business/help/175741192481247) |
| Account controls (placements: Audience Network, Marketplace, right column) apply to all auction campaigns; changes "may take up to 48 hours". | [Set audience and placement controls for your ad account](https://www.facebook.com/business/help/1438478636941047) |
| Help Centre no longer describes detailed-targeting **exclusions** (e.g. "Expats – India"); only custom-audience exclusions are documented. Treat expat exclusion as unavailable unless Ads Manager shows the option. | Same articles; consistent with the 31 Mar 2025 removal noted on 16 Oct |

## 3. Per ad set

Score 0–3 per lever (3 = strict, hard, no leak; 0 = open). Spend = 5–18 Oct unless stated.

### 3.1 SIB-04 Directors WhatsApp — 120247072309210449 (₹2,000/day, ACTIVE)

| Lever | Setting (read-back) | Hard / suggestion | Leak evidence | Score | Strict recommendation |
|---|---|---|---|---|---|
| Audience | 7 Company Director lists; A+A 0; relaxation lookalike 0 / custom 0 | Hard | — | 3 | Keep |
| Location | 19 cities @ 25 mi; home, recent, **frequently_in** | Hard | TN ₹4.68 (Hosur, inside Bangalore radius) | 3 | Drop `frequently_in` only when next editing for another reason |
| Age / gender | Male 25–60 | Hard | All spend male 25–64 | 3 | Keep |
| Language | EN-US 6, EN-UK 24 | Hard | — | 3 | Keep |
| Placements | FB feed/story/reels, IG stream/story/reels | Manual | ₹0 outside; ₹3,913, 13 conversations | 3 | Keep |
| Exclusions | None | — | 6/7 WA leads on 18 Oct = duplicates | 0 | Add exclusion audiences (§4) |

CRM (watch log, 17–18 Oct): 12 leads, 2 junk (17%). Stop-loss read on 23 Oct stands.

### 3.2 SIB-04 Directors Form — 120247072301790449 (₹2,500/day, ACTIVE)

| Lever | Setting | Hard / suggestion | Leak evidence | Score | Recommendation |
|---|---|---|---|---|---|
| Audience | 7 Director lists; A+A 0; relax 0/0 | Hard | — | 3 | Keep |
| Location | 19 cities @ 25 mi; home, recent | Hard | TN ₹9.51 (Hosur) | 3 | Keep |
| Age / gender | Male 25–60 | Hard | — | 3 | Keep |
| Language | 6, 24 | Hard | — | 3 | Keep |
| Placements | Same six positions | Manual | ₹0 outside of ₹6,393 | 3 | Keep |
| Exclusions | None | — | Meta 19 leads vs CRM 15 (see deletion finding) | 0 | Add exclusion audiences (§4) |

CRM 16–19 Oct: 15 leads · junk 1 (7%, "Inquired by Mistake") · Pricing 1 · valid 5 (33%) · unworked 8 (53%) · ≈ ₹1,279 per valid (falls as leads get worked).

### 3.3 #IND1 C1 24Hr INSA — 120240912969640449 (₹2,500/day, ACTIVE)

| Lever | Setting | Hard / suggestion | Leak evidence | Score | Recommendation |
|---|---|---|---|---|---|
| Audience | A+A 1; 17 interests, 2 titles, Small business owners, Business Decision Makers, 4 education statuses | **Suggestions** | Junk 1.4% — no sign of drift yet | 1 | Leave; revisit only if junk > 15% on 3 days |
| Location | 18 cities @ 25 mi; home, recent, frequently_in; `individual_setting.geo = 0` | Hard | Only target states; HP ₹41 / Punjab ₹129 = Chandigarh radius | 2 | Keep |
| Age / gender | age_min 25 hard; age_range 25–45 suggestion; all genders | Min hard, rest suggestion | Women ₹602 (4.3%, 1 lead); 65+ ₹510 (3.6%, 3 leads) | 1 | Leave — small and producing |
| Language | 6, 24 | Hard | — | 3 | Keep |
| Placements | Advantage+ (FB, IG, Threads; incl. in-stream, search, notifications, profile feed, overlay, Explore) | Auto | **₹76.75 of ₹14,086 = 0.54%** outside Feed/Stories/Reels; Reels = 84% of spend | 2 | Second in line (after SIB-02 read) |
| Exclusions | None | — | — | 0 | Add exclusion audiences (§4) |

CRM 5–19 Oct: 71 leads · junk 1 (1.4%, Wrong Info) · valid 34 (48%) · unworked 35 (49%) · ≈ ₹414 per valid.

### 3.4 SIB-02 Trademark — Copy — 120247094867020449 (₹1,200/day, ACTIVE since 19 Oct 03:06; replaces deleted 120247048085540449)

| Lever | Setting | Hard / suggestion | Leak evidence | Score | Recommendation |
|---|---|---|---|---|---|
| Audience | A+A 1; **`targeting_optimization: expansion_all`**; 31 interests (incl. Jewelry, Fashion design, Graphic design, LinkedIn), 15 titles (incl. Designer, Creative director, Angel investor), 2 behaviours, education | **Suggestions** | Original: junk 3.6% on 28 leads | 1 | Leave for now |
| Location | 30 cities @ 25 mi; home, recent, frequently_in; **`individual_setting.geo = 1` (location expansion ON)** | Expansion allowed | 17 Oct read: 0.4% radius spill; no visible widening | 1 | **Change 2:** geo expansion off |
| Age / gender | genders [male], age_range 25–55 — **both suggestions** (no `individual_setting` for gender) | Suggestion | Not measurable yet | 1 | Note only; making gender hard means A+A off |
| Language | 6, 24 | Hard | — | 3 | Keep |
| Placements | **Manually selected loose set**: FB feed, in-stream, story, search, reels, reels overlay, profile feed, notification; IG stream, story, reels, Explore, profile feed, search; **Threads** | Manual (explicit) | Original: ₹18.41 of ₹3,274 = 0.56%; Copy today: ₹1.45 of ₹482 | 1 | **Change 1:** FB + IG Feed, Stories, Reels only |
| Exclusions | None | — | — | 0 | §4 |

CRM: original 5–18 Oct 28 leads · junk 1 (3.6%) · valid 16 (57%) · ≈ ₹205 per valid. Copy today: 7 leads · 1 Lost "No Product Offering" · 2 valid.

### 3.5 SIB-05 India Entry — 120247067863750449 (live, PAUSED) + Subsidiary 120247068431610449 and Branch-Liaison 120247068705380449 (drafts); CBO ₹4,000/day

| Lever | Setting (live read + draft read) | Hard / suggestion | Risk | Score |
|---|---|---|---|---|
| Audience | A+A 1, `expansion_all`; titles CEO, Chairman, Owner, CFO, **Co Owner**, Owner and Founder, MD; Business Decision Makers; Small business owners; Page admins; International business | **All suggestions** | Optimiser finds the cheapest form-filler in 7 countries | 0 |
| Location | US, JP, CA, SG, KR, AE, AU; live: home + **recent**; drafts: home + recent + **frequently_in** | Hard countries, loose type | Travellers, incl. from India; diaspora/job-seekers in AE, SG, CA, AU, US | 1 |
| Age / gender | age_min 25 hard; `individual_setting age 1, gender 1` | Suggestions | — | 1 |
| Language | EN-US 6, EN-UK 24, JA 11, KO 12 | Hard | English includes Indian diaspora | 2 |
| Placements | Advantage+; **effective list includes Audience Network (classic, rewarded video) and FB Marketplace**, plus in-stream, search, notifications, profile feed, Explore | Auto | Account exclusion not reflected on this ad set | 0 |
| Exclusions | None | — | — | 0 |

No first-party list exists for foreign founders, so the Directors model cannot be copied. Decision options are in §5.

## 4. Exclusion audiences (account-wide; none exist today)

Custom audiences found: 7 Company Director lists, 7 LLP lists, 2 GST lists, lookalikes (mostly INACTIVE), 4 website-visitor audiences with only ~20 people (pixel signal is weak), FB/IG engager audiences INACTIVE. **None of CA_ALL_LEADS_180D, CA_CUSTOMERS_540D, CA_FORM_SUBMITTED_30D, CA_WHATSAPP_INITIATED_30D exists.**

Proposed (draft plan only; nothing created):

| # | Audience | Source | Upload needed? | Use |
|---|---|---|---|---|
| X1 | Instant-form submitters, 180 days | Meta engagement audience (Instant form → people who submitted) | No — Meta's own data | Exclude on every form ad set (stops paying twice for the same person) |
| X2 | Instant-form openers who did not submit, 30 days | Same | No | Optional exclusion on cold ad sets |
| X3 | All CRM Leads + Contacts, 180 days (phone/email, hashed by Meta) | Zoho export | **Yes** | Exclude on acquisition ad sets |
| X4 | Paying customers, 540 days | Zoho Accounts/Deals won | **Yes** | Exclude on acquisition ad sets. **Decision needed for SIB-04 ACR:** existing clients are the market for annual filings — exclude them (account managers handle) or not? |
| X5 | Staff and junk numbers (Lost: Inquired by Mistake, Wrong Info, Bot/Spam) | Zoho | **Yes** | Exclude everywhere |

X1/X2 can be created through the connector on your approval. X3–X5 are customer-list uploads: they need your OK and a privacy check under the Digital Personal Data Protection Act 2023 — notice and purpose (s.5), consent (s.6) and processor terms (s.8(2)) — against the current commencement position of the DPDP Rules 2025, and the privacy-policy wording issues already flagged on 10 Oct.

## 5. SIB-05 strict spec — options for Sanjeev

| Decision | Option A (strict) | Option B (tightened A+A) |
|---|---|---|
| Audience | **A+A OFF**, "Further limit": titles hard (Founder, CEO, MD, CFO, Owner, Partner, Managing Partner, Chairman, VP, + India Desk titles found by name), narrowed by Business Decision Makers / Page admins / Small business owners; Advantage+ detailed targeting **unticked** | A+A ON; titles stay suggestions (fix: remove Co Owner, add missing titles) |
| Location type | Home only | Home only |
| Exclusions | X1 + X3–X5 when built | Same |
| Placements | FB + IG Feed, Stories, Reels; limited-spend OFF | Same |
| Risk | Audience may be small per country → CBO starves some countries; CPL higher | Optimiser can still drift to cheap non-founders |

Open sub-decisions: UAE (keep / drop for first 30 days / own capped ad set), gender (all genders recommended — the male-only rule came from Indian Director data), Explore/IG profile placements.

Funding note: today's spend ₹3,980 by ~13:50; ≈ ₹15.8k left on paper (09:41 watch-log figure less today's later spend) → ~1.9 days at ₹8,200/day, **~1.3 days if SIB-05 adds ₹4,000/day**. Top-up is human-only.

## 6. Live ad sets — at most two changes, one at a time

| Order | Change | Ad set | Why first | Confirming metric / stop-loss |
|---|---|---|---|---|
| 1 | Placements → FB Feed, Stories, Reels + IG Feed, Stories, Reels; limited spend OFF | SIB-02 Copy | It is already in learning since 18 Oct, so the edit costs least now; it has the loosest explicit placement list (Threads, in-stream, search, notifications) | 3-day CRM read: **keep** if junk ≤ 25% of worked and valid % not lower than original SIB-02 (57%); **revert** if junk > 40% or spend < 50% of budget on all 3 days |
| 2 | Location expansion `geo` 1 → 0 (and drop frequently_in) | SIB-02 Copy | Removes the only "expand location" switch in the account | Same stop-loss, after change 1's read |
| later | Placements as in 1 | #IND1 | Only 0.54% leak; touch the best performer last | Same |
| account | Exclusion audiences X1 (then X3–X5) | All | Hard even under A+A | Duplicate-flagged leads ↓; junk not higher |

## 7. Publishing traps (unchanged)

Publish in Ads Manager sweeps all pending drafts (SIB-02 TM WhatsApp draft 120247099920320449 is PAUSED). Ads Manager silently reverted the Directors WhatsApp audience on 16 Oct — **read back targeting through the connector after every publish**. Claude never publishes.
