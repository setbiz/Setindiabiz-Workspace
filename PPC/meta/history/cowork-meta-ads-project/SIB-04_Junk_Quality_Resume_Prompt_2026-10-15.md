# Resume prompt — SIB-04 (ACR) junk-lead diagnosis — paused 15 Oct 2026 19:40 IST

Paste this into a new chat in the "Meta Ads - Optimisation" project to resume.

---

## What Sanjeev asked (15 Oct, verbatim)

1. "also check acr campaign and especially placement. we are getting many junk,"
2. "why low quality of leads, check if the setting are such which excludes, illiterate, housewives, etc as in ccfs, incorporation and tm campaign, adsets. study them well then figure out where things are getting heywired"
3. "but pause for resumption tomorrow. create your resume prompt"

Status: read-only investigation, about 70% done. **No Meta or CRM changes were made.**

## Read first

- `SIB-04_Diagnosis_2026-10-13_Placement-Quality-CAPI-Assignment.md`
- `Change_Log_2026-10-13_Placement-Controls.md`. Account-level placement exclusions went live 13 Oct ~12:30 IST: Audience Network, Marketplace and right column. The **3-day stop-loss review is due 17 Oct morning**, measured on 14–16 Oct.
- The SalesIQ handover note of 15 Oct (pasted in the chat). The SIB-04 bot stamps every WhatsApp lead `Meta_Ad_Code = "ACR"`, so SIB-04 cannot be split by ad in CRM.

## IDs

- Account: 152154124583473
- SIB-04 campaign: 120246968311680449
  - Form ad set 120246968737470449: ₹2,500/day, LEAD_GENERATION, ends 29 Nov
  - CTWA ad set 120246968316940449: ₹3,500/day, CONVERSATIONS, no end date
- Comparators:
  - #IND4 CCFS (paused): ad set 120244101705150449
  - #IND1: active ad set "C1 - 24Hr INSA" 120240912969640449; paused Daytime INSA and both LAL ad sets
  - #IND3 TM (paused): ad sets 120243118118000449 (TMF-SA) and 120243249506380449 (Director-TMF)
  - SIB-02 TM (new, active): Form ad set 120247048085540449

## Findings so far

### A. Meta delivery, SIB-04 lifetime (9 Oct – 15 Oct, partial day)

| Ad set | Spend | Results | Cost per result |
|---|---|---|---|
| Form | ₹13,999 | 43 leads | ₹326 (CPM ₹305) |
| CTWA | ₹18,973 | 174 conversations | ₹109 (CPM ₹170) |

**Form leads by placement:**
- FB Reels: 29 of 43 (₹7,496)
- IG Reels: 9
- IG Feed: 3
- FB Feed: 1 (₹1,789)
- IG Stories: 1

**Form leads by age:** 18–24 gave 12 of 43 leads, the cheapest at ₹198.

**CTWA conversations by placement:**
- Audience Network: 45 (₹1,913). Ran 10–13 Oct; ₹0 from 14 Oct after the account exclusion.
- FB Reels: 42
- IG Reels: 39
- FB Feed: 16
- IG Feed: 13
- In-stream: 10
- Reels overlay: 3 (₹256 each)
- IG Stories: 3
- WhatsApp Status: 2 (₹23 spent)

### B. CRM quality

Leads with `Meta_Campaign like '%SIB-04%'`, created from 9 Oct, counted 15 Oct ~19:30 IST via COQL COUNT.
- **Junk** = Why_Disqualified in (Inquired by Mistake, Job Seeker, Bot Created/Spam, Wrong Info), or RM_Lead_Quality = Invalid.
- **Valid** = Lead_Status in (Valid Lead, Negotiation, Proposal Sent, Payment Pending).

| Segment | Leads | Junk | Valid |
|---|---|---|---|
| WhatsApp, created 10–13 Oct (Audience Network ON) | 130 | 33 (25.4%) | 29 (22.3%) |
| WhatsApp, created 14–15 Oct (Audience Network OFF) | 69 | 23 (33.3%) | 3 (4.3%, still young) |
| Form, Advt - Facebook | 23 | 0 | 7 |
| Form, Advt - Instagram | 12 | 0 | 5 |

- **WhatsApp junk did not fall when Audience Network stopped.** Audience Network was not the main junk source.
- **Junk is a WhatsApp-path problem.** Form leads have zero junk.

**Lost leads: 76 in total** (WhatsApp 74, Facebook 1, Instagram 1).

| WhatsApp loss reason | Count |
|---|---|
| Inquired by Mistake | 42 |
| No Product Offering | 6 |
| Job Seeker | 5 |
| Wrong Info | 5 |
| Not Eligible | 4 |
| Bot Created/Spam | 3 |
| Avoiding Call | 2 |
| Language Issue | 2 |
| Not Interested | 2 |
| Other CA | 1 |
| Pricing | 1 |
| Non-Compliant | 1 |

**Loss buckets, all 76 leads, against the project baseline** (51% sales-process / 32% pricing / 11% targeting):

| Bucket | Count | Share |
|---|---|---|
| Junk | 55 | 72% |
| Targeting mismatch (No Product, Not Eligible, Language, Non-Compliant) | 14 | 18% |
| Sales-process | 5 | 7% |
| Pricing | 2 | 3% |

This is the reverse of the baseline: the ad is the problem, not follow-up.

**Early campaign cost per valid lead: about ₹749** (₹32,972 ÷ 44 valid by status). This is campaign level and early. Compare it with the 13 Oct stop-loss baseline of ₹731 and the revert threshold of ₹914.

### C. Targeting: SIB-04 against CCFS, Incorporation and Trademark

Raw targeting specs were pulled 15 Oct with ads_get_ad_entities (level adset, field targeting).

**1. Locations**
- SIB-04: all India.
- CCFS: 19 cities. #IND1: 18 cities. TM and SIB-02: about 30 cities. All of these use a 25-mile radius.

**2. Language (locales 6 and 24, read as English US/UK; verify the IDs)**
- Every comparator ad set has them.
- **SIB-04 has none**, which admits Hindi and regional-only users. This is the likely link to the "illiterate" complaint.

**3. Gender**
- SIB-04: all.
- CCFS, TM-SA, Director-TMF and SIB-02: male only. #IND1 INSA: all; #IND1 LAL ad sets: male.

**4. Age**
- SIB-04: 18–65 with no suggested range.
- CCFS: 18–65 with suggestion 21–55.
- #IND1: minimum 25 (suggestion 25–45).
- TM and SIB-02: minimum 25 (suggestion 25–55).

**5. Education and occupation layer**
- **SIB-04 has no flexible_spec at all.**
- #IND1, TM and SIB-02 add these (an AND / narrowing layer):
  - education_statuses [10, 11, 3, 9], read as professional degree, doctorate, college grad, master's (verify the enum)
  - Small business owners or Page admins behaviours
  - job titles (Founder, Proprietor, Owner, CEO, MD and so on)
  - Business Decision Makers industry
- This narrowing is how the other campaigns keep out the "illiterate / housewife" profile. **None of them uses an exclusion.** All of them do it by narrowing inclusions.

**6. Lists**
- CCFS: 6 Director lists only, `targeting_relaxation` lookalike 0 and custom_audience 0 (no expansion), Advantage+ audience OFF.
- SIB-04: 15 lists (8 LLP, 7 Director) plus a 1% Director lookalike.
  - Relaxation is 1 on both, plus Advantage+ audience ON and `targeting_optimization: expansion_all`.
  - So **every list is only a suggestion**, and Meta can serve anyone in India aged 18+.

**7. Optimisation goal**
- Every comparator uses OFFSITE_CONVERSIONS (Website + Form).
- SIB-04 uses LEAD_GENERATION (on-ad form) and CONVERSATIONS (CTWA), which are the cheapest-action goals.
- CONVERSATIONS rewards one-tap sends of the pre-filled message. That fits "Inquired by Mistake" being 57% of WhatsApp losses.

**8. Placements**
- CCFS: manual, Feed + Stories + Reels.
- SIB-04: Advantage+. After the 13 Oct account exclusion it still includes in-stream, Reels overlay, Search, Notifications, WhatsApp Status, Threads and Explore.

**Working conclusion:** SIB-04 was launched as an open, all-India audience with no language, gender, age or education guardrails, plus list expansion, plus a cheapest-action optimisation goal. The CTWA one-tap format then multiplies accidental and irrelevant chats. Placement was only a small part of it. The form path is clean.

## To do tomorrow (16 Oct), in order

1. **Verify Meta rules** with ads_get_help_article or Meta's docs. Which fields stay hard controls when Advantage+ audience is ON? Expected: location, minimum age, languages, custom-audience exclusions. Gender, maximum age and detailed targeting are only suggestions. Also confirm:
   - the current status of detailed-targeting exclusions
   - the locale IDs 6 and 24
   - the education_statuses enum
2. **Pull the SIB-04 ads and creatives** (ads_get_ad_entities level ad + ads_get_creatives). Check:
   - the copy
   - Hindi or English language
   - the pre-filled WhatsApp text: [ACR-C5], [ACR-C1], [LLP-C1]
   - anything that attracts job seekers or non-company owners

   **Separate the delivery problem from the creative problem.**
3. **CRM checks:**
   - Have the 83 untagged "Self - Web Chat" SIB-04 chats from 13 Oct been backfilled? This affects the WhatsApp counts.
   - Reconcile the 199 CRM WhatsApp leads against Meta's 174 conversations.
   - Exclude test lead 1123581000948692001.
4. **Build the side-by-side table** (SIB-04 vs CCFS vs #IND1 vs TM vs SIB-02) as a Docs or Sheets artifact for Sanjeev.
5. **Recommend at most 1–2 changes**, one variable at a time, each needing approval and a stop-loss. Candidates:
   - (a) Add English locales and city geo matching CCFS to the CTWA ad set. These are hard controls even under Advantage+.
   - (b) Move the CTWA ad set to a CCFS-style manual audience: Director/LLP lists only, no relaxation, Advantage+ audience OFF, minimum age 25.
   - (c) Shift budget from CTWA to the Form ad set, which has zero junk.
   - (d) Add a qualifying first question in the bot before lead creation. **SalesIQ-project owned — ask Sanjeev; do not touch the bots.**

   Gender male-only is Sanjeev's call: women directors and LLP partners are valid buyers. Present it as an option, not a default.

   Remember:
   - An API targeting edit force-pauses the ad set, and reactivation is Sanjeev's in Ads Manager.
   - A targeting edit resets learning.
   - Keep the 17 Oct stop-loss review clean. Ideally make no SIB-04 change before that read, or log any change as a cohort break.

## Ground rules (unchanged)

- Judge only on CRM valid, progressed and won leads, never on Meta conversations or leads.
- The paid segment for SIB-04 includes Advt - WhatsApp.
- Every Meta change needs explicit approval, one variable at a time, before/after evidence and a logged stop-loss.
- No CRM writes without showing Sanjeev first.
- Do not touch SalesIQ bots, plugs, assignment rules or LeadChain.
