# Compliance Reviewer report: Google Ads relaunch, Trademark + Annual Filing (design_draft v1)

Reviewer: ppc-compliance-reviewer (Goldfish), 22 Nov 2026. Read-only. This is a risk screen, not legal advice.

**What I verified online on 22 Nov 2026**
- Google Ads policy answer/6368711 (fetched): "Clearly disclose that you are a private entity and not affiliated with any government". Also: "If you charge fees for services available for free or less from the government, you must disclose this" and "provide a link to the official government site". No last-updated date is shown.
- MCA GC 05/2026: I did not get the official PDF from mca.gov.in. Secondary sources agree on what it says (careerindia, corpseed, carajput, legalsuvidha, calcguru, casahuja; see Sources at the end):
  - FY 2025-26 only.
  - No additional fee if AOC-4 is filed by 31 Dec 2026 and MGT-7/7A by 31 Jan 2027.
  - It does **not** extend AGM timelines.
  - Older years still pay ₹100/day.
  - One source suggests a tiered fee after the window.
- CCPA Misleading Ads Guidelines 2022: secondary summaries confirm the bait, free-claim and disclaimer provisions exist, but they number the clauses inconsistently. I cite them by name below. Verify the clause numbers on consumeraffairs.nic.in.
- Not re-verified online, from repo or memory: Trade Marks Rules 2017 First Schedule fees, TM Act 1999 ss. 18/25/107/145, Companies Act 2013 ss. 92/96/137/164/403 and the Registration Offices and Fees Rules 2014, the Dark Patterns Guidelines 2023 Annexure 1, and the DPDP Rules 2025 phasing. Verify the current version of each on indiacode.nic.in / mca.gov.in / meity.gov.in.

## Findings

**CR-1 · Blocker · §9 build sheet ("ads verbatim as live… see changelog 22 Nov")**
- **Issue:** No verbatim RSA text exists in the repo for any of the 9 ads. The changelog and audit only list claim fragments. For the 5 Annual Filing RSAs, the only text quoted is the 5 prices, the deadline line, "₹100 per day per form" and the s. 164 line. So the full copy cannot be screened, and I cannot confirm several things:
  - that the "not affiliated with MCA" disclaimer is pinned in the Annual Filing ads (the plan says it is pinned only for Trademark);
  - that "Free TM Search Included", "18,000+ Brands Assisted" and "Attorney-Drafted Filing" were removed from the Trademark ads that were rewritten in place (817539840458 etc.).
- **Provision:** Campaign-plan standard, Blockers ("Ad copy not screened by ppc-compliance-reviewer"; a build sheet that leaves decisions to the implementer); CPA 2019 s. 2(28).
- **Fix:** Paste every headline, description, pin, path, callout and sitelink into §9 (export via Supermetrics Ad report) and re-run this screen. In each Annual Filing RSA, pin to description 1: "Setindiabiz is a private firm, not affiliated with MCA or any government body." (77 chars).

**CR-2 · Blocker · "AOC-4 No Late Fee Till 31 Dec" headline + deadline ads 832341064930 / 832283615649**
- **Issue:** The headline is shown to every annual-filing searcher. The relief covers FY 2025-26 filings only, so a company with older years pending still pays the additional fee. The relief also does not extend the AGM (s. 96), and it does not waive penalties for a late AGM (s. 99) or for non-filing (s. 137(3), s. 92(5)). An unqualified "No Late Fee" therefore misleads by omission. "Late fee" is also not the statutory term.
- **Provision:** CPA 2019 s. 2(28)(iv) (deliberately concealing important information); CCPA 2022 Guidelines, conditions for a valid ad and disclaimers; Companies Act 2013 s. 403 + Registration Offices and Fees Rules 2014; MCA GC 05/2026 (verify the primary PDF).
- **Fix:**
  - Headline: "FY25-26 AOC-4: No Extra Fee" (27).
  - Description: "MCA GC 05/2026: no additional fee for FY 2025-26 AOC-4 by 31 Dec. AGM dates unchanged." (88).

**CR-3 · Major · §7 "MGT-7 copy may run to 31 Jan only after a copy edit"**
- **Issue:** The 1 Jan copy is left undrafted and unscreened.
- **Provision:** As CR-2; Dark Patterns Guidelines 2023, Annex 1 "false urgency".
- **Fix:** Pre-write it now:
  - Headline "FY25-26 MGT-7: No Extra Fee" (27).
  - Description "File MGT-7/7A for FY 2025-26 by 31 Jan 2027 with no additional fee (MCA GC 05/2026)." (83).
  - Pause all AOC-4 deadline assets at 23:59 on 30 Dec, not "on 31 Dec". A lead who clicks on 31 Dec cannot have AOC-4 filed that day, so leaving it running is a bait/urgency risk.

**CR-4 · Major · Plan §8 / launch gates G1–G4**
- **Issue:** Website fixes W3 (official-portal link), W4 (strike-through prices) and W5 (₹1,999 header vs ₹2,000 Basic pack) are cited as mitigations, but the request is "not yet started" and none of them is a launch gate.
  - Without W3, the LPs miss Google's own requirement, since AOC-4/MGT-7 and TM filing can be done direct on mca.gov.in / ipindia.gov.in.
  - Without W4 and W5, the ad price does not match the LP, and the "was" prices are unsubstantiated.
- **Provision:** Google Ads "Government documents and official services" (answer/6368711, verified 22 Nov); CPA 2019 s. 2(28); ASCI Code Ch. I; Dark Patterns 2023 Annex 1 (drip pricing).
- **Fix:** Add G5: "W3, W4, W5 live on /lp/trademark-registration and /company-annual-return; owner screenshot on file."

**CR-5 · Major · TM callout "Fee ₹1,999 + GST"**
- **Issue:** Callouts can serve on their own. This one omits the ₹4,500/₹9,000 statutory fee, so the price can display incomplete.
- **Provision:** Dark Patterns 2023 Annex 1 (drip pricing); CCPA 2022 (bait advertisement); ad-copy standard ("₹X + govt fees").
- **Fix:** Callout "₹1,999 + GST + Govt Fee" (23/25).

**CR-6 · Major · TM callout "Filed Within 24 Hrs" / "Filed in 24 Hrs of Documents"**
- **Issue:** The callout drops the "of documents" qualifier. No operational data is on file; the only evidence is the LP's own claim. Placed next to "10-year validity", it can also read as fast registration, when grant follows examination, objection and opposition.
- **Provision:** ASCI Code Ch. I 1.1/1.4 (substantiation); CPA 2019 s. 2(28); TM Act 1999 ss. 18, 21, 23, 25; s. 107 (no ® before registration).
- **Fix:**
  - Callout "Filed 24 Hrs After Docs" (23).
  - Description "We file within 24 hrs of complete documents. Registration is decided by the Registry." (85).
  - Keep 3 months of filing-time logs as evidence.

**CR-7 · Major · AF prices ₹4,599 / ₹5,999 / ₹7,999 (plan) vs ₹2,999 / ₹1,500 also in the ads (audit)**
- **Issue:** The plan lists 3 prices but the ads carry 5. No ad says what each price covers (forms, turnover slab, audit, ITR). Meta's live GC05 copy uses ₹7,499 for a different pack, so the price is inconsistent across channels.
- **Provision:** CCPA 2022 (bait advertisement, conditions for a valid ad); CPA 2019 s. 2(28).
- **Fix:** Name the scope in the ad, e.g. headline "AOC-4 + MGT-7 from ₹4,599" (25), with "+ GST & ROC fee" in the paired description. List all 5 prices with their LP package in §9.

**CR-8 · Major · Plan §8 "Run only services that have passed review (Trademark, Annual Filing…)"**
- **Issue:** This is factually wrong. All 9 ads are IN_REVIEW, and Annual Filing has never been approved. The "Due Date Searches" ad group bids on informational, portal-adjacent queries ("aoc 4 due date"), which is where the government-documents risk sits.
- **Provision:** Google Ads Government documents and official services (answer/13156083); Emblems and Names Act 1950 s. 3; CPA 2019 s. 2(28).
- **Fix:**
  - Reword to "submitted for review".
  - Add campaign negatives "mca portal", "mca login", "mca.gov.in", "v3".
  - Keep the disclaimer pinned in every Due Date ad.

**CR-9 · Major · "Attorney-Drafted Filing" (audit) / LP "Licensed TM Attorneys"**
- **Issue:** India has no "licensed attorney" status. Filing representation is by a registered trade marks agent or an advocate. The current status of this RSA asset is unconfirmed (CR-1).
- **Provision:** TM Act 1999 s. 145; Advocates Act 1961 ss. 29, 33; BCI Rules Part VI Ch. II r. 36 (verify); CPA 2019 s. 2(28).
- **Fix:** Use "Registered TM Agent Filing" (26) only if a named agent's registration number is on file. Otherwise use "Expert Drafting". Ask the LP owner to correct the LP wording.

**CR-10 · Minor · Statutory facts in copy**
- **Issue:**
  - ₹4,500/₹9,000 are the **e-filing** fees (physical filing is higher).
  - "₹100 per day per form" is correct for delays outside the window. RSA combinations can show it next to "No extra fee", so tie it to the year.
  - "3 years… disqualify directors for 5 years" is correct under s. 164(2)(a), but keep "can".
- **Provision:** Trade Marks Rules 2017 First Schedule entry 1; Companies Act s. 403 + 2014 Fees Rules; s. 164(2)(a) (verify the current versions; the plan's "TODO at gate" is not in G1–G4).
- **Fix:** Add G6 "statutory facts re-checked on India Code/mca.gov.in, date logged". Copy: "Govt fee ₹4,500/class (e-filing)" (31 → shorten to "Govt Fee ₹4,500/Class e-File", 28).

**CR-11 · Minor · "100% Online Process" (AF callout)**
- **Issue:** This is an absolute claim. The owner confirmed it, but there is no process note, and the client may still need to hold a physical AGM.
- **Provision:** ASCI Code Ch. I 1.4; CPA 2019 s. 2(28).
- **Fix:** File the owner's confirmation with the evidence. Optionally use "Filing Done Fully Online" (24).

**CR-12 · Minor · §8 Personal data**
- **Issue:** The plan cites "DPDP (phased)" without stating what is in force. On 22 Nov 2026 only the DPDP Rules 2025 r. 1–2, 17–21 and the consent-manager rule (r. 4, ≈Nov 2026) apply. Obligations under ss. 5, 6 and 8 start ≈13 May 2027 (verify on meity.gov.in). The form notice ("used only to respond to your enquiry") does not cover offline-import matching or Enhanced Conversions. Lead-form assets are not used, which is good.
- **Provision:** IT Act 2000 s. 43A + SPDI Rules 2011 r. 4–5 (in force); DPDP Act 2023 ss. 5, 6, 8 (from ≈May 2027).
- **Fix:** State "No lead-form assets, no Customer Match, no EC until W6". Make W6 a gate for the offline import as well as for Enhanced Conversions.

## Sources
- https://support.google.com/adspolicy/answer/6368711
- https://www.careerindia.com/news/mca-filing-relaxation-2026-new-fee-waiver-deadlines-for-aoc-4-and-mgt-7-forms-for-companies-011-67699.html
- https://www.corpseed.com/law-update/mca-extends-aoc-4-31-december-2026-mgt-7-31-january-2027
- https://carajput.com/blog/p33431/
- https://legalsuvidha.com/latest-updates/mca-extends-fee-relief-for-fy-2025-26-annual-returns-281026
- https://calcguru.in/?p=9880
- https://www.casahuja.com/2026/10/mca-extends-annual-filing-timelines-for.html
- https://en.vikaspedia.in/viewcontent/social-welfare/social-awareness/consumer-education/guidelines-for-prevention-of-misleading-advertisements-and-endorsements-for-misleading-advertisements-2022
- https://www.caclubindia.com/articles/guidelines-for-prevention-of-misleading-advertisements-and-endorsements-for-misleading-advertisements-2022-47580.asp
