# SetIndiaBiz Meta Ads — Daily Watchdog
**Run date:** Tuesday, 11 August 2026 (report compiled ~19:00 IST) · **Yesterday scored:** Monday, 10 August 2026
**Account:** SETINDIABIZ (152154124583473) · **Source of truth:** Zoho CRM (paid segment = `Advt - Facebook` + `Advt - Instagram`)

---

## 🚨 Headline: second blackout in under two weeks

Meta delivery went **dark for ~38 hours**, from **10 Aug 00:00 IST through ~11 Aug mid-afternoon**. It has **since recovered** (confirmed as of this report). No delivery-blocking errors were found on the account (`ads_get_errors` returned empty) and the account itself is `ACTIVE` with a valid payment method — this points to the **account spending limit** being hit again, not a policy/billing failure. Please check **Ads Manager → Billing** to confirm/raise the cap.

This is the second cap-driven blackout following the 27 Jul–5 Aug outage — only **4 clean delivery days** (6–9 Aug) elapsed in between.

## 🚦 Delivery & spend

| Date | Spend | Impr. | Clicks | CRM paid leads |
|---|---|---|---|---|
| 3–5 Aug | ₹0 | 0 | 0 | 0 (tail of prior blackout) |
| 6 Aug | ₹11,824.74 | 38,694 | 381 | 35 |
| 7 Aug | ₹17,836.28 | 86,268 | 772 | 79 |
| 8 Aug | ₹8,474.57 | 43,635 | 468 | 41 |
| 9 Aug | ₹8,474.58 | 28,984 | 269 | 17 |
| **10 Aug (yesterday)** | **₹0.01** | **1** | **0** | **0** 🚨 |
| 11 Aug (today, partial, as of 19:00 IST) | ₹6,029.79 | 20,703 | 160 | 11 (first new lead 15:25 IST) |

Aug 8–9 both landing at an identical ~₹8,474.57 (almost exactly half the documented cap-day signature ₹16,949.15) suggests the account was already pacing against a constrained cap before going fully dark on the 10th.

## Inflow vs 7-day baseline
Yesterday: **0 paid CRM leads** vs a 7-day (4–10 Aug) daily average of **24.6/day** → **-100%**, full-day outage. Not a LeadChain sync break (Meta spend was also ~₹0, so both sides agree). Today has resumed: 11 leads (4 FB + 7 IG) since delivery restarted.

## Stop-loss & trigger board
- **C1 Daytime INSA / C1 24Hr INSA:** ⚠️ Valid% breach on a matured 4-day window (6–9 Aug, to avoid the grading-lag trap): Daytime 29.0% (9/31), 24Hr 28.2% (11/39) — both **under the 30% floor**. CPL is healthy (₹177 / ₹117, both well under ₹350), so this is a *quality* flag, not a cost flag. **Recommend holding** the previously-queued +20% staging increment (cleared 10 Aug on the end-date resolution) until valid% recovers — see recommendation below.
- **IND3 TM ramp (TMF-SA / Director-TMF):** Healthy. Live lifetime budgets already at ₹150,000 / ₹60,000 (prior approved ramp), valid% 63.4% / 50.0%. No action needed.
- **DPIIT (#IND5):** Confirmed still paused at campaign level (standing pause since 14 Jul) and all 4 ads paused/campaign_paused. Not re-flagging per standing instruction.
- **Must-stay-paused check:** #IND6 ✅ paused, C1 Daytime LAL1% ✅ paused, C1 24Hr LAL1% ✅ paused, DPIIT ads 2 & 4 ✅ paused. All correct.
- **CCFS (#IND4):** 🚨 Pacing anomaly **worsening**: ₹6,866/day average over 6–9 Aug (vs ~₹3k/day expected re-pace, and above the ₹5k/day anomaly ceiling). This is the single biggest spend line (59% of 7-day account spend) and very likely the main driver of hitting the account cap. Quality itself is fine (45.5% valid) — this is a pure cost-efficiency problem, not a lead-quality one.
- **24Hr INSA learning phase:** Not re-verified this run (edit was over a month ago; delivery has been continuous since, so almost certainly out of learning).

## Yesterday's quality & funnel
Yesterday had **zero new leads**, so there's no fresh cohort to grade. The team was still active clearing the backlog: of leads **touched** yesterday (Modified_Time), there were 245 non-disposition touches plus **51 Lost, 64 Valid Lead, 70 Establishing Contact, 84 Proposal Sent, 9 Negotiation, 11 Postponed, 2 Payment Pending**.

**Form-change watch:** junk-loss share (Inquired by Mistake + Job Seeker) among yesterday's 51 losses = 3/51 = **5.9%** — well under the 30% concern line. (Caveat: these are losses on older backlog leads, not a fresh post-form-change cohort, so less directly comparable.)

## 7-day campaign scorecard (4–10 Aug)

| Campaign | Spend | CRM Leads | CPL | Valid | Valid% | Cost/Valid | Progressed | Cost/Progressed |
|---|---|---|---|---|---|---|---|---|
| #IND4 - CCFS | ₹27,464.71 | 33 | ₹832.27 | 15 | 45.5% | ₹1,830.98 | 6 | ₹4,577.45 |
| #IND3 - Trademark | ₹9,069.64 | 67 | ₹135.37 | 39 | 58.2% | **₹232.55** ✅ best | 19 | ₹477.35 |
| #IND 1 - Incorporation | ₹10,075.83 | 70 | ₹143.94 | 20 | 28.6% | ₹503.79 | 9 | ₹1,119.54 |
| (null Meta_Campaign) | — | 2 | — | — | — | — | — | — |
| **TOTAL** | **₹46,610.18** | **172** | **₹271.10** | **74** | **43.0%** | **₹629.87** | **34** | **₹1,370.89** |

Null-campaign leads: 2/172 = 1.2%, no LeadChain mapping alarm. Worst cost/valid: **CCFS at ₹1,831 — 7.9× worse than Trademark.** Incorporation's below-average 28.6% valid% is entirely explained by the C1 INSA ad-set dip flagged above (Incorporation = only those two ad sets).

**Glidepath verdict:** mid-Aug checkpoint target is ₹150–180 CPL at 125–150 leads/day. Actual blended CPL on active delivery days is **₹271** at **~43 leads/day** — running behind glidepath on both cost and volume, even setting the blackout aside.

## CAPI channel health: 🟢 GREEN (infrastructure) — starved by the blackout
- `server_last_fired_time`: 10 Aug 20:05 IST (well within the 48h freshness bar).
- SERVER_ONLY events, trailing 72h (ending ~12:00 IST today): **29 ValidLead, 14 Purchase**.
- The ~16h silence from 10 Aug evening into today is fully explained by zero new inflow to grade — not a CAPI defect.
- P9 gate (≥50 ValidLead per ad set): cannot be computed via this tool (no per-ad-set breakdown in `ads_get_dataset_stats`). Account-wide pace is ~29/72h (~68/week equivalent). Recommend a manual Events Manager check if a precise per-ad-set gate read is needed.

## Speed-to-lead exceptions (untriaged, as of 19:00 IST)
All 9 exceptions are aging leads from **9 Aug evening** (no new leads since, due to the blackout):

| Age | Name | Phone | Owner | Status |
|---|---|---|---|---|
| 50.2h | Bhola Patel | +918269326696 | Kumar | Postponed |
| 49.8h | PRAKASH Hingwala | +918302072510 | Singh | Establishing Contact |
| 49.2h | S S Chaggar | +917009191010 | Kumar | Establishing Contact |
| 48.6h | Shageer Choudhary | +919717537045 | Singh | Establishing Contact |
| 48.6h | Uday Gupta | +919110550699 | Singh | Establishing Contact |
| 48.5h | Vivekanand Tiwari | +919429362300 | Kumar | Establishing Contact |
| 48.4h | Abhishek | +919212020303 | Tiwari | Establishing Contact |
| 48.3h | vishnu dev singh | +919792975000 | Kumar | Establishing Contact |
| 47.4h | Laguri | +917894953837 | Agrawal | Establishing Contact |

**Owner concentration:** Kumar 4/9 (44%), Singh 3/9 (33%) — 78% of the stale backlog sits with these two reps, matching the recurring pattern noted 10 Aug. (Caveat: status+age is a proxy; first-contact latency isn't directly instrumented.)

## Loss buckets (yesterday, Why_Disqualified on 51 losses)
**Avoiding Call: 20 (39.2%)** — sharp reversal from the ~0% seen 6–7 Aug, back toward the sales-process baseline (~44–51%). Full breakdown: Not Interested 13 (25.5%), Other CA 7 (13.7%), Inquired by Mistake 3 (5.9%), No Product Offering 2 (3.9%), Plan Drop 2 (3.9%), Bot/Spam 1, Non-Serviceable Territory 1, Language Issue 1, Pricing 1.

Rolled to buckets: **sales-process ≈39%** (Avoiding Call), **pricing/competition ≈24%** (Other CA + Plan Drop + No Product Offering + Pricing), **targeting ≈8%**, geography 2%, qualification 2%, natural attrition (Not Interested) 25.5%. Sales-process clearly dominant again — consistent with baseline, **not** a targeting problem. Plausible context: reps were clearing a 200+ record backlog on a zero-new-lead day; some follow-ups likely slipped.

## Pilot monitors
- **WA auto-follow-up:** not launched / no confirmed stamp field to check.
- **TM call-ads pilot:** not launched — no call-objective ad set exists in the current account structure.
- **CTWA pilot:** not launched — 0 leads with `CTWA_Click_ID` in the last 7 days.
- **Website-conversion retest:** gate progress inconclusive (see CAPI section); P9 switch status not confirmed via API.

## Part B — Lead-source QA sweep
- **B1 Chat stragglers:** clean (0).
- **B2 Blank sources:** clean (0).
- **B3 Stray labels:** found 2× `Zoho Bookings` → **corrected to `SEO - Zoho Booking`** (trigger:[], write confirmed successful).
- **B4 Stamped-value contradictions:** spot-checked gclid (0 hits — no Google Ads contamination) and chatgpt/perplexity referrers (3 hits, all already correctly tagged `AI - ChatGPT`). Clean.
- **B5 Meta placement integrity:** clean (0 fb/ig mismatches).
- Deals picklist stray `Self - Referral`: not checked this run (Deals module, out of this run's scope).

---

## Recommended changes for approval

1. **🚨 Check Ads Manager → Billing now.** Second cap-driven blackout in <2 weeks, only 4 clean days between them. Confirming metric: spend holds >₹0 through a full calendar day without collapsing mid-day. Given CCFS's runaway pacing (₹6,866/day vs ~₹3k expected) is the likely single biggest driver of hitting the cap, consider pairing any limit raise with a CCFS-specific daily cap so the next raise doesn't just get consumed by CCFS again in ~4 days.
2. **Hold the C1 Daytime/24Hr INSA +20% staging increment** (previously cleared 10 Aug). Valid% is at 28–29% on a matured window, under the 30% floor, on both ad sets. Recommend reviewing INSA creative/targeting before adding budget. Confirming metric to re-clear: valid% ≥35–40% over the next matured 3–4 day window post-recovery.

*Reminder: ad-level Meta changes must go via browser (API blocked by leadgen-ToS error 1815089); ad-set/campaign-level changes are fine via API. No Meta mutation was executed — both items above are for your approval.*
