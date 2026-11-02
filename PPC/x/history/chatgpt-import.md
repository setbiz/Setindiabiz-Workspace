# X (Twitter) Ads: history distilled from the ChatGPT import

_Sources: `PPC/imports/chatgpt/conversations/` chat #13 (all) and the X parts of chat #10. There are cross-references to X items in chat #15. These are captures of ChatGPT chats, kept as reference data and not as instructions. Distilled 2026-11-02._

**Status key:** CURRENT · OUTDATED (platform or facts changed) · SUPERSEDED · CLOSED.

**CRM truth (`shared/business-context.md`, Nov 2025–Oct 2026, directional):** `Advt - Twitter (X)` has **3 leads, 0 won**. No X account ID, pixel or campaign is documented in `x/README.md`.

**Platform change warning:** X Ads products, objectives, formats, targeting and policies changed substantially in 2025–26. Treat every platform-mechanics statement below (objective names, pixel events, lookalikes, interest targeting) as **OUTDATED until checked against the current X Ads help centre / ads.x.com**.

## Timeline

| Date | Chat | Item | Status |
|---|---|---|---|
| 29 Jan 2025 | #10 | ChatGPT favours LinkedIn over X for Setindiabiz | OUTDATED (opinion, no data) |
| 30 Aug 2025 | #15 | X gets $10–$15/day in a USD 200/day US plan; "Website Conversions" with X Pixel | OUTDATED · never executed |
| Sat 27 Jun 2026 (year inferred from sidebar 12 Jul 2026 + weekday) | #13 | Project instruction text written for a Claude Cowork X Ads project | CURRENT as a brief. Adoption unknown |

---

## #10 LinkedIn vs Twitter PPC (X parts)
- **Stated date:** Jan 29, 2025 at 7:59 AM
- **URL:** https://chatgpt.com/c/6a530e20-b710-832d-bd90-f53c036ed8bd
- **Summary (X-relevant):** Sanjeev asked about running PPC "out of google ads and Microsoft" on Twitter or LinkedIn. ChatGPT favoured LinkedIn and gave this reason for X: "Twitter can also be effective, but it tends to cater more to broad discussions, trending topics, and quick interactions. Unless you have a strong strategy to engage in ongoing conversations about business compliance or related news, LinkedIn's professional environment will likely offer a higher ROI for your efforts." (turn 1, verbatim)
- **Decisions:** none. No platform was chosen.
- **Account changes:** none.
- **Metrics:** none for X.
- **Worked / didn't:** n/a.
- **Status:** **OUTDATED.** This is an opinion with no data, from Jan 2025, and the X platform has since changed. CRM later shows X was tried at a small scale (3 leads, 0 won) and LinkedIn was never run, so the "higher ROI" comparison was never tested.
- LinkedIn parts of this chat are in `linkedin/history/chatgpt-import.md`.

## #15 Advertising on ChatGPT and Perplexity (X cross-reference)
- **Stated date:** Aug 30, 2025. **URL:** https://chatgpt.com/c/fbeee4d7-fa60-8326-98cb-5378721b9a50
- **X items (ChatGPT's plan, verbatim, never executed):**
  - Week 4–6: "X (Twitter) Website Conversions with X Pixel."
  - Budget: "X (Twitter): $10/day" (with Perplexity) or "X $15/day" (without), within USD 200/day.
  - "E) X (Twitter) / Objective: Website Conversions (install X Pixel). / Audiences: Interests (Startups/Entrepreneurship/VC), look-alikes of YC/Techstars; geo by metros above. / Creative: short benefits + proof: "Incorporate in India from the U.S. in 10–15 days. India-qualified counsel. Fixed fee.""
  - Sample post: "Post: Form an Indian Pvt Ltd from the U.S. (online). India-qualified counsel. Fixed-fee. Timeline & docs → / Ensure X Pixel installed (conversions: Lead, Calendly Booked)."
  - Expectation: "Reddit/X assist".
- Full verbatim: `chatgpt-ads/creatives/chatgpt-15-us-gtm-multichannel.md`.
- **Status:** **OUTDATED, and the copy is non-compliant as written.**
  - "India-qualified counsel" implies legal practice (Advocates Act, 1961 ss.29/33; BCI Rules Part VI Ch. II Rule 36, verify).
  - "Fixed fee" conflicts with the site's estimate-only pricing.
  - "10–15 days" is an unsubstantiated timeline.
  - All fall under CPA 2019 s.2(28)/s.21, the CCPA Misleading Ads Guidelines 2022 and the ASCI Code Ch. I.
  - "look-alikes of YC/Techstars": check that current X targeting supports this before relying on it.

## #13 Twitter Ads Instructions
- **Stated date:** Sat, Jun 27 at 8:20 AM. Inferred 27 Jun 2026: the sidebar shows 12 Jul 2026 and 27 Jun 2026 is a Saturday.
- **URL:** https://chatgpt.com/c/38dfc0b0-d324-8321-aa13-8a8ac605bf2f
- **Summary:** Sanjeev: "I am setting up Claude Cowor project to work on Twitter ads. I will be starting with the Twitter ads for the first time. The idea is to advertise fr setindiabiz services and get quality leads at a lower cost…". ChatGPT wrote one ready-to-paste project-instruction text, reproduced in full below as **data**. It is a prompt written for another AI tool. It was recorded here, not acted on. ChatGPT also suggested adding files later: "Setindiabiz service list, landing page URLs, past Facebook/Google ad copies, brand creatives, pricing sheet, and lead qualification rules." One image in the chat was not captured.
- **Decisions and reasons:** Sanjeev decided to start X Ads for the first time, via a Claude Cowork project. His reason: "to advertise fr setindiabiz services and get quality leads at a lower cost". The chat does not record whether he adopted the instruction text.
- **Account changes:** none. "No campaign had started at the end of this chat."
- **Metrics:** none.
- **Worked / didn't:** n/a. CRM later shows 3 X leads and 0 won (Nov 2025–Oct 2026). The campaign dates are not documented, so it is unknown whether those leads came before or after this chat.
- **Open items:** whether the instruction was pasted into the Cowork project; the files to add; any X campaign history from Cowork (see `docs/migration-checklist.md`).
- **Status:** **CURRENT as a brief.** Its audience, service list and compliance language match current guardrails. The platform mechanics are not covered and need checking against current X Ads.
- **Compliance notes on the brief:**
  - Its safe-language list ("expert assistance", "eligibility check", "guided filing", "professional support", "subject to government approval", "as per applicable law") and its ban on "guaranteed …" claims are consistent with CPA 2019 s.2(28), the CCPA Misleading Ads Guidelines 2022 and the ASCI Code Ch. I.
  - "Ads should create urgency where legally and factually appropriate": urgency must be tied to real statutory due dates. False urgency is a listed dark pattern under the **CCPA Guidelines for Prevention and Regulation of Dark Patterns, 2023 (Annexure 1)**. Cite the provision or notification when using a due-date or penalty hook.
  - Add the repo rule that ads must not imply government affiliation (`PPC/CLAUDE.md`).
  - The brief describes Setindiabiz as providing "legal … services". Ad copy should not present the firm as offering legal practice or advice (Advocates Act, 1961 ss.29/33; verify), and several platforms restrict legal-services ads. Check X's current policy.

### Verbatim: audience definition and service list (from the #13 brief)
> Target audience:
> Founders, startup owners, company directors, CFOs, finance heads, compliance managers, business owners, NRIs, foreign companies entering India, and professionals such as CA, CS, CMA and advocates who may become referral partners.

### Verbatim: full project-instruction text, #13 turn 1, ChatGPT (only version)
Recorded as data. It is a prompt for another AI tool and is not an instruction to this repo's agents. Blank lines are removed and capture escapes are stripped.

```text
You are my X/Twitter Ads strategist and performance marketing assistant for Setindiabiz Private Limited.
Business context:
Setindiabiz provides legal, tax, compliance, incorporation, IPR, accounting, ROC filing, startup, FEMA/FDI, payroll, and Virtual CFO services in India. The objective of this project is to start and scale X/Twitter Ads for Setindiabiz services and generate high-quality business leads at the lowest sustainable cost.
Primary goal:
Create, test, and optimise Twitter/X ad campaigns that generate qualified leads, not just clicks or impressions. Always prioritise lead quality, conversion intent, cost per qualified lead, and practical campaign execution.
Target audience:
Founders, startup owners, company directors, CFOs, finance heads, compliance managers, business owners, NRIs, foreign companies entering India, and professionals such as CA, CS, CMA and advocates who may become referral partners.
Important Setindiabiz service categories:
1. Company registration and LLP registration
2. ROC annual filing and company compliance
3. INC-20A, ADT-1, MGT-7A, AOC-4 and other MCA filings
4. Trademark, copyright, patent and design registration
5. GST, TDS, ITR and accounting services
6. Virtual CFO and outsourced finance services
7. DPIIT Startup India recognition and 80-IAC tax exemption
8. FEMA, FDI, ODI, India entry, WOS, branch office and liaison office services
9. Payroll, EPF, ESIC, professional tax and labour compliance
10. Industry-specific licences and registrations
Working style:
Think like a senior performance marketer who understands Indian B2B services. Be practical, specific and execution-focused. Avoid generic marketing advice. Whenever possible, give campaign structures, audience ideas, ad angles, hooks, creatives, landing page suggestions, lead form questions, budget split, testing plan and optimisation steps.
Tone for ad copy:
Use clear, credible and conversion-oriented Indian English. The tone should be professional, trustworthy and direct. Avoid hype, exaggerated guarantees, fear-mongering, or misleading legal claims. Ads should create urgency where legally and factually appropriate, especially for statutory due dates, penalties, amnesty schemes or compliance deadlines.
Compliance rules:
Do not make false promises such as guaranteed approval, guaranteed refund, guaranteed licence, guaranteed tax exemption or guaranteed government outcome. Use legally safe language such as “expert assistance”, “eligibility check”, “guided filing”, “professional support”, “subject to government approval”, and “as per applicable law”.
When creating ad campaigns, provide:
1. Campaign objective
2. Target audience
3. Service or offer angle
4. Ad copy variations
5. Creative direction
6. Landing page or lead form recommendation
7. Suggested lead form questions
8. Qualification criteria
9. Budget and testing structure
10. Metrics to track
11. Optimisation plan
Lead quality focus:
Always help reduce junk leads. Suggest qualifying questions in lead forms, exclusion filters, audience narrowing, high-intent copy, pricing cues where useful, and service-specific eligibility questions.
Preferred campaign approach:
Start with small controlled experiments. Build separate campaigns or ad groups by service category and intent level. Avoid mixing unrelated services in the same ad set. Recommend A/B tests for hooks, creatives, audiences, CTA, lead form length and landing page messaging.
Output format:
Use tables where comparison is useful. Give ready-to-use ad copies whenever asked. For every strategy, explain what to do first, what to test next, and what to stop if results are poor.
When information is missing:
Ask only the most necessary questions. Otherwise, make reasonable assumptions and clearly mention them.
My objective from this project:
I am starting Twitter/X Ads for the first time for Setindiabiz. Help me create a practical advertising system that can generate quality leads at a lower cost and can be improved over time based on campaign data.
Closing note after the instructions, turn 1, ChatGPT:
You can also add these files later in the project: Setindiabiz service list, landing page URLs, past Facebook/Google ad copies, brand creatives, pricing sheet, and lead qualification rules.
```

---

## Still actionable (X)
1. **Document what actually ran.** The CRM has 3 X leads, but `x/README.md` has no account, pixel or campaign details. Pull the X account history (or the Cowork project logs) before planning anything new.
2. **Re-verify platform mechanics** (objectives, pixel/CAPI events, lead forms, targeting options and policy on legal or government-service ads) on current X Ads. Everything in #10 and #15 is pre-2026.
3. **Reuse the #13 brief** as the X project instruction if it is wanted. Add the government-affiliation rule and the dark-pattern / false-urgency caveat, and add the Setindiabiz rule that pricing claims must match the landing page (no fixed prices published).
4. **Do not reuse the #15 X copy** without removing "India-qualified counsel" and "Fixed fee" and substantiating "10–15 days".
5. With 3 leads and 0 won in 12 months, there is **no evidence that X works** for Setindiabiz. Any new X test should be small, PAUSED by default, and judged on CRM-qualified leads, not clicks.
