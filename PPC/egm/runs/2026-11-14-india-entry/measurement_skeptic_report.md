# Measurement Skeptic report: India Entry (FDI) US plan, design_draft v1

_Goldfish reviewer: `ppc-measurement-skeptic`. Target: `egm/runs/2026-11-14-india-entry/design_draft.md`. Context read: `egm/standards/campaign-plan-standard.md`, `reports/cross-platform/2026-11-14-india-entry-diagnosis.md`, `shared/lead-source-attribution-runbook.md`, `shared/kpis.md`, `shared/business-context.md`. Read-only: no ad-platform or CRM tool was called. `[calc]` = my arithmetic on numbers in those files._

**Verdict:** not ready to launch. The primary metric (CPQL) cannot be computed reliably per platform as written: the QL definition and the Zoho attribution path both break for several platforms. The kill and scale rules also act on samples too small to separate signal from noise.

Severity scale: Blocker / Major / Minor. (The persona calls the lowest level "Nit"; I use "Minor" as instructed.)

---

## Blockers

### B1. The QL definition reads a status snapshot, and gate G-T1 changes that snapshot
1. **Severity:** Blocker
2. **Affected scope:** §6.1 primary metric; §6.3 item 1; §7 K1, K2, S1
3. **Finding:** CPQL = spend ÷ leads "with Lead_Status in (Valid Lead, Proposal Sent)". That is the status at the moment someone reads it, not a record that the lead ever qualified. Three things push qualified leads out of the count:
   - **Gate G-T1 requires leads to be converted into deals.** Once a lead is converted (`Converted__s` = true), it is no longer an open lead with status Valid or Proposal Sent. So the best outcome, a lead becoming a deal, removes it from the numerator.
   - A lead that reached Proposal Sent and was later marked Lost drops out.
   - Leads that were never worked also stay out. In SIB-05, 4 of 8 leads were unworked (diagnosis §2a). The metric then partly measures sales follow-up speed, not the platform.

   Example: SIB-05 US has 3 QL, 1 of them at Proposal Sent. If that lead is converted to a deal, the US CPQL moves from ₹4,454 to ₹6,681 (13,361.78 ÷ 2) [calc], and the closest thing to a win has made the channel look worse.
4. **Required fix:** Define QL as "**ever** reached Valid Lead or Proposal Sent, or was converted to a deal", taken from Zoho field history or from a stamped date field (for example `QL_Date__c`, set by a workflow when the status first enters that set and never cleared). Measure CPQL on a cohort: leads created between day 1 and day N, read at day N+7 so they have time to mature. Report unworked leads as a separate number, and do not let any K rule fire while unworked leads are more than 20% of a platform's leads.

### B2. Zoho attribution will send several platforms' paid leads into organic or blank buckets
1. **Severity:** Blocker
2. **Affected scope:** §6.2 table; §6.3 items 2, 5, 7; §11.3 and §11.7; §9.4
3. **Finding:** CPQL per platform depends on `Lead_Source`. Checked against the live classifier rules (runbook §5):
   - **LinkedIn Lead Gen Form leads** arrive with no URL, no referrer and no `li_fat_id`. The classifier has a branch for Meta form leads (`Meta_Ad_Type`) but none for LinkedIn. The workflow's trigger conditions also may not be met, so these leads end up with a blank source or whatever the integration writes. §6.2 also leaves the integration undecided ("LinkedIn–Zoho CRM integration **or** LeadChain").
   - **Website clicks that arrive with UTMs but no click ID** fall through. `li_fat_id` and `rdt_cid` are appended only when the platform's click-ID setting is switched on. Without them, `utm_source=linkedin` is caught only by the referrer rule and becomes **Social - LinkedIn** (organic). Reddit does not appear in the referrer rules, so it becomes **Referral - Web**. The classifier does not read `utm_medium=cpc` anywhere.
   - **Zoho Bookings link** (the main call to action in §6.4, §11.2 and §11.7): bookings come in as `SEO - Zoho Booking`, and the guard in runbook §5 forbids overwriting that value. Every ad visitor who books directly is counted as SEO.
   - **WhatsApp, email and phone contacts** listed on the landing page (§11.7) carry no click ID. They become Social - WhatsApp, Direct or blank. In the baseline, 6 of 20 won deals already have a blank source.
   - **`Advt - ChatGPT` is not in the 38-value picklist** (runbook §2). The plan only says "add if missing". Until it is added, paid ChatGPT traffic is classified as `AI - ChatGPT` (runbook §5 step 4).
4. **Required fix:** Before gate G-T can pass:
   - (a) Add a LinkedIn form-lead branch to the classifier, keyed on an integration field such as `LinkedIn_Campaign`/`LinkedIn_Form_ID`, and name the single integration to use.
   - (b) Add rule 1b to the classifier: if `utm_medium=cpc` (or `paid`) and `utm_source` is linkedin, reddit, chatgpt or bing, map to the matching `Advt - *` value, ahead of the AI, organic and social rules.
   - (c) Give ad traffic its own Bookings link (a separate booking page, or UTM pass-through into a hidden field) so it is not stamped `SEO - Zoho Booking`. Alternatively, exclude bookings from the guard when `UTM_Medium=cpc`.
   - (d) Turn on click-ID appending in LinkedIn and Reddit, and verify it.
   - (e) Add `Advt - ChatGPT` to the picklist on Leads, Deals and Contacts.
   - (f) Change the §6.3 item 2 test: one test conversion per platform **and per contact path** (form, booking, chat), each confirmed with the expected `Lead_Source` in Zoho. Record the results in the run folder.

---

## Major

### M1. The "realistic maximum loss ≈ ₹1,05,000" is wrong
1. **Severity:** Major
2. **Affected scope:** §5 maximum loss; §7 closing line
3. **Finding:** K1 fires only when a platform has **0 QL**. A platform with one QL is never stopped by K1. Google can spend its full ₹1,20,000 with 1 QL (CPQL ₹1,20,000) and nothing stops it before day 30, because K2 is assessed on day 30. The same is true on every platform. So ₹1,05,000 is a best case for the scenario where every platform gets exactly zero QL. It is not a maximum, and labelling it `[calc]` makes it look more certain than it is. The ₹95,000 + ₹10,000 sum is correct for that scenario. The ₹10,000 "K0 losses" figure has no derivation.
4. **Required fix:** State the maximum loss as ₹3,00,000. Add a running-CPQL rule that does not wait until day 30, for example "K1b: spend ≥ 2 × break-even CPQL (₹15,534) per QL to date, after ≥ ₹30,000 spend → pause". Recompute the realistic loss under that rule, or drop the "realistic" figure. Show the working for the ₹10,000 K0 figure or remove it.

### M2. The kill and scale rules act on samples too small to tell signal from noise
1. **Severity:** Major
2. **Affected scope:** §7 K1, K2, S1; §5 caps for Microsoft, ChatGPT and Reddit; §3 P3 and §4 "Reference"
3. **Finding:**
   - **S1 scales on 3 QL.** With 3 events, the exact 95% Poisson interval for the count is 0.62 to 8.77. At a measured ₹6,000 CPQL (₹18,000 spend for 3 QL), the true CPQL could plausibly be anywhere from ₹2,050 to ₹29,000 [calc]. The plan also cites Meta's ₹4,454 per US QL (n = 3) as the reason to fund Meta, with the same uncertainty.
   - **Some platforms can never reach a decision.** At the target CPQL, the month-1 caps can produce at most: Microsoft ₹25,000 → 4.2 QL; ChatGPT ₹20,000 → 3.3; Reddit ₹15,000 → 2.5 (after a 3-week delay, so it runs only about 10 days of the 30) [calc]. None can produce a statistically meaningful CPQL by day 30. Reddit's K1 threshold equals its entire cap.
   - **K1 at ₹15,000 is a coin-flip-adjacent test.** If a platform's true CPQL equals break-even (₹7,767), expected QL at ₹15,000 is 1.93 and P(0 QL) = e^-1.93 ≈ 14.5% [calc]. Even a platform performing at target (₹6,000) has a ≈ 8% chance of zero QL [calc]. Across 6 platforms, one or more false kills is likely: 1 − 0.92^6 ≈ 39% [calc] if all were at target.
4. **Required fix:**
   - Label all day-30 reads on fewer than about 10 QL per platform as **directional**.
   - Change S1 to at least 8 QL and CPQL ≤ ₹6,000, or require the upper confidence bound to be below break-even.
   - Either consolidate the small platforms (fund Microsoft, ChatGPT and Reddit sequentially, not in parallel), or call them "feasibility checks" whose only success test is capture and QL > 0, not CPQL.
   - Write the false-kill risk next to K1, or raise K1 to about ₹23,000 (3 × target), where P(0 | at target) ≈ 2% [calc].

### M3. K1 and K2 ignore the time it takes a lead to become qualified
1. **Severity:** Major
2. **Affected scope:** §7 K1, K2; §6.4 SLA
3. **Finding:** A lead is not a QL until sales has contacted it and updated its status. The SLA is 4 working hours IST, so a US lead that arrives overnight IST is not contacted until the next IST working day. Some leads need several contact attempts. In SIB-05, half the leads were still unworked after 3 weeks. K1 can therefore fire on "0 QL" while qualifiable leads are sitting unworked. K2 on day 30 counts leads created on day 29 that cannot have matured yet.
4. **Required fix:** K1 and K2 should count only leads older than 5 working days, and only once each of those leads has been worked at least once (status ≠ blank or Establishing Contact). Add a capacity metric, "unworked > 48 h", to the weekly reconciliation. Treat a platform with unworked leads as **not evaluable** instead of killing it.

### M4. Google bidding plan: the conversion actions, the switch rule and the offline import do not work as written
1. **Severity:** Major
2. **Affected scope:** §9.1 bidding; §6.3 item 3
3. **Finding:**
   - **The switch rule is ambiguous.** "Maximize clicks … for the first 14 days or 15 conversions, then Maximize conversions on IE – Qualified lead" does not say whichever comes first, or which conversion action counts toward 15. The implementer has to decide, which fails the standard ("A build sheet that leaves a decision to whoever implements it").
   - **There will not be enough qualified-lead conversions to bid on.** At ₹4,000/day and target CPQL, Google produces at most about 20 QL a month [calc], and offline imports arrive days after the click. Bidding on so few QL conversions is unlikely to stabilise. Switching strategy around day 14 also resets learning in the middle of the 30-day read, so days 1–14 and days 15–30 are different regimes.
   - **Offline import may not work.** Zoho's Google Ads integration and offline uploads need the `gclid` in a dedicated field that also exists on the Deal. Today `gclid` sits only inside the `First_Visited_URL` text. That is a website-type field that is not COQL-selectable (runbook §10), and runbook §10 notes that Deals do not carry the URL fields. G-T1's "deals must keep click IDs" has no defined mechanism.
   - **"IE – Website lead" has no firing scope.** The Dec-25 defect was a conversion action that did not match CRM leads (diagnosis §3). The plan does not say which forms or pages fire this action.
4. **Required fix:**
   - Keep one bid strategy for the whole 30-day test: Maximize clicks with max CPC ₹700, or Maximize conversions on "IE – Website lead" fired only on the India-entry form-success event. Import QL and Won as **secondary** conversions (observe only) until there are at least 30 QL in 30 days.
   - Add `GCLID`/`MSCLKID` single-line fields on Leads, filled by a hidden form field, and map them lead → deal on conversion.
   - Specify the trigger for "IE – Website lead": page path and form ID.

### M5. Several overlapping changes and a holiday period mean results cannot be credited to any one cause
1. **Severity:** Major
2. **Affected scope:** §5 duration; §3 phases; §9 LP note; §9.3 form v2; §9.1 bid switch
3. **Finding:** The 30-day window starts in late November 2026. It covers US Thanksgiving (26 Nov 2026), the Christmas–New Year period, and Q4 budget freezes, when US B2B decision-makers are least responsive. Inside the same window, the plan also changes several things:
   - staggered launches in weeks 1, 2 and 3;
   - a swap from the interim landing pages to the rewritten ones "until the new page is live";
   - Meta form v2;
   - the Google bid-strategy switch;
   - a new booking flow;
   - widening the booking email to all India-entry sources.

   A CPQL that is poor (or good) on day 30 cannot be credited to any single platform, page or change. There is also no year-ago baseline for comparison, because there was no paid US India-entry activity.
4. **Required fix:**
   - Freeze landing pages, forms and bidding for the test window. Launch only after the new page is live, or record the swap date and report CPQL before and after it separately.
   - Note the US holiday effect in §5, and either extend the decision date to day 45 or exclude 24 Dec – 1 Jan from the K2 read.
   - Log every change with a date in each platform's `changelog.md`, and annotate the weekly reconciliation with them.

### M6. Unit economics: the AOV and the 15% close rate may not describe ad-sourced US leads
1. **Severity:** Major
2. **Affected scope:** §4 (AOV, QL→won, break-even); §11.4 price block
3. **Finding:**
   - **The AOV may not apply.** The ₹86,300 AOV comes from Product Cat "FDI" deals. 18 of 20 have Country "India", and there is no lead conversion, so their acquisition path and service mix (new entity setup vs FDI compliance filings) are unknown (diagnosis §1). Meanwhile the ads and landing page lead with "From USD 499", which is roughly ₹42,000–45,000 [est, FX not stated in the plan]. If ad-sourced deals close near the advertised price, margin per deal falls to about ₹25,000–27,000. Break-even CPQL would then be about ₹3,800–4,000 at 15% close, below the ₹6,000 target [calc].
   - **The close rate has no stated basis.** The 15% QL→won figure is labelled an estimate, but no reasoning is given. `kpis.md` has a paid lead→won baseline of 3.7%, but that is domestic and low-ticket.
   - **K2 lets losses run well past break-even.** K2 tolerates CPQL up to ₹12,000 (155% of break-even) with no rule for the ₹7,767–₹12,000 band.
4. **Required fix:**
   - Add a sensitivity table: break-even CPQL at close rates of 10%, 15% and 25%, crossed with AOV of ₹45,000 (entry price) and ₹86,300.
   - Pull the median and distribution of FDI deal value for **new-entity** deals only, with source and date.
   - Set K2 at break-even (₹7,767), or justify ₹12,000 explicitly with the open-proposal exception.
   - State the FX rate and date used for the USD figures.

### M7. Weekly reconciliation has no mismatch threshold, and the SEO cannibalisation check cannot detect anything
1. **Severity:** Major
2. **Affected scope:** §6.5; §7 K0; §8 "Cannibalising SEO"
3. **Finding:**
   - **Partial capture failures go unnoticed.** K0 fires only when capture is 0. Losing 40% of leads, or attributing them to the wrong source (see B2), triggers nothing.
   - **Platform-reported numbers are not addressed.** §6.5 does not say that platform-reported conversions must not be used for decisions. LinkedIn and Meta count view-through conversions by default, and Google counts modelled conversions.
   - **The SEO check has no baseline.** The check is "organic India-entry leads should not drop", but there is no number and no threshold. The baseline is 24 SEO - Google FDI leads in 12 months, about 2 a month (diagnosis §1). A drop cannot be told apart from noise within 60 days.
4. **Required fix:**
   - Add **capture rate** to the weekly reconciliation: Zoho `Advt - <platform>` leads ÷ platform-reported form leads. Pause if it falls below 90% for 2 consecutive weeks. Also report the share of India-entry leads with a blank or Direct source, and investigate if it rises.
   - State that all decisions use CRM data only, and that platform conversion columns are shown for reference with their attribution window named.
   - For SEO, state the baseline (24 per 12 months, 2026 trailing figure) and make it explicit that the check is a guardrail only, unable to detect changes under about 50%.

### M8. Platform-access status in §2 contradicts the diagnosis it cites
1. **Severity:** Major
2. **Affected scope:** §2 "Platform access"; §6.5 (reconciliation depends on these connections)
3. **Finding:** The draft says LinkedIn, X and Reddit are "connected in Supermetrics" and cites the diagnosis. The diagnosis (§4, same date) lists LIA, TA and RDA as **Not authenticated**. Either the draft has a newer source it does not cite, or the claim is wrong. Weekly CPQL reconciliation for LinkedIn and Reddit depends on these connections.
4. **Required fix:** Cite the source and time of the reconnection (for example, a Supermetrics `data_source_discovery` result on 14 Nov after the diagnosis). Otherwise mark LinkedIn and Reddit reporting as blocked and add "connector authenticated" as an item in gate G-T.

### M9. Meta setup repeats the volume-optimisation bias that wasted SIB-05 spend
1. **Severity:** Major
2. **Affected scope:** §9.3; §3 P3
3. **Finding:** The diagnosis found that Meta's lead-volume optimisation moved spend to the cheapest-CPM segment (UAE: 39.5% of spend, 0 QL). The rebuild keeps lead-volume optimisation but changes two things:
   - It puts two very different audiences (company expansion, age 30–65; returning founders, age 25–50, with Advantage+ audience expansion) under **CBO**. CBO will fund whichever produces cheaper form leads, likely the broader returning-founder set, so the per-ad-set CPQLs will be built on very uneven spend.
   - The optimisation event is not stated: form leads, or the CAPI ValidLead/QualifiedLead events from §6.3 item 6.
4. **Required fix:** Use ABO with fixed budgets per ad set (for example ₹900 / ₹600), or run two campaigns. State the optimisation event explicitly: "Leads (Instant Form)" now, with "conversion leads" optimisation on the CAPI QualifiedLead event once the volume threshold is met. Switch off Advantage+ audience expansion for the test, or report its spend separately.

---

## Minor

### N1. Placement waste figure does not add up
- **Severity:** Minor. **Scope:** §9.3 ad set 1.
- **Finding:** "Stories and Instagram Feed excluded: ₹8,056 for 0 leads". From diagnosis §2d: 4,643.37 + 1,836.81 + 1,769.37 = **₹8,249.55** [calc].
- **Fix:** Correct the number and cite diagnosis §2d.

### N2. Market-sizing and CPC support is loosely sourced
- **Severity:** Minor. **Scope:** §2 keyword demand; §3 P2.
- **Finding:**
  - "≈600–700 high-intent searches" does not show its sum. All listed terms total 710; excluding the informational "doing business" and "how to start" terms gives 580 [calc].
  - The bid ranges are "INR assumed". The ₹700 and ₹400 max CPCs depend on that assumption.
  - "₹42 CPC on India Entry" (Microsoft) comes from a multi-country "Overseas" campaign with 109 clicks. It is not evidence of US CPCs.
- **Fix:** Show the arithmetic, confirm the account currency in Google Ads settings, and label the Microsoft CPC "non-US, n = 109 clicks".

### N3. The Meta reference figure is cited without its context
- **Severity:** Minor. **Scope:** §2, §3 P3, §4 Reference.
- **Finding:** ₹4,454 per US QL is quoted, but the blended ₹13,741 per QL, n = 3, and the diagnosis's "directional" label are not. "US" mixes Meta delivery country with the parent-company country from the form (diagnosis §2c).
- **Fix:** Quote both figures, say which country basis is used, and mark the figure as directional.

### N4. GST treatment of spend is not defined consistently
- **Severity:** Minor. **Scope:** §5, §6.1.
- **Finding:** Budgets are stated excluding GST. The CPQL numerator ("platform spend") is not defined: platform-reported spend, or invoiced spend including 18% GST. Break-even also assumes an AOV basis that is not stated (excluding GST?).
- **Fix:** Define both as excluding GST, from platform-reported spend.

### N5. "Verified" tracking has no test procedure
- **Severity:** Minor. **Scope:** §6.3 items 4, 5, 7; §9.2 gate.
- **Finding:** Microsoft recorded 0 conversions against 46 CRM leads (diagnosis §3), but the plan only says "UET verified".
- **Fix:** Define the pass test: tag status "Active" in the platform, one test conversion recorded in the platform within 24 h, and the matching Zoho lead carrying the expected click ID and `Lead_Source`. Save a screenshot or log line per platform.

### N6. The day-60 won read has no cohort or lag definition
- **Severity:** Minor. **Scope:** §5 duration; §10 Review 3.
- **Finding:** The time from lead to won is unmeasured for FDI (no conversions exist). A deal won on day 60 may come from a lead created on day 55 or day 2.
- **Fix:** Define the cohort as leads created on days 1–30, with won status read on day 60 and again on day 90. Record days-to-won for every paid deal, so the lag can be measured for the next plan.
