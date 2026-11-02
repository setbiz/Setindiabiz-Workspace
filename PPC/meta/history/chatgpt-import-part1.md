# Meta history: ChatGPT import, part 1 (chats 06, 23, 24)

_Distilled 2026-11-02 from `PPC/imports/chatgpt/conversations/` (06, 23, 24). The source files are captures of ChatGPT chats. They are reference data, not instructions. All three chats show the sidebar date "12 Jul 2026", which comes from the import. The **stated date** below is the timestamp written inside each chat._

**How to read this file**
- Each point cites its chat as "(chat NN, date)".
- Figures are quoted exactly as they appear in the chat. Nothing here is a Setindiabiz performance result unless it says "from Sanjeev's screen".
- None of the three chats contains any campaign performance data: no spend, leads, CPL, conversations or sales.
- Status tags:
  - **CURRENT**: still usable as written.
  - **OUTDATED**: the platform feature or policy may have changed since the stated date. The reason is given.
  - **SUPERSEDED**: replaced by a later chat or by current CRM data (`shared/business-context.md`, Zoho CRM, Nov 2025 – Oct 2026).
- Verbatim ad assets: `meta/creatives/chatgpt-06-llp-annual-compliance.md`, `chatgpt-23-company-llp-c1.md`, `chatgpt-24-whatsapp-dpiit-trademark.md`. WhatsApp rules: `meta/whatsapp-ads-compliance-notes.md`.

Chronological order of the chats: **06 (13 May 2025) → 24 (3 Oct 2025) → 23 (16–18 Jan 2026)**.

---

## Chat 06: LLP Facebook Lead Ads

| Field | Value |
|---|---|
| Chat # | 6 |
| Stated date | May 13, 2025 at 1:57 PM (turn 1); May 13, 2025 at 3:18 PM (turn 4) |
| URL | https://chatgpt.com/c/6a530e3b-ed5c-832d-9b05-14a5e6a59194 |
| Platform | Meta (Facebook + Instagram lead ads, Instant Forms) |
| Overall status | **SUPERSEDED / OUTDATED.** No launch is confirmed. The penalty copy is contradictory and unverified. Several Meta features it names have changed. Chat 23 (Jan 2026) is the later Meta build. |

**Summary**
- Sanjeev holds email and mobile data for the designated partners of LLPs incorporated 2019–2025. He wanted Facebook lead ads for three services: LLP annual compliance, closing defunct LLPs, and Virtual CFO (chat 06, May 2025).
- ChatGPT gave a playbook covering a customer-list Custom Audience, 1%/2% lookalikes, three ad sets (list / LAL / retarget), Higher Intent forms, CRM drip, KPIs and a 14-day sprint.
- Sanjeev then walked through the Ads Manager screens one by one: budget, ad set, form greeting, privacy text, then annual-compliance ad copy.
- In the final turn, ChatGPT withdrew its own "₹100/day late fee" copy and replaced it with "slab-based" penalty copy.

**Decisions and reasons** (chat 06, May 2025)
- Use the designated-partner list for Facebook lead ads. Reason: to reach those LLPs with the three services.
- Conversion location: Instant Form (turn 3). No reason given.
- Performance goal: Maximise number of leads (turn 3). No reason given.
- Lead quality: "I do not want accidental submissions, i want only those leads which are submitted by the leads willing to explore our services" (turn 3).
- Annual compliance ad first (turn 6). No reason given.
- Not decided in the chat: budget strategy, daily budget, cost-per-result goal, location, placements, which form, and which copy.

**Account changes (dated)**
- None confirmed as published.
- Turn 2 (May 13, 2025): Sanjeev's draft screen showed "Advantage+ on", daily budget ₹345.30 and "Highest volume". He was asking what to select, so these were not final settings.
- The chat does not say that a customer list was uploaded or that anything went live.

**Metrics (verbatim, dated)**. These are not results.
- From Sanjeev's screen (turn 2, May 13, 2025), a Meta projection: "You'll spend an average of ₹345.30 per day. Your maximum daily spend is ₹604.27 and your maximum weekly spend is ₹2,417.07."
- ChatGPT targets (turn 1, May 2025): "Cost per Lead (CPL): ≤ ₹ 250 (Annual Compliance) ≤ ₹ 350 (Strike‑off / CFO)"; "Qualified Lead Rate: ≥ 40 % of leads answer sales call"; "Conversion to Sale: ≥ 5 % (cold list) / ≥ 10 % (retarget)".
- ChatGPT budget advice (turn 2): "If your acceptable CPL is ₹ 250–350, set ₹ 1,250–1,750 per ad set per day."
- ChatGPT citing Meta (turn 2): "daily budget should be at least 5 times the result you're optimising for"; "Meta can legally overspend up to 75 % above your stated daily budget … but it will never exceed 7 × your daily budget within a calendar week."
- ChatGPT's own estimates, not evidence: "Native‑camera look + captions ≈ 20 % lift in lead quality vs polished ads." (turn 6); "Expect 5‑10 % more completions but looser intent." (turn 4, if the greeting is skipped).

**What worked / didn't**
- No outcome data exists.
- Process issue: ChatGPT wrote copy around "₹100/day late fee" in turns 1 and 6–9, then in turn 10 called that wrong. Its replacement says late filing "now attracts slab‑based penalties that grow from 1 × to 30 × the normal filing fee, plus ₹10–₹20 per day after one year". The two versions contradict each other, and neither cites a rule.
- **Verify against the current LLP Rules, 2009 fee schedule (Rule 24 / Annexure A as amended) on mca.gov.in before using any penalty figure.** My understanding is that the LLP (Amendment) Rules, 2022 moved LLP forms to a ₹100/day additional fee from 1 Apr 2022, which would make turn 10's "correction" itself wrong. Verify current version.

**Open items** (chat 06)
- Unknown: launch status and which copy or form was used.
- Lead magnets ("2025 LLP Compliance Calendar (PDF)", "Strike‑off cost calculator", Calendly) are not confirmed to exist.
- No ad kit exists for the strike-off or Virtual CFO services.
- Legal basis for the partner list is not established (see compliance flags).
- Overlap check: chat 19 (`19-llp-form-11-ads.md`) may cover the same topic. Not read in this pass.

**Status by item**
- Three-ad-set structure (list / 1% LAL / retarget) and ABO-then-CBO rollout: **OUTDATED**. In Jan 2026, chat 23 followed Meta's broad / Advantage+ approach and was told "Do NOT duplicate ad sets". Meta also now pushes Advantage+ audience over manual lookalikes (verify current).
- "pause any asset with CPL > 1.5 × ad‑set average or Relevance Score < 7" (turn 6): **OUTDATED**. Meta retired Relevance Score in 2019 and replaced it with quality, engagement and conversion rankings.
- "Keep text < 20 % of image" (turns 1, 6): **OUTDATED as a rule**. Meta dropped the 20% text rule in 2020. It is still a reasonable design guideline.
- "enable Dynamic creative" (turns 6, 10): **OUTDATED / verify**. Meta has been folding Dynamic Creative into Advantage+ creative / flexible formats.
- Higher Intent form type and manual placements excluding Audience Network: **CURRENT** (verify option names).
- CPL targets ≤ ₹250 / ≤ ₹350: **SUPERSEDED** by CRM unit economics. Revenue per Facebook lead is ₹271. The example break-even CPL is ≈₹135 at 50% margin, and margin % is still TODO.
- Copy with ₹100/day, "Starts at ₹3,999/yr", "Plans from ₹ 7,500/mo", "72 hrs", "ex‑Big 4 CAs", "Strike‑off in 90 days": **SUPERSEDED / do not use**. ChatGPT invented these figures. The site publishes no package prices (business-context.md).

**Compliance flags (chat 06)**
- **DPDP Act 2023, ss. 4–6 (lawful basis, notice, consent):**
  - Turn 1 suggests storing proof of collection from "MCA filings, public register scrape, etc." and ticking "This data was collected directly from its owners".
  - If the list came from MCA or third parties, that tick would be a false declaration under Meta's Custom Audience Terms.
  - Publicly available data may fall under s. 3(c)(ii), but only if it was made public by the person or under a legal obligation. That needs a legal view. Verify current DPDP Rules 2025 phasing.
- **TRAI TCCCPR 2018:** the form consent "I agree to be contacted by Setindiabiz via phone/WhatsApp" is used to support promotional calls. Recorded consent is needed for calls or SMS to numbers on the DND registry. Verify the current amendment (2025).
- **CPA 2019 s. 2(28) / CCPA Misleading Ads Guidelines 2022 / ASCI:**
  - The penalty claims ("Avoid ₹1 L+ in ROC penalties", "Last year thousands paid heavy ROC fines", "ROC fines can jump to 30× the fee") are unsubstantiated and possibly wrong in law.
  - Absolute claims ("Zero penalties", "Penalty‑proof your LLP") need evidence.
  - "No hidden fees" needs evidence.
  - Prices not on the landing page.
  - "ex‑Big 4 CAs".

---

## Chat 23: Facebook Ads Campaign Setup

| Field | Value |
|---|---|
| Chat # | 23 |
| Stated date | Fri, Jan 16 1:22 PM (turn 1) → Sun, Jan 18 10:27 AM (turn 24). The year 2026 comes from the pasted audit dated January 16, 2026 and from file names dated 2026-01-16 / 2026-01-18. |
| URL | https://chatgpt.com/c/51e64239-3af4-8333-9b24-c02335df21aa |
| Platform | Meta (FB, IG, Messenger, WhatsApp). Also Zoho CRM, Zoho LeadChain and Zoho SalesIQ. |
| Ad account | SETINDIABIZ (152154124583473); dataset "Setindiabiz JS" |
| Overall status | **CURRENT as the latest Meta build in the imports.** Whether it is still live 10 months later must be checked with the Meta Ads connector. |

**Summary**
- Sanjeev pasted a 16 Jan 2026 development audit stating that Meta CAPI and Zoho env vars were deployed via PR #2542.
- He also pasted an earlier assistant's ₹160,000/month four-campaign plan. That assistant was blocked from Ads Manager.
- ChatGPT reduced the plan to 4 Advantage+ Leads campaigns: C1 Company+LLP India, C2 Subsidiary/India Entry Global, C3 Trademark Global, C4 GST India.
- **Only C1 was built** (chat 23, Jan 2026).
- C1 has two ad sets: Forms (3 ads) and Website-First (2 ads), with value rules +20% website / −30% forms, and form leads go to Zoho via LeadChain.
- He also built a separate WhatsApp Messages campaign (WA1) with a Chat Builder template routed to Zoho SalesIQ. Two Automated Rules switch #IND campaigns on and off for business hours.
- It ends with a status report and a read-only Comet browser audit prompt.

**Decisions and reasons** (chat 23, 16–18 Jan 2026)
- Work step by step, with Sanjeev implementing (turn 2). ChatGPT cannot operate Ads Manager (turn 3).
- Skip tracking verification "because he had verified tracking earlier" (turn 4).
- Conversion location: "Website and instant forms". Meta did not offer all three surfaces in one option. He connected the existing "Setindiabiz JS" dataset rather than creating a new pixel, which would fragment tracking (turns 5–8).
- C1 budget: ₹2,500/day instead of ₹1,300 (turn 10). Reason given at turn 33: "keep approx 20 sales staff busy".
- Minimum age 24, no upper cap. The flow allowed only a minimum (turn 11).
- Ads kept in Draft until all were built, then published (turns 18, 21).
- Lower-competition geo ad set (J&K, North East, Tier-2) deferred until all ads exist (turns 22–23).
- "Website and calls" rejected (calls dilute signal and muddy attribution). Value rules +20% website / −30% forms replaced the −90% then on screen, to prefer website leads without stopping forms (turns 26–29).
- WhatsApp as a separate Messages campaign, to avoid mixing objectives (turn 32).
- WhatsApp budget: ₹2,500/day preferred, with ₹1,500–₹2,000 acceptable because other campaigns will follow (turn 33).
- Business hours 9:30 am – 7:30 pm on all campaigns, because "most leads come during the day and that is when the team works" (turn 34).
- Automated Rules with daily budgets (Method B), not lifetime budget + ad scheduling (turn 35).
- Naming tag went IN → IND → #IND because rules only offer "contains", and the tag must not catch future USA campaigns (turns 38, 40, 55–56).
- WhatsApp Status excluded until 9:16 creatives exist (turn 45).
- Zoho SalesIQ / Zobot to handle WhatsApp (turns 48–50).
- All three WhatsApp angles approved: pricing, register today, trust/online (turn 53).
- "should not spend more than 10K for IND Campaigns in a aday" (turn 64), then "skip budget optimisation for now" (turn 65). No spend cap rule was created.

**Account changes (dated)**
- **Fri 16 Jan 2026 (turns 5–11):**
  - Leads campaign and ad set created in SETINDIABIZ (152154124583473).
  - Conversion location Website and instant forms; dataset Setindiabiz JS; event Lead.
  - Campaign daily budget ₹2,500; minimum age 24.
  - Location: told to replace India with the metro list, but this is not confirmed.
- **16–17 Jan 2026 (turns 12–21):**
  - Form "C1 | Company+LLP | Higher Intent | v1" built.
  - Three form ads built: Pricing, Register Today, 100% Online.
  - First publish failed: "Required field is missing: The link field is required" and "Creative missing link URL: Asset customisation ads require a link".
  - UTM'd URLs added, then "Ads Published" (turn 21).
- **By Sat 17 Jan 2026 (turn 23):** Zoho LeadChain configured for the first ad, per Sanjeev.
- **Sun 18 Jan 2026 (turns 24–31):**
  - Website-First ad set duplicated.
  - Value rules +20% website / −30% form created (turn 29).
  - Website ads W1/W2 published (turn 31).
  - Screen showed "Daily budget ₹3,500" (turn 24). Whether it changed is unresolved.
- **Sun 18 Jan 2026 (turn 41):** renamed to `IN | C1 | Company+LLP | Leads | …`; ad sets `IN | C1 | Web | Metros | Website-First`, `IN | C1 | Forms | Metros | Broad`; ads W1/W2, F1/F2/F3.
- **Sun 18 Jan 2026 (turns 42–47):**
  - WhatsApp campaign created (Engagement objective, Ad set budget).
  - Ad set changed from Website at ₹800/day to Message destinations → WhatsApp at ₹2,000/day.
  - WhatsApp Status unticked.
- **Sun 18 Jan 2026 (turns 48–54):**
  - WhatsApp number integrated with Zoho SalesIQ.
  - Chat Builder template created with welcome message, business hours and FAQ buttons.
  - "Create all the three ads". Publication not separately confirmed.
- **18 Jan 2026 or later (turns 55–62):** two Automated Rules read from his screen:
  - ON: "All paused campaigns", Turn on campaigns, name contains #IND.
  - OFF: "All active campaigns", Turn off campaigns, name contains #IND.
  - The ON rule name still said "19:29".
- **Not done:** Tier-2/J&K/NE ad set; C2, C3 and C4; spend cap rules; #HOLD exclusion.

**Metrics (verbatim, dated)**. There are no performance results.
- From Sanjeev's screens (16–18 Jan 2026):
  - "Budget remaining: ₹1,431,574.38" (turn 1, via earlier assistant).
  - C1 daily budget "₹2,500" (turns 6–10) and "₹3,500" (turn 24).
  - WhatsApp ad set "₹800/day" (turn 43), then "₹2,000/day" (turn 44).
  - "approx 20 sales staff" (turn 33).
  - "not more than 10K for IND Campaigns in a aday" (turn 64).
- Earlier assistant's benchmarks (pasted turn 1, Jan 2026). These are not data:
  - Lead Form "2-4%" / "₹800-2000".
  - Landing Page Visits "3-5%" / "₹600-1500".
  - WhatsApp Chat "1-3%" / "₹1500-4000".
  - "Cost per Lead Target: ₹1200".
- ChatGPT estimates (Jan 2026). These are not data:
  - "Conversion volume per campaign is ≥50/week" (turn 1).
  - "This single question increases lead quality by ~30%." (turn 1).
  - "Good start: ₹40–₹120 per conversation" (turn 32).
  - "₹2,000/day → ~13 to 33 conversations/day" (turn 33).
  - Pause rule "Cost per result (Lead) > ₹1,800 AND Results ≥ 3" (turn 31).

**What worked / didn't**
- Worked:
  - Publishing errors on Instant Form ads were cleared by adding a website URL. Meta required a link even on form ads that use asset customisation (turns 20–21, Jan 2026).
  - Square-only creatives triggered a WhatsApp Status warning, which was cleared by unticking the placement (turn 47).
- Didn't: the time picker would not accept 19:29. The ON window was set to 09:30 → 19:00 (turn 60).
- Unknown: every performance outcome. No test lead result is confirmed (asked at turns 23, 29, 31).

**Open items** (chat 23, Jan 2026). See the "Still actionable" list at the end.

**Status by item**
- C1 structure, value rules, LeadChain, WA1, business-hour rules: **CURRENT**, but confirm they are still live with the Meta Ads connector.
- Earlier assistant's 4 × 3 ad-set plan (₹160,000/month, 50/35/15 split): **SUPERSEDED** within the chat by ChatGPT's 4-campaign Advantage+ plan.
- Earlier-assistant / ChatGPT CPL benchmarks (₹800–2,000, ₹1,200, pause at ₹1,800): **SUPERSEDED** by CRM. Facebook revenue per lead is ₹271 (business-context.md, CRM Nov 2025–Oct 2026, directional).
- CRM lead-source labels in the chat ("Set Lead Source = Facebook Lead Ads", turn 21; "Lead Source = Meta - WhatsApp", turns 50–51): **SUPERSEDED**. The CRM's canonical values are `Advt - Facebook`, `Advt - Instagram` and `Advt - WhatsApp`. Check which labels LeadChain and SalesIQ actually write.
- "Special Ad Category ❌ OFF (legal services are allowed)" (turn 1): **OUTDATED / verify**. Meta has broadened special categories, e.g. "Financial products and services". The WhatsApp ad hit a "securities and investments" declaration (turns 43–47), with outcome not confirmed.
- "Andromeda" framing: Andromeda is Meta's ad-retrieval system, not a setting you switch on. The usable advice ("broad targeting, fewer ad sets, more creatives") is still **CURRENT** (verify).

**Compliance flags (chat 23)**
- **Price claim "Professional fee from ₹3,499 (Govt fees extra)" / creative "₹3499/-":**
  - business-context.md says no package prices are published and ads must not quote a fixed price unless it is on the landing page.
  - Confirm `/lp/company-registration` shows ₹3,499 before running (CPA 2019 s. 2(28); CCPA Guidelines 2022 on bait advertising and price claims; ASCI Ch. I).
  - "Company Registration – Low Fee*" is a comparative claim that needs substantiation.
- **"4.8/5 Rated by 10,000+ Businesses" creative (company-registration-4.jpg):**
  - The site claims "4.8 Google rating" and "18K+ clients", and evidence for both is TODO.
  - The creative's "10,000+ businesses" differs from the site.
  - Substantiate with a dated screenshot or remove it (ASCI Ch. I.1; CCPA Guidelines 2022).
- **"Our incorporation expert will call you within 1 business hour"** (thank-you page, turn 14) is a service promise that must be met or softened.
- **WhatsApp greeting / Chat Builder (turns 32–51)** has no explicit opt-in capture (YES/STOP), unlike chat 24's recommended greeting. Marketing templates outside the 24h window need opt-in under WhatsApp Business Messaging Policy (see whatsapp-ads-compliance-notes.md).
- **Form consent** "you consent to be contacted … via phone, WhatsApp, SMS or email" (turn 13): this supports DPDP s. 6 consent and TCCCPR 2018 for promotional calls/SMS. Verify the wording matches the privacy policy, and verify current DPDP Rules / TCCCPR amendments.
- Turn-1 paste contains environment-variable **names** for Meta/Zoho tokens (no values). Do not paste token values into this repo.

---

## Chat 24: WhatsApp ads compliance guide

| Field | Value |
|---|---|
| Chat # | 24 |
| Stated date | Oct 3, 2025 at 12:00 PM (turn 1), 1:00 PM (turn 2), 3:48 PM (turn 8) |
| URL | https://chatgpt.com/c/6f422795-2d1c-832c-ac76-7ba67e9f11ff |
| Platform | Meta (FB, IG, WhatsApp Status placements), WhatsApp Business (WABA, Click-to-WhatsApp) |
| Overall status | **Partly SUPERSEDED.** The WhatsApp build moved to Company+LLP in chat 23 (Jan 2026). The DPIIT and Trademark kits are unbuilt but reusable. The compliance rules are **CURRENT, verify current version**. |

**Summary**
- Sanjeev wanted to target directors of Indian companies on WhatsApp using mobile numbers and emails he holds (chat 24, Oct 2025).
- ChatGPT's answer: Click-to-WhatsApp (CTWA) ads to a Customer List Custom Audience are possible, but unsolicited WhatsApp messages are not. It set out the DPDP consent and WhatsApp opt-in rules.
- It explained that engagement ads are Meta placements that open a 1:1 chat, not a broadcast.
- It supplied director ad variants, auto-replies, templates, a Trademark CTWA kit (ad sets A–D) and a DPIIT Startup Recognition kit, after Sanjeev moved DPIIT ahead of trademark.
- It ends at Meta's "Choose a campaign setup" screen. ChatGPT recommended "Tailored messages campaign", and there was no reply.

**Decisions and reasons** (chat 24, 3 Oct 2025)
- Target directors via Meta ads and WhatsApp (turn 1). No reason given.
- Trademark Registration ad sets (turn 5). No reason given.
- "before trademark - help me with DPIIT Startup Registration Creative" (turn 7). No reason given.
- "I have made the creatives for DPIIT Recognition - Now i will styart working on creation of engagement ads" (turn 8, Oct 3, 2025 3:48 PM).
- Not decided: Tailored vs Manual setup; the lawful basis for the director list.

**Account changes (dated)**
- None confirmed.
- DPIIT creatives were made outside the account (turn 8, 3 Oct 2025).
- Sanjeev reached the campaign-setup screen (turn 9). His choice is unknown.

**Metrics (verbatim, dated)**
- From Sanjeev: none.
- ChatGPT benchmarks/estimates (Oct 2025). These are not data:
  - "Cost per conversation (CPCv) — target: ₹20–₹120 depending on city/segment" (turn 5).
  - "Baseline India ranges: ₹20–₹120 per conversation" (turn 8).
  - "start ₹3k–₹10k/day across 2–3 ad sets (₹1k+ per ad set)" (turn 8).
  - Trademark split "A 40%, B 25%, C 25%, D 10%" (turn 5); DPIIT split "45% / 35% / 20%" (turn 8).
  - "If Cost/Conversation > ₹120 for 2k impressions" (turn 8).
  - "Create a Lookalike 1–2% from that event once you have ~200–300 conversations" (turn 8).
  - "Pause ad if Spend > 3 × target CPL AND Conversations < 2 in last 3 days" (turn 8).
  - "Reply < 2 min" (turns 5, 9).
- ChatGPT citing sources (Oct 2025):
  - DPDP penalties "up to ₹250 crore depending on the breach" (turn 1, MeitY).
  - Customer list "Minimum ~100 records recommended" (turn 1).
  - Broadcast lists "max 256 per list" (turn 2, WhatsApp Help Center).

**What worked / didn't**
- No outcome data.
- Useful clarification: CTWA is a paid placement that the user taps. It is not outbound messaging (turns 2–3, Oct 2025).
- The trust figures in the drafts are inconsistent: "50k+ filings" (turn 4) vs "1,00,000+ filings" (turns 5, 7). "15+ yrs" (turns 5, 7) vs the site's "20+ years".

**Open items** (chat 24, Oct 2025)
- DPIIT launch status unknown.
- Trademark kit pending.
- Fee placeholders unfilled ("Professional fee ₹____ + Govt fee ₹____").
- Lawful basis for the director list not confirmed.
- Not shown as done: privacy notice update, consent log, WABA link, template approval, agent training on STOP/HELP.

**Status by item**
- CTWA vs broadcast explanation, 24-hour window, template categories: **CURRENT** (verify current WhatsApp Business Policy).
- "WhatsApp moved to per-message pricing (country + category)" (turn 1): **CURRENT**. Effective 1 Jul 2025; check current India rates.
- "TRAI/DND: the new spam rules mainly cover calls/SMS. WhatsApp (OTT) isn't in that regime" (turn 1): **verify current version**. TCCCPR 2018 was amended in 2025, and OTT coverage is under discussion. The calls Setindiabiz makes after a WhatsApp lead are covered.
- Detailed targeting (job titles, interests, exclusions) in Ad Sets A–D and Ad Set 1: **OUTDATED / verify**. Meta has removed or merged many detailed-targeting options and exclusions since 2024–25. Chat 23 (Jan 2026) went broad with no detailed targeting.
- Director-list targeting: **SUPERSEDED** by the CLAUDE.md DPDP guardrail. Do not upload without a documented lawful basis.
- DPIIT and Trademark CTWA kits: unbuilt, **CURRENT as drafts**, subject to the claim fixes below.
- CPCv target ₹20–₹120: see CRM contradiction. WhatsApp leads convert at 0.9% lead→won and revenue per lead is ₹157 (business-context.md, Nov 2025–Oct 2026, directional).

**Compliance flags (chat 24)**: details are in `whatsapp-ads-compliance-notes.md`.
- **Implied government affiliation:** "Official Startup India recognition", "Get DPIIT Recognition", "DPIIT Startup Registration – Start Now", "Recognition under DPIIT". The ad must not suggest Setindiabiz is DPIIT/Startup India or can grant recognition.
  - Add "Setindiabiz is a private consultancy; recognition is granted by DPIIT".
  - Do not use the Startup India logo or the State Emblem (State Emblem of India (Prohibition of Improper Use) Act 2005; Emblems and Names (Prevention of Improper Use) Act 1950; CCPA Guidelines 2022). Verify current version.
- **Outcome promises:** "Faster IPR & govt. benefits*", "Save on fees & get relaxations*", "Guidance till approval". Keep "*Subject to eligibility" (CCPA Guidelines 2022, disclaimers must not contradict the main claim).
- **"Talk to a CA now"** (turn 4): only use this if a Chartered Accountant actually answers. Professional-advertising limits may also apply under the ICAI Code of Ethics. Verify current version.
- **Trust figures** "50k+ filings", "1,00,000+ filings", "15+ yrs": these are unsubstantiated and inconsistent with each other and with the site (ASCI Ch. I.1).
- **"Avoid ₹100/day late fees"** (Variant C, director ads): verify this against the current Companies (Registration Offices and Fees) Rules, 2014.
- **Customer list of directors:** DPDP Act 2023 ss. 4–6 require a lawful basis and notice, and Meta's Custom Audience Terms require the right to use the data. Turn 1 itself says "Don't upload scraped or purchased lists".

---

## Contradictions with current CRM data (business-context.md, Zoho CRM, Nov 2025–Oct 2026, directional)
1. **CPL targets vs unit economics:**
   - CRM: revenue per Facebook lead ₹271, Instagram ₹262, WhatsApp ₹157. The break-even example is ≈₹135 at 50% margin, and margin is still TODO.
   - Chat targets: chat 06 (May 2025) CPL ≤ ₹250/₹350; chat 23's pasted benchmarks (Jan 2026) "₹800-2000" and "Cost per Lead Target: ₹1200"; pause at "> ₹1,800".
   - Any of those levels would lose money on current CRM numbers.
2. **Lead→won:**
   - Chat 06 targets "≥ 5 % (cold list)". The CRM shows Facebook at 3.7% and Instagram at 2.8%.
   - Chat 23's pasted plan claims WhatsApp "1-3%" conversion. The CRM shows WhatsApp at 0.9% (3 won of 336 leads).
3. **WhatsApp volume vs value:** chat 23 (Jan 2026) sized WA1 at ₹2,000/day to keep "approx 20 sales staff busy". The CRM shows WhatsApp is the weakest Meta channel by conversion, although its AOV is ₹17,542 on only 3 deals.
4. **Price anchor:**
   - Chat 23 ads lead with "₹3,499". business-context.md says no package prices are published.
   - Facebook AOV is ₹7,284 and all-sources AOV is ₹8,750. The anchor is well below what deals actually close at. This is an observation, not a conclusion.
5. **Lead_Source labels:** chat 23 sets "Facebook Lead Ads" and "Meta - WhatsApp". The CRM uses `Advt - Facebook` / `Advt - WhatsApp`. If LeadChain or SalesIQ write different labels, Meta leads could be under-counted.
6. **Trust claims:** chat 24 "15+ yrs", "1,00,000+ filings"; chat 23 creative "10,000+ businesses". The site says "20+ years", "18K+ clients", "4.8 Google rating", and evidence for all of them is TODO.

## Still actionable
1. **Verify live state** with the Meta Ads connector, in read-only mode:
   - Are `#IND` C1 and WA1 still running?
   - Actual daily budgets: is C1 ₹2,500 or ₹3,500?
   - Locations: 7 metros, or 8 including Kolkata?
   - Value rules (+20/−30).
   - Whether the ON rule (applies to "All paused campaigns", no #HOLD exclusion) is reviving campaigns that were paused on purpose (chat 23, Jan 2026).
2. **Add a `#HOLD` exclusion to the ON rule**, or scope it to specific campaigns. Also confirm the rule time zone is IST (chat 23, turns 35/40/64, Jan 2026).
3. **End-to-end test lead** from Form, Website and WhatsApp into Zoho. **Confirm the Lead_Source labels match the CRM values** `Advt - Facebook` / `Advt - Instagram` / `Advt - WhatsApp` (chat 23, turns 23, 29, 31, 65).
4. **Substantiate or remove** "₹3,499" (unless it is on the LP), "4.8/5 Rated by 10,000+ Businesses", "within 1 business hour" (chat 23), and the chat 24 trust figures.
5. **Add YES/STOP opt-in capture** to the WA1 Chat Builder / Zobot greeting, before sending any marketing template (chat 24 turn 4 pattern; chat 23 greeting lacks it).
6. **Re-set CPL / cost-per-conversation guardrails** from CRM revenue per lead and real gross margin, instead of the chat benchmarks (business-context.md TODO: margin %).
7. **Daily spend cap:** "not more than 10K for IND Campaigns in a aday" (chat 23, turn 64) was never implemented. Decide on an account spending limit or a rule.
8. **DPIIT CTWA kit** (chat 24, Oct 2025): fix the govt-affiliation wording and fill the fee placeholders before any build. Build it PAUSED, per CLAUDE.md.
9. **Director / LLP-partner lists** (chats 06, 24): get a legal view on lawful basis (DPDP ss. 4–6, s. 3(c)(ii)) before any Custom Audience upload. Never commit the list to the repo.
10. **LLP penalty facts** (chat 06): verify the current LLP Rules fee schedule on mca.gov.in before any "late fee" copy.
11. **Deferred builds** (chat 23): Tier-2 / J&K / NE ad set; C2 Subsidiary/India Entry (#USA rules); C3 Trademark; C4 GST; 9:16 creatives so WhatsApp Status can be re-enabled.
12. **Run the Comet read-only audit prompt** (chat 23, turn 66), or do the same audit via the Meta Ads connector, and file it under `meta/reports/`.
