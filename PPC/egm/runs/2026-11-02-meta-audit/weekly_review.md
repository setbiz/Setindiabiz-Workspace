# Meta Ads Audit — account SETINDIABIZ (152154124583473) — 2 Nov 2026

Elephant draft for Goldfish review. Read-only audit: **no changes were made to any ad account.** All numbers are in `data.md` with their source.

## 1. Data provenance
| Platform | Source | Date range | Compared with | Pulled at | Missing? |
|---|---|---|---|---|---|
| Meta | Meta Ads connector | last 90 days (≈4 Aug–2 Nov 2026) | Meta's fixed 28-day trend | 2 Nov 2026 | Campaign-level CRM outcomes; activity log only covers 21 Oct–2 Nov |
| CRM | Zoho CRM (COQL) | leads/deals created 4 Aug–2 Nov 2026 | — | 2 Nov 2026 | No campaign field, so won deals can't be split by campaign |

## 2. Scorecard (90 days)
| Platform | Spend ₹ | Leads (Meta) | CPL ₹ | Leads (CRM) | Won deals (CRM) | Won ₹ (CRM) | Cost/won ₹ | Revenue/spend |
|---|---|---|---|---|---|---|---|---|
| Meta (FB+IG+WA) | 4,50,929 | 1,690 | 267 | 1,851 | 61 | 6,51,039 | 7,392 | 1.44× |

vs target: the KPI file's break-even CPL is ≈₹130–135 at an assumed 50% margin. The blended CPL of ₹267 is about 2× that. At 1.44× revenue/spend, the account only breaks even if gross margin on `Amount` is ≥69%. **Margin is still unknown. This is the most important missing input.**

## 3. Tracking health
- Meta leads (1,690) vs CRM leads (1,851): CRM is higher. Plausible reason: WhatsApp click-to-chat leads (336 in CRM) aren't counted as Meta "leads". Reconciliation is approximately OK.
- **No campaign-level link from CRM to Meta.** The ROI of SIB-01 vs SIB-02 vs SIB-04 vs SIB-05 can't be judged.
- Meta recommends **Conversions API for CRM** (4 pts, "24% lower cost per quality lead"). That would also let Meta optimise towards qualified or won leads instead of form fills.

## 4. What happened and why (diagnosis; hypotheses are labelled)
1. **Seasonal campaigns took 56% of spend at the highest CPLs.** #IND4 CCFS (₹1.72L, CPL ₹435) and SIB-04 Annual Filings (₹0.81L, CPL ₹575) together cost ₹2.53L. Both are now stopped (deleted / paused today).
2. **The evergreen campaigns are cheapest per lead.** SIB-01 Incorporation is at CPL ₹175 and Meta's trend shows it improving. Trademark is at CPL ₹85–129 (SIB-02 new ₹85, #IND3 ₹129, SIB-02 old ₹117).
3. **SIB-05 India Entry is very expensive per lead.** CPL ₹3,793 (6 leads for ₹22,760), CPM ₹3,110, frequency 3.04 on 7,319 impressions: a tiny, saturated audience split across 3 ad sets (Meta flags fragmentation). *Hypothesis:* a high-value service could justify a high CPL, but India-entry deal value isn't known.
4. **Customer-list audiences:** director, LLP and GST contact lists (uploaded 31 Oct–2 Nov) are used in SIB-04 and were added today to SIB-02's "Lists" ad set. There's no documented lawful basis or notice for using these contacts in advertising (DPDP Act 2023 ss. 4–6, 8; see the ChatGPT-import review).
5. **Two operators are changing the account the same day:** a person (Power Editor) and an AI session via the "ads MCP server". There's no shared changelog, so changes can collide.

## 5. Due reviews
No `meta/changelog.md` entries yet. From the ChatGPT import: the value rules (website +20%, form −30%) and the business-hours rules from Jan 2026 can't be verified (rules aren't visible in the log window). Carry these over.

## 6. Proposed actions (ranked; **none executed**)
| # | Platform | Exact change | Evidence | Expected impact | Risk / reversible? | Review on |
|---|---|---|---|---|---|---|
| 1 | Meta | Remove director / LLP / GST customer-list audiences from "SIB-02 \| TM \| Lists \| Form \| 8C" (or pause that ad set). Keep SIB-04's list ad sets off until a lawful basis and notice are documented | Activity log 31 Oct–2 Nov; DPDP Act ss. 4–6, 8 | Removes a legal risk | Low risk; reversible | After legal review |
| 2 | Meta | SIB-05 India Entry: merge the 3 ad sets into 1 (Meta fragmentation rec) and cut the daily budget from ₹4,000 to ₹1,500 until CRM shows India-entry deal value | CPL ₹3,793, CPM ₹3,110, freq 3.04 | Lower waste while learning | Edits pause entities, so reactivate in the same step | 2 weeks |
| 3 | Meta | Hold SIB-01 and SIB-02 budgets (don't scale yet). First add campaign attribution to Zoho (utm_campaign / Meta campaign ID on every lead), then scale whichever has the better cost per **won** deal | Blended revenue/spend 1.44×; no campaign-level CRM data | Lets future scaling be judged on sales | No delivery change | After 30 days of tagged data |
| 4 | Meta + Zoho | Set up Conversions API for CRM (Zoho stage events: qualified, won) and later optimise to "conversion leads" | Opportunity Score rec (4 pts) | Meta claims "24% lower cost per quality lead" (Meta estimate) | Setup work; no spend change | After setup |
| 5 | Meta | MGT-7/7A season (due ≈29 Nov 2026 if AGM was 30 Sep; verify): relaunch an annual-filing campaign only with compliant copy (no unproven claims or govt implication), no customer-list audiences, and a capped budget | SIB-04 CPL ₹575; seasonal deadline | Captures seasonal demand at controlled cost | New entities start PAUSED | Weekly until 29 Nov |
| 6 | Meta | Apply the Advantage+ creative enhancements bundle on active ads | Opportunity Score (9 pts, "3% lower cost per result") | Small CPL gain (Meta estimate) | Reversible | 2 weeks |
| 7 | Process | Start `PPC/meta/changelog.md`. One operator per day, and every AI-session change logged | Same-day human + AI edits | Prevents collisions | None | — |

## 7. Needs human decision
- **Gross margin %** on the deal `Amount`, and whether `Amount` includes govt fees. Without these, no budget can be judged profitable.
- Approve or decline action 1 (customer-list audiences) and whether to get a legal opinion.
- India-entry average deal value (decides whether SIB-05 continues at all).
- Who runs the "ads MCP server" sessions (Cowork?), so all changes go through one log.
- "S1 | From USD 499" (SIB-05): is this price published and substantiated? The website states no package prices.
