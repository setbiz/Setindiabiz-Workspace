# SetIndiaBiz — Meta Ads Watchdog
## Thursday, 13 August 2026 (~09:15 IST) · account SETINDIABIZ 152154124583473

**Verdict: mostly in order, and materially better than 11 Aug — but two new structural problems and one live compliance risk.**

Windows used: Meta spend 7–11 Aug (matured, excludes fresh 12 Aug); CRM cohort 7–11 Aug created-date, n=188 paid-Meta leads (`Advt - Facebook` + `Advt - Instagram`). 10 Aug was dark and is excluded from rate maths.

---

## 1. Delivery — RECOVERED ✅

| Date | Spend | Impr. | Meta leads | CPL |
|---|---|---|---|---|
| 6 Aug | ₹11,824.74 | 38,694 | 39 | ₹303 |
| 7 Aug | ₹17,836.28 | 86,268 | 86 | ₹207 |
| 8 Aug | ₹8,474.57 | 43,635 | 47 | ₹180 |
| 9 Aug | ₹8,474.58 | 28,984 | 20 | ₹424 |
| **10 Aug** | **₹0.01 — DARK** | 1 | 0 | — |
| 11 Aug | ₹17,624.91 | 64,415 | 53 | ₹333 |
| **12 Aug** | **₹20,510.68** | 112,949 | 85 | ₹241 |

- **No 4th blackout.** The 10–11 Aug outage self-resolved, and 12 Aug at ₹20,510.68 is the **highest spend day since 22 Jul (₹21,183)**. The old ₹12,711.86 ceiling is clearly not binding.
- `account_status: ACTIVE`, `has_payment_method: true`, `ads_get_errors` returns **empty** — no delivery-blocking errors, no policy/disapproval issue.
- All five active ad sets read `delivery: active/active`.

## 2. Stop-loss board — ALL CLEAR ✅ (the 11 Aug INSA breach did NOT hold)

Matured 7–11 Aug, CRM-derived:

| Ad set | Spend | CRM leads | CPL | Valid % | Cost/valid | Gate |
|---|---|---|---|---|---|---|
| C3 TMF-SA | ₹5,584 | — | ₹127 | — | — | ✅ |
| C3 Director-TMF | ₹3,515 | — | ₹121 | — | — | ✅ |
| **TM combined** | **₹9,099** | **67** | **₹136** | **59.7%** | **₹227** | ✅ best |
| C1 Daytime INSA | ₹3,590 | 23 | ₹156 | **43.5%** | ₹359 | ✅ clears 30% floor AND 40% gate |
| C1 24Hr INSA | ₹4,707 | 35 | ₹134 | **37.1%** | ₹362 | ✅ clears floor, under 40% gate |
| **C4 CCFS** | **₹35,014** | **61** | **₹574** | 45.9% | **₹1,250** | 🚨 cost |
| **Blended** | **₹52,410** | **188** | **₹279** | **49.5%** | **₹564** | |

**The 11 Aug flag is withdrawn.** On 11 Aug both INSA ad sets read under the 30% valid floor (29.0% / 28.2%) on a 6–9 Aug window. On the fuller 7–11 Aug matured window they read **43.5% and 37.1%**. The queued +20% staging increment is no longer blocked *on quality grounds* — see §4 for why it is still the wrong move.

Progressed rate 19.1% blended; TM 28.4%, CCFS 14.8%, Incorporation 13.8%.

## 3. 🚨 NEW — the CCFS budget cap has been located (open since 9 Aug)

Four consecutive runs reported "no visible budget cap on the CCFS ad set". **The cap is not on the ad set — it is on the campaign.**

- `#IND4 - CCFS` campaign: **lifetime_budget ₹400,000**, spent **₹178,418.83**, **₹221,581 remaining**, `stop_time` **24 Aug 2026**.
- That is **₹20,144/day of headroom over 11 days** — larger than the account's entire recent daily throughput (₹17.6k–20.5k).

So CCFS is *structurally* uncapped: it is the only campaign with meaningful headroom, and it is the worst performer on cost/valid. It took **66.8% of spend for 32.5% of leads** over 7–11 Aug. This is the most plausible mechanism behind the repeat account-spend-limit blackouts.

**Mechanical cause identified — creative fatigue.** `#C4 CCFS - 2` is now the **only active CCFS ad** (CCFS-1, CCFS-3, CCFS-4 all PAUSED) and is carrying 100% of CCFS delivery at **frequency 1.92**, against 1.05–1.47 on every other active ad. Ad-set-level frequency is **2.53**. Concentration onto one fatiguing creative is the direct driver of the ₹574 CPL.

### Counter-evidence that must not be buried
Won-stage deals from paid Meta, 6–12 Aug (8 deals, ₹81,848 total):

| Product | Deals | Revenue |
|---|---|---|
| ACR (CCFS) – Company Annual Return | 2 | ₹35,000 |
| Company Striking Off (Close) – STK2 | 2 | ₹38,674 |
| TMF – Standard TM Filing | 3 | ₹6,000 |
| DIN KYC – Reactivation | 1 | ₹2,174 |

CCFS/closure-funnel products account for **₹73,674 of ₹81,848 (90%)** of won revenue; Trademark's 40 valid leads produced **₹6,000**. The operator objective hierarchy ranks *cost per won deal* above *cost per valid lead* — and on that measure CCFS's expensive leads look justified while Trademark's cheap ones do not. **Judging CCFS on cost/valid alone is the wrong test.** Caveat: deal→campaign attribution is inferred from product names, not a stamped field (Deal-level `Meta_Campaign` remains unusable).

Account-level 6–12 Aug: spend ₹84,747, won revenue ₹81,848, **cost per won deal ₹10,593**. Roughly break-even on first-deal revenue alone, before recurring/LTV value.

## 4. 🚨 NEW — scheduled end-date cliff, 20–24 August

| Ad set / campaign | Ends | Budget left | Needed/day | Actual/day | Will strand |
|---|---|---|---|---|---|
| C3 Director-TMF | **20 Aug** (7d) | ₹21,764 | ₹3,109 | ₹703 | ~₹17k |
| C3 TMF-SA | **23 Aug** (10d) | ₹43,638 | ₹4,364 | ₹1,117 | ~₹32k |
| C1 Daytime INSA | **24 Aug** (11d) | ₹30,279 | ₹2,753 | ₹718 | ~₹22k |
| #IND4 CCFS (campaign + ad set) | **24 Aug** (11d) | ₹221,581 | ₹20,144 | ₹7,003 | ~₹144k |
| C1 24Hr INSA | **no end date** | ₹2,500/day | — | ₹941 | — |

Two consequences:

1. **On 25 August the account collapses to a single ad set** — C1 24Hr INSA at ₹2,500/day, roughly **12% of current delivery**. Nothing else is scheduled to run. This needs a decision before 20 Aug, not after.
2. **~₹71k of TM + Daytime-INSA lifetime budget will strand** unspent, because those ad sets are pacing at 16–26% of the rate their remaining budget and end date imply. Raising their budgets would achieve nothing — they cannot spend what they already have. The constraint is delivery share, not budget.

This reframes the standing "+20% INSA staging increment": **it is moot.** Daytime INSA has ₹30k it cannot spend in 11 days at current pace. Adding budget does not add delivery.

## 5. ⚠️ Compliance — live ad may be showing an expired statutory deadline

- CCFS-2026 was extended to **31 August 2026** by **MCA General Circular 03/2026** (superseding the 15 July 2026 date in GC 01/2026).
- Project record (9 Jul): ad *text* was corrected to "31st August 2026" on both CCFS ads, but the **image graphics still have "Scheme Last Date 15 July 2026" baked in** — new artwork was never confirmed shipped.
- `#C4 CCFS - 3`, the ad created with the corrected creative, is **PAUSED**. `#C4 CCFS - 2` — the older ad — is the **only** CCFS ad serving, at ~₹7,000/day.
- The connector cannot read creative image content, so this cannot be confirmed via API. **It needs a visual check in Ads Manager.** If the image still reads 15 July, a live ad is misstating a government scheme deadline that passed four weeks ago — an accuracy problem under the Companies Act 2013 compliance posture, and a conversion problem regardless.
- Separately: **campaign stops 24 Aug but the scheme runs to 31 Aug** — seven days of scheme-deadline demand, the highest-intent week, currently uncovered.

## 6. Governance & hygiene — clean ✅

- **Must-stay-paused list all correct:** #IND5 DPIIT `CAMPAIGN_PAUSED` (standing pause since 14 Jul), #IND6 Virtual CFO PAUSED, both C1 LAL1% ad sets PAUSED, all #IND2 LLP ACR ad sets PAUSED, DPIIT ads 2 & 4 PAUSED.
- **Budgets unchanged and confirmed:** TMF-SA ₹150,000 lifetime, Director-TMF ₹60,000 lifetime, Daytime INSA ₹190,500 lifetime. Do not re-flag — all intentional.
- **Creative rotation happened since 11 Aug** (not previously logged): Incorporation's original "Ad-1 Lead - Company Registration" ads are now PAUSED in both INSA ad sets, replaced by two new active ads (CPL ₹175 / ₹202, frequency 1.23 / 1.35 — healthy). CCFS narrowed from four ads to one. Ad-level writes remain API-blocked (error 1815089), so these were done in Ads Manager.
- **CAPI GREEN.** Last SERVER_ONLY event ~10.5h ago; 8–12 Aug totals **≈95 ValidLead, 29 Purchase** ≈ **133 ValidLead/week**, comfortably above the ≥50/week account gate. 12 Aug alone fired 40 ValidLead — grading has caught up post-blackout.
- **Part B lead-source QA sweep: 0 writes.** No null `Lead_Source`, no "Zoho Bookings" typo recurrence (the single match is correctly labelled "SEO - Zoho Booking"), no stray legacy values.
- **Null `Meta_Campaign`: 2 of 188 (1.1%)** — LeadChain campaign stamping healthy.

## 7. Speed-to-lead — improved on triage, unchanged on the bottleneck

- **Untriaged (null `Lead_Status`): only 2** — a real improvement (was 9–18 in July runs).
- **Stale in "Establishing Contact" >48h: 29.** Owner concentration:

| Owner | Stale | Share |
|---|---|---|
| Yadav (…919146001) | 9 | 31% |
| Kumar (…898222001) | 6 | 21% |
| Kumar (…005475021) | 6 | 21% |
| everyone else (5 owners) | 8 | 28% |

Three owners hold **72%** of the stale queue. A Kumar-family owner has appeared in the top two on **every run since 6 July**. The specific names rotate; the *pattern* does not. This is an SLA/alerting gap, not a personnel issue — there is no automated escalation when a lead sits unworked past 48h.

- **Loss buckets** (leads created 7–12 Aug now Lost, n=14): Not Interested 35.7%, **Avoiding Call 21.4%**, Inquired by Mistake 14.3%, then singletons. Avoiding Call sits well below the 44–51% historical baseline, but n=14 is too small to call a structural improvement — and note this is a *created-date* cohort, not the *modified-date* basis used on 11 Aug (39.2%), so the two are not directly comparable.

---

## Recommendations — 2 changes, both need approval

**#1 — Cap CCFS pacing rather than cutting it, and fix the creative.**
Do NOT judge CCFS on cost/valid alone; it produces 90% of won revenue. The real problems are (a) ₹20k/day of unconstrained headroom crowding out better campaigns on a shared account limit, and (b) one fatiguing creative at frequency 1.92 carrying all delivery. Proposed: set a **daily cap of ₹5,000** on the CCFS ad set (vs ₹7,003 actual) — this frees ~₹2k/day for TM and INSA, which have ₹95k of budget they will otherwise strand. Pair it with reactivating or re-shooting CCFS-3 so a second creative shares the load. *Confirming metric: CCFS cost/valid < ₹900 and frequency < 1.6 within 3 days; TM + INSA combined daily spend up ≥₹1,500/day.* Stop-loss: revert if CCFS won-deal count drops below 2/week.

**#2 — Decide the post-24-August plan this week.**
Four of five active ad sets end 20–24 Aug. Absent a decision the account runs at ~12% of current volume from 25 Aug. The CCFS scheme itself ends 31 Aug, so the natural move is to extend the CCFS campaign `stop_time` to **31 Aug** (capturing the deadline week) and extend TM + Daytime INSA end dates into September so their remaining ₹95k actually gets spent. All are campaign/ad-set level edits — connector-capable.

**Not recommended:** the +20% INSA staging increment. Quality gates now pass, but Daytime INSA already has ₹30,279 it cannot spend before 24 Aug at current pace. More budget will not produce more delivery.

**Needs a direct answer from you (3rd run asking):** C1 24Hr INSA `daily_budget` reads **₹2,500**. The last logged approval was ₹2,160 on 20 Jul. Was the bump to ₹2,500 yours?

⚠️ *Connector trap reminder: `ads_update_entity` force-pauses the entity on a budget edit. Any approved change must be followed by a status read-back and `ads_activate_entity`.*
