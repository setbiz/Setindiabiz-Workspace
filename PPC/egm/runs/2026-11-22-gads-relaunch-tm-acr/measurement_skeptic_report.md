# Measurement Skeptic report: Google Ads relaunch (Trademark + Annual Filing), design_draft v1

Reviewer: ppc-measurement-skeptic (Goldfish, read-only). Date: 2026-11-22.
Target: `design_draft.md`. Standard: `egm/standards/campaign-plan-standard.md`. Context: `shared/` (business-context, kpis, learnings, lead-source-attribution-runbook), `google-ads/` (README, changelog, audit 22 Nov, session handoff, website request).

Recomputation check: every AOV in §2 (2,300 / 5,953 / 6,568 / 12,780 / 14,647 / 15,265), every break-even CPA and CPL in §4, the 5.6× AOV ratio, and the §5 budget sums (₹42,000; 6 × ₹1,000 + 62 × ₹1,500 = ₹99,000; ₹1,41,000) reconcile with the raw numbers given. The issues are about what the numbers mean and how outcomes will be attributed, not the arithmetic.

## Findings

### MS-1 · Blocker · §6 Measurement (Tags), §7 G4, §8 cannibalisation
**Issue:** The plan says "Zoho's Lead Source workflow classifies `utm_source=google` + `cpc` → `Advt - Google` (attribution runbook)." The runbook has no such rule. In the classifier (`lead-source-attribution-runbook.md` §5, §13 and the Deluge code), `Advt - Google` comes only from the click IDs `gclid` / `gbraid` / `wbraid` / `gad_source`. The UTM rule (step 2) covers Meta sources only. A paid Google lead with no click ID in `Source_Url` / `First_Visited_URL` but a google.com referrer falls through to step 5 and becomes **`SEO - Google`**. The audit (§1) found only 6 of 84 Google leads carrying a gclid. W1 (GCLID capture) is not live, and the plan accepts "UTM-only matching" (D4).
**Effect:** The primary metric (`Lead_Source = Advt - Google`) could undercount paid leads badly. The misclassified leads would also inflate `SEO - Google`, which is the exact series the cannibalisation watch in §8 depends on. Kill rules based on "CRM leads < 10 / < 8" could fire on attribution loss rather than on performance.
**Fix:** Before launch, add a classifier rule (`utm_source=google` and `utm_medium=cpc` → `Advt - Google`) placed ahead of the organic-referrer step, or get W1 live. Change the primary-metric filter to `Lead_Source = Advt - Google` **OR** `UTM_Source = google AND UTM_Medium = cpc`. Extend G4 so the test lead carries no gclid (strip it) and must still land as `Advt - Google`.

### MS-2 · Blocker · §2 table, §4 Unit economics (Trademark)
**Issue:** The Trademark AOVs very likely include the government fee, which the caveat leaves "unconfirmed". The arithmetic points that way: fee ₹1,999 + govt fee ₹4,500 = ₹6,499, against an all-sources TM AOV of ₹6,568 and an organic AOV of ₹5,953. If `Amount` includes the ₹4,500/₹9,000 pass-through, the professional-fee AOV is closer to ₹2,000, and 50% × gross is the wrong break-even formula. Real TM break-even CPA would be about ₹1,000 or less, not ₹2,977. The day-28 kill threshold (> ₹3,000 per won) and the "continue at ₹1,500–3,000" band would then both keep a loss-making campaign running.
**Fix:** Pull 20+ won TM deals and confirm whether `Amount` includes the govt fee. Restate AOV on professional fee only, label it [data] or [est], and recompute break-even, target CPL/CPA and the day-28 bands. Do the same for AF (ROC fees are smaller but still included).

### MS-3 · Major · §7 Trademark day 28, §10
**Issue:** The day-28 decision is a sample-size and lag problem. ₹42,000 at the ₹1,500 target buys at most 28 won deals; at ₹3,000 it buys 14. The scale rule fires on "≥ 5 won", which is far below the role's ~30-event guide. Won deals are counted at day 28, so leads from weeks 3–4 have had little time to close. The plan states no lead→won lag, and the won definition (`Won` + `W-*` stages) is still a TODO assumption in `business-context.md`.
**Fix:** Define the cohort explicitly: leads created in the test window, deals won by window + N days (N taken from the CRM median TM lead→won lag, cited). Label the day-28 read as directional. Use QL rate and cost per QL as the day-28 decision metric, and confirm cost per won at day 28 + N. Confirm the W-* stage definition before launch.

### MS-4 · Major · §7 Annual Filing
**Issue:** Annual Filing has no won-based checkpoint between day 14 and 31 Jan. Up to ≈ ₹99,000 can be spent with only lead-count and CPL gates. Cost per won (≤ ₹4,000) is evaluated only after the campaign ends, so it can't stop any spend.
**Fix:** Add a cost-per-won or cost-per-QL gate on 15 Dec and 31 Dec. For example, pause if cumulative spend is ≥ ₹30,000 and won deals = 0, or if cost per QL is > ₹X, with X taken from the AF break-even CPL.

### MS-5 · Major · §4 targets vs §7 kill thresholds
**Issue:** The thresholds don't match the economics. The TM target CPL of ₹150 is above break-even at 3% lead→won (₹35–89) and needs about 5% or more even at organic AOV (150 / 2,977). The day-14 pause at CPL > ₹300 lets the campaign run at 2× target, which is ₹10,000 per won at 3%. AF is the same: the day-14 pause at CPL > ₹800 is double the target (₹400) and 3.6–4× break-even at 3% (₹192–220).
**Fix:** Set each day-14 CPL kill at or near the break-even CPL for the assumed lead→won rate, or state the lead→won rate each threshold implies and justify it.

### MS-6 · Major · §2 Conversions, §6 Event
**Issue:** The plan says "[data, 22 Nov] GA4 counting switched to once-per-session". The latest `changelog.md` entry (22 Nov) says the counting decision is still "Pending: owner decision", and that it can only be changed in GA4 property 282353741. W2 also suggests the event may fire on field interaction rather than on a real submit. This is a data label that contradicts the cited record.
**Fix:** Cite the evidence for the change (GA4 admin screenshot or connector read, with a time) or relabel it as pending. Platform conversions stay diagnostic either way, but the >30% reconciliation gap rule depends on the event being clean.

### MS-7 · Major · §6 Reconciliation, §9
**Issue:** CRM matching depends on `UTM_Campaign` = campaign name through a `{campaign}` placeholder, described as "mapping already in Zoho" without a source. There are two gaps. First, the UTM fields are documented on **Leads** (runbook §3); nothing shows they carry onto **Deals**, yet the primary metric is won deals by `UTM_Campaign`. Second, "Google clicks/form conversions vs Zoho leads" compares clicks with leads, which is not a like-for-like gap.
**Fix:** In G4, record the literal `UTM_Campaign` value captured. Define the won-deal join (Lead → converted Deal, by lead ID). Reconcile platform form conversions against CRM leads only, and report clicks separately.

### MS-8 · Major · §6 vs `shared/learnings.md`
**Issue:** The 2026-11-02 learning says "Don't relaunch without negatives, conversion import and policy-safe copy." The plan relaunches without offline import (D4) and without the shared negative list that audit §5.3 recommends ("no shared lists"). It doesn't state why the learning is being overridden or what measurement risk is accepted.
**Fix:** Name the override explicitly in §6 and §8, with the accepted risk. Make W1 + offline import a dated dependency before any scale decision, not only before switching to Maximize Conversions.

### MS-9 · Minor · §3 Ad schedule
**Issue:** The Mon–Sat 09:00–19:00 schedule is justified by Meta's 35–52% unworked rate, which is another channel. Google's own 21% never-worked figure (audit §2) is the relevant baseline. The schedule is also wider than the staffed hours in `business-context.md` (09:30–18:30). The schedule, the SLA and new keywords all change at once, so any unworked-% improvement can't be attributed to one of them.
**Fix:** Cite the Google baseline (21%), align the schedule with the staffed hours, and treat the unworked % as a lead-handling KPI, not as evidence for any one change.

### MS-10 · Minor · §7 TM day 7
**Issue:** "> 40% of spend on non-intent search terms" has no classification rule (who tags terms as intent or non-intent, and against which list). The Dec-25 79% / 7% split implies a method that isn't written down.
**Fix:** Pre-register the term-classification rule (for example the portal/DIY token list from audit §2) and the data source (search-term report, visible spend only).

### MS-11 · Minor · §5 Budget
**Issue:** "Launch day + 28 days" is 29 days (₹43,500). Google may spend up to 2× daily budget on a single day. The maximum-loss figure doesn't show how the 30.4× monthly limit interacts with the 31 Jan end date and the mid-month budget change.
**Fix:** State the cap as an explicit spend ceiling, for example a campaign total budget or an account budget of ₹1,41,000, rather than as the product of days × daily budget.

### MS-12 · Minor · §2 Current state
**Issue:** The "two Dec-25 campaigns … brought 84 CRM leads" figure uses a 12-month lead window (1 Nov 25–22 Nov 26). Per audit §2, only 76 of the 84 were created Dec 25–Jan 26, so not all 84 can be attributed to those two campaigns.
**Fix:** Say "84 `Advt - Google` leads in 12 months (76 in Dec–Jan)", with the COQL date range.
