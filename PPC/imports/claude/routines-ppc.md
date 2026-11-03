# Claude scheduled tasks related to PPC (from the Claude export, 3 Nov 2026)

Source: `claude_code_cloud-000.zip` → `routines.json`. These are the scheduled tasks on the owner's Claude account whose name or prompt mentions Meta, PPC, SIB campaigns, CAPI, WhatsApp, LeadChain or lead source. Personal phone numbers and emails are redacted.

| Status | Name | Schedule | ID |
|---|---|---|---|
| off | Retry Chrome for PPC import | `once 2026-11-02T10:46:00Z` | trig_01KRs3LsDVpLGMWpPKDpLYqu |
| off | Check Bigin push after Delay | `once 2026-11-02T10:05:00Z` | trig_01VeRLk9hdGBtPfzvtBR6MKS |
| **ON** | PPC monthly budget and drift review | `CRON_TZ=Asia/Kolkata 43 11 2 * *` | trig_01PdH2TFgPcLhbkaDFQuLtVx |
| **ON** | PPC weekly EGM review | `CRON_TZ=Asia/Kolkata 17 10 * * 1` | trig_01DjFp2wdmjoGbjCWv8atN7c |
| off | Check Airtel IQ records after lunch | `once 2026-11-02T08:55:00Z` | trig_012A5FiPEKDKJm4dVLykiBr7 |
| off | SIB-05 FDI 4-hour check | `once 2026-10-21T09:45:00Z` | trig_01UrcsWUDHkd586rG5fMQQwg |
| off | Re-read Meta spend after top-up | `once 2026-10-17T09:38:00Z` | trig_01FVV1f49ps6hCmSvvX6JPB3 |
| off | SIB-04 Directors ad sets: stop-loss read | `once 2026-10-23T04:45:00Z` | trig_01WunWG2jVXrsXmmMK8vEsWL |
| off | Confirm Meta delivery resumed after top-up | `once 2026-10-17T08:34:00Z` | trig_01Jkg9n38i7Hh5bjHqs7RmUx |
| off | SIB-05: re-check Vipin's creatives | `once 2026-10-16T11:00:00Z` | trig_01L9jHjchMiRonpdWZ8gT4pa |
| off | Check first Incorporation lead after LeadChain fix | `once 2026-10-16T10:00:00Z` | trig_019tR2vXX2AxfwpHdQbsNzNP |
| off | TM/INC WhatsApp drafts: publish-gate check | `once 2026-10-22T05:15:00Z` | trig_01JxBzhSMxMQgB1McNW6tWaC |
| **ON** | Meta lead-quality watch (daily) | `CRON_TZ=Asia/Kolkata 40 9 * * *` | trig_01DPT99ZCoF8rictq4EsC2bP |
| off | SIB-04 audience change decision read | `once 2026-10-22T04:30:00Z` | trig_01MPVr6hm9VZN8k3E8v8H8Dp |
| off | SIB-04 placement read + check audience change is live | `once 2026-10-17T04:30:00Z` | trig_01H2MNnoWAEHnht4NmEhxySb |
| off | Check WhatsApp click signature after secret re-paste | `once 2026-10-15T10:24:00Z` | trig_01SbUGLBwzXTsPNX4UFaf7Pe |
| off | Re-check WhatsApp ad click capture | `once 2026-10-15T10:00:00Z` | trig_01U6GxLH24u4Gn6v8GcExtus |
| off | Check 20:00 CAPI sweep run | `once 2026-10-13T14:40:00Z` | trig_01SLpfavHj2nwZBbypPJbkVy |
| off | Placement change 3-day stop-loss review | `once 2026-10-17T04:30:00Z` | trig_01QQz33Y8aEZqJsgUbvg2UYC |
| off | Check AN/Marketplace spend stopped | `once 2026-10-13T13:00:00Z` | trig_013nhqNCwxe2XezmtHoDdCVM |
| off | Lead Assignment Rule Daily Check | `CRON_TZ=Asia/Kolkata 57 9 * * *` | trig_0142dx52rfEJxFz4Q8kxsh4w |
| **ON** | Weekly paid-channel measurement report | `30 3 * * 1` | trig_019kCqpnADCtD4YA7xNyXSrF |
| **ON** | Monthly LeadChain phone reconciliation | `30 4 1 * *` | trig_01NSKwVPGmF7mC2mF4heq1y1 |

## Retry Chrome for PPC import (off)
`trig_01KRs3LsDVpLGMWpPKDpLYqu` · created 2026-11-02

```text
Retry the Chrome extension for the PPC import (one tabs_context_mcp call). If it answers: capture #33 into doc 1IP4IhMvW13w4LQBf_wC-O7Z4dKZmvi2-pvFjYBkzNs0 (placeholders XXS33A-GXX); compare __store2 with __store in tab 1672110025 (slow re-harvest, __cur3 shows progress), including #16 turn 17 and #23 turns 36 and 49; checksum the 9 full-text sections in doc 17dpnQJkAerWhSSCvwoPsn29gQLMJ_zAG0R7X4W9ELI0 against the source; check page counts; replace XXCOUNTXX; close the tabs I opened; send the final report. If it still does not answer, stop and leave the status with Sanjeev.
```

## Check Bigin push after Delay (off)
`trig_01VeRLk9hdGBtPfzvtBR6MKS` · created 2026-11-02

```text
Check Zoho Flow "Bigin to Zoho CRM Lead" History for runs after 15:08 IST on 2 Nov: confirm completed runs went through the 1-minute Delay, then resolveLeadPush, Decision and their branch, and that no new duplicate Lead appeared (same phone twice since 15:08 among Leads with Lead_Source Self - Cold Call or Self - IVR Call). Tell Sanjeev the result only. If runs stop at the Delay or fail, tell him at once.
```

## PPC monthly budget and drift review (ON)
`trig_01PdH2TFgPcLhbkaDFQuLtVx` · created 2026-11-02

```text
Scheduled run: monthly PPC budget and drift review for Setindiabiz.

Work in /home/user/setindiabiz-workspace (repo setbiz/setindiabiz-workspace; if missing after a container restart, re-attach with add_repo (push access), clone, register_repo_root). Then `git fetch origin main && git checkout main && git pull`.
Unattended: no questions; READ-ONLY on all ad platforms; never invent numbers. Use this session's Meta Ads, Supermetrics and Zoho CRM connectors.
1. Elephant: write PPC/reports/cross-platform/<YYYY-MM>-monthly.md for the previous calendar month — per-platform spend, leads, CRM won deals and won ₹ (Zoho CRM Lead_Source 'Advt - *' is the source of truth), CPL / cost per won deal / ROAS vs PPC/shared/kpis.md, a next-month reallocation proposal in PPC/shared/budget-plan.md format, and an account-drift check of each PPC/<platform>/README.md 'Current structure' table vs the live account.
2. Goldfish: in one message spawn fresh isolated subagents with PPC/egm/reviewers/budget_cfo.md, measurement_skeptic.md and ppc_performance_critic.md against PPC/egm/standards/weekly-review-standard.md, as in .claude/skills/ppc-weekly-cycle/SKILL.md Step 3; consolidate into PPC/egm/runs/<date>-monthly/consolidated_review_report.md.
3. Commit to branch ppc/monthly-<YYYY-MM>, push, open a DRAFT PR, notify if possible, and post a 5-line summary here.
```

## PPC weekly EGM review (ON)
`trig_01DjFp2wdmjoGbjCWv8atN7c` · created 2026-11-02

```text
Scheduled run: weekly PPC evaluate-and-improve cycle for Setindiabiz.

Work in /home/user/setindiabiz-workspace (repo setbiz/setindiabiz-workspace; if the folder is missing after a container restart, re-attach it with add_repo (push access), clone it, register_repo_root). Then `git fetch origin main && git checkout main && git pull`.
Follow .claude/skills/ppc-weekly-cycle/SKILL.md exactly, using this session's Meta Ads, Supermetrics and Zoho CRM connectors. Unattended: no questions to the user; READ-ONLY on all ad platforms; never invent numbers — mark unavailable sources as missing.
Finish: commit to branch ppc/weekly-<date>, push, open a DRAFT PR, send a push notification if a notification tool is available, and post a 5-line summary here (blended spend/CPL vs target, top 3 actions, Blockers, missing sources).
```

## Check Airtel IQ records after lunch (off)
`trig_012A5FiPEKDKJm4dVLykiBr7` · created 2026-11-02

```text
Check that Airtel IQ call records recovered after lunch: count raw/2026/11/02/08 by 5-minute bucket (expected about 35 per 5 minutes after 14:10 IST, as on 31 Oct), check the processor logs for errors, and confirm Zoho Calls and Leads still look right, with no duplicate Leads. Tell Sanjeev only the result.
```

## SIB-05 FDI 4-hour check (off)
`trig_01UrcsWUDHkd586rG5fMQQwg` · created 2026-10-21

```text
4-hour check after SIB-05 switch-on (11:17 IST). Read-only: (1) all 6 SIB-05 ads delivering? spend, impressions and form leads per ad set today; ads_get_errors on campaign 120247067847480449. (2) CRM: FDI leads today (Product Cat FDI / Meta_Campaign 'SIB-05 India Entry') vs Meta lead count — flag any gap (capture stop-loss 80%), owner assigned, Lead_Source/Lead_Channel stamped. (3) Account funding left vs ₹12,200/day budgets. (4) Swati thread 1a152d0bc457c279 reply + how many of the 161 are still open. Then post a short status for Sanjeev and remind him of the pending booking-email workflow fix.
```

## Re-read Meta spend after top-up (off)
`trig_01FVV1f49ps6hCmSvvX6JPB3` · created 2026-10-17

```text
Follow-up (read-only): at 14:06 IST all 4 live ad sets showed delivery "active" after the ₹20,000 top-up, but today's spend was still frozen at the 13:40 snapshot (Directors WA ₹53.12, Directors Form ₹118.64, 24Hr INSA ₹20.80, SIB-02 TM Form ₹22.52 = ₹215.08), probably reporting lag. Re-read today's spend for 120247072309210449, 120247072301790449, 120240912969640449, 120247048085540449 (fields amount_spent, impressions, delivery). If spend is rising on each, tell Sanjeev in one line that delivery has resumed. If still flat, check ads_get_errors for those 4 ad sets plus the budget activity log since 08:00 UTC and tell him what blocks it. Make no Meta changes. Append one line to Meta Ads/Lead_Quality_Watch_Log.md.
```

## SIB-04 Directors ad sets: stop-loss read (off)
`trig_01WunWG2jVXrsXmmMK8vEsWL` · created 2026-10-17

```text
Stop-loss read for the SIB-04 directors-only ad sets (read-only; make no Meta change without Sanjeev's OK). Read Meta Ads/Change_Log_2026-10-16_Lead-Quality-Diagnosis.md (stop-loss, Change B) and the 17 Oct section of Meta Ads/Lead_Quality_Watch_Log.md first. Window = 18–20 Oct (first full delivery days; 17 Oct was cut short when the prepaid balance ran out, top-up ₹20,000 at 13:48 IST). Ad sets: Directors Form 120247072301790449, Directors WhatsApp 120247072309210449. For each: spend per day (and whether it reached ≥50% of budget), CRM leads with Meta_Campaign 'SIB-04 Annual Filings' created 18–20 Oct split Form (Advt - Facebook / Instagram) vs WhatsApp (Advt - WhatsApp; the old WhatsApp ad set has been paused since 16 Oct 22:37, so all new WhatsApp leads are Directors). Report rejected % of worked leads (junk + not a buyer), valid % of worked, unworked %, and cost per valid. Rules: KEEP if rejected ≤25% and valid ≥35% of worked; PAUSE AND REVIEW if rejected >40%; if spend <50% of budget on all 3 days, propose widening to all-India first. Flag any lead marked 'Inquired by Mistake' whose chat summary or description shows a real enquiry (RM mislabel). Tell Sanjeev in a short table plus 2–3 lines and log it in the change log.
```

## Confirm Meta delivery resumed after top-up (off)
`trig_01Jkg9n38i7Hh5bjHqs7RmUx` · created 2026-10-17

```text
Post top-up check (read-only): Sanjeev said at 13:42 IST he was adding balance to ad account 152154124583473. Check ads_account_get_activity_logs (budget) for a new "Money added to balance" entry since 17 Oct 08:00 UTC and note the amount. Then read today's spend per active ad set (Directors WhatsApp 120247072309210449, Directors Form 120247072301790449, 24Hr INSA 120240912969640449, SIB-02 TM Form 120247048085540449) and compare with the 13:40 IST snapshot (₹53 / ₹119 / ₹21 / ₹23, total ₹215). Pass = spend rising on each. Also read back the Directors WhatsApp ad set's live targeting (19 cities, male 25–60, English, FB+IG feed/stories/reels, A+A off). Tell Sanjeev in 2–3 lines; if no top-up shows yet, say so in one line and don't repeat the request more than once.
```

## SIB-05: re-check Vipin's creatives (off)
`trig_01L9jHjchMiRonpdWZ8gT4pa` · created 2026-10-16

```text
16:30 IST read-only re-check of Vipin's SIB-05 creatives (Sanjeev asked for this at 13:50). Follow Meta Ads/SIB-05_Resume_Prompt_2026-10-16_1400.md step 1: (a) Gmail thread 1a1359139e2d73dc for any reply, plus any mail from hatrotech.com; (b) Canva DAHX_Sw46n4: if updated_at > 1792138437, re-read text + all six previews and check the open items (page 5 desk flag, page 1 footer legibility, page 3 footer size/position) and the checks (page 6 cropped "BRANCH OFFIC" sign, page 4 globe India outline); (c) PPC 2026 folder FAHXTwdMxJ4 and recent designs for a 9:16 set; check every word vs claims review §5 + footer and the safe zone (no text above y=269 or below y=1,248 at 1080x1920), no flag/emblem/logo/timeline/"100% FDI"; (d) CRM COQL for Meta_Lead_Form like '%SIB-05%' (G9). Report a short per-page fix list or "clear for G12". If anything is still open, DRAFT a reply to Vipin on the same thread (from one@setindiabiz.com, cc sanjeev@setindiabiz.com) but do NOT send without Sanjeev's yes. No Meta or CRM changes.
```

## Check first Incorporation lead after LeadChain fix (off)
`trig_019tR2vXX2AxfwpHdQbsNzNP` · created 2026-10-16

```text
Post-fix check (read-only): COQL Leads with Meta_Campaign '#IND 1 — Incorporation' created after 2026-10-16T12:35:00+05:30. Pass = Lead_Source 'Advt - Facebook' or 'Advt - Instagram' matching Meta_Ad_Type (fb/ig), Lead_Channel 'Advt'. Fail = 'Meta Ads' or blank (then the LeadChain Incorporation V2 chain or the 'Auto-set Lead Source from URL' workflow needs a look; propose a backfill, don't write without Sanjeev's OK). If no new lead yet, say so in one line; the 09:40 daily watch's source guard will catch it tomorrow. Append the result to section D of Meta Ads/Change_Log_2026-10-16_IND1-Source-Backfill-and-TM-INC-WhatsApp-Drafts.md and tell Sanjeev in one or two lines.
```

## TM/INC WhatsApp drafts: publish-gate check (off)
`trig_01JxBzhSMxMQgB1McNW6tWaC` · created 2026-10-16

```text
22 Oct publish-gate check for the TM and INC click-to-WhatsApp drafts (read-only; do not publish or activate anything). Read Meta Ads/Change_Log_2026-10-16_IND1-Source-Backfill-and-TM-INC-WhatsApp-Drafts.md first, including section D. Check the four gates: (1) today's 10:00 SIB-04 decision read said KEEP; (2) SalesIQ project shipped the ACR qualifier and the TM/INC fb.me fallback (look for Tiya notes with TM-UNK / INC-UNK or a SalesIQ change log in the project); (3) prepaid balance covers at least 7 days at about ₹12k/day (ads_account_get_activity_logs, budget category); (4) no new #IND1 leads with Lead_Source 'Meta Ads' since 16 Oct 12:00 (LeadChain Incorporation V2 'Meta Ads → Lead Source' row removed). Also confirm via the draft read: ad sets 120247062224450449 / 120247062226170449 PAUSED; TM ad 120247062230580449 and INC ad 120247062314820449 still carry the coded pre-filled messages (TM-C1 / INC-C1) with no active_errors; and whether the two 'DISCARD - …' INC ads (120247062232100449, 120247062311800449) have been discarded. Tell Sanjeev in a few lines which gates pass and, if all pass, give him the publish steps from the change log (discard the two DISCARD ads, do not open the INC ad in the editor, publish via Review and publish, then switch both ad sets on).
```

## Meta lead-quality watch (daily) (ON)
`trig_01DPT99ZCoF8rictq4EsC2bP` · created 2026-10-16

```text
Daily Meta lead-quality watch for Setindiabiz (Meta Ads account 152154124583473, INR; Zoho CRM = source of truth). Runs unattended: never ask questions, never change Meta, never write to Zoho CRM. Read and report only. Times are IST (+05:30).

OPERATING PRINCIPLE (Sanjeev, 16 Oct 2026): "We must work towards good quality consistently over time; cost will come down." Judge every campaign on CRM lead quality first. Never recommend a change for cheaper raw leads. Never recommend reverting a quality change on cost alone while junk is falling and valid is rising.

CONTEXT (read first if the Projects tool is available, project "Meta Ads - Optimisation"): Meta Ads/Audience_Placement_Audit_2026-10-19.md (strict audience/placement standard and per-ad-set scores), Meta Ads/Change_Log_2026-10-19_Audience-Placement-Strict.md (incl. the Ads Manager findings), Meta Ads/SIB-04_Junk_Diagnosis_2026-10-16.md, and the newest Meta Ads/Lead_Quality_Watch_Log.md section. Key finding: junk came from Advantage+ audience plus one-tap WhatsApp on an uncontrolled audience. Hard levers Meta enforces: location, minimum age, language and custom-audience exclusions (plus custom-audience inclusions when Advantage+ audience is off). For Instant-form / Maximise-leads campaigns Meta keeps detailed targeting (titles, interests, behaviours) as suggestions even with Advantage+ audience off (Ads Manager notice, 19 Oct).

CAMPAIGNS: discover all campaigns and ad sets with effective_status ACTIVE each run (ads_get_ad_entities). Known on 19 Oct: SIB-04 Annual Filings (Directors WhatsApp 120247072309210449, Directors Form 120247072301790449), #IND 1 — Incorporation (24Hr INSA 120240912969640449), SIB-02 Trademark - Copy (ad set 120247094867020449; original SIB-02 campaign deleted 18 Oct), SIB-05 India Entry (campaign 120247067847480449; India Entry 120247067863750449, Subsidiary 120247068431610449, Branch-Liaison 120247068705380449) once Sanjeev publishes it.

CRM DEFINITIONS (Leads module, COQL):
- Paid Meta leads: any lead with Meta_Campaign not empty, OR Lead_Source in ('Advt - Facebook','Advt - Instagram','Advt - WhatsApp'). Campaign via Meta_Campaign ('SIB-04 Annual Filings', '#IND 1 — Incorporation' with an em dash, 'SIB-02 Trademark', 'SIB-02 Trademark - Copy', 'SIB-05 India Entry', and any new value). Path = WhatsApp if Lead_Source 'Advt - WhatsApp', else Form.
- SOURCE GUARD: the correct Lead_Source for paid Meta leads is 'Advt - Facebook' / 'Advt - Instagram' / 'Advt - WhatsApp', with Lead_Channel 'Advt'. Any lead with Meta_Campaign set but another Lead_Source is invisible to the Conversions API sweep. Count these per campaign every run and flag them first.
- Junk: Why_Disqualified in ('Inquired by Mistake','Job Seeker','Bot Created/Spam','Wrong Info') OR RM_Lead_Quality / Mkt_Leat_Quality = 'Invalid - Bot/Job/Irrelevant'.
- Valid: Lead_Status in ('Valid Lead','Negotiation','Proposal Sent','Payment Pending') OR RM_Lead_Quality / Mkt_Leat_Quality starts with 'Valid'.
- Unworked: Lead_Status null or 'Establishing Contact'.
- Exclude test lead 1123581000948692001.
- COQL quirks: nest conditions in pairs, ((a and b) and c); more than ~4 ORs fails; GROUP BY is unreliable, so pull rows and count yourself; results over ~25k tokens are saved to a file, so parse that file with python.

STEPS
1. DELIVERY: yesterday's spend and results per active ad set; ads_get_errors on the account's active campaigns; flag any active ad set with ₹0 spend yesterday. If total account spend was ₹0, check ads_account_get_activity_logs (event_category budget) for billing / prepaid balance and say so first; funding is human-only. Estimate the remaining prepaid balance from the latest "Money added to balance" (top-ups carry 18% GST: ad credit = top-up ÷ 1.18) minus later "Account billed" entries and unbilled spend, and warn if it covers less than 1.5 days of current budgets.
2. QUALITY SCORECARD per campaign × path (Form / WhatsApp), for three lead cohorts by Created_Time: (a) yesterday, (b) last 7 days, (c) matured cohort = created 10 to 4 days ago. For each: leads, junk %, valid %, unworked %, top 3 Why_Disqualified. Cost per valid lead for (b) and (c) from ad-set spend. Targets: junk ≤ 15%, matured valid ≥ 40%. Compare with the previous run in the log and say whether quality is improving, flat or worse.
3. STRICT GUARDRAIL AUDIT (standard set 19 Oct 2026) on every ACTIVE ad set, from a fresh targeting read:
   a. Language: locales present (English 6 and 24; SIB-05 also 11 Japanese, 12 Korean). Missing = BREACH.
   b. Minimum age ≥ 25. Missing = BREACH.
   c. Location: India ad sets have a city list; SIB-05 has exactly the 7 countries US, AE, SG, KR, JP, AU, CA. Location types home + recent are acceptable (Meta removed home-only); `frequently_in` or `travel_in` = FLAG. `targeting_automation.individual_setting.geo = 1` (location expansion) = FLAG (known on SIB-02 Copy until Sanjeev approves turning it off). Any country added to SIB-05 = BREACH.
   d. Audience: Directors ad sets and all SIB-05 ad sets must have targeting_automation.advantage_audience = 0 and no `targeting_optimization: expansion_all`; Directors keep the 7 Company Director lists with relaxation lookalike 0 / custom_audience 0. SIB-05 should keep both flexible_spec groups (job titles; business-decision-maker behaviours/industry) — note they are suggestions on this campaign type. Any reversion = BREACH (Ads Manager silently reverted an audience on publish on 16 Oct).
   e. Placements: Directors and SIB-05 should have publisher_platforms facebook + instagram only, facebook_positions feed/story/facebook_reels, instagram_positions stream/story/reels (Meta is withdrawing ad-set placement exclusions; if they disappear, say so and rely on account controls). For every active ad set, pull last-7-day spend by ['publisher_platform','platform_position'] and report spend outside FB/IG Feed, Stories and Reels as % of spend; FLAG above 2%; any Audience Network, Marketplace or Threads spend = BREACH.
   f. Exclusions: note whether any custom-audience exclusion is attached (none exist as of 19 Oct; planned X1 instant-form submitters 180d, X3–X5 CRM lists).
   Report PASS / FLAG / BREACH per ad set in one line each.
4. WHATSAPP SIGNALS: for leads created yesterday with Lead_Source 'Advt - WhatsApp' or 'Social - WhatsApp', read their Notes titled 'Zoho SalesIQ chat with Tiya…' and count chats opening with a coded message ([ACR-Cn], [TM-Cn], [INC-Cn], [LLP-Cn]) or the WhatsApp-form message vs Meta's standard greeting. Flag any 'Social - WhatsApp' lead whose first message starts with https://fb.me/ or https://www.instagram.com/p/. Count chats written in an Indian script and leads carrying a "Duplicate Record" note.
5. SPEED: count paid leads older than 24 h still unworked, by owner. Resolve owner IDs with getUsers, because COQL returns surnames only.
6. RECOMMEND at most 1–2 quality changes, each with the metric that will confirm it. Never execute them. Open stop-losses to evaluate: SIB-04 Directors (read 23 Oct: keep if rejected ≤25% of worked, pause if >40%); SIB-05 after launch (capture stop: 2 spend days with 0 CRM leads; under-delivery: spend <50% of ₹4,000 CBO on 2 consecutive days → recommend removing the second flexible_spec group; junk >40% of worked over 3 days → recommend pause; day 7: split by country).
7. LOG: if the Projects tool is available, append a dated section to Meta Ads/Lead_Quality_Watch_Log.md (read it, then write the full content back; create it if missing). Keep each day's section under 40 lines.

OUTPUT: one short message to Sanjeev: a table (campaign × path: leads, junk %, valid %, unworked %, cost per valid) plus 3–4 bullets (any source-guard, funding or guardrail BREACH first, then what changed vs yesterday, recommendations). If nothing material changed and no flag fired, end with one terse line.
```

## SIB-04 audience change decision read (off)
`trig_01MPVr6hm9VZN8k3E8v8H8Dp` · created 2026-10-16

```text
22 Oct decision read (Meta Ads project). Read Change_Log_2026-10-16_SIB-04-CTWA-Audience-Controls.md and SIB-04_Junk_Diagnosis_2026-10-16.md first.

OPERATING PRINCIPLE (Sanjeev, 16 Oct 2026): consistent lead quality comes first; cost per lead will come down as quality holds. Judge on CRM quality, not on Meta cost.

Measure the SIB-04 WhatsApp ad set (120246968316940449) for 17–19 Oct: spend from the connector; CRM leads with Meta_Campaign 'SIB-04 Annual Filings', Lead_Source 'Advt - WhatsApp', created in the window. Report junk% (Why_Disqualified in Inquired by Mistake / Job Seeker / Bot Created/Spam / Wrong Info, or an Invalid quality field), valid% (status Valid Lead/Negotiation/Proposal Sent/Payment Pending or a quality field 'Valid%'), unworked%, and cost per valid lead. Baselines: 27% junk, 18% valid, ₹502 per valid (9–15 Oct, read 16 Oct); same-age cohort 25% junk. Show the Form ad set (untouched) as the control.

QUALITY-FIRST DECISION RULES:
- KEEP the change if junk% is lower than baseline and valid% is not lower, even if cost per valid has risen. Higher cost on its own is NOT a reason to revert.
- Recommend REVERT (remove locales, age_min back to 18) only if quality did not improve (junk% not lower AND valid% lower), or if the ad set cannot deliver (spent under 50% of its ₹3,500 daily budget on all 3 days).
- If junk% is still above 15%, stage Change 2 as an Ads Manager draft for Sanjeev to publish (do not publish it): WhatsApp ad-set location = the 19 CCFS cities at 25 mi (copy geo_locations.cities from ad set 120244101705150449), keeping everything else including locales, age_min 25 and Advantage+ audience. targeting replaces the whole spec, so carry every other field forward unchanged.

Check whether the SalesIQ project has shipped the ACR qualifying question (it changes junk counts). Log the result in the change log and tell Sanjeev in a few lines.
```

## SIB-04 placement read + check audience change is live (off)
`trig_01H2MNnoWAEHnht4NmEhxySb` · created 2026-10-16

```text
17 Oct check-in (read-only, Meta Ads project). Read Change_Log_2026-10-13_Placement-Controls.md and Change_Log_2026-10-16_SIB-04-CTWA-Audience-Controls.md first.
1) Confirm the 16 Oct audience change on SIB-04 WhatsApp ad set 120246968316940449 is LIVE (targeting shows locales [6,24] and age_min 25, no pending draft, ACTIVE, ads_get_errors empty). If it is still a draft, remind Sanjeev to click Publish in Ads Manager.
2) Run the 13 Oct placement-controls stop-loss read: campaign and per-ad-set cost per CRM valid lead for 14–15 Oct (WhatsApp ad set) and 14–16 Oct (Form ad set), against baseline ₹731 / revert ₹914 (CTWA ₹529 / ₹662, Form ₹1,943 / ₹2,428). Note that WhatsApp 16 Oct is mixed by the audience change. Recommend keep or revert; make no change.
3) Append the result to the 16 Oct change log and tell Sanjeev in 3–4 lines.
```

## Check WhatsApp click signature after secret re-paste (off)
`trig_01SbUGLBwzXTsPNX4UFaf7Pe` · created 2026-10-15

```text
Check-in: Sanjeev re-pasted meta_wa_app_secret at ~15:37 IST. Query WA_Ad_Clicks created after 15:37 IST and report the Signature_Check of the newest click(s): "ok" means the secret is fixed; still "mismatch n0 cx" means look at the remaining cause (Zoho altering the body). Read-only; never read or print the secret. Also remind Sanjeev that the two assignment rules are still waiting on his answer about which pool(s) Sudip, Foziya, Himanshu Singh and Shubendu join.
```

## Re-check WhatsApp ad click capture (off)
`trig_01U6GxLH24u4Gn6v8GcExtus` · created 2026-10-15

```text
Re-check CTWA click capture (Step 1, second pass). 1) Confirm SIB-04 (campaign 120246968311680449) resumed delivery after the ₹25,000 top-up at 10:24 IST: hourly spend today via the Meta connector. 2) COQL on WA_Ad_Clicks (all fields). 3) If clicks exist: confirm Signature_Check = ok, Ad_ID is one of the 4 CTWA ads (120246968790550449 ACR-C1, 120246968981980449 ACR-C2, 120246969045870449 ACR-C5, 120246969168420449 LLP-C1), and whether sib_wa_click_match has linked them to 'Advt - WhatsApp' leads (runs every 2h). 4) If delivery resumed but zero clicks, compare against today's 'Advt - WhatsApp' lead count and ask Sanjeev to tap a live SIB-04 ad and send the pre-filled message. Report briefly; don't start W6 CRM writes without his approval.
```

## Check 20:00 CAPI sweep run (off)
`trig_01SLpfavHj2nwZBbypPJbkVy` · created 2026-10-13

```text
Read-only CAPI check: did the 20:00 run of sib_capisweep mark leads 1123581000946568358 and 1123581000946574748 as Meta_CAPI_Sent = true? Use getTimelines (look for the Meta_CAPI_Sent change by sib_capisweep, source custom_function) and the COQL backlog query (paid leads since 6 Oct, valid or progressed, Meta_CAPI_Sent = false). Report the result to Sanjeev in one line and add it to the 13 Oct evening change log.
```

## Placement change 3-day stop-loss review (off)
`trig_01QQz33Y8aEZqJsgUbvg2UYC` · created 2026-10-13

```text
Stop-loss review for the 13 Oct account-level placement exclusions (see Meta Ads/Change_Log_2026-10-13_Placement-Controls.md). For 14–16 Oct: spend per ad set from the Meta connector; CRM valid leads per ad set from Zoho using the baseline method (CTWA = Advt - WhatsApp + untagged Self - Web Chat with a Tiya - Annual Filings chat; Form = Advt - Facebook/Instagram tagged FB-ACR). Compare to thresholds CTWA ₹662, Form ₹2,428, campaign ₹914 per valid. Confirm AN and Marketplace spend is ₹0. If a threshold is breached, recommend reverting (Sanjeev approves; don't change Meta yourself). Report to Sanjeev and log the result in the project.
```

## Check AN/Marketplace spend stopped (off)
`trig_013nhqNCwxe2XezmtHoDdCVM` · created 2026-10-13

```text
Propagation check for the 13 Oct account-level placement exclusions (account 152154124583473). Pull today's spend by publisher_platform + platform_position for ad sets 120246968316940449 (CTWA) and 120246968737470449 (Form). Pass = CTWA Audience Network still ≈ ₹411.20 (classic 389.71 + rewarded 21.49) and Marketplace ≈ ₹1.22, i.e. no growth since the 12:34 snapshot; both ad sets ACTIVE with no errors. Append the result to Meta Ads/Change_Log_2026-10-13_Placement-Controls.md and tell Sanjeev in one or two lines. Read-only — no Meta changes.
```

## Lead Assignment Rule Daily Check (off)
`trig_0142dx52rfEJxFz4Q8kxsh4w` · created 2026-10-07

```text
You are auditing Setindiabiz's Zoho CRM lead assignment rule "Lead - General 2026" (Leads module, rule id 1123581000823594437) for Sanjeev Kumar (sanjeev@setindiabiz.com). This is a READ-ONLY audit: never update, reassign or delete any lead, rule or setting. Use the Zoho CRM connector tools (executeCOQLQuery, getAssignmentRules, getUsers). Times are IST (+05:30).

STOP CONDITION: This check runs daily from 8 Oct to 14 Oct 2026. If today's IST date is after 2026-10-14, do not audit: disable this scheduled task (use list_triggers to find "Lead Assignment Rule Daily Check", then update_trigger enabled=false), tell the user the 7-day monitoring has ended, and stop. On the 14 Oct run, do the audit, then disable the task and add a 7-day wrap-up.

WINDOW: leads created from 00:00 yesterday to 00:00 today IST. On the first run (8 Oct) use 2026-10-07T15:05:00+05:30 to 2026-10-08T00:00:00+05:30 (the new rule went live ~15:03 on 7 Oct).

STEP 1 - Rule still intact: call getAssignmentRules for module Leads. Expect exactly one rule, "Lead - General 2026". Flag if any other Leads rule exists or its modified_time is later than 2026-10-07T15:05+05:30 (someone edited it).

STEP 2 - Pull leads: COQL select Lead_Number, Product_Category, Tag, Owner.email, Created_By.email, Lead_Source, Created_Time from Leads where Created_Time between the window, paginate with limit 200 / offset until done. Exclude: Lead_Source = 'Self - Cold Call' (Bigin flow sets owner itself); leads whose Created_By.email is not sanjeev@setindiabiz.com (created manually by staff - rule not applied). Everything else is rule-routed.

STEP 3 - Expected owner pool. The first matching sub-rule wins, in this order (match if Product_Category is in the list OR the lead has one of the listed tags). Emails: all are @mail.setindiabiz.com except praveen@, santosh@, karishma.singh@, foziya.ansari@, shubendu.banerjee@, jitendra.singh@, suman.khowal@, shubhlam.singhal@, amit.bhatnagar@ which are @setindiabiz.com.
1 Junk: Aayush, Job Seeker, Pest Control -> amit.bhatnagar (Lost Records)
2 LG-01 Entity Setup: Start Company, Start LLP, Start Firm, Start Proprietorship, Start HUF, Name Approval, Digital Signature; tags FB-INC, FB-INCORP -> tarun.kumar, mahima.sehrawat, anish.singh, amit.kumar3, aditya.bisht, krishna.gupta, rama.dwivedi, praveen, santosh
3 LG-02 FDI/FEMA: FDI, BO-LO-PO, Overseas Incorporation, RBI and Fema -> karishma.singh, gaurav.pandey, rishika.singh, foziya.ansari, shubendu.banerjee
4 LG-03 Finance & Fintech: Fincorp, SEBI, IRDA Services -> jitendra.singh, praveen, santosh, rama.dwivedi
5 LG-04 Post-Inc: Post INC -> tarun.kumar, mahima.sehrawat, anish.singh, amit.kumar3, aditya.bisht, krishna.gupta
6 LG-05 Startup & Schemes: DPIIT, Govt Initiative and Subsidy; tag FB-DPIIT -> rishika.singh, pragya.agrawal, amit.kumar3, priyam.tiwari, krishna.gupta
7 LG-06 Basic Registrations: FSSAI, MSME, Govt Registrations, Import, Barcode, GEM Portal -> anshu.yadav, krishna.gupta, aditya.bisht, gaurav.pandey, mahima.sehrawat
8 LG-07 NGO: Start NGO, Start Sec 8, NGO Tax Compl -> gaurav.pandey, pragya.agrawal, rishika.singh, priyam.tiwari, aditya.bisht
9 LG-08 Advanced Licensing: Psara License, Drug, FDA and CDSCO, BIS, Environment, Factory License, Industrial License, Legal Metrology, Foreign Certification, Indian Certification, DGFT, Export, RCMC, Telecom, Trade License, Regulatory - Others -> tarun.kumar, pragya.agrawal, amit.kumar3, anish.singh, gaurav.pandey, jitendra.singh, rama.dwivedi
10 LG-09 IP: Copyright, Design IPR, Patent, International TM, TM Amendement, TM Assignment, TM Certified Copy, TM Evidence Filing, TM Filing in India, TM Legal Matters, TM Notices, TM Objection/SCH, TM Opposition, TM Renewal; tags FB-TMF, FB-CA-IPR -> anshu.yadav, krishna.gupta, aditya.bisht, gaurav.pandey, mahima.sehrawat
11 LG-10 Accounts & Tax: Accounting, CA Certifications, CA Other Services, CFO, GST Return, GST LUT, GSTN Related, GST Legal, Income Tax, Zoho Books, Valuation; tag FB-CFO -> tarun.kumar, anish.singh, priyam.tiwari, amit.kumar3, shubendu.banerjee, praveen, santosh
12 LG-11 Secretarial: Annual Filing, Address Change, Auditor, CS Other Services, Director KYC, Director or DP, Name and Object, Striking Off, LLP Agreement, MCA Login Creation, Government Survey Returns, Retainerships; tags FB-ACR, FB-LLPACR, FB-STK2, FB-LLPCLOSE, FB-CCFS -> pragya.agrawal, rishika.singh, tarun.kumar, mahima.sehrawat, anish.singh, amit.kumar3, priyam.tiwari, gaurav.pandey, suman.khowal, praveen
13 LG-12 Corporate Transactions: Capital, Conversion -> shubhlam.singhal, praveen, gaurav.pandey
14 LG-13 Payroll/Labour/HR: Payroll Processing, EPFO, ESIC, Professional Tax, Labour Welfare Fund, Labour Law Other Matters, POSH, Shops Act, HR Drafting -> shubhlam.singhal, praveen, gaurav.pandey
15 LG-14 Legal: Legal Drafting, Court Matters, NCLT -> shubhlam.singhal, praveen, gaurav.pandey
16 Catch-all (blank, Miscellaneous, Partner Engagement, Website and Designing, anything else) -> pragya.agrawal, rishika.singh, priyam.tiwari, aditya.bisht, amit.kumar3, gaurav.pandey, mahima.sehrawat, tarun.kumar, krishna.gupta
Default assignee (used when nobody in the pool is online, or no rule applied): sanjeev@setindiabiz.com.
Note: Tag holds a list of {name,...}; compare by tag name.

STEP 4 - Compare each rule-routed lead's current owner with its expected pool. Classify: OK (owner in pool); DEFAULT (owner is sanjeev - pool offline or rule not applied); MISMATCH (anyone else). For each MISMATCH, check with COQL/getRecord whether the owner may have been changed after creation (e.g. Modified_By not sanjeev, or the lead is linked to an existing account) and say so. Known pre-existing pattern to watch: on 7 Oct a 'Miscellaneous' lead (L482755) went to Amit Bhatnagar Lost Records and a blank-category web-chat lead (L482756) went to Sanjeev - both before the new rule; report whether this repeats.

STEP 5 - Also report: count of leads per group (LG-01..LG-14, junk, catch-all) and per owner within each group, to show round-robin spread; categories hitting the catch-all most (candidates to map to a group); any owner appearing who is inactive or whose name starts with "Zx".

OUTPUT: Send the user one concise message (SendUserMessage if available; otherwise final reply): headline verdict (rule working / issues found), counts (rule-routed, OK, DEFAULT, MISMATCH, excluded), a short table of every MISMATCH and DEFAULT lead (Lead number, category, owner, expected group, likely reason), per-group spread, and any recommended fix (as a suggestion only - do not change CRM). Keep it under ~25 lines unless there are many mismatches.
```

## Weekly paid-channel measurement report (ON)
`trig_019kCqpnADCtD4YA7xNyXSrF` · created 2026-08-23

```text
Produce the weekly paid-channel measurement report for Setindiabiz, covering the previous Monday–Sunday.

Judge every channel on CRM outcomes, never on platform-reported conversions.

1. Meta Ads: use the Meta Ads tools on ad account 152154124583473 (SETINDIABIZ, INR). Pull campaign-level amount_spent, impressions, results and cost_per_result for the week.
2. X Ads: open https://ads.x.com/manager/18ce54c2t0g/campaigns in Chrome (Claude in Chrome tools) and read spend, impressions, link clicks, CTR and conversions for the week. X bills this account in USD — state the USD figure and note the rupee conversion is approximate.
3. Zoho CRM: query the Leads module with COQL for leads created in that week. Break down by Lead_Source and by UTM_Source / UTM_Campaign, and split each source by Lead_Status and RM_Lead_Quality so cost per VALID lead can be computed, not just cost per raw lead.
4. Compute cost per CRM lead and cost per valid CRM lead for each paid channel, and compare week over week.
5. Flag: any channel whose platform-reported conversions diverge sharply from its CRM lead count (that is the signature of a misconfigured pixel event); any leads arriving with an empty UTM_Source despite a UTM-bearing First_Visited_URL; and any campaign that stopped delivering.

Read the project memory files x_ads_performance_audit.md and x_ads_measurement_fixes.md first for context and known issues. Deliver the report as a file to the user and keep it short — a table plus the three or four things that changed.
```

## Monthly LeadChain phone reconciliation (ON)
`trig_01NSKwVPGmF7mC2mF4heq1y1` · created 2026-08-16

```text
Monthly LeadChain reconciliation for Setindiabiz (Zoho CRM org `setindiabiz`).

Context: Zoho CRM lead phone numbers can drift from what the visitor actually submitted. Two known causes: capture forms (Meta Instant Forms, SalesIQ) attach a country code the visitor never typed, and agents sometimes edit the number by hand in the CRM UI. The LeadChain export is the only record of the submitted value, and LeadChain has no API, so the export is manual. Background is in the Claude project "Zoho CRM & Desk Deduplicate" — read `claude/claude_Zoho_CRM_Dedup_-_ROOT_CAUSE_and_solution_16Aug2026.md` first.

What to do this run:

1. Message Sanjeev asking him to export every chain from the LeadChain web tab (https://crm.zoho.com/crm/setindiabiz/tab/WebTab5 — open each chain, use the download icon) and attach the CSVs. Explain in one line that LeadChain's own export window is roughly 90 days, so anything not exported is lost for good.
2. When the CSVs arrive, join them to CRM Leads on `leadchain0__Social_Lead_ID` via COQL.
3. Report every record where the CRM `Phone` digits differ from the exported `PHONE NUMBER` digits.
4. Write each mismatch to the `Phone_Country_Check` field on that Lead, with the submitted value and the date. **Do not change any phone number.** An automated join made six wrong corrections on 16 Aug 2026; the RMs settle these on a call.
5. Save a dated reconciliation CSV to the project.

Standing rule for this account: reading and analysing CRM data is fine unprompted, but ask Sanjeev before any production write and show the change first.
```
