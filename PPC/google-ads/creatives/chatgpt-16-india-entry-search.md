# Google Ads: India-entry Search keywords, policy-safe wording and landing-page plan (ChatGPT chat #16)

- **Source:** ChatGPT chat #16 "How to advertise", stated date Mon, Jun 29 (year inferred as 2026), turns 12–18. URL: https://chatgpt.com/c/cc30545d-e1a0-8328-8b18-54ca398d8c6e
- **Import file:** `PPC/imports/chatgpt/conversations/16-how-to-advertise.md`
- **Situation reported by Sanjeev (verbatim):** turn 12: "in the Google ads, our ads are not approved because the reason is that it is about some government." Turn 14: "The rejection is mostly because of the government service policy."
- **Status:** not launched. The policy rejections are **unresolved** in the chat. ChatGPT recommended Google Search at 40–50% of budget "once the government-service policy issue is fully resolved".
- Microsoft Ads reuses the same keywords and copy: `PPC/microsoft-ads/creatives/chatgpt-16-india-entry-search.md`.

## Compliance and policy notes
- **Google Ads "Government documents and official services" policy.** ChatGPT (turn 18) read it as: Google "restricts ads promoting direct acquisition of certain government documents and services unless the advertiser is certified/authorised; business identifiers are included, although India appears as an excluded region that still requires applying for exclusion to avoid improper disapproval." This is ChatGPT's reading. **Verify the current policy text and any India exemption or certification route in the Google Ads Policy Centre before appealing.**
- **Implied government affiliation:** the "Avoid" list below is correct practice under CPA 2019 s.2(28), CCPA Misleading Ads Guidelines 2022 and the ASCI Code Ch. I, as well as platform policy. Never use "official", "Government Registration", "MCA approval", "ROC approval guaranteed" or "RBI approval guaranteed".
- **Tax figures on the site** (turn 18): the Liaison Office page says foreign company tax is 40%, the Branch Office page says 35% from AY 2025–26. Finance (No.2) Act 2024 cut the rate to 35%. The Income-tax Act 2025 applies from 1 Apr 2026, so re-cite under the new Act and verify. A Liaison Office cannot earn income in India, so the 40% line is doubly misleading. Fix it before the page is used as a landing page.
- **"18,000+ Happy Customers"** on `/india-entry-services` needs substantiation; it is TODO in `business-context.md`.

## Verbatim assets

### Example keywords (turn 16)
> Set up company in India
> India company incorporation
> Foreign company registration India
> India subsidiary
> Register company India for foreigners
> Wholly owned subsidiary India
> Branch office India
> Liaison office India
> India market entry
> FDI consulting India
>
> This should be nearly 40–50% of your advertising budget.

Turn 10: "On Google Ads and Microsoft Ads, bid on intent-rich keywords like 'set up company in India' or 'India subsidiary registration.'"

Negative-keyword themes, from the "Do not optimize for" list: students, visa seekers, job seekers, local Indian "company registration" searchers, freelancers. Add these to `google-ads/campaigns/negatives.md` when building the campaign.

### Policy-safe wording (turn 16)
> Because your ads relate to government filings, avoid language that implies you are an official authority.
> Avoid:
> ❌ Register Company with MCA
> ❌ Government Registration
> ❌ Official Registration
> Instead use:
> ✅ India Business Setup Experts
> ✅ Company Incorporation Consultants
> ✅ Foreign Investment Advisory
> ✅ End-to-End India Entry Support
>
> Also ensure your landing pages clearly state:
> Setindiabiz is a private legal, tax and compliance consulting firm. We are not affiliated with the Government of India or the Ministry of Corporate Affairs.
>
> That disclaimer should appear in the footer and on service pages. It often helps with policy reviews, though Google's decision depends on the specific policy trigger.

Longer disclaimer for `/company-registration-for-foreigners` (turn 18):
> Setindiabiz is a private legal, tax and compliance advisory firm. We are not affiliated with the Ministry of Corporate Affairs, Registrar of Companies, RBI or any Government of India department.

Government service policy guidance (turn 14):
> To comply, ensure your ad copy clarifies that you're a private consultancy facilitating the process rather than offering a government service directly. You might need disclaimers and a clear distinction that you are not a government entity. If necessary, appeal with supporting documents showing you are a legitimate advisory service.

Turn 13: "you'll need to identify the exact policy trigger … ensure that your ad copy is factual and not promissory … We can refine the wording or apply for a manual review."

### Page rules for every paid landing page (turn 18)
> Every paid landing page should clearly say "private advisory firm, not a government website."
> Avoid hero phrases like "official registration," "government registration," "MCA approval," "ROC approval guaranteed," or "RBI approval guaranteed."
> Use "support," "advisory," "coordination," "documentation," "filing assistance," and "compliance guidance."
> Every page must have: one primary CTA, one downloadable checklist, one comparison table, one "who this is for" section, one "not suitable if" section, FAQ schema, internal links to related pages.
> Treat WOS, Branch Office, Liaison Office and Project Office as separate commercial intents, not one generic "company registration" intent.

### Ad messaging lines (turn 16)
> Expand into India without compliance mistakes.
> Launch your India subsidiary in weeks, not months.
> Enter India's fastest-growing economy with experienced advisors.
> From incorporation to payroll—we manage your India operations.
> Trusted by global companies entering India.

### Existing-page audit: recommended title tags / H1s (turn 18, ChatGPT; not applied)

| Current URL | Recommended title tag | Recommended H1 | Priority |
|---|---|---|---|
| /india-entry-services | India Entry Services for Foreign Companies \| Set Up Business in India | India Entry Services for Foreign Companies and Investors | Very high |
| /company-registration-for-foreigners | Company Incorporation in India for Foreigners & Foreign Investors | Private Company Incorporation Support in India for Foreigners | Very high ("BOFU paid-search landing page") |
| /indian-subsidiary-registration | Wholly Owned Subsidiary Registration in India \| Indian Subsidiary Setup | Wholly Owned Subsidiary Registration in India | Very high |
| /branch-office-registration-india | Branch Office Registration in India for Foreign Companies \| RBI & ROC Support | Branch Office Setup in India for Foreign Companies | High |
| /liaison-office-registration-india | Liaison Office Registration in India \| RBI Approval & ROC Compliance | Liaison Office Setup in India for Foreign Companies | High |
| /project-office-registration-india | Project Office Registration in India for Foreign Companies \| RBI & ROC Support | Project Office Setup in India for Foreign Companies | Medium-high |
| /foreign-direct-investment-india | FDI Advisory in India \| Foreign Direct Investment Rules & Compliance | FDI Advisory for Foreign Investors Entering India (CTA "Get FDI Route Review") | High |
| /fdi-reporting-fcgpr | FC-GPR Filing for Foreign Investment in India \| RBI FIRMS Compliance | Form FC-GPR Filing for FDI in Indian Companies | Medium-high |
| /fla-return-filing-rbi | FLA Return Filing with RBI \| Foreign Liabilities and Assets Return | — | Medium |
| /company-registration-in-india-for-chinese | Company Registration in India for Chinese Investors \| FDI Approval Advisory | — ("Preliminary eligibility review" CTA, not "register now") | Medium |

Note: the title "Liaison Office Registration in India | RBI Approval & ROC Compliance" puts "RBI Approval" in the title. Check it against the "avoid approval language" rule above before using it in ads.

ChatGPT's comment on the current foreigner page H1, "Company Registration By Foreigners In India 100% Online, Simplified & Affordable": "too salesy and policy-sensitive … may increase the risk of government-service policy triggers because it looks like a direct registration service."

Structure selector for `/india-entry-services` (turn 18):

| Your India Objective | Recommended Route |
|---|---|
| Own and operate an Indian company | Wholly Owned Subsidiary |
| Test market without revenue activity | Liaison Office |
| Execute a specific Indian contract | Project Office |
| Conduct limited commercial activities | Branch Office |
| Co-invest with Indian partner | Joint Venture |
| Hire, invoice and operate long-term | Private Limited Company / WOS |

### Landing pages by intent (turn 16)
> USA → India Company Registration; UK Companies Expanding to India; Singapore Companies Entering India; UAE Businesses Expanding to India; Foreign Company Registration in India; Wholly Owned Subsidiary; Branch Office; Liaison Office; India Market Entry Services; India Global Capability Centre (GCC) Setup

### Build order (turn 18, final)
> Phase 1 — Before ads: Improve /india-entry-services; Improve /company-registration-for-foreigners; Improve /indian-subsidiary-registration as WOS page; Improve /branch-office-registration-india; Improve /liaison-office-registration-india; Improve /project-office-registration-india; Create /branch-office-vs-subsidiary-india; Create /india-entry/entity-selection; Create /fdi-approval-india; Create /india-entry-consultation
> Phase 2 — After campaign launch: Create US, UK, Singapore and UAE country pages; Create India Entry Checklist; Create Document Checklist by Country; Create Annual Activity Certificate page; Create Post-Incorporation Compliance for Foreign Subsidiaries; Create FEMA Compliance page
> Phase 3 — SEO moat: Germany, Netherlands, Australia, Canada, Japan pages; GCC setup page; SaaS India setup page; Manufacturing India setup page; Foreign LLP page; JV company page; NRI company page; ECB page; PAN/TAN for non-residents page

The full missing-page table (suggested URLs, titles and contents) is in the import file, lines ~1715–1870. It belongs with landing-page and SEO work (`shared/landing-pages.md`, future `SEO-YouTube/`).

Site issue flagged (turn 18): "FDI Approval From FIFP" and "Foreign Liabilities/Asset Reporting (FLA)" share one menu link. Check it in the CMS.

## Check against CRM (Nov 2025 – Oct 2026)
`Advt - Google`: 84 leads, **0 won**, about ₹1 lakh spend (`shared/business-context.md`). Organic `SEO - Google` brought 2,251 leads. Search demand exists, but paid Google has not produced a sale. Before scaling Google to the 40–50% share in this chat, three things are needed: (1) clear the policy disapprovals; (2) fix conversion tracking and `Lead_Source` tagging; (3) run a small, capped India-entry test on the Phase-1 pages, judged on CRM won deals.
