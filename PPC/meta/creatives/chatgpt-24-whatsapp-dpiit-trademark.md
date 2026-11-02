# Creatives: chat 24, Click-to-WhatsApp for directors, Trademark and DPIIT (stated date 3 Oct 2025)

_Source: `PPC/imports/chatgpt/conversations/24-whatsapp-ads-compliance-guide.md` · https://chatgpt.com/c/6f422795-2d1c-832c-ac76-7ba67e9f11ff_

**How to read this file**
- All text is verbatim. "ð" is a corrupted emoji from the import, and backslash escapes were removed in code blocks.
- None of these assets is confirmed live. Sanjeev made DPIIT creatives (turn 8) and reached campaign setup (turn 9). The Trademark kit was parked behind DPIIT (turn 7).
- Rules and sources: `meta/whatsapp-ads-compliance-notes.md`.

**Status**
- Detailed-targeting specs (job titles, interests, exclusions): **OUTDATED / verify**. Meta has removed or merged many options since 2024–25. Chat 23 (Jan 2026) ran broad.
- Fee placeholders are unfilled.
- Trust figures are unsubstantiated and inconsistent: "50k+ filings" in turn 4, "1,00,000+ filings" in turns 5 and 7, "15+ yrs" against the site's "20+ years".

---

## 1. Director CTWA ads, turn 4 (chat 24, 3 Oct 2025)
Objective: Engagement → Messaging (WhatsApp)

**Variant A — "Talk to a CA now"**
- Primary text: "Director? Need quick clarity on annual ROC filings & GST this month. Chat with a compliance expert on WhatsApp in under 2 minutes."
- Headline: "WhatsApp a Compliance Expert" · Description: "Real answers. No forms." · CTA: Send WhatsApp Message
- Creative: clean banner "Talk to a CA now" + trust badges (50k+ filings, PAN-India)
- Compliance:
  - "Talk to a CA now" is accurate only if a Chartered Accountant actually answers. ICAI advertising limits may apply; verify current version.
  - "in under 2 minutes" is a service promise.
  - "50k+ filings" is unsubstantiated (ASCI Ch. I.1).

**Variant B — "Director's WhatsApp Checklist"**
- Primary text: "Grab the Director's Monthly Checklist on WhatsApp — filings, due dates, penalties, and tips tailored to your company type."
- Headline: "Get the Checklist on WhatsApp" · Description: "Instant. Free." · CTA: Send WhatsApp Message
- Creative: checklist graphic (AOC-4, MGT-7A, TDS, GST, EPF/ESI)

**Variant C — "Missed a deadline?"**
- Primary text: "Worried about late fees or non-filing? Chat now for a 10-min triage and action plan."
- Headline: "Fix It on WhatsApp" · Description: "Talk to a human." · CTA: Send WhatsApp Message
- Creative: alert-style card "Avoid ₹100/day late fees"
- Compliance: check the ₹100/day figure against the current Companies (Registration Offices and Fees) Rules, 2014 before use. Verify current version.

**Primary text, turn 1:** "Director or CS? Get an instant checklist for October ROC + GST deadlines on WhatsApp. Tap Send WhatsApp to chat with our expert now."

**Audience setup, turn 4 (for showing ads, not broadcasting)**
- Prepare CSV with phone numbers in E.164 (e.g., +9198XXXXXXXX) and/or emails.
- Create Customer List Custom Audience from that CSV.
- Optional: build 1–2% Lookalikes from people who started WhatsApp chats ("Messaging Conversations Started").
- Layer B2B filters (job titles: Director/MD/Founder, interests: Compliance/Accounting) to expand if match rate is low.
- Compliance: the director list needs a documented lawful basis before upload (DPDP Act 2023 ss. 4–6; Meta Custom Audience Terms). Turn 1 itself says "Don't upload scraped or purchased lists". Never commit the list to this repo.

**WhatsApp pieces, turn 4**
- Auto-reply: "Hi {{first_name}} ð You're chatting with Setindiabiz. / Reply YES to get checklists, reminders & offers on WhatsApp. Reply STOP to opt out anytime."
- Quick replies: Pricing · Talk to Expert · Send Docs · Free Checklist
- Marketing template `director_monthly_checklist_v1` (Category: Marketing). Body: "Hi {{1}}, your Director's Monthly Compliance Checklist is ready: {{2}}. / Need help filing AOC-4/MGT-7A? Reply HELP or tap a button." Buttons: "Talk to Expert" (Quick reply), "Book a Call" (URL), "Unsubscribe" (Quick reply). Variables: {{1}} = first name, {{2}} = short link to your checklist.
- Utility template `consult_booking_confirm_v1` (Category: Utility). Body: "Hi {{1}}, your consultation is booked for {{2}}. We'll WhatsApp you 10 min before. Reply RESCHEDULE to change." Buttons: "Add to Calendar" (URL)
- KPIs: New messaging conversations (primary KPI) · Cost per conversation started · Reply rate within 24h · Opt-in rate ("YES" rate) · Booked calls / paid filings from chat

---

## 2. Trademark Registration CTWA, turn 5 (chat 24, 3 Oct 2025). Pending (parked at turn 7)

**Campaign setup**
- Objective: Engagement → Messaging (destination: WhatsApp)
- Optimization: Conversations (Messaging conversations started)
- Bid strategy: Lowest cost
- Placements: Advantage+ (FB Feed, IG Feed, Reels, Stories; allow WA Status if available)
- Tracking: `?utm_source=meta&utm_medium=c2w&utm_campaign=tm_india_{adset_name}&utm_content={ad_name}`

**Ad Set A — Founders/Directors (Tier-1 metros)** · Budget: 40% of total
- Location: Delhi-NCR, Mumbai, Bengaluru, Hyderabad, Pune, Chennai, Kolkata, Ahmedabad · Age/Lang: 23–55, English & Hindi
- Audience: Job titles: Founder, Co-founder, Director, CEO, Proprietor, Partner. Interests: Entrepreneurship, Startups, MCA, DPIIT, Legal services, Accounting, Small business.
- Exclusions: Existing customers (your uploaded list), 30-day engagers
- Primary text V1: "Founder? Lock your brand before someone else does. Trademark filing starts today—class search, docs & MSME discount guidance on WhatsApp."
  - Headline: "Trademark Registration – Start Now" · Description: "Free class search in 2 mins" · CTA: Send WhatsApp Message
- Primary text V2 (Hinglish): "Brand banaya? Ab TM file karo. Free class check + docs list WhatsApp par. Reply 'START'."
  - Headline: "Protect Your Brand Name" · CTA: Send WhatsApp Message
- Creative ideas: Clean badge "™ Register Now", checklist tile (Search → Class → File → Objections → Hearing), trust strip "1,00,000+ filings | PAN-India".
- Compliance:
  - The "™ Register Now" badge and "Protect Your Brand Name" must not imply that registration is guaranteed. Registration depends on examination by the Trade Marks Registry.
  - "1,00,000+ filings" is unsubstantiated.
  - Using "MCA" / "DPIIT" as interests is fine, but they must not appear in the copy as an affiliation.

**Ad Set B — E-commerce Sellers** · Budget: 25%
- Location: Pan-India (Tier-1 & Tier-2) · Audience: Interests: E-commerce, Online marketplace, Shopify, WooCommerce, D2C, Logistics/fulfilment; Job titles: E-commerce Manager, Store Owner.
- Primary text V1: "Selling online? Get your Trademark Application Number fast so your brand stays yours. Free class search on WhatsApp."
  - Headline: "TM for Online Sellers" · Description: "Fast filing. Pro support." · CTA: Send WhatsApp Message
- Primary text V2: "Stop me-too listings. Register your brand name & logo. Chat now for class check + timeline."
- Creative ideas: Product photo grid with padlock/™ overlay; "Stop copycats" hook.
- Compliance: "so your brand stays yours" and "Stop me-too listings" overstate what a filed application does. An application number is not registration (CCPA Guidelines 2022).

**Ad Set C — MSME Manufacturers & Services** · Budget: 25%
- Location: Industrial hubs (Rajkot, Surat, Indore, Ludhiana, Jaipur, Coimbatore, Hosur, Faridabad, Noida, Pimpri-Chinchwad, etc.)
- Audience: Interests: MSME, Manufacturing, Packaging, Branding, Export/Import; Job titles: Owner, Managing Director, Plant Head.
- Primary text V1: "Your label = your reputation. Trademark your brand & packaging. Get class mapping + fees breakup on WhatsApp."
  - Headline: "Trademark for MSMEs" · Description: "Free class mapping" · CTA: Send WhatsApp Message
- Primary text V2 (Hinglish): "Duplicate se bachna hai? TM register karo. Docs list abhi WhatsApp par."
- Creative ideas: Before/after shelf visual; "Avoid rebranding costs" caption.

**Ad Set D — Remarketing (Hot)** · Budget: 10%
- Audience: Custom Audience: Website visitors (30/90 days), IG/FB engagers (365 days), Uploaded list of directors. Lookalike (1–2%) of "Messaging Conversations Started" past 180 days.
- Primary text: "You viewed Trademark Registration—need help with class & fees? Chat now. Filing can start today."
  - Headline: "Finish Your TM Filing" · CTA: Send WhatsApp Message
- Compliance: the "Uploaded list of directors" needs a lawful basis (DPDP ss. 4–6).

**WhatsApp setup for Trademark**
- Auto-reply: "Hi {{first_name}} ð You're chatting with Setindiabiz. / Reply YES to get TM class search, fee breakup & filing updates on WhatsApp. Reply STOP anytime."
- Quick replies: Free Class Search · Fees & Timeline · Talk to an Expert · Upload Logo
- Class finder prompt: "Tell us your brand name + what you sell (in 1–2 lines). We'll suggest likely classes and send a checklist."
- Docs checklist: "Typical docs: Applicant ID, logo (PNG/JPG), MSME certificate (if any), Use proof (optional), POA. We'll share the POA format here."
- Price/Timeline: "Professional fee ₹____ + Govt fee ₹____ per class (individual/MSME vs company differs). Filing in 24–48h after docs. TM application no. issued same day of filing."
- Templates (submit for approval):
  - (Marketing) `tm_followup_quote_v1`: "Hi {{1}}, your Trademark class suggestions are ready. Want us to file today? Quote: {{2}}. Reply PROCEED to start or HELP for questions."
  - (Marketing) `tm_checklist_reminder_v1`: "Hi {{1}}, still need your logo + ID to file your TM. Share them here and we'll file in 24–48h."
  - (Utility) `tm_filing_confirmation_v1`: "Hi {{1}}, your Trademark Application has been filed. App. No: {{2}} Class: {{3}}. We'll keep you posted on objections/hearings."
  - Buttons: Talk to Expert (Quick reply), Pay Securely (URL), Unsubscribe (Quick reply)
- Creative specs: "Single image 1080×1080 & 1080×1350; Reels/Stories 1080×1920 (safe zones!)"; "Keep text <20% area; bold "™" / "®" icon; high-contrast headline"; trust strip: "PAN-India • 15+ yrs • Not a law firm; techno-legal consultancy"
- 10–15s video script: "Is your brand protected?" (2s) / "Free class search on WhatsApp" (4s) / Steps: Search→File→Objection→Hearing (5s) / "Start now" + WA button cue (3s)
- Compliance:
  - "®" may only be used for registered marks (Trade Marks Act 1999 s. 107, falsely representing a mark as registered). Do not show "®" next to a client's unregistered brand. Verify current version.
  - "15+ yrs" is inconsistent with the site's "20+ years".
  - "Not a law firm; techno-legal consultancy" is a good disclaimer. Keep it.

---

## 3. DPIIT Startup Recognition CTWA, turns 7–9 (chat 24, 3 Oct 2025)

**Overlay copy (on-creative), turn 7**
- Version A — Benefits (recommended): Headline: DPIIT Startup Recognition · Bullets: Official Startup India recognition / Access tax & IPR benefits* / Tender & compliance relaxations* · CTA Button: WhatsApp Now · Footer microcopy: *Subject to eligibility
- Version B — Offer: Headline: Get DPIIT Recognition · Bullets: Free eligibility check on WhatsApp / Docs & filing support end-to-end / Faster IPR & govt. benefits* · CTA: WhatsApp Now · Footnote: *Subject to eligibility
- Version C — Problem → Outcome: Headline: Protect Your Startup Advantages · Bullets: Recognition under DPIIT / Save on fees & get relaxations* / Guidance till approval · CTA: WhatsApp Now · Footnote: *Subject to eligibility
- Trust strip (bottom): 15+ yrs • 1,00,000+ filings • PAN-India (optional) · Compliance line (tiny): Techno-legal consultancy. Not a law firm.
- Compliance:
  - Risk of **implied government affiliation.** "Official Startup India recognition" and "Get DPIIT Recognition" can read as if Setindiabiz grants recognition or is part of Startup India.
  - Prefer wording such as "Help applying for DPIIT recognition" plus "Recognition is granted by DPIIT; Setindiabiz is a private consultancy".
  - Do not use the Startup India logo, the Ashoka emblem or the tricolour styling. Relevant law: State Emblem of India (Prohibition of Improper Use) Act 2005; Emblems and Names (Prevention of Improper Use) Act 1950; CCPA Guidelines 2022 on endorsements and disclaimers. Verify current version.
  - Tax benefits (s. 80-IAC) need separate IMB approval, so "Access tax … benefits*" must keep the eligibility footnote.

**Ads Manager copy, turn 7**
- Primary Text (long): "Founder? Get DPIIT Startup Recognition with a free eligibility check on WhatsApp. We'll map benefits, documents, timelines & fees. Reply START to begin."
- Primary Text (short/Hinglish): "DPIIT Recognition chahiye? Free eligibility check WhatsApp par. Reply START."
- Headline: DPIIT Startup Registration – Start Now · Description: Free eligibility check on WhatsApp · CTA: Send WhatsApp Message

**Launch kit, turn 8 (Oct 3, 2025 3:48 PM)**
- Objective: Engagement → Messaging · Ad destination: WhatsApp · Optimization: "Messaging conversations started" · Budget: start ₹3k–₹10k/day across 2–3 ad sets (₹1k+ per ad set) · Placements: Advantage+ placements (FB/IG feeds, Stories/Reels; WA Status if available) · CTA: Send WhatsApp Message
- Ad Set 1 – Founders/Directors (metros): Locations: Delhi-NCR, Mumbai, Bengaluru, Hyderabad, Pune, Chennai, Ahmedabad, Kolkata · Age: 23–55 | Lang: English/Hindi · Detailed: Interests—Startup India, DPIIT, Entrepreneurship, Angel/VC, Incubators, IIM/Startup events · Job titles (narrow): Founder, Co-founder, Director, CEO, Proprietor, Partner · Exclude: existing customers list, 30-day engagers
- Ad Set 2 – Early-stage SaaS/D2C: Interests: SaaS, E-commerce, Shopify, D2C, Product Hunt, No-code, Growth marketing · Behaviors: FB page admins, IG business account users (optional)
- Ad Set 3 – Remarketing (hot): Website visitors (30/90d), IG/FB engagers (365d), your director list (if consented). Also test a 1–2% lookalike of "Messaging conversations started" (last 180d)
- Budget split idea: 45% / 35% / 20%.
- Primary text:
  - V1: "Get DPIIT Startup Recognition. Free eligibility check on WhatsApp + docs list + timeline. Reply START to begin."
  - V2 (Hinglish): "DPIIT Recognition chahiye? Eligibility check free—WhatsApp par. Class-A docs list & filing support. Reply START."
  - V3 (Benefit-led): "Unlock tax/IPR/tender relaxations* with DPIIT recognition. Chat with an expert on WhatsApp now." (*subject to eligibility)
- Headlines: "DPIIT Startup Registration – Start Now" · "Free Eligibility Check on WhatsApp" · "Get DPIIT Recognition Today"
- Description (optional): "Docs, fees & timeline in chat"
- On-creative CTA: "WhatsApp Now"; in Ads use Meta's official CTA "Send WhatsApp Message".
- Pre-filled message (turn 8; turn 9 wording "Prior Startup India recognition? (Y/N)"):
  ```
  DPIIT Eligibility:
  • Company name:
  • Sector/industry:
  • Incorporation date:
  • Revenues (approx.):
  • Any prior Startup India recognition? (Y/N)
  ```
- Auto-reply: "Hi {{first_name}} ð You're chatting with Setindiabiz. / Reply YES to receive the DPIIT eligibility checklist, documents list & fee breakup on WhatsApp. Reply STOP anytime."
- Quick replies: Check Eligibility · Docs List · Talk to Expert
- Chat snippets:
  - Docs list: "COI, PAN, founder ID, pitch/brief, website/Deck (if any). We'll share the exact list after eligibility check."
  - Timeline/fees: "Preparation 1–2 days; filing once docs are ready. Govt portal timelines vary. Professional fee ₹___ + taxes; we'll confirm after scope."
- UTM: `?utm_source=meta&utm_medium=c2w&utm_campaign=dpiit_eng_{adset_name}&utm_content={ad_name}`
- Creative QA:
  - Export 1080×1080, 1080×1350, 1080×1920.
  - For 9:16, keep ~250px top and 340px bottom free of text.
  - One core promise per frame; max 3 bullets; add "*Subject to eligibility".
  - File size under 30 MB (images) / 4 GB (video).
- Automated rule: "Pause ad if Spend > 3 × target CPL AND Conversations < 2 in last 3 days."
- Compliance:
  - "Get DPIIT Recognition Today" implies a same-day outcome that DPIIT controls. Do not use it.
  - V2 "Class-A docs list" is unclear wording. Fix it before use.
  - "your director list (if consented)" is the correct framing. Keep it.

**Setup choice, turn 9:** "Go with Tailored messages campaign to get live fast, then graduate to Manual once you see what works." Switch to Manual "after ~3 days or 50+ conversations: CPL > ₹120 in any segment → split to Manual with separate ad sets (Metros, SaaS/D2C, Remarketing)."

**Creative sizes, turn 6 (chat 24, 3 Oct 2025)**
- 1080 × 1080 (1:1) · 1080 × 1350 (4:5) · 1080 × 1920 (9:16)
  - 9:16 safe zone: "leave ~14% top (~250 px) and 20–35% bottom (~340 px) clear of text/logos; also leave ~6% on each side for Reels UI"
- Optional landscape 1200 × 628 (1.91:1)
- Images: JPG/PNG, up to 30 MB · Video: MP4/MOV, up to 4 GB
- Status: CURRENT per chat; verify against Meta's current ad specs.
