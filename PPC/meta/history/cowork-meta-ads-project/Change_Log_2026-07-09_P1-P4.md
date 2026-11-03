# Change Log — 9 Jul 2026 (150×₹150 Plan, Phase 1: P1–P4)

Approval: Sanjeev, 9 Jul 2026 — "Approved for all 4 actions". Executed via Meta connector, account 152154124583473. All state reads logged below (API before/after in lieu of screenshots; Ads Manager links in connector responses).

## P1 — Pause #IND6 Virtual CFO + GST
**Found ALREADY PAUSED at execution time** (status + effective_status PAUSED at 9 Jul pre-check; had spent ₹10,607.26 through 8 Jul). Presumably actioned manually after the 6-Jul watchdog recommendation. **No mutation performed.** Desired end-state confirmed ✔

## P2 — LAL → INSA reallocation (4 mutations, all verified)

| Entity | Before | After | Verified |
|---|---|---|---|
| C1 Daytime LAL1% Director (120242110744990449) | ACTIVE, lifetime ₹185,000, end 30 Jul | **PAUSED**, delivery off | ✔ |
| C1 24Hr LAL1% Director (120240924480770449) | ACTIVE, daily ₹2,000 | **PAUSED**, delivery off | ✔ |
| C1 Daytime INSA (120242110677990449) | ACTIVE, lifetime ₹185,000 | ACTIVE, **lifetime ₹190,500** | ✔ delivering |
| C1 24Hr INSA (120240912969640449) | ACTIVE, daily ₹1,500 | ACTIVE, **daily ₹1,800** | ✔ (in_learning_phase post-edit) |

Sizing note: Daytime INSA is pacing-bound (remaining ≈₹26.4k ÷ 21 days ≈ ₹1,257/day implied vs ₹1,085 actual) → +₹5,500 lifetime lifts implied daily ~+20%, guardrail-compliant. Next staging increments (+20%/day equivalent) daily until LAL's ~₹1,873/day is absorbed, gated on metrics each morning.
Both budget updates were force-paused by the connector (known behaviour) and reactivated immediately; delivery status re-verified ACTIVE.

**Stop-loss (logged):** revert INSA budget raises if 3-day INSA CPL > ₹350 or valid% < 30%. Confirming metric: INSA CPL < ₹350 with valid% ≥ 40% and IND1 campaign CPL falling.

## P3 — Scale #IND3 TM — DEFERRED (mechanism correction, no mutation)
Lifetime-spend read shows TM is **not budget-bound**: TMF-SA ₹53,220 spent of ₹100k (implied pacing ₹2,126/day) and Director-TMF ₹15,610 of ₹50k (implied ₹1,563/day) vs actual ₹1,347/day combined. Binder = account spending-limit pacing (₹16,949.15/day signature). Raising TM budgets today = no-op.
**Mechanism now:** headroom freed by P1/P2 pauses (~₹3.4k/day) + CCFS end (12 Jul, ~₹5.6k/day) flows to remaining ad sets including TM automatically.
**Trigger to mutate:** raise TM lifetime budgets (+~19% of implied daily) when TM actual spend ≥ ₹1,900/day or on 13 Jul, whichever first. **Stop-loss:** halt scaling if 3-day TM CPL > ₹250 or valid% < 30%.

## P4 — Trim DPIIT ads 2 & 4 — ✅ COMPLETED via Ads Manager UI (browser control, 9 Jul)
API path remained blocked (1815089) even though /legal/leadgen/tos shows "Accepted" for the publishing page (627814417091714 = facebook.com/setindiabiz.official, the only page in Sanjeev's ToS dropdown) → stale/re-versioned acceptance on Meta's side, page names/tos flags via API also unreadable. **Workaround: toggled #C5 DPIIT 2 and #C5 DPIIT 4 OFF directly in Ads Manager UI via browser control — published cleanly, NO ToS dialog appeared.** API verified after: DPIIT 2 PAUSED ✔, DPIIT 4 PAUSED ✔, DPIIT 1 & 3 ACTIVE ✔. Campaign budget untouched (CBO redistributes to DPIIT 1 ₹294/lead lifetime, DPIIT 3). Confirming metric: DPIIT CPL <₹300.
**Residual issue (non-blocking, low priority):** connector/API ad-level WRITES still fail with 1815089 account-wide — UI works, so future ad-level changes (incl. new-ad creation P7/P8, reel-reference cleanup, "15 July"→"31 August" copy update) go via browser control until Meta's acceptance state re-syncs. If API writes matter later: re-accept ToS after switching into the Page profile, or contact Meta support.

### (superseded) original blocker note
Both ad-level pause calls rejected: error 100 / subcode **1815089 — "Terms of Service Not Accepted: You can't run lead ads until your Facebook Page accepts Facebook's Lead Generation Terms of Service."** Meta re-validates the full lead-ad object on any ad-level edit; a pending (re-versioned) Leadgen ToS on the Page blocks ALL ad-level mutations account-wide (delivery continues; ad-set/campaign-level edits unaffected — P2 proves it).
**Unblock (Sanjeev, Page admin):** accept the Lead Ads terms at https://www.facebook.com/ads/leadgen/tos while logged in as an admin of the SetIndiaBiz Page, then I retry P4 (~1 min). Note this also blocks P7/P8 (new ads) until accepted.

## Addendum (9 Jul, later) — CCFS extension to 20 Aug + ToS diagnosis

**CCFS-2026 scheme extension VERIFIED:** MCA General Circular No. 03/2026 dated 8 Jul 2026 extends the scheme from 15 Jul → **31 Aug 2026** (MCA data-centre fire of 5 Jun 2026; capacity restoration). Sanjeev directed the CCFS ad set to run until 20 Aug 2026 — compliant (inside scheme window).

| Entity | Before | After | Result |
|---|---|---|---|
| #IND4 CCFS campaign (120244101705120449) | stop 12 Jul, lifetime ₹200,000 (₹72,860 spent) | **stop 20 Aug 2026**, reactivated ACTIVE | ✔ |
| C4 CCFS ad set (120244101705150449) | end 12 Jul | **UPDATE BLOCKED** — error 100/subcode 2446289 "the reel you selected for your ad is not available (deleted or no permission)" — Meta re-validates child ads on ad-set edits; one CCFS ad references a missing/permission-broken reel asset | ⛔ ad set still ends 12 Jul — **must be fixed before Sunday** (manual Ads Manager schedule edit, or fix creative after ToS unblock) |

Re-pacing: remaining ~₹127k over 10 Jul–20 Aug (42d) ≈ **₹3.0k/day** (was ₹5.6k/day). Frees ~₹2.6k/day under the account cap for TM/INSA. If Sanjeev wants ₹5.5k/day held to 20 Aug → lifetime top-up to ~₹3.05L (his decision; not executed).
**Copy compliance:** any live copy/urgency line citing "before 15 July 2026" must change to "31 August 2026" (GC 03/2026) — blocked until ad-level edits unlock; creative review flagged.

**ToS root cause found:** `ads_get_ad_account_pages` shows the ad account promotes TWO pages — **627814417091714** and **185807091504036** — and **both report `leadgen_tos_accepted: false`**. The acceptance done for "Setindiabiz Private Limited" (screenshot, /legal/leadgen/tos) evidently covers a different/insufficient page. Action: on facebook.com/legal/leadgen/tos, open the page dropdown, check BOTH pages, accept wherever the button is active. P4 retry failed again (1815089) pending this.

## Addendum 2 (9 Jul) — CCFS ad set extended; publishing Page identified
- CCFS ad set end date extended to **20 Aug 2026 manually by Sanjeev (Ads Manager UI)** after API edit was blocked by the broken-reel validation. Verified via API: stop_time 20 Aug, ACTIVE, delivering ✔ Campaign + ad set now aligned; no 12-Jul cliff.
- **Publishing Page identified: 627814417091714** — all checked ads (DPIIT 1/2/4, CCFS 1/2) publish under this Page (`effective_object_story_id` prefix), and it reports `leadgen_tos_accepted: false`. The acceptance done for "Setindiabiz Private Limited" is registered against a different page. Fix: at facebook.com/legal/leadgen/tos select THIS page in the dropdown (verify by visiting facebook.com/627814417091714) and accept; requires full-control Page admin. Second promoted page 185807091504036 also shows false — accept both.
- P4 retried after "terms accepted" message — still 1815089. Will retry immediately once the correct page's acceptance registers.
- Broken-reel detail: both CCFS creatives carry `effective_instagram_media_id` (IG reels); one is deleted/permission-broken — harmless to delivery on other placements but blocks API edits touching that ad; fix after ToS unblock.

## Addendum 3 (9 Jul, evening) — CCFS copy compliance fix EXECUTED (browser)
Both CCFS ads' primary text updated "before 15th July 2026" → "before 31st August 2026" (per MCA GC 03/2026) via Ads Manager browser control; API-verified with NEW creative ids: CCFS-1 4406369382841569→**1381759757350320** (ACTIVE, review cleared), CCFS-2 2094165177897110→**3926266181001864** (IN_PROCESS, clearing review — normal post-edit). Only the date changed; headline/description/CTA untouched. "(1 of 5)" on Primary text = slot count, not variants — single text per ad, both covered.
**⚠️ REMAINING COMPLIANCE ITEM — image graphics:** the ads' image variants (5 selected on CCFS-1) have "Scheme Last Date 15 July 2026" BAKED INTO the artwork. Needs new image assets (design task) — flagged to Sanjeev; replace via browser once produced.
Editor also displayed "You've accepted Meta's Lead Ads Terms for this Page" — further confirmation the 1815089 API block is a stale server-side flag, not a missing acceptance. UI publishes work fine.

## Account state after Phase 1
Active spend: IND4 CCFS (CBO ₹200k, ends 12 Jul) · IND5 DPIIT (CBO ₹200k, all 4 ads live pending P4) · IND3 TM (SA ₹100k + Director ₹50k, end 31 Jul) · IND1 2× INSA (₹190.5k lifetime / ₹1.8k daily) · IND6 paused · both LAL paused.
Expected 24–48h: account redistributes ~₹3.4k/day toward TM/INSA/DPIIT under the cap; IND1 CPL should fall (LAL was ₹445–569 vs INSA ₹281–337). Watchdog (08:00 IST) monitors; stop-loss checks daily.
