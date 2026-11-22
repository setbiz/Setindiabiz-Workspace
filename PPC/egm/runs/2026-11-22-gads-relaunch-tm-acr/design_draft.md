# Campaign Plan: Google Ads · Trademark + Company Annual Filing · 2026-11/12 (DRAFT v1)

Status: **DRAFT for Goldfish review → owner approval.** Nothing in this plan is live. Both campaigns exist and are **PAUSED**.
Operator: Google Ads session. Approver: owner (Sanjeev). Labels: [data] = pulled from a connector (source + date given); [calc] = arithmetic on [data]; [est] = estimate / assumption.

## 1. Objective
Win profitable **Trademark registration** and **Private-limited company annual filing (AOC-4 / MGT-7)** clients in India from Google Search, judged on **Zoho CRM won deals and revenue**, not clicks or platform conversions. Annual Filing runs only through the MCA GC 05/2026 no-additional-fee window (to 31 Jan 2027). Trademark is a 4-week test.

## 2. Current state
- **Google Ads, last 12 months** [data: Supermetrics AW, 1 Nov 25–1 Nov 26]: two Dec-25 campaigns spent ₹99,927 and brought 84 CRM leads (`Advt - Google`) → **0 deals**. 63 were Lost (75%), 18 never worked (21%) [data: Zoho COQL, 22 Nov]. Trademark: 79% of visible spend went to IP-India portal / "trademark search" queries; only 7% to registration intent [calc from search-terms report].
- **Account today** [data: Supermetrics, 22 Nov]: Trademark campaign 24046453436 rebuilt (phrase/exact, 28 negatives, Search only, presence geo, Maximize Clicks with ₹60 cap, ₹1,500/day), 4 RSAs in review. Annual Filing campaign 24528891318 built (phrase/exact, 36 negatives, Maximize Clicks ₹80 cap, ₹1,000/day), 5 RSAs in review. Account has no shared negative list attached and no offline conversion import. Prepaid balance ≈ ₹4,630 [owner/handoff, 22 Nov].
- **Conversions** [data, 22 Nov]: only account-default goal = Submit lead form; only Primary action = GA4 form_submission (GA4 counting switched to once-per-session 22 Nov; Ads sync pending).
- **Same services on other channels, won deals closed 1 Nov 25–21 Nov 26** [data: Zoho COQL by `Product_Category` + `Lead_Source`; "won" = Won / W-* stages]:

| Service | Source | Won deals | Won ₹ | AOV ₹ [calc] |
|---|---|---|---|---|
| TM Filing in India | Advt – Facebook + Instagram | 36 | 82,809 | 2,300 |
| TM Filing in India | SEO – Google (organic) | 320 | 19,05,002 | 5,953 |
| TM Filing in India | All sources | 737 | 48,40,675 | 6,568 |
| Annual Filing | Advt – FB + IG + WhatsApp | 67 | 8,56,277 | 12,780 |
| Annual Filing | SEO – Google (organic) | 532 | 77,92,261 | 14,647 |
| Annual Filing | All sources | 1,251 | 1,90,96,393 | 15,265 |

Caveat: deal `Amount` may include government fees (unconfirmed) and some won Annual Filing deals are bundles; Lead_Source was migrated in 2026. Treat as directional.

## 3. Approach and why it should work
- **Google Search only, intent keywords only (phrase/exact)**, India, presence-only geo, Search partners off. Fixes the two Dec-25 failures (broad match into portal queries; foreign geo mismatch). Learning: `shared/learnings.md` 2026-11-02 Google entry.
- **Maximize Clicks with a CPC cap** (TM ₹60, AF ₹80) until ≥30 CRM-qualified conversions/30 days *and* offline import exists. No Maximize Conversions/tCPA: the only conversion is a form submit, which was 75% Lost last time.
- **Ad schedule Mon–Sat 09:00–19:00 IST** [new]: Meta shows 35–52% of ad leads unworked [data: weekly review 16 Nov]. Serve only when the sales desk is staffed so leads get called the same day.
- **Copy:** price-transparent (fees match the landing pages), private-firm disclaimer pinned, statutory facts with provisions (§8). Searchers who click "₹1,999 + GST + govt fee" are pre-qualified on price.
- **Why Annual Filing first:** highest won revenue of any category (₹1.91 cr, 1,251 deals in 12 months) and organic Google already converts it (532 won). There's a hard deadline (31 Dec AOC-4 / 31 Jan MGT-7 under GC 05/2026), and the paid AOV is ≈5.6× Trademark's.
- **Why Trademark as a capped test:** large volume (≈90,500 searches/month for "trademark registration" [data: Keyword Planner via handoff]) but paid-social AOV is only ₹2,300, so the economics are thin (§4).

## 4. Unit economics
Gross margin is unconfirmed: `kpis.md` uses an assumed **50%** [est]. Lead→won for Google Search is unknown. Facebook's 3.7% is the only paid baseline [data: business-context.md]. Range used: 3–8% [est].

| | Trademark | Annual Filing |
|---|---|---|
| AOV used | ₹2,300 (paid-social) – ₹5,953 (organic search) | ₹12,780 (paid) – ₹14,647 (organic) |
| Break-even CPA (AOV × 50%) [calc] | ₹1,150 – ₹2,977 | ₹6,390 – ₹7,324 |
| **Target cost per won deal** | **≤ ₹1,500** | **≤ ₹4,000** |
| Break-even CPL at 3% / 8% lead→won [calc] | ₹35–89 / ₹92–238 | ₹192–220 / ₹511–586 |
| **Target CPL (CRM lead)** | **≤ ₹150** | **≤ ₹400** |
| Expected CPC [est] | ₹16–60 (Dec-25 avg ₹16.5 on junk-heavy mix; intent terms cost more) | ₹30–80 (no history) |

**Reading:** Annual Filing has room. Trademark breaks even only if Google searchers buy closer to the organic AOV (₹5,953) or convert ≥8%. That is why it's a capped 4-week test with an early kill.

## 5. Budget and cap
| Campaign | Daily | Period | Max spend [calc] |
|---|---|---|---|
| Trademark | ₹1,500 | launch day + 28 days | ₹42,000 |
| Annual Filing | ₹1,000 to 30 Nov, then ₹1,500 | launch → 31 Jan 2027 (end date set) | ≈₹99,000 if launched 25 Nov (6 × ₹1,000 + 62 × ₹1,500) |
| **Total** | ≤ ₹3,000/day | | **≤ ₹1,41,000 maximum loss** |

- Google may spend up to 2× daily budget on a day; monthly spend is capped at 30.4 × daily.
- **Funds needed before launch:** at least the first 2 weeks ≈ ₹30,000–35,000 [calc]; balance today ≈ ₹4,630.
- Budget increase (Annual Filing ₹1,000 → ₹1,500 on 1 Dec) only with the owner's OK at the 1 Dec checkpoint.

## 6. Measurement
- **Primary metric:** Zoho CRM won deals and won ₹ with `Lead_Source = Advt - Google` and `UTM_Campaign` = campaign name, per campaign.
- **Leading metrics:** CRM leads, QL rate (Valid Lead + Proposal), unworked %, CPC, search-term junk share.
- **Event:** GA4 `form_submission` (only Primary). Platform conversions are diagnostic only.
- **Tags:** UTM suffix on both campaigns (`utm_source=google&utm_medium=cpc&utm_campaign={campaign}&utm_term={keyword}&utm_content={creative}`); auto-tagging on. Zoho's Lead Source workflow classifies `utm_source=google` + `cpc` → `Advt - Google` (attribution runbook).
- **GCLID capture (W1)** is with the landing-page session. Until it's live, there is no offline import, and CRM matching relies on UTM fields.
- **Reconciliation:** weekly (Mon) in `ppc-weekly-cycle`: Google clicks/form conversions vs Zoho `Advt - Google` leads by `UTM_Campaign`. A gap >30% is investigated before any budget change.
- **Decision threshold:** kill/scale rules in §7, evaluated on CRM numbers only.

## 7. Kill / scale rules (pre-registered)
**Launch gates (all must be true before enabling):**
G1 ads approved by Google (no government-documents disapproval); G2 account funded for ≥14 days; G3 a named sales owner calls Google leads within 2 working hours (owner to name); G4 a test lead from each landing page reaches Zoho as `Advt - Google` with UTM_Campaign filled.

**Trademark**
- Day 7 or ₹10,000 spent, whichever first: pause if CRM leads < 10, or > 40% of spend is on non-intent search terms after negatives are added.
- Day 14 or ₹21,000: pause if CPL > ₹300 or QL rate < 25%.
- Day 28 (≤ ₹42,000): **kill** if cost per won > ₹3,000 (break-even at organic AOV). **Continue** at the same budget if ₹1,500–3,000. **Scale** +20%/week only if ≤ ₹1,500 with ≥ 5 won.
- TM Search Test ad group stays paused for the whole test.

**Annual Filing**
- Day 7 or ₹8,000: pause if CRM leads < 8.
- Day 14 or ₹18,000: pause if CPL > ₹800 or 0 QL.
- 31 Dec 2026: **pause the deadline ads** (832341064930, 832283615649) and the "AOC-4 No Late Fee Till 31 Dec" headline. From 1 Jan 2027 the AOC-4 window has closed under GC 05/2026. MGT-7 copy may run to 31 Jan only after a copy edit.
- 31 Jan 2027: campaign ends (end date). Evaluate: keep for FY 2026-27 season (Sep–Nov 2027) only if cost per won ≤ ₹4,000.

**Both:** any government-documents disapproval → pause that ad, report the policy text to the owner. Do not re-appeal or build a consultation-only page (circumvention risk; account history in `history/2026-11-22-session-handoff.md`).

## 8. Risks
| Risk | Mitigation | Provision / policy |
|---|---|---|
| Account-level government-documents block (history of refused certificates; sibling accounts suspended) | Run only services that have passed review (Trademark, Annual Filing, LLP, Copyright). The escalation email to Google is in the owner's Gmail drafts | Google Ads "Government documents and official services" (answer/13156083, read 22 Nov 2026) |
| Implied government affiliation | Disclaimer pinned in description 1; no emblem; "Private Professional Firm" callout; LP disclaimer + official-portal link (W3) | Emblems and Names (Prevention of Improper Use) Act 1950 s. 3; State Emblem of India (Prohibition of Improper Use) Act 2005; CPA 2019 s. 2(28) |
| Price claims | ₹1,999 + GST + govt fee (TM); ₹4,599 / ₹5,999 / ₹7,999 + GST & ROC fee (AF): match LPs [data: LP fetch 22 Nov]. LP strike-through prices to be removed (W4) | CPA 2019 s. 2(28); CCPA Misleading Ads Guidelines 2022; CCPA Dark Patterns Guidelines 2023 (drip pricing) |
| Statutory facts in copy | TM govt fee ₹4,500 / ₹9,000 per class: Trade Marks Rules 2017, First Schedule. 10-year validity: Trade Marks Act 1999 s. 25. AF additional fee ₹100/day/form: Companies Act 2013 s. 403 + Companies (Registration Offices and Fees) Rules 2014. Director disqualification after 3 years' non-filing: s. 164(2)(a). No-fee window: MCA GC 05/2026 (24 Oct 2026, owner-verified 2 Nov) | Re-check each on India Code / mca.gov.in before enabling (TODO at gate) |
| Time claims: "Filed in 24 Hrs of Documents"; "100% Online Process" | LP states "File trademark in 24 Hrs". Owner confirmed the AF service is fully online (22 Nov) | ASCI Code Ch. I (substantiation) |
| Lead quality / unworked leads | Ad schedule; G3 SLA; weekly unworked % | — |
| Cannibalising organic Google (532 AF + 320 TM won from SEO) | Watch `SEO - Google` leads for the same services week on week. If organic falls while paid rises, test pausing paid on brand-adjacent terms. No brand keywords are bid on | — |
| Personal data | No Customer Match / list uploads in this plan. Enhanced Conversions only after the privacy notice is updated (W6) | IT Act 2000 s. 43A + SPDI Rules 2011 r. 4–5; DPDP Act 2023 (phased) |

## 9. Build sheet (deltas to apply at launch; everything else exists as read on 22 Nov)
Names follow the existing account (renaming to the `GADS_…` convention would reset nothing but break the UTM {campaign} mapping already in Zoho → keep names) [decision for owner].

**Both campaigns:**
1. Ad schedule: Mon–Sat 09:00–19:00 (account time zone Asia/Calcutta). No Sunday.
2. Keep: Search only, partners off, presence geo, IN, en + hi, UTM suffix, Maximize Clicks + CPC cap, AI Max off, no shared lists.

**Trademark 24046453436:** enable campaign + ad groups TM Registration (198205838563), Brand and Logo Registration (201984303749), TM Fees and Cost (205371377227) and their ads. **TM Search Test (202733915016) stays PAUSED.** Budget ₹1,500/day; CPC cap ₹60. Ads verbatim as live in the account on 22 Nov (see `google-ads/changelog.md` 22 Nov entry).

**Annual Filing 24528891318:** set end date 2027-01-31. Enable campaign + all 4 ad groups and 5 ads. Budget ₹1,000/day to 30 Nov, ₹1,500 from 1 Dec (owner OK at checkpoint). CPC cap ₹80. On 31 Dec, pause ads 832341064930 and 832283615649 (deadline copy).

**Not in this plan:** Company / LLP / GST / DPIIT / CFO / Payroll / Copyright campaigns (stay paused); India Entry campaigns (other session).

## 10. Review dates + changelog
- Day 7 and day 14 checkpoints after launch; Trademark decision at day 28; Annual Filing on 31 Dec (copy) and 31 Jan 2027 (end).
- Each weekly cycle (Mon) adds a row to `google-ads/changelog.md`: spend, CRM leads, QL, won, rule outcome.
- On launch, log: "Enabled Trademark + Annual Filing per plan `campaigns/202611-gads-relaunch-tm-acr.md`, approver owner, review <launch+7>".

## Open decisions for the owner
D1 Monthly cap ≤ ₹1.41L total over ~10 weeks (TM ₹42k + AF ≈₹99k): approve / change?
D2 Trademark budget ₹1,500/day (as built) or ₹1,000/day (₹28k max)?
D3 Name the sales owner for Google leads (G3).
D4 Launch before GCLID (W1) is live (UTM-only matching), or wait?
D5 Keep the current campaign names (recommended) or rename to the `GADS_…` convention?
