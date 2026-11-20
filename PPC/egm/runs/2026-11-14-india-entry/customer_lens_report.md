# Customer Lens Report: India Entry (FDI) · US · DRAFT v1

_Goldfish reviewer: `ppc-customer-lens`. Target: `design_draft.md` (§1, §9, §11). Standard: `egm/standards/ad-copy-standard.md`. Date: 14 Nov 2026._

**Persona note:** `reviewers/customer_lens.md` describes a Tier-2 Indian first-time founder. As instructed for this run, I read the ads as two US personas instead:
- **(A)** a US company founder or CFO looking at India expansion
- **(B)** an Indian-origin tech professional in the US who plans to move back and start a company

Severity scale: Blocker / Major / Minor. Minor is the same as "Nit" in the persona file.

**Character limits:** I counted every Google headline and description in §9.1 by hand. All of them are within 30 and 90 characters. The longest headlines are 29 ("Talk to an India Entry Expert", "Private Firm, Not a Govt Body"). The longest description is exactly 90 (AG1/AG2 "Subsidiary, branch or liaison office? …"). Every rewrite below is counted and stays within the limits.

---

## Scorecard (1–5; the standard needs ≥ 4 on both clarity and trust)

| Ad | (A) Clarity | (A) Trust | (B) Clarity | (B) Trust | Passes? |
|---|---|---|---|---|---|
| Google RSA AG1 `Subsidiary` | 3 | 3 | 3 | 3 | No |
| Google RSA AG1 + price lines (held back) | 3 | 3 | 3 | 3 | No |
| Google RSA AG2 `Branch-Liaison` | 2 | 3 | 2 | 3 | No |
| Google RSA AG3 `Returning-Founder` | 2 (not for me) | 3 | 4 | 2 | No |
| Microsoft (copy of 9.1) | same as Google | | | | No |
| ChatGPT (9.1 descriptions) | 3 | 3 | 3 | 3 | No |
| Meta B2 Branch office (existing creative, not shown) | unscorable | | | | No |
| Meta F1, R1, R2 | unscorable: "brief to follow" | | | | No |
| LinkedIn L1, L2 | unscorable: "brief to follow" | | | | No |
| Reddit R1 | unscorable: R1 copy doesn't exist | | | | No |

With the fixes below, I'd expect AG1 and AG3 to reach 4/4 for their own persona and AG2 to reach 4/4 for persona A.

---

## Blockers

### F1
1. **Severity:** Blocker
2. **Affected Scope:** Meta F1, R1, R2 and B2; LinkedIn L1, L2; Reddit R1 (§9.3, §9.4, §9.6)
3. **What I thought / felt:** There's nothing for me to read. Four of the six funded platforms (Meta, LinkedIn and Reddit, about 45% of the month-1 cap) have no verbatim copy. B2 is referenced only by creative ID. I can't judge whether these ads are clear or trustworthy.
4. **What would fix it:** Before Goldfish sign-off, put the verbatim primary text, headline, description, CTA and image or video text for every one of these ads into the plan, then re-run the customer lens on them. Until then, those platforms can't pass the standard's "≥ 4/5 from ppc-customer-lens" gate. Google and Microsoft can go ahead separately.

### F2
1. **Severity:** Blocker (AG3 only)
2. **Affected Scope:** Google/Microsoft AG3 `Returning-Founder`; interim landing page (§9 "Landing pages")
3. **What I thought / felt (B):** I clicked "Moving Back to India?" and landed on a page that, according to the plan itself, is about branch and liaison offices for foreign companies. That isn't me. I'd bounce, and I'd start to think the firm doesn't really serve people like me.
4. **What would fix it:** Hold AG3 until LP (c), "Moving back to India? Start your company", is live with an H1 that repeats the headline (§11.1). If AG3 must launch earlier, send it to a page about forming a private limited company as an individual (for example `/start-business-india` or `/company-registration-for-foreigners`, whichever really covers that). Do this only after a human confirms the page content matches the ad.

---

## Major

### F3: Indian jargon a US buyer can't decode
1. **Severity:** Major
2. **Affected Scope:** AG1 headlines "CS & CA-Led India Team", "FC-GPR & FEMA Reporting"; AG2 headline "BO/LO Filing via AD Bank" and description 1; D1 "RBI & ROC filings"; D4 "DSC"; callout "CS & CA team"; sitelink "FDI reporting (FC-GPR)"
3. **What I thought / felt (A):** CS? Customer service? I have no idea what an AD bank, FC-GPR, ROC or DSC is. It reads like an ad written for someone else. (B can read CS/CA and ROC, but FC-GPR and AD bank still mean nothing to me.)
4. **What would fix it:** Use plain English in AG1/AG2. Keep "CS & CA" in AG3, where B understands it.

   | Current | Rewrite | Chars |
   |---|---|---|
   | CS & CA-Led India Team (AG1, AG2) | Company Secretaries & CAs | 25 |
   | FC-GPR & FEMA Reporting | RBI Foreign Investment Filing | 29 |
   | BO/LO Filing via AD Bank | Branch Office RBI Filing | 24 |
   | AG2 D1: Branch & liaison office applications through your AD bank, plus ROC registration after. | Branch or liaison office application prepared, filed via an Indian bank, then registered. | 89 |
   | D4 (held): …From USD 499 + govt fees & DSC. | Indian subsidiary setup by a CS & CA team. From USD 499 + govt fees & digital signatures. | 89 |
   | Sitelink "FDI reporting (FC-GPR)" | "Foreign investment reporting" | — |

   The compliance reviewer should confirm that "filed via an Indian bank" correctly describes the AD Category-I bank route. If D4 is changed, the LP price block (§11.4) must say "digital signature certificates (DSC)" in the same words.

### F4: No reason to trust a firm I've never heard of
1. **Severity:** Major
2. **Affected Scope:** All Google RSAs, assets, LP §11.5
3. **What I thought / felt (A):** You're asking me to hand my Indian subsidiary to an overseas firm. The headlines give no years in business, no client count, no address and no names. The only "trust" line tells me you aren't the government, which I never thought you were. (B: I'd compare you with a CA friend back home. Why you?)
4. **What would fix it:**
   - Use the one claim already evidenced in `business-context.md`: headline **"4 Offices Across India"** (22) and callout "Offices in Delhi, Mumbai, Bengaluru".
   - Get evidence on file quickly for one more claim (for example "200+ foreign entities" or "20+ years") and add it as a headline.
   - On the LP, add the company's legal name, CIN, registered office address, named CS/CA with membership numbers (already in §11.5), a sample engagement letter, and how a US client pays (USD wire or card).

### F5: Is the call free or paid?
1. **Severity:** Major
2. **Affected Scope:** "Book a Consultation Call", D3, callout "Written quote first"
3. **What I thought / felt (A and B):** Will I be billed for this consultation? Consultants charge for calls. The follow-up email is titled "Free consultation link", but the ad doesn't say so.
4. **What would fix it:** Once the free-consultation process doc is on file (`business-context.md` still marks it TODO), use **"Book a Free 30-Min Call"** (23). If it isn't free, say "Paid consultation" on the LP. Either way, state the reply time on the LP, for example "We reply within 1 business day".

### F6: Resident-director line confuses buyer group B
1. **Severity:** Major
2. **Affected Scope:** AG3 description 2 (also AG1/AG2 description 2)
3. **What I thought / felt (B):** I'm moving back, so I'll be the director. Why would you charge me to arrange one? (A: "Arranged extra". Does that mean you provide one at a cost, or do I have to find one myself?)
4. **What would fix it:**
   - AG3 D2: **"Private consultancy, not a government agency. We explain the resident director rule."** (84). The compliance reviewer should confirm this still doesn't imply that no resident director is needed (Companies Act 2013 s.149(3)).
   - AG1/AG2 D2: **"Private consultancy, not a government agency. Resident director & office: extra cost."** (85)

### F7: "From USD 499" sets an expectation the deal won't meet
1. **Severity:** Major
2. **Affected Scope:** Held-back headline "From USD 499 + Govt Fees", D4, LP §11.4
3. **What I thought / felt (A):** USD 499 for a subsidiary sounds great. Then the quote comes back much higher once the resident director, registered office and post-incorporation filings are added. (The plan's own FDI AOV is ₹86,300, well above USD 499.) I'd feel baited, even though "From" is technically true. Also, AG1 rotates "Compare Branch vs Subsidiary" next to the price, so I might think a branch office also costs USD 499.
4. **What would fix it:**
   - On the LP, list "Included / Not included". FC-GPR, bank account opening and the first-year compliance package must each be marked one way or the other.
   - Show a typical all-in range, marked as an estimate.
   - State that the price applies to a subsidiary only.
   - In the ad, keep "From USD 499 + Govt Fees" only in AG1 and add the callout "Subsidiary setup price".

### F8: The form puts buyer group B off
1. **Severity:** Major
2. **Affected Scope:** LP §11.3 form; Meta form v2; LinkedIn Lead Gen Form "work email"
3. **What I thought / felt (B):** You want my *work* email for a "moving back to India" enquiry? My employer would see it. I'd close the tab. (A: a phone number is required for an overseas firm I don't know yet, so I expect spam calls from India.)
4. **What would fix it:**
   - On LP (c) and in the Meta R ads, label the field **"Email"**, not "Work email".
   - Make phone optional, with the note "only if you'd like a call".
   - Keep "work email" on LinkedIn, which serves group A only.

### F9: Group B's real fear isn't answered
1. **Severity:** Major
2. **Affected Scope:** AG3 headline "Set Up Before You Move Back"; LP (c) §11.6
3. **What I thought / felt (B):** I'm on an H-1B. If I set up an Indian company now, will that hurt my visa? Am I investing as an NRI or as a foreigner? The ad tells me to act now and answers neither question.
4. **What would fix it:** Add an FAQ block to LP (c):
   - "Can I set up while on a US work visa?" Answer: the share-ownership-versus-working distinction, plus "check with a US immigration attorney". We aren't one.
   - "Does it matter whether I invest before or after I move?" Answer: "our team assesses NRI vs FDI route on the call". This matches the plan's rule that the sales call decides the route.

   Keep the ads free of FEMA and visa positions, as §8 requires.

### F10: "NRI" leaves out US-citizen founders
1. **Severity:** Major (B only)
2. **Affected Scope:** AG3 headline "Indian Pvt Ltd for NRIs"; keywords
3. **What I thought / felt (B, US citizen with an OCI card):** I'm not an NRI any more, so this probably isn't for me.
4. **What would fix it:** Use **"Pvt Ltd for NRIs & OCIs"** (23). The compliance reviewer should confirm that naming OCI cardholders doesn't amount to a FEMA route claim (NDI Rules 2019 Sch. IV).

---

## Minor

### F11
1. **Severity:** Minor
2. **Affected Scope:** "Private Firm, Not a Govt Body" (pinned at H3) and D2
3. **What I thought / felt (A):** "Govt Body" reads as Indian English, and the line makes me wonder why you need to say it. It also uses two of my few lines of copy to say the same thing twice.
4. **What would fix it:** For US readers, say **"Private Firm, Not a Gov Agency"** (30). A note for the compliance reviewer: an H3 pin isn't shown in every impression, so if the disclaimer has to appear every time, also pin D2 to description position 1 or 2.

### F12
1. **Severity:** Minor
2. **Affected Scope:** AG1 headline "For US Companies to India"
3. **What I thought / felt (A):** The grammar is clumsy and reads like a translation.
4. **What would fix it:** **"Helping US Firms Enter India"** (28)

### F13
1. **Severity:** Minor
2. **Affected Scope:** AG2 (branch/liaison)
3. **What I thought / felt (A, a 2-year-old startup):** I click, then find out on the LP that I'm not eligible (5 years of profits). That wastes my time and your budget.
4. **What would fix it:** Add the headline **"For Established Foreign Firms"** (29). Keep the detailed eligibility on the LP, as §8 says.

### F14
1. **Severity:** Minor
2. **Affected Scope:** LP §11.7 hours; D3
3. **What I thought / felt (B, Bay Area):** You show IST and ET. I'm on Pacific time, and many people like me are.
4. **What would fix it:** Show IST, ET and PT. The booking slots (19:30–23:00 and 08:00–10:00 IST) work out to roughly 6:00–9:30 am PT and 6:30–8:30 pm PT, so list them that way.

### F15
1. **Severity:** Minor
2. **Affected Scope:** AG3 headline "Returning to India? Plan Now"
3. **What I thought / felt (B, recently laid off):** "Plan Now" feels like it's pushing on my anxiety.
4. **What would fix it:** **"Returning to India? Start Here"** (30)

### F16
1. **Severity:** Minor
2. **Affected Scope:** ChatGPT ads (§9.5)
3. **What I thought / felt:** The Google descriptions are reused here, so they carry the same jargon issues as F3.
4. **What would fix it:** Apply the F3 and F6 rewrites, and write prompt-specific copy before phase 2.

---

## LP requirements (§11): customer view, in short
- **Works for me:** one page per message with the H1 matching the ad; the disclaimer above the fold; USD pricing with exclusions; no unevidenced numbers; IST and ET hours; timelines marked as estimates.
- **Add:** F4 trust block (CIN, address, named team, how to pay in USD); F7 included/not-included list and typical total; F8 form changes; F9 FAQ for group B; F14 PT hours; a stated reply time.
