# Change log: SIB-05 India Entry, G12 build (16 Oct 2026, 18:00–19:10 IST)

**Result: G12 built and read back. Campaign, 3 ad sets and 6 ads exist as a draft in Ads Manager, all PAUSED. Nothing published, nothing activated, no money moved, no CRM writes.**

## Authority

- Sanjeev, 16 Oct 17:59: *"you build campain we will test later. for testing send email to vipin"*.
- This is the explicit go for G12. It changes the build sheet's order: G12 now comes **before** G9, and Vipin, not Sanjeev, runs the G9 tests (amends D27).
- G9 test steps were emailed to Vipin at 18:00 IST:
  - message 1a144b18c56deccf, thread 1a1359139e2d73dc;
  - to vipin.pathak@hatrotech.com, cc sanjeev@setindiabiz.com.

## Objects (account SETINDIABIZ 152154124583473, draft)

| Level | Name | ID | Status |
|---|---|---|---|
| Campaign | SIB-05 India Entry | 120247067847480449 | PAUSED |
| Ad set | SIB-05 \| India Entry \| Form \| INTL | 120247067863750449 | PAUSED |
| Ad | SIB-05 \| E1 \| India entry \| Form | 120247067863760449 | PAUSED |
| Ad | SIB-05 \| E2 \| Structures \| Form | 120247068331330449 | PAUSED |
| Ad set | SIB-05 \| Subsidiary \| Form \| INTL | 120247068431610449 | PAUSED |
| Ad | SIB-05 \| S1 \| From USD 499 \| Form | 120247068431620449 | PAUSED |
| Ad | SIB-05 \| S2 \| After incorporation \| Form | 120247068431630449 | PAUSED |
| Ad set | SIB-05 \| Branch-Liaison \| Form \| INTL | 120247068705380449 | PAUSED |
| Ad | SIB-05 \| B1 \| Liaison office \| Form | 120247068705360449 | PAUSED |
| Ad | SIB-05 \| B2 \| Branch office \| Form | 120247068705370449 | PAUSED |

The connector read-back (`object_state=draft`, 19:00 IST) returned all ten objects as VALIDATED with no active errors.

## Read-back against the build sheet

| Check | Result |
|---|---|
| Campaign | OUTCOME_LEADS, AUCTION, no special ad category, CBO ₹4,000 a day (400000), LOWEST_COST_WITHOUT_CAP ✔ |
| Optimisation | LEAD_GENERATION, instant form (ON_AD), Page 627814417091714 ✔ |
| Countries | US, AE, SG, KR, JP, AU, CA; living in or recently in; no location expansion ✔ |
| Age | age_min 25, hard control (`individual_setting.age = 1`) ✔ |
| Languages | locales [6, 11, 24, 12] = English (US), Japanese, English (UK), Korean ✔ |
| Advantage+ audience | On, with suggestions ✔ (see deviations for the suggestion list) |
| Placements | Advantage+ placements. Ads Manager shows **Platforms: Facebook and Instagram**, 15 placements, 0 excluded, on all three ad sets ✔ Account controls still exclude Audience Network, Facebook right column and Marketplace. Meta now says ad-set placement exclusions are being withdrawn, so manual placements could not be used for this anyway |
| Form | 4073050519663550 on all six ads; CTA Get quote ✔ |
| Identity | Page 627814417091714; Instagram account set on all six ads ✔ |
| Copy | Headline, description and primary text match build sheet §4 **word for word** on all six ads (checked by script; no stray text) ✔ |
| Enhancements | All Advantage+ creative features OPT_OUT, including standard enhancements, text, image animation, touch-ups, brightness, CTA, comments, translation and templates. Music opted out. AI image and video generation not applied (0 used, no videos in the asset feed) ✔ |
| Multi-advertiser ads | contextual_multi_ads OPT_OUT on all six ✔ |
| AI disclosure | self_disclosure OPT_IN on all six (D30) ✔ |
| Follow-up | WhatsApp only (Messenger and Instagram follow-ups off) ✔ |
| 9:16 images | Each ad uses its own uploaded 9:16 file as the vertical; Meta's AI "uncrop" vertical is **opted out** on all six ✔ Padding square and horizontal variants are kept; they are not AI |

### Images: Meta hash to approved file

Each Meta hash below matches the image of that name in the ad account.

| Ad | 4:5 (Meta hash) | 9:16 (Meta hash) |
|---|---|---|
| E1 | e1aa943673369038bb1b9f48c959cad5 | f43584087032ec39fcaf01e267ed76cf |
| E2 | eac8fe9ed8fa95b953a03c9567e354bd | 20c7a6bde213601cab3cf3d02e6b52cd |
| S1 | 70759a9a057a8c9c0a7c5645bc896e2e | acbd5193b6f82b384ce0cddfb03e7e25 |
| S2 | b92e7a4ed016a892d6071cf870c7ee86 | edefcfde87a34be5d63c2aa9100aedbb |
| B1 | bca6cb588cd97a8a1dcf80f7758ff19a | e7e21bfafb38ba68bdc5b4faa00f52ef |
| B2 | 42bae5474a58a69980aea4acd19c632f | 353f3468d7e2276c84ffcf6b556b9754 |

The S2 9:16 file would not group with its 4:5, so it was uploaded inside Customize media. Its hash therefore has no library name. It was checked by eye at 1080×1920 against the frozen `SIB-05_S2_9x16.png` and matches.

## Deviations

1. **Audience suggestions differ from the build sheet.**
   - **Added:** CEO, CFO, Managing Director, Chairman, Owner, "Owner and Founder" and **"Co Owner" (126237404086327)**, plus Business Decision Makers, Small business owners, Facebook Page admins and International business.
   - **"Co Owner" was not in the sheet**; it was added by mistake when picking from Meta's list.
   - **Missing:** "Founder", Partner, Managing Partner, Vice President, the India Desk titles, and the other interests. 代表取締役 is also not there.
   - Impact is low: under Advantage+ audience these are suggestions only, not limits. Sanjeev can trim or extend them before publishing.
2. **Regional rules.** Meta added Singapore and Australia regulated-category entries to each ad set. Advertiser and payer are shown as SETINDIABIZ PRIVATE LIMITED (business 629080835992237). This is required because Singapore and Australia are targeted.
3. **No end date set (D31).** It goes in at publish: 30 days after the publish date.
4. **Start times.** The ad sets carry start times of 16 Oct, so they start as soon as they are published.

## Preview pack

- `SIB-05_Preview_Pack_2026-10-16.html` was sent to Sanjeev.
- It covers all six ads in Instagram Feed, Stories and Reels, with links to the Facebook Feed, Stories and Reels previews.
- Meta's preview links expire on **23 Oct 2026, about 19:00 IST**.

## Chrome

- The Ads Manager tab was reloaded so that the temporary file-upload helper was cleared.
- The tab was left open in Sanjeev's Chrome. All edits are saved as a draft.
- The **Publish** button is now visible on that screen. It was not clicked.
