# LinkedIn: Matched Audience pilot spec for company directors (ChatGPT chat #7)

- **Source:** ChatGPT chat #7 "SEO and PPC in 2025", stated date May 2, 2025. URL: https://chatgpt.com/c/6a530e37-e9c8-832d-a47f-06bd7ed3aa40
- **Import file:** `PPC/imports/chatgpt/conversations/07-seo-and-ppc-in-2025.md` (lines ~537–673 and ~725–803)
- **Question asked (Sanjeev, verbatim):** "in PPC what is your suggestion, should we start using LinkedIn as we have email and mobile number of all the directors for the companies incorporated in past six years"
- **Status:** **never run.** CRM shows 0 LinkedIn leads for Nov 2025 – Oct 2026, and `Advt - LinkedIn` does not yet exist as a Lead_Source.
- **All benchmarks below are "ChatGPT claim — unverified", dated May 2025.** The sources named in the chat (ETBrandEquity, Spiralytics, The B2B House, Storyboard18, tripledart, GrowthSalad, Digital Scholar) were not checked.

---

## Compliance and platform status

| Item | Status |
|---|---|
| "Lookalike Audiences were retired on 29 Feb 2024 … Predictive Audiences instead" | **CURRENT** as of the chat. LinkedIn retired Lookalikes in Feb 2024. Check that Predictive Audiences is still offered. |
| Matched Audience minimum of 300 matched members; location targeting mandatory | CURRENT per the chat. Verify in Campaign Manager. |
| Uploading six years of MCA director emails and phones | **Blocking:** DPDP Act 2023 ss.4–6, s.8. ChatGPT itself said: "Ensure your original opt-in covers 'third-party advertising platforms.'" These directors gave no opt-in to Setindiabiz, so the s.3(c)(ii) "publicly available" exemption needs legal review. DPDP Rules 2025 are phased to May 2027 (verify on meity.gov.in). LinkedIn's Matched Audiences terms also require lawful rights to the data. |
| "Include an unsubscribe link in every Sponsored InMail" | Sponsored InMail is now called Message Ads / Conversation Ads (renamed around 2020). LinkedIn adds its own opt-out. |
| "LinkedIn Business Manager ➜ Audiences ➜ Uploaded list" | The path is Campaign Manager › Plan › Audiences (Business Manager is a separate tool). Verify the current UI. |

---

## Verbatim spec

### Why LinkedIn (ChatGPT claims, unverified, May 2025)
> Audience density: India is LinkedIn's second-largest market; directors and CXOs are heavily represented, so match-rates on contact uploads are usually 50-65 %.
> B2B ROI evidence: In a 2025 LinkedIn study, 94 % of Indian B2B marketers said the platform drives "high" or "very high" ROI when campaigns are fuelled by first-party data.
> Intent alignment: Directors visit LinkedIn for professional advice and peer insights, making your compliance-oriented offers contextually relevant—something harder to achieve on Meta's social feeds.

### Matched Audiences prerequisites
> Upload a CSV of hashed emails (SHA-256 is handled automatically in Campaign Manager). Location targeting is mandatory and the audience must resolve to at least 300 matched members before ads can run.
> Phone numbers are accepted (E.164 format with country codes) but typically deliver 20-30 % lower match-rates than work emails; treat them as a supplemental field.

### Suggested segmentation
> Primary segment: All company directors incorporated 2023-25.
> Nurture segment: Directors from 2019-22 who never clicked an email.
> Exclusion list: Existing Setindiabiz clients (upload a separate suppression file).

### Campaign framework

| Funnel stage | Best LinkedIn ad type | Why it works | Benchmarks (ChatGPT claim — unverified, May 2025) |
|---|---|---|---|
| Top/educate | Single-image Sponsored Content with carousel follow-ups | Thumb-stopping visuals + carousel to tell the compliance story | Avg CTR ≈ 0.55 % |
| Mid/lead capture | Lead Gen Forms pre-filled with LinkedIn profile data | Removes landing-page friction; 10-15 % completion typical in India | B2B CPL global median ≈ US $98 |
| Bottom/close | Conversation Ads or Message Ads | Delivers a personalised checklist or free consultation offer directly to InMail | ≈ 50 % open rate, 12 % click-through |
| Re-engage | Website Retargeting via Insight Tag | Follows warm visitors across LinkedIn after a blog read or pricing-page visit | Needs Insight Tag on all pages |

### Cost expectations (ChatGPT claim — unverified, May 2025)
> Average CPC (global): US $5.58; expect ₹120-₹350 in India for professional-services ads.
> Average CPM (global): US $30-35; Indian CPMs run 15-20 % cheaper but still higher than Facebook.
> Cost per Lead: Global median US $98 for LinkedIn B2B; Facebook lead-gen is often a third of that, but quality differs markedly.
> Budget heuristic: Start with ₹50-75 k / month for a 30-day pilot—enough for 40-60 k impressions and ~250 targeted clicks. Allocate 60 % to Lead Gen Forms, 25 % to remarketing, 15 % to Conversation Ads.

A later turn of the same chat gives "B2B India CPL commonly falls ₹2 000-₹3 500 (US$25-40) owing to CPC US$5.5-10 and ≈10 % lead-form completion", also unverified.

### Implementation roadmap
> 1. Clean & normalise your list (distinct columns for email, country, phone with +91 prefix).
> 2. Create the audience in LinkedIn Business Manager ➜ "Audiences" ➜ "Uploaded list" ➜ wait 24 h for matching.
> 3. Add Insight Tag via GTM or Vercel head injection to enable web retargeting and offline conversion uploads.
> 4. Launch two campaigns: Lead Gen (objective: "Leads") using a compliance-calendar PDF as the hook. Message Ad (objective: "Website conversions") offering a free 15-min incorporation consult.
> 5. Set automated rules to pause ads with CPL > ₹3,000 after 50 clicks; reinvest in the top 50 % performers.
> 6. After 30 days, compare LinkedIn leads to Meta leads on SQL rate; refine creatives and scale budgets by +20 % on the better-quality source.

### Inside the ₹15,000/day split (later turn, same chat)
> LinkedIn (Matched Audiences + Predictive) ₹4 500 (30 %) — Director-level authority offers (consult calls, white-papers) — Expected CPL ₹2 500-3 000 — 1-2 leads/day
> Upload director list ➜ Matched Audience.
> Layer Job Function = 'Founder/CXO/Finance' & Company Size ≥ 10 employees to tighten spend.
> Run Lead Gen Form ads offering a free "2025 Compliance Checklist"; follow with Conversation Ads for demo bookings.
> Expand with Predictive Audience if CPL < ₹3 500 after 14 days.
> Pause … > ₹4 000 CPL (LinkedIn) after 50 clicks
> LinkedIn form-to-SQL rate ≥ 40 % → Increase LinkedIn share up to 40 %

### Decision rule (verbatim, still useful)
> Bottom line: Start LinkedIn now with a well-segmented Matched Audience pilot. Monitor cost per sales-qualified lead, not just CPL. If CPL is ≤ 2× your Meta benchmark yet converts to paying clients at ≥ 1.5× the rate, keep scaling; otherwise tighten filters or redeploy budget back to Meta and Google.

---

## Check against CRM (Nov 2025 – Oct 2026)
The rule above is the right test. The Meta benchmark it refers to is now known: Facebook revenue per lead is ₹271, lead→won is 3.7%, and break-even CPL is about ₹135 at an assumed 50% margin (`shared/business-context.md`). By the chat's own CPL claim of ₹2,500–3,500, a LinkedIn lead costs about 18–26× the break-even CPL. Domestic AOV is ₹8,750, so LinkedIn is unlikely to pay back for low-ticket domestic compliance. Reserve any pilot for high-AOV services (India-entry / WOS; see `chatgpt-16-india-entry-targeting.md`). Create `Advt - LinkedIn` in CRM before launch.
