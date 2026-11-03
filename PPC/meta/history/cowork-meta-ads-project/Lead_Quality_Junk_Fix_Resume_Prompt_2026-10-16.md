# New session: fix junk and irrelevant Meta leads (written 16 Oct 2026, 22:10 IST)

Start this in a **new session** in the "Meta Ads - Optimisation" project. Paste this file's contents, or say: *"Continue from Meta Ads/Lead_Quality_Junk_Fix_Resume_Prompt_2026-10-16.md"*.

## The job

Sanjeev, 16 Oct 22:03: *"first of all we need to fix low quality and mostly irrelevant leads … 80% leads now received in past 3-4 days are junk"*.

This comes **before** any further SIB-05 work. SIB-05 is parked; its state is in `Meta Ads/SIB-05_Resume_Prompt_2026-10-16_1400.md`.

**Operating principle (Sanjeev, 16 Oct):** build and judge every campaign on lead quality first, never on cheap leads.

**Standing instruction for ACR (SIB-04 Company Annual Filings), verbatim:**
> "the audience for ACR has to be only customer data of company director of FY 2025-26 and before with safeguards such as age, gender, education as it was very effective in CCFS."

What this means:
- **Inclusion:** the director custom-audience lists only, i.e. directors of companies incorporated in FY 2025-26 or earlier.
- **Safeguards as hard limits:** age, gender and education.
- **This mirrors #IND4 CCFS:** 6 Director lists, hard; Advantage+ audience OFF; no list or lookalike expansion; male; 19 cities; English. CCFS was the effective campaign.
- **Advantage+ audience must be turned OFF.** Otherwise the lists, gender, maximum age and education are only suggestions (see `SIB-04_Junk_Diagnosis_2026-10-16.md` §1 and the connector's own rule: switch A+A off only when the advertiser requires delivery to only a custom audience; this is that case).
- **Confirm before building:**
  - which director lists (names and IDs) cover "FY 2025-26 and before";
  - whether the 8 LLP lists are included for LLP Form 8 / Form 11;
  - the exact age range, gender and education values.

## Read first

1. `Meta Ads/SIB-04_Junk_Diagnosis_2026-10-16.md`
   - settings side by side (SIB-04 vs CCFS vs #IND1 vs TM);
   - the junk definition;
   - what is hard and what is a suggestion under Advantage+ audience.
2. `Meta Ads/Change_Log_2026-10-16_SIB-04-CTWA-Audience-Controls.md`
   - the English + minimum-age-25 change on the SIB-04 WhatsApp ad set (live 16 Oct 11:41);
   - its read date of 22 Oct.
3. `Meta Ads/SIB-04_Junk_Quality_Resume_Prompt_2026-10-15.md`: the CCFS and SIB-04 targeting comparison (lists, relaxation, education_statuses, optimisation goal, placements).
4. `Meta Ads/SetIndiaBiz_Meta_Saved_Audiences.docx`: SAV-06 ROC Annual Filing and the director custom audience of about 3 lakh.
5. `Meta Ads/Change_Log_2026-10-16_IND1-Source-Backfill-and-TM-INC-WhatsApp-Drafts.md`: the #IND1 and SIB-02 relaunch state.
6. The operator rules in the project instructions:
   - the six diagnostic buckets;
   - the baseline losses (51% sales-process, 32% pricing/competition, 11% targeting);
   - **don't blame targeting before checking speed-to-lead and sales handling**;
   - but separate genuinely irrelevant leads (wrong person, job seeker, mistake, spam) from leads the team failed to work.

## Step 1: measure (read-only)

**Window:** the last 4 days (13–16 Oct) against the 7 days before.

**CRM pull (COQL):** all paid-Meta leads, i.e.
- Lead_Channel "Advt";
- Lead_Source "Advt - Facebook" / "Advt - Instagram" / "Advt - WhatsApp", or Meta_Lead_Form not empty;
- plus "Direct" leads that carry Meta fields.

**Fields:** Meta_Campaign, Meta_Ad_Set, Meta_Ad (or Meta_Ad_Code), Meta_Lead_Form, Lead_Source, Owner, Created_Time, Lead_Status, Why_Disqualified, RM_Lead_Quality, Mkt_Leat_Quality, CSD_Lead_Quality, Select_Country/State/City, Product_Name, First_Contact_Time.

**Classify each lead:**
- **junk/irrelevant:** Inquired by Mistake, Job Seeker, Bot Created/Spam, Wrong Info, or a quality field of Invalid;
- **valid;**
- **not yet worked:** blank or Establishing Contact.

Report the junk % by:
- campaign (SIB-04 Form, SIB-04 WhatsApp, #IND1 Incorporation, SIB-02 Trademark, others live);
- ad set and ad;
- source (form vs WhatsApp);
- state or city, where known;
- owner;
- hour of day.

**Meta pull (connector):** spend, results, and the breakdowns by placement, age, gender and region for the same ad sets and window.

**Live targeting:** for every live ad set, record:
- whether Advantage+ audience is on;
- locales, age_min/age_max, genders, geo;
- custom audiences and relaxation;
- education_statuses;
- optimisation goal;
- placements.

**Compare with CCFS:** pull the CCFS ad set's targeting spec to copy its safeguards. CCFS is **#IND4**; find its ad set IDs with ads_get_ad_entities (name contains "CCFS").

**List the director/LLP custom audiences** with ads_get_ad_account_custom_audiences: names, sizes, created dates and source. Flag which are FY 2025-26-or-earlier directors.

**Watch the 3–4 day timing.** Check what changed on 12–13 Oct:
- the #IND1 and SIB-02 relaunches on 15 Oct;
- the CTWA growth;
- the SIB-04 placement change on 13 Oct;
- the funding top-up.

## Step 2: diagnose and recommend

**Bucket every junk lead** with the six buckets, and name the top 2–3 causes with numbers.

**For SIB-04 ACR, a concrete build to replace the open audience.** Done as a new ad set or a duplicate, never by editing the live one in place without approval:
- Advantage+ audience OFF.
- Custom audiences: director lists, FY 2025-26 and before, only. No lookalike, no expansion (`targeting_relaxation` 0 for both).
- Hard age range, gender, and education (education_statuses; verify the enum).
- English locales; city or state list as CCFS.
- Placements Feed, Stories and Reels.
- Optimisation: consider OFFSITE_CONVERSIONS or quality-lead signals over LEAD_GENERATION/CONVERSATIONS.
- Estimated audience size, budget and a stop-loss.

**For the other campaigns:** where the junk share is high, propose the matching safeguards. The same principle applies: hard limits, not suggestions.

## Step 3: changes (only on Sanjeev's explicit go)

- One variable at a time.
- Before and after evidence.
- A logged stop-loss.
- Read back through the connector.

## Hard rules (unchanged)

- Never publish, activate, or click Publish / "Review and publish" / "Preview to publish". Never call ads_activate_entity.
- Never move money, top up, or enter passwords.
- Every Meta change needs Sanjeev's explicit approval.
- CRM writes:
  - ask first; connector writes pass `trigger: []`;
  - mass writes need a dry run first;
  - never delete records.
- Show code or a diff before saving any production function, template or workflow, and back up the current version first.
  - **Note (16 Oct):** the permission check now refuses Claude typing into the Zoho function IDE and searching the Workflow Rules page. Expect to guide Sanjeev through such edits step by step: he does the clicks, Claude verifies.
- Never read or print the Meta or WhatsApp tokens.
- Zoho Social and the SalesIQ Tiya project's objects are off-limits.

## Working style Sanjeev asked for (16 Oct)

When a step needs him in the browser:
- give **one instruction at a time**;
- open the page in his Chrome first;
- check the screen after each step before giving the next.

## Context from 16 Oct

**Funding:**
- The prepaid account was expected to run out around **Sat 17 Oct midday**.
- Funding is human-only.
- If spend stops, the "last 4 days" pattern can't be retested until it is topped up.

**LeadChain may drop leads whose phone or email already exists in CRM.**
- On the 20:26 SIB-05 test, LeadChain counted the lead but no CRM lead was created.
- Not confirmed.
- If true, real leads are being lost, and the measured junk % is biased. Check the LeadChain logs, or compare Meta lead counts with CRM counts per form for 13–16 Oct.

**SIB-04 WhatsApp:**
- English plus minimum age 25 has been live since 16 Oct 11:41.
- Leads after that time are the first test of it. Split the window there.

## Output

End with:
- a short report: what's junk and why, with numbers;
- the recommended changes, waiting for Sanjeev's go;
- a dated change log;
- the prompt for the next session.
