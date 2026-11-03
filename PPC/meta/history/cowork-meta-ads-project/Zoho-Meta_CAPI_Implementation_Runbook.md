# SetIndiaBiz — Zoho ↔ Meta Closed-Loop Implementation Runbook
**Date:** 27 Jun 2026 · **Business:** Setindiabiz Pvt Ltd (629080835992237) · **Account:** SETINDIABIZ (152154124583473) · **Dataset:** setindiabiz (1242417817083521)

> Goal: make Meta optimise for **quality** (valid → qualified → won) instead of raw form-fills, by sending Zoho downstream outcomes back to Meta, matched to the original lead and ad.

---

## 0. Current state (why this is needed)

- Inbound (Meta → Zoho) works: LeadChain captures `Social_Lead_ID`, `Meta_Campaign`, quality + status fields.
- Outbound (Zoho → Meta) is dead: dataset has **no crm/offline channel**, **CAPI Gateway = NOT_ONBOARDED**, **server events silent since 18 Feb 2026**, all 4 custom conversions **never fired**, ad sets optimise on a raw web `Lead`.
- Result today: Meta is blind to quality and optimises for cheap form-fills.

---

## 1. The event mapping (Zoho → Meta) — the core spec

Events to send back, mapped to **your real Zoho values**:

| # | Journey stage | Meta event | Zoho trigger (actual values) | Value |
|---|---|---|---|---|
| 1 | Raw lead | `Lead` | Lead created, `Lead_Source = PPC Meta Insta` | 0 |
| 2 | Valid lead | `ValidLead` (custom) | `RM_Lead_Quality` ∈ {Valid - RM Working, Valid - Product Not Ready, Valid - NIL RM Action, Valid - Casual RM Action, Valid - Good RM Action} **or** `Lead_Status = Valid Lead` | 0 |
| 3 | Qualified / progressed | `QualifiedLead` (custom) | Deal `Stage` ∈ {Qualified, Follow-Up, Negotiation} = Forecast 'Pipeline' | 0 |
| 4 | Committed | `Committed` (custom) | Deal `Stage` = Payment Wait = Forecast 'Committed' | optional est. value |
| 5 | Won (purchase) | `Purchase` (standard) | Deal `Stage` ∈ {Won, W-SKV, W-SPI, W-CSD, W-Finance, W-Login, W-ACR Login} = Forecast 'Closed' (7 stages) | **Deal amount (INR)** |
| — | Exclude / suppress | (none or `Refund`) | {Lost-Sales, Lost-Final, Junk, Old-Disqualified, Refunded} and `RM_Lead_Quality` Invalid/Fake/Duplicate | — |

**Match keys (sent with every event, in priority order):**
1. `lead_id` = `leadchain0__Social_Lead_ID` — strongest; Meta matches lead-form leads directly on this.
2. `em` (SHA-256 email), `ph` (SHA-256 phone in E.164, e.g. +91XXXXXXXXXX).
3. `fbc` / `fbp` cookies — for website/landing-page leads only.

**Action source:** CRM / system-generated (offline). The cleanest route below (Conversion Leads) keys on `lead_id`, so match quality for form leads is effectively guaranteed.

> ⚠️ **Two confirmations needed from you:** (a) that the `W-*` stages = closed-won (they look like "Won – [dept]" service-delivery stages — 10,866 records vs only 14 in "Won"); (b) which stage we optimise toward first (recommendation: start on **ValidLead** for volume, move to **QualifiedLead** once each ad set clears ~tens of events/week).

---

## 2. Conversions API — the correct method

**Recommended: "Conversion Leads" via the LeadChain CRM integration.** Purpose-built for lead-form + CRM, matches on `lead_id`, needs no developer.

Fallbacks (only if needed): direct CAPI with an access token (needs a server/dev to POST events) or CAPI Gateway/Openbridge (paid; currently `NOT_ONBOARDED` — skip).

**Live steps in Events Manager** (we'll do these together, screen-by-screen):
1. Confirm scope: business `629080835992237`, dataset **setindiabiz** (`1242417817083521`).
2. **Data sources → Server**: note last received = 18 Feb 2026 (confirms dormant).
3. **Settings → Conversions API**: connect via **Partner Integration → Zoho (LeadChain)**, or generate an access token if going direct.
4. **Conversion Leads / CRM**: on the Page, confirm Zoho LeadChain is the connected CRM and enable **Conversion leads**; map CRM milestones → Meta lead stages per §1.
5. **Lead-gen ToS**: both connected Pages show `leadgen_tos_accepted = false` — accept at `facebook.com/legal/leadgen/tos` (needed for lead ads / Conversion Leads).
6. **Fix custom conversions** (4 currently never-fired): correct the "Form Submission" rule (it wrongly checks `PageView` whose name contains "Lead") or replace with the CRM events from §1; archive the misconfigured "Submit Forn".
7. **Switch optimisation** — only after events flow with volume: move active ad sets from `OFFSITE_CONVERSIONS` (raw web Lead) → **Conversion Leads / Qualified event**.

---

## 3. LeadChain metrics update (Zoho extension)

In **Zoho CRM → Setup → Marketplace → LeadChain** (or the LeadChain dashboard):
1. Enable **"send conversion / stage data back to Meta"** (offline-conversion / Conversion-Leads sync).
2. Map **`Lead_Status` / `RM_Lead_Quality` / Deal `Stage` → Meta events** exactly per §1.
3. Set match keys: **Social Lead ID** (already captured) + email + phone.
4. **Ad-level attribution ("LeadChain fix")**: confirm `Meta_Ad_Set` *and* the ad id are written on every lead (today only `Meta_Campaign` is reliably populated). Without this, cost-per-quality can only be reported at campaign level.
5. Backfill hygiene: `Mkt_Leat_Quality` (TL Quality) is empty across the board — partial quality data weakens the signal you send back.

---

## 4. New ad types — capture, taxonomy & measurement

**Taxonomy (decided):** keep single `Lead_Source = PPC Meta Insta`. Separate types with a new picklist field **`Meta Ad Type`** = {Lead Form, WhatsApp (CTM), Call, Landing Page}. Add campaign-name tokens `[FORM]` / `[WA]` / `[CALL]` / `[WEB]` as a parser backup.

**Capture wiring** (WhatsApp & Call are *not in CRM today* — must be built):

| Ad type | Meta side | Capture into Zoho | Meta-native metric |
|---|---|---|---|
| WhatsApp (Click-to-WhatsApp) | Messaging objective; capture `ctwa_clid` | Route the WA number through WhatsApp Business API / Zoho integration → auto-create Lead, `Meta Ad Type = WhatsApp`, store `ctwa_clid` for match-back | Cost per conversation started |
| Call ads | Calls objective | Call-tracking number / Zoho Telephony (PhoneBridge) → log call as Lead, `Meta Ad Type = Call`, store duration | Cost per call |
| Landing page | Traffic/Leads to LP | Pixel + CAPI `Lead` on the LP, push `fbc`/`fbp` + UTM into hidden form fields → Lead, `Meta Ad Type = Landing Page` | Cost per LP view → cost per lead |

**Measurement framework (one model for all types).** For each `Meta Ad Type`, track the objective hierarchy:
`Valid % → Progressed % → Committed % → Won %`, and `cost per valid / progressed / committed / won`. Build a Zoho Analytics pivot: rows = `Meta Ad Type` (drill to `Meta_Campaign` → `Meta_Ad_Set`), measures = the funnel above. This is what lets you compare a cheap-but-junky WhatsApp lead against a pricier-but-better form lead on the same yardstick.

---

## 5. Daily server-channel monitor

A scheduled task reads the dataset each morning and flags if the server/CAPI channel goes silent again (the failure that went unnoticed from 18 Feb). Checks `server_last_fired_time` staleness and whether custom conversions are firing. (Being set up alongside this runbook.)

---

## 6. Verification / QA checklist (run after go-live)

- `ads_get_dataset_quality` now returns a **crm/offline/server** channel (not just `web`).
- `server_last_fired_time` is within the last 24h; EMQ present on `lead_id` / `em` / `ph`.
- Custom conversions show `last_fired_time` ≠ null.
- Fire a **test lead** → confirm it appears in Events Manager **Test Events**.
- Only switch ad-set optimisation after the chosen event has sufficient weekly volume per ad set.

---

## 7. Compliance guardrail (SetIndiaBiz regulated services)

Any new creative for WhatsApp/Call/LP ads must keep claims accurate and defensible under the **Companies Act 2013**, **LLP Act 2008**, and **CGST Act 2017** — no false guarantees, no fabricated timelines, no misrepresentation of government fees.

---

*Data sources: Meta Ads connector — account 152154124583473, dataset 1242417817083521 (datasets, dataset_details, dataset_quality, customconversions, ad_entities, ad_account_pages). Zoho CRM connector — Leads picklists (getFields) and Deals stages (COQL). Mappings use live values pulled 27 Jun 2026.*
