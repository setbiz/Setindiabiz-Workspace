# India Entry (FDI) — Diagnosis, 14 Nov 2026

**Scope:** India Entry Services for foreign companies (subsidiary, branch, liaison, project office, FDI compliance). Read-only. No ad account or CRM record was changed.
**Sources (pulled 14 Nov 2026):** Zoho CRM COQL (Deals, Leads); Meta Ads connector, account 152154124583473; repo baselines `google-ads/reports/2026-11-02-baseline-12m.md` and `microsoft-ads/reports/2026-11-02-baseline-12m.md` (no Google or Microsoft delivery since; last 90 days were nil on 2 Nov); Supermetrics source list.
**Aggregates only.** No names, emails or phone numbers. `[calc]` = my arithmetic on the source numbers.

---

## 1. Where India-entry revenue actually comes from (Zoho, deals closed 1 Nov 2025 – 14 Nov 2026)

Won = stages starting `W-` (same assumption as `shared/business-context.md`). Scope = `Report_Cat = FEMA` (Product Cat "FDI" 17 deals, ₹14,67,582 — matches the 2 Nov figure — plus "RBI and Fema" 3 deals, ₹1,63,898). No deals carry Product Cat "BO-LO-PO".

| Lead Source on the deal | Won deals | Won ₹ | Share of ₹ [calc] |
|---|---|---|---|
| SEO - Google | 11 | 9,78,681 | 60.0% |
| (blank) | 6 | 2,84,304 | 17.4% |
| Direct | 2 | 2,11,203 | 12.9% |
| Self - Web Chat | 1 | 1,57,292 | 9.6% |
| **Any `Advt - *` (paid)** | **0** | **0** | **0%** |
| **Total** | **20** | **16,31,480** | AOV ≈ ₹81,574 [calc] |

- `Lead_Channel` = "SEO" on all 20. `UTM_*` and `First_Touch_Source` are empty on all 20, so keyword, page and campaign are not recorded.
- `Country_Region`: India 18, United Kingdom 1 (₹2,06,769), United States 1 (₹86,212). "India" most likely reflects the Indian entity's address, not the parent's country, so **the parent-country mix of won FDI clients is unknown** (data gap).
- Lost: 3 deals (₹38,500), 2 blank source, 1 IVR call.

### FDI-category leads, same 12 months (Leads, Product Cat FDI / BO-LO-PO / RBI and Fema, by Created_Time)
92 leads: SEO - Google 24 · Direct 19 · SEO - Email 15 · **Advt - Facebook 10** · Self - Web Chat 7 · **Advt - Google 4** · Self - Cold Call 3 · **Advt - Instagram 2** · AI - ChatGPT 2 · AI - Perplexity, Self - IVR Call, **Advt - ChatGPT**, Social - WhatsApp, **Advt - Microsoft**, SEO - Zoho Booking 1 each. Paid = 18 of 92 (20%) [calc].

**No FDI lead is marked converted (`Converted__s` = false on all 92).** Deals are created without lead conversion, so lead → won by source cannot be computed. This is the biggest measurement gap for this service line (see §5).

**Finding 1.** Every rupee of India-entry revenue in 12 months came from organic Google search, direct traffic or chat. Paid channels have produced leads but no won FDI deal yet. Paid search for the same intent is therefore the most logical paid test: it targets the queries that already convert organically.

---

## 2. Meta SIB-05 India Entry (campaign 120247067847480449), 21 Oct – 14 Nov 2026

Status: campaign and all 6 ads ACTIVE; not delivering since 13 Nov because the prepaid balance is nil. **It will resume spending at ₹4,000/day as soon as funds are added.** The owner's ₹15,000 post-2-Nov cap is already exceeded (₹18,463 spent 2–13 Nov, per `reanalysis-2026-11-14.md`).

### 2a. Totals (Meta) vs CRM
| Spend ₹ | Meta leads | CRM leads (`Meta_Campaign` starts "SIB-05") | Qualified (Valid Lead + Proposal Sent) | Won | ₹ per CRM lead [calc] | ₹ per QL [calc] |
|---|---|---|---|---|---|---|
| 41,223.41 | 8 | 8 | 3 | 0 | 5,153 | 13,741 |

Capture is 100% (8 = 8). Of the 8: 1 Proposal Sent, 2 Valid, 1 Lost, **3 Establishing Contact, 1 no status (4 not yet worked)**.

### 2b. By ad
| Ad (ad set) | Spend ₹ | Share [calc] | Impr. | CTR | CPM ₹ | Leads | ₹/lead |
|---|---|---|---|---|---|---|---|
| B2 Branch office (Branch-Liaison) | 26,394.40 | 64.0% | 7,882 | 1.40% | 3,349 | 7 | 3,771 |
| S1 From USD 499 (Subsidiary) | 7,979.01 | 19.4% | 2,660 | 0.71% | 3,000 | 1 | 7,979 |
| B1 Liaison office (Branch-Liaison) | 3,247.82 | 7.9% | 702 | 0.43% | 4,627 | 0 | — |
| E1 India entry (India Entry) | 2,333.23 | 5.7% | 768 | 0.78% | 3,038 | 0 | — |
| E2 Structures (India Entry) | 1,092.95 | 2.7% | 319 | 0.63% | 3,426 | 0 | — |
| S2 After incorporation (Subsidiary) | 176.00 | 0.4% | 54 | 0% | 3,259 | 0 | — |

B2 frequency 2.5 (reach 3,154) — at the day-7 creative-swap threshold in the build spec.

### 2c. By country (Meta audience country) with CRM quality (parent-company country from the form)
| Country | Spend ₹ | Share [calc] | CPM ₹ | Meta leads | CRM quality |
|---|---|---|---|---|---|
| UAE | 16,277.84 | 39.5% | 2,714 | 4 | 0 QL (1 lost, 2 not worked, 1 no status) |
| **US** | 13,361.78 | 32.4% | 8,420 | 3 | **3 QL (1 proposal, 2 valid) → ₹4,454 per QL [calc]** |
| Canada | 5,663.33 | 13.7% | 3,781 | 1 | 0 QL (not worked) |
| Australia | 2,158.89 | 5.2% | 4,433 | 0 | — |
| Japan | 1,888.14 | 4.6% | 985 | 0 | — |
| Singapore | 1,277.27 | 3.1% | 3,234 | 0 | — |
| South Korea | 596.16 | 1.4% | 1,183 | 0 | — |

### 2d. By placement
| Placement | Spend ₹ | Share [calc] | CPM ₹ | Leads |
|---|---|---|---|---|
| Facebook Reels | 17,090.22 | 41.5% | 3,448 | 5 |
| Facebook Feed | 9,274.76 | 22.5% | 2,174 | 1 |
| Instagram Reels | 6,608.88 | 16.0% | 3,734 | 2 |
| Instagram Feed | 4,643.37 | 11.3% | 4,648 | 0 |
| Facebook Stories | 1,836.81 | 4.5% | 8,873 | 0 |
| Instagram Stories | 1,769.37 | 4.3% | 9,513 | 0 |

**Finding 2.** SIB-05 is not a dead campaign, it is a mis-allocated one. **All 3 qualified leads came from the US (₹4,454 per QL)**, while UAE took the largest share (39.5%) and produced 0 qualified leads. Meta's lead-volume optimisation pushes spend to the cheaper-CPM market, not the one that qualifies. Stories (₹3,606, 0 leads, CPM ≈ ₹9,000) and the four non-B2 ads (₹14,829 [calc], 1 lead) are waste. Small numbers (n = 8 leads), so directional.

**Finding 3.** Break-even check: at AOV ≈ ₹86,300 (FDI category) and an assumed 50% margin (still unconfirmed), one won deal is worth ≈ ₹43,150 of margin [calc]. At ₹4,454 per US QL, a QL → won rate of ≥ 10.3% [calc] breaks even. At the blended ₹13,741 per QL it needs ≥ 31.8% [calc]. US-only is plausible; the current mix is not.

---

## 3. Google Ads and Microsoft Ads history (from the 2 Nov baselines; no delivery since)

| Platform | Campaign | Period | Spend ₹ | Clicks | CPC ₹ | Platform conv. | CRM won |
|---|---|---|---|---|---|---|---|
| Google (1859576856) | NPDI_SET_India_Subsidiary_Registration_Dec-25 (removed) | Dec 2025 | 28,092 | 75 | 374.6 | 1 | 0 |
| Microsoft (150488150 / 150329248) | 2026 - Overseas - India Entry Services (paused) | 2026 | 4,607 | 109 | 42.3 | 0 | 0 |
| Microsoft | 2026 - Overseas - Indian Subsidiary (paused) | 2026 | 314 | 6 | 52.3 | 0 | 0 |

Known defects from the baselines: Google had gov-services policy disapprovals, no negative keywords and a conversion action that did not match CRM leads; Microsoft recorded 0 conversions against 46 `Advt - Microsoft` CRM leads overall, so UET / goals are not working. Neither test had offline (CRM) conversion import. **These tests did not fail on demand; they failed on setup** (₹375 CPC with no negatives, no geo/keyword discipline, no CRM feedback). Search-term reports for the Dec-25 subsidiary campaign have not yet been pulled — next step before keyword planning.

---

## 4. Platform access (Supermetrics, 14 Nov)
| Platform | Status | Owner action |
|---|---|---|
| Google Ads `AW` | Authenticated | — |
| Microsoft Ads `AC` | Authenticated | — |
| Meta `FA` + Meta Ads connector | Authenticated | — |
| LinkedIn Ads `LIA` | **Not authenticated** | Connect: https://gcp1-api-default.supermetrics.com/v2/datasource/login/renew/8NSbFR2v5qEgANVzh3kU0SXmgOK883TP3JZwJSWK3FHE8olnI1 |
| X Ads `TA` | **Not authenticated** | Connect: https://gcp1-api-default.supermetrics.com/v2/datasource/login/renew/SblAVehhuChSi09fJxOzfrf8eyZ6OIL9qUrm38zBwTpKV9fK5o |
| Reddit Ads `RDA` | **Not authenticated** | Connect: https://gcp1-api-default.supermetrics.com/v2/datasource/login/renew/_Ibt8WOonwLYGiTbcSsdpC1OHZtVYW5WcdI5Jum0n0IFrRTS2Q |
| ChatGPT Ads `CGPTA` (early access) | **Not authenticated** | Connect: https://gcp1-api-default.supermetrics.com/v2/datasource/login/renew/g9bU8Y_iLF1ad2tp0_K1Q7kQ1iapXGBcuKeNNXOuqhOoidOgyg |

Supermetrics can create/update campaigns on LinkedIn and ChatGPT Ads once connected; X and Reddit would be reporting only (build in their own UIs). Login links are session-generated and may expire; the hub is https://hub.supermetrics.com/token-management?team_id=1070415.

---

## 5. Measurement gaps to fix before scaling any paid India-entry channel
1. **Deal ↔ lead link.** FDI deals are created without lead conversion, so no paid lead can ever be credited with a win. Fix in sales process: convert the lead into the deal (or populate the deal's `Lead_Source`, `UTM_*` and `Meta_*` fields). Without this, every channel test will read "0 won".
2. **UTM capture on deals** is empty for all 20 won deals; Google/Microsoft click IDs (`gclid`, `msclkid`) need to flow lead → deal to support offline conversion import (Google Ads offline conversions / enhanced conversions for leads; Microsoft offline conversions; Meta CAPI already sends ValidLead/QualifiedLead).
3. **Parent-company country** is captured on Meta leads (`Select_Country`) but not on website leads or deals. Add a "country of parent company" field to the India-entry website form (owner is rewriting the page).
4. **Speed-to-lead:** 4 of 8 SIB-05 leads are not worked; 2 UAE leads in "Establishing Contact". Overseas leads need a time-zone plan (US leads arrive overnight IST).

---

## 6. Recommendations (for owner decision; nothing executed)
1. **Pause SIB-05 now, before the next Meta top-up** — it is over the ₹15,000 cap and will restart automatically at ₹4,000/day. Restructure, don't relaunch as-is (US-first, B2-led, Feed + Reels only) — that goes into the channel plan.
2. **Lead paid India-entry with Google Search (and Microsoft) on the intent that already converts organically**, US first, with negatives, policy-safe copy and CRM offline conversion import from day 1.
3. **Fix the deal ↔ lead link (§5.1)** before judging any channel on "won".
4. **Sales:** work the 4 unworked SIB-05 leads this week.
