# ChatGPT Ads: A5 status check and account audit (22 Nov 2026)

_Read-only. No change was made to the ad account or the CRM. Pulled 22 Nov 2026 (IST) from Supermetrics `CGPTA` (account `adacct_6a4a938005f0819d88f16e3e1c8c5e57`, "Setindiabiz Private Limited", INR, account timezone Asia/Kolkata) and Zoho CRM (COQL, aggregates only). 22 Nov is a part day. India Entry / FDI campaigns are reported only as a flag; they belong to the India Entry session._

## 1. Headline
1. **The account is not "2 live campaigns".** 9 campaigns are `ENABLED` with ₹16,400/day of daily budgets in total. Only **CFO Services** spends. GST Filing last spent on 14 Nov. Six enabled campaigns have **approved, enabled ads but have never spent**. The account has no daily cap (lifetime budget field = 1,000,000,000), so nothing stops them from starting. None of this is in the changelog.
2. **A5 QL leg: passed.** Since the 14 Nov restart: 12 `Advt - ChatGPT` CRM leads, **6 QL** (threshold 4), 4 still unworked.
3. **A5 ceiling: 77–83% used.** Spend since 14 Nov is ₹5,459.56 to ₹5,928.93, depending on the report (see §3). At the current ₹300–700/day, the ₹7,115 ceiling is reached around **24–26 Nov**.
4. **Still 0 won.** No deal with `Lead_Source` `Advt - ChatGPT` or `AI - ChatGPT` created since 1 Sep 2026. Lifetime spend since 1 Sep ≈ ₹69,000 [calc, ad report] for 68 paid-UTM CRM leads.
5. **Labelling: mostly correct, 2 leaks.** 66 of 68 paid-UTM leads are `Advt - ChatGPT`. 2 paid CFO leads are labelled `AI - ChatGPT`. Two enabled campaigns have **no UTMs**, so their leads would land as `AI - ChatGPT` or `Direct`.

## 2. Campaign status (campaigns endpoint, 22 Nov)
| Campaign | Status | Daily ₹ | Ads (enabled / approved) | Spend since 1 Sep ₹ | Last spend | Owner |
|---|---|---|---|---|---|---|
| CFO Services | ENABLED | 500 | 5 enabled; only "Founder support" approved, 4 rejected, "Outsourced accounts" approved but PAUSED | 20,414.52 [calc] | 22 Nov | This session |
| GST Filing | ENABLED | 500 | 5 enabled; 2 approved (Recurring compliance, Input review), 2 rejected, 1 in review; "Dedicated return support" approved but PAUSED | 17,163.22 [calc] | 14 Nov | This session |
| Trademark Registration | ENABLED | **2,000** | 6 enabled, 6 approved, UTMs present | 0 | never | This session |
| DPIIT Recognition | ENABLED | 500 | 5 enabled, 5 approved, UTMs present | 0 | never | This session |
| Setindiabiz \| Company Registration \| India \| Leads | ENABLED (start 30 Sep) | **2,900** | 1 enabled, approved, **no UTM** | 0 | never | This session |
| Setindiabiz \| Company Annual Return \| India \| Leads | ENABLED (start 17 Sep) | **2,500** | 5 enabled, 5 approved, **no UTM** | 0 | never | This session |
| Setindiabiz Private Limited campaign | PAUSED (start 2 Sep) | 2,900 | 1 approved, **no UTM** | 15,943.87 | before Oct | This session |
| Branch & Liaison Office Setup | ENABLED | 500 | (not read) | 15,477.40 | 1 Nov | India Entry session |
| India Entry | ENABLED | **3,500** | (not read) | 0 in ad report | — | India Entry session |
| Indian Subsidiary | ENABLED | **3,500** | (not read) | 0 in ad report | — | India Entry session |

Spend per campaign is the sum of its ads in the `ad` report, 1 Sep–22 Nov [calc]. **Why the six approved campaigns don't deliver is unknown.** The connector's change history returned no events for 24 Oct–22 Nov, so I can't say who created them or when. Check in ads.openai.com (delivery status, billing, approval date).

## 3. Spend since the 14 Nov restart (by day)
| Date | CFO ₹ (campaign report, UTC) | GST ₹ (campaign report, UTC) | Total ₹ (country report, by day) |
|---|---|---|---|
| 14 Nov | 990.02 | 569.94 | 1,930.63 |
| 15 Nov | 554.62 | 0 (8 impr.) | 654.22 |
| 16 Nov | 585.30 | — | 733.42 |
| 17 Nov | 616.52 | — | 394.99 |
| 18 Nov | 551.60 | — | 667.73 |
| 19 Nov | 544.94 | — | 203.07 |
| 20 Nov | 351.84 | — | 340.02 |
| 21 Nov | 292.68 | — | 621.02 |
| 22 Nov (part) | 402.10 | — | 383.83 |
| **Total** | **4,889.62** | **569.94** | **5,928.93** |

Campaign report total: **₹5,459.56** [calc]. The country report gives ₹5,928.93 by day and ₹5,621.74 without a date split. The `campaign` report defaults to UTC and the `country` report seems to follow the account's IST day, which explains the shifted days but not the ₹469 gap in totals. `CGPTA` is early-access, so **confirm the figure from billing in ads.openai.com**. For the ceiling I use the higher figure: **₹1,186 left** (₹7,115 − ₹5,928.93) [calc], or ₹1,655 on the lower one.

Platform conversions since 14 Nov: 4 (campaign report). CRM leads: 12. The platform under-counts, which fits "conversion tracking TODO".

## 4. CRM: `Advt - ChatGPT` and `AI - ChatGPT` (aggregates)
QL = Valid Lead + Proposal Sent. Unworked = Establishing Contact + empty (same definitions as the weekly run).

**Since 14 Nov (A5 window)**
| Source | UTM campaign | Valid | Proposal | Est. contact | Empty | Lost | Total | QL |
|---|---|---|---|---|---|---|---|---|
| Advt - ChatGPT | cfo_services | 5 | 0 | 1 | 3 | 2 | 11 | 5 |
| Advt - ChatGPT | gst_filing | 1 | 0 | 0 | 0 | 0 | 1 | 1 |
| AI - ChatGPT | — | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Total** | | 6 | 0 | 1 | 3 | 2 | **12** | **6** |

₹ per CRM lead ₹455–494; ₹ per QL ₹910–988 [calc, on ₹5,459.56–5,928.93]. Worked 8 of 12; QL rate among worked leads 75% [calc]. The weekly run counted 5 leads for 14–15 Nov with 4 unworked; 3 of the 4 now empty are newer leads.

**Since 1 Sep**
| Source | Valid | Proposal | Postponed | Est. contact | Empty | Lost | Total |
|---|---|---|---|---|---|---|---|
| Advt - ChatGPT | 8 | 0 | 1 | 2 | 11 | 44 | 66 |
| AI - ChatGPT | 1 | 1 | 0 | 1 | 0 | 1 | 4 |

By UTM (paid, `utm_source=chatgpt`, `utm_medium=paid`): cfo_services 39 (37 Advt + **2 AI**), gst_filing 28, branch_liaison_office 1. The other 2 `AI - ChatGPT` leads carry `utm_source=chatgpt.com` and no medium: these are organic ChatGPT referrals, correctly labelled (one is at Proposal Sent).

**Deals:** no deal with `Lead_Source` in (`Advt - ChatGPT`, `AI - ChatGPT`) created since 1 Sep 2026 (COQL returned no rows). The A5 "0 won by 31 Dec" leg is still live.

## 5. A5 verdict and recommendation
A5 (proposed in PR #4, not yet approved): hard ceiling ₹7,115 cumulative from 14 Nov; pause both campaigns if < 4 QL by then (worked leads only), or if 0 won by 31 Dec.

| Test | Status | Evidence |
|---|---|---|
| Ceiling ₹7,115 | 77–83% used, hit ≈ 24–26 Nov | §3 |
| ≥ 4 QL on worked leads | **Pass: 6** | §4 |
| ≥ 1 won by 31 Dec | Open: 0 won since Sep on ≈ ₹69k | §4 |

**Recommendation: keep CFO Services to the ceiling, then cap. Pause the dormant campaigns now.**
1. **CFO Services: keep** until ₹7,115, then **pause** (the ceiling is not something the platform enforces). Don't extend on QL alone: 66 paid leads since Sep produced 8 Valid and 0 won, and 44 were Lost. Extend only if at least one deal from the 14 Nov cohort reaches a `W-` stage, or the owner approves a new ceiling.
2. **GST Filing: leave as is, or pause for tidiness.** It has not spent since 14 Nov although 2 ads are approved. If it starts delivering again, its spend counts toward the same ₹7,115.
3. **Pause the 4 dormant campaigns this session owns** (Trademark ₹2,000, Company Registration ₹2,900, Annual Return ₹2,500, DPIIT ₹500 per day). That's ₹7,900/day of approved, unlogged budget that A5 doesn't cover and that could start any day. Two have no UTMs, so their leads would be mislabelled. Pausing removes spend risk only. Relaunching any of them goes through `/ppc-new-campaign`, built PAUSED. Trademark and ROC copy also needs a check against the ad-copy standard and the government-services rule in `PPC/CLAUDE.md` first.
4. **India Entry session:** India Entry ₹3,500, Indian Subsidiary ₹3,500 and Branch & Liaison ₹500 per day are ENABLED. Flagged to that session; it decides.

## 6. Lead labelling: what happens and the fix
**Observed:** 66 paid-UTM leads are `Advt - ChatGPT`, a value that isn't in the runbook's 38-value taxonomy. The deployed classifier in `shared/lead-source-attribution-runbook.md` §12 has no `Advt - ChatGPT` branch: rule 4 sends `utm_source=chatgpt` to `AI - ChatGPT`. So either the live function is newer than the runbook, or another step (form field or integration) sets the value. 2 paid leads (12 Oct, 26 Oct; 1 Valid, 1 Lost) ended up as `AI - ChatGPT`, which is what the runbook logic would produce.

**Proposed fix (owner approval needed for each CRM step):**
1. Confirm in Zoho how `Advt - ChatGPT` is set: the current function body and the picklist.
2. In `autoClassifyLeadSource`, add a paid-ChatGPT rule **before rule 4 (AI)**: `utm_source=chatgpt` (or `chatgpt.com`/`openai`) **and** `utm_medium` in (`paid`, `cpc`, `paid_social`) → `Advt - ChatGPT`. Keep organic ChatGPT referrals (no paid medium) as `AI - ChatGPT`.
3. Re-label the 2 paid `AI - ChatGPT` leads to `Advt - ChatGPT` with `updateRecords`, `trigger: []` (runbook §9).
4. Add `Advt - ChatGPT` to the runbook taxonomy (§2, §5, §13) once confirmed.
5. Any ChatGPT ad without UTMs gets the standard set before it runs: `utm_source=chatgpt&utm_medium=paid&utm_campaign=<slug>`. This applies to Company Registration, Annual Return and the paused "Setindiabiz Private Limited campaign", whose ₹15,944 of spend can't be traced to CRM leads.

I did not check whether OpenAI adds its own click ID to ad URLs. Confirm on ads.openai.com before relying on one.

## 7. Compliance notes
- **Rejected ads.** 4 of 6 CFO ads and 2 of 6 GST ads are `rejected`; one is `in_review`. Rejected ads with past spend were probably approved earlier and rejected on re-review. I haven't seen OpenAI's reasons. The July 2026 capture (chat #30) quoted OpenAI's policy as not permitting ads for "legal services … and document preparation", which may explain it. **Verify against OpenAI's current advertising policies** before any new copy.
- **Ad claims** in new or relaunched copy follow the Consumer Protection Act 2019 s. 2(28) (misleading advertisement), the CCPA Guidelines for Prevention of Misleading Advertisements and for Endorsements in Advertisements, 2022, and the ASCI Code. Before relaunch, check that the current notified versions haven't been amended. The "IPR attorneys" line in the Trademark ads needs substantiation on file.

## 8. Asks for the owner
| # | Decision | Type |
|---|---|---|
| D1 | Approve A5 as written (PR #4), with CFO paused at ₹7,115 cumulative (≈ 24–26 Nov) | Approval |
| D2 | Pause Trademark, Company Registration, Annual Return and DPIIT now | Approval (spend-risk reduction) |
| D3 | GST Filing: pause, or leave it within the same ceiling | Choice |
| D4 | CRM: approve the classifier change and the 2-lead re-label (§6) | Approval |
| D5 | Confirm spend to date from ads.openai.com billing (₹5,460 vs ₹5,929) | Fact check |
| D6 | Who created the 6 never-delivered campaigns, and were they meant to run? | Fact check |
