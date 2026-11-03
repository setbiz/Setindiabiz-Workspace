# SetIndiaBiz Meta Ads — Daily Watchdog
**Run:** 1 August 2026 (report covers 31 Jul, with 24–30 Jul context)
**Posture:** read-only. No Meta mutations made. No CRM writes needed.

---

## 🚨 RED ALERT — Account spending limit reached, campaigns dark

Every ACTIVE ad set returns `delivery.status = off`, `substatus = account_spend_limit_reached`.
This is the confirmed root cause — not a billing card failure, not a campaign schedule problem.

**Daily account spend, 17–31 Jul 2026:**

| Date | Spend | Impressions | Read |
|---|---|---|---|
| 17 Jul | ₹12,711.86 | 64,376 | 0.75× cap |
| 18 Jul | ₹0.01 | 1 | dark |
| 19 Jul | ₹8,474.58 | 32,259 | 0.5× (Sun) |
| 20 Jul | ₹12,711.86 | 67,724 | 0.75× cap |
| 21 Jul | ₹12,711.87 | 68,503 | 0.75× cap |
| 22 Jul | ₹21,183.42 | 112,062 | limit raised |
| 23 Jul | ₹0 | 0 | **dark** |
| 24 Jul | ₹62.55 | 254 | **dark** |
| 25 Jul | ₹0 | 0 | **dark** |
| 26 Jul | ₹8,474.58 | 39,373 | 0.5× cap |
| 27 Jul | ₹0.01 | 1 | **dark** |
| 28 Jul | ₹8,474.57 | 43,474 | 0.5× cap |
| 29 Jul | ₹0.01 | 1 | **dark** |
| 30 Jul | ₹0 | 0 | **dark** |
| 31 Jul | ₹0.91 | 39 | **dark** |

Since 23 Jul the account has delivered on **2 days out of 9**. Three consecutive dark days
(29, 30, 31 Jul). 7-day spend (25–31 Jul) = **₹16,950** = ₹2,421/day against a ₹22,500/day
ceiling — roughly **11% of planned pace**.

The repeated ₹8,474.58 figure is exactly 0.5 × the ₹16,949.15 cap-day value, and ₹21,183.42
on 22 Jul is 1.25 × it. The limit appears to have been raised around 22 Jul and then fully
consumed, leaving the account throttled ever since.

**Action required (human only — I never touch billing):** Ads Manager → Billing & Payments →
Account spending limit. Either raise it or clear the amount spent.

---

## CRM inflow (paid segment: `Advt - Facebook` + `Advt - Instagram`)

| Date | Paid CRM leads |
|---|---|
| 23 Jul | 1 |
| 24–25 Jul | 0 |
| 26 Jul | 34 |
| 27 Jul | 1 |
| 28 Jul | 47 |
| 29 Jul | 0 |
| 30 Jul | 0 |
| 31 Jul | 0 |

Zero inflow on 29–31 Jul is **consistent with zero spend** — this is not a LeadChain sync break.
Verified: both paid picklist values still exist and are being written (no third rename).
`Meta_Campaign` was stamped on 100% of the 82 leads in the window — LeadChain mapping healthy.

7-day paid inflow = 82 leads = 11.7/day against the 150/day goal.

---

## 7-day campaign scorecard (24–30 Jul 2026)

Spend from Meta connector; lead/valid/progressed counts from Zoho CRM. Account-level attribution
caveat does not apply here — `Meta_Campaign` is stamped, so these are true per-campaign figures.

| Campaign | Spend | CRM Leads | CPL | Valid | Valid% | Cost/Valid | Progressed | Cost/Progressed |
|---|---|---|---|---|---|---|---|---|
| #IND3 — Trademark | ₹4,202.71 | 32 | **₹131** | 12 | 37.5% | **₹350** | 8 | ₹525 |
| #IND 1 — Incorporation | ₹4,165.76 | 25 | ₹167 | 17 | 68.0% | ₹245 | 5 | ₹833 |
| #IND4 — CCFS | ₹8,643.25 | 25 | ₹346 | 13 | 52.0% | **₹665** | 5 | ₹1,729 |
| **TOTAL** | **₹17,011.72** | **82** | **₹207** | **42** | **51.2%** | **₹405** | **18** | **₹945** |

- **Best cost-per-valid:** #IND 1 Incorporation at ₹245.
- **Worst cost-per-valid:** #IND4 CCFS at ₹665 — it absorbed 51% of spend for 30% of the valid leads.
- **Glidepath verdict: ON TARGET.** 1 Aug checkpoint is ₹180–220 CPL; blended is **₹207**.
- Valid% at **51.2%** is far above the ≥36–39% floor.

**The efficiency side of the plan is working. Volume is the only broken variable, and it is
broken entirely by the spending limit.**

---

## Stop-loss & trigger board

| Item | Status |
|---|---|
| C1 Daytime INSA (lifetime ₹190,500) | ✅ Healthy — 28 Jul CPL ₹286 (<₹350), valid 68% (≥40%). Both confirming metrics met. Staging increment **cannot be judged** while spend-limited. |
| C1 24Hr INSA (daily ₹2,160) | ✅ Budget shows ₹2,160 — the ~20% staging increment took effect. Learning-phase exit not assessable: no delivery. |
| IND3 TM ramp | ✅ Healthy — CPL ₹131, valid 37.5%. Both well inside stop-loss (₹250 / 30%). TMF-SA lifetime now ₹150,000, Director-TMF ₹60,000 (both raises applied). |
| DPIIT (#IND5) | ⚠️ **Whole campaign is PAUSED**, not just ads 2 & 4. Spec expected ads 1 & 3 live. Needs a decision. |
| Must-stay-paused | ✅ All correct — #IND6 CAMPAIGN_PAUSED, C1 Daytime LAL1% PAUSED, C1 24Hr LAL1% PAUSED. |
| CCFS (#IND4) | ⚠️ ₹8,643 over 7d = ₹1,235/day vs ₹3k/day expected re-pace — but it front-loaded ~₹7,505 on 26 Jul (>₹5k anomaly line) then starved. **Ad copy still cites "15 July" — stale.** Scheme runs to 31 Aug 2026 (MCA General Circular 03/2026); campaign end date is 20 Aug 2026. |

---

## Quality & form-change watch

No cohort for 30 or 31 Jul (zero leads). Most recent real cohort = **28 Jul, 47 leads**:

- Valid 20/47 = **42.6%** — above the ~39% pre-form-change baseline.
- Progressed 9/47 = 19.1%.
- **Junk-loss share = 2/15 losses = 13.3%** (`Inquired by Mistake` ×2, no `Job Seeker`).

That is well under the 30% trigger and far below the 34% seen 2–8 Jul. **The 4-Jul single-question
form is no longer producing a junk problem — P10 (restoring the 2nd qualifying question) is not
needed.** Recommend closing that watch item.

---

## Loss buckets (28 Jul cohort, 15 losses)

| Bucket | Count | Share | Baseline | Read |
|---|---|---|---|---|
| Natural attrition (Not Interested) | 6 | 40% | — | normal |
| Sales-process (Avoiding Call) | 3 | 20% | 51% | ✅ well below |
| Targeting/junk (Inquired by Mistake ×2, Wrong Info) | 3 | 20% | 11% | ⚠️ above |
| Pricing/competition (Other CA) | 2 | 13% | 32% | ✅ below |
| Geography (Off Location – Visit Not Available) | 1 | 7% | — | 1 record |

Sales-process losses at 20% vs a 51% baseline is a genuine improvement. Targeting is modestly
elevated but on a 15-record base — not actionable yet.

---

## CAPI channel health — 🟢 GREEN

- `server_last_fired_time` = 31 Jul 2026 23:57 PDT (~12:27 IST, 1 Aug) — minutes old.
- Dataset 1242417817083521 active, first-party cookie enabled.
- 72h SERVER_ONLY events: **ValidLead 32, Purchase 36**. No QualifiedLead/Committed — expected,
  the hourly sweep sends one event per lead and does not re-send upgrades.
- ValidLead is still firing during the blackout because the sweep grades older leads. Correct behaviour.
- **P9 gate progress:** ~75 ValidLead/week account-wide. Per-ad-set the ≥50 threshold is still
  some weeks out, and the clock is effectively stopped while delivery is throttled.

---

## Speed-to-lead exceptions — 25 stale paid leads

All are `Establishing Contact`, created 26 or 28 Jul. With **zero new inflow for three days**,
there is no queue-pressure excuse for these sitting untouched.

| # | Name | Phone | Owner | Created | Age |
|---|---|---|---|---|---|
| 1 | Chiks gaming | +918160030316 | Kumar | 26 Jul 11:58 | ~5.9d |
| 2 | Neel Kotadia | +919426592923 | Singh | 26 Jul 12:52 | ~5.9d |
| 3 | Mandar | +918879488206 | Bisht | 26 Jul 13:07 | ~5.9d |
| 4 | Vishwakarma | +917618089691 | Kumar 3 | 26 Jul 14:39 | ~5.8d |
| 5 | Vineet Mishra | +919839073321 | Sehrawat | 26 Jul 14:52 | ~5.8d |
| 6 | NAUSHAD K | +918089817458 | Kumar | 26 Jul 16:42 | ~5.8d |
| 7 | Chiranjit Jana | +919831414264 | Kumar | 26 Jul 18:09 | ~5.7d |
| 8 | iam Paramesh interested this car | +919980375164 | Agrawal | 26 Jul 18:54 | ~5.7d |
| 9 | Laxmi Engitech Pvt. Ltd. | +919263783032 | Kumar | 26 Jul 19:08 | ~5.7d |
| 10 | Singh S | +917999377114 | Agrawal | 26 Jul 19:55 | ~5.7d |

**Owner concentration: "Kumar" (ID …898222001) holds 8 of the 25** — the same single-owner
pattern flagged on 6 Jul. Worth a direct word.

(Lead #8's name suggests a mis-targeted click; harmless but a small junk signal.)

---

## Part B — Lead-source QA sweep: **CLEAN**

| Sweep | Result |
|---|---|
| B1 Chat stragglers | 0 records |
| B2 Blank Lead_Source | 0 records — no-blank policy holding |
| B3 Stray labels | No `Zoho Bookings`, no legacy Meta values. `WhatsApp - SETINDIABIZ` present — non-taxonomy, **report only**, no write |
| B4 Stamped contradictions | 0 hits — blueprint default-stamp healthy |
| B5 Meta placement integrity | 0 `ig`-typed leads mislabelled `Advt - Facebook` |

**Zero writes performed.** No sign of the Advt→Direct regression — the 9 Jul workflow fix is holding.
Deals picklist stray `Self - Referral` still pending your deletion (zero records attached).

---

## Pilot monitors

- WA auto-follow-up — not launched, no acknowledgement stamps present.
- TM call-ads — not launched.
- CTWA — not launched, no `CTWA_Click_ID` values.
- Website-conversion retest — gated behind P9; gate not met.

---

## Recommended actions

### 1. Raise or clear the account spending limit — YOU, in Ads Manager (billing)
Ads Manager → Billing & Payments → Account spending limit. This is the single binding constraint;
every other lever is inert until it clears. I do not touch billing.
- **Confirming metric:** next-day account spend > ₹8,500 and all active ad sets showing
  `delivery.status = active`.
- **Stop-loss:** if blended CPL exceeds ₹260 for 3 consecutive full-delivery days, pause the
  weakest ad set rather than reducing the limit again.

### 2. Decide on #IND5 DPIIT — approval needed
The whole campaign is paused, not just ads 2 & 4 as specified on 9 Jul. Either it was paused
deliberately and the spec needs updating, or ads 1 & 3 should be reactivated.
- If reactivating: one variable, ads 1 & 3 only, budget unchanged.
- **Confirming metric:** DPIIT CPL < ₹300 within 3 delivery days.
- **Stop-loss:** frequency > 2.5 or CPL > ₹350 → pause again.

**Note:** ad-LEVEL changes must go through the browser — the API returns leadgen-ToS error
1815089 despite accepted terms. Ad-set and campaign-level API calls work fine.

### Also worth doing (no approval needed)
- Clear the 25 stale leads, starting with the 10 above; check in with owner "Kumar" on the 8 sitting with him.
- Fix the CCFS ad copy — it still says "15 July"; the scheme runs to 31 Aug 2026.
