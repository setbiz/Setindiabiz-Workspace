# Setindiabiz — Lead Source Attribution System
### Implementation Note & Runbook
*Prepared as context for a Claude Cowork scheduled-task project. Covers what was built, the exact CRM configuration, the deployed function, the operational patterns used, and the constraints to respect.*

---

## 1. Purpose & Summary

We rebuilt Lead Source attribution in the **Setindiabiz Zoho CRM** (org: `setindiabiz`) so that every lead is attributed to its **true acquisition source** — paid ads, organic search, AI assistants, social, referral, or a manual channel — instead of the inconsistent 15-year legacy labels that had accumulated.

The system has four parts, all now **live**:

1. **A prefixed Lead Source taxonomy** (38 values) mirrored across Leads, Deals, and Contacts.
2. **A cross-module migration** folding ~28 legacy labels into the new taxonomy.
3. **A real-time workflow** (Deluge function) that classifies each lead from its URL / referrer / Meta / UTM fields on create and edit.
4. **Historical corrections** applied via the API for two edge cases the migration couldn't resolve (Meta Facebook-vs-Instagram, and chat leads masking real sources).

---

## 2. Final Lead Source Taxonomy (38 picklist values)

Every value carries a **prefix that is the channel roll-up** (filter "starts with `SEO`" for all organic search, etc.).

| Prefix | Meaning | Values |
|---|---|---|
| **Advt** | Paid advertising | Advt - Email Campaign · Advt - Facebook · Advt - Google · Advt - Instagram · Advt - LinkedIn · Advt - Microsoft · Advt - Reddit · Advt - Twitter (X) |
| **AI** | LLM / AI-assistant referrals | AI - ChatGPT · AI - Claude · AI - Gemini · AI - Other · AI - Perplexity |
| **SEO** | Organic search + owned channels | SEO - Bing · SEO - Email · SEO - Google · SEO - Other · SEO - Yahoo · SEO - YouTube · SEO - Zoho Booking |
| **Social** | Organic social | Social - Facebook · Social - Instagram · Social - LinkedIn · Social - Quora · Social - Twitter (X) · Social - WhatsApp |
| **Referral** | Inbound referral | Referral - Clients · Referral - Employee · Referral - Partner · Referral - Web |
| **Self** | Manual / offline / support | Self - B2B Meeting · Self - Cold Call · Self - IVR Call · Self - Support · Self - Trade Fair · Self - Walk In · Self - Web Chat |
| **Direct** | No referrer / typed URL | Direct |

**Manual / integration-owned values** (never overwritten by the workflow): all `Self - *`, `Referral - Clients`, `Referral - Partner`, `Referral - Employee`, `SEO - Zoho Booking`. `Referral - Web` **is** auto-managed (it's the "unrecognised external referrer" bucket).

The picklists on **Leads, Deals, and Contacts are identical/mirrored**. **Accounts** has a Lead Source field but it is entirely null (populated only at conversion; not migrated).

---

## 3. Zoho CRM Field Reference (exact API names)

These are the signal fields the classifier reads. **Note the case and type quirks — they matter.**

| Field label | API name | Type | Notes |
|---|---|---|---|
| Source URL | `Source_Url` | text | **NOT `Source_URL`.** Case matters in Deluge `lead.get()`. |
| First Page Visited | `First_Visited_URL` | website | Landing/entry URL; holds UTM + click-IDs |
| Referrer | `Referrer` | website | Previous-page domain |
| Lead Source | `Lead_Source` | picklist | The target field |
| Meta Ad Type | `Meta_Ad_Type` | picklist | **fb / ig** (Meta `site_source_name`); the FB-vs-IG signal for lead-form leads |
| Meta Ad ID | `Meta_Ad_ID` | text | Present ⇒ Meta lead-form lead |
| Meta Campaign / Ad Set / Ad Name / Lead Form | `Meta_Campaign`, `Meta_Ad_Set`, `Meta_Ad_Name`, `Meta_Lead_Form` | text | Descriptive Meta fields |
| FB Click ID | `FB_Click_ID` | text | Meta paid click id (dedicated field) |
| CTWA Click ID | `CTWA_Click_ID` | text | Click-to-WhatsApp ad click id |
| UTM Source / Medium / Campaign / Content / Term | `UTM_Source`, `UTM_Medium`, `UTM_Campaign`, `UTM_Content`, `UTM_Term` | text | Dedicated UTM fields (folded into the classifier's search text) |
| Number Of Chats | `Number_Of_Chats` | integer | SalesIQ chat count — **unreliable** (can be null on chat leads); use `Lead_Source = "Chat"` as the chat marker instead |
| Lead Channel | `Lead_Channel` | picklist | SalesIQ channel field |

---

## 4. The Live Workflow Rule

- **Module:** Leads
- **Rule name:** Auto-set Lead Source from URL (rule id `1123581000914152864`)
- **URL:** `https://crm.zoho.com/crm/setindiabiz/settings/workflow-rules/1123581000914152864`
- **Trigger:** **Create** and **Edit** (Edit fires when Source URL / First Page Visited / Referrer are modified)
- **Condition (fires if ANY are true):**
  1. Source URL is not empty
  2. First Page Visited is not empty
  3. Referrer is not empty
  4. Meta Ad Type is not empty
  5. UTM Source is not empty
  6. **Lead Source is Chat** ← lets null-URL SalesIQ chat leads fire the rule
- **Instant action:** Function (Deluge) `automation.autoClassifyLeadSource(String leadId)`, argument `leadId` mapped to **Leads › Lead Id**
- **Status:** Active

The function is **idempotent** (writes only when the derived value differs from the current one), so it cannot loop on its own edit.

---

## 5. Classification Logic (precedence — first match wins)

Signals from the landing URL (Source URL + First Page Visited + dedicated UTM fields) are the "urlText"; the referrer domain is "refText"; both combined is "allText".

0. **Meta lead-form platform** (`Meta_Ad_Type`): `ig` → Advt - Instagram · `fb` → Advt - Facebook · `an`/`msg` → Advt - Facebook
1. **Paid click-IDs** (in urlText): `gclid`/`gbraid`/`wbraid`/`gad_source` → Advt - Google · `msclkid` → Advt - Microsoft · `li_fat_id` → Advt - LinkedIn · `rdt_cid` → Advt - Reddit · `twclid` → Advt - Twitter (X)
2. **Paid Meta via URL UTM** (`utm_medium=paid` + `utm_source=ig/fb/…`) → Advt - Instagram / Advt - Facebook
3. **Email** (`utm_medium=email`, or `utm_source=newsletter/zeptomail/zohocampaigns`) → Advt - Email Campaign
4. **AI** (referrer or utm_source): chatgpt/openai → AI - ChatGPT · perplexity → AI - Perplexity · gemini/bard → AI - Gemini · claude/anthropic → AI - Claude · copilot/deepseek/grok/meta.ai/you.com/poe/mistral/phind → AI - Other. *(Checked before search because gemini/copilot contain "google"/"bing".)*
5. **Organic search** (referrer): google → SEO - Google · bing → SEO - Bing · yahoo → SEO - Yahoo · youtube → SEO - YouTube · duckduckgo/ecosia/yandex/baidu/brave/startpage → SEO - Other
6. **Organic social** (referrer): instagram → Social - Instagram · facebook / `fbclid` → Social - Facebook · linkedin/lnkd.in → Social - LinkedIn · quora → Social - Quora · twitter/x/t.co → Social - Twitter (X) · whatsapp/wa.me → Social - WhatsApp
7. **Meta click-ID field fallback** (`FB_Click_ID` / `CTWA_Click_ID` / `Meta_Ad_ID` present, placement unknown) → Advt - Facebook
8. **Fallback:** external referrer (not setindiabiz.com) → Referral - Web · else if `Lead_Source = "Chat"` → Self - Web Chat · else → Direct

**Guard (applied before writing):** if the current value starts with `Self -` OR is `Referral - Clients/Partner/Employee` OR `SEO - Zoho Booking`, do not overwrite.

---

## 6. Special Handling (the two tricky cases)

### 6a. Meta lead-form leads — Facebook vs Instagram
Meta Instant-Form / lead-gen leads submit **on** Facebook/Instagram, so they carry **no URL/referrer**. The platform is in **`Meta_Ad_Type`** (`fb`/`ig`), populated on 100% of them by the lead-ads (leadchain) integration. The integration historically stamped **every** Meta lead as `Advt - Facebook` regardless of placement — which mislabeled all Instagram leads. The workflow now reads `Meta_Ad_Type` first and splits correctly.
*(If Meta ever serves Audience Network / Messenger placements — `an`/`msg` — they currently fold into `Advt - Facebook`; split out later if those channels start running.)*

### 6b. SalesIQ chat leads — attribute to source, fall back to chat
SalesIQ pushes leads with `Lead_Source = "Chat"` (a value not in the picklist). A chat is the **conversion action, not the source** — the visitor may have arrived from a paid ad or organic search and *then* opened a chat, with the `gclid`/`utm`/referrer captured on the lead. So the rule **classifies chat leads by their real acquisition source first**, and only lands them in `Self - Web Chat` when there is genuinely no source. `Number_Of_Chats > 0` remains available for reporting "chat-assisted" volume independent of source.

### 6c. SalesIQ integration (left as-is on purpose)
SalesIQ → CRM config (`salesiq.zoho.com/wwwsetindiabizcom/settings/integrations/zohocrm/config`) maps its **"Lead Source" field → CRM "Lead Source"**, emitting the system value **"Chat"**. This is a field-to-field mapping with no constant-value option, so it was **not changed** — "Chat" is a clean, reliable marker the CRM workflow keys off to normalize.

---

## 7. Data Migration (legacy → new)

Applied via **Zoho Mass Update** across Leads, Deals, Contacts (one pass per target value, filtering `Lead Source is one of […]`). Legacy labels were record-level values from old imports/tools — many not in the current picklist, but Mass Update filters on the record value so they were still found.

| New value | Legacy labels folded in |
|---|---|
| SEO - Google | Google Search |
| Advt - Google | Google AdWords, Google Adwords |
| Advt - Facebook | Facebook Ads |
| Advt - Email Campaign | Email Marketing, Sales Mail Alias |
| Social - Facebook | Facebook |
| Social - Instagram | Instagram |
| Social - WhatsApp | Whats App, WhatsApp - SETINDIABIZ PRIVATE LIMITED, WhatsApp - SETINDIABIZ, WATI |
| Self - IVR Call | IVR Call |
| Self - Cold Call | Bigin Calling, MCA Company, GST Data, Direct Call |
| Referral - Clients | Client Referral |
| Self - Web Chat | Chat *(now handled by the workflow going forward)* |
| Self - Support | ZohoDesk, Desk |
| SEO - Zoho Booking | Zoho Bookings, Zoho Webinar |
| Referral - Web | kpsconsultants.com, tm-logo.com, From Leadsquared |
| Direct | WebSite Visit, Query from website, Contact US from website, Direct Organic |
| *(left null)* | all blank records |

---

## 8. Historical Corrections (applied via the API, workflow suppressed)

### 8a. Meta Facebook / Instagram split
The migration had lumped all Meta leads into `Advt - Facebook`. Corrected from `Meta_Ad_Type`:
- **70** `ig` leads → `Advt - Instagram`
- **5** blank `fb` leads → `Advt - Facebook`
- **Final state:** 141 fb → Advt - Facebook · 70 ig → Advt - Instagram (zero mislabels)

### 8b. Chat leads masking real sources
**37** `Self - Web Chat` leads that actually arrived from a trackable source were reclassified:
- 23 → SEO - Google · 10 → SEO - Yahoo · 2 → AI - Perplexity · 1 → SEO - Other (DuckDuckGo) · 1 → Social - LinkedIn
- The ~3,212 genuinely source-less chats correctly remain `Self - Web Chat`.
- (No paid-ad chats existed historically; the going-forward rule will catch them via `gclid` in `First_Visited_URL`.)

---

## 9. Connector Operations Reference (patterns used — reuse these in the scheduled task)

**Read distributions / counts (COQL):**
```
SELECT Lead_Source, COUNT(id) FROM Leads WHERE Created_Time > '2015-01-01T00:00:00+05:30' GROUP BY Lead_Source
SELECT Meta_Ad_Type, Lead_Source, COUNT(id) FROM Leads WHERE Meta_Ad_ID is not null GROUP BY Meta_Ad_Type, Lead_Source
SELECT id FROM Leads WHERE Meta_Ad_Type = 'ig' LIMIT 200
```
COQL can filter/group and select **text/picklist/id** fields, but **cannot select the website-type fields** (`First_Visited_URL`, `Referrer`) — and `Source_Url` returns "unsupported column".

**Find records by referrer / value (searchRecords):** returns website fields; supports `starts_with` on `Referrer`:
```
((Lead_Source:equals:Self - Web Chat)and(Referrer:starts_with:https://www.google))
(Referrer:starts_with:https://www.setindiabiz.com)
(Source_URL:contains:...)   ← NOT supported (Source_Url is not search-indexed)
```
`Referrer` supports `starts_with` but **not** `contains`. Combine with `and`/`or` in nested parentheses.

**Read specific records (getRecords):** by `ids`, with an explicit `fields` list — returns website fields fine.

**Bulk update WITHOUT triggering workflows (updateRecords):** each record `{id, Lead_Source}`, up to 100 per call, and critically `"trigger": []` to suppress the workflow (essential for corrections so the rule doesn't re-fire / clobber).

**Single update WITH the workflow (updateRecord):** `"trigger": ["workflow"]` — used for live-testing that the rule fires and classifies correctly.

**Search-index lag:** searchRecords criteria run against a search index that lags **~1–2 minutes** behind writes. Immediately after a bulk update, a criteria filter may still match records under their *old* value even though the returned field values are already correct. Verify by the returned field value, or wait a couple of minutes.

---

## 10. Key Gotchas & Constraints (read before automating anything)

- **`Source_Url` not `Source_URL`.** Wrong case ⇒ Deluge reads null and the field is silently ignored.
- **Website-type fields** (`First_Visited_URL`, `Referrer`) are **not COQL-selectable** and **not searchable with `contains`** (only `starts_with` on `Referrer`). Plan queries accordingly.
- **Deluge function editor is strict:** it rejects raw statements and inline `{...}` map/list literals. Code **must** be wrapped in a signature: `void automation.name(String arg) { … }`.
- **`trigger: []`** on API updates suppresses workflows — always use it for data corrections; use `["workflow"]` only when you *want* the rule to fire (e.g., testing).
- **Click-IDs normally land in `First_Visited_URL`** for fresh ad clicks (caught). In rare historical internal-navigation cases the `gclid` sits only in the **referrer** and is not caught — negligible, not worth special-casing.
- **`Meta_Ad_Type`** only contained `fb`/`ig` in the data (no Audience Network / Messenger).
- **`Number_Of_Chats` is unreliable** as a chat marker (null even on real chat leads). Use `Lead_Source = "Chat"`.
- **Meta lead-form leads have null URL/referrer** — their only signal is the `Meta_*` fields.
- **Deals/Contacts inherit Lead Source at conversion** and do **not** carry `Meta_Ad_Type` / URL fields, so they can't be re-derived the same way — only value-remapped or inherited.
- **Do NOT do a blanket re-derivation of historical website leads.** A dry-run proved it degrades data: internal-referrer leads (~61) currently sensibly labelled would flip to `Direct`, and some Google-Ads-in-referrer leads would be mis-set. The migration + live rule already handle the bulk correctly.

---

## 11. Suggested Scheduled Task (for the Cowork project)

The live workflow classifies in real time on create/edit. A scheduled task should act as a **safety net + QA sweep**, not a blanket re-run. Recommended scope and cadence:

**A. Normalize stragglers (daily).** Find leads the workflow may have missed — created/modified in the last ~2 days with a signal but a blank or un-normalized source:
- `Lead_Source = "Chat"` still present (workflow didn't fire) → re-derive / set `Self - Web Chat`.
- `Lead_Source` blank **and** (`Meta_Ad_Id` not null **or** `Referrer`/`First_Visited_URL` populated) → re-derive.
- Bulk imports bypass workflows — this catches them.

**B. Meta placement integrity (daily/weekly).** Confirm the integration hasn't drifted:
- `Meta_Ad_Type = 'ig'` **and** `Lead_Source = 'Advt - Facebook'` → should be `Advt - Instagram`. Fix any found.

**C. Distribution & anomaly report (weekly).** `GROUP BY Lead_Source` over the last 7 days; flag spikes in `Direct`/`Self - Web Chat` (possible tracking breakage) or any non-taxonomy value (e.g. a new stray SalesIQ/import label) appearing.

**Safety rules for the scheduled task:**
- Reuse the **exact classification logic** in §5 so the batch and the live rule never disagree.
- Respect the **guards** in §5 — never overwrite `Self -*`, the three manual `Referral -*`, or `SEO - Zoho Booking`.
- Use `updateRecords` with **`trigger: []`** for corrections.
- For any batch over a few hundred records, **dry-run first** (report the proposed old → new changes) before writing.
- Scope by **`Modified_Time`** windows so each run is bounded and re-runnable (don't re-scan the whole module).

---

## 12. The Final Deluge Function (deployed — complete)

This is the exact function running in the workflow. The scheduled task should embed the same logic (adapting the write to whichever records it selects).

```javascript
void automation.autoClassifyLeadSource(String leadId)
{
	lead = zoho.crm.getRecordById("Leads", leadId.toLong());
	srcUrl = ifnull(lead.get("Source_Url"), "").toString().toLowerCase();
	firstUrl = ifnull(lead.get("First_Visited_URL"), "").toString().toLowerCase();
	refText = ifnull(lead.get("Referrer"), "").toString().toLowerCase();
	current = ifnull(lead.get("Lead_Source"), "").toString();
	metaAdType = ifnull(lead.get("Meta_Ad_Type"), "").toString().toLowerCase();
	metaAdId = ifnull(lead.get("Meta_Ad_ID"), "").toString();
	fbClickId = ifnull(lead.get("FB_Click_ID"), "").toString();
	ctwaClickId = ifnull(lead.get("CTWA_Click_ID"), "").toString();
	utmSource = ifnull(lead.get("UTM_Source"), "").toString().toLowerCase();
	utmMedium = ifnull(lead.get("UTM_Medium"), "").toString().toLowerCase();
	utmCampaign = ifnull(lead.get("UTM_Campaign"), "").toString().toLowerCase();
	urlText = srcUrl + " " + firstUrl + " utm_source=" + utmSource + " utm_medium=" + utmMedium + " utm_campaign=" + utmCampaign;
	allText = urlText + " " + refText;
	newSource = "";
	// 0) META LEAD-FORM (no URL/referrer) — platform from Meta_Ad_Type
	if(metaAdType == "ig")
	{
		newSource = "Advt - Instagram";
	}
	else if(metaAdType == "fb")
	{
		newSource = "Advt - Facebook";
	}
	else if(metaAdType == "an" || metaAdType == "msg")
	{
		newSource = "Advt - Facebook";
	}
	// 1) PAID click-IDs
	else if(urlText.contains("gclid=") || urlText.contains("gbraid=") || urlText.contains("wbraid=") || urlText.contains("gad_source="))
	{
		newSource = "Advt - Google";
	}
	else if(urlText.contains("msclkid="))
	{
		newSource = "Advt - Microsoft";
	}
	else if(urlText.contains("li_fat_id="))
	{
		newSource = "Advt - LinkedIn";
	}
	else if(urlText.contains("rdt_cid="))
	{
		newSource = "Advt - Reddit";
	}
	else if(urlText.contains("twclid="))
	{
		newSource = "Advt - Twitter (X)";
	}
	// 2) PAID META via URL utm
	else if((urlText.contains("utm_medium=paid") || urlText.contains("utm_medium=paid_social") || urlText.contains("utm_medium=cpc")) && (urlText.contains("utm_source=ig") || urlText.contains("utm_source=fb") || urlText.contains("utm_source=instagram") || urlText.contains("utm_source=facebook") || urlText.contains("utm_source=meta")))
	{
		if(refText.contains("instagram.com") || urlText.contains("utm_source=ig") || urlText.contains("utm_source=instagram"))
		{
			newSource = "Advt - Instagram";
		}
		else
		{
			newSource = "Advt - Facebook";
		}
	}
	// 3) EMAIL
	else if(urlText.contains("utm_medium=email") || urlText.contains("utm_source=newsletter") || urlText.contains("utm_source=zeptomail") || urlText.contains("utm_source=zohocampaigns"))
	{
		newSource = "Advt - Email Campaign";
	}
	// 4) AI
	else if(allText.contains("chatgpt.com") || allText.contains("chat.openai.com") || allText.contains("openai.com") || allText.contains("utm_source=chatgpt"))
	{
		newSource = "AI - ChatGPT";
	}
	else if(allText.contains("perplexity.ai"))
	{
		newSource = "AI - Perplexity";
	}
	else if(allText.contains("gemini.google.com") || allText.contains("bard.google.com"))
	{
		newSource = "AI - Gemini";
	}
	else if(allText.contains("claude.ai") || allText.contains("anthropic.com"))
	{
		newSource = "AI - Claude";
	}
	else if(allText.contains("copilot.microsoft.com") || allText.contains("bing.com/chat") || allText.contains("deepseek") || allText.contains("grok.com") || allText.contains("//x.ai") || allText.contains("meta.ai") || allText.contains("//you.com") || allText.contains("poe.com") || allText.contains("mistral.ai") || allText.contains("phind.com"))
	{
		newSource = "AI - Other";
	}
	// 5) ORGANIC SEARCH
	else if(refText.contains("google.com") || refText.contains("google.co."))
	{
		newSource = "SEO - Google";
	}
	else if(refText.contains("bing.com"))
	{
		newSource = "SEO - Bing";
	}
	else if(refText.contains("yahoo.com") || refText.contains("search.yahoo"))
	{
		newSource = "SEO - Yahoo";
	}
	else if(refText.contains("youtube.com") || refText.contains("youtu.be"))
	{
		newSource = "SEO - YouTube";
	}
	else if(refText.contains("duckduckgo.com") || refText.contains("ecosia.org") || refText.contains("yandex.") || refText.contains("baidu.com") || refText.contains("search.brave.com") || refText.contains("startpage.com"))
	{
		newSource = "SEO - Other";
	}
	// 6) ORGANIC SOCIAL
	else if(refText.contains("instagram.com"))
	{
		newSource = "Social - Instagram";
	}
	else if(refText.contains("facebook.com") || urlText.contains("fbclid="))
	{
		newSource = "Social - Facebook";
	}
	else if(refText.contains("linkedin.com") || refText.contains("lnkd.in"))
	{
		newSource = "Social - LinkedIn";
	}
	else if(refText.contains("quora.com"))
	{
		newSource = "Social - Quora";
	}
	else if(refText.contains("twitter.com") || refText.contains("//x.com") || refText.contains("//t.co/"))
	{
		newSource = "Social - Twitter (X)";
	}
	else if(refText.contains("whatsapp.com") || refText.contains("//wa.me"))
	{
		newSource = "Social - WhatsApp";
	}
	// 7) Paid Meta via click-ID field, placement unknown -> Facebook
	else if(fbClickId != "" || ctwaClickId != "" || metaAdId != "")
	{
		newSource = "Advt - Facebook";
	}
	// 8) External referral -> Web Chat fallback -> Direct
	else if(refText != "" && !refText.contains("setindiabiz.com"))
	{
		newSource = "Referral - Web";
	}
	else if(current == "Chat")
	{
		newSource = "Self - Web Chat";
	}
	else
	{
		newSource = "Direct";
	}
	// GUARD — never overwrite manual / integration-owned values
	isProtected = false;
	if(current.startsWith("Self -"))
	{
		isProtected = true;
	}
	if(current == "Referral - Clients" || current == "Referral - Partner" || current == "Referral - Employee" || current == "SEO - Zoho Booking")
	{
		isProtected = true;
	}
	// WRITE
	if(newSource != "" && newSource != current && !isProtected)
	{
		upd = Map();
		upd.put("Lead_Source", newSource);
		updateResp = zoho.crm.updateRecord("Leads", leadId.toLong(), upd);
		info "Lead " + leadId + " : " + current + " -> " + newSource;
	}
}
```

---

## 13. Quick Reference — Detection Tokens

| Signal (in URL / referrer / field) | → Lead Source |
|---|---|
| `Meta_Ad_Type = ig` | Advt - Instagram |
| `Meta_Ad_Type = fb` | Advt - Facebook |
| `gclid=` / `gbraid=` / `wbraid=` / `gad_source=` | Advt - Google |
| `msclkid=` | Advt - Microsoft |
| `li_fat_id=` | Advt - LinkedIn |
| `rdt_cid=` | Advt - Reddit |
| `twclid=` | Advt - Twitter (X) |
| `utm_medium=paid` + `utm_source=ig/fb` | Advt - Instagram / Facebook |
| `utm_medium=email` / newsletter / zeptomail / zohocampaigns | Advt - Email Campaign |
| chatgpt.com / openai.com / `utm_source=chatgpt` | AI - ChatGPT |
| perplexity.ai | AI - Perplexity |
| gemini.google.com / bard.google.com | AI - Gemini |
| claude.ai / anthropic.com | AI - Claude |
| copilot / deepseek / grok / meta.ai / you.com / poe / mistral / phind | AI - Other |
| referrer google.com / google.co.* | SEO - Google |
| referrer bing.com | SEO - Bing |
| referrer yahoo / search.yahoo | SEO - Yahoo |
| referrer youtube.com / youtu.be | SEO - YouTube |
| referrer duckduckgo / ecosia / yandex / baidu / brave / startpage | SEO - Other |
| referrer instagram.com | Social - Instagram |
| referrer facebook.com / `fbclid=` | Social - Facebook |
| referrer linkedin.com / lnkd.in | Social - LinkedIn |
| referrer quora.com | Social - Quora |
| referrer twitter.com / x.com / t.co | Social - Twitter (X) |
| referrer whatsapp.com / wa.me | Social - WhatsApp |
| `FB_Click_ID` / `CTWA_Click_ID` / `Meta_Ad_ID` (no placement) | Advt - Facebook |
| external referrer (not setindiabiz.com), nothing else | Referral - Web |
| `Lead_Source = Chat` and no source | Self - Web Chat |
| own-domain / empty referrer, no signal | Direct |

*End of note.*