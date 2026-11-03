> **Update 13 Oct 20:08 IST:** Sanjeev moved the ticket work (steps 1–3 below) to the **SalesIQ Tiya project**. The prompt is `Meta Ads/Tiya_Project_Prompt_Chat_Tickets_2026-10-13.md`. In this project:
> - do not run T1–T7;
> - run step 0 (SIB-04 checks), then step 4 (SIB-05), then step 5 (INC/TMF);
> - when Sanjeev pastes back the Tiya project's summary, record it in a change log and add any new daily checks.
>
> Sanjeev's decisions on 13 Oct: include website chats; don't create tickets where none exist.

You are continuing Setindiabiz work in the "Meta Ads - Optimisation" project. The order Sanjeev set on 13 Oct is:

1. **Desk tickets for chat leads.** Fix these first. This is the main job of this session.
2. **SIB-05 India Entry (FDI Services).** Resume it with `Meta Ads/SIB-05_Resume_Prompt_2026-10-14.md`.
3. **Then the next two campaigns: Incorporation (INC) and Trademark (TMF).** They were the strongest lead sources earlier. Start planning only after SIB-05 is built.

SIB-04 Company Annual Filings is live and needs its daily checks only.

Zoho CRM is crm.zoho.com (US DC, org 36264019; Setup URLs use /crm/setindiabiz/). Zoho Desk org is 669468905, department "Support Desk" 293676000000006907, and the CRM↔Desk connection is "crm_and_desk_connection". SalesIQ is at salesiq.zoho.com/wwwsetindiabizcom/. The Meta account is SETINDIABIZ 152154124583473; Meta tool calls use client_model "claude-opus-5-5".

## Read first (project docs)

- `Meta Ads/Desk_Tickets_Diagnosis_2026-10-13.md`: **start here.** It has the findings, R137–R142, the dry-run table (54 SIB-04 leads / 58 chat tickets) and the proposed changes T1–T7.
- `Meta Ads/Change_Log_2026-10-13_SIB-05-G11-Decisions.md`: the SIB-05 state and open items 1–11.
- `Meta Ads/SIB-05_Resume_Prompt_2026-10-14.md`: SIB-04 morning-check method, owner IDs and the SIB-05 steps.
- `Meta Ads/Change_Log_2026-10-13_CAPI-Sweep-v2.md` and `Meta Ads/Change_Log_2026-10-13_Duplicate-Detector.md`: patterns for scheduled functions and code backups.

## State at 13 Oct 2026, ~20:00 IST

- **Two kinds of Desk ticket exist.**
  - **Chat tickets** come from the SalesIQ→Desk integration: one per chat session, channel Chat, usually unassigned, and nothing is written back to CRM.
  - **Lead Tickets** come from the CRM "Create Ticket" step: channel Web, subject "L<Lead_Number> - name - product", and the ticket number goes into RM_Lead_Ticket.
- **Duplicates.**
  - 7 people have 2 chat tickets because they chatted twice. 4 of them are SIB-04 leads: Hafeez 1414789+1414796, kim 1414886+1414909, parbhabhai2 1414902+1414905, Znight 1415416+1415810.
  - 1 CRM double so far: Khushboo Yadav …946554242, chat ticket 1414892 + Lead Ticket 1415338.
- **Assignment gap.**
  - 49 of the 58 SIB-04 chat tickets are unassigned.
  - None of those 54 leads has RM_Lead_Ticket set.
  - `transferdeskticketstoleadowner` (35880000003681001) and `create_desk_ticket_from_lead` (35880000003620001) look up Desk contacts **by email only**. WhatsApp leads have a phone and no email (only 7 of 127 SIB-04 WhatsApp leads have one).
- **No ticket at all.** 76 SIB-04 WhatsApp leads have no Desk ticket.
- **Nothing has been changed yet.** The dry run was shown to Sanjeev at ~20:00.

## Next, in order

**0. SIB-04 morning checks (read-only).** Use the method in `SIB-05_Resume_Prompt_2026-10-14.md`, step 1:
- placements for 14 Oct (Audience Network and Marketplace should both be ₹0);
- the 13 Oct full-day scorecard and speed-to-lead;
- the CAPI sweep (were …946568358 and …946574748 sent at the 20:00 run on 13 Oct?).

Keep the report short, then move on to tickets.

**1. Refresh the dry run (read-only).** New chats arrive every hour.
- Desk `searchTickets` with channel "Chat" and createdTimeRange from 2026-10-09T18:30:00.000Z to now. Use limit 100 and page with `from`. The result saves to a file; parse it with jq.
- Pull Phone, Owner, RM_Lead_Ticket, Lead_Source, Meta_Campaign and Duplicate_Status by COQL `Phone in (…)`, at most 40 values per query.
- Match on the exact "+91…" phone. Rebuild the table in the diagnosis doc's format.
- Get the Desk agent IDs for each owner. There is no agents tool in the connector, so open desk.zoho.com in the built-in browser and run a read-only fetch of `/api/v1/agents?limit=200` from the page (or ask Sanjeev for a Desk agents export). Match the CRM user's email to the agent's emailId.
- Known agent IDs: Tarun 293676000508366084, Mahima 293676000509340034, Shivam Chauhan 293676000455065135, Soina Jain 293676000470025003, Sanjeev 293676000000088035.
- Confirm whether owners …919146001 (Yadav) and …900716015 (Bisht) have Desk agents.

**2. Back up the code (read-only), before any edit.** Read the current source of these three functions and save each to the project as `Meta Ads/<name>_v1_2026-10-14.deluge.txt`:
- `transferdeskticketstoleadowner` (35880000003681001)
- `create_desk_ticket_from_lead` (35880000003620001)
- `updatedeskticketownerfromlead` (35880000003679001)

To read the source, use GET `/crm/v7/settings/functions/{id}?source=crm` from the CRM tab, with headers X-CRM-ORG = window.crmZgid and X-ZCSRF-TOKEN = 'crmcsrfparam=' + the crmcsr cookie. The 1123… workflow action IDs return 204, so use the 35880000… IDs above.

**3. Ask Sanjeev for decisions, then do T1–T7 one at a time, each on his explicit OK:**

- **T1. Backfill RM_Lead_Ticket.**
  - Value: the first chat ticket number, plain digits.
  - Scope: the SIB-04 leads in the refreshed table (54 on 13 Oct).
  - Method: connector `updateRecords` on Leads with `trigger: []`, in batches of 100 or fewer.
  - Show the final list first. Afterwards, verify by COQL and log it.
- **T2. Assign those chat tickets to the lead owner's Desk agent.**
  - Method: Desk `updateTicket` → `assigneeId`.
  - Scope: 42 leads / 44 tickets on 13 Oct.
  - Skip leads owned by Lost Records (…117753968) or admin (…006825001).
  - Hold Gaurav's leads (disabled) until Sanjeev names new owners. Ask about Hafeez (…946586197, Duplicate_Status = Yes).
  - Tell Sanjeev that Desk emails the agents an assignment notification.
- **T3. Second-session duplicates** (4 SIB-04 pairs + 3 others).
  - Sanjeev chooses merge into the first ticket, close as duplicate, or leave as is.
  - The connector has no merge tool, and a merge is irreversible. So Sanjeev merges in Desk, or approves each browser click.
- **T4. New scheduled function `sib_chat_ticket_link`, hourly.**
  - Show the full code first. Follow the sib_capisweep v2 pattern (schedule, log, idempotent).
  - Pick leads created in the last 7 days where RM_Lead_Ticket is empty and Phone is not empty. Sources: "Advt - WhatsApp", "Self - Web Chat" and SIB paid form leads.
  - Look up the Desk contact by exact Phone, take the newest open Chat ticket, write RM_Lead_Ticket with no workflow trigger, and assign to the owner's agent unless the owner is skipped.
  - Test on one lead before scheduling.
- **T5. Patch `transferdeskticketstoleadowner`.**
  - Show the diff first.
  - If RM_Lead_Ticket is set, fetch that ticket and assign it. Also search contacts by exact Phone, not just Email. Keep the Duplicate_Status guard.
  - Test on one lead.
- **T6. Patch `create_desk_ticket_from_lead`.**
  - Show the diff first.
  - If there is no email match, look up the contact by Phone before creating one.
  - If that contact has an open Chat ticket, write it to RM_Lead_Ticket and assign it instead of creating a second ticket.
  - Test on one lead.
- **T7. SalesIQ › Settings › Integrations › Zoho Desk (read-only).**
  - Record when tickets are created (missed, offline, all chats).
  - Record whether a new chat can be added to the person's open ticket.
  - Report the findings; change nothing without OK.

**Open decisions to raise once each:**
- phase 2 (24 non-SIB-04 chat leads, 27 tickets);
- the 76 SIB-04 WhatsApp leads with no ticket (recommendation: no mass creation; RMs press Create Ticket after T6 is live);
- new owners for Gaurav's 3 SIB-04 leads (…946345169, …946520407, …946590157).

**4. When the tickets are sorted, switch to SIB-05.** Follow `SIB-05_Resume_Prompt_2026-10-14.md`:
- G9 once Sanjeev confirms the three test leads;
- Vipin's 12 images (Gmail thread 1a1359139e2d73dc), with an on-image claims check before G12;
- G12 build with the campaign OFF;
- G13: Sanjeev publishes.

**5. After SIB-05: plan the INC and TMF campaigns.** Before proposing anything, read:
- `Meta Ads/Deep_Analysis_2026-10-06.md`
- `Meta Ads/Ad_Product_Mix_and_Ticket_Size_2026-08-23.md`
- `Meta Ads/Account_Review_2026-07-02.md`
- the IND1/IND3 watchdogs from Jul–Aug

What those docs already establish:
- **TMF (IND3)** gave the cheapest valid leads: cost per valid ₹233–350 in Jul–Aug.
  - The best ad was "Trademark Filing @ ₹1,999 Only", which showed the government fee upfront (Meta CPL ₹133–151).
  - Ads with a clear price beat generic and fear angles by 2–7x on CPL.
- **INC (IND1)**: the "Pvt Ltd – ₹2,499" creative had CPL ₹172–206.
  - "in 7 days" is a timeline claim that can't be guaranteed, so don't reuse it.
- **On business outcomes, both returned only about 0.33–0.34x first-deal revenue per rupee spent.** Judge the relaunch on cost per won deal and first-year account value. Consider the bundles in the product-mix doc (INC + Key Five Docs + ADT-1 + INC-20A + first-year ACR; TM filing + exam-report reply).
- **Re-verify every government fee against the current rules before any copy.**
  - TM: Trade Marks Rules 2017, First Schedule. On 2 Jul the fee was ₹4,500 for individuals, startups and MSMEs and ₹9,000 for others (e-filing). Check the latest amendment.
  - INC: the Companies (Registration of Offices and Fees) Rules 2014 and the current SPICe+ fee.
- Draft a build spec for each campaign, as was done for SIB-04 and SIB-05. Get Sanjeev's OK on copy before any Meta build.

## Owner IDs

Use the table in `SIB-05_Resume_Prompt_2026-10-14.md` (prefix 1123581000).

Owners seen on chat-ticket leads:
- Lost Records 117753968
- Gaurav 900792006 (disabled)
- Yadav 919146001 and Bisht 900716015 (not yet resolved)
- Tomar 929638024
- Vishwakarma 939988020

## Hard rules

- **Meta.** Never activate or publish a Meta campaign. Never move money, never top up, never enter passwords, never call ads_activate_entity.
- **Changes.** Any CRM record, workflow, function, Desk ticket, SalesIQ or Meta change needs Sanjeev's explicit approval, one change at a time, with before/after evidence. Mass writes need a dry run and approval first.
- **Code.** Show the code or a diff before saving any production function, workflow or schedule. Back up the current version to the project first.
- **CRM edits with the connector.** Pass `trigger: []` and skip assignment rules. Don't delete CRM records or Desk tickets. Don't edit the 11 older LeadChain chains.
- **Emails and messages on Sanjeev's behalf.** Draft first, confirm the recipient, and send only on his yes. Gmail sends from one@setindiabiz.com; cc sanjeev@setindiabiz.com when he asks.
- **Copy.** Ad copy, on-image text and website text need Sanjeev's OK on the exact text. No unprovable claims: no "in X days", no guarantees, and no "100% FDI allowed" or "no approval needed" for SIB-05. Quote government fees from current rules only.
- **Browser.** If the permission check refuses a Setup page or a click, hand that step to Sanjeev. Reset any viewport to desktop afterwards.

## Tool notes

- **Desk `searchContacts` by phone** works only with the exact "+91XXXXXXXXXX" form. Wildcards and `_all` return 204.
- **Desk `searchTickets`:**
  - phone search returns 204;
  - `contactId` must be a single value, not a list;
  - `getTicketsByContact` rejects include values such as "assignee,departments".
  - Ticket search by `ticketNumber` takes a list and works.
- **Large Desk results** save to a file; parse them with jq.
- **COQL:** use `Phone in (…)` with at most 40 values per query, and GROUP BY for counts.
- **CRM API from the page:** /crm/v8/settings/automation/workflow_rules?module=Leads, and /crm/v7/settings/functions?type=org&start=N.

## Output

End with:
- a short report (done / open / who);
- a new dated change log (`Meta Ads/Change_Log_2026-10-14_Desk-Tickets.md`, continuing from R143 and C94);
- the prompt for the session after.
