# Compliance Reviewer Report: India Entry (FDI) US cross-platform plan, DRAFT v1

_Goldfish: ppc-compliance-reviewer · Review date 14 Nov 2026 · Target `design_draft.md` · This is a risk screen, not legal advice. Items marked **[lawyer]** need a qualified opinion._

**Verdict:** NOT READY TO PUBLISH. There are 2 Blockers, 7 Majors and 8 Minors. The Google RSA copy in §9.1 is close to compliant. The Blockers are (a) copy that hasn't been written yet for Meta, LinkedIn, Reddit and ChatGPT, and (b) lead data shared back to ad platforms under a website notice that rules this out.

## Provisions checked and found correct (no action)
| Plan citation | Check | Result |
|---|---|---|
| BO: profit in each of the last 5 FYs + net worth ≥ USD 100,000; LO: 3 FYs + USD 50,000 (§8, §11.6) | RBI Master Direction 10/2015-16 on rbi.org.in, fetched 14 Nov 2026. Last update shown: **18 May 2021**, so no later update | Correct and current |
| FC-GPR within 30 days, Reg. 4(1) FEMA 395/2019-RB | Matches Build Spec §1 (rbi.org.in, 12 Oct 2026) | Correct |
| FEMA 22(R)/2016-RB full title; Form FNC through AD Cat-I bank ("BO/LO Filing via AD Bank") | Matches MD 10/2015-16 | Correct |
| Companies Act 2013 s.149(3): resident director (182 days in the FY) | Matches; the 2020 relaxations have lapsed | Correct (bare Act on indiacode not re-opened) |
| FEMA 1999 s.2(v), s.2(w); NDI Rules 2019 Sch. IV (NRI non-repatriation) | Correct sections | Correct |
| Emblems and Names Act 1950 s.3 + Schedule; State Emblem of India (Prohibition of Improper Use) Act 2005 | Correct statutes. Descriptive text such as "RBI filings" is not use of a scheduled name for trade | Correct |
| FTC Act s.5, 15 U.S.C. 45 for US audiences | Correct | Correct |
| GDPR Art. 3(2)/Art. 27 not triggered (US-only geo, D16) | Every platform in §9 is US-only | Correct |
| DPDP Act ss.4–6, 8 not yet in force; notice/consent from ≈13–14 May 2027 (G.S.R. 846(E)) | Secondary sources (Nov 2025 notification); no 2026 change to the dates found | Correct. See m4 for the wording |

---

## BLOCKERS

### B1. Copy for four platforms isn't written yet, so it can't be cleared
1. **Severity:** Blocker (for the entities concerned only)
2. **Affected Scope:** §9.3 Meta ads **F1 "Expanding to India"**, **R1 "Moving back to India?"**, **R2 "Set up before you move"** ("brief to follow"); §9.4 LinkedIn **L1, L2** ("brief to follow"); §9.6 Reddit "Ad R1 copy" (undefined for Reddit); §9.5 ChatGPT "Ad text from 9.1 descriptions" (it doesn't say which descriptions, and 9.1 description (4) is the held price line).
3. **Issue + Provision:** The ad-copy standard requires every ad to have compliance sign-off before it publishes, and this reviewer can't clear text that doesn't exist. The four platforms also have their own text limits, and none of their copy carries the government-affiliation disclaimer that §8 requires on "every ad set". Provisions: CPA 2019 s.2(28); CCPA Misleading Ads Guidelines 2022; ASCI Code Ch. I; Meta Advertising Standards (Personal Attributes, see M1); LinkedIn Advertising Policies; Reddit Advertising Policy; OpenAI ad policies (verify current).
4. **Compliant Alternative:** Write the verbatim copy for F1, R1, R2, L1, L2, Reddit R1 and the ChatGPT text, including on-image text, and send it through Goldfish compliance review before any create call. Keep these entities out of the build until then. Every one must carry "Private consultancy, not a government agency" (in primary text or on the image) and must say "resident director arranged separately" wherever it mentions incorporation. For ChatGPT, name the exact descriptions: use 9.1 (1), (2) and (3), and **exclude (4)**.

### B2. Lead data goes back to ad platforms, but the website notice promises otherwise
1. **Severity:** Blocker (for gate G-T items 3–5; do not enable until fixed)
2. **Affected Scope:** §6.3 item 3 "Enhanced conversions for leads on" and offline imports "IE – Qualified lead" / "IE – Won deal"; item 4 Microsoft offline goal; item 6 Meta CAPI sweep; item 7 Reddit Conversions API. §8 "Lead data" row: "no list uploads in this plan".
3. **Issue + Provision:** Enhanced conversions and offline or CAPI uploads send hashed email and phone numbers (or click IDs tied to a named lead) to Google, Microsoft, Meta and Reddit. That is a disclosure of personal data to a third party, even though §8 says there are "no list uploads". The website form notice reads **"Details used only to respond to your enquiry"** (`shared/business-context.md`), and `PPC/CLAUDE.md` already records that this notice "does **not** cover ad targeting". Provisions:
   - **In force now:** CPA 2019 **s.2(47)(ix)**: disclosing personal information given in confidence is an unfair trade practice. The clause number comes from secondary sources; verify it on indiacode.
   - **In force now:** IT Act 2000 s.43A and SPDI Rules 2011 r.4 (the privacy policy must state the purpose and the disclosures).
   - **Platform terms:** Google Ads Customer Data Policies and the enhanced conversions terms require the advertiser's privacy disclosures to cover sharing with Google. Meta Business Tools Terms, Microsoft and Reddit CAPI terms are similar.
   - **From ≈May 2027:** DPDP Act ss.5–6 (purpose-limited notice and consent).
4. **Compliant Alternative:** Before G-T closes, (a) change the website and LP form notice to something like: "We use your details to respond to your enquiry and to measure our advertising. We share limited, hashed contact data with advertising partners (Google, Microsoft, Meta, LinkedIn, Reddit) for measurement only. See our Privacy Policy." (b) Add a matching clause to `/privacy-policy` that names the partners and the measurement purpose. (c) Record the source, purpose, notice version and approver in the plan. Until then, run gclid/msclkid-only offline imports (no hashed PII), or leave enhanced conversions off. Correct the §8 row so it doesn't say "no list uploads" while CAPI and EC are planned. **[lawyer]** for the final notice text.

---

## MAJORS

### M1. "Moving back to India?" may break Meta's Personal Attributes policy
1. **Severity:** Major
2. **Affected Scope:** §9.3 ad names **R1 "Moving back to India?"** and **R2 "Set up before you move"**. If reused on Meta: Google ad group 3 headlines "Moving Back to India?" and "Returning to India? Plan Now", and description (1) "Planning to move back to India?".
3. **Issue + Provision:** Meta Advertising Standards, Privacy Violations and Personal Attributes: ads must not assert or imply a person's race, ethnicity or national origin, directly or indirectly. "Moving **back** to India?" in the second person implies the viewer is of Indian origin. It is likely to be rejected, and repeat rejections hurt the ad account. Google has no comparable copy rule; its Personalized advertising policy covers targeting, not copy. So the Google headlines can stay.
4. **Compliant Alternative (Meta):** Use third-person or service framing that doesn't address the viewer's origin. For example: "Starting a company in India? Set up a private limited company with a CS & CA team." Or: "Planning a business in India from the US? Talk to an India-entry team." Don't use "you/your" next to India origin, NRI status, layoffs or visas. Never mention layoffs or H-1B status in any copy. That would also risk ASCI Code Ch. I (abuse of trust / exploiting a consumer's situation).

### M2. The price headline can appear without its exclusions, and doesn't match the LP
1. **Severity:** Major (headline and description held for now, but the wording must be fixed before release)
2. **Affected Scope:** §9.1 RSA ad group 1 headline **"From USD 499 + Govt Fees"** and description (4) **"…From USD 499 + govt fees & DSC."** These are compared with the §11.4 LP price block **"From USD 499 — consultation and services up to the Certificate of Incorporation. Government fees, stamp duty and DSC extra. Registered office and resident director arranged separately."**
3. **Issue + Provision:**
   - The headline leaves out stamp duty, DSC, the scope limit (up to COI), registered office and resident director. RSAs combine assets freely, so the headline can serve next to descriptions (1) or (3), which carry no exclusions.
   - Description (4) leaves out stamp duty and the scope limit.
   - This conflicts with the ad-copy standard (complete price; ad matches LP) and with CCPA Misleading Ads Guidelines 2022, disclaimer conditions: a disclaimer must not hide material information, and the qualification has to sit with the claim. Clause numbers to be verified against the consumeraffairs.nic.in notification.
   - CCPA Dark Patterns Guidelines 2023, Annexure 1 "drip pricing".
   - CPA s.2(28) and s.2(47)(i).
4. **Compliant Alternative:** Delete the price headline, or keep it only if it is pinned and a pinned description carries the full exclusions. Rewrite description (4) as: "From USD 499 up to incorporation certificate. Govt fees, stamp duty & DSC extra." (78 characters). Pin it to description position 2 whenever the price headline is live. Keep "Resident director & office arranged extra" in pinned description 1 (see M5).

### M3. "From USD 499" needs bait-ad substantiation
1. **Severity:** Major
2. **Affected Scope:** Every "From USD 499" line (§8, §9.1, §11.4).
3. **Issue + Provision:** FDI average order value is ₹86,300 (§2/§4), about 2× USD 499. The plan has no evidence on file of how many subsidiary engagements actually close at USD 499 for the stated scope. CCPA Misleading Ads Guidelines 2022, bait-advertisement conditions: a low-price ad must not entice consumers unless the service is genuinely available at that price, and any limitations must be stated. Also CPA s.2(28) and ASCI Ch. I 1.1 (substantiation).
4. **Compliant Alternative:** Put an evidence note on file before the price is released. It should give the scope delivered at USD 499, the count and share of FDI deals in the last 12 months billed at that professional fee, and a statement that the price is offered to all comers. If the evidence is thin, run without price (the "Get a Written Quote" CTA already works).

### M4. GST isn't covered in the USD 499 price for buyer group B
1. **Severity:** Major
2. **Affected Scope:** §11.4 price block. Any price line shown to ad group 3 / Meta ad set 2 / Reddit (returning founders).
3. **Issue + Provision:** The zero-rating in Build Spec §1 (IGST Act ss.2(6), 13(2), 16; LUT) holds only when the recipient is outside India and pays in convertible foreign exchange. A returning founder who pays after moving, pays in INR, or contracts in the name of an Indian entity owes 18% GST. "USD 499" with no tax note is then an incomplete price: CPA s.2(28); Dark Patterns Guidelines 2023, drip pricing.
4. **Compliant Alternative:** Add "GST extra where applicable (zero-rated for clients outside India paying in foreign currency)" to the LP price block. Keep price out of all group B ads, as the plan currently does. **[lawyer/CA]** to confirm the export-of-services position for individual clients.

### M5. The government-affiliation disclaimer isn't guaranteed to show
1. **Severity:** Major
2. **Affected Scope:** §9.1/§9.2 "Pin 'Private Firm, Not a Govt Body' to position 3". Description "(2) Private consultancy, not a government agency…" is unpinned. §8 says "Every ad set/LP" carries it.
3. **Issue + Provision:** Google often serves only headlines 1–2. A position-3 pin is shown only some of the time, and an unpinned description may never serve. Provisions: Google Ads policy "Government documents and official services" (verify current; it requires that ads and LPs not imply government affiliation) and Misrepresentation policy; Emblems and Names Act 1950 s.3; CCPA Guidelines 2022 (no false impression of affiliation). Microsoft imports the same pins.
4. **Compliant Alternative:** Pin description (2) "Private consultancy, not a government agency. Resident director & office arranged extra." to **description position 1** in all three ad groups (descriptions in position 1 serve on every impression that shows a description). Keep the headline pin at 3 as an extra. Keep the callout "Private consultancy". For Meta, LinkedIn, Reddit and ChatGPT, carry the line in body or on-image text (B1).

### M6. Reddit and Meta targeting contradicts the plan's own no-national-origin rule
1. **Severity:** Major
2. **Affected Scope:** §9.6 communities **r/ABCDesis**, **r/nri**, **r/h1b**, r/returnToIndia, r/IndiaInvestments. §9.3 ad set 2 "Advantage+ audience with suggestions". §8 "No ethnicity/national-origin targeting on any platform".
3. **Issue + Provision:** r/ABCDesis is defined by ethnicity (American-born South Asians) and doesn't fit the returning-founder profile either. r/nri is defined by national origin and residency, and r/h1b by immigration status. Targeting them reaches people through a protected or sensitive attribute, which is what §8 forbids. Provisions: Reddit Advertising Policy (targeting/sensitive categories; verify the current text in the Reddit UI at build); Meta Discriminatory Practices policy; ASCI Ch. I (exploiting the consumer's situation, given the layoffs/visa framing in §1). US civil-rights ad law is strict mainly for housing, employment and credit, which don't apply here. But the plan has adopted a stricter rule and should follow it.
4. **Compliant Alternative:** Drop r/ABCDesis. The owner should decide on r/nri and r/h1b and record the decision in the plan: either keep them as communities about **returning or starting a business**, with the §8 wording changed to match, or replace them with r/returnToIndia, r/IndianStartups and r/Entrepreneur plus keyword targeting ("start company in India", "move to India business"). Note the internal inconsistency: Google negates "visa, h1b" while Reddit targets r/h1b. On Meta ad set 2, document the seed interests, and confirm none is an ethnicity proxy (e.g., Indian culture, Bollywood, Indian diaspora).

### M7. "CS & CA-Led" claim, and publishing professionals' names and membership numbers
1. **Severity:** Major **[lawyer]**
2. **Affected Scope:** §9.1 headline **"CS & CA-Led India Team"**, callout "CS & CA team", ad group 3 description (1) "…with a CS & CA team". §11.5 "CS & CA team names and membership numbers with consent".
3. **Issue + Provision:**
   - D21 (13 Oct) substantiates only that the FDI team has "a qualified CS and CA **on staff or retainer**". "**Led**" is a stronger claim (CPA s.2(28); ASCI Ch. I 1.1).
   - If the CA or CS is a **member in practice** (for example, on retainer), naming them in paid ads, with membership numbers, for the firm's benefit can expose them to professional misconduct for solicitation or advertising: Chartered Accountants Act 1949, First Schedule Part I, Clauses (6) and (7); Company Secretaries Act 1980, First Schedule Part I, Clauses (6) and (7); ICAI/ICSI advertisement guidelines (verify current editions).
4. **Compliant Alternative:** Change the headline to "CS & CA India-Entry Team" or "Team with CS & CA Experts" (the D21-approved phrase). Use "Led" only if a CS or CA employee actually heads the FDI desk, with evidence on file. Before §11.5 goes live, confirm each named professional's status (in employment, not in practice) and get written consent. If they are in practice, don't publish names or numbers.

---

## MINORS (Nit)

### m1. The "US time zone" promise is wider than actual coverage
- **Scope:** §9.1 descriptions **"Book a call at a time that suits your US time zone…"**; callout **"US time-zone calls"**. §6.4 itself says "Pacific mornings fall outside". Actual slots are 19:30–23:00 IST = 9:00–12:30 ET / 6:00–9:30 PT, and 08:00–10:00 IST = 21:30–23:30 ET (previous day).
- **Provision:** CPA s.2(28); ASCI Ch. I 1.1.
- **Fix:** "Book a call in US morning or evening hours, or ask for a written quote by email." (83 characters). Callout: "US-Hours Call Slots".

### m2. "Written quote first" has no evidence
- **Scope:** Callout "Written quote first"; headline "Get a Written Quote".
- **Provision:** ASCI Ch. I 1.1. `shared/business-context.md` marks "written estimate first" as "Process doc TODO".
- **Fix:** File the process doc (SOP: quote issued before any payment). Until then, use "Get a Written Quote" only, which is a CTA rather than a claim.

### m3. "Free consultation" in the follow-up flow
- **Scope:** §6.4 email template "SIB-05 India Entry – Free consultation link" and Zoho Bookings "Free Consultation - Ordinary Services". These are customer-facing.
- **Provision:** CCPA Misleading Ads Guidelines 2022, free-claim conditions (only if nothing is payable beyond the unavoidable cost of responding); dark-pattern flag F7.
- **Fix:** Keep "free" only if the consultation is unconditional, with no fee credited, deposit or obligation. Otherwise say "Consultation call".

### m4. Citation precision in §8
- **Advocates Act row:** BCI Rules Part VI Ch. II r.36 binds advocates, not Setindiabiz. The rules that bind a non-advocate firm are Advocates Act 1961 **s.33 and s.45** (practising law without enrolment), with *Bar Council of India v. A.K. Balaji* (2018) 5 SCC 379 on foreign or non-advocate legal practice. Add these; keep r.36 only for the Juriskps point.
- **Lead-data row:** SPDI Rules **r.5** applies to *sensitive* personal data (passwords, financial or health data); name, email and phone are not SPDI, so cite r.4 (privacy policy) and CPA s.2(47)(ix) instead. Restate DPDP as follows. Board provisions in force since 13/14 Nov 2025. Consent-manager provisions (Rule 4) from 13/14 Nov 2026, i.e. this week; no direct effect. Act ss.4–6, 8 and the Rules' notice requirements from ≈13/14 May 2027. Verify on meity.gov.in / egazette.
- **Missing:** add the **CCPA Guidelines for Prevention and Regulation of Dark Patterns, 2023** (Annexure 1: drip pricing, false urgency, disguised ads) to the §8 misleading-claims row and to §11.4/§11.5. Verify the CCPA 2022 clause numbers against the consumeraffairs.nic.in notification before quoting numbers.

### m5. Land-border sources and first-call screening
- **Scope:** §3 Geo "Press Note 3 (2020) as amended by Press Note 2 (2026)"; §8 regulatory row "S.O. 2174(E), 3030(E), 4870(E)".
- **Issue:** Build Spec §1 records that the government copies of Press Note 2 (2026) and the three S.O.s were **never opened**; all are secondary sources. Also, a US parent can still have land-border beneficial owners (the look-through test in S.O. 2174(E)). This plan doesn't carry the SIB-05 first-call screening into §6.4.
- **Provision:** FEM (Non-debt Instruments) Rules 2019 r.6(a) proviso as amended; Press Note 3 (2020) / PN 2 (2026). Mark these "verify current version".
- **Fix:** Open dpiit.gov.in and egazette.gov.in copies before launch. Add to §6.4: "Handler screens land-border beneficial ownership on the first call, before any proposal."

### m6. US contact and email law for US leads
- **Scope:** §6.4 calls and WhatsApp to US numbers; Zoho Marketing Hub drip (separate session).
- **Provision:** TCPA, 47 U.S.C. 227 (no autodialled or prerecorded calls or automated texts to US mobiles without prior express written consent; manual calls are fine). CAN-SPAM Act, 15 U.S.C. 7704 (physical postal address, working opt-out honoured within 10 business days, non-deceptive subject lines) for the drip. US state privacy laws (e.g., California CCPA/CPRA) probably fall below their revenue or volume thresholds; confirm and note it in the plan.
- **Fix:** Add one line to §6.4 and to the drip brief. Keep WhatsApp outreach manual, or base it on the consent checkbox wording ("email, phone and WhatsApp").

### m7. Past Google policy disapprovals are unexplained
- **Scope:** §2 "Google Dec-25 … policy disapprovals".
- **Provision:** Google "Government documents and official services" and Misrepresentation policies (verify current).
- **Fix:** Record which policy and which asset were disapproved before building §9.1, and check that the new copy doesn't repeat the problem. Kill rule K4 then has a baseline.

### m8. Form wording for individuals (group B)
- **Scope:** §9.3 form v2 keeps Q2 "Where is your parent company incorporated?" while adding the option "Private limited company (I am moving to India)". §11.3 LP form.
- **Provision:** Data accuracy and minimisation, dark-pattern flag F11; DPDP Act s.6(1) (from May 2027).
- **Fix:** In form v2, add a Q2 option "I am an individual (no parent company)", per §6.3 item 8. Keep company optional for individuals in the LP form and in the LinkedIn Lead Gen Form.

---

## Personal data in the repo
No raw customer PII found in the target. Account IDs only; no customer names, emails or phone numbers. The phone number in the Build Spec is already redacted.

## Sources consulted (14 Nov 2026)
- RBI Master Direction 10/2015-16 (BO/LO/PO), rbi.org.in, `BS_ViewMasDirections.aspx?id=10404`: last updated 18 May 2021; criteria confirmed.
- Meta Advertising Standards, Personal Attributes / Privacy Violations and Personal Attributes; Discriminatory Practices (transparency.meta.com, via search results).
- DPDP Rules 2025 phased commencement: secondary summaries (Mondaq, AZB, AMS Shardul). No 2026 amendment found.
- CCPA Misleading Ads Guidelines 2022: secondary summaries (Vikaspedia, AZB, Mondaq). Clause numbers not verified; the official text is on consumeraffairs.nic.in.
- CPA 2019 s.2(47)(ix): secondary sources; verify on indiacode.nic.in.
