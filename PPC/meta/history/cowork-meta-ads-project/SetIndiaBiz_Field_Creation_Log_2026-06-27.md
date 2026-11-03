# SetIndiaBiz — Field Creation Log
**Date:** 27 Jun 2026 · **By:** Meta Ads operator (approved by Sanjeev) · **Org:** Setindiabiz Pvt Ltd · **CRM:** Zoho (connector, `createFields` API)

**Action:** Created **26 custom fields** across Leads, Deals, Accounts to close the Lead→Deal→Revenue attribution gap (per `SetIndiaBiz_Lead-Deal-Revenue_Field_Spec_2026-06-27.md`). All returned `SUCCESS`. Read-only verification (COQL select of every new API name) **passed** — all fields exist and are empty (`null` / `false`), nothing back-filled. No money, campaign, or record-data changes.

---

## Leads — 12 fields created
| API Name | Label | Type | Notes | Field ID |
|---|---|---|---|---|
| `Meta_Ad_Type` | Meta Ad Type | Picklist | Lead Form / Website / Call / WhatsApp / Instagram Post / Unknown | 1123581000911390050 |
| `Meta_Ad_Name` | Meta Ad Name | Text(255) | | 1123581000911390066 |
| `Meta_Ad_ID` | Meta Ad ID | Text(50) | | 1123581000911390075 |
| `First_Contact_Time` | First Contact Time | DateTime | speed-to-lead | 1123581000911390083 |
| `UTM_Source` | UTM Source | Text(100) | | 1123581000911390091 |
| `UTM_Medium` | UTM Medium | Text(100) | | 1123581000911390099 |
| `UTM_Campaign` | UTM Campaign | Text(150) | | 1123581000911390107 |
| `UTM_Content` | UTM Content | Text(150) | | 1123581000911390115 |
| `UTM_Term` | UTM Term | Text(150) | | 1123581000911390123 |
| `FB_Click_ID` | FB Click ID | Text(255) | = fbclid (CAPI match key) | 1123581000911390131 |
| `CTWA_Click_ID` | CTWA Click ID | Text(255) | = ctwa_clid (CAPI match key) | 1123581000911390139 |
| `WhatsApp_Number` | WhatsApp Number | Phone | | 1123581000911390147 |

## Deals — 9 fields created
| API Name | Label | Type | Notes | Field ID |
|---|---|---|---|---|
| `Meta_Campaign` | Meta Campaign | Text(255) | mirror of Lead | 1123581000911328088 |
| `Meta_Ad_Set` | Meta Ad Set | Text(255) | mirror | 1123581000911328098 |
| `Meta_Lead_Form` | Meta Lead Form | Text(255) | mirror | 1123581000911328106 |
| `Meta_Ad_Name` | Meta Ad Name | Text(255) | mirror | 1123581000911328114 |
| `Meta_Ad_Type` | Meta Ad Type | Picklist | same 6 values as Lead | 1123581000911328123 |
| `FB_Click_ID` | FB Click ID | Text(255) | = fbclid | 1123581000911328137 |
| `CTWA_Click_ID` | CTWA Click ID | Text(255) | = ctwa_clid | 1123581000911328145 |
| `First_Touch_Source` | First Touch Source | Picklist | 26 source values (mirror Lead_Source) | 1123581000911328154 |
| `Attribution_Confidence` | Attribution Confidence | Picklist | Direct (lead-linked) / Inherited (account) / Unknown | 1123581000911328189 |

## Accounts — 5 fields created
| API Name | Label | Type | Notes | Field ID |
|---|---|---|---|---|
| `First_Touch_Lead_Source` | First Touch Lead Source | Picklist | 26 source values | 1123581000911306073 |
| `First_Touch_Meta_Campaign` | First Touch Meta Campaign | Text(255) | | 1123581000911306109 |
| `First_Touch_Meta_Ad_Type` | First Touch Meta Ad Type | Picklist | same 6 values | 1123581000911306118 |
| `First_Touch_Date` | First Touch Date | Date | acquisition date | 1123581000911306132 |
| `Meta_Sourced` | Meta Sourced | Checkbox | defaults FALSE | 1123581000911306140 |

---

## Implementation status — ✅ COMPLETE (27 Jun 2026)
The configuration steps below are not exposed by the connector; they were completed in the Zoho Setup UI (conversion mapping by Sanjeev; the two workflows built via browser control):

1. ✅ **Lead Conversion Mapping** (Setup › Customization › Modules and Fields › Leads › ⋯ › Lead Conversion Mapping) — all 10 §5A mappings configured: Lead `Meta_Campaign`/`Meta_Ad_Set`/`Meta_Lead_Form`/`Meta_Ad_Name`/`Meta_Ad_Type`/`Lead_Source`/`Social_Lead_ID`/`Source_Url`/`FB_Click_ID`/`CTWA_Click_ID` → matching Deal fields; plus Lead→Account first-touch (`Meta_Campaign`→`First_Touch_Meta_Campaign`, `Meta_Ad_Type`→`First_Touch_Meta_Ad_Type`, `Lead_Source`→`First_Touch_Lead_Source`).
2. ✅ **Workflow — `Stamp Account Meta Sourced`** (Accounts, on Create; ACTIVE). Implemented as a **no-code Field Update** (simpler than the planned function): criteria `First_Touch_Lead_Source` is `PPC Meta Insta`/`PPC Insta` → set `Meta_Sourced` = true. `First_Touch_Date` left unused — Account `Created_Time` already serves as the acquisition date.
3. ✅ **Workflow — `Inherit Deal Attribution`** (Deals, on Create, `Account Name` is not empty; ACTIVE). Deluge function `Inherit_Deal_Attribution(int dealId)`: if Deal `Meta_Campaign` blank, copies Account `First_Touch_Meta_Campaign`/`First_Touch_Meta_Ad_Type`/`First_Touch_Lead_Source` → Deal `Meta_Campaign`/`Meta_Ad_Type`/`First_Touch_Source` and sets `Attribution_Confidence = Inherited (account)`; else marks `Direct (lead-linked)`. (Clean code in `Inherit_Deal_Attribution.txt`.)

### Still optional (not blocking)
- **Backfill** historical Meta leads/accounts (`Meta_Ad_Type` from campaign naming; `First_Touch_*` on existing Meta accounts).
- **Live test**: convert a Meta lead + create a job-deal on that account, confirm fields populate.
- Widen/retire Deals `Lead_Channel` (still defaults to "SEO").
4. **Layouts & profiles** — confirm the new fields appear on the page layouts/profiles you want (the API creates the field; layout placement may need a check).
5. **Backfill** (optional) — set `Meta_Ad_Type` on historical Meta leads from `Meta_Campaign`/`Meta_Ad_Set` naming; stamp `Account.First_Touch_*` on existing Meta-sourced accounts.
6. **`Lead_Channel` on Deals** — widen the 4-value picklist or retire in favour of `Lead_Source` (existing field; not touched here).

## Compliance
Schema-only change; no ad spend, campaign state, payment, or customer-record data was modified. Consistent with project guardrails (read/screenshot/scorecard auto; schema change on explicit human approval; money/campaign mutations never automated).
