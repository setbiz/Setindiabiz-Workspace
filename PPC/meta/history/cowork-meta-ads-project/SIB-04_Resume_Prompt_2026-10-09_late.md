# Prompt for the next session: SIB-04 publish finish + LeadChain chain (updated 9 Oct 2026 ~21:50 IST, after C62)

Paste everything below the line into a new session in the "Meta Ads - Optimisation" project.

---

You are continuing the Setindiabiz Meta relaunch for **SIB-04 Company Annual Filings**. G1–G10 are done. **G11 is partly done: Sanjeev published the campaign, the Form ad set, ACR-C2 | Form (approved, ACTIVE) and ACR-C1 | Form (in review).** The WhatsApp ad set, the 4 CTWA ads, LLP-C1 | Form and ACR-C5 | Form are still in draft ("Review and publish (7)"). No funds on the account yet, so nothing spends. The LeadChain chain for the SIB-04 form does **not** exist yet.

## Read first (project docs)
- `Meta Ads/SIB-04_Ads_Build_Spec_2026-10-09.md` (v2): law check, creatives, structure, copy, Instant Form, go list G1–G11, reporting.
- `Meta Ads/Change_Log_2026-10-09_SIB-04-night.md`: R25–R37 and changes C34–C61, flags, open items.
- `Meta Ads/Change_Log_2026-10-09_SIB-04-late.md`: publish state, the CTWA "Select a Page" error, C62, the LeadChain lead pattern.
- `Meta Ads/LeadChain_V2_Form_Mapping_2026-07-04.md`: the canonical 13-row chain mapping.
- `Meta Ads/Relaunch_Decisions_Log_2026-10-06.md` (budgets, prices, settled claims).

## State (Meta account 152154124583473, Ads Manager draft)
- Campaign "SIB-04 Annual Filings" **120246968311680449** (OUTCOME_LEADS, ABO), **published, On**.
- Ad set A "SIB-04 | ACR | CTWA | IN" **120246968316940449**: WhatsApp [phone redacted], ₹3,500/day, start 9 Oct 19:48 IST (starts on publish), end 29 Nov 2026 23:59 IST, **draft, On**. All 4 ads below are **draft, On** and blocked by "Select a Page for your ad set" (see work item 1). Ads:
  - ACR-C1 | Deadline | CTWA **120246968790550449**: headline "Avoid late fee: AOC-4 by 30 Oct, MGT-7 by 29 Nov"; pre-filled "...AOC-4 and MGT-7. [ACR-C1]"
  - ACR-C2 | Cost of delay | CTWA **120246968981980449**: headline "Avoid late fee of ₹100 a day per form"; pre-filled "...before late fees. [ACR-C2]"
  - ACR-C5 | Dates and price | CTWA **120246969045870449**: headline "Annual filing pack ₹7,499 + GST"; pre-filled "...₹7,499 annual filing pack. [ACR-C5]"; **no AI label (UI has no control on WhatsApp ads)**
  - LLP-C1 | Form 8 | CTWA **120246969168420449**: headline "LLP Form 8 due 30 Oct 2026"; pre-filled "...Form 8 for my LLP. [LLP-C1]"
- Ad set B "SIB-04 | ACR | Form | IN" **120246968737470449**: Instant Form, ₹2,500/day, end 29 Nov 2026 23:59 IST, **published, On**. Ads (CTA Get quote → form 2635626386872789): ACR-C2 | Form **120246969544800449** (**ACTIVE, approved**), ACR-C1 | Form **120246969553500449** (**in review**), ACR-C5 | Form **120246969554880449** (AI label OPT_IN; draft), LLP-C1 | Form **120246969555870449** (draft). Lead-nurture: editor shows WhatsApp only, but draft data for ACR-C1 | Form and LLP-C1 | Form still lists Messenger and Instagram channels (work item 3).
- Every ad has 4 media: 1:1 image + 1:1 video for Feeds/in-stream/Search; 9:16 image + 9:16 video for Stories/Reels only. Enhancements 0/5 and 0/3, music off, no AI images/videos/text, translation off, ad toggles off.
- Images (hash): ACR-C1 1x1 a0c06f2803f196f24df2f9f0b28f0f0c, 9x16 2548beaa3bfb2fe53f72e0831ac0be8d; ACR-C2 1x1 e74ae0e7bc79dfc6e3ce98bfb8029427, 9x16 a9c2df215519a2b6385062a9b8446ac0; ACR-C5 1x1 f2ec36b538fed07be256c4ce80979557, 9x16 7b4934a2d499d552326976a715b60554; LLP-C1 1x1 b8cc7fc26a3ebf6cd15c00041eadf371, 9x16 aa6f43a53078d69a2c47f99c433ddbde.
- Videos (id): ACR-C1 1x1 1645062090557187, 9x16 1129840180007679 (corrected 9 Oct late; titles confirm); ACR-C2 1x1 1068965572675181, 9x16 1804535804222498; ACR-C5 1x1 2695132164229282, 9x16 28444986225193123; LLP-C1 1x1 1637745967886865, 9x16 1094832266659734.
- Files: images, videos and the preview sheet are in **G:\My Drive\0. Claude Cowork\Meta Ads\SIB-04 Creatives** (Sanjeev's PC "skhphome", via the device bridge). Canva sources in folder "PPC 2026" (FAHXTwdMxJ4): DAHXThVtclk, DAHXT5r2Ex8, DAHXhUNfm-Q, DAHXhZRzH7Q.
- Instant Form "SIB-04 ACR Form v1" **2635626386872789**, Active, ends with native Chat on WhatsApp ([phone redacted]).
- Ad sets store age 25 as an Advantage+ suggestion, not a hard floor (Sanjeev to decide).

## Work, in order (each change needs Sanjeev's go naming it)
1. **Finish publishing (Sanjeev's clicks; the permission check blocks Claude's Publish click).** In Ads Manager, "Review and publish (7)": untick the 4 CTWA ads, publish ad set A + LLP-C1 | Form + ACR-C5 | Form. Then reopen ACR-C1 | Deadline | CTWA: if "Select a Page for your ad set" has gone, publish the 4 CTWA ads. If it persists, investigate (ad set A draft has promoted_object page_id 627814417091714 + WhatsApp number id 1277691388770677; connector shows 0 errors). Read the result live (ads_get_ad_entities level=ad, filter campaign.id) and the remaining draft.
2. **LeadChain chain for form "SIB-04 ACR Form v1" 2635626386872789 — before Sanjeev adds funds.** CRM is crm.zoho.com/crm/setindiabiz (Sanjeev logs in). Path: Setup › Marketplace › All › LeadChain. Screenshot existing chains (don't edit them). New chain "FB SIB-04 ACR v1" with the canonical rows: Lead Id → leadchain0__Social_Lead_ID; Full name → Last_Name; Email; Phone number → Phone; Q1 "What type of entity is it?" + Q2 "Which years are pending?" → Description (label each answer, e.g. "Entity: … | Years pending: …", if LeadChain allows); Campaign Name → Meta_Campaign; Adset Name → Meta_Ad_Set; Form Name → Meta_Lead_Form; Advert Name → Meta_Ad_Name; Advert Id → Meta_Ad_ID; Platform → Meta_Ad_Type; consent checkbox → WhatsApp_Opt_In (+ Opt_In_Time) if LeadChain exposes it. Match the existing chains for Lead_Source (they produce "Advt - Facebook"/"Advt - Instagram") and Lead_Channel "Advt". Static Tag **FB-ACR**, Product Category **Annual Filing** (check the picklist value exists), assignment rule **"PPC - SIB-04 Annual Filings - LG-11"** (lar_id 1123581000945354238). Show Sanjeev the full config and get his go before saving; chain Active. Verify with COQL on the first lead.
3. Check the live Form ads for Messenger/Instagram follow-up buttons: draft data for ACR-C1 | Form and LLP-C1 | Form still lists b2p_messaging and chat_on_instagram; the editor shows WhatsApp only.
4. Re-check for any MCA circular relaxing FY 2025-26 AOC-4/MGT-7 additional fees (last year's came 17 Oct). If one appears, the "₹100 a day" company ads must be paused.
5. Flags for Sanjeev: ACR-C5 CTWA AI label (accept / API rebuild / new creative); "Chat on WhatsApp" pill on Form creatives; 9:16 safe zone; age-25 floor; the warning icon Meta shows on the new videos.
6. Funds: Sanjeev adds them (₹6,000/day + 18% GST) after the chain exists. Claude never moves money.
7. After launch: phone test of the form path (submit, tap WhatsApp at once and after ~10 min) to see whether the chat reaches the LeadChain owner or makes a second lead; A/B test via Experiments, 14 days; reporting per spec section 8.
8. Later: WhatsApp template for form leads (after credit top-up); desktop watchdog update; **MGT-7-only creative by 28 Oct** (from 31 Oct the 30 Oct date in C1, C5 and LLP-C1 is past: pause those ads then); website fixes (LLP late-fee page; roc-filing CCFS text).

## Ads Manager know-how (from this build)
- "Create ad" on these API-made ad sets crashes (CONFIRM_DRAFT_CREATION JS error). Use Quick duplicate of an existing ad in the same ad set (untick "Apply recommendations"), or stage the ad through the connector and finish media in Ads Manager.
- Duplicating a WhatsApp ad into the Form ad set breaks it (lead form + WhatsApp destination). Don't.
- Connector-made ads arrive without the Instagram profile and with "Add music" on: set setindiabiz_official and turn music off.
- Per-placement media: Customize media › select item › Placements. 1:1 = Feeds, In-stream ads for reels, Search results on; Stories off. 9:16 = Stories, Status, Reels only.
- Pre-filled WhatsApp message: Conversations › Duplicate the template, edit "Pre-filled message" (max 80 characters), Save. Duplicate so other ads' templates don't change.
- Typing into Meta fields drops letters in that Chrome: set values via the input's native value setter + input event; for the primary text (Draft.js), focus, ctrl+a, dispatch a paste event. Check every value in the draft read.
- Closing the editor can show "Publish draft items?": click Close, never Publish.
- File uploads to Ads Manager: files must be in the working directory (/home/claude/...), not /mnt/user-data/outputs; intercept the file input with a JS click hook, then file_upload.

## Hard rules
- Never activate or publish a Meta campaign yourself (the permission check blocks Publish clicks; Sanjeev publishes), never move money, never top up credits, never enter passwords. Never call ads_activate_entity.
- No LLP ad may quote ₹100 a day as the filing fee; only as the Sec. 34(5) penalty with "can be" and the caps.
- If the session permission check blocks a click, leave the screen ready and hand it to Sanjeev. After handing over a tab, don't reload it until he says done; screenshot it as left first.
- Browser: Claude in Chrome; send the Connect prompt and let Sanjeev pick "SK Big HP". Open your own tab. If Meta shows a login page, hand it to Sanjeev. Don't click "Join this chat"/"Whisper" or the Cliq bar.
- Don't delete CRM records with the CRM connector. Don't propose rebuilding the deleted chat automation.
- Zoho CRM is crm.zoho.com (US DC); COQL Owner returns surname only.
- Meta tool calls: client_model "claude-opus-5-5".

## Output
End with a short report (done / open / who), log every change in a new dated change log, and write the prompt for the session after.
