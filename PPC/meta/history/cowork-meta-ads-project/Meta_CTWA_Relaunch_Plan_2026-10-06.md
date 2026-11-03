# SetIndiaBiz — Meta Relaunch Plan: Click-to-WhatsApp + Instant Form Hybrid, FDI Services, Zobots
**Date:** 6 Oct 2026 · **Owner:** Sanjeev Kumar · **Prepared by:** Claude (Meta Ads operator) · **Status:** Plan approved in part, build pending
**Evidence:** `Deep_Analysis_2026-10-06.md` (same folder) — 4,260 paid-Meta CRM leads, ₹12.67L spend, 1 Apr–5 Oct 2026, read-only.

---

## 0. Decisions at a glance

| # | Decision | Why |
|---|---|---|
| 1 | **Hybrid, not CTWA-only.** Trademark, Incorporation and Annual Return run CTWA **and** Instant Form side by side as a Meta A/B test for 14 days. GST/CFO and DPIIT run CTWA only. FDI runs Instant Form (higher-intent) with a WhatsApp hand-off. | Forms have 4,000+ leads of history and the best cost per valid lead. CTWA has no captured history: the May test produced 77 conversations, none of which reached CRM. A side-by-side test answers the question with your own data in two weeks, instead of betting the budget on it. |
| 2 | **Every form lead gets a WhatsApp message within 60 seconds** from the product's number (utility template). | 44% of form leads were never reached. That rate is the same at every hour, on FB and IG, in metros and elsewhere, so the ad isn't the cause. The fix is to open a channel the lead will answer. |
| 3 | **Budget: ₹15,000/day ad spend** = Domestic ₹7,000 + Annual Filing ₹5,000 + FDI ₹3,000. | As you instructed. Meta adds **18% GST**, so funding needed is about **₹17,700/day, or ₹1.24L for 7 days**. |
| 4 | **Fund a 7-day balance or turn on auto-pay before launch.** | Daily UPI top-ups caused 46 dark days in 150, and every dark day resets Meta's learning. |
| 5 | **Six brand numbers → five live campaigns.** Regulatory ([phone redacted]) stays bot-ready with no ad budget for now. | Mapped to your list (§2). |
| 6 | **24-hour delivery, no dayparting.** Night leads get the bot plus a first human reply at 09:30. | Night CPL is ₹210 vs ₹318 at midday, with the same quality. The 24-hour ad set beat the daytime one. |
| 7 | **Price-led creatives everywhere**, with professional fee and government fee shown separately. | The TM "₹1,999 + govt fee ₹4,500" ad brought 82% of TM leads at ₹133–151 CPL. "Free search" and fear angles cost 2–7× more per lead. |
| 8 | **New `Lead_Source` = `Advt - WhatsApp`**, plus an ad-code stamp read from the first message. | SalesIQ is not documented to pass Meta's `ctwa_clid` (see §7). The ad code in the pre-filled message gives ad-level attribution anyway. |
| 9 | **#IND1 and #IND3 PAUSED at campaign level** (done 6 Oct, verified). | So a top-up doesn't restart the old instant-form settings before the new structure is ready. |

---

## 1. What the data says (the short version)

- **Targeting worked.** Junk was 3.5% for TM and 7.5% for Incorporation. Age, gender and state are not levers: CPL differs by 15% or less across age bands, and women's CPL equals men's.
- **Connectivity failed because of process, not the ad.** No-contact runs at 44% in every slice. On identical IND1 leads it ranges **from 20% to 68% depending on which RM owns the lead**. `First_Contact_Time` is empty on all 4,260 leads.
- **Incorporation and Trademark did not pay back on the first sale:** 0.33× and 0.34× first-deal revenue/spend. They only pay through the back end (Post-INC docs, TM exam replies, ACR renewal), so **sell bundles**.
- **Annual Return is the earner.** CCFS returned 1.95×; the 2-week LLP ACR campaign returned 1.47× at ₹3.9k per win. This justifies the ₹5k/day special.
- **Chat converts better than forms.** As organic benchmarks (an upper bound for CTWA):

  | Source | Avoiding Call | Won rate |
  |---|---|---|
  | WhatsApp | 15.9% | 4.1% |
  | SalesIQ web chat | 2.1% | 12.1% |
  | Meta forms | 38.5% | 3.2% |

- **CTWA test of 23–30 May:** ₹343 per conversation vs ₹400 per form lead. **All 77 conversations were lost.** Nothing was captured in CRM. This is the first thing the new build must fix.

---

## 2. Campaign architecture and budget

Budgets are ad spend excluding GST. Ad sets marked **A/B** run as a Meta A/B test (CTWA vs Form, same audience and creative, 50/50) for 14 days.

| Campaign (WhatsApp number) | Ad set | Daily | Destination | Objective → goal | Audience |
|---|---|---|---|---|---|
| **SIB-01 Startups** (+91 95991 99509) | Incorporation — CTWA | ₹1,250 | WhatsApp | Leads → Conversations* | India, 25–55, all genders, Advantage+ audience |
| | Incorporation — Form (A/B) | ₹1,250 | Instant form + WA auto-message | Leads → Leads (Conversion leads once CAPI volume allows) | same |
| | *DPIIT ads sit inside the Incorporation CTWA ad set* | — | WhatsApp | — | bot asks "New company or DPIIT?" |
| **SIB-02 IPR** (+91 95994 81905) | Trademark — CTWA | ₹1,250 | WhatsApp | Leads → Conversations* | India, 25–55, Advantage+ |
| | Trademark — Form (A/B) | ₹1,250 | Instant form + WA auto-message | Leads → Leads | same |
| **SIB-03 GST & CFO** ([phone redacted]) | GST Return + Accounting/CFO — CTWA | ₹2,000 | WhatsApp | Leads → Conversations* | India, 25–60, Advantage+; bot screens job seekers |
| **SIB-04 Annual Filings** ([phone redacted]) | Company ACR — CTWA | ₹3,000 | WhatsApp | Leads → Conversations* | Director custom audience + Advantage+ expansion |
| | Company ACR — Form (A/B) | ₹2,000 | Instant form + WA auto-message | Leads → Leads | same |
| **SIB-05 FDI Services** ([phone redacted]) — **CBO ₹3,000** | India Entry Services | CBO | Instant form (higher intent) → WA/email hand-off | Leads → Leads | See §4 |
| | Indian Subsidiary Incorporation | CBO | same | same | |
| | Branch / Liaison Office Registration | CBO | same | same | |
| **Regulatory** ([phone redacted]) | — | ₹0 | bot only | — | — |
| **Total** | | **₹15,000** | | | |

\* **Check in Ads Manager when building:** WhatsApp Business documents a **"Leads" performance goal for WhatsApp destinations** (not in EU/UK/JP/KR, so India qualifies). The Marketing API lists only "Conversations" under the Leads objective. Choose "Leads" if Ads Manager offers it for these ad sets, otherwise "Maximise conversations".

**Placements.** Use Advantage+ and exclude Audience Network. Reels and Stories were the cheapest placements, so every ad needs a 9:16 version. Review the Instagram feed for Incorporation on day 7 (₹322 CPL historically).

**Ad Set budget minimums.** Each CTWA/Form half at ₹1,250/day should give about 40–60 conversations or leads a week. That is enough for Meta's learning phase. Going below this is not recommended.

**Annual Filing window.** Run until **29 Nov 2026**. That is the MGT-7 due date for a 30 Sep AGM: s.92(4) Companies Act 2013 allows 60 days from the AGM. The AOC-4 date is **30 Oct** under s.137(1), which allows 30 days. After 30 Oct, switch creatives to MGT-7 and late-filers. **LLP Form 8 is due 30 Oct** (Rule 24, LLP Rules 2009); add an LLP ad until then.

**Timing.** DPIIT and CFO historically lost money (DPIIT cost/won ₹48.8k on n=1; CFO 0 wins in 40 leads). They get no dedicated budget until CTWA proves itself on them.

---

## 3. Why hybrid, and how the test is judged

**Arguments for CTWA**
- The lead starts the conversation, so they're reachable by definition.
- Chats are logged.
- Price questions get answered instantly.
- Under Meta's free entry point, when a business replies within 24h to a CTWA chat, **all messages for 72 hours are free**.

**Arguments for Instant Forms**
- Proven volume and cost, and a full CRM/CAPI loop already live.
- Can optimise on lead quality (ValidLead/QualifiedLead events via the live CAPI). CTWA quality optimisation is **not documented** except purchase optimisation through CAPI for Business Messaging, which needs `ctwa_clid`.

**Verdict at day 14 (per product), in this order** (the project's objective hierarchy):
1. Cost per **contacted** lead: reached = not "Establishing Contact" and not "Avoiding Call" after 48h.
2. Cost per strict-valid lead.
3. Cost per progressed lead (Proposal Sent / Negotiation / Payment Pending).
4. Cost per won deal (directional at day 14; final at day 30).

The winner takes the loser's budget. If they are within ±15%, keep both. Use Meta's A/B test tool (`ads_experiment_abtest_create_test`) so the split is clean.

---

## 4. FDI Services campaign (new)

**Countries.** United States, United Kingdom, UAE, Singapore, South Korea, Japan, Germany, Netherlands, Australia, Canada.
- **Exclude** every country sharing a land border with India (China, Pakistan, Bangladesh, Nepal, Myanmar, Bhutan, Afghanistan). Investment from these needs Government approval under **Press Note 3 (2020)** (DPIIT, FDI Policy para 3.1.1).
- Meta will drift budget towards the cheapest geo, likely UAE. A form question ("Where is your parent company incorporated?") screens out individual expats and job seekers.

**Why a form, not CTWA, for FDI.** WhatsApp is not the default business messenger in the US, South Korea (KakaoTalk) or Japan (LINE). Leads also arrive outside Indian hours. Higher-intent forms work across time zones.
- **Completion screen:** "Chat with our India-entry team on WhatsApp" (wa.me link to [phone redacted] with pre-filled `[FDI-FORM]`).
- **Immediate email** with a booking link.
- **Hours:** 09:30–19:30 IST covers UAE, Singapore, Korea, Japan and UK mornings. US leads get a booked call.

**Form questions** (higher intent):
1. Parent company country.
2. Entity type wanted: Subsidiary / Branch / Liaison / Not sure.
3. Sector.
4. Timeline: within 3 months / 3–6 / exploring.
5. Name, business email, phone.

**Expectations.** No baseline exists; label this a 30-day test. The KPI is **qualified meetings**, not CPL. Overseas CPMs are a multiple of India's, so expect few leads at ₹3k/day. Judge on meetings and FDI deals (FDI incorporation avg ticket ₹46k; nominee director ₹1.34L).

**Claims-safe copy anchors** (verify at copy sign-off):

| Product | Safe claim | Basis |
|---|---|---|
| Subsidiary | "At least one director resident in India is required." | s.149(3) Companies Act 2013 |
| Subsidiary | "FC-GPR reporting within 30 days of share allotment." | FEMA (Mode of Payment and Reporting of Non-Debt Instruments) Regulations 2019, FEMA 395/2019-RB |
| Subsidiary | "Most sectors are on the automatic route, subject to sectoral caps." | FEMA (Non-debt Instruments) Rules 2019 |
| Branch / Liaison Office | "Set up through an AD Category-I bank; some sectors and countries need RBI/Government approval; a Liaison Office cannot earn income in India." | FEMA 22(R)/2016-RB — **re-verify before use** |

**Never say:** "100% FDI allowed", "no approval needed", "set up in X days".

---

## 5. Creatives

### 5.1 What exists in Canva (reviewed 6 Oct)

| Product | Reuse (with fixes) | Retire |
|---|---|---|
| Annual Filing | *2026 Ads 1200* p1, p3, p5 ("Late ROC filing gets costly ₹100/day", "Timeline: AGM → AOC-4 in 30 days → MGT-7 in 60 days"). *WhatsApp Ads* p9 "All 6 filings @ ₹7,499". | All CCFS "90% waiver" pages: the scheme **ended 15 Sep 2026** (GC 04/2026). The "ROC Return Filing 2024" pages. The LLP "Form 11 last date 30 May" pages. |
| Incorporation | p13 "Register your Pvt Ltd Company" and p14 "Choose the right structure" (compliant footers). *WhatsApp Ads* p6 "Pvt Ltd @ ₹2,499". | "MCA Approved", "Launch in days not weeks" pages. |
| Trademark | p16 "TM vs ®" (good, cites s.107). Rebuild the **₹1,999 + ₹4,500 govt fee** winner in the new style. | p15 "Free preliminary search" lead angle (the worst CPL historically). |
| GST Return / CFO | p17 "Virtual CFO for small business", p18 "Accounting, MIS & Tax Compliance". | The old "GST return filing" generic pages. |
| DPIIT | none usable as-is | **All current DPIIT pages** (see 5.3). |
| FDI | p7 "Launch your India subsidiary end to end", p9 "Enter India with confidence". | — |

### 5.2 Changes every CTWA creative needs

- On-image CTA: **"Chat on WhatsApp"** instead of "Request a call", "Get quote" or "Apply now".
- Sizes: 1:1 (1080) plus **9:16 (1080×1920)** for Reels and Stories.
- **Pre-filled message** carrying the ad code, e.g. *"Hi Setindiabiz, I want to register my trademark. [TM-C1]"* (see §6.4). This is the attribution backbone.
- Footer on every image: *"Setindiabiz is a private professional services firm, not affiliated with MCA / IP India / DPIIT / GSTN. Government fees and stamp duty at actuals."*

### 5.3 Claims that must change (found in current creatives)

| Current claim | Problem | Replace with |
|---|---|---|
| DPIIT: "Tax exemptions", "From tax relief to funding support" | Tax holiday needs a separate **Inter-Ministerial Board certificate** (s.140, Income-tax Act 2025, formerly s.80-IAC). Recognition alone gives none. | "DPIIT recognition for entities ≤10 yrs old and ≤₹200 cr turnover (G.S.R. 108(E), 4 Feb 2026). Tax holiday needs separate IMB approval." |
| DPIIT: old ₹100 cr limit (if anywhere) | Limit raised to ₹200 cr in 2026 | as above |
| Incorporation: "Government fees ₹6,000 (approx.) payable to Govt" | ROC fee is **nil** for authorised capital ≤₹15 lakh. Stamp duty varies by state. DSC is not a government fee. | "ROC fee nil up to ₹15 lakh capital · stamp duty (state-wise) & DSC at actuals" |
| "Pvt Ltd registered in 7 days", "Launch in days" | MCA processing is not in your control | Keep "7 days" only if your median turnaround supports it, and always with "typically, after complete documents; subject to MCA processing" |
| "MCA Approved", "ROC-approved process", mock MCA form with "Government of India" | Implies government affiliation (State Emblem of India (Prohibition of Improper Use) Act 2005, s.3; CCPA Guidelines 2022) | Remove |
| "25,000+", "50,000+ founders", "4.8/5 by 10,000+", "8 out of 10 funded startups" | Inconsistent numbers, unsubstantiated (ASCI Ch. I.1; CPA 2019 s.2(28)) | Use one number you can prove from CRM, or none |
| "Filed before deadlines, guaranteed" | Guarantee claim | "We file within X working days of receiving complete documents" |
| ACR: "Director KYC" bullet; "DIR-3 KMC" typo | DIR-3 KYC is no longer annual (Rule 12A amended 2026) | Drop the bullet, or "DIR-3 KYC (if due)" |
| GST Registration "in 3 days" | Rule 14A applies only to eligible applicants (≤₹2.5L monthly B2B output tax) | "3 working days under Rule 14A for eligible applicants" |
| "Accountant + CA + CS" (CFO) | Must actually be delivered by a CA/CS (CA Act 1949 ss.24, 26) | Keep only if true for every engagement |

### 5.4 New angles to build (from the data)

| Product | Angles |
|---|---|
| **Trademark** | (1) "Trademark filing ₹1,999 + govt fee ₹4,500/class (individual, startup, MSME)". (2) "Use ™ the day we file; ® only after registration" (s.107). (3) Bundle: "Filing + reply to examination report". |
| **Incorporation** | (1) "Pvt Ltd ₹2,499 professional fee · ROC fee nil up to ₹15L capital". (2) **Bundle:** Incorporation + Post-INC Key Five Docs + first-year ACR. Lifts the ₹4.6k ticket and locks in the renewal. |
| **Annual Filing** | (1) "AOC-4 due 30 Oct · MGT-7 due 29 Nov · ₹100/day per form after that". (2) "All 6 filings @ ₹7,499" (bundle). (3) "Missed 3 years? Directors face disqualification for 5 years" (s.164(2)(a)). Add an LLP Form 8 ad until 30 Oct. |
| **GST Return** | (1) **Three-year time bar:** "GST returns can't be filed once 3 years pass from the due date" (s.39(11) CGST Act, inserted by Finance Act 2023; enforced on the portal from July 2025). For example, Oct 2023 GSTR-3B becomes un-fileable on 20 Nov 2026. A real, rolling urgency hook. (2) GSTR-9 FY 2025-26 due **31 Dec 2026** (optional ≤₹2 cr turnover). (3) Monthly filing from ₹750/month. |
| **Virtual CFO** | "Your monthly books, GST and TDS for a fixed fee". The bot must screen "Are you hiring?" out (CFO ads drew 17.5% job seekers). |
| **DPIIT** | Eligibility-checker angle: "Is your startup eligible? ≤10 yrs, ≤₹200 cr turnover". No tax claims. |

**Canva blocker:** copying *2026 Ads – 1200X1200* and *Whatsapp Ads* failed with "Not allowed to access design". These designs are owned by another team account. See §8 for the fix.

---

## 6. Zobot design (one bot per brand; the same skeleton with product-specific questions)

### 6.1 Skeleton (Codeless builder, WhatsApp channel)

1. **Start: read the first message.** If it contains `[XX-NN]`, store `ad_code`. Otherwise `ad_code = organic-wa`.
2. **Greeting and notice (every bot):**
   > "Hi 👋 This is Setindiabiz, a private professional services firm (not a government office). I'll ask 3 quick questions so the right expert can help you. We use your details only to respond to this enquiry — privacy: setindiabiz.com/privacy-policy. Reply STOP anytime."

   Buttons: **Continue** · **Talk to an expert now** · **See price**
3. **See price** → a price card (professional fee and government fee shown separately, the same figures as the ad) → back to Q1.
4. **Q1–Q3 product questions** (6.2). Buttons where possible (WhatsApp shows up to 10 as a list). Max 3 questions before the hand-off.
5. **Name.** Prefill from the WhatsApp profile and confirm. **Email** is optional ("Skip" allowed). **Do not ask for PAN or Aadhaar numbers**: WhatsApp policy bars sensitive ID collection.
6. **Opt-in:**
   > "Can we send you updates about this enquiry on WhatsApp?"

   Yes / No → `WhatsApp_Opt_In`. Required before any later template follow-up (WhatsApp Business Messaging Policy).
7. **Create or update the CRM Lead** (6.3) via a Webhook card → Deluge function: search by phone first, update if found, else create.
8. **Hand-off:**
   - **In hours:** Forward to Operator → the product group's agents (selected operators, *round-robin / route one-by-one*). If nobody accepts within 2 minutes, go to the fallback pool.
   - **Outside hours or unavailable:**
     > "Thanks {name}! Our {product} expert will message you here by 9:30 AM. You can type your questions meanwhile."

     Plus a CRM task due at 09:30 for the owner.
9. **Job-seeker exit** (GST/CFO and Startups bots): "Are you looking for a job with us?" → if yes, careers link and end. No CRM lead created.

### 6.2 Product questions

| Bot / number | Q1 | Q2 | Q3 |
|---|---|---|---|
| **Startups** (…509) | What do you need? New Pvt Ltd / LLP / OPC / DPIIT recognition / Not sure | When do you want to start? This week / This month / Exploring | Your city/state (stamp duty varies by state) |
| **IPR** (…905) | What to protect? Brand name / Logo / Both / Already filed – got objection | Applicant: Individual / Startup or MSME / Other company *(drives the ₹4,500 vs ₹9,000 fee)* | Is the brand already in use? Yes / Not yet |
| **GST & CFO** (…107) | Need: GST return filing / Pending old returns / GSTR-9 annual / Monthly accounting & CFO / Looking for a job | Business type: Proprietor / Pvt Ltd / LLP / Other | Approx. monthly invoices: <50 / 50–300 / 300+ |
| **Annual Filings** (…455) | Entity: Pvt Ltd / OPC / LLP | Which year? FY 2025-26 only / Older years also pending | AGM held for FY 2025-26? Yes / No / Not sure |
| **FDI** (…508) | Where is the parent company? (list of countries) | Setup: Subsidiary / Branch office / Liaison office / Not sure | Timeline: <3 months / 3–6 / Exploring |
| **Regulatory** (…960) | Licence needed: FSSAI / Import-Export (IEC) / Shops & Establishment / Other | City/state | Business already running? Yes / No |

### 6.3 CRM mapping (Leads)

| Field | Value |
|---|---|
| `Lead_Source` | **`Advt - WhatsApp`** (new value) when `ad_code` ≠ organic-wa, else `Social - WhatsApp` |
| `Meta_Ad_Type` | `ctwa` |
| `Meta_Campaign` / `Meta_Ad_Set` / `Meta_Ad_Name` | looked up from the ad-code table (6.4) |
| `CTWA_Click_ID` | `ctwa_clid` **if** Zoho confirms SalesIQ exposes it (see §7) |
| `WhatsApp_Opt_In` (new checkbox) + `Opt_In_Time` (new datetime) | from step 6 |
| `Service` / `Description` | product and Q1–Q3 answers |
| Owner | the SalesIQ chat attender (SalesIQ–CRM integration setting "owner = attender"). The CRM assignment rule for `Advt - WhatsApp` follows the same product groups. |

### 6.4 Ad-code table (pre-filled message codes)

| Code | Campaign / ad set / ad |
|---|---|
| `INC-C1`…`C4` | SIB-01 Incorporation CTWA ads 1–4 |
| `DPT-C1`, `DPT-C2` | SIB-01 DPIIT ads |
| `TM-C1`…`C4` | SIB-02 Trademark CTWA ads |
| `GST-C1`, `GST-C2`, `CFO-C1` | SIB-03 |
| `ACR-C1`…`C4`, `LLP-C1` | SIB-04 |
| `FDI-FORM` | FDI completion-screen link |
| `IF-INC`, `IF-TM`, `IF-ACR` | WhatsApp auto-message to form leads (they reply into the same bot) |

### 6.5 WhatsApp auto-message to Instant Form leads (the connectivity fix for forms)

On Lead create with `Meta_Lead_Form` not empty, send a utility template from that product's number within 60s:

> "Hi {first_name}, thanks for your enquiry about {service} with Setindiabiz. Reply here to chat with an expert now, or tap below to choose a call time." [Chat now] [Call me at…]

- **Cost:** utility template, about ₹0.115 plus GST per message.
- **Mechanism to confirm with Zoho:** SalesIQ's API or CRM-workflow route for sending a SalesIQ WhatsApp template.
- **Consent:** add one line to every Instant Form: *"I agree to be contacted by Setindiabiz on phone/WhatsApp about this enquiry."* This is the consent trail for the template.

### 6.6 Routing (product groups; names pending from you)

| Group | Numbers / bots | Agents |
|---|---|---|
| Startups & DPIIT | …509 | *to be named* |
| IPR | …905 | *to be named* |
| GST & CFO | …107 | *to be named* |
| Annual Filings | …455 | *to be named* |
| FDI | …508 | *to be named (senior: FDI ticket avg ₹46k–₹1.34L)* |
| Regulatory | …960 | *to be named* |

**Rules:**
- Only **active sales RMs** go in these pools. About 700 leads previously went to inactive or non-RM users, with almost no wins.
- **First human reply ≤5 minutes in hours.**
- "Avoiding Call" may not be used on a chat lead. A chat lead that goes silent → "Nurture" after 3 follow-ups over 5 days.

---

## 7. Attribution and CAPI — what changes in the same release

**Must change together** (or the paid segment silently undercounts):
1. Add picklist value `Advt - WhatsApp` to `Lead_Source` (Leads, Contacts, Deals).
2. Create fields: `WhatsApp_Opt_In`, `Opt_In_Time`, and `Meta_Ad_Code` (text).
3. **WF1 "Stamp Account Meta Sourced":** add `Advt - WhatsApp` to the criteria.
4. **Weekly paid-channel report and any daily watchdog:** the paid segment becomes the three values `Advt - Facebook`, `Advt - Instagram` and `Advt - WhatsApp`.
5. **CAPI sweep `sib_capisweep` and Rule 1:** keep `Advt - WhatsApp` **out** for now. Sending CTWA leads to the web dataset without `ctwa_clid` would credit the wrong ads. Document this deliberately so nobody "fixes" it.

**Phase 2 (only after Zoho confirms `ctwa_clid` is available):**
- Link the dataset to the WABA (`POST /{WABA_ID}/dataset` reuses the existing dataset).
- Send events with `action_source: business_messaging`, `messaging_channel: whatsapp`, `user_data.ctwa_clid`:
  - `LeadSubmitted` at bot completion
  - `QualifiedLead` at RM grading
  - `Purchase` on won
- Meta currently documents **purchase optimisation** for CTWA via this route. Test a Sales-objective CTWA ad set on Purchase once there are about 50 won CTWA deals a month.

**Question for Zoho support:**
> "For WhatsApp chats started from a Meta Click-to-WhatsApp ad, does SalesIQ capture the webhook `referral` object (source_id, source_url, headline, ctwa_clid)? Can a Zobot (Codeless or Plugs/Deluge) read it, and can it be pushed to a Zoho CRM Lead field? Also: do bot and agent replies inside the 72-hour free-entry window consume SalesIQ WhatsApp credits? How many Zobots does our plan allow (we need 6)?"

---

## 8. Plugins, connectors and skills — what to add (clear instructions)

**No new ad-platform plugin is needed.** The catalog's Meta tools (Adplane, Adspirer, Windsor.ai, Hyper, PaidSync) wrap the same Meta API you already have through the official Meta Ads connector. They would add another party with write access to your ad account, and none of them reads Zoho quality grades.

| # | Do this | Where | Why |
|---|---|---|---|
| 1 | **Give the connected Canva account edit access** to *2026 Ads – 1200X1200*, *Whatsapp Ads*, *Whatsapp Ads (Your Story)* and *2026 Ads – 1080 x 1350 Vertical*. Alternatively, open each design → **File → Make a copy** into the folder you shared (you then own the copy). | Canva → design → Share → add the email of the Canva account connected to Claude → **Can edit** | My copy attempts failed with "Not allowed to access design". |
| 2 | **Keep the Claude desktop app open and sign in to salesiq.zoho.com and Ads Manager in the built-in browser** when we build. | Desktop app | No Zoho SalesIQ connector exists, so the Zobots are built through the browser. The same applies to any ad-level edits the API blocks. |
| 3 | **Disconnect Supermetrics.** | claude.ai → Settings → Connectors → Supermetrics → Disconnect | Trial lapsed in July and it confuses tool choice. |
| 4 | **SalesIQ:** turn on **Auto-refill** for WhatsApp credits (balance is 10). Confirm the plan allows 6 bots (Professional = 5, Enterprise = 10 per Zoho's pricing page). | SalesIQ → Settings → WhatsApp → Auto-refill; Settings → Subscription | Bots stop when credits or plan limits run out. |
| 5 | **Meta Business:** confirm each of the 6 numbers shows under the Page **setindiabiz.official → Linked accounts → WhatsApp**, with display names approved. Accept the Lead Ads Terms again at facebook.com/legal/leadgen/tos. | Meta Business Suite | CTWA needs the number linked to the Page. The ToS is the old ad-level API block (error 1815089). |
| 6 | **Funding:** add a card for auto-pay, or keep a ≥7-day balance (about ₹1.24L). | Ads Manager → Billing | Removes blackouts. |
| 7 | **Raise the Zoho support ticket** in §7 and forward me the reply. | Zoho support | Decides Phase 2 CAPI. |
| 8 | Nothing to install for skills. These are already available and will be used: `product-legal:marketing-claims-review` (every ad), `canva:edit-design` / `canva:resize-for-social-media` / `canva:brand-check`, `small-business:speed-to-lead`, `data:statistical-analysis` (A/B verdicts). | — | — |
| 9 | After launch, I create a **cloud scheduled task "Meta daily watchdog"** (cheap model, 08:15 IST) covering delivery, balance runway, CTWA→CRM capture rate, first-reply SLA and stop-losses. | I do this | The old watchdog hasn't written a file since 13 Aug. |

---

## 9. Sales-process guardrails (the bigger lever)

| Rule | Metric | Target |
|---|---|---|
| First human reply on WhatsApp | median minutes, in hours | ≤5 min |
| Form leads get the WA auto-message | % within 60s | ≥98% |
| CTWA chats captured as CRM leads | CRM leads ÷ Meta conversations | ≥90% (May was 0%) |
| No "Avoiding Call" without evidence | 6 logged attempts over 5 days on 2 channels | 100% |
| Stale pipeline | Proposal/Negotiation >14 days reviewed weekly | 0 unreviewed |
| Pools | only active sales RMs receive paid leads | 100% |

---

## 10. Stop-loss and review cadence

| Check | Rule |
|---|---|
| Daily (watchdog) | Pause an ad set if 3-day CPL/cost per conversation is >2× its ceiling, or 2 spend days pass with 0 CRM leads (capture failure). |
| Ceilings (cost per lead or per conversation) | TM ₹170 · Incorporation ₹220 · ACR ₹500 · GST/CFO ₹300 · DPIIT ad within Startups ₹350 · FDI: no ceiling for 30 days (KPI = qualified meetings) |
| Day 7 | Creative rotation (frequency >2.5 → swap); placement check. |
| Day 14 | CTWA vs Form verdict per product (§3). |
| Day 30 | Cost per won by product; FDI go/no-go; budget re-split. |
| 30 Oct / 29 Nov | ACR creative switch; ACR wind-down. |

---

## 11. Build sequence

| Step | Who | When |
|---|---|---|
| Fund account / auto-pay; SalesIQ auto-refill; Canva edit access; agent names; Zoho ticket; confirm CFO & GST prices | Sanjeev | Today |
| Creatives (Canva copies + fixes, 1:1 and 9:16) → claims review → your approval | Claude | Next session |
| CRM: picklist value, 3 fields, WF1 criteria, report filters | Claude (connector + browser) with your approval | Next session |
| Zobots ×6 (Codeless), routing, CRM webhook, form-lead WA template | Claude via built-in browser, you approve | Next session |
| Meta: 5 campaigns built **as drafts** (draft mode is on, so nothing spends) → your review → publish | Claude, you approve | Next session |
| End-to-end test: tap own ad preview → WhatsApp → bot → CRM lead with ad code → agent gets chat | Both | Before publish |
| Watchdog scheduled task | Claude | Launch day |

---

## 12. Open items for Sanjeev
1. Agent names per product group (§6.6) and working hours.
2. Prices to show: confirm **TM ₹1,999 · Incorporation ₹2,499 · ACR bundle ₹7,499 (6 filings) · DPIIT ₹4,999 · Accounting/GST from ₹750/month**. Still needed: **GST return** price and **Virtual CFO** monthly price.
3. Median incorporation turnaround from ops data, before any "7 days" claim.
4. One provable customer-count number for creatives, or drop it.
5. Do you want a Regulatory campaign later? Its bot is built regardless.
