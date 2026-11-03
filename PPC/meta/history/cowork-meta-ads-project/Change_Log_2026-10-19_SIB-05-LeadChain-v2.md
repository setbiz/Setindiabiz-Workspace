# Change log: 19 Oct 2026, SIB-05 FDI: new LeadChain chain for form v2

**Why:** The SIB-05 ads now use "SIB-05 India Entry Form v2". The existing chain "FB SIB-05 FDI v1" can't be repointed, because LeadChain locks the source form once a chain is saved.

## What was done
- Created a new chain **FB SIB-05 FDI v2**. It went **Active** at about 13:12 IST; Sanjeev clicked Save and Publish.
  - Source: FB account Sanjeev Kumar → SETINDIABIZ → Setindiabiz Private Limited → **SIB-05 India Entry Form v2**
  - Destination: ZohoCRM → Leads
  - Tag: FB-FDI
  - Layout: Standard
  - Assignment rule: PPC - SIB-05 India Entry - PG…
- The 15 field mappings are a copy of v1, verified on the saved view page:
  - Lead Id → Social Lead ID
  - Full name → Last Name
  - Work email → Email
  - Phone number → Phone
  - Company name → Account Name
  - "What do you want to set up…" and "When do you plan to start?" → Description
  - Static picklist value Advt → Lead Channel
  - "Where is your parent company…" → Select Country
  - Static picklist value FDI → Product Cat
  - Campaign Name → Meta Campaign
  - Form Name → Meta Lead Form
  - Advert Name → Meta Ad Name
  - Adset Name → Meta Ad Set
  - Advert Id → Meta Ad ID
  - Platform → Meta Ad Type
- **No Lead Source mapping.** This was deliberate. The editor pre-fills Lead Source ← "Meta Ads" and also Full Name ← Full name; both were removed before saving.
- **FB SIB-05 FDI v1** is unchanged and still Active (3 leads; last on 16 Oct). The chain count is now 14.

## Gotchas learned
- The source form on an existing chain is read-only, so a new form needs a new chain.
- The first Save can store the chain as a **Draft** while the editor freezes; after that, Save and Publish does nothing and shows no error. Fix: reopen the draft from the chain list in a fresh tab, re-map, then publish.
- The field-search boxes only filter when typed key by key; pasted text does not filter.
- Picklist static values (Advt, FDI) are under the dropdown's **CRM FIELDS** tab.

## Lead Source / Lead Channel flag: WITHDRAWN (13:30)
- The v1 test leads showed "Direct / SEO" only because they were testing-tool dummies with **no Platform value**. "Auto-set Lead Source from URL" sets "Direct" for them, and a later edit-time rule derives Lead Channel "SEO" from "Direct". This is the known R67 pattern.
- Real form leads in the last two days get "Advt - Facebook" or "Advt - Instagram" with Lead Channel "Advt": 40 of 40 checked across SIB-04 ACR, Incorporation V2 and Trademark V2. Two of the 40 still had Lead Channel blank shortly after arrival.

## Test lead: assigned to Swati (Sanjeev, 13:14: "send to swati")
- Email sent at about 13:20 IST, Gmail message 1a1531f6ffe94021, to swati.dhoundiyal@setindiabiz.com, cc Sanjeev.
  - Asked for fresh email and phone; her own are already on lead 1123581000948692001.
  - Sanjeev is to WhatsApp her the preview link of a v2 ad such as E2 120247068331330449, **not E1**.
- **Sanjeev at 13:24: "continue without this check".** The v2 test is no longer a gate for launch. If Swati submits, check it then.

## Dropped 16 Oct 20:26 lead: explained
- The Recycle Bin shows a Lead "Sanjeev Kumar" **deleted 16/10/2026 20:27 by "Sanjeev Kumar"**, one minute after LeadChain created it.
- So the lead was created and then **deleted by an automation running under Sanjeev's account**. It was not skipped by LeadChain.
  - No Lead or Contact with that phone or email was modified, so it was a delete, not a merge.
- The same pattern runs all day. Today's bin has Leads deleted by "Sanjeev Kumar" every few minutes (e.g. "Aditya Bisht" ×4 between 12:43 and 13:07), together with their "Duplicate Record(s) Found" notes.
- What it is NOT:
  - "Detect Duplicate Lead" v2 only flags and notes; it never deletes.
  - Function "Dedup CRM Merge Drainer" (dedup_crm_merge_drainer) exists, but it is Standalone, not associated with a workflow, and not in Schedules.
  - **The deleter is not yet identified.** It is probably an external job or integration using Sanjeev's OAuth.
- Exposure (LeadChain "leads synced" vs CRM Leads by Meta_Lead_Form, lifetime):

| Form | LeadChain | CRM | Gap |
|---|---|---|---|
| Trademark V2 | 831 | 786 | 45 |
| Incorporation V2 | 843 | 811 | 32 |
| CCFS2026 V2 | 611 | 552 | 59 |
| SIB-04 ACR | 92 | 80 | 12 |
| DPIIT V2 | 97 | 92 | 5 |
| Virtual CFO V2 | 17 | 17 | 0 |

  - The gaps include converted leads, so they are an upper bound, not a count of deletions.
- Risk for SIB-05: a returning client or anyone already in CRM may submit the FDI form, and that lead may be deleted within a minute. FDI leads are high-value, so this matters.

## SIB-05 launch readiness (connector read-back, 13:25)

| Item | State |
|---|---|
| Campaign 120247067847480449 + ad set India Entry + E1 | Live, PAUSED, ₹0 |
| E1 | Pending **modify** draft: form v1 4073050519663550 → v2 1741840353557832. VALIDATED, 0 errors |
| E2, S1, S2, B1, B2 | Drafts (add), PAUSED, form v2, VALIDATED, 0 errors |
| Ad sets Subsidiary, Branch-Liaison | Drafts, VALIDATED, 0 errors |
| Audience suggestions | Still include "Co Owner"; Founder, Partner, Managing Partner, VP and the India Desk titles are missing (suggestions only) |
| LeadChain v2 / PPC Form Tidy v2 entry | Done |
| Booking-email workflow | Still v1-only (parked) |
| End date (D31) | Not set; set to 30 days on publish |
| Funding | About ₹17.4k on the morning of 19 Oct; SIB-05 adds ₹4,000/day |

## Next
1. Sanjeev: decide on the booking-email condition and the audience suggestions, fund the account, set the 30-day end date, then publish SIB-05 in Ads Manager (G13; human click).
2. Identify the job that deletes Leads as "Sanjeev Kumar" (check Zoho Flow, Catalyst, SalesIQ and Connected Workflows, and the API-usage log). Decide whether paid "Advt - *" leads should be exempt.
3. If Swati's test lead arrives, run the G9 checklist on it.
