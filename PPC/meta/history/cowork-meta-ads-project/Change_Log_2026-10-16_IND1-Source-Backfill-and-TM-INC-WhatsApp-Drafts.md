# Change log: 16 Oct 2026 — #IND1 Lead Source backfill + TM/INC WhatsApp ad drafts

**Approval:** Sanjeev, 16 Oct about 11:50 IST, in chat:
- (1) "Yes, correct all 13" Incorporation leads stamped "Meta Ads".
- (2) TM/INC WhatsApp ads: "Drafts now, publish after 22 Oct".
- (3) "Reuse approved form-ad text + images".

**Executed by:** Claude via the Zoho CRM and Meta connectors, 11:55–12:15 IST.

**Operating principle (Sanjeev, 16 Oct):** consistent lead quality comes first; cost will come down over time.

---

## A. #IND1 leads: Lead_Source corrected (CRM, live)

**Why:** from 15 Oct 17:43 the LeadChain *Incorporation V2* chain stamped #IND1 form leads with Lead_Source **"Meta Ads"**.
- The Conversions API sweep only reads `Advt - Facebook / Instagram / WhatsApp`, so Meta could not learn which of these leads were good.
- The daily scorecard would also have missed them.

**What:** `updateRecords`, module Leads, `trigger: []` (no workflows fired), at 11:55:05 IST.
- Set Lead_Source to the platform found for each lead.
- Set Lead_Channel to "Advt".
- Meta_Campaign was already "#IND 1 — Incorporation" and was not touched.

| Lead id | Created (IST) | Lead_Source before → after |
|---|---|---|
| 1123581000948417207 | 15 Oct 17:43 | Meta Ads → Advt - Facebook |
| 1123581000948723026 | 15 Oct 19:48 | Meta Ads → Advt - Facebook |
| 1123581000948635035 | 15 Oct 20:08 | Meta Ads → Advt - Facebook |
| 1123581000948639027 | 15 Oct 20:13 | Meta Ads → Advt - Instagram |
| 1123581000948717083 | 15 Oct 23:23 | Meta Ads → Advt - Facebook |
| 1123581000948718118 | 15 Oct 23:59 | Meta Ads → Advt - Facebook |
| 1123581000948736063 | 16 Oct 00:12 | Meta Ads → Advt - Instagram |
| 1123581000948764055 | 16 Oct 00:39 | Meta Ads → Advt - Facebook |
| 1123581000948581149 | 16 Oct 01:18 | Meta Ads → Advt - Facebook |
| 1123581000948655082 | 16 Oct 02:17 | Meta Ads → Advt - Instagram |
| 1123581000948718206 | 16 Oct 02:44 | Meta Ads → Advt - Instagram |
| 1123581000948723233 | 16 Oct 09:17 | Meta Ads → Advt - Facebook |
| 1123581000948723290 | 16 Oct 11:02 | Meta Ads → Advt - Instagram |

**Read-back (COQL, about 12:00 IST):**
- All 13 records now show the new Lead_Source, Lead_Channel "Advt" and Meta_Campaign "#IND 1 — Incorporation".
- A search for Lead_Source = "Meta Ads" created since 15 Oct 00:00 returns no records.

**Root cause still open (Sanjeev's step; Claude does not edit the older LeadChain chains):**
- The *Incorporation V2* chain's Lead Source mapping still says "Meta Ads".
- It should pass `Advt - Facebook` / `Advt - Instagram` from the platform, or at least `Advt - Facebook`, with Lead_Channel `Advt`.
- Until it is fixed, every new #IND1 form lead needs the same correction. The daily watch (trig_01DPT99ZCoF8rictq4EsC2bP) has a SOURCE GUARD step that counts them first.

---

## B. TM and INC click-to-WhatsApp ads: built as drafts (Meta, NOT live)

Nothing is serving and nothing was published. Both ad sets are set to **PAUSED inside the draft**, so they would stay off even if they were published by accident. (Ads Manager's Publish button can sweep up every pending draft, for example when the 22 Oct Change 2 draft is published.)

### Ad sets

| | TM | INC |
|---|---|---|
| Ad set id (draft) | **120247062224450449** | **120247062226170449** |
| Name | SIB-02 \| TM \| WhatsApp \| IN | C1 - INC \| WhatsApp \| IN |
| Campaign | SIB-02 Trademark 120247048085410449 (ad-set budgets, OUTCOME_LEADS) | #IND 1 — Incorporation 120240912969660449 (ad-set budgets, OUTCOME_LEADS) |
| Optimisation / destination | CONVERSATIONS / WHATSAPP | same |
| WhatsApp number (promoted_object) | +91 95994 81905 | +91 95991 99509 |
| Budget | ₹1,000/day, highest volume | ₹1,500/day, highest volume |
| Language (hard) | English US + UK [6, 24] | same |
| Min age (hard) | 25 (suggested range 25–55, as in the SIB-02 form ad set) | 25 (suggested range 25–45, as in 24Hr INSA) |
| Location (hard) | The 30 cities of the SIB-02 form ad set, 25 mi, living in or recently in | The 18 cities of #IND1 24Hr INSA, 25 mi, living in or recently in |
| Detailed targeting (suggestion under A+A) | Copied from the SIB-02 form ad set, including the male suggestion | Copied from 24Hr INSA, all genders |
| Advantage+ audience | On | On |
| Placements | Facebook (feed, in-stream video, stories, search, reels, reels overlay, profile feed, notifications) + Instagram (feed, stories, reels, explore home, profile feed) | same |
| Draft status | PAUSED, VALIDATED, no errors | PAUSED, VALIDATED, no errors |

**Deliberate differences from the source ad sets:**
- **No Threads.** The spec said FB + IG only.
- **No Instagram search.** It is not among the live placements of the working ACR WhatsApp ad set.
- **No "frequently in" location type.** It is a legacy option.
- **The TM source's Advantage+ location setting (geo = 1) was not carried over.** Its city list therefore stays a hard limit, in line with the 16 Oct finding that cities are one of the three working junk filters.

### Ads (under each ad set; status ACTIVE inside the paused ad set; Meta validates them when Ads Manager opens them)

| | TM | INC |
|---|---|---|
| Ad id (draft) | **120247062230580449** "TM-C1 \| ₹1,999 brand check \| CTWA" | **120247062232100449** "INC-C1 \| ₹2,499 name and structure \| CTWA" |
| Image | d4fb9ef89190d1dbef762e23c478f7cc (approved SIB-02 form image) | 395068f10307ec22bf11663cf34f372e (approved #IND1 Ad-2 image) |
| Headline | Trademark Filing @ ₹1,999 + GST | Pvt Ltd Registration @ ₹2,499 + GST |
| Description | Free TM Search Included | Register Your Own Pvt Ltd Company |
| Button | Send WhatsApp message (WHATSAPP_MESSAGE) | same |
| Pre-filled message (`page_welcome_message`) | **Hi, I want to register a trademark (TM-C1)** | **Hi, I want to register my company (INC-C1)** |
| Identity | Page 627814417091714 + Instagram @setindiabiz_official (17841473603642746) | same |
| Meta AI enhancements | All opted out: image touch-ups, brightness/contrast, uncrop, animation, templates, text optimisations, enhance CTA, inline comments, adapt to placement, text overlay, description automation; multi-advertiser ads OPT_OUT | same |

**Primary text, TM:** the approved creative 1414111734270603 body, word for word, plus the approved last line "Tap Send WhatsApp message to check your brand name before filing."

**Primary text, INC:** the approved creative 2219613962304030 body, word for word, except that the 👉 line now reads "👉 Tap Send WhatsApp message to confirm your company name and structure."

**Claims check:** the claims are unchanged from the texts approved on 15 Oct:
- Fees are shown as professional fee + GST.
- Government fees are at actuals, per the Trade Marks Rules, 2017 First Schedule.
- "Subject to MCA processing" stays.
- The non-affiliation lines (IP India, MCA, marketplaces) stay.

### Publish checklist (on or after 22 Oct)

**Gates — all four must be true before publishing:**
1. The 22 Oct ACR decision read says **KEEP**, meaning the English + age-25 controls cut junk.
2. The SalesIQ project has shipped:
   - the ACR qualifier;
   - the TM/INC fallback (fb.me / instagram link → TM-UNK / INC-UNK).
   Also, a test chat to each number with "TM-C1" / "INC-C1" creates a lead with the right campaign, tag and rule.
3. **The account is topped up** to last at least a week at the new run-rate (about ₹9.5k + ₹2.5k = ₹12k/day). Top-ups are human-only.
4. The LeadChain *Incorporation V2* Lead Source mapping is fixed (Part A), so form and WhatsApp leads for INC count in the same place.

**Sanjeev's steps in Ads Manager:**
1. Open each draft ad and check:
   - (a) the WhatsApp number shown is …81905 (TM) / …99509 (INC);
   - (b) **the message template shows the coded pre-filled message above, not Meta's default "Hello! Can I get more info on this?"**. If it shows the default, type the coded message there. This is the one setting the API could stage but not confirm;
   - (c) the preview shows the approved text, and Advantage+ creative enhancements are off.
2. Publish.
3. Switch the two ad sets **On**. They publish paused.
4. Tell Claude, who reads back the live spec, then checks the first chats arrive coded and are filed under the right campaign.

**Stop-loss after switch-on:**
- Window: the first 3 full days.
- From the 15 Oct spec, kept as a brake: pause if 3-day cost per CRM lead is above ₹340 (TM) / ₹440 (INC), or after 2 spend-days with 0 CRM leads.
- Quality rule (16 Oct principle): also pause if junk is above 25% in the first 3 days' cohort. The form ad sets ran 13–21% in Jul–Aug.
- Do not pause on Meta cost per conversation alone.
- Judge on CRM leads with Meta_Campaign "SIB-02 Trademark" / "#IND 1 — Incorporation" and Lead_Source "Advt - WhatsApp".

---

## C. Other updates

- `Change_Log_2026-10-16_SIB-04-CTWA-Audience-Controls.md`: the stop-loss now uses the quality-first rules, matching the 22 Oct scheduled read. The old cost-only "revert above ₹628" rule is retired.
- Scheduled: 22 Oct 10:45 IST, a check-in in this session on the four publish gates above (after the 10:00 ACR decision read).

## D. Browser session, 16 Oct about 12:05–12:40 IST ("you take browser control and do the needful")

**D1. Ads Manager check of the drafts (in-app browser).** Nothing was published. "Publish" was not clicked; a "Publish draft items?" dialog was closed with **Close**.

| Draft | Finding |
|---|---|
| TM ad 120247062230580449 | Connected WhatsApp number **+91 9599481905**. Primary text, headline and description are as approved. The Destination preview shows the coded pre-filled message **"Hi, I want to register a trademark (TM-C1)"** (confirmed in the page DOM). Ads Manager did not change the draft. **OK.** |
| INC ad 120247062232100449 (original) | Connected number **+91 9599199509** and text as approved. **But opening it in the Ads Manager editor made Ads Manager overwrite the pre-filled message on its own (`user_edit: false`)** with a WhatsApp Flow lead form: "Welcome! Please fill out the form below to sign up!", button "Join now", flow "Default Flow Title" (flow_id 2299347806918374, WABA 28134106499605130). That is not the approved setup. It would also collide with the SalesIQ Zobot on …99509. |

**D2. INC fix (Meta connector, drafts only):**
- 120247062232100449 → status **PAUSED**, renamed **"DISCARD - INC-C1 auto WA form (Ads Manager default) | CTWA"**. Deleting it from the browser was refused by a permission check, so it was not deleted.
- 120247062311800449 → a re-create with a malformed message field (Claude's error, a misplaced brace). Meta flagged it HAS_ERRORS ("Welcome message should not exceed 300 characters"). Now **PAUSED** and renamed **"DISCARD - INC-C1 malformed message | CTWA"**.
- **120247062314820449 "INC-C1 | ₹2,499 name and structure | CTWA"**: the clean ad, approved text, coded message "Hi, I want to register my company (INC-C1)", `user_edit: true`. VALIDATED, no errors. **This replaces 120247062232100449 in Part B.**

**D3. Publish checklist additions (the Part B steps still apply):**
- **Do not open the INC ad in the Ads Manager editor.** That is what triggered the overwrite. Publish from **Review and publish**, and let Claude read back the live ad afterwards.
- Before publishing, **discard the two "DISCARD - …" ads** under C1 - INC | WhatsApp | IN (tick → Discard draft for those rows only). The malformed one has an error that can block the publish.
- The INC WhatsApp number has a Meta WhatsApp Flow ("Default Flow Title") that Ads Manager now uses as the default. Decide whether to delete that flow in WhatsApp Manager, or keep it unused.

**D4. LeadChain *Incorporation V2* chain (Sanjeev's Chrome, Zoho Setup → Marketplace → Facebook → LeadChain).**
- Read only; **not changed**. Opening the editor was refused by a permission check.
- **Before state (12 rows):**
  - Email → Email
  - Full name → Last Name
  - Phone number → Phone
  - Which service do you need? → Description
  - **[fixed value "Meta Ads"] → Lead Source**
  - Lead Id → Social Lead ID
  - Campaign Name → Meta Campaign
  - Form Name → Meta Lead Form
  - Advert Name → Meta Ad Name
  - Adset Name → Meta Ad Set
  - Advert Id → Meta Ad ID
  - Platform → Meta Ad Type
- **Reference:** the healthy **Trademark V2** chain has **no Lead Source row**. On 10 Oct (R41), Incorporation V2 leads also arrived with Lead_Source empty, and the workflow "Auto-set Lead Source from URL" then set "Advt - Facebook" / "Advt - Instagram". LeadChain pre-fills "Meta Ads" whenever a chain is saved (10 Oct R42-d). The 15 Oct tag edit most likely re-saved it.
- **Fix for Sanjeev:**
  1. Open the chain and click the pencil icon.
  2. Remove only the "Meta Ads → Lead Source" row.
  3. Save.
  4. Re-open the chain view and confirm the other **11 rows** are still there (re-maps have dropped rows before, 25 Jun).
- **Claude then checks** the next Incorporation form lead: Lead_Source should be "Advt - Facebook" or "Advt - Instagram".

**D4a. LeadChain fixed by Sanjeev (~12:35 IST); verified by Claude in the in-app browser:**
- The Incorporation V2 chain now has **11 rows**, and the "Meta Ads → Lead Source" row is gone.
- These rows are all present:
  - Email → Email
  - Full name → Last Name
  - Phone number → Phone
  - Which service do you need? → Description
  - Lead Id → Social Lead ID
  - Campaign Name → Meta Campaign
  - Form Name → Meta Lead Form
  - Advert Name → Meta Ad Name
  - Adset Name → Meta Ad Set
  - Advert Id → Meta Ad ID
  - Platform → Meta Ad Type
- The chain is **Active**.
- Workflow **"Auto-set Lead Source from URL"** (Leads, create or edit) is **active**. It fills a blank Lead Source with Advt - Facebook / Instagram.
- No Incorporation lead had arrived since the fix at the time of the check. The first one is checked by a scheduled follow-up at 15:30 IST, and by the daily 09:40 watch's source guard.

**D4b. Post-fix check, 16 Oct 15:31 IST (scheduled follow-up, COQL, read-only): PASS.**

There were 5 #IND1 form leads ("Incorporation V2") between 12:35 and 15:31. Every one has Lead_Source matching its platform, and none has "Meta Ads".

| Lead id | Created | Meta_Ad_Type | Lead_Source | Lead_Channel |
|---|---|---|---|---|
| 1123581000948989001 | 12:50 | fb | Advt - Facebook | (blank) |
| 1123581000949016001 | 12:56 | ig | Advt - Instagram | Advt |
| 1123581000949104030 | 14:57 | ig | Advt - Instagram | (blank) |
| 1123581000949119027 | 15:05 | fb | Advt - Facebook | (blank) |
| 1123581000949072034 | 15:15 | ig | Advt - Instagram | (blank) |

**Lead_Channel blank on arrival is the normal pattern, not a regression:**
- A Trademark V2 lead from the healthy chain (1123581000949004013, 13:41) is also blank.
- Older Trademark V2 and Incorporation V2 leads show "Advt" only after a later edit.
- The CAPI sweep keys on Lead_Source, so it sees these leads.

No backfill is needed.

**D5. Not done:**
- Switching off the expired "Lead Assignment Rule Daily Check" (trig_0142dx52rfEJxFz4Q8kxsh4w) was refused by a permission check. Sanjeev can switch it off in Scheduled tasks.
- Top-up: human-only.

## Flags for Sanjeev

- **Funds:** about ₹15.7k left at 06:42 today against about ₹9.5k/day of budgets. It runs out around **Saturday 17 Oct midday**.
- **Lead Assignment Rule Daily Check** (trig_0142dx52rfEJxFz4Q8kxsh4w) was meant to switch itself off after 14 Oct, but it is still enabled and ran today. Mentioned only; not changed.

## E. Publish-gate check, 22 Oct 2026 ~10:50 IST (scheduled task trig_01JxBzhSMxMQgB1McNW6tWaC; read-only)

**Verdict: HOLD. Do not publish.** 3 of the 4 gates fail. Nothing was published, activated or changed.

| Gate | Result | Evidence |
|---|---|---|
| 1. 22 Oct SIB-04 read says KEEP | **FAIL (not met)** | The 10:00 read was **SUPERSEDED**: the old WhatsApp ad set is archived, with ₹0 spend on 17–19 Oct. The successor, Directors WhatsApp, had 9 leads on 17–19 Oct: 33% junk (25% without the known RM mislabel) and 22% valid. That is too few to call. The formal Directors read is 23 Oct 10:15. |
| 2. SalesIQ: ACR qualifier + TM/INC fb.me fallback + test chats | **FAIL** | No WhatsApp lead since 16 Oct has a "Not Eligible" disposition, so the qualifier is not live. No CRM lead carries Meta_Ad_Code TM-UNK or INC-UNK. The only coded TM/INC lead since 15 Oct is the 15 Oct TM-C1 test (…948692001); there is no INC-C1 test. No SalesIQ change log is in this project. |
| 3. Balance covers ≥ 7 days | **FAIL** | The last top-up was ₹20,000 on 21 Oct 11:17, and there has been none since. About ₹3.2k of credit was left at 09:45 (watch log), less than half a day. 7 days at the India budgets plus TM/INC (≈ ₹10.7k/day) needs about ₹88k including 18% GST; with SIB-05 on (≈ ₹14.7k/day) it needs about ₹1.21 lakh. |
| 4. No #IND1 leads with Lead_Source "Meta Ads" since 16 Oct 12:00 | **PASS** | COQL Lead_Source = 'Meta Ads', created ≥ 16 Oct 12:00 → 0 records. |

**Draft read (connector, object_state=draft):**
- **TM:** the original 120247062224450449 / ad 120247062230580449 no longer exist. They went when the SIB-02 Trademark campaign was deleted on 18 Oct.
  - The rebuild is ad set **120247099920320449** in "SIB-02 Trademark - Copy": PAUSED, VALIDATED, no errors, ₹1,000/day.
  - The hard limits match the 30 cities, English and 25+, with home + recent location.
  - Placements are FB/IG feed, stories and reels only.
  - Ad **120247099921540449** carries the coded message "Hi, I want to register a trademark (TM-C1)", `user_edit` true, enhancements opted out, no active errors. It shows NEEDS_VALIDATION, which Meta resolves on publish.
- **INC:** ad set 120247062226170449 is PAUSED and VALIDATED, with no errors. Ad 120247062314820449 carries "Hi, I want to register my company (INC-C1)", `user_edit` true, VALIDATED, no errors.
- **The two "DISCARD - …" INC ads (120247062232100449, 120247062311800449) are gone** from both the drafts and the live objects. They have been discarded, so that pre-publish step is done.
- **New flag: the INC ad set still has the wide 16 Oct placements.** These are FB in-stream, search, reels overlay, profile feed and notifications, plus IG Explore and profile feed. The TM rebuild was tightened to feed, stories and reels on 19 Oct, because one-tap WhatsApp chats from low-intent placements drove the ACR junk. **Recommend** the same tightening on INC before publishing. That is an audience edit, so it needs Sanjeev's go; it was not done.
- **Also open:** the TM bot's `campaign` value may need to read "SIB-02 Trademark - Copy" (19 Oct note), so that form and WhatsApp leads group together.

**When all 4 gates pass, Sanjeev's steps:**
1. Do not open the INC ad in the Ads Manager editor.
2. Check in **Review and publish** that only the TM and INC WhatsApp items are included. The two DISCARD ads are already gone.
3. Publish.
4. Switch both ad sets On; they publish paused.
5. Claude then reads back the live specs and the first coded chats.

**Next gate check:** none is scheduled. Re-run on request once SalesIQ confirms the qualifier and the TM/INC test chats, and the account is funded for a week.
