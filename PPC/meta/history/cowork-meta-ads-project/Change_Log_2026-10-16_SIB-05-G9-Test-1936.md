# Change log: SIB-05 G9 test leads, first check (16 Oct 2026, 19:40 IST)

Read-only check. Nothing in CRM or Meta was changed.

## What arrived

Sanjeev said "tested" at 19:36. COQL `Meta_Lead_Form = 'SIB-05 India Entry Form v1'` returned 2 leads. Both were made with the testing tool's **"Create lead"** button, so every answer is Meta's dummy text, and email and phone are blank.

| Lead | ID | Created |
|---|---|---|
| L485184 | 1123581000949025246 | 19:28:00 |
| L485185 | 1123581000949072191 | 19:29:27 |

## Results

| Check | Result |
|---|---|
| Lead reaches CRM through LeadChain | ✔ Within about 1 second; Social Lead IDs 1955306015425995 and 1139734841948841 |
| Owner | ✔ Shubendu Banerjee, through assignment rule "PPC - SIB-05 India Entry - PG-02"; Reporting Manager Himanshu Sharma |
| Tag / Lead Channel | ✔ FB-FDI / Advt |
| Lead Source | ✔ "Direct", set by workflow "Auto-set Lead Source from URL". It is **not** "Meta Ads" |
| Product | ✔ FDI - Subsidiary Incorporation (the fallback, because the answer was dummy text); Product Category FDI, Report Cat FEMA. "Pull Product…" blanks Category and Report Cat; PPC Form Tidy restores them about 3 minutes later. This is the known pattern |
| Duplicate detector | ✔ Duplicate_Status = No |
| Description | Not testable. It holds the two dummy answers **with no ", " between them**; recheck with real answers |
| Select_Country / "Other" | Not testable (dummy text) |
| Branch office → BO-LO-PO routing | Not tested |
| Booking email "SIB-05 India Entry - booking email" | **Did not fire.** Expected, because the leads have no email address; still needs a real test |
| WhatsApp-button phone test | Not done. No WhatsApp or chat lead from the test after 19:15 |

## Guided retest, 20:08–21:15 (Sanjeev in his Chrome, Claude guiding)

- **20:26: Preview form lead** (Subsidiary, United States, Within 3 months). Sanjeev's saved Facebook details were kept: "Sanjeev Kumar", [phone redacted], sanjeev@setindiabiz.com.
  - Meta's testing tool showed delivery to app 191062257579887 (Zoho Social) with status **Success** at 20:27.
  - LeadChain chain "FB SIB-05 FDI v1" counted it (3 leads; last lead "Sanjeev Kumar", +919560900901, 20:26).
  - **No CRM lead was created**, and no existing Lead or Contact was updated.
  - [phone redacted] is already on two internal CRM Contacts ("Commitment Manager", "Tanveer Kaur"), and sanjeev@setindiabiz.com is on a Contact. The likely cause is LeadChain's duplicate handling or a CRM rule dropping it. **Not confirmed.** The LeadChain sync log is not visible, so this needs checking: a live lead whose phone or email is already in CRM may be dropped the same way.
- **WhatsApp button:** on the thank-you screen it opened chat with **[phone redacted]** (Sales), not [phone redacted] (the SIB-05 number in the spec).
  - The ads' follow-up settings were built with …508.
  - The testing tool may simply use the Page's default number.
  - Confirm on the first live lead before relying on D22 Support-first routing.
- **20:57:** Sanjeev deleted the test lead in the tool.
- **21:05 and 21:12:** two more Preview-form submissions (TEST SIB-05 1, personal email and mobile). The thank-you screen showed both times, but **Meta did not record either**:
  - the form still shows 3 untargeted leads;
  - the tool shows no "Track status";
  - LeadChain still counts 3;
  - no CRM lead.
  - Probably Meta does not record repeat submissions of the same form by the same Facebook user. Unconfirmed.
- **Day question raised by Sanjeev (20:14):** "When do you plan to start?" should offer shorter horizons ("this week, next week, next month").
  - Claude suggested: Within a month / 1 to 3 months / 3 to 6 months / Just exploring.
  - **Sanjeev has not chosen yet.**
  - Any change needs a new form v2: re-link the 6 ads, LeadChain (Sanjeev), the booking-email workflow, and a retest.

## Still needed for G9

- The three leads with **"Preview form"** and real answers (Subsidiary + United States; Branch office + Japan; Not sure yet + Other), each with a real email and phone.
- The WhatsApp button test from a phone.
- Vipin has the same steps (email 1a144b18c56deccf). Only one person should run them, because Meta allows one test lead per form at a time.
- The 2 dummy leads can be deleted from CRM by Sanjeev. Claude never deletes CRM records.

## Form v2 (16 Oct, 21:19–21:35)

- **Decision (Sanjeev, 21:19):** "When do you plan to start?" = Within a week / 1 to 3 weeks / 3 to 6 weeks / Just exploring for now.
  - Claude flagged that nothing fits a 2-to-3-month plan; there was no reply, so the four choices were used as given.
- **"SIB-05 India Entry Form v2", ID 1741840353557832.** Duplicated from v1 in the Ads Manager ad editor, in Sanjeev's Chrome.
  - Name and Q3 answers changed.
  - The duplicate came with flexible form delivery ON. Claude switched it OFF, as in v1.
  - Meta offered SMS verification and Messenger chat; both were declined.
  - Messenger follow-up stays unticked.
  - The WhatsApp button is **[phone redacted]**. The testing tool's [phone redacted] was the Page's default number, not the form's.
  - Sanjeev clicked "Create form" at about 21:26.
- **All six ads switched to v2** in the editor. Draft read-back at 21:33 shows `lead_gen_form_id` = 1741840353557832 on all six; nothing else changed on E2, S1, S2, B1 or B2.
- **Finding: part of the campaign was published at 19:26 IST.**
  - The campaign was created live at 13:56:45 UTC, with the India Entry ad set and ad E1. Ad sets Subsidiary and Branch-Liaison and the other five ads are still drafts.
  - Live status at 21:33: campaign, ad set and E1 all **PAUSED**, ₹0 spent, 0 impressions.
  - E1 is live on form v1; the switch to v2 waits as an unpublished edit.
  - The TM/INC WhatsApp drafts were not published.
  - Probably the Publish button in the Ads Manager tab left open on E1. Who clicked it is not confirmed.

## 21:32–22:03

- **PPC Form Tidy v1.3** (approved 21:32).
  - Live code checked first: it matched v1.2 (hash 6efc489899e092e4).
  - The permission check refused Claude's edit, both by editor script and by typing. Sanjeev typed `cfg.put("SIB-05 India Entry Form v2",c);` on line 36 and saved: revision 5, about 21:46.
  - Re-read in a fresh IDE tab: it matches the expected code (fee1e32320b6bc6a).
  - Copy saved as `ppc_form_tidy_v1.3_2026-10-16.deluge.txt`.
- **Booking-email workflow:** the permission check refused Claude searching the Workflow Rules page. Sanjeev parked the change at 22:03.
- **22:03:** Sanjeev parked SIB-05 and asked for a new session on junk leads (about 80% junk in the last 3–4 days). He also set the ACR audience rule: director customer data, FY 2025-26 and before, with age, gender and education safeguards as in CCFS. Kickoff prompt: `Lead_Quality_Junk_Fix_Resume_Prompt_2026-10-16.md`.

## Still to do for v2

1. LeadChain: point chain "FB SIB-05 FDI v1" at form v2, or clone it as "FB SIB-05 FDI v2". This is Sanjeev's step; Claude is refused LeadChain edits.
2. PPC Form Tidy: add a CONFIG entry for "SIB-05 India Entry Form v2". Needs Sanjeev's OK on the diff.
3. Booking-email workflow: the condition must cover v2. Needs Sanjeev's OK.
4. Retest on v2, by Vipin or from another Facebook account.
