# SIB-04 LG-11 build — steps and status (13 Oct 2026)

Approved by Sanjeev on 13 Oct: "LG11 would work" and "Yes, build it". The four new agents were confirmed added at 12:39.

Claude's attempt to save a builder card (the A00 wait time) was blocked by the session's permission check ("Modify Shared Resources"). The edit was cancelled and nothing was saved; the bot is still V3, published 9 Oct. So bot and CRM-setting edits are done by Sanjeev from the steps below, and Claude checks them read-only afterwards.

## Verified read-only, 12:40–12:55

**CRM rule "PPC - SIB-04 Annual Filings - LG-11"** (1123581000945354238) has 14 users. Default when no one is online: Pavneet Kaur.

| User | Email |
|---|---|
| Praveen Singh | praveen@ |
| Suman Khowal | suman.khowal@ |
| Foziya Ansari | foziya.ansari@ |
| Shubendu Banerjee | shubendu.banerjee@ |
| Sudip Manna | sudip.manna@ |
| Himanshu Singh | himanshu.singh@ |
| Pragya Agrawal | pragya.agrawal@mail. |
| Rishika Singh | rishika.singh@mail. |
| Krishna Gupta | krishna.gupta@mail. |
| Tarun Kumar | tarun.kumar@mail. |
| Mahima Sehrawat | mahima.sehrawat@mail. |
| Amit Kumar 3 | amit.kumar3@mail. |
| Priyam Tiwari | priyam.tiwari@mail. |
| Anish Singh | anish.singh@mail. |

Gaurav Pandey is no longer in the rule.

**SalesIQ department "Sales - CACS ACR"** (61466000026678128) has 30 operators. All 14 LG-11 users are in it, including the 4 new agents.

**Bot "Tiya - Annual Filings"** (61466000026786012, V3 published 9 Oct). Flow today:
- A00 Welcome → A01 Entity → A02 Year → A04 CRM lead (plug) → A05 Route → A06 forward to owner, or A07 department.
- Counters: 146 chats reached A00; 66 answered A01; **79 left at the entity question**. Those chats never reached the CRM step, which is why about 82 chat leads stayed untagged "Self - Web Chat".
- **A05 has owner routes for only 10 people:** Pragya, Rishika, Tarun, Mahima, Anish, Amit Kumar 3, Priyam, Gaurav, Suman and Praveen.
- **No route exists for Krishna Gupta, Sudip Manna, Foziya Ansari, Himanshu Singh or Shubendu Banerjee.** When the lead goes to any of them, the chat falls to the department. That is a second source of chat/lead mismatch.

**Timing.** SalesIQ's own CRM push creates the lead about 2 seconds after the chat opens. For example, lead …566429 has a visit time of 10:13:32 and a created time of 10:13:34. If the CRM step runs immediately at chat start, it finds no lead and creates a second one. So the first card waits 5 seconds.

**CRM workflow "Lead Assignemnt - Edits"** (1123581000748082795):
- Trigger: Lead Assignment is modified (repeats every time).
- Condition: Lead Assignment is Auto.
- Actions: field update "Lead Assigned On", then Assign Owner by rule "Lead - General 2026".
- In that rule, entry 12 (Annual Filing / FB-ACR) still lists the old 10 users ("Pragya Agrawal & 9 More").

## Step 1 — Bot (Sanjeev). SalesIQ › Settings › Zobot › Tiya - Annual Filings › Codeless bot builder

**1a. A00 Welcome**
- Turn on **Card wait time = 5 Seconds**.
- Set the Info message to **One moment please ⏳**.
- Save.

**1b. New Plugs card "A03 CRM claim (start)"**
- Place it between A00 and A01: A00 → A03, and A03 Success → A01 and Failure → A01.
- Plug: **sib_wa_lead_1791383468657**.

| Input | Value |
|---|---|
| name | %visitor.name% |
| phone | %visitor.phone% |
| email | %visitor.email% |
| adcode | ACR |
| productid | 1123581000000185017 |
| campaign | SIB-04 Annual Filings |
| productcat | Annual Filing |
| ruleid | 1123581000945354238 |
| tag | FB-ACR |
| answers | Chat opened (before questions) |
| dryrun, clid | leave empty |

Outputs:

| Output | Store in |
|---|---|
| matched | wa_matched |
| status | wa_status |
| owneremail | wa_owneremail |
| recordid | wa_recordid |
| ownerid | wa_ownerid |
| ownername | wa_ownername |

**1c. A05 Route to CRM owner**
Add 5 rules of the form `wa_owneremail contains …`, each pointing to a new forward card:

| Rule value | New card |
|---|---|
| sudip.manna@ | A06 Forward to Sudip Manna |
| foziya.ansari@ | A06 Forward to Foziya Ansari |
| himanshu.singh@ | A06 Forward to Himanshu Singh |
| shubendu.banerjee@ | A06 Forward to Shubendu Banerjee |
| krishna.gupta@ | A06 Forward to Krishna Gupta |

**1d. Each new A06 card**
- Type Forward, department **Sales - CACS ACR**, **Transfer to selected operators** with that one person.
- Message: "Connecting you to <Name>, your Setindiabiz compliance expert ⏳".
- Offline hours, operators not available and invalid operators all go to **A07 Forward to Sales - CACS ACR**.

**1e. Leave as is**
- A04 cards: on the second call they find the claimed lead, add the answers as a note and return the owner for A05.
- A07 and A08.
- The Gaurav route: harmless, can be removed later.

**Known limitation:** an LLP chat keeps the company product ("ACR - Company Annual Return"), because the claim happens before the entity question. The LLP answer still arrives in the note. Fixing this needs a small plug code change, to be done later if wanted.

**1f. Don't publish yet.** Claude checks the draft read-only, then Sanjeev publishes and runs the test chat (step 4). Rollback: Versions › restore V3.

## Step 2 — CRM workflow "Lead Assignemnt - Edits" (Sanjeev)

**2a. Stop the re-run on WhatsApp leads.** In Condition 1, add criterion 2 **Lead Source is not Advt - WhatsApp**, with pattern (1 and 2). Pavneet's "Auto" then no longer moves a WhatsApp lead away from the owner who has the chat.

**2b. Recommended: give Pavneet's off-hours leads an LG-11 owner.** Add Condition 2 with three criteria:
- Lead Assignment is Auto
- Lead Source is Advt - WhatsApp
- Lead Owner is Pavneet Kaur

Its action: Assign Owner by rule **PPC - SIB-04 Annual Filings - LG-11**.

**Optional, Sanjeev's call:** add the 4 new agents to "Lead - General 2026" entry 12. That entry covers all Annual Filing leads, not just Meta.

## Step 3 — Backfill (Claude, after Sanjeev's go)

The dry run is in file `SIB-04_Backfill_DryRun_2026-10-13.csv`: **82 leads**.

**Selected:** Self - Web Chat leads with a "Zoho SalesIQ chat with Tiya - Annual Filings" note created since 9 Oct 21:35, with no Meta_Ad_Code.

**How the 135 chat-note leads break down:**

| Group | Count |
|---|---|
| Selected for backfill | 82 |
| Duplicates parked on admin (IIFA, SRIDHAR KUMAR KAMIDI, nayudu345, Jaswinder Ram) | 4 — left out |
| Created before the campaign (returning visitors from 2025) | 2 — left out |
| Already tagged Advt - WhatsApp | 38 |
| Form or SEO leads (7 Facebook, 1 Instagram, 1 SEO) | 9 |

The 2 Contacts with a chat note are left out as well.

**Write:**
- Fields set: Lead_Source "Advt - WhatsApp", Lead_Channel "Advt", Meta_Ad_Type "WhatsApp", Meta_Ad_Code "ACR", Meta_Campaign "SIB-04 Annual Filings".
- Tag FB-ACR is added (added, not replaced).
- trigger [] means no workflow, assignment or blueprint runs. Owners, statuses and products don't change, and nothing is sent to Meta.

**Profile of the 82:** 13 Valid, 44 Establishing Contact, 20 Lost, 5 empty. 4 are owned by "Lost Records".

## Step 4 — Test chat (Sanjeev's phone, after publish)

**Test A:** from a number that is not a client, send any message to [phone redacted] and don't answer the questions. Within about 10 seconds there should be one lead only:
- Lead_Source Advt - WhatsApp, Meta_Ad_Code ACR, Tag FB-ACR.
- Owner is an LG-11 user, or Pavneet if no one is online.

**Test B:** from a second number, answer both questions. Expect the same lead checks, plus:
- a note with the answers;
- the chat forwarded to that same owner.

**Fail →** restore V3 and report.
