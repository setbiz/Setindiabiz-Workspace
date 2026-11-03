# Junk and irrelevant Meta leads — diagnosis, 16 Oct 2026 (night)

Read-only. **No Meta or CRM changes were made in this session.**

**Sources:** Zoho CRM COQL, pulled 16 Oct ~22:20–23:00 IST (all 405 leads with Meta_Campaign stamped, created 10–16 Oct; row totals and status / loss-reason totals re-checked against CRM GROUP BY counts and matched exactly). Meta connector: daily ad-set spend and results 10–16 Oct, age × gender, region and placement breakdowns 13–16 Oct, live targeting specs, custom-audience list, CCFS lifetime age × gender.

**Definitions (project standard):**
- **Junk** = Why_Disqualified is Inquired by Mistake, Job Seeker, Bot Created/Spam or Wrong Info, or a quality field is Invalid.
- **Not a buyer** = No Product Offering, Not Eligible, Non-Compliant, Language Issue.
- **Rejected** = junk + not a buyer.
- **Valid** = Lead_Status Valid Lead / Negotiation / Proposal Sent / Payment Pending, or a quality field starting "Valid".
- **Worked** = Lead_Status is not blank or Establishing Contact.
- Windows: **10–12 Oct** (the first SIB-04 leads arrived 10 Oct, so there is no earlier 7-day base) against **13–16 Oct**.

## Answer in one paragraph

Sanjeev's "80% junk" is correct, and it is almost entirely **one ad set: SIB-04 WhatsApp**. Of the 93 SIB-04 WhatsApp leads the team worked from 13–16 Oct, **81 (87%) were rejected** and only **8 (9%) were valid**; in 10–12 Oct it was 52% rejected and 43% valid. The cause is the audience, not follow-up: **95% of 13–16 Oct losses are targeting** (baseline 11%), sales-process is 3%. SIB-04's director and LLP lists are only *suggestions* (Advantage+ audience on, list expansion on, 12 hidden lookalikes auto-added), so Meta can show the ads to anyone in India. Since 13 Oct Meta's optimiser has found ever-cheaper people to tap "Send message" — cost per chat fell from ₹157 to ₹48 — and those people are not company directors. The SIB-04 Form ad set is starting to drift the same way (58% of its 13–16 Oct leads were aged 18–24). **#IND1 Incorporation and SIB-02 Trademark are clean so far** (0 rejected of 16 worked).

## 1. Where the junk is

| Campaign / path | Window | Leads | Worked | Rejected (of worked) | Valid (of worked) | Unworked |
|---|---|---|---|---|---|---|
| SIB-04 WhatsApp | 10–12 Oct | 101 | 61 | 32 (52%) | 26 (43%) | 40 |
| SIB-04 WhatsApp | **13–16 Oct** | **208** | 93 | **81 (87%)** | **8 (9%)** | 115 |
| SIB-04 Form | 10–12 Oct | 16 | 9 | 0 | 8 | 7 |
| SIB-04 Form | **13–16 Oct** | 40 | 15 | **10 (67%)** | 5 | 25 |
| #IND1 Incorporation (form) | 15–16 Oct | 26 | 10 | 0 | 10 | 16 |
| SIB-02 Trademark (form + 1 WA) | 15–16 Oct | 14 | 6 | 0 | 6 | 8 |

- SIB-04 WhatsApp leads per day: 21, 30, 50, 28, 42, 55, **83** (10→16 Oct). Volume quadrupled while daily spend stayed ~₹2.2–4.2k.
- The SIB-04 bot stamps every WhatsApp lead "ACR", so WhatsApp junk cannot be split by ad in CRM. Form leads by ad show no standout ad.
- Junk is spread across ~30 owners; it is not one rep's mislabelling.
- Geography cannot be read from CRM (only 5 of 365 SIB-04 leads have State/City).

**The 16 Oct 11:41 English + age-25 change has not helped yet:** WhatsApp leads after it: 50, of which 19 worked → 15 junk, 1 valid. Early and in a learning reset, but no sign of improvement.

## 2. Loss reasons, six buckets (all Meta leads with a disqualify reason)

| Bucket | 10–12 Oct | 13–16 Oct | Baseline |
|---|---|---|---|
| Targeting — junk (Mistake 76 overall, Wrong Info 12, Job Seeker 6, Bot 6) | 28 (72%) | 72 (75%) | |
| Targeting — not a buyer (No Product 10, Not Eligible 5, Language 5, Non-Compliant 2) | 3 (8%) | 19 (20%) | |
| **Targeting total** | 80% | **95%** | **11%** |
| Offer / pricing / competition (Pricing, Other CA) | 4 (10%) | 0 | 32% |
| Sales-process (Avoiding Call) | 3 (8%) | 3 (3%) | 51% |
| Natural attrition (Not Interested) | 1 | 2 | |
| Geography / serviceability | 0 | 0 | |
| Total with a reason | 39 | 96 | |

This is the reverse of the baseline. The operator rule says check speed-to-lead and pricing before blaming targeting: both were checked, and the losses are not there. **This is an ad-audience problem.**

## 3. What changed in the last 3–4 days (Meta side)

**SIB-04 WhatsApp ad set (CONVERSATIONS), by day:**

| Day | Spend | Chats (Meta) | Cost per chat | CRM WA leads |
|---|---|---|---|---|
| 10 Oct | ₹3,803 | 22 | ₹173 | 21 |
| 11 Oct | ₹3,599 | 31 | ₹116 | 30 |
| 12 Oct | ₹4,176 | 47 | ₹89 | 50 |
| 13 Oct | ₹3,607 | 23 | ₹157 | 28 |
| 14 Oct | ₹2,230 | 32 | ₹70 | 42 |
| 15 Oct | ₹3,168 | 49 | ₹65 | 55 |
| 16 Oct | ₹3,314 | 69 | ₹48 | 83 |

The optimiser is doing exactly what it is told — more chats for less money — by moving to people who tap readily. With the lists set as suggestions, nothing stops it.

**Who it reached, 13–16 Oct:**

| | SIB-04 WhatsApp | SIB-04 Form | #IND4 CCFS (lifetime, the model) |
|---|---|---|---|
| Aged 18–24 | 26% of chats (45/173) | **58% of leads (25/43)**, 40% of spend | 3.6% of spend |
| Women | 25% of chats, 18% of spend | 33% of leads | 5.3% of spend |
| Locations | 35 states/UTs, top spend UP, Maharashtra, WB, Rajasthan, Bihar | same | 19 metro cities |

**Cost per valid lead (13–16 Oct is young; half unworked):**

| Ad set | 10–12 Oct | 13–16 Oct |
|---|---|---|
| SIB-04 WhatsApp | ₹11,577 / 26 = ₹445 | ₹12,319 / 8 = **₹1,540** |
| SIB-04 Form | ₹7,402 / 8 = ₹925 | ₹10,080 / 5 = **₹2,016** |
| #IND1 24Hr INSA | — | ₹7,141 / 10 = ₹714 (15–16 Oct) |
| SIB-02 TM Form | — | ₹1,576 / 6 = ₹263 (15–16 Oct) |

Other events 12–16 Oct (activity log): #IND1 relaunched and SIB-02 created 15 Oct (both clean); SIB-04 WhatsApp English + age 25 on 16 Oct; the SIB-05 India Entry campaign was created (inactive, not spending). The 13 Oct placement exclusions did not cause this (Audience Network was ₹419 of the WhatsApp spend 13–16 Oct, all on 13 Oct).

## 4. Live targeting vs CCFS

| Setting | SIB-04 WhatsApp (now) | SIB-04 Form (now) | #IND4 CCFS ad set 120244101705150449 |
|---|---|---|---|
| Advantage+ audience | **On** | **On** | **Off** |
| Lists | 15 (8 Director incl. 1% LAL, 7 LLP) **as suggestions**; relaxation 1/1; `expansion_all`; Meta has added **12 hidden 1% lookalikes** | same | **6 Director lists, hard** (2019-20 to 2024-25); relaxation 0/0; no lookalikes |
| Gender | all | all | male (5.3% of spend still reached women) |
| Age | 25–65 hard min (since 16 Oct 11:41) | 18–65 | 18–65 hard, 21–55 suggested (3.6% of spend to 18–24) |
| Language | English (US, UK) since 16 Oct | **none** | English (US, UK) |
| Location | all India | all India | 19 cities, 25 mi |
| Education | none | none | **none** — CCFS never used an education filter |
| Placements | Advantage+ (FB/IG/WhatsApp Status/Threads) | FB + IG automatic | FB + IG Feed, Stories, Reels only |
| Optimises for | Chats started | On-ad form leads | Dataset Lead event |

Meta's rule (help article: [How to create a campaign using Advantage+ audience](https://www.facebook.com/business/help/793748385630490)): with Advantage+ audience on, only location, minimum age, language and custom-audience exclusions are hard. Age range, gender, custom-audience inclusions and detailed targeting become hard only under "Further limit your audience / reach" with "Use as a suggestion" unticked ([How to use Advantage+ custom audience](https://www.facebook.com/business/help/414975413946182)).

## 5. Director and LLP custom audiences (customer lists)

| List | Audience id | Size (Meta range) | In SIB-04 now | In CCFS |
|---|---|---|---|---|
| Company Director 2019-20 | 120243249278260449 | 60–71k | yes | yes |
| Company Director 2020-21 | 120243249316070449 | 80–94k | yes | yes |
| Company Director 2021-22 | 120227495253470449 | 72–85k | yes | yes |
| Company Director 2022-23 | 120226471598550449 | 99–117k | yes | yes |
| Company Director 2023-24 | 120226339094810449 | 268–315k | yes | yes |
| Company Director 2024-25 | 120226217224820449 | 247–291k | yes | yes |
| Company Director 2025-26 | 120243249459750449 | 232–273k | yes | no (created Jun 2026) |
| Company Director 2026-27 | 120243249482500449 | 43–51k | no | no — **outside "FY 2025-26 and before"; keep out** |
| LLP 2019-20 … LLP 2025-26 (7 lists) | see Saved Audiences | 28k–139k each, ~0.47–0.56M total | yes | no |
| LAL-Director-2024-25 1% | 120239558688100449 | lookalike | yes | no |

The seven Director lists for FY 2025-26 and before total about **1.06–1.25 million matched people before overlap**. After male, age, English and 19 cities the reachable audience will be far smaller; Ads Manager shows the estimate when the ad set is drafted.

## 6. LeadChain drop check

Form leads 13–16 Oct, Meta vs CRM: SIB-04 Form 43 vs 40, #IND1 27 vs 26 (Meta figure includes website leads), SIB-02 13 vs 13 → **CRM has ~95%**. About 4 form leads in 4 days did not create a CRM lead, which fits LeadChain merging onto an existing record when the phone/email already exists. It does not move the junk % materially. WhatsApp: CRM 208 leads vs Meta 173 chats (CRM is higher; repeat and non-ad chats to the ACR number land as leads too).

## 7. Sales-process side (not the cause, but real)

- 155 of 309 SIB-04 WhatsApp leads were never worked. 85 of the 208 from 13–16 Oct arrived between 21:00 and 09:00, and 62 of those are unworked.
- 17 Meta leads sit with an owner named **"Lost Records"** and 18 with the default owner (Kaur). Worth a look by the SalesIQ project; not touched here.
- #IND1 and SIB-02: 24 of 40 leads still Establishing Contact or blank.

## 8. Recommended changes

> **Update 16 Oct ~23:15 IST.** Sanjeev approved A (done: WhatsApp ad set paused 22:37 IST) and chose for B: directors only, male, age 25–60 **with** graduate+ education, 19 CCFS cities. B is built as paused drafts for him to publish. Details in `Change_Log_2026-10-16_Lead-Quality-Diagnosis.md`. The table below is the original proposal.

**Change A — now: pause the SIB-04 WhatsApp ad set (120246968316940449).**
- Why: 87% rejected, 9% valid on 13–16 Oct; no improvement after the 16 Oct change; it takes ~₹3.3k/day of the remaining funds that #IND1 and SIB-02 (both clean) can use.
- This replaces the 22 Oct read of the English + age-25 change and its staged Change 2 (city limit); both are overtaken by Change B.
- One variable (status). Before/after: ad-set status and spend read back through the connector.
- Resume rule: it does not come back in its current form — WhatsApp returns only as the directors-only ad set in Change B.

**Change B — after Sanjeev confirms the values below: two new directors-only ad sets in SIB-04, built as paused drafts (Sanjeev publishes).**

| Setting | Proposed | To confirm |
|---|---|---|
| Advantage+ audience | **Off** ("Further limit", "Use as a suggestion" unticked) | — |
| Custom audiences (hard) | 7 Director lists, FY 2019-20 to 2025-26 | LLP lists for the LLP-C1 Form 8 ad? (Form 8 due 30 Oct, LLP Act 2008 s.34 with LLP Rules 2009 r.24) |
| Lookalikes / expansion | none; relaxation 0 / 0 | — |
| Gender | male (as CCFS) | yes / no — it drops genuine women directors |
| Age (hard) | 25–60 | range |
| Education | none (as CCFS) | Adding it is possible as a hard filter with A+A off, but it narrows on top of the list and many Indian profiles have no education entered |
| Language | English (US, UK) | — |
| Location | 19 CCFS cities, 25 mi | or all India (the list is already the main filter) |
| Placements | FB + IG Feed, Stories, Reels | — |
| Form ad set | LEAD_GENERATION, existing form and ads | — |
| WhatsApp ad set | CONVERSATIONS, existing CTWA ads | — |
| Budget | ₹2,500 Form + ₹2,000 WhatsApp per day (was ₹6,000 together) | |

- On publish, the old SIB-04 Form ad set (120246968737470449) is paused in the same step, so the audience is the only thing that changes.
- **Stop-loss:** 3 full days, read on day 6 so leads are worked. **Keep** if rejected ≤25% of worked and valid ≥35% of worked. **Pause and review** if rejected >40%, or if either ad set spends <50% of budget on all 3 days (audience too small — then widen location to all India first, gender second).
- Judge in CRM only, never on Meta's chat or lead count.

**Other campaigns: no change.** #IND1 and SIB-02 already have the hard limits (English, cities, age 25) and are clean. Re-read at the 22 Oct check when more leads are worked. The TM and INC WhatsApp drafts stay unpublished; given what CONVERSATIONS optimisation did here, publish them only after Change B shows a WhatsApp ad set can stay clean.

## 9. Not changed / for others

- Funding: ~₹15.7k was left at 06:42 on 16 Oct against ~₹11k spent on 16 Oct, so delivery likely stops on 17 Oct. Top-up is human-only. Pausing SIB-04 WhatsApp stretches what is left.
- Meta auto-created an ad variant "ACR-C5 | Dates and price | CTWA_Group_1" and an "asa_auto_custom_audience"; noted, not touched.
- SalesIQ project: the ACR bot qualifier ("Are you a director or partner?") is still worth doing; overnight chats and the "Lost Records" owner are theirs.
