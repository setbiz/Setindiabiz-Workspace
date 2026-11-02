# ChatGPT import — consolidated review (2026-11-02)

37 of 39 approved chats were imported and distilled by 5 isolated agents, each reading 100% of its files. Raw captures are in `imports/chatgpt/conversations/` and the routing index in `imports/chatgpt/INDEX.md`.
Per-platform outputs: `<platform>/history/chatgpt-import*.md`, verbatim assets in `<platform>/creatives|campaigns/chatgpt-*.md`, landing pages in `shared/landing-pages-chatgpt-import.md`, strategy in `reports/cross-platform/chatgpt-import-strategy-history.md`. Lessons were merged into `shared/learnings.md`.

## Headline findings
1. **The chats contain almost no performance data.** The only real account numbers are in chat 2 (ChatGPT Ads, Oct 2026). Everything else is plans, settings or ChatGPT estimates.
2. **The plans had the channel mix backwards.** They put Google first and Meta at 20–30%. In the CRM, Meta (FB+IG) is ≈96% of ad-attributed sales and Google is 0 won.
3. **Google:** the chats don't explain the 0 sales directly. Likely causes are a policy disapproval (gov-services policy, unresolved Apr 2025 → Jun 2026), negatives that were never applied, conversions "set up later", and an India campaign built from a USA plan.
4. **Microsoft:** tracking was never verified (owner's own words, Aug 2025). Fix it before any spend.
5. **ChatGPT Ads:** live since ~Sep 2026 at ₹500/day per campaign. It optimises to "Lead Created", 0 CRM sales so far, and 5 of 6 Branch & Liaison ads are policy-blocked.
6. **Lead-source labels differ** between Meta forms and the CRM, so Meta may be under-reported.

## Compliance flags (fix before reuse; verify current versions)
| Issue | Where | Provision |
|---|---|---|
| Customer / MCA director lists uploaded as audiences or used for cold outreach without a documented lawful basis; a "collected directly from owners" declaration may be false | chats 1, 6, 8 | DPDP Act 2023 ss. 4–6, 8 (DPDP Rules 2025, phased to May 2027); TRAI TCCCPR 2018 |
| Website form notice ("used only to respond to your enquiry") doesn't cover advertising use | site + chat 1 | DPDP Act 2023 s. 5 |
| Unsubstantiated claims: "100% compliance guaranteed", "lowest price guaranteed", "India's most trusted", "10,000+/50,000+/1,00,000+", "4.8 by 10,000+", "7 days", "24/7" (office is Mon–Sat), invented prices ₹1,999 / ₹3,499 / ₹5,999 | chats 6, 9, 17, 19, 23, 27, 28 | CPA 2019 s. 2(28), s. 21, s. 89; CCPA Misleading Ads Guidelines 2022; ASCI Code ch. I |
| Disparaging CAs ("Tired of CAs…") | chat 19 | ASCI Code ch. IV |
| Implied government affiliation: MCA logo, "official Startup India recognition/badge", "Invest India advisory", "Start your application" | chats 12, 18, 20, 23, 35 | Emblems and Names Act 1950 s. 3; State Emblem Act 2005; Google gov-documents policy |
| "Attorneys / India counsel" wording | chat 15 | Advocates Act 1961 ss. 29, 33; BCI Rules r. 36 |
| GST notice representation offers | chat 38 | CGST Act 2017 s. 116 (authorised representative) |
| Wrong statutory facts: "all filings within 30 days" (INC-20A is 180 days), LLP "no upper cap" penalty, outdated angel-tax claim, 80-IAC without IMB certificate | chats 8, 19, 35 | Companies Act 2013 s. 10A; LLP Act 2008 s. 35 (verify); Income-tax Act 2025 (map s. 80-IAC) |
| False urgency, drip pricing, "save ₹" reference prices on landing pages | chats 8, 36, 37 | CCPA Dark Patterns Guidelines 2023 |
| Discriminatory targeting advice (exclude homemakers / rural users) | chat 21 | Meta discriminatory-practices policy |

## Action list (ranked)
1. **Meta (now):** use the connector to audit the live setup (budgets, rules incl. #HOLD, value rules, forms), standardise `Lead_Source`, add the WhatsApp opt-in, strip non-compliant claims.
2. **Seasonal (now):** MGT-7/7A for FY 2025-26 is due ≈29 Nov 2026 (if AGM was 30 Sep). AOC-4 and LLP Form 8 (30 Oct) just passed, so a late-filer angle is possible. Verify dates against current MCA circulars first.
3. **ChatGPT Ads:** reconcile the Oct campaigns with CRM before activating the 2 paused ads. Chase OpenAI support on Branch & Liaison. Re-check won deals in 60–90 days.
4. **Google relaunch (via `/ppc-new-campaign`):** pull the Dec-25 search terms, geo and conversion-action data. Find the policy trigger. Shared negative list. Enhanced conversions + Zoho offline import. Policy-safe copy.
5. **Microsoft:** fix and test UET + goal, mark the 2 "Active" idle campaigns properly, prune the chat 17 keyword lists.
6. **Legal review** before any customer or MCA list is used for ads or outreach.
7. **Landing pages:** pick a design from chat 42 and remove dark patterns / unsupported claims.

## Not captured (decide before deleting in ChatGPT)
- **#33** 140-series Call Pickup Ratio: not captured at all.
- **Images, files or outputs not in the capture:** #3, #4, #13, #16, #19, #20, #35 (images); #8 (5 HTML emails); #36, #37 (PDFs / mockups); #42 (master-prompt file); #1 (turns before 6).
