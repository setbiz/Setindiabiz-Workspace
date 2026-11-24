# Goldfish Review: PPC Performance Critic (Hostile Media Buyer)

- **Target:** `PPC/egm/runs/2026-11-14-india-entry/design_draft.md` (DRAFT v1)
- **Standard:** `PPC/egm/standards/campaign-plan-standard.md`
- **Context read:** `shared/business-context.md`, `shared/kpis.md`, `shared/learnings.md`, `shared/budget-plan.md`, `shared/landing-pages.md` (empty), `reports/cross-platform/2026-11-14-india-entry-diagnosis.md`, `meta/history/chatgpt-import-part1.md` (automated-rule scope only)
- **Reviewer date:** 2026-11-14. No ad platform or CRM was queried.
- **Labels:** `[calc]` = my arithmetic on numbers in the plan or diagnosis. `[est]` = my estimate (industry rule of thumb, not account data). Severity scale: Blocker / Major / Minor (Minor = the persona's "Nit").

---

## Finding 1
1. **Severity:** Blocker
2. **Affected Scope:** §9 Build sheet (9.1 cap method, 9.3 Meta ads and targeting, 9.4 LinkedIn ads, 9.5 ChatGPT ads, 9.6 Reddit); §9 intro vs §6.3 gate G-T items 2 and 8
3. **Finding:** The build sheet leaves decisions to whoever builds it, which the standard lists as a failing condition. No data needed; these are gaps in the plan:
   - **No verbatim copy for 7 of the planned ads.** Meta F1, R1, R2; LinkedIn L1, L2; Reddit R1 (which reuses Meta R1). All say "brief to follow". The ChatGPT ad text is "from 9.1 descriptions" without saying which ones.
   - **Meta targeting by reference only.** "Copy of SIB-05 … 'India Desk' stack + owner layer-2 behaviours" and "interests to be copied from the same stack". Nobody who hasn't seen the account can rebuild this, and nobody can review it.
   - **Google cap method is an either/or.** "Account-level budget order **or** campaign end date". These two behave differently. An account budget order needs monthly invoicing. An end date doesn't cap spend at ₹1,20,000.
   - **Reddit communities:** "verify each is targetable at build". This gives no fallback list, so the builder decides.
   - **Landing-page contradiction.** G-T (§6.3) says no platform goes live until an India-entry LP captures click IDs and the parent-country field. §9 says to launch on the existing `/indian-subsidiary-registration` and `/india-entry-services` pages "until the new page is live". The builder has to pick which instruction wins.
4. **Recommended Fix:** Write every ad verbatim, with character counts per platform: Meta primary text/headline/description, LinkedIn intro text ≤150 chars + headline ≤70, Reddit headline. Then send all copy through `ppc-compliance-reviewer`. List the Meta detailed-targeting items by name and ID. For Google, choose one method: a campaign total budget of ₹1,20,000 if the account has it, otherwise ₹4,000/day plus a calendar task to pause at ₹1,20,000. Give Reddit a primary and backup community list. Make one LP rule: either G-T item 2/8 is a hard gate and no website-traffic platform launches until the new LP is live, or name the interim pages and remove item 8 from the gate for them.

## Finding 2
1. **Severity:** Major
2. **Affected Scope:** §5 Budget (Google ₹4,000/day, ₹1,20,000, 40%); §7 K1 (Google ₹20,000); §2 demand data
3. **Finding:** The plan's own demand data can't absorb the Google budget, and the Google kill rule won't fire within the test window.
   - The targeted keywords add up to ≈ **620 US searches/month** [calc from §2: 320+50+40+40+40+20+(7×10)+40].
   - With 100% impression share, 10% CTR and every click at the ₹700 cap, the ceiling is ≈ 62 clicks × ₹700 = **₹43,400/month** [calc]. That is about 36% of the ₹1,20,000 cap.
   - A realistic case for a new account is 50% IS, 8% CTR [est] and ~₹500 average CPC [est]. That gives ≈ 25 clicks and **≈ ₹12,400/month** [calc].
   - At that pace, K1 (₹20,000 with 0 QL) triggers around day 45–50 [calc]. That is after the day-30 decision.
   - Phrase-match close variants may double volume. Even so, the budget stays well under the cap.

   As a result, 40% of the "₹3,00,000 plan" is notional. The real month-1 mix is decided by LinkedIn and Meta, and the plan doesn't show this.
4. **Recommended Fix:** Size Google to demand: ₹1,500/day, ₹45,000 month-1 cap. Set K1 for Google as "₹12,000 or day 30 with 0 QL, whichever comes first". Restate §5 to show expected spend per platform next to the cap, labelled [est], so the CFO sees the real ₹ deployed. Don't move the freed budget automatically (see Finding 6 for where it should go).

## Finding 3
1. **Severity:** Major
2. **Affected Scope:** §9.1 bidding; §3 P1
3. **Finding:** The bid strategy doesn't suit this volume.
   - **Maximize Clicks with a ₹700 ceiling** will go after the cheapest clicks. Those are the informational phrase terms in ad group 3: "how to start a business in india" (40/month) and "start business in india from usa". This happens under one shared budget, so ad group 3 drains the Subsidiary ad group.
   - **₹700 is below the low end of the top-of-page range** for [incorporate in india] (₹898–₹17,980). It is barely above the low end for [set up company in india] (₹607). So some of the best keywords may not serve at all.
   - **The switch rule is "first 14 days or 15 conversions"**, so it fires at day 14 whether or not any conversions exist. It then moves to Maximize Conversions on "IE – Qualified lead". Expected volume is ~1–2 QL/month [calc: 25–60 clicks × 5–10% click→lead [est] × 37.5% lead→QL (3/8, SIB-05)]. Smart Bidding on that signal will choke delivery or bid at random.
   - **Unit economics don't close at the plan's own CPC.** At ₹500 CPC, 7.5% click→lead [est] and 37.5% lead→QL, click→QL is 2.8% and **CPQL ≈ ₹17,800 [est]**, about 3× the ₹6,000 target. Break-even needs click→QL ≥ 6.4% at ₹500 CPC [calc: 500 / 7,767]. The plan never models CPC → CVR → CPQL per platform.
4. **Recommended Fix:** Use Manual CPC with keyword-level bids: exact ₹700–₹900 on the top 6 terms, phrase ₹400–₹500. Put ad group 3 in its own campaign with its own small budget (₹300/day) so it can't drain Subsidiary. Delete the automatic day-14 switch. Move to Maximize Conversions only on "IE – Website lead", and only after ≥ 15 website-lead conversions in 30 days. Never bid on "IE – Qualified lead" at this volume; import it for reporting only. Add a per-platform funnel table to §4 (CPC or CPM → CTR → CVR → lead→QL → expected CPQL), every cell labelled.

## Finding 4
1. **Severity:** Major
2. **Affected Scope:** §3 P1 "Why" column; §8 "Cannibalising SEO"
3. **Finding:** The core rationale for Google doesn't hold. The plan says P1 has the "same intent as the organic SEO - Google queries that produced 11 of 20 wins". But the diagnosis says the 20 won deals are **18 India / 1 UK / 1 US** by `Country_Region`, the parent-country mix is "unknown", and `UTM_*` / keyword are empty on all 20. Nothing shows that the organic wins came from US searchers. In 12 months there was **one** US won India-entry deal (₹86,212) from any channel.

   Second problem: if Setindiabiz already ranks organically for these US queries, paid search buys clicks it would get free. The only control in the plan is "monitor organic India-entry leads weekly". At 20 organic deals a year, that can't detect anything.
4. **Recommended Fix:** Before launch, pull a Search Console report for the target queries, filtered to country = United States, last 12 months: impressions, clicks, average position. Drop or down-bid keywords where the site already holds positions 1–3 in the US. Reword P1's "Why" to what the data supports ("organic search is the only proven India-entry channel; US share unknown"). Label the US-buyer assumption [est].

## Finding 5
1. **Severity:** Major
2. **Affected Scope:** §3 P4, §5 (LinkedIn ₹75,000, 25%), §9.4 audience
3. **Finding:** LinkedIn gets the second-largest share, but it has **zero account history** (0 LinkedIn leads, per `business-context.md`) and **no India-intent signal** in the targeting. The audience is generic US Owner/CXO/VP/Director × 4 functions × 11–5,000 employees × 5 industries. Almost none of these people are planning India entry.
   - At ₹2,500/day (~USD 28 [est at ₹88/USD]) and US senior-B2B CPC of ~USD 8–15 [est], that buys ≈ 2–3.5 clicks/day.
   - CPL lands around ₹7,000–₹15,000 [est]. At a cold-audience lead→QL of 20–30% [est], **CPQL ≈ ₹25,000–₹75,000 [est]**. That is 4–12× target.
   - The ICP is inconsistent: LinkedIn uses company size 11–5,000, while Microsoft (§9.2) boosts 51–1,000.
   - The "country" field on the Lead Gen Form pre-fills the member's location. It does not capture the parent-company country, which is what §6.3 item 8 needs.
4. **Recommended Fix:** Cut LinkedIn to ₹40,000 for month 1 (₹1,300/day) and add an India signal to the targeting. Options:
   - a company-list Matched Audience of US firms with Indian operations or hiring in India (company names only, not personal data, so it doesn't conflict with "no list uploads")
   - member skills or interests tied to "international expansion" or "India"
   - 3 industries instead of 5

   Align company size with Microsoft: 51–1,000 on both. Replace the pre-filled "country" field with a custom question: "Where is your company headquartered?" State the forecast audience size in the plan.

## Finding 6
1. **Severity:** Major
2. **Affected Scope:** §5 Budget allocation; §3 P3; §4 "Reference"
3. **Finding:** The allocation runs opposite to the evidence:
   - **Meta** is the only platform with US qualified leads (3 QL at ₹4,454 [calc in diagnosis], below the ₹6,000 target). It gets **15%**.
   - **Google** (0 won from ₹99,927 in Dec-25 per learnings, and demand-capped per Finding 2) gets **40%**.
   - **LinkedIn** (no history) gets **25%**.

   Separately, the ₹3,00,000 is a ceiling the owner set, not a target. Breaking even on margin in month 1 would need **5.8 won deals** [calc: 3,00,000 / 51,780]. All channels together produced 1 US won deal in 12 months. The plan doesn't explain why month 1 should use the full ceiling.
4. **Recommended Fix:** Reallocate month 1:

   | Platform | Daily | Month-1 cap |
   |---|---|---|
   | Google | ₹1,500 | ₹45,000 |
   | Meta US | ₹2,500 | ₹75,000 |
   | LinkedIn | ₹1,300 | ₹40,000 |
   | Microsoft | ₹500 | ₹15,000 |

   Hold ChatGPT and Reddit (Findings 9–10). That totals ≈ **₹1,75,000** [calc]. Keep the ₹1,25,000 balance as a reserve released only under S1/S2 with owner approval. If the owner wants the full ₹3L, state in writing that it's a deliberate learning budget, so nobody mistakes it for an expected-ROI budget.

## Finding 7
1. **Severity:** Major
2. **Affected Scope:** §9.3 Meta structure (CBO ₹1,500/day across 2 ad sets; ad set 2 Advantage+ audience)
3. **Finding:** Two problems with the Meta structure:
   - **₹1,500/day is split across 2 ad sets and 4+ ads under CBO.** At the diagnosis US CPM of ₹8,420, that is ≈ **178 impressions/day** for the whole campaign [calc]. Expected volume is ~2 leads/week [calc at ₹4,454/lead]. That is nowhere near the ~50 optimisation events per ad set per week Meta needs to exit learning, so both ad sets stay in learning for the whole test.
   - **CBO will repeat the SIB-05 failure.** The diagnosis showed lead-volume optimisation moving spend to the cheaper pocket (UAE, 0 QL). Here the cheaper pocket will be ad set 2 (age 25–50, **Advantage+ audience with suggestions**, which lets Meta go broad). Its "interests copied from the same stack" is the company-expansion stack, which has nothing to do with returning NRIs. So in practice ad set 2 is a broad US 25–50 audience, chosen by the algorithm for cheap leads.
   - Also unproven: the diagnosis doesn't split ad × country. That makes it unproven that **B2** produced the US QLs (4 of B2's 7 leads could be UAE).
4. **Recommended Fix:** Month 1 should be one ad set, US 30–65, the named targeting stack, Advantage+ audience **off**, with B2, F1 and R1 competing inside it. Optimise for leads with a higher-intent form, keeping Q1 as a qualifying question. If the owner insists on a separate group-B test, use ABO with a fixed ₹700/day for ad set 2, Advantage+ audience off, and a K3 check after 5 worked leads. Before reusing B2, pull SIB-05 ad × country to confirm which ads produced the 3 US QLs.

## Finding 8
1. **Severity:** Major
2. **Affected Scope:** §5 "Maximum loss" (₹1,05,000); §7 K1/K2/K3/S1; §4 target CPQL
3. **Finding:** The downside presented to the CFO is understated, and the rules have gaps:
   - **K1 fires only on 0 QL.** A platform that gets one QL at ₹15,001 keeps running to day 30 and spends its full cap. LinkedIn would spend ₹75,000 for 1 QL, a CPQL of ₹75,000. So the true realistic maximum loss is close to the ₹3,00,000 cap total, not ₹1,05,000.
   - For **Reddit** (cap ₹15,000 = K1 threshold), K1 can never fire before the cap is spent.
   - **K2 gap.** It pauses only above ₹12,000 CPQL. Between ₹7,767 (break-even) and ₹12,000 a platform loses money with no rule. The "proposal ≥ ₹50,000 open" exception lets a single open proposal keep a losing platform running.
   - **Target CPQL ₹6,000 is above break-even** if QL→won is below 11.6% [calc: 6,000 / 51,780]. The diagnosis' own break-even was 10.3%. The 15% QL→won [est] has no basis, and the target leaves almost no margin of safety under it.
   - **S1** scales at +20%/week after only 3 QL. Four approvals compound to +107% [calc] before any won deal.
   - **K3** needs ≥ 10 worked leads per platform, which most platforms won't reach in 30 days, so it will never trigger.
   - **AOV:** the plan uses the FDI-only AOV of ₹86,300. The full India-entry set (20 deals) is ₹81,574 [diagnosis], giving a break-even CPQL of ₹7,342 at 15% [calc]. `business-context.md` also warns that deal Amount may include government fees.
4. **Recommended Fix:**
   - Add a spend-based kill: any platform at ≥ 2× target CPQL (₹12,000 per QL) once spend reaches ₹25,000 is paused, regardless of the 0/≥1 QL state.
   - Restate maximum loss as the sum of caps, and give the realistic case under the new rule.
   - Set the target CPQL at ≤ ₹5,000, or run a sensitivity table for 10/15/20% QL→won.
   - Remove the K2 open-proposal exception, or require stage ≥ Proposal Sent with a written scope.
   - S1 needs ≥ 5 QL and at least 1 won or "Proposal Sent" from that platform.
   - Lower K3 to ≥ 5 worked leads.
   - Use the all-FEMA AOV, or show both.

## Finding 9
1. **Severity:** Major
2. **Affected Scope:** §3 P5, §5 (ChatGPT ₹20,000), §9.5
3. **Finding:** The plan repeats a known failure. Per learnings (2026-10-09), ChatGPT Ads produced **54 CRM leads and 0 won**, and **5 of 6 Branch & Liaison ads were policy-blocked**. §9.5 still targets "branch office vs subsidiary India" and "liaison office India". US geo-targeting availability in the ChatGPT Ads early access is unverified (the prior campaigns were INR/domestic), and CGPTA isn't connected. At ₹20,000, even at target CPQL this gives ≤ 3 QL [calc], which isn't enough to decide anything.
4. **Recommended Fix:** Take ChatGPT out of month 1. Re-enter at the day-30 review only if: (a) US geo targeting is confirmed in the UI; (b) branch/liaison prompts are dropped in favour of subsidiary-only prompts; (c) a test ad passes policy review before any budget is committed.

## Finding 10
1. **Severity:** Major
2. **Affected Scope:** §3 P6, §5 (Reddit ₹15,000 from week 3), §9.6
3. **Finding:** The Reddit test is too small to read and poorly targeted.
   - **Budget:** ₹750/day from week 3 spends only ≈ ₹12,000 in month 1 [calc: ~16 days], below its own ₹15,000 cap. Conversion-objective optimisation on 0–2 pixel conversions is effectively random.
   - **Community choice:** r/IndiaInvestments is mostly India-resident users, so a US geo filter leaves almost nothing. r/ABCDesis is an identity community for American-born desis, not returnees or founders. It is low intent and sits close to the plan's own "no ethnicity/national-origin targeting" rule (§8). r/h1b contradicts the Google negatives (`h1b`, `visa`).
   - **Naming:** `RDT_Traffic_…` names a Traffic objective while the build uses Leads. That breaks the `<Platform>_<Objective>_…` convention.
4. **Recommended Fix:** Either remove Reddit from month 1, or fund it at ≥ ₹25,000 over 30 full days with r/nri, r/returnToIndia and r/IndianStartups only. Drop r/ABCDesis and r/IndiaInvestments. Rename to `RDT_Leads_IndiaEntry_US_Returning_202612`. Make one consistent decision on whether H-1B/visa audiences are in or out, across Google and Reddit.

## Finding 11
1. **Severity:** Major
2. **Affected Scope:** §9.1 negative list `IE Negatives`; ad group 3 keywords
3. **Finding:** Ad group 3 phrase terms ("how to start a business in india", "start business in india from usa", "moving back to india business") will match "small business ideas" and "low investment" queries. The negative list doesn't cover these. Missing:
   - ideas, low investment, small business, home based, franchise, loan, mudra, startup india scheme, without money
   - domestic services: gst, trademark, msme, udyam, proprietorship, partnership firm, pan card, aadhaar, oci, nre, nro, nri account, income tax, itr

   Learnings show the Dec-25 Google campaign had no negatives and spent ₹99,927 for 0 won. This is the same leak with a shorter list. No search-term report from Dec-25 was pulled, although the diagnosis named that as the step before keyword planning.
4. **Recommended Fix:** Pull the Dec-25 "Subsidiary_Registration" search-term report before finalising, and add every irrelevant term. Add the negatives above at campaign level. Make ad group 3 exact-match only for month 1, or split it off as in Finding 3. Schedule a search-term review at day 3 and day 7, not just at Review 1.

## Finding 12
1. **Severity:** Major
2. **Affected Scope:** §9.2 Microsoft Ads; §3 P2
3. **Finding:** The Microsoft line rests on bad assumptions and leaks spend.
   - **"Low CPC history (₹42)" doesn't support the US case.** That campaign ran without working UET and its geo isn't stated in the diagnosis, so the figure says nothing about US exact/phrase CPCs.
   - **The budget won't spend.** Bing's US share is a fraction of Google's ~620 searches [est: ~100–150/month], so ₹800/day (₹25,000) won't spend either.
   - **Bid adjustments are meaningless at this volume.** LinkedIn-profile adjustments of +25% and +15% on ~100 searches change nothing measurable.
   - **The network setting is missing.** An import from Google keeps Microsoft's default "all search networks, incl. syndicated search partners", which is a known spend leak.
   - **The bid strategy is implied, not named** ("Enhanced CPC off, max CPC ₹400").
4. **Recommended Fix:** Set Microsoft to ₹500/day (₹15,000 cap). Name the bid strategy as Manual CPC, per learnings ("Manual CPC until 15–30 conv/month"). Set the network to "Bing, AOL and Yahoo search (owned and operated) only". Remove the profile bid adjustments for month 1. Delete the "₹42 CPC" rationale.

## Finding 13
1. **Severity:** Major
2. **Affected Scope:** §6.2/§6.3 (LinkedIn and Reddit Lead_Source); §6.4 SLA; §7 K1
3. **Finding:** Two gaps can make the kill rules read false zeros:
   - **Missing picklist values.** `Advt - LinkedIn` and `Advt - Reddit` don't exist in Zoho (`business-context.md`: "Add … before launching those platforms"). G-T doesn't list this, and only the ChatGPT rule change is flagged. LinkedIn Lead Gen Form → Zoho (integration or LeadChain) is also undecided in §6.2. Leads may land unattributed, and K1 then reads "0 QL" on a platform that actually produced leads.
   - **Leads aren't worked fast enough.** QL status depends on sales working the lead. SIB-05 had **4 of 8 leads unworked** after up to 3 weeks. The SLA is "4 working hours IST", so a US lead from 14:00 ET gets first contact at ~03:00 ET [calc], and late-shift handlers aren't named. An unworked lead counts as non-QL, so K1 can kill a good platform.
4. **Recommended Fix:** Add to G-T:
   - (a) create the `Advt - LinkedIn` and `Advt - Reddit` picklist values
   - (b) choose the LinkedIn→Zoho route and submit a test lead on it
   - (c) name the late-shift owner(s) before go-live

   Change K1 to "0 QL with all leads worked (status ≠ Establishing Contact / blank) for ≥ 3 working days". Add "unworked leads > 24 h" to the Monday reconciliation as a stop condition for further spend.

## Finding 14
1. **Severity:** Major
2. **Affected Scope:** §9 interim LP routing; §9.1 ad group 3; §9.1 RSA pinning
3. **Finding:** Two problems between the ads and the pages they send traffic to:
   - **Ad group 3 lands on the wrong page.** "Moving Back to India? / Indian Pvt Ltd for NRIs" sends traffic to `/india-entry-services`, which the plan itself labels the branch/liaison page. The interim subsidiary page offers no US booking link and no parent-country field (the reasons the new LP exists).
   - **The H3 pin doesn't guarantee the disclaimer shows.** "Private Firm, Not a Govt Body" is pinned to headline 3, and Google often doesn't show H3. Given the unresolved government-services disapprovals in learnings, a disclaimer that shows only sometimes doesn't protect the ad.
4. **Recommended Fix:** Hold ad group 3 (and Meta/Reddit returning-founder traffic to the website) until LP (c) "Moving back to India?" is live. Pin the disclaimer headline to position 2, or pin description (2) "Private consultancy, not a government agency…" to description position 1, which always shows.

## Finding 15
1. **Severity:** Minor
2. **Affected Scope:** §5 "Meta prepaid balance"; §9.3
3. **Finding:** A prepaid Meta balance is account-level and can't be ring-fenced per campaign. SIB-01/02/04 will use up any top-up first, and the campaign spending limit doesn't reserve funds. Repeated dark periods also reset delivery or learning. The existing business-hours ON/OFF rules (`name contains #IND`) don't match the new name, which is correct; keep it that way.
4. **Recommended Fix:** Make an attached card or postpaid billing a G-T prerequisite for the Meta line. Otherwise schedule top-ups sized to the whole account's burn, not just ₹1,500/day. Add to §9.3: "campaign name must not contain `#IND`".

## Finding 16
1. **Severity:** Minor
2. **Affected Scope:** §9.3 ad set 1 placement rationale; §2 platform access
3. **Finding:** Two numbers in the plan don't match their sources:
   - **Placement waste.** Instagram Feed + FB Stories + IG Stories = **₹8,249.55** [calc from diagnosis §2d: 4,643.37 + 1,836.81 + 1,769.37], not ₹8,056.
   - **Platform access.** §2 says LinkedIn, X and Reddit are "connected in Supermetrics". The diagnosis (same day) lists all three as **not authenticated**, and the plan gives no source or time for the change.
4. **Recommended Fix:** Correct the figure. Add a source and timestamp for the connection status, or mark it "to verify".

## Finding 17
1. **Severity:** Minor
2. **Affected Scope:** §5 Duration vs caps; §9.1 assets
3. **Finding:**
   - **Ambiguous test window.** Duration is "30 days from first delivery per platform", but the caps are "Month-1". For platforms starting in week 2 or 3, it's unclear whether the cap covers the 30-day test or the calendar month.
   - **Low-intent sitelink.** The `/fdi-reporting-fcgpr` sitelink is a post-incorporation compliance page, so it pulls entry-stage searchers to a lower-intent page.
   - **Contact sitelink mismatch.** The "Contact us" sitelink lands on a page that states Mon–Sat 9:30–18:30 IST and an Indian number, which contradicts the "US time-zone calls" callout.
4. **Recommended Fix:** Define caps per 30-day test window. Replace the FC-GPR sitelink with "Subsidiary vs branch vs liaison" (comparison content), and point "Contact us" to the booking link once the LP shows ET hours.
