# Creatives: chat 23, Company + LLP C1 and WA1 (stated date 16–18 Jan 2026)

_Source: `PPC/imports/chatgpt/conversations/23-facebook-ads-campaign-setup.md` · https://chatgpt.com/c/51e64239-3af4-8333-9b24-c02335df21aa_

**How to use this file**
- Text is verbatim. Backslash escapes from the export were removed in code blocks. Each asset is tagged with its turn.
- "FINAL" means the chat confirms the asset was used, or it is the last version given (that is said where it applies).
- Ad account: SETINDIABIZ (152154124583473). Dataset: Setindiabiz JS.
- Before reuse, confirm live state via the Meta Ads connector.

---

## 1. Campaign and ad set settings

**C1 campaign + ad set, turn 4 (chat 23, 16 Jan 2026). First version; turns 5/10 revised location and budget**
- Campaign Name: `C1 | India | Company & LLP Registration | Advantage+`
- Buying Type: Leave as Auction · Advantage+ Campaign Budget: ON · Budget type: Daily · Amount: ₹1,300 per day (~₹40,000 / month)
- Special Ad Categories: ❌ NONE selected · A/B Test: ❌ OFF
- Ad Set Name: `AUTO | India | Founders & Entrepreneurs`
- Performance Goal: Maximize number of leads · Conversion Event: Select Lead (Source should show Pixel + Conversions API)
- Location: Delhi NCR, Mumbai, Bengaluru, Hyderabad, Chennai, Pune, Ahmedabad · Age: 24 – 55 · Gender: All
- Detailed Targeting: ❌ Leave COMPLETELY EMPTY · Placements: Select Advantage+ placements, Everything ON
- Attribution setting: 7-day click / 1-day view (default is fine)

Status: verify "Special Ad Categories NONE". Meta's categories have broadened (e.g. Financial products and services), and the WA1 ad hit a securities/investments declaration (turns 43–47).

**Conversion location, turn 5 (chat 23, 16 Jan 2026). FINAL for C1**
- "Ad Set A (Primary): Website and instant forms (covers landing page + lead form in one ad set, fully AI-optimized)"
- "Pixel: Select Setindiabiz JS (1242417817083521)"; "Conversion event: Select Lead"; "Performance goal: Maximise number of leads (keep as-is)"

**As built (from Sanjeev's screens, 16–18 Jan 2026)**
- C1 daily budget: ₹2,500 kept (turn 10). The screen showed ₹3,500 at turn 24, and this is unresolved.
- Minimum age 24 (turn 11). Locations: metro list recommended; actual list not confirmed.
- Names (turn 41): `IN | C1 | Company+LLP | Leads | …`; ad sets `IN | C1 | Forms | Metros | Broad` and `IN | C1 | Web | Metros | Website-First`.

**Website-First ad set, turn 25 (chat 23, 18 Jan 2026)**
- `AUTO | India | Website-First | Company+LLP`. Campaign conversion location: Website and instant forms.
- Ads: `C1 | Web | Register Today | W1` (company-registration-1.jpg); `C1 | Web | Pricing | W2` (company-registration-1 Pricing.jpg)
- "Website-first ad set: ₹1,000/day"; "Form ad set: ₹2,500/day (or reduce slightly)"; "Ad set minimum spend (if available) on Website-first: ₹800–₹1,200/day."

**Value rules, turn 27 (chat 23, 18 Jan 2026). FINAL; Sanjeev confirmed +20% / −30% at turn 29**
- Rule 1 (Instant forms): Criteria: Conversion location → Instant forms · Action: Decrease bid by 30% · Rule name: `Downweight - Instant forms (-30%)`
- Rule 2 (Website): Criteria: Conversion location → Website · Action: Increase bid by 20% · Rule name: `Upweight - Website (+20%)`
- Rule set name (turn 28): `C1 | Prefer Website (+20/-30)`

**WA1 WhatsApp campaign, turn 41 (chat 23, 18 Jan 2026), with settings confirmed on screen at turns 42–47**
- Campaign name: `IN | WA1 | Company+LLP | Messages | WhatsApp`. Ad set name: `IN | WA | Metros | BusinessHours`
- On screen: "Objective = Engagement; Ad set budget; Campaign bid strategy = Highest volume; A/B test OFF; Special Ad Categories None"; "Conversion location = Message destinations; WhatsApp selected; ₹2,000/day; minimum age 24; WhatsApp Status unticked"
- Turn 41 budget guidance: "Set ₹2,000/day for first 48–72 hours. If cost per WhatsApp conversation is ≤ ₹120 and quality is fine → increase to ₹2,500/day"
- Locations (turn 41): "Delhi NCR, Mumbai, Bengaluru, Hyderabad, Chennai, Pune, Ahmedabad, Kolkata (use whatever you already used in C1 metros)"
- Turn 33 guidance: "Untick: "Share some of your budget with other ad sets""; "Scaling rule: increase in steps of 15–25% per day, not all at once."

**Detailed targeting suggested for WA, turn 32 (chat 23, 18 Jan 2026). Not confirmed used; turn 41 says "Keep broad"**
Entrepreneurship · Startup company · Small business owners · Business registration · Company registration · GST registration (optional) · Founder / CEO / Director (if job titles available)

**Lower-competition geo ad set, turn 22 (chat 23, 17 Jan 2026). Not implemented**
- Ad set: `AUTO | India | Tier2 + NE + J&K | Exclude Metros`
- Option 1: "Include: India. Exclude: Delhi NCR, Mumbai, Bengaluru, Hyderabad, Chennai, Pune, Ahmedabad, Kolkata (and optionally Jaipur/Surat if you want them separate)"
- A) Jammu, Srinagar, Anantnag, Baramulla, Leh (Ladakh)
- B) Guwahati (Assam), Silchar (Assam), Shillong (Meghalaya), Agartala (Tripura), Imphal (Manipur), Aizawl (Mizoram), Kohima / Dimapur (Nagaland), Itanagar (Arunachal Pradesh)
- C) "Pick 12–18 from this list (don't add 50 at once)":
  - North / Central: Chandigarh – Mohali – Panchkula (Tri-city), Jaipur, Indore, Bhopal, Lucknow, Kanpur, Nagpur, Surat, Vadodara, Rajkot
  - West / South: Coimbatore, Madurai, Kochi, Thiruvananthapuram, Visakhapatnam, Vijayawada, Bhubaneswar, Raipur, Ranchi, Patna
- D) Baddi (HP) / Solan belt; Pantnagar / Rudrapur (Uttarakhand); Vapi / Ankleshwar (Gujarat); Aurangabad / Nashik belt (Maharashtra)
- "Set Tier-2 ad set at 30% of spend initially"; extra form qualifier: "Business type" (Startup / Trading / Services / Manufacturing)

---

## 2. Instant form: `C1 | Company+LLP | Higher Intent | v1`

**Turn 12 (chat 23, 16 Jan 2026). Second version; form selected on Ad 1 per turn 16**
- Form type: ✅ Higher intent (not "More volume")
- Intro screen: Title: Company / LLP Registration · Text: Share your details. Our team will call you to confirm eligibility, documents, fees and timeline.
- Contact fields: Full name · Email · Phone number
- Custom question 1 (Multiple choice): Which service do you need? → Company Registration / LLP Registration / Not sure
- Custom question 2 (Multiple choice – qualification): When do you plan to start? → Immediately (0–7 days) / In 1–2 weeks / Just exploring
- Optional: "If there is an "City" field available, include it. If not, add a short answer question: Your City"
- Thank-you screen: Message: Thank you. Our expert will contact you shortly. · Button: Visit website · URL: https://www.setindiabiz.com/lp/company-registration

Turn 8, first version: the intro text was "Share your details. Our expert will call you shortly to confirm eligibility, documents, fees and timeline."

**Form disclosure, turn 13 (chat 23, 16 Jan 2026). Full version; the version actually pasted is not stated**
> "By submitting this form, you consent to be contacted by Setindiabiz Private Limited via phone, WhatsApp, SMS or email for consultation and service updates. Your details will be used to evaluate eligibility, share document checklist/fees/timeline, and create a lead record in our CRM. We do not sell your personal information to third parties. See our Privacy Policy for more."

Short version: "Your details will be used to contact you about Company/LLP registration and to create a lead record in our CRM. We do not sell your data. See Privacy Policy."

Third version (turn 21, given after the form was live; use not confirmed):
> "By submitting this form, you agree that Setindiabiz may contact you by phone, email or WhatsApp regarding company/LLP registration and related compliance services. Your details will be used only to respond to your enquiry and may be stored in our CRM for follow-up. We do not sell your personal information. We may share it internally with our authorised team/service partners strictly for fulfilling your request, where required."

Compliance: these support DPDP s. 5 notice / s. 6 consent and TCCCPR 2018 consent for promotional calls and SMS. Keep them aligned with the site privacy policy, and verify the current DPDP Rules 2025 phasing and the current TCCCPR amendment.

**Thank-you page, turn 14 (chat 23, 16 Jan 2026). Full version; pasted version not stated**
> "Thank you. We have received your details. Our incorporation expert will call you within 1 business hour to confirm eligibility, fees and the document checklist. For faster assistance, keep your PAN/Aadhaar (or Passport for NRIs) and proposed company/LLP name options handy."

Short: "Thank you. Our expert will call you within 1 business hour with eligibility, fees and document checklist. Please keep your ID details and 2–3 name options ready."

Third version (turn 21): "Thank you—your request has been received. Our incorporation team will review your details and reach out with the next steps for name finalisation, DSC/DIN and incorporation documents. To speed things up, please keep ready: (1) 2–3 proposed company names, (2) director PAN/Aadhaar, (3) registered office address proof."

Compliance: "within 1 business hour" is a service promise (CPA 2019 s. 2(28)), so meet it or soften it. The turn 21 version avoids it.

---

## 3. Instant Form ads (ad set Forms)

Creatives (Sanjeev's 1080×1080 files, as named in chat 23):
- `company-registration-1 Pricing.jpg` (₹3499)
- `company-registration-1.jpg` ("Register Your Company Today")
- `company-registration-2.jpg`
- `company-registration-3.jpg` ("Clean blue, ₹3499 inside but more "brand"")
- `company-registration-4.jpg` ("Company Registration in India / 100% Online"; "Rated/10,000+ businesses")

Claims on the creatives: "₹3499/-" and "4.8/5 Rated by 10,000+ Businesses".

Compliance:
- The ₹3,499 price must appear on `/lp/company-registration`. business-context.md says no package prices are published (CPA 2019 s. 2(28); CCPA Guidelines 2022).
- The "4.8/5 … 10,000+" rating needs dated evidence. The site says "4.8 Google rating" and "18K+ clients", and both are TODO (ASCI Ch. I.1). The turn 65 report itself said "if you claim ratings, you should be able to substantiate if asked."

**F1: Pricing, turn 15 (chat 23, 16 Jan 2026). FINAL (turn 16 read this primary text from screen, CTA Get quote); renamed `IN | Form | Pricing | F1`**
- Ad name: `C1 | Form | Pricing | Creative-01` · Upload image: company-registration-1 Pricing.jpg
- Primary text: Register your Private Limited Company online with expert support. Professional fee from ₹3,499 (Govt fees extra). Get document checklist, fees and timeline on call.
- Headline: Company Registration – From ₹3,499*
- Description: Expert callback · CTA: Apply Now / Get Quote · Instant Form: C1 | Company+LLP | Higher Intent | v1

Compliance: price claim. See the note above.

**F2: Register Today, turn 18 (chat 23, 16–17 Jan 2026). Last version given; renamed `IN | Form | Register Today | F2`**
- Ad name: `C1 | Form | Register Today | Creative-02` · Creative: company-registration-1.jpg
- Primary text: Start your Private Limited Company with expert support. Eligibility, DSC/DIN and filing guidance included. Share your details to get a callback.
- Headline: Register Your Company Today · Destination: Instant form · CTA: Get Quote / Apply Now

Turn 15 first version of the primary text: "Start your Private Limited Company with a guided process—eligibility, documents, DSC/DIN and filing support. Share details to get a callback."

**F3: 100% Online, turn 19 (chat 23, 16–17 Jan 2026). Last version given; creative used not stated; renamed `IN | Form | 100% Online | F3`**
- Ad name: `C1 | Form | 100% Online | Creative-03` · Creative: company-registration-4.jpg, or company-registration-2.jpg or company-registration-3.jpg (non-rating options)
- Primary text: 100% online company registration support across India. Get eligibility check, document checklist, fees and timeline from our expert. Share your details for a callback.
- Headline: Company Registration – 100% Online · Description: Expert callback · CTA: Get Quote (or Apply Now)

Compliance: if company-registration-4.jpg is used, the rating-claim note applies. "100% online" must hold, because some steps may need physical documents.

**Form-ad website URLs (fixes "The link field is required"), turn 20 (chat 23, 17 Jan 2026). Errors cleared at turn 21**
```
https://www.setindiabiz.com/lp/company-registration?utm_source=meta&utm_medium=paid_social&utm_campaign=C1_company_llp&utm_content=pricing
https://www.setindiabiz.com/lp/company-registration?utm_source=meta&utm_medium=paid_social&utm_campaign=C1_company_llp&utm_content=register_today
https://www.setindiabiz.com/lp/company-registration?utm_source=meta&utm_medium=paid_social&utm_campaign=C1_company_llp&utm_content=online
```
Turn 29 last-given variants use `utm_content=form_pricing`, `form_register_today` and `form_online` (use not confirmed).

URL parameters template (turn 21): `utm_source=facebook&utm_medium=paid_social&utm_campaign={{campaign.id}}&utm_adset={{adset.id}}&utm_ad={{ad.id}}&utm_placement={{placement}}`

---

## 4. Website ads (ad set Website-First). Published per turn 31

**W1: Register Today, turn 30 (chat 23, 18 Jan 2026). FINAL set; ChatGPT recommended Option A + Headline 1 + Description 1 + Learn More; option pasted not stated**
- Primary Text (Option A – balanced): Start your Private Limited Company with expert support—eligibility check, DSC/DIN guidance, and end-to-end filing. Get the checklist, fees and timeline. Click to proceed online.
- Primary Text (Option B – stronger CTA): Ready to incorporate your Pvt Ltd company? Get a quick eligibility check and document checklist from our team. Transparent process, expert guidance, 100% online. Click to get started.
- Headlines: Register Your Company Online · Start a Pvt Ltd Company · Company Registration in India
- Descriptions: Get checklist & timeline · Expert callback · Start online in minutes
- CTA: Learn More (preferred for website) (or Get Quote if that matches your page better)
- URL: `https://www.setindiabiz.com/lp/company-registration?utm_source=meta&utm_medium=paid_social&utm_campaign=C1_company_llp&utm_content=web_register_today`

**W2: Pricing, turn 30 (chat 23, 18 Jan 2026). FINAL set; recommended Option A + Headline 1 + Description 1 + Get Quote; option pasted not stated**
- Primary Text (Option A – compliant & clear): Register your Private Limited Company with professional fee from ₹3,499. Government fees and stamp duty are extra as applicable. Click to see eligibility, documents and timeline.
- Primary Text (Option B – conversion focused): Professional fee from ₹3,499 for Pvt Ltd registration (Govt fees extra). Get the document checklist, name options guidance and filing support. Click to start online.
- Headlines: Pvt Ltd Registration From ₹3,499* · Company Registration – Low Fee* · Start Company Registration
- Descriptions: *Govt fees extra · Check eligibility online · Get timeline & checklist
- CTA: Get Quote (best for price-led) (or Apply Now if available and you prefer a stronger push)
- Optional one-line disclaimer: Government fees and stamp duty are additional and depend on state and authorised capital.
- URL: `https://www.setindiabiz.com/lp/company-registration?utm_source=meta&utm_medium=paid_social&utm_campaign=C1_company_llp&utm_content=web_pricing`

Compliance: price claim (see above). "Low Fee*" is a comparative claim that needs substantiation (CCPA Guidelines 2022; ASCI Ch. IV).

**Optional pause rule, turn 31 (chat 23, 18 Jan 2026). Not confirmed created**
Rule: Pause expensive website ads · Apply to: Website ads (W1/W2) · Condition: Cost per result (Lead) > ₹1,800 AND Results ≥ 3 · Action: Turn off ad · Time: Continuous

Status: SUPERSEDED. A ₹1,800 threshold is far above the CRM revenue per Facebook lead of ₹271 (business-context.md, Nov 2025–Oct 2026).

---

## 5. WhatsApp ads (WA1). "Create all the three ads" (turn 54); publication not separately confirmed

**Three WhatsApp ads, turn 53 (chat 23, 18 Jan 2026). FINAL as last version given; Sanjeev said Yes to all three angles**
- **A1 Pricing**: Ad name `IN | WA1 | Pricing | A1` · Creative: company-registration-1 Pricing.jpg (₹3,499)
  - Primary Text: Private Limited Company registration starting at ₹3,499. / Chat on WhatsApp to get exact fee breakup, timeline and document checklist. / Share your City/State to begin.
  - Headline: Chat on WhatsApp · Description: Fees + checklist + timeline (9:30 AM–7:30 PM IST).
  - Compliance: price claim, and the A1 text omits "(Govt fees extra)". Add it.
- **A2 Register Today**: Ad name `IN | WA1 | RegisterToday | A2` · Creative: company-registration-2.jpg (Register Today)
  - Primary Text: Register your Company or LLP with Setindiabiz. / Message us on WhatsApp for step-by-step guidance and document checklist. / Share your City/State + when you want to start.
  - Headline: Start on WhatsApp · Description: Fast response during business hours.
- **A3 Trust / 100% Online**: Ad name `IN | WA1 | 100Online | A3` · Creative: one of company-registration-4.jpg (Rated/10,000+ businesses), company-registration-3.jpg (100% online all India), company-registration-1.jpg (same style as pricing but no price)
  - Primary Text: 100% online Company/LLP registration — All-India service. / Chat on WhatsApp to get checklist, fees and expected timeline. / Our team will guide you end-to-end.
  - Headline: Company/LLP Registration · Description: Share your city & requirement on WhatsApp.
  - Compliance: if company-registration-4.jpg is used, the rating needs substantiation.
- All three: Destination: WhatsApp · CTA: Send WhatsApp message · Chat template: the same template already built.

**Other WA primary texts, turns 41/44/52 (chat 23, 18 Jan 2026). Alternates**
- Turn 41: Need help registering a Private Limited Company or LLP in India? Chat with our expert team on WhatsApp for eligibility check, document checklist, fees and timeline. 100% online process.
- Turn 44, Text 2: Starting a business? Get your Company/LLP registered in India. WhatsApp us for a quick checklist + exact fee quote + expected timeline.
- Turn 44, Text 3: Company Registration starting @ ₹3,499. Chat on WhatsApp to confirm eligibility, documents and total govt + professional fee breakup.
- Turn 52:
  - "Register your Private Limited Company or LLP with Setindiabiz. Chat on WhatsApp for fees, timeline and document checklist."
  - "Starting a business? Get step-by-step guidance for Company/LLP registration. Message us on WhatsApp to begin."
  - "Need MCA filing support for Company/LLP registration? WhatsApp us—our team shares checklist + estimated timeline."
  - "Quick assistance on Company/LLP registration. Message on WhatsApp—share your city and requirement."
- Turn 52 headlines: "Company/LLP Registration" · "Get Fees & Checklist" · "Start on WhatsApp"
- Turn 52 descriptions: "Share your city & requirement. Our team replies 9:30 AM–7:30 PM IST." · "Get checklist + fees + timeline on WhatsApp. Reply in minutes during business hours."
- WA URL parameters (turn 52): `utm_source=meta&utm_medium=whatsapp&utm_campaign=IN_WA1_CompanyLLP&utm_content={{ad.name}}`

Compliance: "Need MCA filing support" must not imply MCA affiliation. Keep "support". "Reply in minutes" is a service promise.

**Chat Builder welcome, turn 51 (chat 23, 18 Jan 2026). FINAL as last version given; turn 52 read a welcome message with business hours + FAQ buttons from his screen**
> Hi! Welcome to Setindiabiz. Please reply with:
> 1 = Company Registration
> 2 = LLP Registration
> Also share your City/State + when you want to start (This week / 15 days / 30 days).
> (Team hours: 9:30 AM–7:30 PM IST. Outside hours, share details and we will call back.)

- Call to action: Get quote (preferred). If "Get quote" is not available, choose "Get started".
- FAQs: 1 - Company Registration · 2 - LLP Registration · Fees & timeline · Send document checklist
- Template names given: `IN | WA1 | Start Conversations | 18-01-2026` (turn 48); `IN | WA1 | Company+LLP | StartConv | 18-01-2026` (turn 50)

Compliance: there is **no explicit marketing opt-in (YES/STOP)** in this greeting. Before sending any marketing template outside the 24-hour window, add one (WhatsApp Business Messaging Policy; DPDP s. 6). See chat 24 and `meta/whatsapp-ads-compliance-notes.md`.

**Zobot / SalesIQ spec, turns 50–51 (chat 23, 18 Jan 2026). Recommended; not confirmed built**
- Name: `Zobot - Meta WA - Company/LLP`
- Trigger on first inbound message containing: 1, 2, "Company", "LLP", "fees", "checklist"
- First 4 questions: Service selection (Company vs LLP) · City/State · Timeline (This week / 15 days / 30 days) · Phone + Email (or just Phone, then email later)
- In hours: "Connecting you to an expert now." Outside hours: "Thanks. Our team will call you tomorrow between 9:30 AM–11:30 AM IST."
- CRM creation: "Lead Source = Meta - WhatsApp"; "Campaign = IN | WA1 | Company+LLP"; hidden tags "SourceCampaign = IN_WA1", "Adset = Metros_BusinessHours"

Status: the Lead Source "Meta - WhatsApp" is **SUPERSEDED** by the CRM canonical `Advt - WhatsApp` (business-context.md). The same applies to LeadChain's "Set Lead Source = Facebook Lead Ads" (turn 21), whose canonical value is `Advt - Facebook`.

---

## 6. Naming and automated rules

**Naming convention, turn 40 (chat 23, 18 Jan 2026). FINAL for the IN | names; tag later changed to #IND**
- Campaign `IN | <Service> | <Objective> | <Channel> | <Version>` · Ad set `IN | <Audience/Geo> | <Intent> | <Placement>` · Ads `IN | <Channel> | <Angle> | <Creative#>`
- Renames: `IN | C1 | Company+LLP | Leads | Advantage+`; `IN | C1 | Forms | Metros | Broad`; `IN | C1 | Web | Metros | Website-First`; F1/F2/F3; W1/W2; `IN | WA1 | Company+LLP | Messages | WhatsApp`; `IN | WA | Metros | BusinessHours`; `IN | WA | Checklist+Timeline | WA1`
- #IND examples (turn 56): `#IND | C1 | Company+LLP | Leads | Advantage+` · `#IND | C1 | Web | Metros | Website-First` · `#IND | WA1 | Company+LLP | Messages | WhatsApp`

Note: the repo naming convention (`PPC/CLAUDE.md`) is `<Platform>_<Objective>_<Service>_<Geo>_<Audience>_<YYYYMM>`. Any rename must keep `#IND`, or the rules stop matching.

**Business-hours rules, turns 61–63 (chat 23, 18 Jan 2026 or later). FINAL; applied to all #IND per turn 63**
- Rule 1 — ON: `#IND | BusinessHours | ON | 09:30-19:00 IST` · Apply rule to: All paused campaigns · Condition: Campaign name contains #IND · Action: Turn on campaigns · Schedule: Custom; Mon–Sun; 09:30 to 19:00
- Rule 2 — OFF: `#IND | BusinessHours | OFF | 19:30 IST` · Apply rule to: All active campaigns · Condition: Campaign name contains #IND · Action: Turn off campaigns · Schedule: Custom; Mon–Sun; 19:30 to 19:30
- On screen at turn 62, and in the turn 65 report, the ON rule name still read `#IND | BusinessHours | ON | 09:30-19:29 IST`.
- Meta UI text quoted at turn 57: "If the start and end time are the same, then the rule will run once per day within 30–60 minutes after the set time."

Risk: there is no `#HOLD` exclusion, so the ON rule turns on **any** paused #IND campaign, including ones paused on purpose. Proposed at turns 35/40/64; not done.

**Spend cap rule, turn 64 (chat 23). Not implemented (skipped at turn 65)**
- Rule name: `#IND | SpendCap | OFF | C1 | ₹2600` · Action: Turn off campaigns · Conditions: Campaign name contains #IND; Campaign name contains C1 (or WA1 etc.); Amount spent → today → greater than ₹2,600 · Schedule: Continuously · Hold tag: #HOLD (Campaign name does not contain #HOLD)
- Budget allocation: "C1 Leads campaign: ₹2,500/day"; "WA1 WhatsApp campaign: ₹2,000/day"; "Total = ₹4,500/day"; "When you add another #IND campaign, allocate ₹1,500–₹2,000/day"

---

## 7. Instant form spec from the four-campaign plan, turn 1 (chat 23, 16 Jan 2026). Superseded by the C1 form above
- Form Type: Higher Intent (NOT "More volume")
- Fields (MANDATORY): Full Name · Email · Phone · City · Service Type (Dropdown – prefilled per campaign)
- Custom Question (1 only): "Are you looking to start immediately or just exploring?"
- Campaign names planned: `C2 | Global | India Entry & Subsidiary | Advantage+` (USA, UK, Canada, UAE, Singapore, Australia, Germany, France; English; completely broad) · `C3 | Global | Trademark Registration | Advantage+` · `C4 | India | GST Compliance | Advantage+` ("Increase budget +30% between 20th–31st of filing months")
- Distribution: C1 30% · C2 25% · C3 20% · C4 25% of "₹160,000 (as approved)"
- Scaling Rule: "If CPL stable for 3 days → increase 20%" · "Never more than once every 48 hours"
