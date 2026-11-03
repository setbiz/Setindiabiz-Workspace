# SIB-04 paid leads: agent follow-up investigation (13 Oct 2026)

**Requested by:** Sanjeev, 17:32 IST. The ask was a report with lead details so that Swati can investigate and speak with each agent, emailed to Swati with Sanjeev in cc.

**Owner of the follow-up:** Swati Dhoundiyal (Support Team), swati.dhoundiyal@setindiabiz.com.

**Sent:** 13 Oct 2026, about 17:50 IST. It went from one@setindiabiz.com to Swati, with sanjeev@setindiabiz.com in cc. Gmail thread 1a13532c74089ddf.

**Tracker (Google Sheet):** https://docs.google.com/spreadsheets/d/1zEdc9Ey6vxMH7d1cUssW7yj8DOxH5SeEg9ZDKzNnSRw/edit
- The sheet is owned by Sanjeev, and Swati has edit access.
- It has three tabs: How to use, Agent Summary (live COUNTIFS formulas) and Leads to Investigate.

**Offline copy:** SIB-04_Lead_Followup_Investigation_2026-10-13.xlsx. It has a Notes Log tab with all 135 notes. It was sent to Sanjeev in the chat.

**Deadline given to Swati:** Thursday 15 Oct 2026.

## Scope
There are 28 leads from SIB-04 (Lead_Source Advt - WhatsApp, Facebook or Instagram), as of 17:35 IST. They fall into three groups:
- (A) Lead Status blank.
- (B) "Establishing Contact" for more than 48 hours with RM quality blank or "Still Evaluating".
- (C) Owner is "Lost Records".

Excluded: Virendra Sharma (…946567286), which stays on the admin account by Sanjeev's choice.

## Findings

| Issue | Leads | Who |
|---|---|---|
| No contact logged | 4 | Sudip 2, Praveen 1, Suman 1 |
| Worked, CRM not updated | 3 | Sudip (Founder Agreement), Gaurav (Section 8), Priyam (ROC + DIN reactivation) |
| Follow-up gap or slow first contact | 9 | Gaurav 3, Amit Kumar 3 3, Anish 2, Priyam 1 |
| Closed as "mistake", needs checking | 1 | Harish Kumar (Gaurav) |
| Invalid number not closed | 1 | Priyam |
| Marked spam, needs checking | 1 | "." (…946463283), parked by Pavneet |
| Spam not closed | 2 | social media promotion111, Znight (both on Lost Records) |
| Fresh, SLA check | 2 | Mahima, Anish |
| Good effort, close per rule | 5 | Krishna 1, Tarun 4 |

**Notes on specific leads**
- Harish Kumar: the customer shared files in the WhatsApp chat three times, including once after the "mistake" note.
- Priority split: P1 14, P2 8, P3 6.

## Patterns to fix
1. **Calls are not logged in CRM.** There are zero Call records on all 28 leads; notes are the only evidence of work.
2. **WhatsApp-origin leads are chased by phone only.** Chats were missed, and Support closed chats saying "lead is with X". The Support-first bot flow (V5, live about 16:44 on 13 Oct) addresses the closing.
3. **Ungraded leads never reach Meta.** The CAPI sweep sends only Valid or Progressed leads, so agent grading drives Meta learning.
4. **Phone format error (FIXED).** Lead …946613161 (A.V.R. Naidu) was stored as +19177944455.
   - It was corrected to +919177944455 at 17:51 IST on 13 Oct, with Sanjeev's approval.
   - The update ran with trigger [] and skipped assignment rules and cadences.
   - The Google Sheet row was updated to match.
5. **Spam parked on "Lost Records" without being closed.** This is not a routing bug (traced 13 Oct, 18:30; see below).

## Lost Records trace (13 Oct 2026, 18:30 IST)
Method: CRM timelines (getTimelines) for the 3 leads, plus COQL on all leads owned by "[customer name redacted] Lost Records" (…117753968) created since 13 Sep.

**How the three leads got there**
- All 3 were created by SalesIQ as "Self - Web Chat" with owner Pavneet Kaur. Pavneet moved them to Lost Records by hand in the CRM UI (source crm_ui), each time just after setting Product = "Spam Junk Promo and Competitor".
  - "." (…946463283): moved 13 Oct 10:51.
  - social media promotion111 (…946538530): moved 13 Oct 10:39.
  - Znight (…946575496): moved 13 Oct 15:59, from Priyam, after the visitor's second chat turned out to be an SEO agency pitch.
- No assignment rule, workflow or function set the owner to Lost Records.

**Why they appeared as paid leads**
- Claude's 13:57 backfill (trigger []) re-labelled them as Advt - WhatsApp, because each had a "Tiya - Annual Filings" chat note.
- The label is correct: they came in through the SIB-04 WhatsApp ad number.

**This is a team-wide convention**
- About 200 leads created since 13 Sep are owned by Lost Records: 139 with Product "Spam Junk Promo and Competitor" and 36 with "Job Seeker".
- 173 of the 200 have a blank Lead Status, so parked spam still counts as open.
- Two other SIB-04 WhatsApp leads (foujisarsar, NextGen) were parked the same way but closed correctly as Lost / Job Seeker.

**Verdicts**
- social media promotion111: confirmed spam (Shaily's note: "Promotional chat").
- Znight: confirmed spam; a vendor using the ad.
- ".": not supported by evidence. The only message is the Instagram ad's pre-filled text, the chat was missed, there is no note, and there is no Desk ticket or contact for [phone redacted]. Ask Pavneet what she saw; otherwise give it to an RM.

**Correct close for spam:** Lead_Status "Lost" with Why_Disqualified "Bot Created/Spam". This value exists but has been used only 5 times since 1 Jul.

**Sheet updated** (rows 26–28, 18:35 IST). Swati is now asked to check the "." spam call and to close the other two. She is no longer asked to chase a routing bug.

**Proposed (not applied, needs Sanjeev's go):**
- A CRM workflow on Leads: when Product becomes "Spam Junk Promo and Competitor", set Lead_Status = Lost and Why_Disqualified = "Bot Created/Spam" if it is empty.
- Optionally, a one-off clean-up of the ~139 parked spam leads with blank status (dry run first, trigger []).

## Compliance point given to Priyam (Ayush Kerkar)
The government fee for DIN reactivation is Rs 5,000. Sources:
- Companies (Registration Offices and Fees) Amendment Rules, 2026, in force 21 Apr 2026.
- Rule 12A, Companies (Appointment and Qualification of Directors) Rules, 2014.

KYC now runs on a 3-year cycle. A competitor's "Rs 2,000 including late fees" quote is therefore questionable if his DIN is deactivated.

## Next
- Review Swati's filled sheet on 15 Oct and roll the root causes into the loss-bucket diagnosis (sales-process bucket).
- Decide on the spam auto-close workflow and the clean-up.
