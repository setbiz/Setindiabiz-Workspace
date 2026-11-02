# Consolidated Goldfish review: Meta audit, 2 Nov 2026

**Reviewers (isolated, read-only, files only):** ppc-performance-critic, ppc-measurement-skeptic, ppc-budget-cfo, ppc-compliance-reviewer, ppc-customer-lens, egm-zoom-out (EGM built-in).
**Totals:** 6 Blockers · ~32 Majors · ~20 Nits. All arithmetic in the draft re-computed correctly. **No invented numbers.** The problems were in interpretation, completeness and the actions.
**Elephant follow-up already done:** campaign-level CRM backfill via Zoho `Meta_Campaign`, live ad copy pulled, WhatsApp figures re-queried. See `data.md` addenda.

## 🔴 Blockers
| # | Finding | Raised by | Resolution |
|---|---|---|---|
| B1 | Customer-list audiences (GST / LLP / Director lists) are live in "SIB-02 \| TM \| Lists \| Form \| 8C" with no recorded source, notice or basis. The website form says "used only to respond to your enquiry" | compliance, customer, CFO, critic | **Action 1**: pause the Lists ad set now and detach the lists everywhere |
| B2 | Draft cited DPDP ss. 4–6, 8 as current law. They commence ≈13 May 2027 (verify). In force today: IT Act 2000 s. 43A + SPDI Rules 2011 r. 4–5; CPA 2019 s. 2(47) (disclosure of personal info given in confidence; verify clause); Meta Custom Audience Terms | compliance | Citations corrected here and in `PPC/CLAUDE.md` |
| B3 | Annual-filing relaunch proposed with no data, cap or kill rule | critic, CFO | **Resolved by backfill:** CCFS 2.52× and Annual Filing product ₹4.52L won. Now justified with a cap and kill rule (Action 4) |
| B4 | SIB-05 live at ₹4,000/day with no loss cap; CPL ₹3,793 (n=6; 95% CI ≈₹1,740–10,350) | CFO, critic | **Action 3**: pause |
| B5 | "From USD 499" price not on the website | compliance | **Downgraded to Major:** the live creative states "Government fees, stamp duty and DSC extra, at actual cost" and is an Instant Form (no landing page). Remaining question: is USD 499 a real, honoured price? |
| B6 | No check of live ad copy | customer | **Resolved:** live copy pulled. New issue: "served 25,000+ businesses" vs website "18K+ clients" (Action 2) |

## 🟡 Key Majors (deduplicated)
- **Wrong break-even basis** (zoom-out, skeptic, critic, CFO): use the 90-day CRM basis. Revenue/CRM lead ₹352, so break-even CPL ≈ ₹176 at 50% margin. Blended CRM CPL ₹244 = 1.39× (not 2×). **Corrected.**
- **Reconciliation backwards** (all 4 quantitative reviewers): Meta 1,690 vs CRM FB+IG 1,515, so **175 Meta leads (≈10%, ≈₹47K) not found in Zoho as FB/IG**. Cause unknown. → Action 6.
- **SIB-01 "improving" was cherry-picked** (skeptic, critic, zoom-out): Meta also flags ROAS −62%. **The backfill confirms the bad news:** SIB-01 (assumed = Zoho "#IND 1 — Incorporation") returned **0.25×**: 7 won / 687 leads, ₹30,368 on ₹1,20,202.
- **Don't wait 30 days for attribution** (zoom-out, CFO, critic): **done today.** Zoho already has `Meta_Campaign`, `Meta_Ad_ID`, `Meta_Ad_Set` and `Product_Category`.
- **Drop Advantage+ creative bundle** (all six): too small to measure (n needed ≈17k/arm), generated text risks compliance claims, confounds the baseline. **Dropped.**
- **Too many edits on SIB-02** (skeptic, critic, CFO): 4 changes today. Take Action 1 as a status-only pause of the Lists ad set, then a 7-day no-edit window on SIB-02 Interest.
- **Two operators** (all): a person plus an "ads MCP server" AI session made unreviewed changes (USD 499 ad, list uploads, SIB-04 pause). → Action 8.
- **WhatsApp:** 0.9% lead→won, no opt-in line (compliance, customer). The 90-day = 12-month figures were **re-queried and are real**: all WhatsApp-ad leads fall after Aug 2026.
- **Missing from scorecard:** prior period, clicks/CTR/CPC, Pixel/CAPI health. → carried to next weekly run.

## Revised action list (Elephant recommendation after review; **nothing executed**)
| # | Action | Evidence | Approve? |
|---|---|---|---|
| 1 | **Pause ad set "SIB-02 \| TM \| Lists \| Form \| 8C"** (status only, ₹0 spent so far). Keep SIB-04's list ad sets off. Record each list's source, date, notice and uploader. Get a legal opinion on deleting or keeping. | B1, B2 | ☐ |
| 2 | Annual-filing creatives: replace "served 25,000+ businesses" with the substantiated website figure ("18K+ clients") or remove it. Confirm ₹7,499 / ₹2,499 / ₹1,999 / USD 499 are real list prices honoured in quotes. | B6, customer F3 | ☐ |
| 3 | **Pause SIB-05 India Entry** (0 won, CPL ₹3,793). Before any restart: India-entry AOV from Zoho, then a ₹15K cap / 14-day kill rule. | B4, backfill | ☐ |
| 4 | **Reactivate SIB-04 Annual Filings, interest/website ad sets only (no lists)**, until 29 Nov 2026 (MGT-7/7A due 60 days after AGM, Companies Act 2013 s. 92(4); AGM assumed 30 Sep; check MCA circulars for FY 2025-26 extensions). Cap **₹25,000 total**. Kill if CPL > ₹600 after ₹8,000. **First confirm why the AI session paused it today.** | CCFS 2.52×, Annual Filing ₹4.52L won, SIB-04 1.07× and early | ☐ |
| 5 | **Cut SIB-01 Incorporation budget by 50%** (current daily budget to be read before the change) and review lead quality: 687 leads → 7 won. Hypothesis: the price-led "Rs2499 + GST" form attracts price shoppers. Re-test after 2 weeks with CRM-qualified leads as the metric. Requires confirming that "#IND 1 — Incorporation" = SIB-01. | backfill 0.25× | ☐ |
| 6 | Investigate the 175-lead gap (Meta lead export vs Zoho, matched in scratch space, never committed) and the blank `Meta_Campaign` on 3 won deals. | reconciliation | ☐ |
| 7 | Trademark (SIB-02): no scaling. AOV ≈₹2,000 vs cost per won ₹2,500–3,600, so it loses at current CPL. Options: raise the package price, bundle with search/objection, or cap CPL ≤ ₹50. | backfill | ☐ (decide option) |
| 8 | Process: create `PPC/meta/changelog.md`. AI sessions **propose only**; a human approves every activation and audience upload, with a named approver logged. Check Automated Rules for any ON rule covering SIB-* campaigns. | all reviewers | ☐ |
| 9 | Later, after legal sign-off: Conversions API for CRM using `lead_id` only (no extra identifiers). | compliance, zoom-out | ☐ later |

**Dropped:** Advantage+ creative enhancements; SIB-05 merge (superseded by the pause).

## Still needed from the owner
1. **Gross margin %** and whether deal `Amount` includes govt fees. This decides whether CCFS / annual filing at 2.5× is profitable.
2. Confirm "#IND 1 — Incorporation" in Zoho = SIB-01 (renamed).
3. Who runs the "ads MCP server" sessions (Cowork?), and why was SIB-04 paused today?
4. Source of each customer list (MCA public data, CRM, purchased?).

## Owner resolution (2 Nov 2026)
| # | Decision |
|---|---|
| 1 | **Declined.** Owner accepts the data-protection position for now. Customer lists stay, including for annual-return campaigns. Recorded as an owner decision. |
| 2 | **Declined.** "25,000+ businesses" is verifiable per owner, so it stays. Follow-up: update the website's "18K+ clients" so both match. All prices (₹7,499 / ₹2,499 / ₹1,999 / USD 499) confirmed real. |
| 3 | **Revised.** India-entry AOV from Zoho (FDI category, 12 months, all sources): 17 won, ₹14,67,582, so **≈₹86,300 per deal**. At CPL ₹3,793 and 50% margin, break-even needs lead→won ≥ 8.8% [calc]. No longer "pause": keep running with a ₹15K further cap and judge on CRM-qualified India-entry leads. |
| 4 | Pending owner confirmation to reactivate SIB-04 (with lists, per owner). The AI session that paused it was Claude (Cowork). |
| 5 | **Approved.** SIB-01 ad-set budget ₹2,500 → ₹1,250 staged as a draft. Note: last 7 days SIB-01 spent only ₹3,439 (≈₹491/day) for 24 leads at ₹143, so the old budget wasn't binding. |
| 8 | Owner confirmed the "ads MCP server" sessions are Claude. Rule stands: log every change in `meta/changelog.md`. |


## Update (Cowork session log, 2 Nov 2026 evening)
- **Confirmed:** `#IND 1 — Incorporation` = SIB-01 (campaign 120240912969660449 renamed 12:51). The SIB-01 0.25× figure stands.
- **Confirmed:** the SIB-04 pause at 11:35 was the owner's decision, carried out via a Claude (Cowork) session.
- **New issue:** MCA General Circular 05/2026 makes the SIB-04 deadline copy inaccurate. See `meta/changelog.md`.
- **New issue:** prepaid balance vs ₹13,750/day of budgets. ₹25,000 was added 08:26 and ₹6,306 was spent by evening.
