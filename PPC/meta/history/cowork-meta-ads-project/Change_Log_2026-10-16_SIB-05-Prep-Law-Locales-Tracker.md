# Change log: SIB-05 prep while waiting for Vipin (16 Oct 2026, about 13:55–14:00 IST)

**Read-only for Meta, Zoho CRM, Canva, Gmail and Google Sheets. Nothing was edited, sent or created in any of them.** One scheduled task was created at Sanjeev's request (below). Government PDFs were read in the built-in browser; nothing was downloaded.

## Scheduled

| Item | Detail |
|---|---|
| 16:30 IST re-check of Vipin's creatives | One-off message back into this session, trigger **trig_01L9jHjchMiRonpdWZ8gT4pa**, fires 11:00 UTC. Follows step 1 of `SIB-05_Resume_Prompt_2026-10-16_1400.md`. Drafts a reply to Vipin if anything is open; sends nothing without Sanjeev's yes. |

## 1. Language keys for G12 (D26: English + Japanese + Korean)

| Finding | Source |
|---|---|
| English keys **6 = English (US)** and **24 = English (UK)** confirmed from Meta's own docs. These are what #IND1, #IND3, SIB-02, CCFS and (since 16 Oct) SIB-04 use. | Meta Marketing API, Targeting Search › Locales (developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/targeting-search.md) |
| **Japanese and Korean keys not confirmed.** The Meta connector has no targeting-search tool, and Meta's docs page shows only English examples. Expected keys from Meta's long-standing numbering: **11 = Japanese, 12 = Korean**, unverified. | — |
| **Korean may not be selectable.** Meta's help list of audience languages, as returned by the connector, includes Japanese and Japanese (Kansai) but **no Korean**. This may be a gap in the help text, not in Ads Manager. | Meta help article "About audience language settings" (facebook.com/business/help/1024084489118213), via `ads_get_help_article` |
| Meta's guidance on the same page: ad creative and landing pages should match the languages chosen. SIB-05 creatives and form are English only. This is the trade-off D26 accepted; the day-7 check watches Japan and South Korea separately. | Same article |

**G12 plan:** build the draft ad sets with `locales` [6, 24, 11, 12]; Meta's validation and the connector read-back settle the keys. If 12 (Korean) is rejected or reads back as another language, stop and ask Sanjeev before building without it.

## 2. Land-border law: government copies opened (closes the parked item)

| Instrument | Government copy | What it says (relevant to SIB-05) |
|---|---|---|
| **Press Note No. 2 (2026 Series)**, DPIIT F. No. 5(5)/2020-FDI Policy (Pt-1), **dated 15.03.2026** (not 10 Mar as the secondary sources said), signed Jai Prakash Shivahare, JS. Effective from the date of the FEMA notification. | dpiit.gov.in/static/uploads/2026/03/b9da5830b052c2f2d788593e97d07c63.pdf | Rewrites para 3.1.1 of the FDI Policy. See the reading below. |
| **S.O. 2174(E)**, 1 May 2026, MoF (DEA), FEMA (NDI) (Amendment) Rules, 2026; F. No. 1/4/2026-EM; Gazette Extraordinary No. 2093, published **2 May 2026** (CG-DL-E-02052026-272196) | egazette.gov.in/WriteReadData/2026/272196.pdf | Substitutes rule 6(a) of the NDI Rules, 2019 with the PN2 text, as a proviso and Explanations 1–3. |
| **S.O. 2186(E)**, 2 May 2026, NDI (Second Amendment) Rules, 2026 (CG-DL-E-02052026-272206) | egazette.gov.in/WriteReadData/2026/272206.pdf | Insurance sector entry F.8 (100% automatic for Indian insurance companies, with conditions). **No land-border change.** New to our file. |
| **S.O. 3030(E)**, 12 Jun 2026, NDI (Third Amendment) Rules, 2026; F. No. 1/11/2025-EM; Gazette No. 2924 (CG-DL-E-12062026-273406) | egazette.gov.in/WriteReadData/2026/273406.pdf | Individual persons resident outside India in **listed** companies. The land-border proviso is in **both rule 12(1) and rule 13(1)** (confirmed in the gazette; one secondary source said rule 12 only). Spec §1 is right. |
| **S.O. 4870(E)**, 2 Sep 2026, NDI (Fourth Amendment) Rules, 2026 | **No gazette copy found.** Secondary sources agree (TaxTMI, TeamLease, LexComply, TaxUpdate) | Schedule I entry 15.2.5: inventory-based e-commerce for exports only. No land-border change. |

**Reading of the official text (PN2 para 3.1.1 / new rule 6(a)):**
- An **entity or citizen of a land-border country**, or an investment whose **beneficial owner is a citizen of such a country**, invests **only under the Government route**. Pakistan: Government route, and not in defence, space, atomic energy or prohibited sectors.
- "Beneficial owner" is tested at the level of the **investor entity incorporated outside a land-border country**, using rule 9(3) of the PML (Maintenance of Records) Rules, 2005. Beneficial ownership is treated as vested in a land-border country if land-border citizens or entities, directly or indirectly, hold rights (i) above the rule 9(3) thresholds over that investor entity, or (ii) that give control of the investor entity, or (iii) that give ultimate effective control of the Indian investee.
- An investor entity with **any** land-border ownership that does not need approval must still report in the format of the DPIIT SOP.
- The rule 9(3) threshold for a company is **10%** since the 2023 amendment to the PML Rules (secondary: Fox Mandal, LiveLaw; government copy not opened).

**Correction to our docs.** Spec §1 and claims review §2 say PN2 "lets a land-border investor take up to 10% without control on the automatic route". The official text is narrower: a land-border entity or citizen investing **directly** still needs Government approval at any percentage. The 10% / no-control relief applies to land-border owners **of a non-land-border investor entity** (for example a Singapore parent with a small Chinese shareholder), which then goes automatic with SOP reporting.
- **No ad change needed.** The approved S1 line "Investors from countries sharing a land border with India follow separate rules" stays accurate.
- **Handler briefing:** the FDI team's first-call land-border screen (spec §1, D10) should follow the official reading above.
- The spec and claims review text are **not edited yet**; this log supersedes those two rows.

## 3. Swati's tracker (SIB-04 follow-up investigation, due 15 Oct)

Sheet "SIB-04 Lead Follow-up Investigation - 13 Oct 2026" (1zEdc9Ey6vxMH7d1cUssW7yj8DOxH5SeEg9ZDKzNnSRw), read 13:55 IST.

**Swati has not filled any row.** Columns R–V (explanation, root cause, action, "CRM updated?", spoken on) are blank on all 28 rows; Agent Summary shows 0 rows covered. So there are no agent root causes to roll up, and every row is effectively "CRM updated? = blank".

**Roll-up by the 13 Oct issue type instead** (our classification, not the agents' explanations):

| Bucket | Issue types | Rows |
|---|---|---|
| Sales-process | Follow-up gap / slow first contact (9), no contact logged (4), worked but CRM not updated (3), fresh-lead SLA (2), invalid number not closed (1), closed as mistake, check (1) | **20** |
| Natural attrition | Good effort, unreachable, close per rule | **5** |
| Qualification / spam | Spam not closed (2), marked spam, check (1) | **3** |

**Where the 28 leads stand in CRM now (COQL, 13:55 IST):**

| State | Count | Leads |
|---|---|---|
| Valid Lead | 3 | …553288 (Valid - RM Working), …574748, …586161 (both with RM quality blank) |
| Lost | 5 | …561146 Other CA; …554044 Bot Created/Spam; …567156 Inquired by Mistake; …586197 Avoiding Call; …494612 Avoiding Call |
| Still Establishing Contact | 18 | incl. …575496 on Lost Records; 5 with RM quality blank (…538212, …549264, …463322, …488294, …586836) |
| Status blank (Lost Records) | 2 | …463283, …538530 |

**Closures that contradict the 13 Oct evidence** (worth a look; not changed):
- …554044 closed **Bot Created/Spam**: the customer shared files in the chat three times.
- …567156 closed **Inquired by Mistake**: had asked for AOC-4 and MGT-7.
- …586197 closed **Avoiding Call**: had asked to be messaged on WhatsApp.
- …494612 closed **Avoiding Call**: "wants to file before late fees".

"Bot Created/Spam" and "Inquired by Mistake" count as **junk** in the SIB-04 stop-loss. Mislabelled sales-process losses raise junk% and make targeting look worse than it is.

**Not touched since 13 Oct:** …564159 (invalid number, still open, last modified 11 Oct), …586137 and …586836 (Priyam), …549264 (worked, CRM still not updated).

**Owners have moved** on most rows since 13 Oct (Amit Kumar 3's and Gaurav's leads now with Sudip Manna, Shivam Chauhan, Aman Raj, Shubham Kumar, "Das" …838091001 and others; Sudip's form leads with "Jain" …804800001).

## 4. Gaurav Pandey's 3 SIB-04 leads (parked item)

| Lead | Owner now | Status |
|---|---|---|
| …946345169 | "Singh" …796765001 (not in the owner map) | Establishing Contact / Invalid - Bot/Job/Irrelevant |
| …946520407 | Pragya Agrawal | Valid Lead / Still Evaluating |
| **…946590157** | **still Gaurav Pandey (user disabled 13 Oct)** | **Valid Lead** / Still Evaluating |

One valid lead still sits on a disabled user.
