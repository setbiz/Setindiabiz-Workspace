# Change Log — 13 August 2026
## End-date extensions + CCFS creative compliance verification
Account: SETINDIABIZ 152154124583473 · Approved by Sanjeev, interactive, 13 Aug 2026

---

## Decisions taken

| # | Decision | Choice |
|---|---|---|
| 1 | CCFS pacing (66.8% of spend, ₹1,250/valid) | **Leave uncapped** — justified by CCFS funnel producing ₹73,674 of ₹81,848 won revenue, 6–12 Aug |
| 2 | End-date cliff 20–24 Aug | **Extend all except CCFS**; CCFS keeps its 24 Aug end |
| 3 | Extension target date | **30 September 2026** — aligns with AGM (s.96 Companies Act 2013), AOC-4 (s.137), MGT-7 (s.92) and DIR-3 KYC, all due 30 Sep |
| 4 | CCFS creative compliance check | Verified via ad preview render |

## Changes applied — before / after

| Entity | ID | Field | Before | After | Verified |
|---|---|---|---|---|---|
| #IND3 – Trademark (campaign) | 120243118117990449 | `stop_time` | 2026-08-23T12:20Z | **2026-09-30T18:29Z** | ✅ ACTIVE |
| C3 Adset – Director-TMF | 120243249506380449 | `end_time` | 2026-08-20T12:20Z | **2026-09-30T18:29Z** | ✅ ACTIVE, delivery `active`, lifetime ₹60,000 unchanged |
| C3 Adset – TMF-SA | 120243118118000449 | `end_time` | 2026-08-23T12:20Z | **2026-09-30T18:29Z** | ✅ ACTIVE, delivery `active`, lifetime ₹150,000 unchanged |
| #IND4 – CCFS (campaign + ad set) | 120244101705120449 / …150449 | `stop_time` / `end_time` | 2026-08-24 | **unchanged (intentional)** | ✅ |

No budget, audience, bid or creative values were touched. Schedule was the only variable changed.

### ⚠️ Connector trap — confirmed wider than previously logged
All three `ads_update_entity` calls returned `success: true` **together with `status_forced_to_paused: true`**, silently setting each entity PAUSED. Each was recovered within seconds via `ads_activate_entity` and re-read as ACTIVE with `delivery: active`.

The July note recorded this trap for *budget* edits. **It also fires on a pure schedule edit.** Treat it as applying to every `ads_update_entity` call regardless of field. Never accept `success: true` alone as done — always read back status.

## ❌ Not applied — C1 Daytime INSA

`end_time` → 30 Sep on ad set **120242110677990449** was rejected:

> `error_code 100 / subcode 2446289` — *"Ad Creative Is Incomplete: The reel you selected for your ad is not available. It could be deleted or you might not have permissions to see it."*

**Diagnosis.** Meta re-validates every child ad when an ad set is edited, including paused ones. The ad set has two children:

| Ad | ID | Created | Status |
|---|---|---|---|
| Ad-1 Lead - Company Registration | 120242110678000449 | 17 May 2026 | **PAUSED** — holds the broken reel reference |
| Ad-1 Lead - Company Registration - Copy | 120245819917720449 | 6 Aug 2026 | ACTIVE, healthy (CPL ₹175, frequency 1.23) |

`ads_get_errors` on the ad set returns empty — a paused ad's broken creative does not surface as a delivery-blocking error, only as an edit-validation failure. It cannot be fixed through the API either, because ad-level writes remain blocked account-wide by error 1815089 (leadgen ToS).

**Fix:** delete or detach ad `120242110678000449` in Ads Manager, then the ad-set edit will go through via connector. It is already paused, so removing it has no delivery impact.

**Until then C1 Daytime INSA still ends 24 Aug 2026**, with ~₹30,279 of its ₹190,500 lifetime budget unspent.

## Compliance verification — CLOSED (open since 9 Jul 2026)

`#C4 CCFS - 2` (120244142710410449), the only serving CCFS ad, rendered via `ads_get_ad_preview` → browser screenshot:

- **Body copy:** "Missed ROC Annual Returns in any past year. File now with 90% late fee waiver before **31st August 2026**. This includes essential documents such as AOC-4, MGT-7 and ADT-1 Filings… In case your company needs to close, the closure fee is also reduced from 10K to 2.5K."
- **Image graphic:** "CCFS 2026 gives 90% waiver on late fees — **Last date: 31 Aug 2026**"
- **Headline:** "90% Late Fee Waiver — Subject to CCFS eligibility"

The stale "Scheme Last Date 15 July 2026" artwork is gone; new creative was shipped at some point without being logged. All claims are consistent with **MCA General Circular 03/2026**, which extended CCFS-2026 to 31 August 2026, and the eligibility qualifier is present. No action required; no need to reactivate CCFS-3.

*Technique worth reusing: the connector cannot read creative image content, but `ads_get_ad_preview` returns a `preview_url` that renders the full ad including baked-in image text when opened in a browser tab. Allow ~3s for the iframe to paint — the first screenshot returns blank.*

## Stop-loss / monitoring

- No stop-loss applies — schedule extensions carry no spend or quality risk on their own.
- **Watch from 25 Aug:** CCFS stops, freeing ~₹7,000/day of account capacity. TM and INSA should accelerate. If combined TM + INSA daily spend does not rise materially by 27 Aug, delivery is constrained by something other than CCFS crowding and needs re-diagnosis.
- **Budget-exhaustion watch:** TMF-SA ₹43,638 and Director-TMF ₹21,764 remaining. At post-24-Aug pace these may exhaust before 30 Sep — flag for a top-up rather than letting them go dark.
- **Reminder due 22–23 Aug:** confirm Sanjeev still wants CCFS off on 24 Aug, given the scheme itself runs to 31 Aug and the final week is typically the highest-intent period.

## Still open

1. **C1 24Hr INSA `daily_budget` = ₹2,500**, unverified for a third run (last logged approval ₹2,160 on 20 Jul).
2. **Speed-to-lead SLA gap** — 29 leads stale >48h; Yadav + two Kumar owners hold 72%. A Kumar-family owner has been top-two on every run since 6 Jul. Needs an automated 48h escalation, not a daily flag.
3. **Daytime INSA extension**, pending the ad deletion above.
