# ppc_performance_critic report: weekly review w/e 2026-11-08

Raw output from the isolated Goldfish subagent (read-only), 9 Nov 2026.

**ppc-performance-critic: REVIEW of `PPC/egm/runs/2026-11-09-weekly/weekly_review.md`**
Against `PPC/egm/standards/weekly-review-standard.md`. Verdict: **FAIL: 1 Blocker, 9 Major, 6 Nit.**

I re-checked every [calc] in the scorecard, §3, §4 and §6 against `data.md`. They are all arithmetically correct. The problems are numbers with no source, a missing due review, wrong delivery-day maths, and diagnoses or exposures the data supports but the review leaves out.

---

**1. Severity: Blocker**
- **Affected Scope:** Header ("Every number is in `data.md`"); §2 target ₹176; §4.5, §6 #2 and §7.2 (SIB-05 ₹15,000 cap, ₹3,078 remaining, AOV ₹86,300, 8.8% break-even); §4.7 ("≈51% of lost deals to the sales process"); §3 ("`sib_wa_lead` plug, Cowork change logs 7–15 Oct").
- **Finding:** None of these numbers is in `data.md`, `PPC/shared/`, `meta/README.md` or `meta/changelog.md`.
  - `kpis.md` still says ₹130–135, and the "2 Nov audit" is not cited by path.
  - The ₹15,000 SIB-05 cap is the only stated reason for action #2, a campaign pause. It appears nowhere in the changelog.
  - Every "vs target" multiple (1.7×, 2.1×, 6.0×, 4.0×) depends on the ₹176 figure, which has no source.
  - The standard says an unsourced number is a Blocker, and the header's claim of full sourcing is false.
- **Recommended Fix:**
  - Add the file path for the 2 Nov audit and the 2 Nov owner resolution next to each figure, and copy the figures into `data.md` as new tables (e.g. T11 targets, T12 owner rules).
  - If no file records the SIB-05 cap, log it in `meta/changelog.md` before action #2 relies on it. Otherwise base action #2 only on T2/T3/T8 (₹11,921.51 → 2 CRM leads, 1 QL; B2 ₹9,449.53 → 1 lead).
  - Label the 51% and the WA-plug references as unverified, or cite where they come from.

**2. Severity: Major**
- **Affected Scope:** §5 Due reviews ("No other changelog has a due 'Review on' date").
- **Finding:** This statement is false. The `meta/changelog.md` entry "SIB-04 ads replaced (GC 05/2026)" has **Review on 2026-11-09** and is missing from the table. The data to judge it is already in the inputs:
  - The GC05 Form ad got 11 leads at ₹422.08 (T3). The `learnings.md` baseline from 2 Nov is Form ₹21,559 / 59 = ₹365 per lead [calc].
  - The WhatsApp ad set cost ₹494.92 per conversation started (T2). The baseline is ₹17,449 / 52 = ₹336 per chat [calc].
  - So the new creative is running 16–47% worse than the old baseline. That baseline was itself measured without layer-2 targeting.

  The SIB-04 rows that are in the table are confounded. On 2 Nov SIB-04 got reactivation, layer-2 targeting, an age change to 25–55, a full creative swap and the `GST - Company` audience at the same time. That is at least 4 structural changes, so a separate "Inconclusive. Extend" verdict on the age change alone can never be read. "Age breakdown not pulled" is a one-call gap.
- **Recommended Fix:**
  - Add the GC05 row with the numbers above.
  - Merge the SIB-04 rows into one bundled verdict ("2 Nov SIB-04 relaunch package").
  - Pull the Meta `age` breakdown for both SIB-04 ad sets for 2–8 Nov. Report the 46–55 band's spend and leads, which is the only evidence for or against the age change.

**3. Severity: Major**
- **Affected Scope:** Headline ("about 3.2 days of full delivery", "dark since 6 Nov 06:52"); §3 Funding; §4.1.
- **Finding:** By the review's own data, 3 Nov and 5 Nov were cut short by funding.
  - 4 Nov billed ₹1,893.14 + 6 Nov billed ₹10,818.72 = **₹12,711.86 = ₹15,000 ÷ 1.18 exactly** (T6) [calc]. The ₹15,000 UPI top-up was used up to the paisa during 5 Nov.
  - Likewise, 2 Nov + 3 Nov spend was ₹21,186.43, which × 1.18 = ₹25,000 [calc]. That implies a ₹25,000 top-up on 2 Nov before the T6 window, which also ran out on 3 Nov. This is an inference: the top-up is not in T6.
  - So at most one day (2 Nov) ran without a funding limit, and 2 Nov was also the creative-swap day. "06:52" is a billing timestamp. The account stopped delivering on 5 Nov.
  - Intra-day cut-offs push delivery into the early hours, which also skews the CPM and CTR comparison with P.
- **Recommended Fix:**
  - Correct the headline: "≈1 uncapped day; 3 and 5 Nov were cut off when credit ran out".
  - Tell the owner plainly that a ₹15,000 top-up buys ≈₹12.7k of delivery, under one day at current budgets.
  - Define "7 funded days" as 7 days with **no** intra-day cut-off, and check it with an hourly spend breakdown.

**4. Severity: Major**
- **Affected Scope:** §2 target column; §6 #3; §7.3 (SIB-01); SIB-02 marked "best" at 1.7×.
- **Finding:** One blended ₹176 target hides service-level economics that are in the inputs.
  - **SIB-01:** `meta/changelog.md` (2 Nov) gives 90-day "#IND 1" 7 won / 687 leads, ₹30,368 won on ₹1,20,202 spend = **0.25×**, at ≈₹175 per lead [calc].
    - Cost per CRM lead has since doubled to ₹366 (T1/T7).
    - The owner's unlogged ₹1,250 → ₹2,500 restore is also a **+100% budget jump**, well past the ~20–30% safe step, so it resets learning.
    - Action #3 would keep spending ₹2,500/day for 7 days on a campaign whose last-known return is ₹0.25 per ₹1.
  - **SIB-02:** paid trademark won deals average ₹2,000 (W: ₹4,000 / 2) and ₹2,500 (P: ₹5,000 / 2) (T9). At ₹293 per CRM lead and 50% margin, break-even lead→won = 293 ÷ (2,000–2,500 × 0.5) = **23–29%** [calc]. Facebook's baseline is 3.7% (`business-context.md`).
- **Recommended Fix:**
  - Add a per-campaign break-even CPL column: AOV × margin × lead→won, with AOV from 90-day T9-style data per `Meta_Campaign`. Caveat it as directional (small n, deal Amount definition unconfirmed).
  - In §7.3, put the 0.25× figure in front of the owner. The data-backed default is to revert SIB-01 to the approved ₹1,250 as the one change.
  - Flag that SIB-02's real economics may be worse than SIB-01's despite the lower CPL.

**5. Severity: Major**
- **Affected Scope:** §4.2 (layer-2 diagnosis); standard §4 (actual drivers).
- **Finding:** The hypothesis that higher CPMs drove the CPL rise is mostly contradicted by the review's own data. The main driver is a drop in click→lead conversion.
  - **SIB-01:** CPM ₹273 → ₹308 (+13%) [calc T1/T1-P], CTR 1.16% → 0.89%. Click→lead fell from 24/146 = 16.4% to 11/116 = 9.5%. So CPL × 2.56 ≈ CPC × 1.47 times a conversion-rate drop of × 1.74.
  - **SIB-02:** CPM ₹229 → ₹349 (+52%). Click→lead fell from 17/72 = 23.6% to 26/187 = 13.9%.
  - The SIB-02 comparison is also confounded. P was a different entity ("SIB-02 Trademark - Copy", ₹1,307.62 base), and the 2 Nov Trademark rebuild added the Lists ad set and new ads (changelog).
  - No placement, age, region, audience-size or form-type driver was pulled, which the standard requires.
- **Recommended Fix:**
  - Rewrite §4.2 around the conversion-rate drop.
  - Pull `publisher_platform` + `platform_position`, `age`, `region` and the ad set audience size (delivery estimate) via the Meta connector for W and P.
  - Check whether the instant form or its type changed on 2 Nov.
  - Label the SIB-02 W vs P comparison as not like-for-like.

**6. Severity: Major**
- **Affected Scope:** §5 layer-2 row; §6 #1 and #6 (refund, then hold for 7 funded days).
- **Finding:** The review asks for ₹90,860–₹1,23,900 to finish a test that has no quality baseline, no success threshold and no stop-loss.
  - The test's premise is "higher quality", but no P-cohort Lead_Status at the same lead age is shown.
  - The changelog says SIB-01 quality should be judged on the Zoho **TL/RM Lead Quality fields**. The review uses Lead_Status only.
  - Among leads already worked, quality looks high: SIB-02 13/17 = 76% and SIB-01 5/6 [calc T8]. Neither number is used.
- **Recommended Fix:**
  - Pull Lead_Status and TL/RM Lead Quality for the 2-week cohort before 2 Nov as a baseline.
  - Write pass/fail criteria into §5 before refunding, e.g. "keep layer-2 on an ad set if cost/QL ≤ break-even QL cost from finding 4". Add a stop-loss: after 4 uncapped days, if cost/QL > 2× that threshold, revert layer-2 on that ad set only.

**7. Severity: Major**
- **Affected Scope:** §6 #1 and #6 (refund and hold SIB-02 Lists and the SIB-04 director/GST lists); §7.
- **Finding:** The ad set the review calls SIB-02's main engine is a customer-list audience: ₹5,754.87 = 78% of SIB-02 spend, at ₹3,000/day, the largest non-SIB-05 budget (T2). SIB-04 targets Company Director and `GST - Company` lists, and a "custom-audience refresh" was done on 2 Nov (changelog).
  - `learnings.md` (2026-10-18) records that customer-list audiences need consent.
  - Workspace rules forbid list use without a recorded source, notice, purpose and approver, and the website notice ("used only to respond to your enquiry") does not cover ad targeting.
  - The review refunds and holds these ad sets without raising any of this. Under the standard's §7, anything touching compliance must go to a human.
- **Recommended Fix:** Add to §7: "Confirm a recorded source, notice, purpose and approver for each list in SIB-02 Lists and the SIB-04 audiences before funds resume. If not, switch those ad sets to their non-list interest equivalent." Governing provisions:
  - In force now: IT Act 2000 s. 43A with the SPDI Rules 2011 r. 4 and r. 5, Consumer Protection Act 2019 s. 2(47), and Meta's Custom Audience Terms.
  - From ≈13 May 2027: DPDP Act 2023 ss. 4–6 and 8 under the DPDP Rules 2025 phased commencement.
  - Check applicability and the current commencement status on meity.gov.in.

**8. Severity: Major**
- **Affected Scope:** Live ads in T3: "TM-F1 | Rs1999 + GST", "INC-F1 | Rs2499 + GST", "SIB-05 | S1 | From USD 499".
- **Finding:** These ads quote fixed prices (the price is in the ad name). `business-context.md` (2 Nov site fetch) says "No package prices are published… Ads must not quote a fixed price unless one is added to the landing page."
  - That is a mismatch between the ad and the landing page.
  - It is also a likely reason for the low-value trademark deals: W won AOV is ₹2,000 (T9), so the price-led ads are probably drawing price shoppers.
  - The review does not mention it.
- **Recommended Fix:** Check whether the landing page or instant-form intro now shows the same price and says statutory or government fees are extra. If not, add it to §7 as a compliance item: Consumer Protection Act 2019 s. 2(28), and the CCPA Guidelines for Prevention of Misleading Advertisements, 2022. Hidden or "drip" fees also fall under the CCPA Guidelines for Prevention and Regulation of Dark Patterns, 2023. Confirm each is the current version.

**9. Severity: Major**
- **Affected Scope:** §3 ChatGPT Ads; §6 #7.
- **Finding:** The review offers only the cheap explanation ("stopped or budget exhausted"). The expensive one is that campaigns are still spending while CRM tagging is broken.
  - `learnings.md` (2026-10-09): 3 campaigns at ₹500/day each, about ₹10,500/week if still live [estimate].
  - The channel has 54 CRM leads and 0 won deals lifetime (`business-context.md`), and 0 CRM leads in W.
  - None of this exposure is sized.
- **Recommended Fix:**
  - Move this to §7 with the ₹10,500/week estimate.
  - The owner should check the ChatGPT Ads dashboard for W spend today. If it is spending, pause it until it reconciles with CRM; a pause is a human decision.
  - Keep the Supermetrics/CSV fix as a separate follow-up.

**10. Severity: Major**
- **Affected Scope:** §3 Tracking health; whole review (bid strategy and learning status).
- **Finding:** The standard's §3 requires tag/CAPI status, and none is given; `meta/README.md` still says "Pixel + CAPI status: TODO verify".
  - The review never states any ad set's optimisation goal, bid strategy or learning-phase status.
  - SIB-05 shows Meta results "n/a" at campaign level and on all 3 ad sets, at ₹3,573–₹3,879 CPM (T1/T2). Nobody has checked what it is optimising for.
  - At 2–20 leads per ad set per week, every ad set is likely Learning Limited. That makes "extend to 7 days" unlikely to produce a stable read.
- **Recommended Fix:**
  - Pull `optimization_goal`, `bid_strategy` and learning stage for all 8 ad sets.
  - If SIB-05 continues, merge it into one ad set optimising for leads under the ₹4,000 CBO.
  - Add CAPI status and whether CRM stages are sent back to Meta. A CRM-feedback lead goal (conversion-leads optimisation) is a bigger quality lever than the layer-2 targeting.

**11. Severity: Nit**
- **Affected Scope:** §6 ranking.
- **Finding:** Action #5 (21 unworked paid leads × ₹706 ≈ ₹14.8k of leads already paid for [calc]) ranks below #3, a logging and process item. The standard asks for ranking by expected impact.
- **Recommended Fix:** Move #5 to #2 or #3.

**12. Severity: Nit**
- **Affected Scope:** §2 Scorecard.
- **Finding:** The CPA column required by standard §2 is missing. P revenue/spend of 1.61× (₹27,369 / ₹16,949 [calc]) isn't shown next to W's 0.21×.
- **Recommended Fix:** Add CPA as "n/a (2–4 week lag)" or show a lagged figure with a caveat, and show both revenue/spend ratios.

**13. Severity: Nit**
- **Affected Scope:** §6 #1 (18% GST).
- **Finding:** The 1.18 factor isn't sourced in the review. The T6 billing figures prove it (₹15,000 → ₹12,711.86 of credit).
- **Recommended Fix:** Cite that derivation. Workspace rules require a cited legal provision for any compliance statement, so if the tax rate is stated, cite the applicable IGST rate notification for advertising services.

**14. Severity: Nit**
- **Affected Scope:** §3 WhatsApp; §6 #4.
- **Finding:** "10 conversations started" vs 1 CRM lead may mean chats that were never answered (lost leads), not only lost attribution. "Conversations started" is also not a lead count.
- **Recommended Fix:** First count the chats received in the WhatsApp Business inbox for 2–8 Nov, then run the end-to-end CTWA test.

**15. Severity: Nit**
- **Affected Scope:** §6 #1 ("consider a payment method").
- **Finding:** This is vague after 3 interruptions in 14 days. Also, per Meta's learning-phase guidance (verify current wording), ad sets that stay inactive 7+ days re-enter learning, which could happen if funds are not added by about 12–13 Nov.
- **Recommended Fix:** Name the option: an automatic card payment method if available on the account, or a prepaid buffer of at least 7 days at budget. Set a top-up deadline of 12 Nov.

**16. Severity: Nit**
- **Affected Scope:** §6 #2 (pause SIB-05).
- **Finding:** `learnings.md` (2026-01-18) notes a business-hours ON rule with no #HOLD exclusion that can restart paused campaigns. T6 shows no status changes after 2 Nov, so the rule is probably inactive, but that is unverified.
- **Recommended Fix:** List the account's automated rules before relying on the pause, and add the #HOLD exclusion if any rule targets SIB-05.