# Desk tickets from chat leads: diagnosis and dry run (13 Oct 2026, ~20:00 IST)

**Status:** read-only. Nothing in CRM, Desk or SalesIQ was changed. Every change below (T1–T7) needs Sanjeev's explicit OK, one change at a time.

**Question (Sanjeev, 19:50):** "Do we have two tickets created from a lead? How do we backfill the Lead Ticket field in CRM for leads that came in through these chats, and then auto-assign the ticket to the lead owner?"

**Window checked:** tickets created 10 Oct 00:00 to 13 Oct 20:00 IST.

---

## 1. Short answer

**Yes, there are duplicate tickets, in two ways:**

1. **SalesIQ opens a new chat ticket for every chat session.** If the same person chats twice, Desk gets two tickets. In four days, **7 people have 2 chat tickets each**. Four of them are SIB-04 leads:

   | Lead | Tickets |
   |---|---|
   | Hafeez | 1414789, 1414796 |
   | kim | 1414886, 1414909 |
   | parbhabhai2 | 1414902, 1414905 |
   | Znight | 1415416, 1415810 |

2. **The CRM "Create Ticket" step does not look for the existing chat ticket.** It makes a second ticket.
   - So far there is **1 case**: Khushboo Yadav (…946554242, Self - Web Chat), with chat ticket **1414892** and Lead Ticket **1415338**. Both are under the same Desk contact and both are with Krishna.
   - The risk is much larger than one case. **47 SIB-04 WhatsApp leads already have a chat ticket.** If an RM presses Create Ticket on any of them, they get a second ticket. Where the lead has no email, they also get a second Desk contact.

**The bigger problem is assignment, not duplicates:**
- Of the **58 chat tickets that belong to SIB-04 leads, 49 are unassigned**.
- **None** of those leads has the chat ticket number in Lead Ticket (RM_Lead_Ticket).
- The owner-transfer function never finds these tickets, because it searches Desk **by email only**, and WhatsApp chat contacts have a phone number but no email.

## 2. How tickets are made today

| Path | Created by | Channel / subject | Assignee | Written to CRM? |
|---|---|---|---|---|
| **Chat ticket** | SalesIQ → Desk integration, one per chat session (54 offline, 32 online, 1 feedback in the window) | Chat / "Sales Inquiry (…) — name" | Usually none. Online chats sometimes get the operator. | **No.** RM_Lead_Ticket stays empty. |
| **Lead Ticket** | CRM workflow "Create Desk Ticket From Lead" (1123581000899715293) → function `create_desk_ticket_from_lead` (35880000003620001), when Create_Ticket = Yes and RM_Lead_Ticket is empty | Web / "L<Lead_Number> - name - product" | The user who triggered it, falling back to the owner | **Yes.** The ticket number goes into RM_Lead_Ticket. |
| Owner transfer | Workflow "Transfer Desk Tickets To Lead Owner" (1123581000912769323) → `transferdeskticketstoleadowner` (35880000003681001). Fires on any change to Owner, Refresh or Lead_Status, when Duplicate_Status ≠ Yes. | — | Moves tickets to the owner's Desk agent | Finds tickets **by email only** |
| Also present | `updatedeskticketownerfromlead` (35880000003679001): also email only. "Leads_ZohoFlow_Create Contact in Desk From Lead" (1123581000896072001): webhook on edit. | | | |

**Code defects behind the problem** (read 13 Oct; code not yet backed up to the project):
- `transferdeskticketstoleadowner` builds its search list from Email and Secondary_Email, then looks up the Desk contact by email. If the lead has no email, it does nothing. It never uses Phone or RM_Lead_Ticket.
- `create_desk_ticket_from_lead` looks up the Desk contact by email only. If there is no match, it creates a new contact and a new Web ticket. It never checks for an open chat ticket on the same phone.

## 3. Numbers (read-only checks R137–R142)

| Ref | Check | Result |
|---|---|---|
| R137 | COQL: SIB-04 leads with Lead_Source "Advt - WhatsApp" | **127 leads.** 4 have RM_Lead_Ticket (…946463144 → 1414594, …946586082 → 1414670, …946442337 → 1415955, …946420529 → 1415780). None of those 4 has a chat ticket. Only 7 of the 127 have an email. |
| R138 | Desk: channel = Chat in the window | **87 tickets** (54 OFFLINE_CHAT, 32 ONLINE_CHAT, 1 FEEDBACK). 57 unassigned. 80 distinct phones. 7 phones have 2 tickets. |
| R139 | Matched the 80 phones to CRM leads (COQL `Phone in (…)`) | **85 ticket–lead pairs.** 58 tickets ↔ **54 SIB-04 leads** (47 WhatsApp + 7 form leads who also chatted). 27 tickets ↔ 24 other leads (mostly Self - Web Chat). 2 tickets have no lead (1414883 +919919001970, 1415687 +918961995011). |
| R140 | Desk: channel = Web, subject "L48*" in the window (CRM Lead Tickets) | **214 tickets.** Phone overlap with chat tickets: **1** (Khushboo Yadav, 1414892 + 1415338). |
| R141 | Read the 3 functions and 4 Leads workflow rules (section 2) | As in section 2 |
| R142 | Tool behaviour | Desk `searchContacts` by phone works only with the exact "+91…" form (Rachna +918949373250 → contact 293676000532948712). Wildcard, `_all` and ticket search by phone return 204. |

SIB-04 WhatsApp leads by ticket state:

| State | Leads |
|---|---|
| Chat ticket | 47 |
| Lead Ticket only | 4 |
| **No Desk ticket at all** | **76** |

Phone is the only key that joins CRM, SalesIQ and Desk for these leads.

## 4. Dry run: SIB-04 backfill (T1 + T2), 54 leads / 58 tickets

**Proposed rule:**
- RM_Lead_Ticket = the lead's **first** chat ticket number (plain digits, no "#").
- Assign each ticket to the lead owner's Desk agent.
- Skip leads parked on Lost Records, on the admin user, or on the disabled user.

| Action | Tickets |
|---|---|
| Assign to owner | 44 (42 leads; includes 2 second-session tickets, and 2 waiting until Yadav and Bisht are confirmed as Desk agents) |
| Already with the owner | 3 (1414488 Tarun, 1414786 and 1414787 Priyam) |
| Hold: owner Gaurav is disabled | 2 (1414780, 1414801) |
| Decide: lead marked Duplicate_Status = Yes (Hafeez) | 2 (1414789, 1414796) |
| Skip: owner is Lost Records | 6 |
| Skip: stays on admin (Virendra Sharma) | 1 (1414880) |

RM_Lead_Ticket writes: **54** (it is safe to link even the skipped ones).

| # | Lead (…id) | Source | Owner | Chat ticket(s) | Now assigned | RM_Lead_Ticket → | Ticket action |
|---|---|---|---|---|---|---|---|
| 1 | …946442225 | WhatsApp | Tarun | 1414488 | Tarun | 1414488 | 1414488: none (already owner) |
| 2 | …946345169 | WhatsApp | Gaurav(disabled) | 1414780 | Gaurav | 1414780 | 1414780: hold: owner disabled, needs new owner |
| 3 | …946586137 | WhatsApp | Priyam | 1414786 | Priyam | 1414786 | 1414786: none (already owner) |
| 4 | …946590181 | WhatsApp | Priyam | 1414787 | Priyam | 1414787 | 1414787: none (already owner) |
| 5 | …946586197 | Facebook | Anish | 1414789, 1414796 | UNASSIGNED, UNASSIGNED | 1414789 | 1414789: decide: lead is Duplicate_Status = Yes<br>1414796: decide: lead is Duplicate_Status = Yes; second chat session: merge into 1414789 |
| 6 | …946532152 | WhatsApp | Anish | 1414791 | UNASSIGNED | 1414791 | 1414791: assign to Anish |
| 7 | …946554177 | WhatsApp | Aman Raj | 1414792 | UNASSIGNED | 1414792 | 1414792: assign to Aman Raj |
| 8 | …946520407 | WhatsApp | Gaurav(disabled) | 1414801 | UNASSIGNED | 1414801 | 1414801: hold: owner disabled, needs new owner |
| 9 | …946520431 | WhatsApp | Lost Records | 1414825 | UNASSIGNED | 1414825 | 1414825: skip: parked on Lost Records |
| 10 | …946574255 | WhatsApp | Tarun | 1414835 | UNASSIGNED | 1414835 | 1414835: assign to Tarun |
| 11 | …946532212 | WhatsApp | Lost Records | 1414855 | Sanjeev | 1414855 | 1414855: skip: parked on Lost Records |
| 12 | …946574293 | Facebook | Anish | 1414859 | UNASSIGNED | 1414859 | 1414859: assign to Anish |
| 13 | …946463283 | WhatsApp | Lost Records | 1414860 | Priyanka | 1414860 | 1414860: skip: parked on Lost Records |
| 14 | …946532260 | WhatsApp | Anish | 1414862 | UNASSIGNED | 1414862 | 1414862: assign to Anish |
| 15 | …946345256 | WhatsApp | Praveen | 1414863 | UNASSIGNED | 1414863 | 1414863: assign to Praveen |
| 16 | …946543235 | WhatsApp | Anish | 1414865 | UNASSIGNED | 1414865 | 1414865: assign to Anish |
| 17 | …946564200 | WhatsApp | Tarun | 1414866 | UNASSIGNED | 1414866 | 1414866: assign to Tarun |
| 18 | …946532284 | WhatsApp | Rishika | 1414867 | UNASSIGNED | 1414867 | 1414867: assign to Rishika |
| 19 | …946420286 | WhatsApp | Anish | 1414868 | UNASSIGNED | 1414868 | 1414868: assign to Anish |
| 20 | …946549288 | WhatsApp | Tarun | 1414870 | UNASSIGNED | 1414870 | 1414870: assign to Tarun |
| 21 | …946568358 | WhatsApp | Pragya | 1414872 | UNASSIGNED | 1414872 | 1414872: assign to Pragya |
| 22 | …946520482 | Facebook | Praveen | 1414874 | UNASSIGNED | 1414874 | 1414874: assign to Praveen |
| 23 | …946489273 | WhatsApp | Pragya | 1414878 | UNASSIGNED | 1414878 | 1414878: assign to Pragya |
| 24 | …946567286 | Facebook | Sanjeev | 1414880 | UNASSIGNED | 1414880 | 1414880: skip: stays on admin |
| 25 | …946549314 | WhatsApp | Anish | 1414882 | UNASSIGNED | 1414882 | 1414882: assign to Anish |
| 26 | …946493238 | Facebook | Mahima | 1414884 | UNASSIGNED | 1414884 | 1414884: assign to Mahima |
| 27 | …946566271 | WhatsApp | Tarun | 1414885 | UNASSIGNED | 1414885 | 1414885: assign to Tarun |
| 28 | …946435157 | WhatsApp | Anish | 1414886, 1414909 | UNASSIGNED, UNASSIGNED | 1414886 | 1414886: assign to Anish<br>1414909: assign to Anish; second chat session: merge into 1414886 |
| 29 | …946564254 | WhatsApp | Rishika | 1414887 | UNASSIGNED | 1414887 | 1414887: assign to Rishika |
| 30 | …946493326 | WhatsApp | Amit Kumar 3 | 1414902, 1414905 | UNASSIGNED, UNASSIGNED | 1414902 | 1414902: assign to Amit Kumar 3<br>1414905: assign to Amit Kumar 3; second chat session: merge into 1414902 |
| 31 | …946549338 | WhatsApp | Pragya | 1414903 | UNASSIGNED | 1414903 | 1414903: assign to Pragya |
| 32 | …946427283 | WhatsApp | Praveen | 1414906 | UNASSIGNED | 1414906 | 1414906: assign to Praveen |
| 33 | …946420324 | WhatsApp | Mahima | 1414911 | UNASSIGNED | 1414911 | 1414911: assign to Mahima |
| 34 | …946435191 | WhatsApp | Rishika | 1414914 | UNASSIGNED | 1414914 | 1414914: assign to Rishika |
| 35 | …946400342 | WhatsApp | Tarun | 1414915 | UNASSIGNED | 1414915 | 1414915: assign to Tarun |
| 36 | …946575232 | Facebook | Sudip | 1414917 | UNASSIGNED | 1414917 | 1414917: assign to Sudip |
| 37 | …946345208 | WhatsApp | Pragya | 1415137 | Sanjeev | 1415137 | 1415137: assign to Pragya (now Sanjeev) |
| 38 | …946575411 | WhatsApp | Pragya | 1415344 | UNASSIGNED | 1415344 | 1415344: assign to Pragya |
| 39 | …946493599 | WhatsApp | Praveen | 1415354 | UNASSIGNED | 1415354 | 1415354: assign to Praveen |
| 40 | …946442754 | WhatsApp | Krishna | 1415414 | UNASSIGNED | 1415414 | 1415414: assign to Krishna |
| 41 | …946574661 | WhatsApp | Rishika | 1415415 | UNASSIGNED | 1415415 | 1415415: assign to Rishika |
| 42 | …946575496 | WhatsApp | Lost Records | 1415416, 1415810 | UNASSIGNED, Swati | 1415416 | 1415416: skip: parked on Lost Records<br>1415810: skip: parked on Lost Records; second chat session: merge into 1415416 |
| 43 | …946520858 | WhatsApp | Yadav | 1415437 | UNASSIGNED | 1415437 | 1415437: assign to Yadav once Desk agent confirmed |
| 44 | …946575520 | WhatsApp | Amit Kumar 3 | 1415438 | UNASSIGNED | 1415438 | 1415438: assign to Amit Kumar 3 |
| 45 | …946494707 | WhatsApp | Amit Kumar 3 | 1415441 | UNASSIGNED | 1415441 | 1415441: assign to Amit Kumar 3 |
| 46 | …946613511 | Facebook | Rishika | 1415444 | UNASSIGNED | 1415444 | 1415444: assign to Rishika |
| 47 | …946586565 | WhatsApp | Bisht | 1415445 | UNASSIGNED | 1415445 | 1415445: assign to Bisht once Desk agent confirmed |
| 48 | …946575570 | WhatsApp | Anish | 1415447 | UNASSIGNED | 1415447 | 1415447: assign to Anish |
| 49 | …946435461 | WhatsApp | Tarun | 1415448 | UNASSIGNED | 1415448 | 1415448: assign to Tarun |
| 50 | …946575596 | WhatsApp | Mahima | 1415453 | UNASSIGNED | 1415453 | 1415453: assign to Mahima |
| 51 | …946345542 | WhatsApp | Anish | 1415457 | UNASSIGNED | 1415457 | 1415457: assign to Anish |
| 52 | …946420579 | WhatsApp | Mahima | 1415470 | UNASSIGNED | 1415470 | 1415470: assign to Mahima |
| 53 | …946543594 | WhatsApp | Tarun | 1415471 | UNASSIGNED | 1415471 | 1415471: assign to Tarun |
| 54 | …946538530 | WhatsApp | Lost Records | 1415560 | Shaily | 1415560 | 1415560: skip: parked on Lost Records |

### Other chat leads (phase 2, not proposed yet): 24 leads, 27 tickets

| Chat ticket | Lead (…id) | Source | Owner | Now assigned | Thread |
|---|---|---|---|---|---|
| 1414243 | …946493001 | Self - Web Chat | Mahima | Mahima | OFFLINE_CHAT |
| 1414290 | …945961039 | Advt - ChatGPT | Priyam | Swati | ONLINE_CHAT |
| 1414565 | …945961063 | Self - Web Chat | Tarun | Swati | ONLINE_CHAT |
| 1414783 | …946442201 | Self - Web Chat | Praveen | UNASSIGNED | OFFLINE_CHAT |
| 1414794 | …741843105 | Advt - Facebook | 805919001 | UNASSIGNED | OFFLINE_CHAT |
| 1414795 | …741813001 | SEO - Google | Alerts | UNASSIGNED | OFFLINE_CHAT |
| 1414842 | …946429391 | Self - Web Chat | Krishna | UNASSIGNED | OFFLINE_CHAT |
| 1414858 | …946532236 | Self - Web Chat | Sudip | Sudip | OFFLINE_CHAT |
| 1414869 | …946532236 | Self - Web Chat | Sudip | Sudip | ONLINE_CHAT |
| 1414873 | …946517070 | Self - Cold Call | Tomar | Arjit | ONLINE_CHAT |
| 1414879 | …946567253 | Self - Web Chat | Singh 340174041 | Jitendra | ONLINE_CHAT |
| 1414881 | …946553356 | Self - Web Chat | Anish | UNASSIGNED | OFFLINE_CHAT |
| 1414892 | …946554242 | Self - Web Chat | Krishna | Krishna | ONLINE_CHAT |
| 1415025 | …946586415 | Self - Web Chat | Lost Records | Krishna | ONLINE_CHAT |
| 1415108 | …946429391 | Self - Web Chat | Krishna | Krishna | ONLINE_CHAT |
| 1415197 | …946463485 | Self - Web Chat | Lost Records | Krishna | ONLINE_CHAT |
| 1415199 | …946549464 | Self - Web Chat | Lost Records | Priyanka | ONLINE_CHAT |
| 1415462 | …946568660 | Self - Web Chat | Tarun | UNASSIGNED | OFFLINE_CHAT |
| 1415468 | …946488420 | Self - Web Chat | Tarun | UNASSIGNED | OFFLINE_CHAT |
| 1415540 | …933055659 | Social - WhatsApp | Priyam | Pavneet | ONLINE_CHAT |
| 1415686 | …946420746 | Self - Web Chat | Lost Records | Priyanka | FEEDBACK |
| 1415755 | …946586415 | Self - Web Chat | Lost Records | Priyanka | ONLINE_CHAT |
| 1415790 | …946477046 | Advt - ChatGPT | Lost Records | Shaily | ONLINE_CHAT |
| 1415812 | …943975226 | Self - Cold Call | Vishwakarma | Swati | ONLINE_CHAT |
| 1415813 | …947159009 | Self - Web Chat | Amit Kumar 3 | Amit | ONLINE_CHAT |
| 1415829 | …946568823 | Self - Web Chat | Lost Records | Pavneet | ONLINE_CHAT |
| 1415894 | …946463240 | Self - Web Chat | Anish | Priyanka | ONLINE_CHAT |

In these 24 leads, Krishna's (…946429391) and Sudip's (…946532236) each have 2 chat tickets. Khushboo Yadav (…946554242) is the one CRM double (chat 1414892 + Lead Ticket 1415338).

## 5. Proposed changes, in order (each needs Sanjeev's OK)

**T1. Backfill RM_Lead_Ticket**
- Scope: 54 SIB-04 leads.
- Method: CRM connector `updateRecords` on Leads, with `trigger: []`, in batches of 100 or fewer.
- Value: the first chat ticket number.
- Re-run the R138/R139 match first, because new chats arrive every hour.
- Afterwards, verify by COQL.

**T2. Assign the chat tickets to the lead owner**
- Scope: 42 leads (44 tickets until T3 is decided).
- Method: Desk `updateTicket`, setting `assigneeId` to the owner's Desk agent. Match the CRM user's email to the agent's emailId, the same way the existing functions do.
- Desk sends the agent an assignment notification: expected.
- Hold, skip and decide cases are as in the table above.

**T3. Second-session duplicates**
- Scope: 4 SIB-04 pairs plus 3 others.
- Sanjeev chooses one of: merge into the first ticket in Desk (ticket › More › Merge), close as duplicate, or leave as is.
- The connector has no merge tool, and a merge can't be undone. So Sanjeev does it in Desk, or approves each browser click.

**T4. New scheduled CRM function `sib_chat_ticket_link`** (code to be shown before saving)
- Runs every hour.
- Picks leads created in the last 7 days where RM_Lead_Ticket is empty and Phone is not empty. Sources: "Advt - WhatsApp", "Self - Web Chat", and SIB paid form leads.
- For each lead:
  1. Look up the Desk contact by exact Phone.
  2. Take the newest open Chat ticket.
  3. Write its number to RM_Lead_Ticket with `trigger: []`.
  4. If the owner is a live user who isn't on the skip list, assign the ticket to the owner's Desk agent.
- Writes a log line for each lead.
- Why a sweep: the chat ticket is created when the chat ends, usually 10–60 minutes **after** the lead, so a create-time workflow would miss it.

**T5. Patch `transferdeskticketstoleadowner`** (diff to be shown before saving)
- If RM_Lead_Ticket is set, fetch that ticket and assign it.
- Also look up the Desk contact by Phone (exact "+91…") as well as by email, and move all of that contact's open tickets.
- Keep the Duplicate_Status guard.

**T6. Patch `create_desk_ticket_from_lead`** (diff to be shown before saving)
- If the lead has no email match, look up the contact by Phone before creating a new one.
- If that contact has an open Chat ticket, write that ticket's number to RM_Lead_Ticket and assign it, instead of creating a second ticket.

**T7. SalesIQ check (read-only first)**
- Settings › Integrations › Zoho Desk: record which chats create tickets (missed, offline, all), and whether there is an option to add a new chat to the person's open ticket.
- Report the findings. Change nothing without OK.

**Decisions for Sanjeev**
- New owners for Gaurav's 3 SIB-04 leads. 2 of them have chat tickets.
- Whether to assign Hafeez's tickets (lead is Duplicate_Status = Yes).
- Whether to include phase 2 (the 24 non-SIB-04 chat leads).
- What to do about the 76 SIB-04 WhatsApp leads with no ticket. **Recommendation:** no mass creation. RMs press Create Ticket once a lead is qualified, after T6 is live so no doubles are made.

## 6. Decisions and handoff (13 Oct 2026, 20:08 IST)

**Sanjeev's decisions**
- Include the website chat leads (phase 2: 24 leads, 27 tickets).
- No Desk ticket is to be created for leads that don't have one.
- The ticketing fix moves to the **SalesIQ Tiya project**, which holds the history of the SalesIQ→Desk integration, the Zoho Flows, Desk dedup and the ops task.

**Handoff**
- The prompt for that project is `Meta Ads/Tiya_Project_Prompt_Chat_Tickets_2026-10-13.md`.
- The data file is `Chat_Tickets_DryRun_2026-10-13.csv`: 85 ticket–lead pairs with a proposed action for each. It was sent to Sanjeev to attach there.

**Extra read-only checks (R143–R144)**
- **R143.** Desk contact 293676000532544128 (WhatsApp, phone only): `zohoCRMContact` = null, owner Sanjeev. Khushboo Yadav's contact 293676000532636103 (has an email): `zohoCRMContact` = lead …946554242, owner is a sales agent. So for phone-only chat contacts, the Desk↔CRM link is missing.
- **R144.** The scheduled task "Setindiabiz Ops — Tiya + Desk + CRM" (every 3 h at :15 UTC) already matches chat leads to chat tickets by phone. But its allowed writes exclude RM_Lead_Ticket and ticket assignment.
- Also from R144: the CRM owner-change triggers fire at chat **start**. The chat ticket is only created at chat **end**. So nothing fires after the ticket exists.

**No changes made in this project.** T1–T7 above are now for the Tiya project to confirm or replace.
