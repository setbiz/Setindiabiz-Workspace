# TM + INC WhatsApp-ad build: spec and decisions (15 Oct 2026, updated ~15:55 IST)

Follows `Change_Log_2026-10-15_IND1-Relaunch-SIB-02-Draft.md` and `Change_Log_2026-10-15_W6-Deployed.md`. This is the "then continue" part of Sanjeev's 13:06 request: optimise Incorporation and Trademark "with new form and also whatsapp ads".

## 1. Sanjeev's decisions

| # | When | Question | Answer |
|---|---|---|---|
| D1 | ~15:10 | Routing for paid TM and INC leads | **New PPC rule per product**: round robin with online status, Pavneet Kaur as default owner |
| D2 | ~15:10 | WhatsApp chats from TM and INC ads | **Support-first**, same as SIB-04 and SIB-05 |
| D3 | ~15:10 | Where the INC WhatsApp ad set lives | **New ad set inside #IND1** (keeps account history) |
| D4 | 15:53 | Add Sudip Manna, Foziya Ansari, Himanshu Singh, Shubendu Banerjee to which pool? | **Both** rules |

## 2. Findings (R-numbers continue the 15 Oct logs)

| # | Finding | Method |
|---|---|---|
| R1 | 14:55 live check. #IND1 Ad-2 ACTIVE and delivering (₹198.77, 429 impressions today, 0 leads). SIB-02 still a draft: EDITING, VALIDATED, no errors. | Meta connector (live + draft) |
| R2 | First click after hook v1.1: WA_Ad_Clicks 1123581000948301060 at 14:53:51, ad 120246968790550449, Signature_Check **`mismatch n0 cx`**. The body is plain ASCII, so the non-ASCII theory (W6 doc §3 cause b) is ruled out. `cx` = no Content-Length header, so the "arrived unchanged" flag can't be read; the 14 Oct synthetic test already showed Zoho passes the body unchanged. Most likely cause: the stored App secret is wrong (cause a). Four more clicks 15:21–15:34 showed the same. | COQL |
| R3 | No business_messaging event sent yet. Fatema (1123581000948418152), the first matched click lead, is **Lost**. | COQL |
| R4 | 16 paid-Meta leads since 12:00, all SIB-04 (12 WhatsApp, 4 form). 12 have no Lead_Status; oldest 13:19. | COQL |
| R5 | Team Sheet, "Lead Handler Group" tab (only this tab read). Headers are now **PG-01 … PG-14**. PG-09 Intellectual Property: Anshu Yadav, Krishna Gupta, Aditya Bisht, Gaurav Pandey, Mahima. PG-01 Entity Setup - Domestic: Tarun Kumar, Mahima, Anish Singh, Amit Kumar3, Aditya Bisht, Krishna Gupta, Rama Dwivedi, Praveen Singh, Santosh Kumar. PG-11 now lists 13 names (Sudip Manna, Foziya Ansari, Shubendu Banerjee, Himanshu Singh added; Gaurav gone). | Google Sheets |
| R6 | Only 3 Leads assignment rules exist: Lead - General 2026, PPC - SIB-04 (LG-11), PPC - SIB-05 (PG-02). No TM or INC rule. | getAssignmentRules |
| R7 | Sept form leads: Incorporation V2 → product "Incorporation - Pvt Ltd" 1123581000069126115, Product Cat **Start Company** (also Start LLP, Start Firm, Start Sec 8, Post INC). Trademark V2 → "TMF - Standard TM Filing" 1123581000103801012, Product Cat **TM Filing in India**. Both forms spread over ~14 RMs via Lead - General 2026. Meta_Campaign stamped as **"#IND 1 — Incorporation"** and **"#IND3 - Trademark"**. | COQL |
| R8 | Tags already exist: **FB-TMF** 1123581000904279034 and **FB-INC** 1123581000836327716. Use these (not "FB-TM" as the IND1/SIB-02 log said). | getTags |
| R9 | CRM user IDs (all active): Anshu Yadav 1123581000919146001, Krishna Gupta 1123581000893487006, Aditya Bisht 1123581000900716015, Mahima Sehrawat 1123581000899805001, Tarun Kumar 1123581000898222001, Anish Singh 1123581000904230019, Amit Kumar 3 1123581000900455002, Rama Dwivedi 1123581000517691001, Praveen Singh 1123581000005632013 (Gold Team), Santosh Kumar 1123581000005475021 (Gold Team), Sudip Manna 1123581000057363001, Foziya Ansari 1123581000033869514, Himanshu Singh 1123581000796765001, Shubendu Banerjee 1123581000037468001, Pavneet Kaur 1123581000757738001. Gaurav Pandey is disabled, so he is left out. | getUsers |
| R10 | SIB-02 draft ad: legacy top-level `body`/`title` still showed the old text; flagged for a check after publishing (see R12). Still on in the draft: show_summary, reveal_details_over_time, show_destination_blurbs, generate_cta (AI options), and Messenger lead follow-up (b2p_messaging). | Meta connector (draft) |
| R11 | Claude could not create the assignment rules from this session (the CRM API create was not permitted). **Nothing was created by Claude.** Sanjeev creates both rules himself in Setup (steps in §3); Claude then reads them back. | Browser |
| R12 | **SIB-02 published by Sanjeev (~15:30).** Ad 120247048085600449 ACTIVE / PENDING_REVIEW, new creative **1414111734270603**. Published body and title match the approved text exactly ("₹1,999 + GST", per-class ₹4,500 / ₹9,000 government fee, 14,000+ applications filed, both non-affiliation lines). | Meta connector |
| R13 | **App secret re-pasted by Sanjeev into `meta_wa_app_secret` at ~15:37.** Claude opened the two pages in his Chrome and did not read either. **Both clicks after the re-paste (15:39:03 WA_Ad_Clicks 1123581000948312080, 15:45:25 1123581000948380104) still show `mismatch n0 cx`.** So the secret was not the (only) cause; the remaining explanation is that Zoho hands the function a body that is not byte-identical to what Meta signed (the `cx` flag means this can't be measured on this endpoint). Per W6 doc §2: **signature can't be enforced here; the hook stays record-only**, and the secret URL plus API key remain the gate. Hook v2 (enforcement) is dropped; click capture and matching are unaffected. | Chrome (tabs only); COQL |
| R14 | **Rules created by Sanjeev (16:01 and 16:20).** A = **PPC - SIB-02 Trademark - PG-09, id 1123581000948411109**: matches §3 exactly (Product Cat TM Filing in India OR Tag FB-TMF; 8 users; online status; default Pavneet). B = **PPC - INC Incorporation - PG-01, id 1123581000948411180**: 13 users, online status, default Pavneet all correct, but the two criteria are joined with **AND** instead of OR, so a lead needs both a Start Company/Firm/LLP category and Tag FB-INC. Fix: change the pattern to "1 or 2". Both descriptions are empty (cosmetic). | CRM v8 GET (read-only) |
| R15 | **Lead - General 2026** (modified by Sanjeev 16:14): entry 2 (Start Company/LLP/Firm/Proprietorship/HUF/Name Approval/DSC **or** Tag FB-INC or **FB-INCORP**) now round-robins over the same 13 people as rule B. Gaurav Pandey (disabled) is still listed in entries 3, 7, 9, 12 and 16. | CRM v8 GET |
| R16 | **FB-INCORP usage.** Leads tag 1123581000909297197: **892 records**, still being stamped today by the LeadChain Incorporation V2 chain (leads 15:25 and 16:16). Referenced by Lead - General 2026 entry 2 and by the **inactive** workflow "1 Lead Source" (1123581000225325419); no Leads custom view uses it (37 scanned). Contacts has a separate empty FB-INCORP tag (1123581000909131512, 0 records). Deals: none. FB-INC (1123581000836327716) has 1,321 Leads. | getTags, COQL, v8 GET of 30 workflows and 37 views |
| R17 | **First relaunch form leads.** IND1: Jagjit Singh Phogat 1123581000948383116 (15:25, LLP Registration / Start LLP, owner Rama Dwivedi); Mukesh Vyas 1123581000948436150 (16:16, **Product Name and Product Cat blank**, owner Praveen Singh). SIB-02: E Jayachandrareddy 1123581000948436123 (15:50, Meta_Campaign "SIB-02 Trademark", Tag FB-TMF, **Product Name and Product Cat blank**, owner Krishna Gupta). Owners all came from the general rule and sit in the right pools. Blank product on 2 of 3 → add `ppc_form_tidy` CONFIG blocks for "Incorporation V2" and "Trademark V2" (code to be shown before saving). | COQL |

## 3. The two assignment rules (final spec, created by Sanjeev in Setup)

Both: module Leads, one rule entry, criteria pattern "1 or 2", round robin over users, **user availability = online status**, default owner **Pavneet Kaur**. Same layout as "PPC - SIB-05 India Entry - PG-02".

### A. PPC - SIB-02 Trademark - PG-09
- Criteria: Product Category is **TM Filing in India** OR Tag is **FB-TMF**
- Round robin (8): Anshu Yadav, Krishna Gupta, Aditya Bisht, Mahima Sehrawat, Sudip Manna, Foziya Ansari, Himanshu Singh, Shubendu Banerjee
- Description: "15 Oct 2026. Meta SIB-02 Trademark (Form + WhatsApp). Invoked by the TM WhatsApp bot and any LeadChain chain that passes this rule id. Product Cat TM Filing in India, or Tag FB-TMF, round robin over 8 users with online status. If none online, Pavneet Kaur."

### B. PPC - INC Incorporation - PG-01
- Criteria: Product Category is **Start Company, Start LLP or Start Firm** OR Tag is **FB-INC**
- Round robin (13): Tarun Kumar, Mahima Sehrawat, Anish Singh, Amit Kumar 3, Aditya Bisht, Krishna Gupta, Rama Dwivedi, Praveen Singh, Santosh Kumar, Sudip Manna, Foziya Ansari, Himanshu Singh, Shubendu Banerjee
- Description: "15 Oct 2026. Meta #IND1 Incorporation (Form + WhatsApp). Invoked by the INC WhatsApp bot and any LeadChain chain that passes this rule id. Product Cat Start Company / Start LLP / Start Firm, or Tag FB-INC, round robin over 13 users with online status. If none online, Pavneet Kaur."
- Sec 8 (Start Sec 8, PG-07 NGO) and Post INC do not match, so they fall to Pavneet for triage.

**Risk note (for Sanjeev, not a blocker):** in the 13 Aug speed-to-lead check, Anshu Yadav (69%), Tarun Kumar (83%) and Santosh Kumar (89%) left most paid leads unworked. Re-check first-contact rate per owner after 3 days.

**What the rules change:** nothing until something passes their id.
- **WhatsApp leads:** the bot plug `sib_wa_lead` passes `ruleid`, so TM/INC chat leads use the new rules from day 1.
- **Form leads (#IND1 Incorporation V2, SIB-02 Trademark V2):** keep the general round robin until the LeadChain chains pass the new rule ids. Older chains are not edited by Claude; repointing them is Sanjeev's step.
- **Known gap, harmless:** workflow "Lead Assignemnt - Edits" Condition 3 sends any Auto + Advt - WhatsApp + owner Pavneet lead to the SIB-04 LG-11 rule. For a TM/INC lead that rule doesn't match, so it falls back to Pavneet (no misroute). Scoping Condition 3 to SIB-04, or adding TM/INC conditions, is a later one-line change.

## 4. Bots (SalesIQ Tiya project) — handoff prompt

Separate file: `Meta Ads/Tiya_Project_Prompt_TM-INC_Bots_2026-10-15.md`. Paste it into the SalesIQ Tiya project once the rule ids exist.

| | Trademark | Incorporation |
|---|---|---|
| WhatsApp number | +91 95994 81905 | +91 95991 99509 |
| SalesIQ brand | Trademark & IPR | Start Business |
| Ad codes in pre-filled message | TM-C1, TM-C2 … | INC-C1, INC-C2 … |
| `campaign` | SIB-02 Trademark | #IND 1 — Incorporation |
| `productid` | 1123581000103801012 (TMF - Standard TM Filing) | 1123581000069126115 (Incorporation - Pvt Ltd) |
| `productcat` | TM Filing in India | Start Company |
| `tag` | FB-TMF | FB-INC |
| `ruleid` | 1123581000948411109 (rule A) | 1123581000948411180 (rule B) |
| Chat routing | Support-first (Customer Support, then transfer to CRM owner) | Support-first |

## 5. CTWA ad sets (draft specs for a later approval; nothing built)

| | SIB-02 TM WhatsApp | #IND1 INC WhatsApp |
|---|---|---|
| Home | Campaign SIB-02 Trademark (120247048085410449) | Campaign #IND1 (120240912969660449) |
| Name | SIB-02 \| TM \| WhatsApp \| IN | C1 - INC \| WhatsApp \| IN |
| Destination | WhatsApp +91 95994 81905 | WhatsApp +91 95991 99509 |
| Budget | ₹1,000/day (planned in the 15 Oct log) | ₹1,500/day proposed (domestic cap ₹6,500: IND1 ₹2,500 + SIB-02 Form ₹1,000 + TM WA ₹1,000 + INC WA ₹1,500 = ₹6,000) |
| Targeting | Same as the SIB-02 form ad set | Same as #IND1 24Hr INSA |
| Placements | FB + IG; no Audience Network (account-level exclusion) | same |
| Copy | Approved TM text, with "Message us on WhatsApp" and the ad code in the pre-filled message; Sanjeev OKs exact text | Approved INC Ad-2 text, same pattern |
| Creatives | Vipin (Canva "PPC 2026"), 4:5 feed + 9:16 Stories/Reels | same |
| Pre-condition | Bot live on …81905 and rule A exists | Bot live on …99509 and rule B exists |
| Stop-loss | Pause if 3-day cost per CRM lead > ₹340, or 2 spend-days with 0 CRM leads | Pause if 3-day cost per CRM lead > ₹440, or 2 spend-days with 0 CRM leads |

Off-hours: SIB-04 spent 28% of a day's budget between 00:00 and 06:00 IST (15 Oct log R5). Chat hours are Mon–Sat 09:30–19:30. A schedule needs a lifetime budget; decide before building.

Funds: every extra ₹2,500/day shortens the prepaid runway. ₹25,000 added 10:24 today was expected to last to about Saturday at ~₹12.4k/day.

## 6. Order of work

| # | Step | Who | Status |
|---|---|---|---|
| 1 | Create rules A and B in Setup per §3 | Sanjeev | **Done** (R14); rule B pattern still to change from AND to "1 or 2" |
| 2 | Read the rules back; fill both rule ids into the Tiya handoff prompt | Claude | **Done** |
| 2a-done | **Done 17:00 (R18).** Rule B on OR (16:42); Gaurav and FB-INCORP removed from Lead - General 2026 (16:51); LeadChain Incorporation V2 chain tag = FB-INC (assignment rule still Lead - General 2026, whose entry 2 routes Start Company/LLP/Firm or FB-INC to the same 13 people); Leads tag merged: FB-INCORP gone, **FB-INC 2,213 = 1,321 + 892**, today's two IND1 leads now carry FB-INC; the empty Contacts FB-INCORP was renamed to FB-INC (0 records). No FB-INCORP remains in Leads, Contacts, Deals or any assignment rule. | Sanjeev; verified by Claude | Done |
| 2a | Retire FB-INCORP (Sanjeev, 16:21): (i) LeadChain Incorporation V2 chain static tag FB-INCORP → FB-INC; (ii) remove FB-INCORP from Lead - General 2026 entry 2; (iii) Leads → Actions → Manage Tags → edit FB-INCORP → rename to FB-INC → "Yes, Merge" (moves all 892 records); (iv) Contacts → Manage Tags → delete the empty FB-INCORP. Claude then confirms FB-INCORP is gone and FB-INC's count rose. | Sanjeev, then Claude | Open |
| 2b | `ppc_form_tidy` CONFIG blocks for Incorporation V2 and Trademark V2 (R17) | Claude, approved by Sanjeev 17:07 | **Done 17:10** — v1.2 live (`ppc_form_tidy_v1.2_2026-10-15.deluge.txt`); Section 8 → Sec 8 Pvt Guarantee; lead 1123581000948436150 backfilled |
| 3 | Paste the Tiya prompt into the SalesIQ Tiya project | Sanjeev | After 2 |
| 4 | Publish SIB-02; check published creative text | Sanjeev, Claude | **Done** (R12); Meta review pending |
| 5 | Repoint the Incorporation V2 and Trademark V2 LeadChain chains to the new rule ids (optional) | Sanjeev | Open |
| 6 | Re-copy the App secret into `meta_wa_app_secret` | Sanjeev | **Done** (R13); confirm on next click |
| 7 | WhatsApp creatives and exact copy for TM and INC | Vipin, Sanjeev | Open |
| 8 | Build both CTWA ad sets as drafts once 1–3 and 7 are done; Sanjeev publishes | Claude, Sanjeev | Later |
