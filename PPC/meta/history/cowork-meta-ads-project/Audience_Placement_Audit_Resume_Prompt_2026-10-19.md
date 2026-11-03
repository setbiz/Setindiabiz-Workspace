# Resume prompt: strict audience and placement audit (written 19 Oct 2026, 13:45 IST)

Start a new session in the "Meta Ads - Optimisation" project and say: *"Continue from Meta Ads/Audience_Placement_Audit_Resume_Prompt_2026-10-19.md"*.

## The ask (Sanjeev, 19 Oct 13:31, verbatim)

> "You have to rework on audience and plateforms and we have to be very strict on it so that the money is not wasted on junk. read earlier convesation to gather insights and them restart another session to audit the audience and the placements"

**Scope**
1. **SIB-05 India Entry (FDI) first.** It is about to launch, and its audience and placements are the loosest in the account.
2. **Then every live ad set**, with the same strict lens.

**Operating principle (Sanjeev, 16 Oct):** quality first. Judge in CRM, never on Meta's lead or chat counts. Higher cost per lead is acceptable if junk falls.

## Read first (in this order)

1. `Meta Ads/Lead_Quality_Junk_Diagnosis_2026-10-16.md`: how SIB-04 went to 87% rejected, and Meta's hard-vs-suggestion rules (§4).
2. `Meta Ads/Lead_Quality_Watch_Log.md`: daily results since the strict Directors rebuild (17–19 Oct). The 19 Oct entry is the latest.
3. `Meta Ads/Change_Log_2026-10-16_Lead-Quality-Diagnosis.md`: how the strict Directors ad sets were built and published, including the **silent revert to all-India on publish**.
4. `Meta Ads/Change_Log_2026-10-16_SIB-05-G12-Build.md` and `Meta Ads/SIB-05_G12_Build_Sheet_2026-10-16.md` §3: the SIB-05 build and its audience deviations.
5. `Meta Ads/Change_Log_2026-10-19_SIB-05-LeadChain-v2.md`: SIB-05 state today (LeadChain v2, launch readiness, the lead-deletion finding).
6. `Meta Ads/SetIndiaBiz_Meta_Saved_Audiences.docx`: SAV-10 India Desk stack, and the planned exclusion audiences (CA_ALL_LEADS_180D, CA_CUSTOMERS_540D, CA_FORM_SUBMITTED_30D, CA_WHATSAPP_INITIATED_30D). Check whether these exist.

## Insights gathered (what we already know)

### A. What causes junk in this account
1. **Advantage+ audience (A+A) ON is the main leak.** With A+A on, only these are hard:
   - location;
   - minimum age (max 25);
   - language;
   - custom-audience **exclusions**.
   Everything else is a suggestion: job titles, interests, behaviours, education, gender, age max, custom-audience inclusions. Meta's help articles: [Advantage+ audience](https://www.facebook.com/business/help/793748385630490), [Advantage+ custom audience](https://www.facebook.com/business/help/414975413946182).
   - The optimiser then finds whoever converts cheapest. On SIB-04 WhatsApp, cost per chat fell from ₹157 to ₹48 while rejected rose to 87%.
2. **The strict model that works:**
   - CCFS (lifetime ~13–21% junk) and the SIB-04 Directors rebuild (17–18 Oct: 15% junk, 4 of 26).
   - Settings: **A+A OFF**, custom lists **hard**, relaxation lookalike 0 / custom_audience 0, no `expansion_all`, male, age 25–60, English [6, 24], 19 metro cities at 25 mi, **FB + IG Feed, Stories, Reels only**.
3. **One-tap paths (WhatsApp / CONVERSATIONS) attract junk** unless the audience is hard-limited. Instant forms set to "Higher intent" with qualifying questions are much cleaner.
4. **Language is a strong hard filter.** Chats in Indian scripts were about 1 in 16 valid.
5. **Education:** Meta removed occupation and education *exclusions* on 31 Mar 2025. An education *inclusion* filter shrank the Directors audience too far and was dropped on 16 Oct (22:54).
6. **Loss buckets on the junk days:** 95% targeting, against an 11% baseline. Speed-to-lead and pricing were checked first and were not the cause.

### B. Placements
- **Account-level exclusions** (13 Oct): Audience Network, FB Marketplace, FB right column. Holding: ₹0 spend there 14–18 Oct.
- **Leaks seen outside the CCFS placement set:**
  - FB in-stream (₹412 CTWA, ₹134 Form, 14–16 Oct);
  - Reels overlay (₹261);
  - Threads (pennies);
  - WhatsApp Status (₹0 after the exclusion).
- **Advantage+ placements** (no `publisher_platforms` set) also open search, notifications, profile feed, Explore and in-stream.
- The 16 Oct G12 note says "Meta says ad-set placement exclusions are being withdrawn". Yet the Directors ad sets do carry manual FB/IG feed/story/reels positions. **Verify how they were set and whether SIB-05 can be set the same way** (connector `ads_update_entity` with `publisher_platforms` + positions, as a draft).

### C. Publishing traps
- **Ads Manager silently reverted** the Directors WhatsApp audience to all-India on publish (16 Oct). **Always read back targeting through the connector after Sanjeev publishes.**
- Publish in Ads Manager sweeps **all** pending drafts. The SIB-02 TM WhatsApp draft (ad set 120247099920320449, PAUSED, ad 120247099921540449) is pending; it is PAUSED, so it won't spend.
- The connector stages new or edited objects as drafts. Sanjeev publishes; Claude never does.

## Current targeting snapshot (connector read, 19 Oct ~13:40 IST)

| Ad set | Status | A+A | Hard limits | Audience | Placements | Strict? |
|---|---|---|---|---|---|---|
| SIB-04 Directors WhatsApp 120247072309210449 (₹2,000) | ACTIVE | **0** | Male 25–60, EN, 19 cities, home/recent/**frequently_in** | 7 Director lists hard, relax 0/0 | FB feed/story/reels, IG stream/story/reels | ✔ (frequently_in is legacy; minor) |
| SIB-04 Directors Form 120247072301790449 (₹2,500) | ACTIVE | **0** | Male 25–60, EN, 19 cities, home/recent | 7 Director lists hard, relax 0/0 | same | ✔ |
| #IND1 C1 24Hr INSA 120240912969640449 (₹2,500) | ACTIVE | **1** | 25+, EN, 18 cities | 17 interests, behaviours, 2 titles, education: **all suggestions**; all genders | **Advantage+ (all)** | ✘ loose, but clean so far (0% junk 7d, 43% valid) |
| SIB-02 TM Form - Copy 120247094867020449 (₹1,200) | ACTIVE | **1** | 25+, EN, 30 cities, **`individual_setting.geo = 1` (location expansion)**, `expansion_all` | 31 interests, 15 titles, education: suggestions | FB feed, **instream, search, reels overlay, profile feed, notification**, IG incl. **explore, profile, search**, **Threads** | ✘ loose, but clean so far (4% junk 7d) |
| **SIB-05 India Entry 120247067863750449** (+ Subsidiary, Branch-Liaison drafts; CBO ₹4,000) | live PAUSED / drafts | **1** | 25+, locales EN-US/UK, JA, KO; 7 countries US/AE/SG/KR/JP/AU/CA; home + **recent**; all genders | 7 titles (incl. mistaken **"Co Owner"**), 1 interest, 2 behaviours, 1 industry: **suggestions**; `expansion_all` | **Advantage+ placements (15)** | ✘ **loosest; not launched yet** |
| #IND3 Director-TMF 120243249506380449 | CAMPAIGN_PAUSED | 1 | 28 cities | 19 lists, relax custom 1 | Advantage+ | ✘ (the campaign was never switched on) |
| Others (DPIIT, CCFS, old #IND1, TMF-SA, Restart Oct) | paused | — | — | — | — | not in scope unless revived |

**No ad set uses any custom-audience exclusion.** Exclusions stay hard even under A+A, so this is the cheapest strictness win.

## SIB-05 specific risks to solve
- **No first-party list exists for foreign founders**, so the Directors model can't be copied directly. Options to put to Sanjeev:
  1. **A+A OFF + detailed targeting hard:** job titles (Founder, CEO, MD, CFO, Owner, Partner, Managing Partner, Chairman, VP, Country Manager, Head of International, General Counsel, Finance Director, Head of Legal) AND narrow by Business decision makers / Page admins / Small business owners. Check audience size per country; CBO ₹4,000 across 7 countries may starve.
  2. **Keep A+A ON but tighten the hard levers:**
     - location type **home only** ("recently in" brings in travellers, including from India);
     - age 25 min;
     - language;
     - exclusions: all CRM leads, customers, employees, past junk numbers.
- **Indian-diaspora / job-seeker risk** in UAE, SG, CA, AU and US: English locale includes them.
  - Consider dropping or limiting the UAE share. On 6 Oct the plan predicted Meta would drift budget to the cheapest geo (likely UAE). Country split with per-country ad sets, or a country cap?
  - Check whether Meta still allows detailed-targeting exclusions (Expats – India). They were being retired; verify with `ads_get_help_article`, not memory.
- **Form v2 hardening (optional; needs a new form v3 + LeadChain chain + PPC Form Tidy line):** work email with business-domain validation; a qualifier question "Are you the founder/director of the overseas company?".
- **Placements:** set FB + IG Feed, Stories, Reels only; no Threads, in-stream, search, Explore or notifications.
- **Remove "Co Owner"** (126237404086327) from suggestions, and add the missing India Desk titles (only matters if A+A stays ON).
- Regulated-category entries for SG/AU are required while those countries are targeted; leave them.

## What the new session should do

1. **Funding check first** (read-only; human top-up). About ₹17.4k on the 19 Oct morning, about 2 days.
2. **Pull evidence** (connector, last 14 days, per live ad set):
   - breakdowns `['age','gender']`, `['region']` (or `['country']` for SIB-05 later) and `['publisher_platform','platform_position']`;
   - spend share outside FB/IG Feed, Stories and Reels;
   - spend share on 18–24, women and non-listed regions.
   - Join to CRM rejected % and valid % by `Meta_Ad_Set` (same definitions as the watch log).
3. **List custom audiences** (`ads_get_ad_account_custom_audiences`). Confirm which exclusion audiences exist. If none, propose building them (CRM export of all leads and customers 540d, plus junk numbers) as a **draft plan only**: customer-list upload needs Sanjeev's OK and a privacy check (DPDP Act 2023: purpose and consent; the privacy-policy wording issues are already flagged).
4. **Write the audit** `Meta Ads/Audience_Placement_Audit_2026-10-19.md`: per ad set, each setting → hard or suggestion → leak evidence → strict recommendation. Use one table per ad set, and a 0–3 score on audience, location, age/gender, language, placements and exclusions.
5. **SIB-05 strict spec:** use AskUserQuestion for options A/B above, location type, UAE handling, gender and placements. Then **stage as drafts** with `ads_update_entity`, one variable per change, read back, and log. Do not publish.
6. **Live ad sets:** recommend at most 1–2 changes, one variable each, with a stop-loss.
   - Likely first: SIB-02 Copy placements to FB/IG Feed/Stories/Reels and location expansion `geo` off.
   - Second: #IND1 placements.
   - Don't break what is clean: #IND1 and SIB-02 show 0–4% junk. Make each change on its own with a 3-day CRM read: **keep if rejected ≤25% of worked and valid not lower; revert if rejected >40% or spend <50% of budget on all 3 days.**
7. Log everything in a change log, and update the watch log's guardrail-audit line so the daily task checks the new strict settings.

## Hard rules (unchanged)
- Never publish, never call `ads_activate_entity`, never click Publish / "Review and publish". Sanjeev publishes, then Claude reads back targeting.
- Never move money or enter passwords. Every Meta change needs explicit approval, one variable at a time, with before/after evidence and a logged stop-loss.
- No CRM writes without asking; never delete. Don't touch SalesIQ bots, LeadChain, Zoho Social or the Tiya project's objects.
- Ad claims must stay accurate under the Companies Act 2013, the LLP Act 2008, the CGST Act 2017, and FEMA / FDI policy for SIB-05.

## Other open items (not this session's job; just don't lose them)
- SIB-05 booking-email workflow still matches v1 only (parked).
- **Leads being deleted as "Sanjeev Kumar"** within a minute of creation; deleter not identified. See the 19 Oct change log.
- The Swati v2 test lead is optional now (Sanjeev 13:24: "continue without this check").
- 189 paid leads unworked > 24 h (19 Oct watch log).
