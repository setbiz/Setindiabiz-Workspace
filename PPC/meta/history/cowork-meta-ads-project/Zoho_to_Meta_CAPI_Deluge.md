# Zoho CRM → Meta Conversions API — Implementation (SetIndiaBiz)

**Status: ✅ LIVE — Lead-quality coverage expanded 28 Jun 2026**
Dataset `1242417817083521` · Ad account `152154124583473` · Page `627814417091714` · Currency INR · Business `629080835992237`

The closed loop runs in **both directions**. As of 28 Jun 2026 the Lead side sends quality signals from **all three quality fields (RM / TL / CSD) and Lead_Status**, not just RM Quality.

---

## 1. What's live

| Piece | Status |
|---|---|
| Access token in Org Variable `meta_capi_access_token` | ✅ |
| Dataset **Auto‑tracking** → SETINDIABIZ ad account | ✅ |
| Deluge sender — **two purpose‑named copies** | ✅ |
| Rule 1 — Leads → `ValidLead` / `QualifiedLead` | ✅ live (4‑field trigger) |
| Rule 2 — Deals → `QualifiedLead`/`Committed`/`Purchase` | ✅ live |
| Daily server‑channel monitor | ✅ |

> ⚠️ **Two‑copy maintenance:** Zoho associates a function per module, so the sender exists as two copies, now named by purpose:
> - **`sib_sendMetaCAP_Lead`** (display "SIB Send Meta CAP Lead") — used by **Rule 1 / Leads**.
> - **`sib_sendMetaCAPI_Deal`** (display "SIB Send Meta CAPI Deal") — used by **Rule 2 / Deals**.
>
> The body below is identical in both; only the first‑line function name differs. If you change logic, update **both** (or at least the copy whose module branch you touched).

---

## 2. Event mapping (verified against live picklist values, 28 Jun 2026)

All three quality fields (`RM_Lead_Quality`, `Mkt_Leat_Quality` = TL Quality, `CSD_Lead_Quality`) share the **same** picklist. The four "valid" tiers below were confirmed present in live data via COQL.

| Journey stage | Meta event | Zoho trigger (actual values) | Value |
|---|---|---|---|
| Valid lead | `ValidLead` | **RM Quality OR TL Quality OR CSD Quality** ∈ {Valid - RM Working, Valid - NIL RM Action, Valid - Casual RM Action, Valid - Good RM Action} **or** `Lead_Status` = "Valid Lead" | 0 |
| Progressed (lead side) | `QualifiedLead` | `Lead_Status` ∈ {Negotiation, Proposal Sent, Payment Pending} | 0 |
| Qualified (deal side) | `QualifiedLead` | Deal `Stage` ∈ {Qualified, Follow‑Up, Negotiation} | 0 |
| Committed | `Committed` | Deal `Stage` = Payment Wait | 0 |
| Won | `Purchase` | Deal `Stage` ∈ {Won, W‑SKV, W‑SPI, W‑CSD, W‑Finance, W‑Login, W‑ACR Login} | **Deal Amount (INR)** |
| Excluded | — | `Valid - Product Not Ready` (unserviceable), all Invalid/Fake/Duplicate/Still‑Evaluating tiers; Lost/Postponed/Establishing Contact statuses; Lost‑Sales/Refunded deal stages | — |

> **Why `Valid - Product Not Ready` is excluded:** it marks a real but unserviceable lead; per the KPI mapping confirmed with Sanjeev it is **not** counted as a valid lead, so it must not fire `ValidLead`.

> **Precedence in the Lead function:** Lead_Status progression is checked first (→ `QualifiedLead`), otherwise any valid quality tier or `Lead_Status = "Valid Lead"` → `ValidLead`. A lead can be quality‑valid even if later Lost — `ValidLead` reflects lead *quality*, while outcome is carried by the deal‑stage events.

**Match keys:** `lead_id` = `leadchain0__Social_Lead_ID` (lead‑form leads) **plus** SHA‑256 hashed `em`/`ph`. Deal events match on the **linked Contact's** email/phone (the LeadChain `Social_Lead_ID` is not exposed in Lead→Deal conversion mapping).

---

## 3. The deployed function (body identical in both copies)

First line is `sib_sendMetaCAP_Lead` in the Leads copy and `sib_sendMetaCAPI_Deal` in the Deals copy.

```deluge
void automation.sib_sendMetaCAP_Lead(string moduleName, string recordId)
{
	datasetId = "1242417817083521";
	apiVersion = "v21.0";
	accessToken = zoho.crm.getOrgVariable("meta_capi_access_token");
	rec = zoho.crm.getRecordById(moduleName, recordId.toLong());
	eventName = "";
	value = 0;
	actionSource = "system_generated";
	email = "";
	phone = "";
	if(moduleName == "Leads")
	{
		rmq = ifnull(rec.get("RM_Lead_Quality"),"").toString();
		tlq = ifnull(rec.get("Mkt_Leat_Quality"),"").toString();
		csdq = ifnull(rec.get("CSD_Lead_Quality"),"").toString();
		status = ifnull(rec.get("Lead_Status"),"").toString();
		validSet = {"Valid - RM Working","Valid - NIL RM Action","Valid - Casual RM Action","Valid - Good RM Action"};
		progressSet = {"Negotiation","Proposal Sent","Payment Pending"};
		if(progressSet.contains(status))
		{
			eventName = "QualifiedLead";
		}
		else if(validSet.contains(rmq) || validSet.contains(tlq) || validSet.contains(csdq) || status == "Valid Lead")
		{
			eventName = "ValidLead";
		}
		email = ifnull(rec.get("Email"),"").toString();
		phone = ifnull(rec.get("Phone"),"").toString();
		if(phone == "")
		{
			phone = ifnull(rec.get("Mobile"),"").toString();
		}
	}
	else if(moduleName == "Deals")
	{
		con = rec.get("Contact_Name");
		if(con == null)
		{
			return;
		}
		contact = zoho.crm.getRecordById("Contacts",con.get("id").toLong());
		if(ifnull(contact.get("Lead_Source"),"").toString() != "PPC Meta Insta")
		{
			return;
		}
		email = ifnull(contact.get("Email"),"").toString();
		phone = ifnull(contact.get("Phone"),"").toString();
		if(phone == "")
		{
			phone = ifnull(contact.get("Mobile"),"").toString();
		}
		stage = ifnull(rec.get("Stage"),"").toString();
		qualifiedSet = {"Qualified","Follow-Up","Negotiation"};
		committedSet = {"Payment Wait"};
		wonSet = {"Won","W-SKV","W-SPI","W-CSD","W-Finance","W-Login","W-ACR Login"};
		if(wonSet.contains(stage))
		{
			eventName = "Purchase";
			value = ifnull(rec.get("Amount"),0);
		}
		else if(committedSet.contains(stage))
		{
			eventName = "Committed";
		}
		else if(qualifiedSet.contains(stage))
		{
			eventName = "QualifiedLead";
		}
	}
	if(eventName == "")
	{
		return;
	}
	userData = Map();
	leadId = ifnull(rec.get("leadchain0__Social_Lead_ID"),"").toString();
	if(leadId != "")
	{
		userData.put("lead_id",leadId);
	}
	if(email != "")
	{
		userData.put("em",zoho.encryption.sha256(email.toLowerCase().trim()));
	}
	if(phone != "")
	{
		phNorm = phone.replaceAll("[^0-9]","");   // NB: Deluge replaceAll is REGEX — strip non-digits this way
		if(phNorm.length() == 10)
		{
			phNorm = "91" + phNorm;
		}
		userData.put("ph",zoho.encryption.sha256(phNorm));
	}
	if(userData.size() == 0)
	{
		return;
	}
	eventTime = zoho.currenttime.toString().unixEpoch() / 1000;   // unixEpoch returns ms; /1000 = unix seconds
	event = Map();
	event.put("event_name",eventName);
	event.put("event_time",eventTime);
	event.put("action_source",actionSource);
	event.put("user_data",userData);
	if(eventName == "Purchase")
	{
		cd = Map();
		cd.put("value",value);
		cd.put("currency","INR");
		event.put("custom_data",cd);
	}
	dataList = List();
	dataList.add(event);
	payload = Map();
	payload.put("data",dataList);
	endpoint = "https://graph.facebook.com/" + apiVersion + "/" + datasetId + "/events?access_token=" + accessToken;
	response = invokeurl
	[
		url : endpoint
		type : POST
		parameters : payload.toString()
		content-type : "application/json"
	];
	info "Meta CAPI [" + eventName + "] -> " + response;
}
```

**Deluge gotchas already resolved (don't re‑introduce):** no `toEpoch()` — use `<text>.unixEpoch()`; `replaceAll` is regex — use `[^0-9]`; SHA‑256 via `zoho.encryption.sha256()` (lowercase hex, Meta‑ready). Field API name for TL Quality is `Mkt_Leat_Quality` (the "Leat" typo is the real API name).

---

## 4. Workflow rules (as built)

**Rule 1 — "Meta CAPI - ValidLead" (Leads):** Record action → Edit → **fires when ANY of: RM Quality, TL Quality, CSD Quality, Lead Status is modified** (execute when *any* of the criteria are satisfied) → Condition: **Lead Source is PPC Meta Insta** → Instant action **Function `sib_sendMetaCAP_Lead`** (`moduleName="Leads"`, `recordId = Lead Id`). *(Updated 28 Jun 2026 from the previous RM‑Quality‑only trigger.)*

**Rule 2 — "Meta CAPI - Deal Stage" (Deals):** Record action → Edit → **Stage is modified to any value** → Condition: **All Deals** → Instant action **Function `sib_sendMetaCAPI_Deal`** (`moduleName="Deals"`, `recordId = Deal Id`). The function self‑gates on the linked Contact's `Lead_Source = "PPC Meta Insta"`.

Both rules are Active; both function associations survived the 28 Jun rename (verified in the rule canvas).

---

## 5. Verification

**Field/value verification (COQL, 28 Jun 2026):** all four trigger fields exist under the exact API names used; every `validSet`/`progressSet` string matches live picklist values exactly. Notable: **`Mkt_Leat_Quality` (TL Quality) is the most‑populated quality field** (~17k valid gradings) — the previous RM‑only function was missing the largest valid‑signal source.

**Original end‑to‑end test (27 Jun 2026):** `ValidLead` on a lead → Meta `events_received: 1`; `Purchase` on a Won deal → `events_received: 1` with value; dataset `server_last_fired_time` moved from 2026‑02‑18 to current.

**Re‑test PASSED (28 Jun 2026):** ran `sib_sendMetaCAP_Lead` with `moduleName = Leads`, `recordId = 1123581000888516561` (a Meta lead valid by **TL Quality only** — RM null, status Lost) → console: `Meta CAPI [ValidLead] -> {"events_received":1,"messages":[],"fbtrace_id":"A_NyDdnutHBo9qyBCG9Unbu"}`. Clean accept (zero warning messages), with GET 200 on the record and POST 200 to the events endpoint. Confirms TL Quality now drives `ValidLead` — under the old RM‑only code this lead sent nothing.

---

## 6. Monitoring & next optimisation step

- **Daily monitor** (scheduled task) checks `server_last_fired_time` + that a server/CRM channel exists; alerts if the channel goes quiet.
- After the chosen event accrues weekly volume per ad set, switch ad‑set optimisation from raw web `OFFSITE_CONVERSIONS` toward **Conversion Leads / `ValidLead`**, then **`QualifiedLead`**. Approve one variable at a time per guardrails.

---

## 7. Next phase — WhatsApp / Call / Web (not yet built)

Keep single `Lead_Source = "PPC Meta Insta"`; separate types with the **`Meta Ad Type`** picklist. The function already has the structure to add `CTWA_Click_ID` (→ `ctwa_clid`) and `FB_Click_ID` (→ `fbc`) fallbacks when those leads flow into CRM. Measure every type on the objective hierarchy (Valid% → Progressed% → Won%, cost per valid/progressed/won) in Zoho Analytics.

---

## 8. Compliance

All ad creative/claims must stay accurate and defensible under the **Companies Act 2013**, **LLP Act 2008**, and **CGST Act 2017** — no false guarantees, fabricated timelines, or misrepresentation of government fees.

---

*Data sources: Meta Ads connector (dataset 1242417817083521, account 152154124583473); Zoho CRM connector (Leads/Deals/Contacts; COQL picklist verification). Built 27 Jun 2026; lead‑quality coverage expanded and verified 28 Jun 2026.*
