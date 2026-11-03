# SetIndiaBiz Meta Ads — Daily Scorecard
**9 Aug 2026 (Sunday)** | Account: SETINDIABIZ 152154124583473 | Source of truth: Zoho CRM, `Lead_Source IN ('Advt - Facebook','Advt - Instagram')`

*Cross-checked against project memory (last watchdog entry: 24 Jul). Budget figures for INSA/TM ad sets below are from that 16-day-old entry — I didn't re-pull current `lifetime_budget`/`daily_budget` this run, so treat those specific numbers as last-known, not verified-today.*

## 🚨 Top finding: 5-day blackout, 1–5 Aug (new — not yet in memory)
Account-level daily spend (1–8 Aug) shows **zero spend/impressions/clicks on Aug 1–5**, confirmed on the CRM side too (zero paid leads those days). Delivery resumed Aug 6. This extends a recurring pattern already on record (18 Jul full blackout, 23 Jul full blackout, both spend-limit/billing related) — but at 5 days it's the longest yet. **Action: check Ads Manager → Billing** (billing changes are human-only).

| Date | Spend | Impr. | Clicks | CRM paid leads |
|---|---:|---:|---:|---:|
| 1–5 Aug | ₹0 | 0 | 0 | 0 |
| 6 Aug | ₹11,824.74 | 38,694 | 381 | 35 |
| 7 Aug | ₹17,836.28 | 86,262 | 772 | 79 |
| 8 Aug (yesterday) | ₹8,474.57 | 43,498 | 466 | 41 |

"7-day" and "trailing baseline" figures below are really **3-day (6–8 Aug) recovery data** — glidepath comparisons are directional only this week.

## 🚦 A1 — Delivery & spend (yesterday, 8 Aug)
Spend ₹8,474.57, impressions 43,498, clicks 466. Not dark. This is **not a new pattern** — memory shows Sun 19 Jul landed at ₹8,474.58, essentially the identical figure (1 paisa apart). So this "half-cap" tier (½ × ₹16,949.15) recurs on low-delivery days regardless of exact weekday (was Sunday in Jul, is Saturday now) — consistent with the account's spending-limit mechanics, not a tracking issue. Separately, 7 Aug spend (₹17,836.28) is comfortably above the ₹12,711.86 confirmed weekday ceiling (per 21 Jul finding) — a second data point that the cap has room above the old ₹12,711.86 level, in line with the 22 Jul "raised to ~₹21k" observation. Worth re-confirming the current effective daily cap since it's moved at least twice since 21 Jul.

## A2 — CRM inflow vs recent trend
Yesterday: **41** paid leads vs 57/day average for the immediate pre-period (Aug 6–7). That's –28%, not a >50% flag, and it tracks the spend drop (Aug 8 spend ≈ 48% of Aug 7's) rather than looking like a sync break. A longer 7-day baseline isn't meaningful this week because of the blackout.

## A3 — Stop-loss & trigger board
| Item | Read | Verdict |
|---|---|---|
| C1 Daytime INSA | Matured (6–7 Aug, excl. fresh Aug-8): valid **58.3% (14/24)**. 3-day blended CPL ₹177 | ✅ Healthy |
| C1 24Hr INSA | 3-day blended valid 22.2% (6/27) *looked* like a breach, but **matured 6–7 Aug read is 31.6% (6/19), just above the 30% floor** — this is the known grading-lag trap (a 3-day window including a fresh, mostly-ungraded yesterday under-reads valid%). **Not calling a revert on this.** CPL ₹130, fine either way. | ⚠️ Borderline — watch, don't revert |
| IND3 TM (TMF-SA + Director-TMF) | 3-day CPL ₹135, valid 47.8% (32/67); matured (6–7) valid 53.3–55.2% per ad set | ✅ Healthy. Per memory, TM was already raised to TMF-SA ₹150,000 / Director-TMF ₹60,000 on 14 Jul — **no further ramp is due**; the ₹100k→₹109k trigger in the original task file is explicitly superseded (do not re-apply it) |
| DPIIT (#IND5) | `CAMPAIGN_PAUSED`, ₹0 spend, 0 leads | ✅ This is the **standing intentional pause** Sanjeev confirmed 14 Jul ("not converting as sales") — continuing to hold correctly, not a new issue |
| Must-stay-paused (#IND6, C1 Daytime/24Hr LAL1%) | All PAUSED/CAMPAIGN_PAUSED | ✅ Clean |
| CCFS (#IND4) | ₹6,685.52/day — prior readings ranged ₹1.4k–3.8k/day, all inside the healthy band | 🚨 **New pacing anomaly**, >2× anything seen since 10 Jul and above the ₹5k flag line — worth checking remaining lifetime budget against the 31 Aug scheme end |
| C1 Daytime INSA lifetime budget | Still delivering 9 Aug; memory shows an **open, unresolved question since 20 Jul** about extending its end date (was tracking to strand ~₹38–42k against a 30 Jul end) | ⚠️ Still open — needs Sanjeev's call, not new |

## A4 — Yesterday's quality & funnel
Aug 8 cohort (n=41): Valid Lead 5, Establishing Contact 28, Proposal Sent 4, Postponed 1, blank 3 → **valid 24.4% (10/41)** — low, but expected given most of the cohort hasn't been graded yet (grading-lag, see A3). Progressed 4, lost 0 (too fresh). Cost/valid ≈ ₹847 on this immature read.

**Form-change watch:** 6–8 Aug junk-loss share (Inquired by Mistake + Job Seeker) = 4/16 = **25%**. Memory's 21 Jul read had this fully resolved at 6.7% — today's small post-blackout sample is noisier (16 losses) and shouldn't be over-read, but worth one more clean day to confirm it's still under control.

## A5 — Campaign scorecard (6–8 Aug ≈ this week's usable data)
| Campaign | Spend | Leads | CPL | Valid | Valid% | Cost/Valid | Progressed | Cost/Prog |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| #IND3 - Trademark | ₹9,069.64 | 67 | ₹135.37 | 32 | 47.8% | ₹283.43 | 17 | ₹533.51 |
| #IND 1 — Incorporation | ₹9,009.38 | 58 | ₹155.33 | 20 | 34.5% | ₹450.47 | 4 | ₹2,252.34 |
| #IND4 - CCFS | ₹20,056.57 | 28 | ₹716.31 | 16 | 57.1% | ₹1,253.54 | 5 | ₹4,011.31 |
| #IND5-DPIIT / #IND6 / #IND2 (×2) | ₹0 | 0 | — | 0 | — | — | 0 | — |
| **TOTAL** | **₹38,135.59** | **155**¹ | **₹246.04** | **68** | **44.4%** | **₹560.82** | **26** | **₹1,466.75** |

¹ incl. 2 leads with null Meta_Campaign (1.3%, well under the 10% alarm line).

**Glidepath:** on 24 Jul (pre-blackout), blended CPL was ₹224 @48.2% valid, ahead of checkpoint. Today's ₹246 @44.4% is a mild step back — expected after a 5-day dark stretch feeding into a 3-day recovery read, not itself alarming. CCFS remains the weakest cost/valid (₹1,254) and is also the pacing outlier flagged in A3.

## A6 — CAPI channel health: 🟢 GREEN
Server last fired ~12.7h ago, client pixel ~25 min ago. Last 72h SERVER_ONLY: **34 ValidLead + 22 Purchase**. Lower than the 24 Jul read (66+104) but that period included a large Purchase batch and predates the blackout — not a concern on its own. Per-ad-set gate progress toward the switch isn't separable from this endpoint; would need a `Meta_CAPI_Sent` × `Meta_Ad_Set` CRM cross-tab to size precisely.

## A7 — Speed-to-lead exceptions: 🚨 severe, and shifted to new owners
Of 119 paid leads created in the last 48h, **66 (55.5%) are still untriaged** (null / Establishing Contact / Postponed) — this recurring problem (previously flagged 6/15/18/20 Jul against different owners each time) has now moved to different reps. Top 10 oldest, all ~44.5–45.7h old, still in Establishing Contact:

| Lead | Phone | Owner | Age | Status |
|---|---|---|---|---|
| A.Nolakha | +919529993833 | Agrawal | 45.7h | Establishing Contact |
| Ashok Kumar | +919805186240 | Kumar | 45.7h | Establishing Contact |
| john | +919513555566 | Sehrawat | 45.7h | Establishing Contact |
| mithlesh Kumar Chauhan | +919792317018 | Pandey | 45.5h | Establishing Contact |
| Subham | +918462903514 | Agrawal | 45.1h | Establishing Contact |
| Advocate vishal yadav | +919660327991 | Kumar | 45.0h | Establishing Contact |
| Anandarao John Chinthaguntla | +919652059668 | Kumar | 44.9h | Establishing Contact |
| Dipak Majumder | +917063263423 | Bisht | 44.8h | Establishing Contact |
| Saurabh Agarwal | +918383090469 | Sehrawat | 44.8h | Establishing Contact |
| shishir | +918827118571 | Tiwari | 44.5h | Establishing Contact |

**Owner concentration (stale ÷ total assigned in 48h, by owner ID):** Kumar (…898222001) 11/11 = **100% stuck**; Yadav (…919146001) 7/7 = **100% stuck**; Kumar (…005475021) 8/9 = 89%; Sehrawat 9/14 = 64%; Tiwari 6/12 = 50%. Note this is a *different* Kumar ID than the one flagged 6/15/20 Jul (…006825001, only 2 stale this time) — the bottleneck keeps recurring but keeps moving between reps, which points at a process gap (no SLA/alerting) rather than one person.

*(Status+age remains a proxy — first-contact latency isn't directly instrumented. CAPI test lead 1123581000888516561 not present in this window.)*

## A8 — Loss buckets
Yesterday alone: 0 losses (too fresh). Using 6–8 Aug (16 losses, small sample):

| Bucket | Reasons | Share |
|---|---|---|
| Qualification/junk | Language Issue(2), Inquired by Mistake(3), Job Seeker(1), No Product Offering(1) | 7/16 = 44% |
| Ambiguous / possible sales-process | Not Interested(5) | 5/16 = 31% |
| Pricing/competition | Other CA(2) | 2/16 = 12.5% |
| Natural attrition | Plan Drop(1) | 1/16 = 6% |
| Geography/serviceability | Not Eligible(1) | 1/16 = 6% |
| Targeting | — | 0% |

Small sample (post-blackout restart) — treat as directional. Targeting at 0% is consistent with the general instruction not to blame targeting first.

## A9 — Pilot monitors
No campaign/ad-set in the account matches a call-ads or CTWA pilot; no WA-stamp field checked this run. Reporting all four as **not launched / no gate data this run**: WA auto-follow-up, TM call-ads, CTWA, website-conversion retest.

## Part B — Lead-source QA sweep
- B1 Chat stragglers (2d): clean
- B2 Blank sources: clean
- B3 Stray labels (2d, all sources): 1 hit — **"Zoho Bookings" → corrected to "SEO - Zoho Booking"** (record 1123581000925808003, `trigger:[]`)
- B4 Stamped-value contradictions: UTM↔Lead_Source cross-tab, 2 rows, both consistent — clean
- B5 Meta placement integrity: clean
- Writes this run: **1**

## ✅ Recommended for approval (2)
1. **Resolve the C1 Daytime INSA lifetime end-date question** — open since 20 Jul per project notes, still unresolved as of today, and the ad set is still delivering past its last-known 30 Jul end reference, so this needs a decision either way (extend the end date, or confirm it was already handled and I'm working from a stale note). Not a number I'm proposing — just needs your call recorded so it stops recurring.
2. **Check CCFS remaining lifetime budget** — pacing jumped to ₹6,685.52/day (>2× anything seen in the last month, above the ₹5k flag line). At this rate it could exhaust well before the 31 Aug scheme-extension end date. Confirming action: pull remaining lifetime budget vs. days left; if the pace is intentional (catching up after the blackout), no change needed — otherwise dial back.

**Not recommending a TM or INSA budget change this run** — TM is already at its last-approved level with no new trigger met, and the apparent 24Hr INSA valid% breach turned out to be a grading-lag artifact once checked against the matured window. Next run should re-pull current `lifetime_budget`/`daily_budget` on the INSA and TM ad sets to refresh what's now a 16+ day-old baseline in memory.

*Ad-LEVEL changes still require the Ads Manager browser route (API blocked by leadgen-ToS error 1815089); campaign/ad-set level is fine via API. Nothing above was executed — awaiting approval. No Zoho Analytics publish tool available in this session; this file is today's record.*
