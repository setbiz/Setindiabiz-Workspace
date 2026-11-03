# Prompt for the "SalesIQ Tiya" project: chat tickets → CRM lead link and lead-owner assignment

*Paste everything below this line into a new chat in the SalesIQ Tiya project. Attach `Chat_Tickets_DryRun_2026-10-13.csv`.*

---

You are working in the SalesIQ Tiya project for Setindiabiz.

Use this project's own docs and memory: Tiya (the Zia agent), the SalesIQ→Desk integration, the Zoho Flows, the Desk dedup functions and the consolidated ops task. On top of that, use the findings below, which came from the "Meta Ads - Optimisation" project on 13 Oct 2026.

**The problem.** WhatsApp and website chat tickets in Zoho Desk are not linked to their CRM lead and are not assigned to the lead owner. Sanjeev believes this was solved here earlier and wants to know why it is happening again. Then fix it, carefully.

## Systems and IDs

**Zoho CRM**
- US data centre, crm.zoho.com, org 36264019; Setup URLs use /crm/setindiabiz/.
- CRM API from a logged-in tab: header X-CRM-ORG = window.crmZgid, header X-ZCSRF-TOKEN = 'crmcsrfparam=' + the crmcsr cookie.
- Workflow rules: `/crm/v8/settings/automation/workflow_rules?module=Leads`, then GET each by id.
- Functions list: `/crm/v7/settings/functions?type=org&start=N`. Function source: `/crm/v7/settings/functions/{35880000… id}?source=crm`.

**Zoho Desk**
- Org 669468905; department "Support Desk" 293676000000006907; chat tickets have channel = "Chat".
- The CRM↔Desk connection is "crm_and_desk_connection".

**SalesIQ** is at salesiq.zoho.com/wwwsetindiabizcom/.

**SIB-04 (Meta click-to-WhatsApp, Company Annual Filings)**
- WhatsApp number [phone redacted], brand Compliance & ACR.
- Zobot "Tiya - Annual Filings", plug `sib_wa_lead_1791383468657`.
- What happens on a chat:
  1. SalesIQ's native push creates a "Self - Web Chat" lead.
  2. The plug claims it: Lead_Source = "Advt - WhatsApp".
  3. The LG-11 round robin sets the owner.
- Since 13 Oct, chats go Support-first: Customer Support picks up, then transfers to the lead owner. SIB-05 (FDI, +919599199508) works the same way.

**Lead Ticket field:** CRM field RM_Lead_Ticket (label "Lead Ticket", text). It holds the Desk ticket number.

## What was found (read-only, 13 Oct 2026, ~19:50–20:10 IST)

Window: tickets created 10 Oct 00:00 to 13 Oct 20:00 IST.

1. **Volume.**
   - 87 Desk chat tickets in the window: 54 OFFLINE_CHAT, 32 ONLINE_CHAT, 1 FEEDBACK. 57 of them are unassigned.
   - Matched on exact phone, they belong to 78 CRM leads: 54 SIB-04 leads (58 tickets) and 24 website or other chat leads (27 tickets).
   - 2 tickets have no lead: 1414883 (+919919001970, Spinkart E-commerce) and 1415687 (+918961995011, Divya Upadhyay).
2. **No link and no owner.**
   - None of the 54 SIB-04 leads has its chat ticket in RM_Lead_Ticket.
   - 49 of their 58 chat tickets are unassigned. Only 3 sit with the lead owner (1414488 Tarun, 1414786 and 1414787 Priyam).
3. **The Desk contacts behind WhatsApp chats are not linked to CRM.**
   - Example: Desk contact 293676000532544128 (+917463095566, lead …946568358). It has phone only, no email, `zohoCRMContact` = null, and its owner is Sanjeev.
   - Compare Khushboo Yadav, contact 293676000532636103. She has an email, `zohoCRMContact` = {lead 1123581000946554242}, and her owner is a sales agent.
   - Only 7 of the 127 SIB-04 WhatsApp leads have an email.
   - **Hypothesis:** every owner sync from CRM to Desk depends on that email-based link. The Desk rule "Sync Owner and include CC in ticket", the Zoho Flow "Lead Owner - Ticket Owner" and the CRM functions below would all then miss phone-only chat contacts. Verify this.
4. **The CRM functions match by email only.** All three are attached to Leads workflow rules.
   - `transferdeskticketstoleadowner` (35880000003681001), rule "Transfer Desk Tickets To Lead Owner" (1123581000912769323). It fires on a change to Owner, Refresh or Lead_Status, when Duplicate_Status ≠ Yes. It searches Desk contacts only by Email and Secondary_Email.
   - `updatedeskticketownerfromlead` (35880000003679001): email only.
   - `create_desk_ticket_from_lead` (35880000003620001), rule "Create Desk Ticket From Lead" (1123581000899715293), when Create_Ticket = Yes and RM_Lead_Ticket is empty. It finds the contact by email; if there is no match it creates a new contact and a new **Web** ticket ("L<Lead_Number> - name - product"). It never checks for an existing chat ticket.
   - There is also the webhook rule "Leads_ZohoFlow_Create Contact in Desk From Lead" (1123581000896072001).
5. **A timing gap.** The chat lead is created, claimed and assigned when the chat **starts**. The Desk chat ticket is created only when the chat **ends**, usually 10–60 minutes later, sometimes days later. That follows from the integration setting "convert chats as tickets while ending chat", and this project's ops task documents it. So every CRM trigger on owner change fires **before** the ticket exists. Nothing fires once the ticket appears.
6. **Duplicate tickets.**
   - **Repeat chats:** SalesIQ opens one ticket per chat session, so a person who chats twice gets two tickets. In 4 days, 7 people did:

     | Lead | Tickets |
     |---|---|
     | Hafeez (…946586197) | 1414789, 1414796 |
     | kim (…946435157) | 1414886, 1414909 |
     | parbhabhai2 (…946493326) | 1414902, 1414905 |
     | Znight (…946575496) | 1415416, 1415810 |
     | rajalekshmi (…946429391) | 1414842, 1415108 |
     | Sanu Meena (…946532236) | 1414858, 1414869 |
     | Neeshu (…946586415) | 1415025, 1415755 |

     The hourly Desk schedule "Dedup Hourly Retirement" (Dedup_Retirement) did not retire any of them. Check whether it is meant to.
   - **CRM double:** pressing Create Ticket on a chat lead makes a second ticket. One case so far: Khushboo Yadav, chat 1414892 + Lead Ticket 1415338, same contact.
   - **New contact:** on a phone-only lead, Create Ticket also makes a new Desk contact. Example: Rachna …946442337 got new contact 293676000532948712 and ticket 1415955.
7. **The consolidated ops task** ("Setindiabiz Ops — Tiya + Desk + CRM", runs every 3 h at :15 UTC). In PART B it already matches chat leads to chat tickets by phone. But its allowed writes are limited to subjects, blank Description/Email, Notes and deleting sync-gap notes. So it never writes RM_Lead_Ticket and never assigns tickets. That is probably why this looked solved: the subjects and descriptions are handled, the link and the assignment never were.

**Tool quirks.**
- Desk `searchContacts` by phone needs the exact stored form, e.g. "+917463095566". Wildcards and `_all` return nothing. Use the ops task's five-variant phone ladder.
- `searchTickets` by phone returns 204.
- Desk `getContact` rejects `include`.

## Sanjeev's decisions (13 Oct, 20:08 IST)

- **Include website chats** ("Self - Web Chat", ChatGPT and other chat sources), not just SIB-04 WhatsApp.
- **Where a lead has no Desk ticket, don't create one.** No mass ticket creation.
- **Work on ticketing here,** in this project, because it has the history and the setups.

## What to do, in order

**Step 1. Read this project's own history first (read-only).** Then answer two questions in plain words:
- What was built here earlier for chat tickets ↔ CRM leads ↔ owner?
- Why doesn't it cover these tickets?

Check at least:
- the Zoho Flows "Lead Owner - Ticket Owner" and "Job Associate - Ticket Owner": trigger, matching key, last runs;
- the Desk workflow rules, especially "Sync Owner and include CC in ticket", and any Desk custom function or rule on ticket create for channel Chat;
- the Desk schedule Dedup_Retirement: what it retires and why the 7 pairs above survived;
- the SalesIQ › Settings › Integrations › Zoho Desk settings: when tickets are created, which department and team, and whether the Desk contact gets linked to the CRM lead;
- whether Tiya (the Zia agent) or any SalesIQ workflow writes tickets or leads;
- whether anything here broke or was switched off around 9–13 Oct, when SIB-04 went live. In that period, rules and functions were cleaned up and deleted on 9 Oct, the "Lead Assignemnt - Edits" workflow was changed and Support-first routing started.

**Step 2. Refresh the dry run (read-only).**
- Re-pull chat tickets from 10 Oct to now and match them to leads with the phone ladder.
- Rebuild the attached CSV with the same columns.
- Get the Desk agent ID for every owner by matching the CRM user's email to the agent's emailId.
- Known agent IDs: Tarun 293676000508366084, Mahima 293676000509340034, Shivam Chauhan 293676000455065135, Soina Jain 293676000470025003, Sanjeev 293676000000088035.

**Step 3. Propose one design for the fix and wait for Sanjeev's OK.** The recommendation from the Meta project is a **Desk-side workflow on ticket create (channel = Chat)** with a Deluge custom function, because it fires at the right moment. The function should:
- (a) find the CRM lead by phone (phone ladder; prefer the newest lead that is not a duplicate; for an existing client, the Contact);
- (b) write the ticket number into RM_Lead_Ticket only if the field is empty;
- (c) assign the ticket to the lead owner's Desk agent, but only if all of these hold:
  - the subject category is Sales Inquiry (the ops task's PART A runs later, so on create, judge by lead and owner, not subject);
  - the ticket is Open;
  - the owner is an active user who isn't on the skip list.

  Leave Customer Support, Complaint, Job Application, Vendor and General Query tickets with Support;
- (d) optionally link the Desk contact to the lead, if the API allows it.

Add a matching patch to `transferdeskticketstoleadowner` so that a later owner change also moves the ticket, using RM_Lead_Ticket and phone as well as email.

Add a patch to `create_desk_ticket_from_lead` so that it reuses an open chat ticket and the existing contact found by phone, instead of creating a second ticket.

If this project already has a better mechanism, such as fixing the Flow or the Desk link, propose that instead and say why.

**Step 4. Backfill, after OK and in batches.**
- **RM_Lead_Ticket.** For each lead without one, write the first chat ticket number. 75 leads on 13 Oct: 54 SIB-04 and 21 others; 3 already have a value. Use the CRM connector with `trigger: []` and skip assignment rules.
- **Assignment.** On 13 Oct: 44 SIB-04 tickets plus 7 website-chat tickets, 51 in all. 4 of the 51 (2 SIB-04, 2 website) wait until their owners are confirmed as Desk agents. Desk sends each agent an assignment notification.
- **Skip or hold:**
  - owner Lost Records (…117753968): skip;
  - admin (…006825001): skip;
  - Gaurav Pandey (…900792006, disabled): hold until Sanjeev names new owners;
  - Hafeez (Duplicate_Status = Yes): ask;
  - old 2025 leads on system or inactive owners (Gopal Roy …741813001 on Alerts, Pradeep Jena …741843105 on …805919001): ask;
  - closed tickets and non-sales tickets: leave as they are.
- **Repeat-chat tickets:** Sanjeev decides between merging into the first ticket, closing as duplicate, or leaving. A merge can't be undone, so Sanjeev does it in Desk.

**Step 5. Monitoring.** Propose (don't apply) a small addition to the ops task: report chat tickets older than 1 h with no linked lead or with an assignee who isn't the owner. Any change to the ops task needs Sanjeev's OK on the exact text.

## Hard rules

- **One change at a time.** Every change to CRM, Desk, SalesIQ, Zoho Flow, a scheduled task or Tiya needs Sanjeev's explicit OK, one change at a time, with before/after evidence, logged in a dated change log in this project.
- **Code.** Show the code or diff before saving any function, workflow or schedule. Back up the current code to the project first.
- **Mass writes** need a dry-run list and approval. Don't delete or merge CRM records or Desk tickets. CRM connector writes use `trigger: []` and skip assignment rules.
- **Hands off without OK:** the SIB-04 / SIB-05 plugs, Zobots or routing, and the Tiya agent.
- **Emails:** draft first and send only on Sanjeev's yes.
- **Browser:** if a permission check blocks a Setup click, leave the screen ready and hand the click to Sanjeev.

## Output

End with:
- a short plain-language answer to "why did this happen again";
- the change log;
- a resume prompt for this project;
- a **3–5 line summary for Sanjeev to paste back into the "Meta Ads - Optimisation" project.** It should say what changed, which mechanism now links and assigns chat tickets, and anything the SIB-04 / SIB-05 daily checks should watch.
