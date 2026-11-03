# 150 × ₹150 Optimisation Plan — 9 Jul 2026

**Goal (confirmed):** ~150 raw CRM leads/day at ~₹150 average CPL, budget ceiling ₹22,500/day, valid% held at or above current (~36–39%).
**Data:** Meta connector (spend/delivery, 2–8 Jul) + Zoho CRM `Lead_Source IN ('Advt - Facebook','Advt - Instagram')` (outcomes, 2 Jul → 9 Jul AM). Valid = status ∈ {Valid Lead, Negotiation, Proposal Sent, Payment Pending} — a floor; 113 of 249 leads still untriaged.

---

## 1. Where we are (post-restart week, 2–8 Jul)

| Campaign | Spend | Meta leads | CPL (Meta) | CRM leads | Valid | Valid% | Cost/valid |
|---|---|---|---|---|---|---|---|
| #IND3 Trademark | ₹9,431 | 65 | **₹145** | 60 | 25 | 41.7% | **₹377** |
| #IND4 CCFS | ₹38,964 | 88 | ₹443 | 74 | 34 | **45.9%** | ₹1,146 |
| #IND5 DPIIT | ₹15,051 | 46 | ₹327 | 41 | 12 | 29.3% | ₹1,254 |
| #IND1 Incorporation | ₹23,405 | 60 | ₹390 | 50 | 17 | 34.0% | ₹1,377 |
| #IND6 Virtual CFO | ₹10,607 | 23 | ₹461 | 21 | **1** | **4.8%** | **₹10,607** |
| **Account** | **₹97,458** | **282** | **₹346** | **246** | **89** | **36%** | **₹1,095** |

Run-rate ₹13,923/day, ~36 CRM leads/day. **Gap to goal: 2.3× on CPL, 4× on volume.**

## 2. Findings

**F1 — The ₹150 target already exists in-account.** TM runs at ₹145 CPL with 41.7% valid and the account's cheapest CPM (₹207–274), frequency only 1.20–1.37, on ~10% of spend. Best ads: C3B TM Ad 2 ₹65 CPL (11 leads), C3A TM Ad 7 ₹74, C3A TM Ad 6 ₹140, C3A TM Ad 2 ₹141 (28 leads). This is the scaling engine.

**F2 — LAL question answered: kill it.** Since 28 Jun (ad-set CRM attribution live): INSA ad sets 45.2% valid (14/31) vs LAL1% Director 22.7% (5/22); CPL ₹281–337 vs ₹445–569. LAL loses on **both** cost and quality (June review said LAL is defensible only if quality ~2.5× better — it's 2× *worse*). Small samples, but direction matches June CPL data. ₹1,873/day is parked there.

**F3 — IND6 CFO fails after creative rework too.** 21 leads, 1 valid (4.8%), ₹10,607/valid. Offer/market problem, not creative. Pause fully; frees ₹1,515/day.

**F4 — CCFS cliff on Sunday.** IND4 = 40% of spend and best valid% ends 12 Jul (scheme closes 15 Jul — CCFS-2026, MCA General Circular 01/2026; claims cannot run past it). ₹5,566/day and ~13 leads/day vanish. The replacement is **#IND2 Annual Return relaunch** — same deadline-compliance playbook: AGM by 30 Sep (s.96 Companies Act 2013), AOC-4 within 30 days / MGT-7 within 60 days of AGM (ss.137, 92), DIR-3 KYC by 30 Sep (r.12A, Companies (Appointment & Qualification of Directors) Rules 2014), LLP Form 8 by 30 Oct (s.34 LLP Act 2008). Director + LLP lists already exist.

**F5 — Don't cut Instagram; fix the creative format instead.** IG CPM ₹435 vs FB ₹262 (+66%), but IG leads validate at **43.8%** (35/80) vs FB 31.3% (55/176) → cost/valid IG ₹924 vs FB ₹1,184. Keep Advantage+ placements. The real gap: **zero 9:16 vertical/reels creative on any ad set** (Opportunity Score flagged all 4) — we pay feed-format prices for reels inventory. Scripts already drafted (Reels_Video_Scripts_2026-07-04.md).

**F6 — 4-Jul form change (2→1 qualifying questions) is showing early junk drift.** Valid% 38.8% pre (2–3 Jul) → 36.1% post (5–8 Jul, 46% untriaged so provisional). Targeting-bucket losses (Mistake 7 + Job Seeker 6 + Language 1 + Not Eligible 1 = 34% of 44 losses) vs 17% June / 11% baseline. Not fatal yet — but scaling cheap volume amplifies it. Keep friction on ad sets we scale.

**F7 — Schedule is right; don't touch it.** Delivery 08:00–19:00 IST (account TZ confirmed Asia/Calcutta), aligned to calling hours. Cost/click is flat by hour (₹30–42); 13:00–15:00 takes 40% of spend at only slightly worse efficiency. Evening (19:00–23:00) is untapped inventory but breaks speed-to-lead (Avoiding Call = #1 historical loss driver) — test only with a next-morning-first-call SLA + WhatsApp auto-acknowledgement in place.

**F8 — The billing pacing cap is the hard prerequisite.** Daily spend shows the limiter: ₹16,949.15 cap-days, ₹12,711.86 (0.75×), Sunday ₹8,475 (0.5×) — the ₹10L/59-day construct. **150/day at ₹150 needs ₹22.5k/day; nothing scales until the spending limit is raised in Ads Manager → Billing (your action only — I never touch payment settings).**

**F9 — Ops reality check.** 150 leads/day at ~37% valid ≈ 55 valid leads/day for the tele-team — 4× today's ~13. Speed-to-lead is already leaking (16 leads untriaged >48h on 6 Jul). Without RM capacity/SLA enforcement, extra spend converts to "Avoiding Call" losses, not revenue.

## 3. The plan (every Meta change needs your approval; one variable at a time; before/after screenshots; stop-loss logged)

### Phase 1 — this week: stop waste, fund winners (net ₹0 extra budget)
| # | Change | Money | Stop-loss / confirming metric |
|---|---|---|---|
| P1 | **Pause #IND6 CFO** (campaign) | frees ₹1,515/day | Account cost/valid falls within 7d |
| P2 | **Pause both C1 LAL1% ad sets**; stage the freed budget into C1 Daytime INSA + C1 24Hr INSA at +20%/day (guardrail-compliant, ~4 days to absorb) | reallocates ₹1,873/day | INSA CPL stays <₹350 and valid% ≥40%; else revert |
| P3 | **Scale #IND3 TM +20%/day compounding** (₹1.35k → ~₹4k/day over ~6 days) | +₹2,650/day (from P1 + CCFS release) | Pause scaling if 3-day CPL >₹250 or valid% <30% |
| P4 | **Trim DPIIT ads 2 & 4** (₹565/₹410 CPL) into DPIIT 1 (₹270); hold campaign budget flat — pool saturating (freq 2.17, reach 18k) | ₹0 | DPIIT CPL <₹300 |

### Phase 2 — from 13 Jul: replace CCFS, expand reach ("target more people")
| # | Change | Money | Stop-loss |
|---|---|---|---|
| P5 | **Relaunch #IND2 Annual Return** — Director FY + LLP lists, deadline copy per F4 (all statutory claims verified before launch) | start ₹3k/day (CCFS's released budget) | Day-7: CPL <₹400 and valid% ≥35%, else halve |
| P6 | **Two new IND1 ad sets:** (a) INSA-v2 fresh interest stack (GST registration, Startup India, MSME/Udyam, entrepreneurship) + Advantage detailed targeting; (b) **LAL 1–2% seeded from CAPI ValidLead/Won customers** — the quality seed we never had before 27 Jun | ₹1.5–2k/day each | Day-7: CPL <₹400, valid% ≥35% |
| P7 | **Reels 9:16 ads** from the 4-Jul scripts into TM, IND1 INSA, DPIIT (captures the IG quality advantage at reels-priced CPM) | within existing budgets | Ad-level: pause any reel >₹300 CPL after ₹1.5k spend |
| P8 | **2 creative variants vs Ad-1** in IND1 INSA (single creative since April = concentration risk) | within budget | Standard |

### Phase 3 — from ~16 Jul (once ≥50 CAPI ValidLead events accrued)
| # | Change |
|---|---|
| P9 | Switch **C1 Daytime INSA → quality (ValidLead) optimization** per the 2-Jul protocol; TM ad set follows if CPL holds. This is the structural fix that lets CPL fall *without* valid% falling. |
| P10 | **Form friction A/B on one scaled ad set:** restore the 2nd qualifying question (or disqualifying multiple-choice format). Decide on F6 data at day 14. |

## 4. Trajectory to 150 × ₹150 (honest maths)

| Checkpoint | Daily budget | Blended CPL | Leads/day | Valid/day (~37%) |
|---|---|---|---|---|
| Now | ₹13.9k | ₹346 | ~36 | ~13 |
| 16 Jul (Phase 1 done) | ₹14k | ~₹270–300 | 47–52 | ~18 |
| 23 Jul (P5–P7 live) | ₹17–18k | ~₹230–260 | 65–78 | ~26 |
| 1 Aug (quality-opt + reels scaled) | ₹20–22.5k | ~₹180–220 | 100–125 | ~40 |
| Mid-Aug (if gates pass) | ₹22.5k | **₹150–180** | **125–150** | ~50–55 |

₹150 blended is reachable only if TM-share grows, reels open cheap inventory, and IND2/INSA-v2 land near ₹250 entry CPL then compress. If any leg misses, the honest trade-off is 150/day at ~₹180–200 (needs >₹22.5k/day — your call then) or ~120/day at ₹150. Each checkpoint is a go/no-go gate, not a promise.

## 5. Prerequisites on your side
1. **Raise the account spending limit / pacing construct** in Ads Manager → Billing before Phase 2 (I never execute billing/money actions).
2. **RM capacity plan** for 4× valid-lead inflow + speed-to-lead SLA (the 6-Jul watchdog owner-level leak is still open).
3. Approvals for P1–P4 to start this week.

## 6. Verification notes
Campaign spends sum to ₹97,457.63 = daily spends sum ✓. CPL/cost-per-valid divisions recomputed programmatically ✓. CRM campaign-stamped total 246 + 3 unstamped = 249 = status-group total ✓ (FB/IG split query ran minutes later at 256 — live inflow, not an error). INSA 14/31 = 45.2%, LAL 5/22 = 22.7% ✓. Platform quality: IG 35/80 = 43.8%, FB 55/176 = 31.3% ✓. Windows use explicit +05:30 offsets (Zoho org on US DC — offsets keep IST windows exact).
