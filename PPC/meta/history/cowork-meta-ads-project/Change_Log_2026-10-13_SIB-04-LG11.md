# Change log — 13 Oct 2026 — SIB-04 LG-11 build (assignment fixes)

Sanjeev approved the build at 13:21: "do all the three suggested by you. you can take browser control and do the needful". Build plan: `SIB-04_LG11_Build_Steps_2026-10-13.md`.

**Redesign at 15:53 (Sanjeev):** "lets build some thing simple, we will keep support team always available, when the lead is auto assigned the support team will transfer the chat". At 16:25 he added: "whether this is new or existing chat let it go to support who will then engage with client and will then proactively transfer to sales team after record is transferred to [the owner]". As a result, the per-owner chat routing (Step 1c–1d of the build plan) was dropped. See L5–L7.

**16:33 (Sanjeev, "Yes"):** remove the two bot questions so chats go straight to Support. See L8–L9. **V5 published by Sanjeev at ~16:44.**

| # | Item | Change | Before | After | Verified |
|---|---|---|---|---|---|
| L1 | CRM workflow "Lead Assignemnt - Edits" (1123581000748082795), Condition 1 | Added the criterion **Lead Source isn't Advt - WhatsApp**, pattern (1 and 2). | Lead Assignment is Auto → field update "Lead Assigned On" + Assign Owner by "Lead - General 2026" | Same actions. Auto no longer re-runs the general round robin on WhatsApp ad leads. | Yes. The API read-back (GET workflow_rules) shows the group Manual_RM equal Auto AND Lead_Source not_equal Advt - WhatsApp. Saved 13:4x (PUT 200). |
| L2 | Same rule, new **Condition 3** | Criteria: Lead Assignment is Auto AND Lead Source is Advt - WhatsApp AND Lead Owner is Pavneet Kaur. Action: Assign Owner by rule **PPC - SIB-04 Annual Filings - LG-11** (1123581000945354238). No notification, no related-record transfer. | 2 conditions (C2 = Lead Assignment is Sanjeev Kumar → Sanjeev, untouched) | 3 conditions; modified 13:52:57 | Yes. Read-back shows condition id 1123581000946926304 with the LG-11 rule. |
| L3 | **Backfill of 82 SIB-04 chat leads** (list: `SIB-04_Backfill_DryRun_2026-10-13.csv`) | Fields set: Lead_Source "Advt - WhatsApp", Lead_Channel "Advt", Meta_Ad_Type "WhatsApp", Meta_Ad_Code "ACR", Meta_Campaign "SIB-04 Annual Filings". Tag FB-ACR added (none had tags before). trigger [] (no workflows, assignment or blueprint). One test record (…520233) at 13:56, then 81 more at 13:57:25. | Self - Web Chat, no ad fields | Advt - WhatsApp + ACR + FB-ACR | Yes. All 82 re-read by COQL. **Owners unchanged on all 82**, products unchanged. 4 statuses differ from the 12:55 dry run: …435637 and …493599 went from empty to Establishing Contact; …543594 and …564200 went to Lost. These were RM edits in the hour between; the backfill sent no status field and ran no workflows. |
| L4 | Bot "Tiya - Annual Filings" — **A00 Welcome** | 5-second wait on, info message "One moment please ⏳", default exit → A03. | No wait | Saved by Sanjeev ~14:10 | Yes (actions API: delay_config enabled, time 5) |
| L4b | Bot — new plug card **A03 CRM claim (start)** (1791881828323) | Runs `sib_wa_lead` right after the welcome, so the SalesIQ lead is claimed and assigned through LG-11. Inputs: adcode ACR, productid 1123581000000185017, campaign "SIB-04 Annual Filings", productcat Annual Filing, answers "Chat opened (before questions)", phone/email from visitor, ruleid 1123581000945354238, tag FB-ACR. | Plug ran only after both questions (A04) | Saved by Sanjeev ~14:27 | Yes (actions API) |
| L5 | Bot — **A05** router (1791370009000) | Renamed **"A05 Existing customer or new lead"**. All 10 owner rules were removed, plus the 5 owner rules added at 15:42 (Sudip, Foziya, Himanshu Singh, Shubendu, Krishna). One rule kept: `ctx.wa_matched == contact` → A07 Forward to Customer Support. Default → A07 (new lead). | "A05 Route to CRM owner", 16 rules → 11 A06 per-owner forward cards | Saved by Sanjeev 16:24 | Yes (actions API: 1 rule + default) |
| L6 | Bot — card 1791370010000 | Renamed **"A07 Forward to Customer Support (new lead)"**. Department changed from Sales - CACS ACR to **Customer Support** (61466000018349043), all available operators. Message unchanged: "Connecting you to our compliance team ⏳". Fallbacks (offline / operators NA / invalid) → A08 Team offline - close. | "A07 Forward to Sales - CACS ACR" (fallback target of the A06 cards) | Saved by Sanjeev ~16:25 | Yes (actions API: department 61466000018349043) |
| L7 | Bot — 11 unused forward cards | **Deleted by Claude** at 16:28–16:33, each confirmed in the Delete Card dialog: A06 Forward to Pragya Agrawal, Rishika Singh, Tarun Kumar, Mahima Sehrawat, Anish Singh, Amit Kumar, Priyam Tiwari, Gaurav Pandey, Suman Khowal and Praveen Singh. Also deleted: the A06 Forward to Sudip Manna card, created 15:4x for the dropped design, with its 2 empty exits. | Disconnected after L5; the builder showed 13 errors | 13 cards, all connected; error badge gone | Yes (actions API + builder header) |
| L8 | Bot — question cards | **Deleted by Claude** at 16:35–16:40: A01 Entity type; A02 Year (Pvt Ltd / OPC / LLP); A04 CRM lead (Pvt Ltd / OPC / LLP). A03's Success and Failure exits were then connected by drag to A05. | A03 → A01 → A02 → A04 → A05 | A03 → A05 (both exits) | Yes (actions API: A03 success/default → 1791370009000) |
| L9 | Bot — A00 Welcome text | "…Two quick questions, then we'll connect you to a compliance expert." changed to **"👋 Hi %visitor.name%! Thanks for contacting Setindiabiz about annual ROC filings. Connecting you to a compliance expert now."** The 5 s wait is unchanged. | — | Saved by Sanjeev ~16:43; **published as V5 ~16:44** | Yes (actions API text; builder header "V5 - PUBLISHED"; bot API published=true) |

Side effect of L1: Zoho warned "Change criteria: the data in the reports generated up to this point will be reset". This is the rule's own usage counter only; lead data is unaffected.

Canvas-only change: the builder re-arranged card positions after the deletions (layout only).

Permission note: Claude's Save clicks in the SalesIQ bot builder are refused by the session's permission check ("Modify Shared Resources"). Claude prefilled each panel and Sanjeev clicked Save. Connecting exits by drag and deleting cards were not refused.

## Live bot V5 (published ~16:44)

A00 Welcome (5 s wait) → A03 CRM claim (start) → A05 Existing customer or new lead
- existing customer (CRM contact) → **A07 Forward to Customer Support** ("Connecting you to your Setindiabiz relationship team ⏳")
- everyone else → **A07 Forward to Customer Support (new lead)** ("Connecting you to our compliance team ⏳")
- if no Customer Support operator is available → **A08 Team offline - close** (end chat: "…An expert will call you on this WhatsApp number…")

Support then talks to the client, checks the CRM owner (assigned through LG-11 at A03) and transfers the chat to that salesperson. If the owner doesn't accept, the chat stays with Support.

## First live chat on V5 — PASSED (checked 17:05)

Chat **#61499 "Sumit Kohli"** ([phone redacted], conversation 61466000026783664). Timeline:

| Time | Event |
|---|---|
| 17:02:37 | Chat starts |
| 17:02:39 | SalesIQ creates the lead **1123581000946561933** |
| 17:02:43 | The A03 plug claims it: Lead_Source **Advt - WhatsApp**, Meta_Ad_Code ACR, Meta_Campaign SIB-04 Annual Filings, Product Cat Annual Filing, tag **FB-ACR**, owner **Krishna Gupta** (LG-11) |
| 17:02:44 | The bot sends the new welcome and "Connecting you to our compliance team ⏳", then forwards to **Customer Support** |
| 17:02:48 | **Pavneet Kaur** (Support) picks the chat up |
| 17:03:11 | Pavneet **reassigns it to Krishna Gupta** (Sales - CACS ACR) |

Result: **the chat handler matches the lead owner** (Krishna Gupta). Support handed the chat over 23 seconds after picking it up.

## What to watch

- Customer Support must stay online during ad hours. If nobody in Customer Support is available, the bot closes the chat with the call-back message.
- A salesperson can only receive a transfer if they are a SalesIQ operator.
- Product: with no entity question, every lead gets "ACR - Company Annual Return" (1123581000000185017), LLPs included. Support or sales correct it on the lead.
- The CRM note text from A03 still reads "Chat opened (before questions)". This is cosmetic and needs one Save to change.

## Related, same day

CRM → Meta CAPI sweep v2 (WhatsApp leads now reported; leak fixed; 36 events sent): `Change_Log_2026-10-13_CAPI-Sweep-v2.md`.
