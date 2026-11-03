# SetIndiaBiz — Zoho Admin Guide: Attribution Mapping + Workflows
**Date:** 27 Jun 2026 · **Prereq:** the 26 fields from `SetIndiaBiz_Field_Creation_Log_2026-06-27.md` already exist · **Audience:** Zoho CRM admin

> Goal: make the new attribution fields actually populate. **Part 1** carries Lead attribution onto the Deal and stamps first-touch on the Account at conversion. **Part 2** finishes the Account first-touch (date + Meta flag). **Part 3** back-fills attribution onto recurring "job" deals that are created straight from the Account (no lead). Paths verified against Zoho's current help docs, Jun 2026.

---

## 0. Before you start
- Log in as an **Administrator** (or a profile with **Manage Automation** + **Customize Zoho CRM** + **Convert Leads**).
- Picklist/text fields only map to the **same type and length** (all 26 fields were built to match — e.g. text 255 ↔ 255, the `Meta Ad Type` picklists share the same 6 values).
- ⚠️ **Mass Convert does NOT apply custom field mapping.** Conversion mapping fires on **single convert, API convert, and workflow-triggered convert** only. If your team uses **Actions → Mass Convert**, the Deal mirror fields stay blank — Part 3's inheritance function is the backstop for that, but prefer single/workflow conversion for Meta leads.

---

## Part 1 — Lead Conversion Mapping (Lead → Deal + Lead → Account)

**Navigate:**
1. **Setup** (gear icon, top-right) → **Customization** → **Modules and Fields**.
2. In the list of modules, click **Leads**.
3. Click the **Module Settings icon** (the **⋯ / gear** on the Leads module tile) → **Lead Conversion Mapping**.
4. You're on the **Map Fields for Leads Conversion** page. Left column = **Lead Fields**; to its right are dropdowns for **Accounts**, **Contacts**, **Deals**. (Leave the **Layout** selector on **Standard** unless you use multiple Lead layouts.)

**Set these rows** (for each Lead field, pick the Account and Deal targets from the dropdowns; leave Contacts as-is):

| Lead field (label) | → Accounts | → Deals |
|---|---|---|
| Meta Campaign | First Touch Meta Campaign | Meta Campaign |
| Meta Ad Set | — | Meta Ad Set |
| Meta Lead Form | — | Meta Lead Form |
| Meta Ad Name | — | Meta Ad Name |
| Meta Ad Type | First Touch Meta Ad Type | Meta Ad Type |
| Lead Source | First Touch Lead Source | Lead Source |
| Social Lead ID *(leadchain0__Social_Lead_ID)* | — | Social Lead ID |
| Source URL | — | Source URL |
| FB Click ID | — | FB Click ID |
| CTWA Click ID | — | CTWA Click ID |

5. Click **Save**.

**What this does & the write-once guarantee:** on conversion, Lead values flow to the new Deal (full attribution) and to the Account's First-Touch fields. When a lead is merged into an **existing** Account, Zoho does **not** overwrite that Account's existing field values — so First-Touch is effectively **write-once** (it sticks to the first lead that created the account). `First Touch Date` and `Meta Sourced` can't be mapped here (a datetime won't map to a date, and there's no source boolean on the Lead) — Part 2 handles those.

---

## Part 2 — Workflow 1: finish the Account first-touch (date + Meta flag)

### 2a. Create the function
Create a **Deluge** function — either standalone (**Setup → Developer Space → Functions → + New Function**; some editions label it *Developer Hub*) or, easier, **inline from the workflow action in 2b** (*Function → + New Function → Write your own*). Name it `Stamp_Account_FirstTouch`, add one argument **`accId`** (you'll map it to `${Accounts.Account Id}` in 2b), and paste:

```deluge
acc = zoho.crm.getRecordById("Accounts", accId.toLong());
upd = Map();
// First touch date = the day the account was created (write-once)
if(acc.get("First_Touch_Date") == null)
{
	upd.put("First_Touch_Date", zoho.currentdate);
}
// Flag Meta-acquired accounts
src = ifnull(acc.get("First_Touch_Lead_Source"),"");
if(src.startsWith("PPC Meta") || src.startsWith("PPC Insta"))
{
	upd.put("Meta_Sourced", true);
}
if(!upd.isEmpty())
{
	updResp = zoho.crm.updateRecord("Accounts", accId.toLong(), upd);
	info updResp;
}
```

### 2b. Create the workflow rule
**Setup → Automation → Workflow Rules → + Create Rule**.
1. **Module:** Accounts → **Next**.
2. **When:** *On a record action* → check **Create**. (Optionally also **Edit** → *when First Touch Lead Source is modified*, to catch back-filled accounts.) → **Next**.
3. **Condition:** *Records matching certain conditions* → `First Touch Lead Source` **is not empty** → **Next**.
4. **Instant Actions** → **Function** → choose **Stamp_Account_FirstTouch** → in the argument mapping, set **accId = Account Id** (merge field `${Accounts.Account Id}`) → **Save**.
5. **Save** the rule.

---

## Part 3 — Workflow 2: Account → Deal inheritance (recurring job-deals)

This is the LTV fix: when a Deal is created **without** lead attribution (the ACR / annual-return / GST job-deals spun up from the Account), copy the Account's first-touch onto the Deal.

### 3a. Create the function
Create a **Deluge** function (standalone via **Setup → Developer Space → Functions**, or inline from the workflow action in 3b). Name it `Inherit_Deal_Attribution`, add one argument **`dealId`** (map to `${Deals.Deal Id}` in 3b), and paste:

```deluge
deal = zoho.crm.getRecordById("Deals", dealId.toLong());
accObj = deal.get("Account_Name");
if(accObj != null)
{
	accId = accObj.get("id");
	acc = zoho.crm.getRecordById("Accounts", accId.toLong());
	upd = Map();
	if(deal.get("Meta_Campaign") == null && acc.get("First_Touch_Meta_Campaign") != null)
	{
		upd.put("Meta_Campaign", acc.get("First_Touch_Meta_Campaign"));
	}
	if(deal.get("Meta_Ad_Type") == null && acc.get("First_Touch_Meta_Ad_Type") != null)
	{
		upd.put("Meta_Ad_Type", acc.get("First_Touch_Meta_Ad_Type"));
	}
	if(deal.get("First_Touch_Source") == null && acc.get("First_Touch_Lead_Source") != null)
	{
		upd.put("First_Touch_Source", acc.get("First_Touch_Lead_Source"));
	}
	if(!upd.isEmpty())
	{
		// attribution came from the parent account, not the originating lead
		upd.put("Attribution_Confidence", "Inherited (account)");
		zoho.crm.updateRecord("Deals", dealId.toLong(), upd);
	}
	else if(deal.get("Meta_Campaign") != null && deal.get("Attribution_Confidence") == null)
	{
		// deal already has its own (lead-converted) attribution
		mp = Map();
		mp.put("Attribution_Confidence", "Direct (lead-linked)");
		zoho.crm.updateRecord("Deals", dealId.toLong(), mp);
	}
}
```

### 3b. Create the workflow rule
**Setup → Automation → Workflow Rules → + Create Rule**.
1. **Module:** Deals → **Next**.
2. **When:** *On a record action* → check **Create** only (not Edit — prevents loops) → **Next**.
3. **Condition:** *All Deals* (or restrict to `Account Name` is not empty) → **Next**.
4. **Instant Actions** → **Function** → **Inherit_Deal_Attribution** → map **dealId = Deal Id** (`${Deals.Deal Id}`) → **Save**.
5. **Save** the rule.

---

## Part 4 — Test & verify (10 minutes)
1. **Lead path:** take one `PPC Meta Insta` test lead (has `Meta Campaign`), **Convert** it (tick *Create a new Deal*). Open the new Deal → `Meta Campaign`, `Meta Ad Type`, `Social Lead ID`, `Attribution Confidence = Direct (lead-linked)` should be filled. Open the Account → `First Touch Meta Campaign`, `First Touch Lead Source`, `First Touch Date`, `Meta Sourced = ✓`.
2. **Job-deal path:** on that same Account, create a new Deal manually (no lead). On save, the function should copy `Meta Campaign` / `Meta Ad Type` / `First Touch Source` and set `Attribution Confidence = Inherited (account)`.
3. **Spot-check via the connector:** `SELECT Deal_Name, Meta_Campaign, Meta_Ad_Type, First_Touch_Source, Attribution_Confidence FROM Deals WHERE Created_Time > [today] ORDER BY Created_Time desc` — non-blank rows confirm it's live.

---

## Caveats & gotchas
- **Mass Convert** bypasses Part 1 mapping (Zoho limitation). Convert Meta leads singly or via a conversion workflow; Part 3 cushions job-deals.
- **Picklist parity:** mapping needs identical picklist types; the mirrors match today. If you later add a `Lead_Source` value, add it to `First Touch Source` / `First Touch Lead Source` too, or it won't map.
- **No loops:** Workflow 2 triggers on **Create** only; the function's `updateRecord` won't re-fire it.
- **Layouts:** if Leads/Deals use multiple page layouts, repeat the Part 1 mapping per layout (the mapping screen has a layout selector).
- **Backfill (separate task):** this wires *new* records. Historical Meta leads/accounts need a one-time backfill (`Meta_Ad_Type` from campaign naming; `First_Touch_*` on existing Meta accounts) — I can script that on your approval.
- **`Lead_Channel` on Deals** still defaults to "SEO"; widen its picklist or retire it in favour of `Lead_Source` separately.

## Compliance
Configuration only — no ad spend, campaign state, payments, or customer-record content are altered by these rules. Any ad creative referenced downstream must remain accurate and defensible under the **Companies Act 2013**, **LLP Act 2008**, and **CGST Act 2017**.

---
*Sources: Zoho CRM Help — “Converting Leads / Map Fields” (help.zoho.com) and “Lead Conversion Mapping” tips (zoho.com/crm), confirmed 27 Jun 2026; Deluge `zoho.crm.updateRecord` / `getRecordById` reference.*
