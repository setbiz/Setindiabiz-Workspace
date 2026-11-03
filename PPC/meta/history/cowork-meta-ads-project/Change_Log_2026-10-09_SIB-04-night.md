# Change Log: SIB-04, 9 Oct 2026 night (from 18:42 IST)

Continues `Meta Ads/Change_Log_2026-10-09_SIB-04-evening.md` (last entries R24, C33). Scope: step 1 (law and fee re-check), the read-only groundwork for step 2 (Meta build), then G1–G10 from the spec's go list (Canva fixes, LLP creative, campaign, both ad sets, Instant Form, eight ads with images and videos, previews). Nothing was changed in SalesIQ, CRM or Desk. **Nothing is live in Meta: G11 (publish) waits for Sanjeev.** Output: `Meta Ads/SIB-04_Ads_Build_Spec_2026-10-09.md`.

## Read-only findings

| # | Item | Finding | Method |
|---|---|---|---|
| R25 | Law re-check, companies | Sec. 96(1) AGM 30 Sep 2026; Sec. 137(1) AOC-4 by 30 Oct (OPC 27 Sep, passed); Sec. 92(4) MGT-7/7A by 29 Nov; ₹100 a day per form, no cap, under Sec. 403 read with the Fees Rules 2014 (2018 Second Amendment). Only 2026 amendment to the Fees Rules is G.S.R. 300(E), 21 Apr 2026 (DIR-3 KYC Web, item VII). | Web: incometaxindia.gov.in, egazette.gov.in, copies of the 2018 rules |
| R26 | MCA circulars | No FY 2025-26 additional-fee relaxation as of 9 Oct. 2026 circulars: 01 (CCFS), 02 (DPT-3), 03 and 04 (CCFS to 31 Aug, then 15 Sep). Last year's waiver came on 17 Oct (GC 06/2025), so watch for a repeat. | Web search |
| R27 | Law re-check, LLP | Form 8 rule is **Rule 24(4)** (handover said 24(8), which is the audit threshold). LLP late fee is **not ₹100 a day** since 1 Apr 2022: slab multiples under Annexure A substituted by G.S.R. 109(E), 11 Feb 2022. Our page setindiabiz.com/learning/llp-form-8-filing-late-fee still says ₹100 a day. | Web: ICAI branch and other reproductions, MCA LLP FAQ |
| R28 | Meta 152154124583473 | 7 campaigns PAUSED, Ads Manager draft empty, account ACTIVE with a payment method. Pages 627814417091714 and 185807091504036 both report leadgen_tos_accepted=false via API (unchanged since July). IG account setindiabiz_official linked. Custom audiences include Company Director 2019-20 to 2026-27 and LAL-Director-2024-25 1%. | Meta connector |
| R29 | Connector limits | ads_create_creative has no WhatsApp pre-filled message and no lead-form field; there is no form-creation tool. Instant Form, form ads and CTWA ads must be built in Ads Manager. | Tool schemas |
| R30 | Canva "PPC 2026" (FAHXTwdMxJ4) | Two designs: 1:1 DAHXThVtclk and 9:16 DAHXT5r2Ex8, 3 pages each (p1 ACR-C2, p2 ACR-C1, p3 ACR-C5). Claims check out; fixes proposed: F1 stray "?," on p2; F2 "Complete annual filing" wording on p2/p3; F3 AI disclosure for the p3 photo. | Canva read-design (view only) |
| R31 | Privacy policy URL | https://www.setindiabiz.com/privacy-policy live, updated 4 Oct 2026 | WebFetch |

| R32 | LLP penalty | Sec. 34(5) LLP Act (as substituted by Sec. 13, LLP (Amendment) Act 2021, in force 1 Apr 2022): ₹100 a day for failing Sec. 34(3), capped at ₹1 lakh (LLP) and ₹50,000 (each designated partner). **Corrects R27's wording**: "₹100 a day" can be used for LLP as the adjudicated penalty with caps, not as the filing fee. | PRS copy of the 2021 Act; Taxmann on commencement |
| R33 | Custom audiences page 2 | Company Director 2024-25 = 120226217224820449; LLP 2021-22 to 2024-25 lists found (ids in spec section 3). | Meta connector |

## Decisions (Sanjeev, 18:56)
Q1 audit included, wording "audit support" · Q2 director audiences up to 2025-26 · Q3 ACR-C5 photo AI-generated → disclosure OPT_IN · Q4 route B, API plus browser · Q5 WhatsApp button on form completion, duplicate/test leads accepted · Q6 add LLP Form 8 ad. Spec updated to v2 (19:10).

## Changes (Sanjeev's go: "go G1–G5")

| # | Go | Change | Before | After | Verified by |
|---|---|---|---|---|---|
| C34 | G1 | Canva DAHXThVtclk (1:1) and DAHXT5r2Ex8 (9:16), page 2 headline: stray "?," removed | "AGM held on 30 Sep 2026?, File annual returns…" | "AGM held on 30 Sep 2026? File annual returns on time to avoid late filing costs" | Thumbnails before commit; committed |
| C35 | G2 | Same two designs, footer on pages 1–3: "audit support" added to the inclusions | "…AGM documents, AOC-4, MGT-7 / 7A and ITR-6…" | "…AGM documents, audit support, AOC-4, MGT-7 / 7A and ITR-6…" | Thumbnails; committed |
| C36 | G2 (fit) | Layout fixes so the longer footer fits: 1:1 footer font 17→16 px on pages 1 and 2 (page 2 had broken "ITR-" across lines); 9:16 page 3 footer box widened 480→540 px (it had split "MGT-7") | Footer overflow | One clean footer per page | Thumbnails; committed |
| C37 | G3 | New design DAHXhUNfm-Q "SIB-04 LLP Form 8 – 1:1 Feed" (copied from page 2 of the 1:1 design) with LLP-C1 text per spec section 2 | Did not exist | Committed; moved into Canva folder "PPC 2026" (FAHXTwdMxJ4) | Thumbnail; folder listing |
| C38 | G3 | New design DAHXhZRzH7Q "SIB-04 LLP Form 8 – 9:16 Stories/Reels", same text. Sec. 34(5) line set to 36 px so "2008." does not orphan next to the CTA | Did not exist | Committed (transaction 7470864324468922641); moved into "PPC 2026" | Thumbnail; folder listing |
| C39 | G4 | Campaign "SIB-04 Annual Filings" **120246968311680449**: OUTCOME_LEADS, AUCTION, no special ad category, no campaign budget (ABO) | Ads Manager draft empty | Staged in the Ads Manager draft, validated, no errors | ads_get_ad_entities (draft) |
| C40 | G4 | Draft campaign status set ACTIVE→**PAUSED**. The connector is in draft mode and stages new objects with status ACTIVE, which would go live on publish; G4 was approved as "created PAUSED" | status ACTIVE (draft) | status PAUSED (draft) | ads_get_ad_entities (draft) |
| C41 | G5 | Ad set "SIB-04 \| ACR \| CTWA \| IN" **120246968316940449**: CONVERSATIONS, destination WhatsApp, promoted object Page 627814417091714 + [phone redacted], ₹3,500 a day (350000 paise), IMPRESSIONS, lowest cost, India, Facebook + Instagram placements (no Audience Network, no Messenger), Advantage+ audience with the 15 custom audiences from spec section 3 as suggestions, end 29 Nov 2026 23:59 IST | Did not exist | Staged in the draft, validated, no errors | ads_get_ad_entities (draft) |
| C42 | G5 | Draft ad set status ACTIVE→**PAUSED** (same reason as C40) | status ACTIVE (draft) | status PAUSED (draft) | ads_get_ad_entities (draft) |

Notes on C39–C42:
- Nothing is published. Both objects sit in the Ads Manager draft for account 152154124583473 and show nowhere as live campaigns. The connector's summary cards carry "Publish Campaign" / "Publish Ad Set" buttons: **don't click them**. Publishing happens only at G11, in Ads Manager, with Sanjeev.
- Age: the connector stored 25 as an Advantage+ **age suggestion** (age_min_suggestion 25), not a hard floor. Spec section 3 says "age 25+". If a hard floor is wanted, set "Minimum age 25" under Audience controls in Ads Manager during G7 (needs its own go).
- Before/after evidence for the API steps is the draft read (empty before C39; both objects PAUSED and VALIDATED after C42). No browser screenshots: the browser was not used in this block.

## G6: Instant Form (Sanjeev's go 19:14 "yes" to start G6; "go create form" 19:38)

Browser: Claude in Chrome. Two browsers showed as "Browser 1/2"; Connect prompt sent, Sanjeev picked **"SK Big HP"**. That Chrome was logged out of Meta; Sanjeev logged in himself (19:20). Built in Business Suite › Lead ads forms (Page "Setindiabiz Private Limited", 627814417091714), not inside an ad.

| # | Item | Finding | Method |
|---|---|---|---|
| R34 | MCA circulars, re-check before G6 | Still nothing after GC 04/2026; no FY 2025-26 additional-fee waiver. Company "₹100 a day" copy stands. | Web search, 19:15 |
| R35 | WhatsApp number on the Page | Business Suite's WhatsApp list for the Page includes **[phone redacted]** (primary is [phone redacted]). **Closes the open item "confirm the number is linked to the Page".** | Form editor dropdown |
| R36 | Page Messenger in SalesIQ | SalesIQ › Facebook Messenger: **"Yet to configure" on all 8 brands**; the Page's Messenger is not in SalesIQ. | SalesIQ settings (view only, separate tab, closed) |
| R37 | setindiabiz.com/roc-filing as a possible thank-you link | Right FY 2025-26 dates, but: WhatsApp and phone go to [phone redacted] (main number, not the owner); has its own "Request a Call / Quote" form (second lead); no ₹7,499 pack price; **CCFS-2026 text still says the window is open "until 31 August 2026" and urges action before then** (GC 04/2026 extended it to 15 September; closed now); no LLP Form 8 content. | WebFetch |

Decisions (Sanjeev): 19:28 first said keep the Messenger chat routed to the LeadChain owner, then **19:30 "not messenger, WhatsApp only"**; 19:31 asked about sending people to a website page instead; after R37, **19:38 "go create form"** with the WhatsApp button.

| # | Go | Change | Before | After | Verified by |
|---|---|---|---|---|---|
| C43 | G6 | Instant Form **"SIB-04 ACR Form v1"**, Form ID **2635626386872789**, created 9 Oct 2026 7:38 PM. Higher intent (review screen), no OTP. **Flexible form delivery OFF** (Meta could otherwise drop questions). Intro: "Annual filing for FY 2025-26" + spec text. Q1 "What type of entity is it?" Private Limited / One Person Company (OPC) / LLP. Q2 "Which years are pending?" FY 2025-26 only / FY 2025-26 and earlier years / Not sure. Contact: Full name, Phone, Email (all required); Meta-required description "Our team will use these details to call or WhatsApp you about your annual filing." Privacy link https://www.setindiabiz.com/privacy-policy. Custom disclaimer title "Consent to contact", text "Setindiabiz Private Limited will use these details to respond to this enquiry.", required checkbox "I agree to be contacted by Setindiabiz on phone and WhatsApp about this enquiry." Ending: "Thank you." / "Our team will contact you on the number you shared. To talk now, chat with us on WhatsApp." + native **Chat on WhatsApp** button on [phone redacted]. "Start conversations on Messenger" **unticked**. Settings: English (US), Sharing **Restricted**, default field names. | 5 forms on the Page (Trademark V2, DPIIT V2, Virtual CFO V2, Incorporation V2, CCFS2026 V2) | 6 forms; SIB-04 ACR Form v1 **Active**, 0 leads, Restricted | Forms list + details panel; preview screens 1–5 sent to Sanjeev before creating; screenshots before/after Create |

Notes on C43:
- The form is Active but no ad uses it yet. A form can't be deleted, only archived.
- The native WhatsApp button carries no pre-filled text, so "[IF-ACR]" is not possible. A form lead who taps it reaches the SIB-04 bot; the plug finds the CRM lead by the last 10 phone digits and the bot forwards to its owner. **Timing gap:** LeadChain takes ~7 min to create the form lead; a tap before that creates an Advt - WhatsApp chat lead owned by the next LG-11 person, who may differ from the owner LeadChain later sets (unless LeadChain merges by phone). Check in the phone test after the chain exists.
- Typing into the form dropped letters (a writing extension in that Chrome); values were set directly and checked in the preview.

## G7–G10: ad set B, eight ads, videos, previews (Sanjeev's go 19:45 "You complete all, i am watching")

Browser: Claude in Chrome ("SK Big HP"), Ads Manager draft for account 152154124583473. API steps via the Meta connector in draft mode. Every new object was set to PAUSED straight after creation; every ad's on/off toggle is off.

| # | Go | Change | Before | After | Verified by |
|---|---|---|---|---|---|
| C44 | G8 | Eight images uploaded to the ad account library: ACR-C1 1x1 a0c06f28…, 9x16 2548beaa…; ACR-C2 1x1 e74ae0e7…, 9x16 a9c2df21…; ACR-C5 1x1 f2ec36b5…, 9x16 7b4934a2…; LLP-C1 1x1 b8cc7fc2…, 9x16 aa6f43a5… (full hashes in the resume prompt) | Not in library | In library as "SIB-04 …" | ads_get_ad_images; media picker |
| C45 | G7 | Ad set **"SIB-04 \| ACR \| Form \| IN" 120246968737470449**: LEAD_GENERATION, destination ON_AD (Instant Form), Page 627814417091714, ₹2,500 a day (250000 paise), same targeting as ad set A (India, FB + IG, 15 audience suggestions, age 25 as suggestion), end 29 Nov 2026 23:59 IST; set PAUSED | Did not exist | Draft, PAUSED, validated | Draft read |
| C46 | G8 | Ad set A: Ads Manager had swapped the CTWA number to +91 95991 99509 while the first ad was built; reselected **[phone redacted]** (G5 scope) | 95991 99509 | [phone redacted] (page_whatsapp_number_id 1277691388770677) | Draft read |
| C47 | G8 | **ACR-C1 \| Deadline \| CTWA 120246968790550449**: spec copy; CTA Send WhatsApp message; conversation template "Start conversations" with pre-filled "Hi Setindiabiz, I want to file my company's AOC-4 and MGT-7. [ACR-C1]" | Did not exist | Draft, PAUSED | Ads Manager; draft read |
| C48 | G8 | **ACR-C2 \| Cost of delay \| CTWA 120246968981980449** (quick duplicate of C1, "Apply recommendations" unticked); spec copy; pre-filled "Hi Setindiabiz, I want to file my annual returns before late fees. [ACR-C2]" (spec text was 81 characters; limit is 80, so "start" was dropped) | Did not exist | Draft, PAUSED | Draft read |
| C49 | G8 | ACR-C2 headline changed on Sanjeev's instruction ("headline is vague", then "it should say Avoid late fee") | "₹100 a day per form, no upper limit" | **"Avoid late fee of ₹100 a day per form"** | Draft read |
| C50 | G8 | **ACR-C5 \| Dates and price \| CTWA 120246969045870449** (duplicate of C2); spec copy; duplicated template with pre-filled "Hi Setindiabiz, please share details of the ₹7,499 annual filing pack. [ACR-C5]" (79 chars) | Did not exist | Draft, PAUSED | Draft read |
| C51 | G8 | **LLP-C1 \| Form 8 \| CTWA 120246969168420449** (quick duplicate of C1); LLP images; spec LLP copy (₹100 a day only as the Sec. 34(5) penalty with "can be" and both caps); headline "LLP Form 8 due 30 Oct 2026"; description "Form 8 filing from ₹2,499 + GST"; duplicated template with pre-filled "Hi Setindiabiz, I want to file Form 8 for my LLP. [LLP-C1]" | Did not exist | Draft, PAUSED | Draft read |
| C52 | Sanjeev's request | **Eight 12-second MP4 videos** (1080x1080 and 1080x1920, H.264, 30 fps, silent track) made from the approved Canva exports: a spotlight moves over each block in turn with a 2% slow zoom. **No text was added or changed**; every word is from the approved creative. Meta's own AI video options were not used (they misstated dates and called the ₹100 a "penalty"). Uploaded to the ad account: ACR-C1 1x1 1129840180007679, 9x16 1645062090557187; ACR-C2 1x1 1068965572675181, 9x16 1804535804222498; ACR-C5 1x1 2695132164229282, 9x16 28444986225193123; LLP-C1 1x1 1637745967886865, 9x16 1094832266659734 | No videos | In library | ads_get_ad_videos; frame sheets checked |
| C53 | G8 | Each of the four CTWA ads now carries 4 media with **placement-specific assets**: 1:1 image + 1:1 video for Feeds, in-stream for Reels, Search; 9:16 image + 9:16 video for Stories, Status, Reels only. Advantage+ creative enhancements 0/5, essential enhancements 0/3, music off, AI image/video/text suggestions not applied, translation 0 languages, "Optimize text per person" disabled | 2 images each (C1–C5) / not built (LLP) | 4 media each, placements as stated | Customize media re-read per item; draft read (placement_customizations) |
| C54 | G8 | ACR-C1 CTWA headline changed on Sanjeev's go (20:45 "yes to Avoid late fee") | "AOC-4 by 30 Oct, MGT-7 by 29 Nov" | **"Avoid late fee: AOC-4 by 30 Oct, MGT-7 by 29 Nov"** | Draft read |
| C55 | G9 | Ads Manager "Create ad" on the Form ad set failed again (JS error CONFIRM_DRAFT_CREATION). First workaround, duplicating C1 into ad set B, produced draft **120246969483460449** "ACR-C1 \| Deadline \| CTWA - Copy" with an error (lead form + WhatsApp destination in one spec). **Deleted on Sanjeev's go (20:47 "yes")**; it was never published | Broken draft | Deleted ("Ad deleted") | Screenshot after delete; ads list shows 8 ads |
| C56 | G9 | Four Form ads staged via the connector in ad set B, each set PAUSED: **ACR-C2 \| Cost of delay \| Form 120246969544800449**, **ACR-C1 \| Deadline \| Form 120246969553500449**, **ACR-C5 \| Dates and price \| Form 120246969554880449**, **LLP-C1 \| Form 8 \| Form 120246969555870449**. CTA **Get quote** → form 2635626386872789. Copy per spec; last line of C1, C2 and LLP-C1 "Tap Get quote and answer two short questions. Our team will call or WhatsApp you."; C5 unchanged. Headlines as the CTWA versions (C1 "Avoid late fee: AOC-4 by 30 Oct, MGT-7 by 29 Nov", C2 "Avoid late fee of ₹100 a day per form") | Did not exist | Draft, PAUSED, validated | Draft read |
| C57 | G9 | In Ads Manager, each Form ad: Instagram profile setindiabiz_official set (API had left it blank); single image replaced by the same 4 media with the same placement split as C53; Meta's default "Add music" (on for API ads) turned off; enhancements 0/5 and 0/3; translation 0 languages; lead-nurture follow-up channels **Messenger and Instagram unticked** (Meta ticks them by default; Sanjeev's 19:30 decision "WhatsApp only"); WhatsApp stays as the form's completion button | API defaults | As stated | Ads Manager checks; draft read |
| C58 | G9 | **ACR-C5 \| Form: "Ad includes media created or edited with AI" ticked** (Q3 decision, AI photo) | Off | self_disclosure OPT_IN | Draft read (transparency_metadata) |
| C59 | G7/G5 | Ad set A had lost its end date in Ads Manager (showed "End date: None"); restored to spec via the connector | None | **29 Nov 2026 23:59 IST**, PAUSED | Ads Manager screenshot before; draft read after |
| C60 | G10 | Previews: Advanced preview of all 8 ads captured and sent to Sanjeev as one sheet (SIB-04_Draft_Ad_Previews_2026-10-09.jpg) | – | Sent | File in chat |
| C61 | Sanjeev's request | Images, videos and the preview sheet saved to **G:\\My Drive\\0. Claude Cowork\\Meta Ads\\SIB-04 Creatives** (17 files) | – | Written | device_commit_files result |

Final draft state (connector read after C59): campaign 120246968311680449 PAUSED; ad set A 120246968316940449 PAUSED, ₹3,500/day, WhatsApp [phone redacted], end 29 Nov 23:59 IST; ad set B 120246968737470449 PAUSED, ₹2,500/day, form, end 29 Nov 23:59 IST; 8 ads PAUSED, 0 active errors. Ads Manager's top bar shows "Review and publish (11)". Nothing published.

Notes on C44–C61:
- Ad set A's start time is stored as 9 Oct 2026 19:48 IST (already past), so it will start the moment it is published. Ad set B has no start time and also starts on publish.
- **AI disclosure on ACR-C5 \| CTWA is not set.** Ads Manager offers the "created or edited with AI" box only on the Form (lead) ads; on the WhatsApp ad it does not appear, even after removing and re-adding media (tested; media and placements restored, pre-filled message intact). The connector's update tool cannot change a creative. Options for Sanjeev under Flags.
- Typing into Meta fields still drops letters; all text was set directly and checked in the draft read, not by eye.
- Meta's video picker shows a small warning icon on the new videos; not opened. Likely the silent audio track or a placement-fit note; check in Ads Manager before G11.
- Each Ads Manager "Publish"/"Preview to publish" button was left alone. The "Publish draft items?" dialog appeared once when closing the editor; "Close" was clicked, not "Publish".

## Flags raised for later
- **ACR-C5 \| CTWA AI label**: Ads Manager has no AI disclosure control for this WhatsApp ad. Options: (a) accept it without the label (the Form version carries it); (b) rebuild C5-CTWA with a creative made through the API with the disclosure, if Meta accepts it on a WhatsApp ad; (c) ask the designer for a C5 variant without the AI photo.
- **On-image "Chat on WhatsApp" pill in Form ads**: all four creatives show a green "Chat on WhatsApp" pill, but the Form ads' button is "Get quote". Not wrong (the form ends with a WhatsApp button) but mixed. Option: designer makes Form variants without the pill.
- 9:16 creatives: footer and price sit in the bottom ~250 px, which Instagram Stories/Reels overlays can cover; the previews also show the profile name over the top "ATTENTION" band. Designer to check the safe zone.
- Website: setindiabiz.com/learning/llp-form-8-filing-late-fee calls ₹100 a day the "late fee"; it is the Sec. 34(5) penalty. Content fix for the website team.
- Website: setindiabiz.com/roc-filing still presents CCFS-2026 as open until 31 August 2026 (R37). Content fix for the website team.

## Awaiting Sanjeev
- **G11 publish**: review the previews sheet, then publish from Ads Manager ("Review and publish (11)") with every ad toggle left off, or tell Claude which ads to switch on. Check the account has funds or auto-pay first (₹6,000 a day + 18% GST).
- LeadChain SIB-04 chain on form "SIB-04 ACR Form v1" (2635626386872789): rule "PPC - SIB-04 Annual Filings - LG-11", static Tag FB-ACR, Product Cat Annual Filing, Q1/Q2 into Description. **Must exist before the Form ads go live**, or form leads won't reach CRM.
- Decide the ACR-C5 CTWA AI label and the "Chat on WhatsApp" pill on Form creatives (Flags).
- Say whether age 25 should be a hard floor (see C41 note).
