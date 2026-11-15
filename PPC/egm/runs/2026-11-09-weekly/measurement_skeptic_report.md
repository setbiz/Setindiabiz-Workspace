# measurement_skeptic report: weekly review w/e 2026-11-08

Raw output from the isolated Goldfish subagent (read-only), 9 Nov 2026.

MEASUREMENT SKEPTIC — REVIEW of `PPC/egm/runs/2026-11-09-weekly/weekly_review.md`
Against: `PPC/egm/standards/weekly-review-standard.md`. Context read: `data.md`, `PPC/shared/*`, `PPC/meta/README.md`, `PPC/meta/changelog.md`.

**Recomputation check:** I recomputed every scorecard ratio from T1/T1-P/T2/T3/T4/T6/T7/T8/T9. CTR, CPC, Meta CPL, CRM CPL, cost/QL, the "vs prev" figures, the 94% forms→CRM match, 79% for B2, ₹3,078 cap remaining, 52%/45% QL, 21/48 = 44%, 14.6%, 13%, 0.21× and ₹1,23,900 / ₹90,860 all match the stated arithmetic. Daily spend (T4) adds up to ₹33,898.29, and so do the billing events (T6). I found no arithmetic errors. The findings below are about sourcing, inference and design.

---

### 1
1. **Severity:** Blocker
2. **Affected Scope:** Header ("Every number is in `data.md`"), §2 target and the "vs target" column, §4.5, §6 actions 1–2, §7.2, §4.7, §3 WhatsApp hypothesis, §7.5
3. **Finding:** Several numbers that drive decisions appear nowhere in `data.md` or in the GoldfishContext:
   - **₹176 break-even CPL** ("90-day CRM basis, 2 Nov audit"). No file, date range or derivation is given. The only sourced target is `kpis.md` / `business-context.md`: ₹130–135 (271 × 50% ≈ ₹135). The whole "vs target" column depends on it. Against ₹130–135 the multiples become: SIB-02 2.2–2.3× (stated 1.7×), SIB-01 2.7–2.8× (2.1×), SIB-04 7.9–8.2× (6.0×), blended 5.2–5.4× (4.0×) [calc: 293/135–130, 366/135–130, 1,062/135–130, 706/135–130].
   - **SIB-05 "₹15,000 further-spend cap" / "owner's 2 Nov rule".** This is the basis for action 2 (a pause) and has no source.
   - **India-entry AOV ≈ ₹86,300 and break-even lead→won ≥ 8.8%** (§7.2). No source, and the CPL it is computed from isn't stated.
   - **18% GST multiplier** (action 1). It's labelled [calc] but the rate isn't sourced. It is corroborated by the data: ₹15,000 / 1.18 = ₹12,711.86 [calc], which exactly equals 4 Nov + 5 Nov spend (1,912.86 + 10,799.00) (T4, T6). Cite that as the evidence.
   - **"≈51% of lost deals to the sales process"** (Cowork baseline), **"Cowork change logs 7–15 Oct" / `sib_wa_lead`**, and the **ads "25,000+"** claim. None has a path.
   - **P "≈1.75 delivery days"** and **"P spend equals the ₹16,949 credit from the 26 Oct top-up"** rest on a Cowork watch log with no path. There's no P daily-spend table (no T4-P).
4. **Required Evidence or Fix:** Add a "Reference figures" table to `data.md` that gives, for each figure, the source file path or connector, the date range and the pull date. Alternatively, re-label each one as "owner-stated, unverified" or as an estimate. Until ₹176 is sourced, compute "vs target" against `kpis.md` ₹130–135, or show both. Pull T4-P (daily spend for 26 Oct–1 Nov) from the Meta connector. Remove the "Every number is in `data.md`" claim, or make it true.

### 2
1. **Severity:** Major
2. **Affected Scope:** §4.2, §5 row 1 ("CPL up 2.5–3.7×")
3. **Finding:** The hypothesis that the narrower audience raised CPMs is only partly backed by the numbers, and the lead counts are below ~30 per arm. Breaking CPL into CPM, CTR and click→lead [calc]:
   - **SIB-01:** CPM ₹273.4 → ₹308.0 (**+13% only**). CTR 1.161% → 0.887% (×0.76). Click→lead 24/146 = 16.4% → 11/116 = 9.5% (×0.58). Combined: 1.13 / 0.764 / 0.577 = 2.56× ✓. Most of the rise comes from CTR and conversion rate, not CPM.
   - **SIB-02:** CPM ₹229.2 → ₹349.4 (+52%). CTR ×0.71. Click→lead 23.6% → 13.9% (×0.59). Combined: 3.67× ✓.
   - **Significance:** the CTR drops are statistically distinguishable (two-proportion z ≈ 2.2 for SIB-01, ≈ 2.5 for SIB-02). The click→lead drops are not: z ≈ 1.6 (p ≈ 0.10) on 24 vs 11 leads, and z ≈ 1.9 (p ≈ 0.06) on 17 vs 26 leads.
   - **Bases differ:** §4 and §5 use the Meta CPL basis. The scorecard uses CRM, which `kpis.md` names as the source of truth. On CRM, SIB-02 is ₹93 → ₹293 = 3.1×, not 3.7×.
   - The bold lead sentence "Costs per lead rose sharply after the 2 Nov targeting change" reads as a finding, not as directional.
4. **Required Evidence or Fix:** Label the CPL comparison as directional (n < 30 per arm, partial weeks). Restate the hypothesis around CTR and click→lead, with CPM as a secondary factor for SIB-01. Pull the auction drivers before attributing the rise: placement, age and audience breakdowns, plus any form changes from the Trademark rebuild. Use one basis (CRM) for "CPL up X×".

### 3
1. **Severity:** Major
2. **Affected Scope:** §4.2–4.4, §5 (all three verdicts), §6 action 1 ("first clean 7-day read"), headline
3. **Finding:** The P→W comparison has confounders that the review doesn't list:
   - **SIB-04 had at least 4 structural changes on 2 Nov:** reactivation, layer-2 targeting, age 25–45 → 25–55, all ads replaced (GC05), and `GST - Company` added in the morning. The Form ad set also had no live ad until 20:42. This meets the standard's ">3 simultaneous structural changes" condition. §5 gives three separate SIB-04 verdicts, but these effects can never be separated.
   - **SIB-02** was rebuilt. P was the "SIB-02 Trademark - Copy" entity (T7), and W added a new Lists ad set on top of layer-2. That means a new learning phase, not a like-for-like comparison.
   - **SIB-01** combined layer-2, a budget cut to ₹1,250, and a budget restore to ₹2,500 on 4 Nov 18:14. W mixes two budget levels. §4.2 doesn't mention this.
   - **2 Nov is not a clean post-change day.** Old ACR ads spent ₹2,090.97 before the pause (T3), and the time the layer-2 change was published isn't given.
   - **Festive seasonality is not mentioned.** Diwali (Lakshmi Puja) falls on Sun 8 Nov 2026 and Dhanteras on 6 Nov (verify against the holiday calendar). W's delivery days (2–5 Nov) are the pre-Diwali week, when Indian CPMs typically rise. P delivered on 26–27 Oct. The proposed "first clean 7-day read" after the top-up would cover the Diwali / Bhai Dooj week, so it isn't clean either. Festive leave also likely explains part of the 21-lead sales backlog.
   - `learnings.md` (2026-01-18) records business-hours automated rules (09:30–19:30). If they are still active, they change what a "delivery day" means.
4. **Required Evidence or Fix:** List these confounders in §4. Treat SIB-04 as one bundled change with a single verdict. Give the publish timestamp of the layer-2 change and exclude pre-change 2 Nov hours, or flag them. Use a full-day pre-period baseline (for example 12–25 Oct for the same campaigns or their predecessors) in addition to P. Add a festive-period caveat and stop calling the next read "clean". Check via the connector whether the automated rules are still active.

### 4
1. **Severity:** Major
2. **Affected Scope:** §5 row 1 (layer-2), action 3 (SIB-01 quality read), action 6, §2 QL definition, review dates in actions 1/3/6
3. **Finding:** The experiments are not pre-registered:
   - **No decision rule.** Neither the layer-2 test nor the SIB-01 test has a primary metric, a baseline, a threshold or MDE, or a stop rule. "Extend to 7 funded days" says how long to run, not how to decide.
   - **The metric doesn't match the changelog.** The 2 Nov SIB-01 entry says to "judge lead quality in Zoho (TL/RM Lead Quality fields)". The review uses Lead_Status (Valid Lead + Proposal Sent) instead, and `kpis.md` doesn't define QL.
   - **No quality baseline at the same lead age** for P or the pre-change period, so "higher quality" can't be tested.
   - **The QL rate measures the sales backlog.** Unworked leads are in the denominator:

     | Campaign | QL / all leads | QL / worked leads [calc] |
     |---|---|---|
     | SIB-02 | 13/25 = 52% | 13/17 = 76% |
     | SIB-01 | 5/11 = 45% | 5/6 = 83% |
     | SIB-04 | 3/10 | 3/3 |

   - **7 days won't produce enough leads.** Projected at W rates per funded day [calc]:

     | Campaign | CRM leads/day | Leads in 7 days | QL in 7 days |
     |---|---|---|---|
     | SIB-02 | 25/3.2 ≈ 7.8 | ≈ 55 | ≈ 28 |
     | SIB-01 | 11/3.2 ≈ 3.4 | ≈ 24 | ≈ 11 |
     | SIB-04 | 10/3.2 ≈ 3.1 | ≈ 22 | ≈ 7 |

     SIB-01 and SIB-04 won't reach ~30 qualified events.
   - **The 16 Nov review date can't be met.** Actions 1, 3 and 6 are set for 2026-11-16, but the account was still unfunded at the 9 Nov ≈10:20 pull, so 7 funded days can't have passed by then.
4. **Required Evidence or Fix:** For each test, state:
   - the primary metric (cost per CRM QL at a fixed lead age, e.g. 14 days, using the TL/RM Lead Quality field the changelog designated);
   - the baseline (pre-change cohort at the same age);
   - the decision threshold (e.g. cost/QL ≤ X, or QL rate ≥ Y percentage points above baseline);
   - the minimum sample (≈30 QL per arm, or a spend cap);
   - a stop rule (e.g. stop if cost per CRM lead > 3× break-even after ₹N).

   Report QL as a share of worked leads alongside a share of all leads. Express review dates as "top-up time + 7 funded days (+ lead-age window)", not as a fixed date.

### 5
1. **Severity:** Major
2. **Affected Scope:** §3 WhatsApp → CRM and ChatGPT bullets, §6 actions 4 and 7, T7 filter
3. **Finding:** The WhatsApp and ChatGPT gaps may be artifacts of how the CRM labels leads, not delivery or plug failures:
   - **Missing labels.** `shared/lead-source-attribution-runbook.md` (§2, §5) has no `Advt - WhatsApp` or `Advt - ChatGPT` value.
   - **How the classifier routes these leads:**
     - `CTWA_Click_ID` → `Advt - Facebook` (rule 7)
     - wa.me / WATI → `Social - WhatsApp`
     - chatgpt / openai referrer → `AI - ChatGPT` (rule 4)
   - **Overwrite risk.** The overwrite guard protects only `Self -*`, `Referral - Clients/Partner/Employee` and `SEO - Zoho Booking`. A lead edit can therefore relabel `Advt - WhatsApp` or `Advt - ChatGPT` leads.
   - **The T7 filter misses them.** `Lead_Source like 'Advt%'` excludes `Social - WhatsApp` and `AI - ChatGPT`. So "10 conversations vs 1 lead" and "0 vs 8 ChatGPT leads" may come from labelling, not from failures.
   - **No baseline for the WhatsApp ratio.** T1-P gives SIB-04 results only as "mixed", so P's conversations-to-CRM-lead ratio is unknown.
   - **The 10 conversations include the old ads.** They cover the old ACR CTWA ads (₹1,068.11 on 2 Nov [calc 4,949.17 − 3,881.06]), and no ad-level conversation split was pulled. The claim that the plug is "not firing for the new GC05 ad" is unsupported.
   - **Attribution setting unknown.** Meta's attribution setting for "conversations started" isn't stated.
4. **Required Evidence or Fix:** Before blaming the plug or a campaign stop, pull CRM counts (aggregates only) for W and P:
   - `Lead_Source` = `Social - WhatsApp`;
   - `Lead_Source` = `AI - ChatGPT`;
   - `Advt - Facebook` with `CTWA_Click_ID` not null;
   - all of the above by `Meta_Campaign`.

   Also pull ad-level messaging conversations for W and P and state the attribution window. Reframe the §3 bullets as hypotheses pending this check. Add the classifier gap to action 4.

### 6
1. **Severity:** Major
2. **Affected Scope:** §5 Due reviews
3. **Finding:** The changelog entry "SIB-04 ads replaced (GC 05/2026)" has Review on 2026-11-09 but is missing from §5. The standard requires every due entry. The data for it exists:
   - GC05 Form: ₹4,642.93 → 11 Meta leads at ₹422.08 (T3);
   - CTWA: ₹3,881.06 with ad-level results "—";
   - CRM: SIB-04 form leads FB+IG = 9 of 11 (82%) [calc].
4. **Required Evidence or Fix:** Add a §5 row for it, with expected vs actual, a verdict (likely "Inconclusive", since it is bundled with the other SIB-04 changes, see finding 3) and its learning status.

### 7
1. **Severity:** Nit
2. **Affected Scope:** §3 Funding bullet, §6 action 1
3. **Finding:**
   - "The ₹15,000 top-up lasted ≈1 day at ₹15,000/day of budgets." In fact the credit after GST was ≈₹12,712 [calc], and actual full-day spend was ₹9,804–11,382, not ₹15,000. Budgets under-deliver by about 25–35%.
   - Action 1's ₹1,23,900 is therefore an upper bound. At actual spend (average of the full days 2, 3 and 5 Nov ≈ ₹10,662 [calc]), 7 days ≈ ₹74,633 of credit ≈ ₹88,067 payment incl. GST [calc].
4. **Required Evidence or Fix:** Show both figures, budget-based (maximum) and actual-spend-based (expected), and cite the T4/T6 GST arithmetic.

### 8
1. **Severity:** Nit
2. **Affected Scope:** §2 Blended row
3. **Finding:** The blended row mixes Instant Form, CTWA and international high-AOV objectives. SIB-05 alone is 35.2% of spend [11,921.51 / 33,898.29]. Without SIB-05 [calc]:
   - W: ₹21,976.78 / 46 CRM leads = ₹478 per lead; CPC ₹39.04 (563 clicks);
   - P: ₹11,711.01 / 44 = ₹266.

   The blended 4.0× and ₹55.66 CPC are mostly a mix effect.
4. **Required Evidence or Fix:** Add a "Blended excl. SIB-05" row.

### 9
1. **Severity:** Nit
2. **Affected Scope:** §6 action 2 evidence, §4.5
3. **Finding:**
   - The evidence for the SIB-05 pause is a performance read on n = 2 CRM leads (1 valid), which is too small to judge a high-AOV, long-cycle service. The action is only valid as enforcement of the spending cap.
   - "Saves ₹4,000/day" is the budget. Actual spend was ≈ ₹3,725/day [11,921.51 / 3.2].
   - The cap's start time isn't stated. B2 started 2 Nov 23:04, and any SIB-05 spend on 2 Nov before the rule may not count, so ₹3,078 remaining may be understated.
4. **Required Evidence or Fix:** Justify the action on the cap alone (once it is sourced, see finding 1), not on CPL. State the cap's start time. Use the actual-spend figure for the savings.

### 10
1. **Severity:** Nit
2. **Affected Scope:** §4.3 (Lists vs Interest), §3 forms → CRM, §1 provenance, §3 tracking
3. **Finding:**
   - "Comparable on cost" rests on 20 vs 6 Meta leads with no CRM QL by ad set.
   - The 94% forms→CRM match hides SIB-04 at 9/11 = 82%. The missing leads are SIB-02 1 and SIB-04 2.
   - Not stated:
     - the Meta attribution window;
     - the time zone used for Meta dates and for the COQL `Created_Time` filter;
     - Pixel/CAPI status (`meta/README.md` still says TODO; standard §3 asks for it).
   - Won deals are counted by `Closing_Date` with "W-*" stages treated as won. `business-context.md` lists that assumption as unconfirmed (TODO).
4. **Required Evidence or Fix:**
   - Label §4.3 as directional and pull CRM QL by `Meta_Ad_Set`.
   - List the missing leads by campaign.
   - Add the attribution window, time zone, and Pixel/CAPI status ("not checked" is acceptable) to §1 and §3.
   - Note the unconfirmed won-stage definition next to T9.