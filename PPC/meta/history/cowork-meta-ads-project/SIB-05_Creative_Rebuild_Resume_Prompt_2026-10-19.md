# Resume prompt: SIB-05 creative rebuild and publish hand-off (19 Oct 2026, 14:42 IST)

Paste into a new session: "Continue from Meta Ads/SIB-05_Creative_Rebuild_Resume_Prompt_2026-10-19.md"

## Context
- Ask (Sanjeev): strict audience and placements so money isn't wasted on junk. Audit: `Meta Ads/Audience_Placement_Audit_2026-10-19.md`. Change log: `Meta Ads/Change_Log_2026-10-19_Audience-Placement-Strict.md` (read the Incident section first).
- Sanjeev said "yes" to rebuild S1, S2, B1, B2 in Chrome (HP laptop, Ads Manager) and stop at the publish screen. **Sanjeev clicks Publish himself.** ("if i have publish something, then select that and show me option to publish i will cliq")

## Status of the rebuild (Ads Manager editor, unpublished edits)
| Ad | ID | Status |
|---|---|---|
| S1 | 120247068431620449 (live PAUSED, live creative 1130585629367155 is EMPTY) | Rebuilt: 4:5 + 9:16, S1 text, Get quote, form v2, WhatsApp-only follow-up, enhancements off, related media + AI versions removed, AI disclosure ticked |
| S2 | 120247068431630449 | Rebuilt, 4:5 only (no S2 9:16 exists anywhere) |
| B1 | 120247068705360449 | Rebuilt: 4:5 + 9:16, B1 text |
| **B2** | 120247068705370449 | **In progress.** Done: multi-advertiser off, Messenger off, Instagram off, WhatsApp on, form v2. Was in the Image ad media picker when the session stopped; the creative is NOT saved — restart from "Set up creative" → Image ad |
| E1, E2 | 120247067863760449, 120247068331330449 | Intact (E1 has a pending modify draft: strict targeting + form v2) |

## B2 remaining steps
1. Set up creative → Image ad. Search media "SIB-05_B2". Select 4x5 (hash 42bae5474a58a69980aea4acd19c632f) first, then 9x16 (353f3468d7e2276c84ffcf6b556b9754). Next.
2. Text:
   - Primary: "A branch office lets your company carry out the activities the RBI permits for branches in India. Eligibility: generally a profit-making record over the last five financial years and net worth of at least USD 100,000. Applicants in some sectors and from some countries need prior RBI approval. We check eligibility and prepare the application."
   - Headline: "Open a branch office in India"
   - Description: "5 years' profits, USD 100,000 net worth"
   - CTA: **Get quote** (open dropdown, click the option; typing picks "Get offer").
3. Next through Image generation and Video generation without selecting anything; Enhancements: every switch off (incl. Relevant comments, brightness/contrast); Translation off; Done.
4. Expand Related media → trash it. Customize media: untick AI vertical and AI square versions; keep the uploaded 9:16; Save.
5. Tick "Ad includes media created or edited with AI" (scroll; ref clicks may fail, click by coordinate and zoom to verify).
6. Description fields sometimes don't take text: verify with JS before leaving.

## Then
1. Read back via connector (`ads_get_ad_entities`, object_state=draft and live): S1, S2, B1, B2, E1, E2 and ad sets India Entry 120247067863750449, Subsidiary 120247068431610449, Branch-Liaison 120247068705380449. Confirm: form v2 1741840353557832, text word for word (G12 build sheet §4), images, CTA GET_QUOTE, no errors; Subsidiary = 7 countries (US, AE, SG, KR, JP, AU, CA, home + recent) + SINGAPORE_UNIVERSAL / AUSTRALIA_UNIVERSAL with SG identities 629080835992237.
2. Open the publish review with **only SIB-05 campaign 120247067847480449 items selected**. Untick the TM-C1 and INC-C1 click-to-WhatsApp drafts and anything else outside SIB-05. Screenshot and stop. Do NOT click Publish / "Review and publish" / "Preview to publish".
3. After Sanjeev publishes: read back targeting, set 30-day end date (D31) with his OK, update the change log.

## Hard rules
- Never publish, never call ads_activate_entity, never move money, never enter passwords.
- **Never re-select the Page on an ad set that has ads** (wipes creatives). Do not retry targeting edits through the API on lead ad sets (error 1815089).
- One variable at a time, before/after evidence, stop-loss logged. No CRM writes, no deletes. Don't touch SalesIQ bots, LeadChain, Zoho Social, Tiya project objects.
- Ad claims must stay accurate (Companies Act 2013, LLP Act 2008, CGST Act 2017, FEMA / FDI policy).

## Findings to report to Sanjeev (not yet told in full)
- Titles can't be hard: with Instant forms + Maximise leads, detailed targeting is always a suggestion. Hard levers: countries, age 25+, languages, placements, exclusions.
- "Home only" reverts to home + recent.
- Ad-set placement exclusions are being withdrawn by Meta; long-term strictness → account-level placement controls.
- S2 has no 9:16 image.
- Funding ≈ ₹15.8k ≈ 1.3 days with SIB-05 on.
- Not approved yet: SIB-02 Copy placements, exclusion X1, X3–X5 (DPDP Act 2023 ss.5, 6, 8 check first).
