# SetIndiaBiz — Lead → Deal → Revenue Field & Conversion-Mapping Spec
**Date:** 27 Jun 2026 · **Segment:** `Lead_Source = PPC Meta Insta` · **Source of truth:** Zoho CRM × Meta Ads connector
**Scope chosen:** all four Meta ad types (Lead Form, Website/Traffic, Call, WhatsApp); revenue measured **two ways — first-deal and account lifetime value (LTV)**.

> ✅ **Status — 27 Jun 2026:** all **26 custom fields created** in Zoho and verified via API — 12 Leads, 9 Deals, 5 Accounts. The two click-ID fields were created as `FB_Click_ID` and `CTWA_Click_ID` (Zoho derived these from the labels). Still to do in Zoho admin (not available through this API): the conversion mapping (§5), the Account→Deal inheritance workflow, and backfill. Full audit trail: `SetIndiaBiz_Field_Creation_Log_2026-06-27.md`.

> One-line answer: your **Leads** are well-instrumented for Meta, but the attribution **dies at conversion** — Deals have no Meta fields, and the recurring "job" deals that carry most lifetime revenue are created outside lead conversion entirely. You need a small set of new fields on **Deals** and **Accounts**, a conversion mapping, and (for Call/WhatsApp/Web) a handful of capture fields on **Leads**.

---

## 1. The gap in one picture

```
            M');  Meta ad  ─────────────► LEAD ──────────────► DEAL ─────────► ACCOUNT
                                  (rich)        (conversion)   (blind)        (LTV, blind)
 campaign / adset / form / ad      ✅ ~98%        ✗ not carried   ✗ no fields    ✗ no first-touch
 Social_Lead_ID (match key)        ✅             ✗ empty on Deal  ✗              —
 Lead_Source / channel             ✅             ~12% / default   wrong          ✗
 quality / status / funnel         ✅             n/a              n/a            n/a
 revenue (Amount, 7 won stages)    —              —                ✅             ✅ rollup
```

Both halves of the data exist in Zoho — **Meta campaign/adset on the Lead, won-revenue on the Deal** — but today you **cannot connect a single rupee of won revenue back to a Meta campaign, ad set, or ad.**

### Verified evidence (pulled live 27 Jun 2026)
- **Inbound works:** of **869** `PPC Meta Insta` leads in the last 30 days, `Meta_Campaign` is filled on **851 (98%)**. Split: #IND1 Business Registration 507 · #IND3 Trademark 196 · #IND4 CCFS 70 · #IND2 Annual Return 40 · #IND5 DPIIT 28 · #IND6 Virtual CFO 10 · blank 18. `Meta_Ad_Set` and `Meta_Lead_Form` are captured too (lower fill on older leads); individual **ad** is not captured as a structured field.
- **Lead→Deal link mostly holds from the Lead side:** of **71** Meta leads that converted in the last 90 days, **64 (90%)** have the `Converted_Deal` lookup populated.
- **Deal side is blind:** on recent Deals, `Meta_*` fields **don't exist**; `Lead_Source` is populated on ~1 in 8; `Lead_Channel` defaults to **"SEO"** (wrong for Meta); `Campaign_Source`, `Source_Url`, and `leadchain0__Social_Lead_ID` are **null on 100%**.
- **Most Deals bypass lead conversion:** **8 of 10** recent deals are recurring job-deals (ACR, Annual Return, Shop Act, TM Renewal) created from the account/job workflow with `Lead_Number` / `Lead_Created_Time` / `Lead_Source` all **null**. These carry recurring revenue but have **zero** lead/Meta lineage.
- **Revenue itself is clean:** Deal `Amount` + a 7-stage "won" family + the Accounts `Deal_Revenue` rollup (lifetime value). The problem is *attribution*, not revenue capture.

> **Schema change — 27 Jun 2026:** the *Facebook Advert Manager* extension was uninstalled, removing the `facebookadvertmanager__Facebook_Ad` lookup (and its `facebook_Accounts` module) from Leads. Verified live: the **LeadChain** fields — `Meta_Campaign`, `Meta_Ad_Set`, `Meta_Lead_Form`, `leadchain0__Social_Lead_ID` — are **unaffected and still populating** on the newest leads. The only loss is the ad-level lookup, which means ad-level identity now has **no field at all** — making the proposed `Meta_Ad_Name` / `Meta_Ad_ID` fields a real gap to fill, not just a nicety.

---

## 2. What you already have (relevant fields only)

### Leads — well instrumented
| Purpose | Field(s) | State |
|---|---|---|
| Meta attribution | `Meta_Campaign`, `Meta_Ad_Set`, `Meta_Lead_Form` (text); `Facebook_ID` (text) | Campaign/adset/form filling via LeadChain (~98% campaign). Ad-level lookup **removed 27 Jun 2026** with the extension → **no ad-level / ad-type field** |
| Match key | `leadchain0__Social_Lead_ID` | Well filled on form leads |
| Web context | `Source_Url`, `First_Visited_URL`, `Referrer`, `Lead_IP_Address` | Present; **no parsed UTM / fbclid** |
| Source / channel | `Lead_Source` (27 vals incl `PPC Meta Insta`), `Lead_Channel` (11 vals) | Good |
| Quality | `RM_Lead_Quality`, `Mkt_Leat_Quality` (TL), `CSD_Lead_Quality` (14-val) | RM ok; TL mostly blank |
| Funnel | `Lead_Status`, `Why_Disqualified` (21), `Lost_Date`, `Lost_Confirmed` | Good |
| Lead value | `Lead_Amount` (currency); `MX_Total_Sale_Value` / `_Prof_Fee` / `_TP` / `_GST` (formulas off `Product_Matrix`) | Partial fill |
| Timing | `Created_Time`, `Lead_Assigned_on` (**empty**), `Lead_Conversion_Time`, `Lead_Age`; `Lead_Status_Modified_Time` (not COQL-selectable) | No first-contact stamp |
| Conversion links | `Converted__s`, `Converted_Contact`, `Converted_Account`, `Converted_Deal`, `Converted_Date_Time` | ~90% link to a deal |
| Channel hint | `Contact_Method` (incl. "WhatsApp Call") | Not an ad-type field |

### Deals — revenue rich, attribution poor
| Purpose | Field(s) | State |
|---|---|---|
| Revenue | `Amount`, `Expected_Revenue`, `Total_Sale_Value` (formula), `RM_Product_Matrix` subform, many CSD/SPI/Tally currency fields | Good |
| Stage (won) | `Stage` — **7 won**: `Won`, `W-ACR Login`, `W-Login`, `W-Finance`, `W-CSD`, `W-SPI`, `W-SKV`; lost: `Refunded`, `Lost-Sales`, `Lost-Final`; open: `Qualified`, `Follow-Up`, `Negotiation`, `Payment Wait` | Use `Forecast_Category__s = Closed` for won, never `Stage='Won'` alone |
| Attribution (exists, empty) | `Lead_Source`, `Lead_Channel` (only 4 vals), `Campaign_Source` (→Campaigns), `Source_Url`, `leadchain0__Social_Lead_ID` | **Empty / defaulted** |
| Meta attribution | — | **ABSENT — no `Meta_*` field at all** |
| Lead lineage | `Lead_Number` (text echo), `Lead_Created_Time`, `Lead_to_Deal_Minutes`, `Lead_Amount`, `Lead_Stage` | Only on lead-converted deals (minority) |
| Lost reason | `Lost_Reasons` (custom, 21 — used), `Reason_For_Loss__s` (stock, 10) | Under-filled |

### Accounts — lifetime value, no source memory
| Purpose | Field(s) | State |
|---|---|---|
| LTV | `Deal_Revenue` (rollup: Σ won Deal `Amount`), `Deals_Won` (count), `Outstanding`, `SPI_Earned` | Works |
| Attribution | — | **None — no `Lead_Source`, no Meta, no first-touch** |

---

## 3. The Lead → Deal conversion mapping — reality

**How Zoho works.** Converting a Lead creates/links a **Contact + Account + (optional) Deal**. A custom field's value carries across **only if** (a) a compatible field exists on the target module **and** (b) it is added to *Setup → Lead Conversion Mapping*. Standard fields (`Lead_Source`, name, email, phone) auto-map if configured.

**Why attribution is lost today — two break points:**
1. **No target fields on Deals.** `Meta_Campaign`/`Meta_Ad_Set`/`Meta_Lead_Form` have nowhere to land, so they can't be mapped. `leadchain0__Social_Lead_ID` *does* exist on Deals but isn't in the mapping (empty on 100% of deals).
2. **Most deals never go through lead conversion.** Recurring job-deals are spun up from the Account ("Create Deal" workflow). A perfect lead→deal mapping still wouldn't attribute these — they need to **inherit first-touch from the Account.**

**Consequence for the two revenue views:**
- **First-deal revenue** *is* reconstructable today from the **Lead side** (`Converted_Deal` → Deal `Amount`/`Stage`), but only ~90% linked, only for post-stamping leads, and clumsy in COQL/Analytics.
- **LTV** is **not** measurable by Meta source at all, because downstream recurring deals carry no source.

---

## 4. Recommended new fields (the create-list for your approval)

Legend — **P0** unblock first-deal attribution · **P1** LTV + speed-to-lead · **P2** new ad types / web. Type = Zoho field type. "Map from" = lead-conversion / workflow source.

### 4A. LEADS — add capture gaps (12 fields)
| # | Proposed API name | Label | Type | Values / notes | Prio |
|---|---|---|---|---|---|
| 1 | `Meta_Ad_Type` | Meta Ad Type | Picklist | `Lead Form` / `Website` / `Call` / `WhatsApp` / `Instagram Post` / `Unknown` | **P0** |
| 2 | `Meta_Ad_Name` | Meta Ad | Text(255) | individual ad name | P0 |
| 3 | `Meta_Ad_ID` | Meta Ad ID | Text(50) | numeric ad id — stable key | P1 |
| 4 | `First_Contact_Time` | First Contact Time | DateTime | stamped on first outbound touch | **P0** (speed-to-lead = #1 loss driver) |
| 5 | `UTM_Source` | UTM Source | Text(100) | website/LP leads | P2 |
| 6 | `UTM_Medium` | UTM Medium | Text(100) | website/LP leads | P2 |
| 7 | `UTM_Campaign` | UTM Campaign | Text(150) | website/LP leads | P2 |
| 8 | `UTM_Content` | UTM Content | Text(150) | ad/creative | P2 |
| 9 | `UTM_Term` | UTM Term | Text(150) | keyword/audience | P2 |
| 10 | `FB_Click_ID` | FB Click ID | Text(255) | match key for web/LP leads (CAPI) | P2 |
| 11 | `CTWA_Click_ID` | CTWA Click ID | Text(255) | match key for WhatsApp ads (CAPI) | P2 |
| 12 | `WhatsApp_Number` | WhatsApp Number | Phone | WA-sourced leads | P2 |

*Already on Leads — just enforce fill, no new field:* `Meta_Campaign`, `Meta_Ad_Set`, `Meta_Lead_Form`, `leadchain0__Social_Lead_ID`, `Lead_Source`, `Source_Url`, `Lead_Amount`, quality + status fields, **`Lead_Assigned_on`** (currently empty — populate for routing lag).

### 4B. DEALS — add the mirror + match keys (9 fields)  ← biggest unlock
| # | Proposed API name | Label | Type | Map from (Lead) | Prio |
|---|---|---|---|---|---|
| 1 | `Meta_Campaign` | Meta Campaign | Text(255) | `Meta_Campaign` | **P0** |
| 2 | `Meta_Ad_Set` | Meta Ad Set | Text(255) | `Meta_Ad_Set` | **P0** |
| 3 | `Meta_Lead_Form` | Meta Lead Form | Text(255) | `Meta_Lead_Form` | P0 |
| 4 | `Meta_Ad_Name` | Meta Ad | Text(255) | `Meta_Ad_Name` | P1 |
| 5 | `Meta_Ad_Type` | Meta Ad Type | Picklist (same 6 vals) | `Meta_Ad_Type` | **P0** |
| 6 | `FB_Click_ID` | FB Click ID | Text(255) | `FB_Click_ID` | P2 |
| 7 | `CTWA_Click_ID` | CTWA Click ID | Text(255) | `CTWA_Click_ID` | P2 |
| 8 | `First_Touch_Source` | First Touch Source | Picklist (mirror `Lead_Source` 27 vals) | Account first-touch (for job-deals) | P1 |
| 9 | `Attribution_Confidence` | Attribution Confidence | Picklist | `Direct (lead-linked)` / `Inherited (account)` / `Unknown` | P1 |

*Already on Deals — populate via mapping, do **not** create:* `leadchain0__Social_Lead_ID`, `Lead_Source`, `Source_Url`, `Lead_Number`, `Lead_Created_Time`, `Lead_to_Deal_Minutes`, `Amount`, `Stage`, `Lost_Reasons`. **Also widen `Lead_Channel`** from 4 → the 11 values used on Leads (or retire it in favour of `Lead_Source`).

### 4C. ACCOUNTS — first-touch memory for LTV (5 fields)  ← makes LTV-by-source possible
| # | Proposed API name | Label | Type | Values / notes | Prio |
|---|---|---|---|---|---|
| 1 | `First_Touch_Lead_Source` | First Touch Source | Picklist (mirror `Lead_Source`) | stamped once, from the converting lead | **P1** |
| 2 | `First_Touch_Meta_Campaign` | First Touch Meta Campaign | Text(255) | | P1 |
| 3 | `First_Touch_Meta_Ad_Type` | First Touch Meta Ad Type | Picklist (same 6 vals) | | P1 |
| 4 | `First_Touch_Date` | First Touch Date | Date | acquisition date | P1 |
| 5 | `Meta_Sourced` | Meta Sourced? | Checkbox | quick filter for Meta-acquired accounts | P1 |

*Already on Accounts — use as-is:* `Deal_Revenue` (LTV), `Deals_Won`, `Outstanding`, `SPI_Earned`.

**Total new fields: 12 Leads + 9 Deals + 5 Accounts = 26.** The P0 subset (the minimum to attribute *won revenue to a Meta campaign*) is just **6 fields** (Deals 1,2,3,5 + Leads 1,4).

---

## 5. Conversion-mapping & inheritance spec

**A. Lead → Deal (Setup → Lead Conversion Mapping):**
```
Lead.Meta_Campaign            → Deal.Meta_Campaign
Lead.Meta_Ad_Set              → Deal.Meta_Ad_Set
Lead.Meta_Lead_Form           → Deal.Meta_Lead_Form
Lead.Meta_Ad_Name             → Deal.Meta_Ad_Name
Lead.Meta_Ad_Type             → Deal.Meta_Ad_Type
Lead.leadchain0__Social_Lead_ID → Deal.leadchain0__Social_Lead_ID   (field exists; add to map)
Lead.Lead_Source              → Deal.Lead_Source                    (enforce)
Lead.Source_Url               → Deal.Source_Url
Lead.FB_Click_ID / CTWA_Click_ID       → Deal.FB_Click_ID / CTWA_Click_ID
```

**B. Lead → Account (first-touch, write-once):**
```
Lead.Lead_Source              → Account.First_Touch_Lead_Source     (only if blank)
Lead.Meta_Campaign            → Account.First_Touch_Meta_Campaign    (only if blank)
Lead.Meta_Ad_Type            → Account.First_Touch_Meta_Ad_Type     (only if blank)
Lead.Created_Time             → Account.First_Touch_Date             (only if blank)
(Lead_Source starts with 'PPC Meta'/'PPC Insta') → Account.Meta_Sourced = true
```

**C. Account → Deal (the LTV fix for job-deals):** a workflow on Deal create — *if* `Deal.Meta_Campaign` is blank, copy `Account.First_Touch_Meta_Campaign / _Ad_Type / First_Touch_Lead_Source` into the Deal and set `Attribution_Confidence = Inherited (account)`. This is what attributes recurring revenue back to the original Meta source.

---

## 6. Per-ad-type capture & one-yardstick measurement

| Ad type | Meta objective | How it enters Zoho | Key fields (new in **bold**) | Meta-native metric |
|---|---|---|---|---|
| **Lead Form** (Instant Form) | Leads | LeadChain (live) | `leadchain0__Social_Lead_ID`, `Meta_Campaign`/`_Ad_Set`, **`Meta_Ad_Type=Lead Form`** | Cost / lead |
| **Website / Traffic** (landing page) | Leads / Traffic | Pixel + CAPI `Lead`; hidden form fields push UTM + click id | **`UTM_*`**, **`FB_Click_ID`**, `Source_Url`, **`Meta_Ad_Type=Website`** | Cost / LP view → lead |
| **Call ads** | Calls | Call-tracking number / Zoho PhoneBridge → auto-create Lead | **`Meta_Ad_Type=Call`**, **`First_Contact_Time`**, call duration (Calls module) | Cost / call |
| **WhatsApp** (Click-to-WhatsApp) | Engagement / Messages | WhatsApp Business API / Zoho integration → auto-create Lead | **`CTWA_Click_ID`**, **`WhatsApp_Number`**, **`Meta_Ad_Type=WhatsApp`** | Cost / conversation started |

**One measurement model for all four** (Zoho Analytics pivot): rows = `Meta_Ad_Type` → drill `Meta_Campaign` → `Meta_Ad_Set` → `Meta_Ad_Name`; measures =
`Leads → Valid % → Progressed % → Committed % → Won %`, plus **cost per valid / progressed / committed / won** (Meta connector spend), plus the two revenue columns below. This lets a cheap-but-junky WhatsApp lead and a pricier-but-better form lead be judged on the **same** objective hierarchy (cost per *won*, never cost per raw lead).

---

## 7. Revenue model — both views, side by side

| View | Definition | Built from | Sliced by |
|---|---|---|---|
| **First-deal revenue** | `Amount` of the first won deal tied to the originating Meta lead | `Deal.Amount` where `Forecast_Category__s = Closed`, joined via `Converted_Deal` or `Deal.Meta_*` | `Deal.Meta_Ad_Type` / `Meta_Campaign` |
| **Lifetime value (LTV)** | Σ of all won deals for the customer over time | `Account.Deal_Revenue` rollup | `Account.First_Touch_Meta_Ad_Type` / `First_Touch_Lead_Source` |

Then per Meta source: **ROAS-first-deal = first-deal revenue ÷ spend** and **ROAS-LTV = LTV ÷ spend** (spend from the Meta connector, account-level until ad-level attribution is confirmed). LTV is the number Meta should ultimately optimise toward — it captures the recurring ACR / annual-return / GST / KYC revenue that a single first purchase hides.

---

## 8. How this connects to the closed loop (CAPI)

The same new match-key fields on the **Deal** — `leadchain0__Social_Lead_ID`, `FB_Click_ID`, `CTWA_Click_ID` (+ hashed email/phone already present) — are exactly what the **Conversions API** needs to fire a `Purchase` event **with the deal `Amount`** when a deal reaches a won stage. So this field work is the CRM-side prerequisite for the outbound loop in `Zoho-Meta_CAPI_Implementation_Runbook.md`: build the fields → map them → then send graded events (ValidLead → Qualified → Purchase) back to Meta keyed on these IDs.

---

## 9. Suggested sequence

1. **P0 — first-deal attribution (1–2 days, admin-only):** create Deals fields 1,2,3,5 + Leads `Meta_Ad_Type`, `First_Contact_Time`; add the §5A mapping; backfill `Meta_Ad_Type` from campaign/adset naming; enforce `Lead_Source` on Deals. → *Confirming metric:* a Zoho Analytics pivot of won `Amount` by `Deal.Meta_Campaign` returns non-blank rows.
2. **P1 — LTV + speed-to-lead:** Accounts first-touch fields + §5B/5C inheritance; populate `Lead_Assigned_on`; stamp `First_Contact_Time`. → *Confirming metric:* `Account.Deal_Revenue` sliced by `First_Touch_Meta_Ad_Type` is non-empty; lead→first-contact median computable.
3. **P2 — new ad types & web:** `UTM_*`, `FB_Click_ID`, `CTWA_Click_ID`, `WhatsApp_Number`; landing-page hidden-field wiring; WhatsApp Business API + PhoneBridge call capture. → *Confirming metric:* leads appear with `Meta_Ad_Type ∈ {Website, Call, WhatsApp}`.

*Effort:* P0/P1 are **Zoho admin** config (fields + mapping + 2 workflows). P2 needs **LeadChain settings** (web/UTM, CTWA) and **integration work** (WhatsApp API, call tracking). No code for P0/P1.

---

## 10. Compliance guardrail

These are measurement fields only. Any **new creative** for Website / Call / WhatsApp ads must keep claims accurate and defensible under the **Companies Act 2013**, **LLP Act 2008**, and **CGST Act 2017** — no false guarantees, no fabricated timelines, no misrepresentation of MCA/ROC/government fees. Field changes here do not touch ad spend or campaign state; per project guardrails, schema creation will be done in **one batch on your explicit approval**, and no money/campaign mutation is performed.

---

*Data sources: Zoho CRM connector — `getFields` (Leads 138 after the 27 Jun extension removal, Contacts 174, Deals 201, Accounts 163) and COQL on `Lead_Source = 'PPC Meta Insta'` and Deals, pulled live 27 Jun 2026. Meta spend context from the Meta Ads connector (account 152154124583473). Companion: `Zoho-Meta_Signal_Audit_2026-06-27.md`, `Zoho-Meta_CAPI_Implementation_Runbook.md`.*
