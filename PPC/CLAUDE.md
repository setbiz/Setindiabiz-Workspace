# Setindiabiz — PPC Workspace

This folder holds all paid-advertising work for **Setindiabiz's own ads** (setindiabiz.com).
Read this file at the start of every session. Then read `shared/` before giving any recommendation.

## Platforms in scope
| Folder | Platform | Tracking tag |
|---|---|---|
| `google-ads/` | Google Ads (Search, PMax, YouTube, Demand Gen) | Google tag / GA4 + Enhanced Conversions |
| `meta/` | Meta (Facebook + Instagram) | Meta Pixel + Conversions API |
| `x/` | X Ads | X Pixel |
| `linkedin/` | LinkedIn Ads | LinkedIn Insight Tag |
| `microsoft-ads/` | Microsoft Advertising (Bing) | UET tag |
| `reddit/` | Reddit Ads | Reddit Pixel + Conversions API |
| `chatgpt-ads/` | ChatGPT Ads (ads.openai.com) | Confirm what OpenAI currently supports |

## How to work in this repo
1. **Before recommending:** read `shared/business-context.md`, `shared/kpis.md`, `shared/learnings.md`, and the platform's `README.md` + latest `reports/`.
2. **After any change on a platform:** add an entry to that platform's `changelog.md` with the date, what changed, why, the expected impact, and a date to check results.
3. **Reports:** save them as `<platform>/reports/YYYY-MM-DD-<topic>.md`. Cross-platform reports go in `reports/cross-platform/`.
4. **Learnings:** when a test concludes, record the result in `shared/learnings.md`, with the platform, dates and data. This applies whether the test won or lost.
5. **Live data:** use connected tools (Meta Ads connector, Supermetrics) rather than guessing. Never make up metrics. Label estimates as estimates.
6. **Confirm before spending:** never create or activate campaigns, or raise budgets or bids, without explicit approval in the session. Default new entities to PAUSED.

## Compliance guardrails (India)
- **Personal data:** customer lists for Custom Audiences, Customer Match, Matched Audiences and CAPI uploads are personal data. **In force now:** IT Act 2000 s. 43A + SPDI Rules 2011 (r. 4 privacy policy, r. 5 collection purpose); Consumer Protection Act 2019 s. 2(47) (disclosure of personal information given in confidence; verify clause); each platform's custom-audience terms. **From ≈13 May 2027:** DPDP Act 2023 ss. 4–6, 8 under the DPDP Rules 2025 phased commencement (verify on meity.gov.in). The website form notice says details are used only to respond to the enquiry, so it does **not** cover ad targeting. No list upload without a recorded source, notice, purpose and approver. **Never commit raw lists, phone numbers or emails to this repo.**
- **Ad claims:** follow the ASCI Code for Self-Regulation of Advertising Content and the Consumer Protection Act, 2019 (s. 2(28) misleading advertisement; s. 21 CCPA powers), plus the CCPA Guidelines for Prevention of Misleading Advertisements, 2022. Don't use claims like "Govt approved", "guaranteed approval" or "lowest price" unless they can be substantiated.
- **Government-service ads:** many platforms have policies on ads for government documents and services. Check each platform's current policy before running ads for ROC/GST/Trademark filings.
- **Secrets:** API tokens and keys must never go into files. Use connectors or environment variables.

## Naming convention (all platforms)
`<Platform>_<Objective>_<Service>_<Geo>_<Audience>_<YYYYMM>`
e.g. `GADS_Search_PvtLtdReg_PanIndia_Intent_202611`, `META_Leads_GSTReg_Delhi_LAL1_202611`

## Operating model
Planning and review follow the Elephant-Goldfish Model. See `docs/egm-operating-plan.md`.
EGM artifact directory: PPC/egm/runs/<YYYY-MM-DD>-<slug>

Other live monitors on the owner's Claude account (see `imports/claude/INDEX.md`): the daily Meta lead-quality watch (Cowork, 09:40 IST), a weekly paid-channel report (Mon 09:00 IST) and the monthly LeadChain reconciliation. Before proposing a Meta change, read the latest `meta/history/cowork-meta-ads-project/Lead_Quality_Watch_Log_*.md` and this repo's `meta/changelog.md`.

## Open items
See `docs/migration-checklist.md` for moving in past Cowork and ChatGPT work.
