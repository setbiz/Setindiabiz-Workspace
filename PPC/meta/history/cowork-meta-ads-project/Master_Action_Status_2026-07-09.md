# Master Action Status — Meta Ads Optimisation project
**Compiled 9 Jul 2026** from all working sessions (26 Jun – 9 Jul), project files, and operator memory. This is the handover doc for fresh chats — point any new chat here first.
**Goal of record:** 150 raw CRM leads/day @ ₹150 avg CPL, ceiling ₹22.5k/day, valid% ≥ ~36–39%. Glidepath: 16 Jul ₹270–300 → 23 Jul ₹230–260 → 1 Aug ₹180–220 → mid-Aug ₹150–180.

## ✅ DONE (built & verified)
| # | Item | When |
|---|---|---|
| 1 | Lead→Deal→Revenue attribution architecture: 26 new fields, Lead→Deal conversion mapping, 3 workflows (Account Meta_Sourced stamp, Deal inheritance, Direct-label), backfills (1,775 leads Meta_Ad_Type; 953 accounts first-touch) | 27 Jun |
| 2 | Zoho→Meta **CAPI loop LIVE** (ValidLead/QualifiedLead/Committed/Purchase; dataset 1242417817083521); TL-quality trigger expansion | 27–28 Jun |
| 3 | LeadChain Meta_Campaign/Ad_Set/Form mappings restored on all 7 chains + 77-lead gap backfill | 28 Jun |
| 4 | Billing restart + C1 Daytime budgets ₹150k→₹185k after the 29 Jun–2 Jul blackout | 2 Jul |
| 5 | Full 30-day account review (Account_Review_2026-07-02.md) | 2 Jul |
| 6 | V2 instant-form chains mapped & auto-backfilled; CCFS V2 ad-set row patched | 4 Jul |
| 7 | Reels 9:16 scripts drafted (Reels_Video_Scripts_2026-07-04.md); Opportunity Score reviewed (only real gap = vertical video) | 4 Jul |
| 8 | Supermetrics let expire; all reporting on Meta connector | 5–6 Jul |
| 9 | Lead_Source taxonomy migration: CAPI rule + both function gates + WF1 fixed for 'Advt - Facebook'+'Advt - Instagram'; 25 missed events backfilled | 6 Jul |
| 10 | **"Auto-set Lead Source from URL" classifier de-fanged** (was rewriting paid leads to 'Direct' on any edit) + **200 flip-victim leads restored** to 'Advt - Facebook' | 9 Jul |
| 11 | **Hourly CAPI sweep sender live** (`sib_capisweep` + Meta_CAPI_Sent checkbox) — durable ValidLead delivery independent of Rule 1's Kiosk-path defect; first run events_received:20 | 9 Jul |
| 12 | **150×150 plan + Phase 1 executed:** IND6 confirmed paused · both C1 LAL1% ad sets paused · Daytime INSA lifetime →₹190,500 · 24Hr INSA daily →₹1,800 · DPIIT ads 2 & 4 paused (via browser; API ToS-blocked) | 9 Jul |
| 13 | **CCFS extended to 20 Aug** (campaign via API, ad set manually by Sanjeev) after verifying scheme extension to 31 Aug — MCA General Circular 03/2026 | 9 Jul |
| 14 | **Scheduled tasks consolidated to ONE** (`setindiabiz-meta-daily-watchdog`, 08:00 IST: ops watchdog + stop-loss board + CAPI health + QA sweep + Monday rollup); 4 old tasks disabled & marked safe-to-delete; valid IN-list fixed to live 'Valid - ' prefixed picklist values | 9 Jul |
| 15 | Pilot specs written (Pilot_Specs_2026-07-09.md): WA auto-follow-up, TM call ads, CTWA, website retest | 9 Jul |

## 🟢 LIVE / MONITORING (daily task carries these)
- **INSA stop-loss:** revert budget raises if 3-day CPL >₹350 or valid% <30%; staging +20%/day continues until ~₹4.3k/day combined absorbed.
- **TM ramp trigger:** raise TM lifetime budgets (SA →₹109k, Director →₹56.5k) when TM actual ≥₹1,900/day or 13 Jul; stop-loss 3-day CPL >₹250.
- **DPIIT post-trim:** CPL <₹300 confirm; no budget increases (pool ~18k, freq >2.1).
- **CCFS re-pace:** ~₹3k/day expected to 20 Aug; flag ₹0 or >₹5k/day.
- **Form-change watch:** post-4-Jul cohorts valid% (38.8→36.1 early) + junk-losses (Mistake+Job Seeker 34% vs 17% baseline) → restore 2nd question if >30% persists a week (P10).
- **CAPI gate:** cumulative ValidLead toward ≥50/ad-set/week → then P9 switch C1 Daytime INSA to quality optimisation (structural fix).
- **Must stay paused:** IND6, both LAL ad sets, DPIIT 2 & 4.
- Speed-to-lead exceptions + loss buckets daily; Monday full-funnel rollup + source distribution.

## 🔴 WAITING ON SANJEEV
1. **Billing spending-limit raise** (Ads Manager → Billing) — hard prerequisite for ₹22.5k/day Phase 2. (Never done by Claude.)
2. **Pilot 0 inputs:** WhatsApp provider/number for outbound (Tiya's WABA?), template sign-off, WA-contact line on forms.
3. **Pilot 1 input:** dedicated phone number for TM call ads + who answers.
4. **RM capacity & speed-to-lead SLA** — 150/day ⇒ ~55 valid/day (4× today); owner-level leak (Kumar, 6 Jul) unresolved.
5. **IND2 Annual Return relaunch approval** (~₹3k/day from CCFS release; creative build via browser; statutory deadline copy ready to draft).
6. **2-minute Kiosk test:** one RM changes RM Quality on an Advt lead at a known minute while we watch Rule 1 usage (confirms why RM-path edits skip it).
7. **Zoho Analytics scorecard queries** still 'Advt - Facebook'-only → approve adding 'Advt - Instagram'.
8. Housekeeping approvals: archive ~60 stale audiences · delete Deals picklist stray 'Self - Referral' · First_Touch_Lead_Source option-list still old-scheme · Accounts split-brain (964 accounts carry old 'PPC Meta Insta' first-touch value) · align #IND1 campaign-name pair.

## 🟡 CLAUDE'S QUEUE (gated/scheduled)
1. Next INSA staging increments after each morning's stop-loss check.
2. TM budget-raise brief at trigger (13 Jul latest).
3. IND2 relaunch build on approval + verify TM V2 / IND2 chains stamp correctly on first organic leads.
4. Pilots in order: P0 WA follow-up (Zoho workflow) → P1 call ads → P2 CTWA (gated on WA capture + taxonomy decision — a new Lead_Source value would need CAPI gates + daily-task filters updated) → P3 website retest (gated on CAPI ≥50 ValidLead/wk + P9 done).
5. Browser-route ad work (API ad-level writes blocked by leadgen-ToS 1815089 despite accepted terms): CCFS copy "15 July"→"31 August 2026" · broken-reel reference cleanup on one CCFS ad · P7 reels ads (scripts ready) · P8 two creative variants vs Ad-1 in INSA.
6. P9 quality-optimisation switch at CAPI gate; P10 form-friction A/B at day-14.

## ⚠️ Standing quirks (read before touching anything)
Ad-level API writes fail (1815089) — browser only; ad-set/campaign API fine. `ads_update_entity` force-pauses — always reactivate after. COQL: binary-nested WHERE, IST offsets, dual-form valid IN-list ('Valid - ' prefixes live). Modified_Time polluted by 4-Jul rename + hourly sweep touches. LeadChain batch syncs distort Created_Time. Account spending-limit pacing (₹16,949.15 signature) is the binding constraint until raised. CAPI test lead 1123581000888516561 = do not work.

**Key files:** Optimisation_Plan_150x150 · Change_Log_2026-07-09_P1-P4 · Pilot_Specs · Account_Review_2026-07-02 · Operator_Instructions · Zoho_to_Meta_CAPI_Deluge · LeadChain_V2_Form_Mapping · Reels_Video_Scripts.
