# WhatsApp ads: compliance notes (from ChatGPT chat 24, 3 Oct 2025)

_Source: `PPC/imports/chatgpt/conversations/24-whatsapp-ads-compliance-guide.md` (chat 24, stated date Oct 3, 2025) · https://chatgpt.com/c/6f422795-2d1c-832c-ac76-7ba67e9f11ff_

**About this file**
- These are the rules as ChatGPT stated them, with the source ChatGPT named. It is not legal advice.
- ChatGPT named its sources only as labels: "WhatsApp Business", "Facebook", "Facebook Developers", "MeitY", "WhatsApp Help Center", "India TV News", "CookieYes". The chat contains no URLs or section numbers.
- The "Statutory anchor" column adds the provision Setindiabiz's workspace rules require. Each row is marked **⚠ verify current version** because these rules change.
- Distilled 2026-11-02.

## A. Core rule

| # | Rule (as stated in chat 24, quoted where verbatim) | Source named in chat | Statutory / policy anchor | Status |
|---|---|---|---|---|
| A1 | "you can run Click-to-WhatsApp ads on Facebook/Instagram and target your list via a Customer List Custom Audience—but you can't blast unsolicited WhatsApp messages to those numbers." (turn 1) | WhatsApp Business | WhatsApp Business Messaging Policy; Meta Custom Audience Terms | ⚠ verify current version |
| A2 | "WhatsApp requires opt-in before you send any proactive marketing messages, and Meta requires you to have the legal right/consent to use that data for ad targeting." (turn 1) | WhatsApp Business | WhatsApp Business Messaging Policy (opt-in); Meta Custom Audience Terms (rights certification) | ⚠ verify current version |

## B. India law

| # | Rule | Source named in chat | Statutory anchor | Status |
|---|---|---|---|---|
| B1 | "DPDP Act (India): have clear, specific consent (or another lawful basis) to use personal data (emails/phone numbers) for ads and for WhatsApp messages; be ready to prove consent and honor withdraw/erasure requests." (turn 1) | MeitY | Digital Personal Data Protection Act 2023: s. 4 (lawful grounds), s. 5 (notice), s. 6 (consent, withdrawal), s. 7 (legitimate uses), s. 8 (Data Fiduciary duties incl. erasure), s. 12 (erasure right). DPDP Rules 2025 (notified Nov 2025) phase in through May 2027 | ⚠ verify current version on meity.gov.in |
| B2 | "Penalties for violations can be very high (up to ₹250 crore depending on the breach)." (turn 1) | MeitY | DPDP Act 2023 s. 33 and Schedule | ⚠ verify current version |
| B3 | "Log consent for each contact (source, timestamp, purpose)." (turn 1) | MeitY | DPDP Act 2023 s. 6(10) (burden of proving notice and consent on the Data Fiduciary) | ⚠ verify current version |
| B4 | "TRAI/DND: the new spam rules mainly cover calls/SMS. WhatsApp (OTT) isn't in that regime, but your use is still governed by DPDP + WhatsApp/Meta policies." (turn 1) | India TV News (a news report, not a primary source) | TRAI Telecom Commercial Communications Customer Preference Regulations 2018 (TCCCPR), as amended in 2025. Covers commercial voice calls and SMS via telecom access providers; OTT coverage under discussion. **Follow-up sales calls to WhatsApp or form leads are in scope** | ⚠ verify current version on trai.gov.in. Do not rely on a news source |
| B5 | Use uploaded lists "only if you have a lawful basis (consent/legit interest) and show opt-out in your privacy notice." (turn 5) | none named | DPDP Act 2023 ss. 4, 5, 7. Note: the DPDP Act has **no general "legitimate interest" ground**; s. 7 lists specific "certain legitimate uses". ChatGPT's "legit interest" wording is a GDPR concept | ⚠ verify current version. Treat "legit interest" as not available |

## C. WhatsApp platform rules

| # | Rule | Source named in chat | Anchor | Status |
|---|---|---|---|---|
| C1 | "you may contact people on WhatsApp only if (a) they gave you their number and (b) they've opted-in to receive messages. You can collect opt-in on your site, forms, ads, or in-thread—just make it explicit." (turn 1) | WhatsApp Business | WhatsApp Business Messaging Policy (opt-in) | ⚠ verify current version |
| C2 | "During the 24-hour session that starts when they message you, answer live FAQs with quick replies. If you want to message later (outside 24h) about marketing, send a pre-approved "Marketing" template—only if you have opt-in." (turn 1) | Facebook Developers | WhatsApp Cloud API: customer service window and message templates | ⚠ verify current version |
| C3 | "WhatsApp categorizes templates as marketing/utility/authentication/service and charges per message." (turn 1) | Facebook Developers | WhatsApp Business Platform pricing | ⚠ verify current version |
| C4 | "WhatsApp moved to per-message pricing (country + category). Check India rates in your WABA timezone and pick the right category (marketing vs utility)." (turn 1) | Facebook Developers | WhatsApp Business Platform pricing (per-message from 1 Jul 2025) | ⚠ verify current India rates |
| C5 | Broadcast lists: contacts "must have your number saved; max 256 per list" (WhatsApp Business app). For the API: "you send pre-approved message templates (marketing/utility) to opted-in users, including outside the 24-hour window." (turn 2) | WhatsApp Help Center | WhatsApp Business app help; WhatsApp Business Messaging Policy | ⚠ verify current version |
| C6 | "Always honor STOP and delete on request." (turn 4); "Honor STOP immediately." (turn 8); "define STOP/HELP handling" (turn 1) | none named | WhatsApp Business Messaging Policy (opt-out); DPDP Act 2023 s. 6(4) (withdrawal), s. 12 (erasure) | ⚠ verify current version |

## D. Click-to-WhatsApp ads (CTWA)

| # | Rule | Source named in chat | Anchor | Status |
|---|---|---|---|---|
| D1 | "No—Engagement ads aren't a broadcast." When someone taps the ad, "it opens a 1:1 chat with your business; you are not pushing a message to everyone on a list." (turn 2) | Facebook | Meta Ads: Click-to-WhatsApp | ⚠ verify current version |
| D2 | Ads can appear in "FB/IG Feed, Stories/Reels, Marketplace (and Meta also supports ads that appear in WhatsApp Status)". When tapped, a chat opens "(often with a pre-filled first message). Nothing is sent until the person actually hits Send." (turn 3) | WhatsApp Business; Facebook | Meta Ads placements | ⚠ verify current version |
| D3 | "After the user messages you, a 24-hour customer-service window starts. Inside that window you can reply freely; outside it, you may only send approved message templates (e.g., marketing/utility)." (turn 3) | Facebook Developers | WhatsApp Cloud API | ⚠ verify current version |
| D4 | Use an auto-reply greeting that captures explicit opt-in, e.g. "Reply YES to receive compliance tips and offers on WhatsApp; reply STOP anytime." "This gives you an audit trail of WhatsApp opt-in inside the thread." (turn 1) | Facebook Developers | WhatsApp Business Messaging Policy; DPDP s. 6(10) | ⚠ verify current version. **Gap:** the WA1 greeting built in chat 23 (Jan 2026) has no YES/STOP line |

## E. Customer lists

| # | Rule | Source named in chat | Anchor | Status |
|---|---|---|---|---|
| E1 | "Create a CSV with phone (E.164, e.g., +9198….) and/or email … Meta hashes identifiers on upload. You must certify you have the rights/permissions to use this data. (Minimum ~100 records recommended for match quality.)" (turn 1) | Facebook | Meta Custom Audience Terms | ⚠ verify current version |
| E2 | "Don't upload scraped or purchased lists; don't message numbers without opt-in; and don't imply affiliation/endorsement. Meta may restrict customer-list audiences in certain categories and requires certification you have proper rights." (turn 1) | Facebook | Meta Custom Audience Terms; Meta Advertising Standards. For "don't imply affiliation", see section F | ⚠ verify current version |

## F. Privacy notice and consent wording

| # | Rule | Source named in chat | Anchor | Status |
|---|---|---|---|---|
| F1 | Update the privacy notice to say: "We use your email/phone to show you ads on Meta and to message you on WhatsApp after your consent; you can withdraw anytime." (turn 1) | CookieYes (a vendor blog, not a primary source) | DPDP Act 2023 s. 5 (notice). Compare the current site note: "Details used only to respond to your enquiry." (business-context.md). It does **not** mention ad targeting or WhatsApp marketing | ⚠ verify current version. Update the site privacy policy before any list upload |
| F2 | Consent line for forms and landing pages: "I agree to receive messages from Setindiabiz on WhatsApp and understand I can opt out anytime." (turn 1) | Facebook Developers | DPDP s. 6; WhatsApp opt-in policy | ⚠ verify current version |
| F3 | DPIIT creatives: add a "*Subject to eligibility" footnote for tax/IPR/tender relaxations (turn 7). Mention that "govt fees vary by applicant type (Individual/MSME/Company) and per class" for Trademark (turn 5) | none named | CCPA Guidelines for Prevention of Misleading Advertisements 2022 (disclaimers must not contradict or hide the main claim); ASCI Code Ch. I | ⚠ verify current version |
| F4 | Trust strip / compliance line: "Techno-legal consultancy. Not a law firm." (turns 5, 7) | none named | Advocates Act 1961 / BCI Rules (only advocates may hold out as providing legal services); CCPA Guidelines 2022 | ⚠ verify current version. Keep it on all ads |

## Not raised in chat 24 (added for completeness)
- **Implied government affiliation in DPIIT copy.** "Official Startup India recognition" and "Get DPIIT Recognition" can read as if Setindiabiz is part of Startup India or grants recognition.
  - Do not use the Startup India logo or the State Emblem.
  - Make it clear that recognition is granted by DPIIT.
  - Relevant law: State Emblem of India (Prohibition of Improper Use) Act 2005; Emblems and Names (Prevention of Improper Use) Act 1950; CCPA Guidelines 2022; PPC/CLAUDE.md "Government-service ads".
  - Also check Meta's current policy on ads for government documents and services. ⚠ verify current version.
- **Unsubstantiated trust figures** in chat 24 copy: "50k+ filings", "1,00,000+ filings", "15+ yrs". They are inconsistent with each other and with the site ("20+ years", "18K+ clients"). Basis: CPA 2019 s. 2(28); ASCI Code Ch. I.1. ⚠ verify current version.

## Checklist before running any Click-to-WhatsApp campaign
1. Document the lawful basis for every uploaded list (B1, E1, E2). Never commit the list to this repo.
2. Update the site privacy notice to cover Meta ad targeting and WhatsApp messaging (F1).
3. Add a YES/STOP opt-in line to the greeting and log opt-ins with source, timestamp and purpose (B3, D4).
4. Send marketing templates only to opted-in users. Handle STOP immediately (C2, C6).
5. Check the DND and TCCCPR position for any follow-up calls or SMS (B4).
6. Run a claims check: fees shown match the LP, no government-affiliation wording, trust figures substantiated (F3, F4, Not raised).
