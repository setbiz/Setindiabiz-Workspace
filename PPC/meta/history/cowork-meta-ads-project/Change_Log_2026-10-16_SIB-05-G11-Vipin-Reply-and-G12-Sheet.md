# Change log: SIB-05 Vipin's reply, 9:16 found, G12 build sheet (16 Oct 2026, about 14:45–15:10 IST)

**Read-only for Meta, Zoho CRM and Canva.** One email sent to Vipin on Sanjeev's instruction ("Send to Vipin", 15:07). Two project docs written.

## Vipin's reply

| Item | Detail |
|---|---|
| Message | 1a143db230e313b0, 14:06 IST, thread 1a1359139e2d73dc. Body: "Updated." No mention of the 9:16 set |
| 4:5 file DAHX_Sw46n4 | Saved again 14:08, 14:43 and **15:03 IST (epoch 1792143199)** |
| 9:16 set | **Found as pages 1–6 of "SIB-04 Annual Filings – 9:16 Stories/Reels" (DAHXT5r2Ex8)**, saved 14:18 and **15:02 IST (epoch 1792143170)**. SIB-04's own pages are intact as pages 7–9 (ACR-C2, ACR-C1, ACR-C5); the file had 3 pages on 9 Oct and 9 now, so nothing was overwritten. The 13:00 and 13:45 reviews missed it because they searched by title |

## 4:5 set (read at 14:43; re-checked at the 15:03 save, no material change)

| # | Fix (13:02 email) | Status |
|---|---|---|
| 1 | Page 3 footer | Done, word for word; **still much smaller than on the other pages** |
| 2 | Page 3 crest | Done |
| 3 | Page 5 "Setindibiz" | Done |
| 4 | Flags on pages 3, 5, 6 | **All done** (page 5 desk flag now gone) |
| 5 | Page 1 footer legibility | **Done**, footer now sits in the dark band |
| — | Page 4 globe India outline | Check |
| — | Page 6 sign cropped "BRANCH OFFIC" | Cosmetic |

Wording on all six pages still matches claims review §5 and the footer. No §8 legal-stop wording, client logos, emblems or flags.

## 9:16 set (pages 1–6 of DAHXT5r2Ex8; re-checked at the 15:02 save, no material change)

- **Wording:** matches §5 and the footer on all six pages. No flags or crest visible; page 5 has the "Liaison Office" nameplate; page 6 sign cropped ("BRANCH C…"); page 4 has the same globe.
- **Safe zone: fails on all six pages.** At 1080×1920 the brief allows text only between y = 269 and y = 1,248 px (previews at 335×596: y ≈ 84 to 387). Every page has the headline above that band and the small print and footer below it. Page 6 also has "USD 100k net worth" and the RBI line below it. In Stories and Reels those areas sit under the profile name, caption and CTA button, so the compliance footer would be hidden.
- Page 3 (S1) will be the hardest to fit; the email asks Vipin to say so rather than cut text.

## Email to Vipin: SENT

| Field | Value |
|---|---|
| Sent | **~15:08 IST, message 1a144139650b891e**, reply to 1a143db230e313b0 on thread 1a1359139e2d73dc. Sanjeev's instruction: "Send to Vipin" (15:07) |
| Pre-send check | Draft unchanged; no new mail from Vipin; both Canva files re-read after their 15:02–15:03 saves, fix list still accurate |
| From / To / Cc | one@setindiabiz.com / vipin.pathak@hatrotech.com / sanjeev@setindiabiz.com |
| Content | Same text as draft r8900458062539897730: 4:5 page 3 footer to normal size; page 4 globe outline check; page 6 sign (optional). 9:16: move all text into 269–1,248 px; same fixes as 4:5; move the six SIB-05 pages into their own design "SIB-05 India Entry – 9:16 Stories/Reels"; ask rather than shorten |
| Leftover | The draft **r8900458062539897730 is still in Drafts** (the connector has no send-draft action, so the reply was sent as a new message). Not deleted by Claude. **Sanjeev to discard it** so it is not sent twice |

## G12 build sheet

Written: `Meta Ads/SIB-05_G12_Build_Sheet_2026-10-16.md`. Exact campaign, ad set and ad settings, the approved copy word for word (checked against claims review §4), and the build order.

**Finding that changes the G12 plan:** the build cannot be done through the connector alone.
- `ads_create_creative` has no lead-form field, so it cannot make a placement-customised (4:5 + 9:16) creative that opens form 4073050519663550.
- API writes to lead ads have failed with 1815089 (Lead Ads terms) since July. On 16 Oct `ads_get_ad_account_pages` still reads `leadgen_tos_accepted = false` for both Pages. The 15 Oct fix (reconnect the connector with `pages_manage_ads`) has not shown up.

Settings captured from live ad sets for reuse (read-only): SIB-04 Form uses LEAD_GENERATION / ON_AD / IMPRESSIONS / highest volume; SIB-02 Form uses OFFSITE_CONVERSIONS with WEBSITE_AND_LEAD_FORM, includes Threads, and has location expansion (`individual_setting.geo = 1`), neither of which SIB-05 should copy. Job-title, industry and behaviour IDs already used in the account are listed in the sheet.

## Decisions (Sanjeev, 16 Oct 14:58: "agree to all four")

| # | Decision | Effect |
|---|---|---|
| **D28** (B1) | **Build route:** campaign through the connector; ad sets and ads in Ads Manager in Sanjeev's own Chrome (Claude in Chrome), as SIB-04; everything read back through the connector | G12 needs Sanjeev's Chrome open with the Claude extension and logged in to Meta |
| **D29** (B2) | **Wait for Vipin's 9:16 re-layout**; no feeds-only launch | G12 waits for the 9:16 set to clear review |
| **D30** (B3) | **AI disclosure ticked on all six ads if the photos were made or edited with AI.** Default if Sanjeev does not say otherwise: tick it (the scenes look AI-composited; SIB-04 ACR-C5 precedent) | Set when each ad is built |
| **D31** (B4) | **End date 30 days after publish**, set on the publish date | Checked again at G13 |

These do **not** authorise G12. G12 still needs G11 clear, G9 passed and Sanjeev's explicit go.

## Open — who

| Item | Who |
|---|---|
| Discard leftover draft r8900458062539897730 in Gmail Drafts | Sanjeev |
| 4:5 page 3 footer; 9:16 re-layout into own file | Vipin |
| Confirm D30 default (photos AI-made/edited?) only if the default is wrong | Sanjeev |
| G9 test leads | Sanjeev |
| Account funding (runs out ~Sat midday) | Sanjeev |
| 16:30 re-check (trigger trig_01L9jHjchMiRonpdWZ8gT4pa) | Claude |
