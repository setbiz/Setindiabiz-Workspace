# SetIndiaBiz — Zoho ↔ Meta Lead-Quality Signal Audit
**Date:** 27 Jun 2026 · **Account:** SETINDIABIZ (152154124583473, INR) · **Dataset:** setindiabiz (1242417817083521)

---

## Verdict — NOT robust. The loop is one-directional.

Meta is **not receiving any lead-quality signal from Zoho.** The connection that exists runs only *inbound* (Meta → Zoho): leads and their ad attribution flow into the CRM correctly. The *outbound* half (Zoho → Meta), the half that would let Meta optimise for quality instead of cheap raw leads, **does not exist / is dormant.**

Today Meta optimises every ad set toward a **front-end web "Lead" pixel event** — i.e. whoever is most likely to submit a form. It has **zero visibility** into which of those leads turned out valid, qualified, or won. So it cannot "boost conversion quality"; structurally it can only chase volume.

---

## What works (inbound: Meta → Zoho)

| Signal in Zoho | Status | Evidence |
|---|---|---|
| LeadChain pulling FB/IG lead-form leads | ✅ Live | `leadchain0__Social_Lead_ID` populated on every recent lead |
| Facebook Advert Manager extension | ✅ Installed | `facebookadvertmanager__Facebook_Ad` lookup field present |
| Campaign attribution | ✅ Working | `Meta_Campaign` matches live campaign names (#IND1 BizReg, #IND3 Trademark, #IND4 CCFS, #IND5 DPIIT…) |
| Ad-set / form fields | ⚠️ Exist, fill unverified | `Meta_Ad_Set`, `Meta_Lead_Form` fields exist |
| Quality + funnel fields | ⚠️ Partial | `RM_Lead_Quality` filled ~7/15 sampled; `Lead_Status` progresses (Establishing Contact → Valid → Proposal Sent); **`Mkt_Leat_Quality`/TL Quality null on all 15** |
| Volume | ✅ Healthy | **869** `PPC Meta Insta` leads in last 30d — the largest genuine paid source |

**The quality data Meta needs already exists inside Zoho. It is simply never sent back.**

---

## What's missing / broken (outbound: Zoho → Meta) — the part that matters

1. **No offline/CRM conversion channel on the Meta dataset.** Querying the dataset for `offline`, `crm`, and `custom_attribution` channels returns **empty**. Only a `web` (browser pixel) channel exists. There is no mechanism delivering CRM outcomes to Meta.
2. **Server / Conversions API channel is dormant.** Dataset `server_last_fired_time = 2026-02-18` — ~4 months silent. The browser pixel fired yesterday, but the server side (which would carry CRM events) stopped.
3. **All custom conversions have never fired.** All 4 custom conversions (incl. the LEAD-type "Form Submission") show `last_fired_time: null`. The "Form Submission" rule is also malformed (`event = PageView AND name contains "Lead"`).
4. **Ad sets optimise on raw web conversions.** Every active ad set uses `optimization_goal = OFFSITE_CONVERSIONS` (web Lead pixel), not a quality/Conversion-Leads goal. Campaigns are `OUTCOME_LEADS`.
5. **The optimisation signal is incomplete anyway.** Web "Lead" pixel fired **395 times / 28d**, but the CRM received **869 Meta leads / 30d** → the pixel sees **under half**. Most leads come through Instant Forms that never touch the website, so they never reach the event Meta is optimising on.

**Net effect:** Meta is steering ~₹298,000/month of spend using a partial, top-of-funnel signal and no quality feedback. This is exactly the "optimise for cheap raw leads" failure mode the operator brief warns against.

---

## Why this caps conversion quality (mechanism)

Meta's delivery system optimises toward *whatever event you feed it*. Feed it a web "Lead" form-fill, and its model finds people who fill forms — not people who buy. To make Meta improve *quality*, the optimisation event must represent quality: a **Qualified / Committed / Won** signal produced downstream in Zoho and sent back, **matched to the original lead and ad**. That return path is the missing link.

---

## Fixes — priority order

1. **Build the closed loop (highest impact).** Push Zoho stage events back to Meta via **Conversions API for CRM / offline conversions**, keyed on `leadchain0__Social_Lead_ID` (Meta lead-form lead id) and/or hashed email+phone. Send graded events, e.g. `QualifiedLead` (RM Valid), `Committed`, `Won` — mapped from `RM_Lead_Quality` / `Lead_Status` / Deal Stage.
2. **Re-activate the server/CAPI channel** (silent since 18 Feb) and confirm Event Match Quality on the identifiers above.
3. **Repoint ad-set optimisation to quality** once the upstream event has enough weekly volume (Meta needs ~tens of events/week per ad set) — move from raw `OFFSITE_CONVERSIONS` toward Conversion-Leads / the Qualified event.
4. **Fix custom conversions** — correct the "Form Submission" rule and archive the misconfigured ones, or replace with CRM-driven events from step 1.
5. **Confirm ad-level attribution (the "LeadChain fix").** Verify `Meta_Ad_Set` / ad-id capture so cost-per-quality can be reported below campaign level.
6. **Backfill data hygiene** — TL Quality (`Mkt_Leat_Quality`) is empty across the board; partial quality data weakens any signal you send back.

---

## Snapshot data (last 30d unless noted)

- Meta spend (sum of active+paused campaigns): **₹298,260** · implied **~₹343 per raw Meta lead** (account-level, pre-quality).
- Largest sources: Self-Bigin 2,563 · **PPC Meta Insta 869** · SEO-Google 262 · (null) 261 · MCA 201.
- Dataset events 28d: PageView 36,832 · scroll 34,382 · form_start 4,182 · click 3,377 · form_submit 2,631 · **Lead 395**.
- Custom conversions: 4 total, **0 ever fired**.

*Data sources: Meta Ads connector — ad account 152154124583473, dataset 1242417817083521 (datasets, dataset_quality, dataset_stats, customconversions, ad_entities). Zoho CRM connector — Leads module (getFields, COQL on Lead_Source = 'PPC Meta Insta'). Account-level cost metrics per operator guardrail until ad-level attribution is confirmed.*
