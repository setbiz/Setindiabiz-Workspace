# Google Ads account audit (read-only), 22 Nov 2026

Scope: domestic Google Ads for account 1859576856 "SETINDIABIZ PRIVATE LIMITED 2026" (INR, Asia/Calcutta, auto-tagging on). India Entry / FDI campaigns are owned by the India Entry session and are noted here for context only.
Sources: Supermetrics `AW` (campaign list, campaign detail, conversion actions, shared negative lists, search-term, geo and change-history reports), Zoho CRM COQL (aggregates only), live landing pages fetched 22 Nov 2026, Google Ads policy pages answer/6368711 and answer/13156083 (no "last updated" date shown; read 22 Nov 2026).
**No changes were made to the ad account by this session.**

## 1. Current account state

The repo said the account was empty after Dec 2025. It is not. It holds 12 Search campaigns; none has spent since Jan 2026.

| Campaign | ID | Status | Budget/day | Bidding | Ad review | Notes |
|---|---|---|---|---|---|---|
| Search \| Company Annual Filing \| India | 24528891318 | PAUSED (start 22 Nov 2026) | ₹1,000 | Maximize Clicks, ₹80 CPC cap | 5 RSAs IN_REVIEW | **Created today, 22 Nov 14:59**, via the Claude app under the owner's Google login. Not in any repo changelog. Search only, presence-only geo, en+hi, 36 campaign negatives, no shared list. 4 ad groups (AOC-4/MGT-7, Due Dates, ROC Annual Filing, Annual Compliance) |
| Search \| Trademark Registration \| India | 24046453436 | **ENABLED** (ad groups paused, so NOT_ELIGIBLE) | ₹1,000 | Maximize Clicks | APPROVED | One ad-group unpause from spending. Search partners on, "presence or interest" geo |
| Search \| Company Registration \| India | 24046453343 | PAUSED | ₹1,000 | Maximize Clicks | **DISAPPROVED: GOVERNMENT_DOCUMENTS_AND_OFFICIAL_SERVICES (fully limited)** | Sitelinks edited today 14:55 |
| Search \| GST Registration \| India | 24041432538 | PAUSED | ₹1,000 | Maximize Clicks | **DISAPPROVED: same topic** | Sitelinks edited today |
| Search \| LLP Registration \| India | 24046453643 | PAUSED | ₹1,000 | Maximize Clicks | no disapproval flag | Sitelinks edited today |
| Search \| Copyright Registration \| India | 24041433549 | PAUSED | ₹1,000 | Maximize Clicks | no disapproval flag | Sitelinks edited today |
| Search \| Startup India DPIIT \| India | 24046454783 | PAUSED | ₹1,000 | Maximize Clicks | has disapproved ads | Sitelinks edited today |
| Search \| Virtual CFO \| India | 24050956765 | PAUSED | ₹1,000 | Maximize Clicks | has disapproved ads | Sitelinks edited today |
| Search \| Payroll Outsourcing \| India | 24050957884 | PAUSED | ₹1,000 | Maximize Clicks | has disapproved ads | Sitelinks edited today |
| Search \| Indian Subsidiary Registration \| India | 24041435490 | PAUSED | ₹1,000 | Maximize Clicks | has disapproved ads | India Entry session's scope |
| Search \| India Entry Services \| India | 24041435880 | PAUSED | ₹1,000 | Maximize Clicks | — | India Entry session's scope |
| GADS_Search_IndiaEntry_US_Intent_202612 | 24465038588 | PAUSED (1–30 Dec) | ₹1,500 | Manual CPC | has disapproved ads | India Entry session, logged in PR #2 |

The nine July-2026 campaigns (start 19 Jul 2026) never served. Most likely cause: the disapprovals, and the ad groups being paused.

### Conversion actions (definitions; primary/secondary flags can't be read via Supermetrics)
| Action | Type | Counting | Issue |
|---|---|---|---|
| SETINDIABIZ – GA4 (web) form_submission | GA4 custom | **Many per click** | Use *one per click* for leads |
| SETINDIABIZ – GA4 (web) phone_click | GA4 custom | Many per click | A click, not a call. Should be secondary |
| SETINDIABIZ – GA4 (web) whatsapp_click | GA4 custom | Many per click | A click, not a chat. Should be secondary |
| Lead form – Submit | Google lead-form asset | One per click | OK if lead-form assets are used |
| 4 × "Smart campaign …" (map directions, calls), 2 × YouTube | legacy | — | Clutter; check they aren't primary |
| *NPDI_Thank_You* | — | — | Counted 31 of the 38.94 Dec-25 conversions. **No longer in the account** |

- No offline / CRM import action exists, and no Enhanced Conversions for Leads action is visible. TODO (owner, in the UI): check the Enhanced Conversions toggle and customer-data terms.
- Only **6 of 84** Google leads in the CRM (Nov 25 – Nov 26) have a `gclid` in `Source_Url`. Zoho has no dedicated GCLID field among the classifier fields (`lead-source-attribution-runbook.md` §3). **Offline conversion import cannot work until the GCLID (plus gbraid/wbraid) is captured into a hidden form field and a Zoho field.**

### Shared negative keyword lists: 9 exist, but only 1 is attached
"2022 – Global Negative List" (2,073 terms), "2022 Startup Negative List" (1,641), "New Neg Com Reg Keywords" (1,271), "Startup Negative" (668), "Info Based List" (492), "2022 Trademark Negative List" (239), "SC-SetindiaBiz-Negative-Keywords" (111), "Director KYC Negative" (17), "IE Negatives" (92, attached to the India Entry US campaign only).
**None is attached to a domestic campaign.** The domestic campaigns rely on 14–36 campaign-level negatives each. The old lists are broad-match and some are large; review them before attaching (e.g. "search" in the trademark list is correct, but generic terms in a 2,000-term list may block service queries).

### Billing
Not readable through Supermetrics. TODO (owner): confirm the payment method and any account-level budget in Billing.

## 2. Dec-25 campaigns: what went wrong (data)

### Trademark (₹71,836; search terms visible for ₹51,335)
- **79% of visible spend (₹40,504, 2,630 clicks) went to navigational / DIY queries:** "trademark search" (₹13,760 broad + exact close variant), "ip india" (₹4,084), "ipindia", "ip india trademark search", "trademark public search", "trademark status", and even "https ipindiaonline gov in tmrpublicsearch…". These are people looking for the free IP India public-search portal.
- Only **7% (₹3,629)** went to service-intent queries such as "trademark registration" and "apply / consultant".
- Spend by match type: broad ₹27,753, phrase (close variant) ₹13,811, exact (close variant) ₹7,209, exact ₹1,135, phrase ₹1,426. **Close variants and broad turned registration keywords into portal searches.**
- Geo: India metros (Delhi ₹14.1k, Mumbai ₹8.8k, New Delhi, Bengaluru, Pune…). The geo was not the problem.

### Subsidiary (₹28,092; visible ₹19,127; all broad match)
- Foreign geos (UAE, US, UK, SG, DE, AU) were correct, but broad match bought "how to register a company in india" (3 clicks, **₹7,600**), "subsidiaries" (₹3,078), and "udyam / udyog aadhar" (Indian MSME portal, ≈₹3,000). Effective CPCs of ₹2,500+ suggest an uncapped automated bid strategy.

### Conversion definition
31 of 38.94 conversions came from "NPDI_Thank_You" (now deleted), 4.67 from GA4 form_submission and 3.27 from WhatsApp clicks. The bidder optimised toward page loads and clicks, not qualified leads.

### CRM outcome of the 84 `Advt - Google` leads (Created 1 Nov 2025 – 22 Nov 2026)
| Lead_Status | Leads |
|---|---|
| Lost | 63 (75%) |
| (blank, never worked) | 18 (21%) |
| Valid Lead | 1 |
| Postponed | 1 |
| Establishing Contact | 1 |
| **Deals created** | **0** |

76 of the 84 were created in Dec 2025 – Jan 2026. **Reading:** junk queries brought DIY/portal seekers who were lost. About 1 in 5 leads was never touched, which is a lead-handling gap as well.

**Context, directional only:** for deals created Jan 2023 – Oct 2025 with `Lead_Source = Advt - Google`, there are 22 in W-Login (₹1,13,228) and 9 in W-CSD (₹3,54,698). Google has produced won business before. Caveat: Lead_Source values were migrated (`lead-source-attribution-runbook.md`), and the won-stage definition is still unconfirmed.

## 3. Policy diagnosis (Google Ads "Government documents and official services")
- Policy text read 22 Nov 2026 (answer/13156083): *"Only certified governments and authorized providers may run ads that promote direct acquisition of specific government documents and services."* **"Business identifiers" (e.g. company registration number) is an in-scope category, and India is not in its exclusion list.** Advertisers who don't promote direct acquisition "can request exclusion from the policy" through the certification (godos) form. After that, "you can appeal existing ad disapprovals or resubmit".
- Summary page (answer/6368711): *"Clearly disclose that you are a private entity and not affiliated with any government"*. If you charge for services available free or for less from the government, *"you must disclose this and provide a link to the official government site."* Google also auto-adds a "Not a government website" label on in-scope searches.
- **So the "private firm" line in the ad text alone does not clear Company/GST registration.** The route is the policy-exclusion request (we assist and don't sell the identifier itself), plus a landing page that names the official portal (mca.gov.in / gst.gov.in / ipindia.gov.in) and the statutory fee. Trademark (not a business identifier) was approved with the same style of copy.
- Landing pages already carry disclaimers: `/lp/company-registration` ("not affiliated with or endorsed by MCA or any government body", under the H1), `/lp/trademark-registration` (CGPDTM equivalent), `/company-annual-return` ("independent consultancy, not a government body or law firm"). None of them links to the official portal. That link is the likely gap.

## 4. Compliance flags in ads already built (not live)
Statutes: Consumer Protection Act, 2019 s. 2(28) (misleading advertisement) and s. 21 (CCPA directions/penalties); CCPA Guidelines for Prevention of Misleading Advertisements and Endorsements, 2022; ASCI Code Ch. I (substantiation); Emblems and Names (Prevention of Improper Use) Act, 1950 s. 3. Numbers re-checked against India Code before use: TODO.

| Campaign / asset | Claim | Issue | Fix |
|---|---|---|---|
| All 7 July campaigns, callout | "18,000+ Businesses Served" | Evidence not on file (`business-context.md`) | Substantiate or remove |
| Trademark RSA | "18,000+ Brands Assisted" | Conflicts with LP "13,500+ trademarks protected" | Use the LP figure, with evidence |
| Trademark RSA | "Free TM Search Included" / "Free search…" | "Free" claim not on LP; must be unconditional (CCPA 2022 free-claim provision) | Remove unless the LP states it |
| Trademark RSA | "Attorney-Drafted Filing" | LP says "Licensed TM Attorneys". Needs a named registered trademark agent/advocate | Substantiate |
| Company Reg RSA | "Professional Fees ₹2,499" | Matches LP Basic ₹2,499 (govt fees and GST at actuals stated). But the LP shows strike-through prices (₹6,499 → ₹2,499) | Strike-through "was" prices need a genuine prior price (CPA s. 2(28); ASCI Ch. I) |
| Company Reg RSA | "Incorporation in 7-10 Days", "Free Expert Consultation" | Speed claim depends on MCA processing; "free" must be unconditional | Qualify ("typically, subject to MCA approval") |
| GST RSA | "GST Registration in 3 Days" | Statutory timeline is set by CGST Rules, 2017 r. 9 and is not in our control | Qualify or remove |
| All | "100% Online Process", "No Surprise Pricing" | Absolute claims | Keep only if true for every case |
| Annual Filing (today) | ₹4,599 / ₹5,999 / ₹7,999 / ₹2,999 / ₹1,500 | **Match the live `/company-annual-return` page** ("GST & ROC Fee on Actual") | OK. `business-context.md` "no prices published" is now outdated |
| Annual Filing (today) | "No additional fee: AOC-4 by 31 Dec 2026, MGT-7 by 31 Jan 2027" | Matches MCA General Circular 05/2026 (24 Oct 2026), owner-verified 2 Nov; also on the LP | OK until 31 Jan 2027. Set an end date / pause rule |
| Annual Filing (today) | "₹100 per day per form" | Companies Act 2013 s. 403 + Companies (Registration Offices and Fees) Rules, 2014 (additional fee table) | OK. LP says "₹100 a day" |
| Annual Filing (today) | "3 years in a row can disqualify directors for 5 years" | Companies Act 2013 s. 164(2)(a) | OK |

## 5. Implications for the relaunch
1. **Duplicate-operator risk.** Someone (another Claude session or the owner in Claude) built Annual Filing and edited 7 campaigns today, without a changelog entry. One operator per platform is needed.
2. **Measurement first.** GCLID capture → Zoho field → offline import of *Qualified* and *Won* stages; GA4 actions to secondary; form_submission to one per click. Until then, use Maximize Clicks with a CPC cap or Manual CPC, not Maximize Conversions.
3. **Exact/phrase only, plus an attached shared negative list** seeded from the Dec-25 search terms (ip india, ipindia, public search, trademark search/status/check, udyam, udyog, gov.in, tmr…).
4. **Policy:** file the exclusion request for business-identifier services (Company/LLP/GST) before relaunching those. Lead with services that already pass (Trademark, Annual Filing pending review, Copyright, LLP).
5. **Lead handling:** 21% of Google leads were never worked. Set a response SLA before spending.
