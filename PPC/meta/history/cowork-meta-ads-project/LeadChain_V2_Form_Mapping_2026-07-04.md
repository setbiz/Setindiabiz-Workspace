# LeadChain Field Mapping — V2 Instant Forms
**Date:** 4 Jul 2026 · **For:** manual mapping by Sanjeev · **Applies to:** the 4 new forms created today — **Incorporation V2** (12:11), **Virtual CFO V2** (12:22), **DPIIT V2** (12:29), **Trademark V2** (14:00).

## ⚠️ Why this is urgent (verified 4 Jul)
Zoho received 9 `PPC Meta Insta` leads today — **all from OLD forms** (5× "C1 | Company+LLP | Higher Intent | v1", 4× "CCFS"). Meta shows **6 V2-form leads (5 DPIIT V2 + 1 Incorporation V2) that never reached Zoho** — LeadChain chains are form-scoped and no chain covers the V2 forms yet. Until mapped, every V2 lead is invisible to the tele-team → speed-to-lead (our #1 loss driver) is zero on these. DPIIT campaign leads have stopped arriving in CRM entirely.

## The canonical mapping (28 Jun 2026 standard — replicate EXACTLY per chain)

| # | LeadChain source field (Facebook) | → Zoho Leads field | Notes |
|---|---|---|---|
| 1 | Lead Id | LeadChain Social Lead ID (`leadchain0__Social_Lead_ID`) | Dedup + CAPI match key — never skip |
| 2 | Full name | Last Name (`Last_Name`) | |
| 3 | Email | Email | CAPI match key |
| 4 | Phone number | Phone | CAPI match key |
| 5 | City | City | If asked on the form |
| 6 | Qualifying question (the single V2 question) | Description | Prefix with question label so answers stay readable |
| 7 | Campaign Name | `Meta_Campaign` | |
| 8 | Adset Name | `Meta_Ad_Set` | Feeds per-ad-set cost/valid KPIs (day-14 gates) |
| 9 | Form Name | `Meta_Lead_Form` | Will read "DPIIT V2" etc. — the V2 cohort marker |
| 10 | Advert Name | `Meta_Ad_Name` | |
| 11 | Advert Id | `Meta_Ad_ID` | |
| 12 | Platform | `Meta_Ad_Type` | Holds `fb`/`ig` since 28 Jun re-map |
| 13 | *(static value)* | Lead Source = **`PPC Meta Insta`** | Exact string. NOT "Meta Ads" / "PPC Insta" / "SEO - Meta" — those are excluded from all paid-Meta reporting |

## Chain checklist (one chain per form, create — don't edit existing ones)

- [ ] **DPIIT V2** → chain "FB DPIIT V2" — 5 leads already waiting
- [ ] **Incorporation V2** → chain "FB Incorporation V2" — 1 lead waiting
- [ ] **Virtual CFO V2** → chain "FB CFO V2"
- [ ] **Trademark V2** → chain "FB TM V2" (campaign paused; map now so relaunch is safe)

Per chain: all 13 rows above → save → chain **Active** → send/await one test lead → verify (below). The 7 existing chains stay untouched (the 25 Jun lesson: chain re-maps silently drop rows). Old chains can be retired only after their form is deactivated in Meta AND the V2 chain has verified leads. STANDARD plan quota is 2,000 synced/mo — 8+ active chains is fine, volume is the cap.

## Verification (after each chain — I can run this)

```sql
SELECT id, Last_Name, Lead_Source, Meta_Campaign, Meta_Ad_Set, Meta_Lead_Form, Meta_Ad_Type, leadchain0__Social_Lead_ID
FROM Leads
WHERE ((Meta_Lead_Form like '%V2%') and (Created_Time >= '2026-07-04T00:00:00+05:30'))
LIMIT 50
```

Pass = all six Meta_* fields non-null, Lead_Source = `PPC Meta Insta`, Social_Lead_ID present. Screenshot the chain before/after per change discipline.

## Recovering the 6 stranded leads
LeadChain only syncs forward — leads submitted before the chain exists won't backfill automatically. Same route as the 28 Jun recovery: LeadChain "Download Leads" (or Meta per-form CSV export — UTF-16/tab-delimited; strip `l:` from lead id, `p:` from phone, `ag:` from ad id), then import matched on `leadchain0__Social_Lead_ID`. **These 6 are aging right now — recover them today, don't wait for the chains.** I can do the import with your approval once you've downloaded the CSVs (or straight after mapping, via the LeadChain export).
