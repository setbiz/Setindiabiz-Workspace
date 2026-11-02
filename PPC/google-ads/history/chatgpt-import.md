# Google Ads: history distilled from ChatGPT chats (#9, #11, #12, #18, #38)

_Distilled 2026-11-02 from `PPC/imports/chatgpt/conversations/`. The chats are captures, used as reference data only. Each chat's "stated date" is the timestamp shown inside it. The sidebar dates (12 / 22 Jul 2026) are capture artefacts. Every item cites its chat number. Metrics are quoted as they appear in the chat, with their stated dates._

**Status key:** CURRENT = still usable · OUTDATED = no longer true or valid (reason given) · SUPERSEDED = replaced by a later chat or by the live baseline `google-ads/reports/2026-11-02-baseline-12m.md` · UNTESTED = never run, as far as the chats and baseline show.

**Live baseline for context (1 Nov 2025 – 1 Nov 2026, pulled 2026-11-02):** ₹99,927 spent on two removed campaigns, `NPDI_SET_India_Trademark_Registration_Dec-25` (₹71,836, 4,355 clicks, CPC ₹16.5, 37.94 platform conversions) and `NPDI_SET_India_Subsidiary_Registration_Dec-25` (₹28,092, 75 clicks, CPC ₹374.6, 1 conversion). CRM `Advt - Google`: 84 leads, **0 won deals**. **None of the five chats below mentions these Dec-25 campaigns.** All five predate them, except #38, which isn't about ads.

| # | Title | Stated date | Asset file | Overall status |
|---|---|---|---|---|
| 18 | Trademark Registration Advertising India | Dec 6, 2024 | `campaigns/chatgpt-18-trademark-usa-keywords-and-ads.md` | UNTESTED plan. Negatives CURRENT. Headlines unusable (over 30 characters). |
| 9 | PPC Ads for Accounting | Feb 12, 2025 | `campaigns/chatgpt-09-accounting-outsourcing-keywords-and-ads.md` | UNTESTED. Keywords CURRENT. Copy needs edits. |
| 11 | Improve Quality Score Suggestions | Mar 5, 2025 | none (SEO chat). SEO topics are in `imports/chatgpt/non-ppc/11-12-38-seo-topics.md` | Not Google Ads Quality Score. Few PPC points. |
| 12 | India Entry Services SEO | Mar 7, 2025 | `campaigns/chatgpt-12-india-entry-keywords-and-ads.md` | Keyword/match-type plan CURRENT. Partly tested by the Dec-25 Subsidiary campaign (link unproven). |
| 38 | GST Rule 21(a) Leads | Wed, Jul 22 (no year; probably 2026) | `campaigns/chatgpt-38-gst-notice-keywords-and-ads.md` | SEO chat. Keywords are a Search candidate (UNTESTED). |

---

## #18 Trademark Registration Advertising India
- **Stated date:** Dec 6, 2024 at 5:05 PM (turn 1), Dec 6, 2024 at 6:46 PM (turn 5) · **URL:** https://chatgpt.com/c/6a530e16-e0ac-832d-a3e9-2ef1d03453ce
- **Summary:** Sanjeev asked how to advertise trademark-registration-in-India services to foreign countries. ChatGPT gave general channels, a country list (US, UK, China, Germany, Japan, Singapore, UAE, South Korea, Australia, Canada, Israel, France, Netherlands, Switzerland, Italy, Spain, Vietnam, Thailand) and a 10-country strategy. Sanjeev then asked for a **USA Google Ads strategy "considering that the ad does not violate government document policy of google ads"**. ChatGPT gave compliant copy, keywords, negatives, targeting, a landing page, bidding, extensions, a compliance checklist and a step-by-step build guide.
- **Decisions and reasons:** advertise trademark registration to foreign countries (turn 1, no reason). Accepted the country-wise strategy (turn 3, no reason). **USA first, Google Ads first, on condition of compliance with Google's government-document policy** (turn 4; the policy is the stated constraint, and no reason is given for choosing the USA). Asked for a build guide (turn 5). **Not decided:** budget, bid strategy, keywords, ad copy.
- **Account changes:** none (Dec 6, 2024). Nothing shows the campaign was built.
- **Metrics:** "From Sanjeev: none in this chat." ChatGPT's recommendations only: "Daily budget: $50–$100/day initially (turns 4 and 5)." "Audience age: 25–55 (turn 4)." "Responsive ad limits: up to 15 headline variations and up to 4 description variations (turn 5)."
- **Worked / didn't:** no test, so there are no results. Reviewer check (2026-11-02): **all 8 headlines are over 30 characters** (32–52), and 1 of 7 descriptions is over 90 (106).
- **Open items (from chat):** US landing page; conversion tracking for forms and calls; a US phone number "if available"; replace the sample display URL `www.yourdomain.com/trademark-india`; the other 9 countries weren't developed.
- **Status:** plan **UNTESTED**. Negatives **CURRENT**. "Configure conversions later" and Enhanced CPC **OUTDATED / SUPERSEDED** (baseline lesson 3; Google retired ECPC for Search in 2025, verify). Copy **unusable as-is**.

## #9 PPC Ads for Accounting
- **Stated date:** Feb 12, 2025 at 8:04 AM · **URL:** https://chatgpt.com/c/6a530e26-125c-832d-9d04-bcc98464b157
- **Summary:** scope of Google PPC for accounting outsourcing. ChatGPT said it's significant (high intent, targeting, formats, budget control). It drafted "What makes your products or services unique?" (generic, then a final version based on `/accounting-process-outsourcing`), a 10-keyword priority list and four ad variations with tips.
- **Decisions and reasons:** accepted the high-intent phrases (turn 4: "I like the keywords suggested"). The reason, from the passage he quoted: "These queries indicate that the searcher is already considering a solution, which can lead to higher conversion rates." Pointed the uniqueness text at the APO page (turn 3, no reason). **Not chosen:** which draft, which keywords or which ad.
- **Account changes:** none (Feb 12, 2025). The baseline has no accounting campaign.
- **Metrics:** none in this chat.
- **Worked / didn't:** untested. Reviewer check: 3 of 12 headlines are over 30 characters, and all 4 descriptions are over 90 (91–115).
- **Open items (from chat):** test long-tail terms ("best virtual accounting services", "cost-effective accounting outsourcing"); run several ad variations; add sitelinks, callouts and snippets; keyword and competitor research. Claims such as "24/7 Support" weren't confirmed.
- **Status:** keywords **CURRENT (candidate)**. Ads **need edits**. "Search & Display" **OUTDATED** for a measurement-first relaunch. "24/7 Support" **do not use** (hours are Mon–Sat 9:30–18:30).

## #11 Improve Quality Score Suggestions (mostly SEO)
- **Stated date:** Mar 5, 2025 at 8:27 AM (turn 1); Mar 5, 2025 at 2:48 PM (turn 9). Data periods mentioned: Dec 2024 (SimilarWeb), Feb 2025 and Jan (IndiaFilings visits). · **URL:** https://chatgpt.com/c/6a530e2a-f2f0-832d-9bf3-00ea3c5e8e68
- **Summary:** the "quality score around 32" vs IndiaFilings "exceeding 75" is **a site authority-type SEO score, not Google Ads Quality Score**. The chat doesn't name the tool. Sanjeev said only "I have access to semrush report", and ChatGPT's figures cite a SEMrush Authority Score of ~71 for IndiaFilings. The rest is SEO: backlink job description and KPIs, 100 infographic topics, AI vs designed infographics, the Pvt Ltd infographic spec, and the Startup Cost Calculator URL and meta. SEO topics are listed in the non-ppc file, not copied.
- **Decisions and reasons (all SEO):** focus on backlinks and hire for it (turn 3; the reason in the pasted report was "a major factor in lower authority and rankings"). Set the infographic scope (turn 5). Start with the Pvt Ltd guide infographic (turn 7). Use `/startup-cost-calculator` (turn 10; ChatGPT's reason: "clear, concise, includes … SEO-friendly keyword … matches search intent"). Include "cost of company or llp registration in india" in the meta (turn 11).
- **Account changes:** none.
- **Metrics (verbatim, as dated in the chat):**
- Sanjeev's statements, turn 1
- setindiabiz.com quality score: around 32
- indiafiling.com score: exceeding 75
- The chat does not state which tool these scores came from. Sanjeev's only comment is "I have access to semrush report" (turn 2).
- ChatGPT's research quoting third-party sources, turn 2. These are not Sanjeev's data. The source chip shown in the chat is in brackets.
- Setindiabiz.com Moz Domain Authority: around 49/100 (setindiabiz.com.usitestat.com)
- IndiaFilings.com SEMrush Authority Score: \~71 (semrush.com)
- IndiaFilings.com referring domains: \~9.7K (semrush.com)
- IndiaFilings.com total backlinks: 289K (semrush.com)
- IndiaFilings.com traffic: around 2.9 million visits/month, SEMrush estimate (semrush.com)
- IndiaFilings.com traffic rank in India: \~#1611 (semrush.com)
- IndiaFilings.com search visits: 1.9M in Feb 2025, up by 99K from Jan (ahrefs.com)
- IndiaFilings.com share of traffic from India: \~98% (ahrefs.com)
- IndiaFilings.com organic keywords: over 526K, according to Ahrefs (ahrefs.com)
- IndiaFilings.com keyword "domicile certificate": #1 in Google India, \~19,000 monthly visits (ahrefs.com)
- IndiaFilings.com category rank: #8 in the "Business Services" category in India (similarweb.com)
- Setindiabiz.com total visits: \~51.8K in Dec 2024, SimilarWeb (no chip)
- Setindiabiz.com traffic growth: +22% MoM in a recent month (no chip)
- Setindiabiz.com bounce rate: \~5%, SimilarWeb, Dec 2024 (no chip)
- Setindiabiz.com pages/visit: 1.57, SimilarWeb, Dec 2024 (no chip)
- Setindiabiz.com homepage Google PageSpeed score: 89/100 (setindiabiz.com.usitestat.com)
- IndiaFilings.com PageSpeed score: "isn’t publicly known here"
- ChatGPT's own estimates with no source, turn 2
- Setindiabiz.com referring domains: "likely only a few hundred domains"
- Setindiabiz.com ranking keywords: "likely only a few thousand keywords"
- Setindiabiz.com traffic: "only in the tens of thousands per month"

- **PPC-relevant content (verbatim):**
- What specific quality score are you referring to? (Google Ads, SEO-related metrics like Moz DA/PA, Core Web Vitals, or another specific tool?)
- Are you looking for SEO improvements, PPC (Google Ads) optimization, or overall site quality enhancements?
- PPC content, paid search note, turn 2, ChatGPT
- Paid Search: (Not specifically asked, but worth noting) IndiaFilings likely also invests in Google Ads for some keywords. If Setindiabiz is not doing so, IndiaFilings could be capturing even more visibility through paid ads, making it harder for Setindiabiz to get noticed.

- Match User Intent: For each target keyword, ensure the content type matches what users want. For example, if users search “LLP vs Pvt Ltd”, they likely want a comparison – provide a clear comparison article. If they search “register company online India”, they might be looking for a service – ensure your landing page addresses that with a strong call-to-action.

- Setindiabiz.com homepage Google PageSpeed score: 89/100 (setindiabiz.com.usitestat.com)

- **What this means for Google Ads (reviewer reading, not in the chat):** (1) **There is no Google Ads Quality Score data in any chat.** Pull keyword-level QS (expected CTR, ad relevance, landing-page experience) from the account before the relaunch. (2) The search-intent point ("LLP vs Pvt Ltd" = comparison, "register company online India" = service) is the same split the Microsoft keyword lists in chat #17 ignore. (3) The final Startup Cost Calculator meta ("Startup Cost Calculator – Company & LLP Registration Cost") makes that page a possible landing page for "company registration fees/cost" keywords, a cost query that can be answered without publishing a fixed price. Check the page exists.
- **Worked / didn't:** not measured in the chat. Homepage PageSpeed 89/100 (source chip usitestat, date not stated).
- **Open items (from chat):** calculator content-structure plan not taken up; the meta isn't confirmed; only 1 of 100 infographics developed; CTA placeholders `[Your Contact Number]` / `[Your Website Link]`; backlink KPIs need a baseline and a DA threshold.
- **Status:** PPC note "IndiaFilings likely also invests in Google Ads" is **speculation** (no evidence in the chat). SEO figures dated Dec 2024 / Feb 2025 are **OUTDATED** as current benchmarks: re-pull them.

## #12 India Entry Services SEO (mixed: PPC keyword strategy extracted)
- **Stated date:** Mar 7, 2025 at 7:47 AM · **URL:** https://chatgpt.com/c/6a530e2b-c528-832d-8e6f-96ae0368515e
- **Summary:** turns 1–2 are SEO (page keywords, improvements, 15 FAQs). Turn 3 is PPC: "what should be the keywords on which I should run a PPC Campaign on google and which countries to target. My objective would be to seek qualified leads only". ChatGPT gave primary, secondary and competitor keywords, three country tiers, phrase/exact match, landing-page CTAs, a qualifying form, audiences and conversion definitions.
- **Decisions and reasons:** objective **"qualified leads only"** (Sanjeev, turn 3). No keyword or country choice is recorded.
- **Account changes:** none (Mar 7, 2025).
- **Metrics:** none in this chat. Later live data on the theme (baseline, Nov 2025 – Nov 2026): Google Subsidiary 75 clicks, ₹28,092, CPC ₹374.6, 1 platform conversion. Microsoft "2026 - Overseas - India Entry Services" 109 clicks, ₹4,607, CPC ₹42.3, 0 conversions.
- **Worked / didn't:** no evidence links this keyword list to the Dec-25 Subsidiary campaign.
- **Open items:** none stated by Sanjeev. ChatGPT's recommendations (qualifying form, phrase/exact) aren't recorded as implemented.
- **Status:** match-type rule and qualifying form **CURRENT**. "Business visa India" **drop** (off-service; Google government-documents policy). "Invest India advisory" **drop or never echo** (implied government affiliation). Conversion definition = form/call **SUPERSEDED** by offline conversion import (baseline lesson 3).

## #38 GST Rule 21(a) Leads (mixed: keywords and landing page)
- **Stated date:** Wed, Jul 22 at 6:11 PM. **No year is shown.** The sidebar is 22 Jul 2026, and 22 Jul 2026 is a Wednesday, so probably 2026 (inference). · **URL:** https://chatgpt.com/c/6a60ba80-b188-83ee-8d79-578487b5e697
- **Summary:** Sanjeev uploaded a sample Rule 21(a) notice and asked for lead-generating content. ChatGPT proposed a funnel (landing page, FAQ, emergency checklist, downloadable reply checklist, contact form, blogs) and 12 high-intent keywords. In turn 2, a master table of ~30 GST notices with fee bands and timelines, a size-based fee multiplier, and a 15-page priority list. **No ad platform is discussed.**
- **Decisions and reasons:** turn 2, "well then i will create services pages like that of GST Registration", following ChatGPT's "service hub rather than just a blog" recommendation. Table requested "to create unique service pages".
- **Account changes:** none.
- **Metrics:** none (fee bands are ChatGPT's "indicative internal pricing bands", not data).
- **Open items:** service pages not recorded as built. Legal accuracy of the notice table unverified (see the non-ppc file).
- **Status:** keywords **CANDIDATE for a Google Search test (UNTESTED)** once a dedicated landing page is live. Fees **internal only**.

---

## Cross-check: why did the Dec-25 Google Trademark campaign get 0 won deals?
**Direct evidence in the chats: none.** No chat mentions `NPDI_SET_India_Trademark_Registration_Dec-25`, its geo, keywords, match types, landing page or conversion action.

**Indirect evidence, all from chat #18 (Dec 6, 2024, a year before the campaign):**
1. **Keyword intent.** Chat #18 named the junk-query classes to exclude: "free," "DIY," "Indian government site," and "online trademark search". These match what the baseline suspects (₹16.5 CPC and 11.8% CTR fit cheap, informational clicks). Nothing shows these negatives were applied. → Pull the Dec-25 search-terms report to confirm.
2. **Geo and audience mismatch is possible.** Chat #18's plan was a **USA, foreign-applicant** campaign. The Dec-25 campaign is named **"India"**. If it targeted Indian searchers, it ran without any documented plan from the chats. Indian DIY applicants can file on the official portal themselves, which is a known low-intent pool (reviewer note).
3. **Conversion action.** Chat #18's build guide says "If not set up yet, you can proceed and configure conversions later" and "Choose Maximize Conversions or Manual CPC". That combination is a route to bidding on an undefined or loose conversion. The baseline shows 37.94 platform conversions against 84 CRM leads and 0 won, consistent with a conversion that doesn't represent a qualified lead. **There is no evidence of what was actually configured.**
4. **Landing page.** The only trademark landing-page plan in the chats is a **US-audience** page (chat #18 step 5), and it isn't recorded as built. No chat reviews `/trademark-registration` for Indian searchers.
5. **Match types.** Chat #18 gives no match types. Chat #12 (Mar 2025) recommends phrase/exact, but for India entry, not trademark.

**Subsidiary (₹374.6 CPC):** chat #12 supplied the likely keyword universe and the qualifying-form idea. No chat estimated CPCs or capped budget, and no chat links to the Dec-25 build.

## Compliance flags across these chats (verify current versions of every rule cited)
| Chat | Claim / item | Issue | Provision |
|---|---|---|---|
| 9 | "24/7 Support" | False against stated office hours | Consumer Protection Act, 2019 s.2(28); CCPA Misleading Ads Guidelines 2022; ASCI Code Ch. I |
| 9 | "highest standards of data security", "Uncompromised … Compliance" | Unsubstantiated superlatives | Same as above; DPDP Act, 2023 s.8 if claimed |
| 12 | Keyword "Business visa India" | Visa service: off-service and government-document service | Google Ads Government documents and official services policy |
| 12 | Keyword "Invest India advisory" | Implies a link to the GoI investment agency | Emblems and Names (Prevention of Improper Use) Act, 1950 s.3; Google misrepresentation policy |
| 12 | Competitor names TMF, Vistra | Keyword OK, not in ad text | Google trademark policy |
| 18 | "Start Your Application", "100% Compliance", "Trusted … for US Companies" | Implies filing authority / guarantee / unproven US base | CPA 2019 s.2(28), s.21 (CCPA powers); CCPA Guidelines 2022; ASCI Ch. I |
| 18 | Trademark filing ads to USA | Official service | Google Government documents and official services policy (check certification) |
| 18 | U.S. office / phone | Don't imply a US presence that doesn't exist | CPA 2019 s.2(28) |
| 38 | "represent … before GST Authorities", hearing attendance | Only s.116 authorised representatives may appear | CGST Act, 2017 s.116 |
| 38 | "Can GST registration be restored? Yes.", "Fast Turnaround" | Outcome and speed claims | CPA 2019 s.2(28); CCPA Guidelines 2022; ASCI Ch. I |
| 38 | "only 7 Working Days" | True only per r.22(1); urgency must be accurate | CGST Rules, 2017 r.22(1); CCPA Dark Patterns Guidelines, 2023 |
| 38 | Lead magnet collecting GSTIN, mobile | Personal data | DPDP Act, 2023 ss.5–6; DPDP Rules, 2025 (phased) |
| 11 | Infographic icon "A certificate with a government seal" | Don't depict the State Emblem or an official seal | State Emblem of India (Prohibition of Improper Use) Act, 2005; Emblems and Names Act, 1950 s.3 |
| 11 | Example About-page wording "20+ years experience, helped 10,000+ startups" | Number conflicts with the site's "18K+ clients"; both need evidence | CPA 2019 s.2(28); ASCI Ch. I |

---

## Still actionable (for the planned Google relaunch)
1. **Before anything else:** pull the Dec-25 Trademark and Subsidiary **search-terms, geo and conversion-action** reports. The chats can't explain the 0 won deals (see the cross-check above).
2. **Seed the negative list** from chat #18 ("free", "DIY", "Indian government site", "online trademark search"), plus chat #28 (Free, DIY, Templates, Internship) and chat #17 ("free company registration", "jobs in company registration").
3. **Measurement first:** don't follow chat #18's "configure conversions later". Set up enhanced conversions plus offline conversion import from Zoho (baseline lesson 3) before using Maximize Conversions.
4. **Decide the trademark market:** India-domestic or foreign (USA plan, chat #18). If USA: build the US landing page and rewrite all 8 headlines to 30 characters or fewer.
5. **India entry / subsidiary:** phrase/exact only. Add the qualifying form (country, nature of business, proposed structure, investment size; chat #12). Cap the budget given the ₹374.6 CPC. Drop "Business visa India" and "Invest India advisory".
6. **New-line tests:** accounting outsourcing (chat #9; fix 7 over-length lines, remove "24/7 Support") and GST notice response (chat #38; landing page first, legal check, s.116 wording, no fees in ads).
7. **Pull actual Quality Score** components. None exist in the chats (chat #11 was an SEO score).
8. **Check that `/startup-cost-calculator` exists** and consider it as the landing page for "company registration fees/cost" queries (chat #11 meta; chat #17 has "company registration fees" keywords).
9. **Substantiate or strip claims** everywhere: 10,000+ / 18K+, 7 days, 100% compliance, lowest price, 24/7 (see `business-context.md` claims table).
