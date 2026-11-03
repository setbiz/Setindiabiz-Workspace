You are continuing two Setindiabiz Meta jobs in the "Meta Ads - Optimisation" project:
- **SIB-05 India Entry (FDI Services)** is being built. This is the main job for this session.
- **SIB-04 Company Annual Filings** is live and needs daily checks only.

Zoho CRM is crm.zoho.com (US DC, org 36264019). The Meta account is SETINDIABIZ 152154124583473. Meta tool calls use client_model "claude-opus-5-5".

## Read first (project docs)

**SIB-05**
- `Meta Ads/SIB-05_Resume_Prompt_2026-10-12_G11.md`: G9 checklist, G11–G13 steps, browser notes. Still valid; this prompt only updates it.
- `Meta Ads/Change_Log_2026-10-12_SIB-05-G11-review.md`: R117–R128 and open items 1–8.
- `Meta Ads/SIB-05_G11_Creative_Copy_and_Claims_Review_2026-10-12.md`: decisions A–E, revised copy for the six ads, designer brief.
- `Meta Ads/SIB-05_India_Entry_Build_Spec_2026-10-10.md` (v4).

**SIB-04 (13 Oct)**
- `Meta Ads/SIB-04_Scorecard_2026-10-13.md`
- `Meta Ads/Change_Log_2026-10-13_Placement-Controls.md`: stop-loss and the 18:31 propagation check.
- `Meta Ads/Change_Log_2026-10-13_SIB-04-LG11.md`: Support-first bot V5.
- `Meta Ads/Change_Log_2026-10-13_CAPI-Sweep-v2.md` and `Meta Ads/Change_Log_2026-10-13_Duplicate-Detector.md`
- `Meta Ads/SIB-04_Agent_Investigation_2026-10-13.md`: Swati's tracker and the Lost Records trace.

## State at 13 Oct 2026, 18:45 IST

**SIB-05 has not changed since 12 Oct 14:15.**
- G9: still 0 leads on "SIB-05 India Entry Form v1" (checked 13 Oct 18:40). The three test leads have not been submitted.
- G11: decisions A–E are still with Sanjeev. Nothing has changed in Canva.
- G12 and G13 have not started.

**What changed on 13 Oct that affects SIB-05**
1. **Placement exclusions now apply account-wide, including SIB-05** (set about 12:30). Excluded: Audience Network (all positions), FB Marketplace and FB right column. Don't add them back at ad-set level. In-stream, Reels overlay, Search and Notifications cannot be excluded this way.
2. **CAPI sweep v2** (`sib_capisweep`, runs every 2 hours) sends ValidLead/QualifiedLead for Lead_Source "Advt - Facebook", "Advt - Instagram" and "Advt - WhatsApp".
   - SIB-05 leads are sent only if their Lead Source is one of these.
   - Testing-tool leads arrive as "Direct", so they are not sent, which is right for tests.
   - Once live, confirm real SIB-05 form leads get "Advt - Facebook" or "Advt - Instagram".
3. **Duplicate detector v2:** leads whose Lead Source starts with "Advt - " keep their owner when a duplicate is found; they only get a note. Other leads still move to the admin account. In G9, a "Direct" test lead that matches an existing record will still move to admin. That is expected, not a fault.
4. **SIB-04 chat model changed** (Sanjeev, 13 Oct 16:25). Every WhatsApp chat goes to Customer Support first. Support engages the customer and transfers the chat to the sales owner once the lead is assigned. Bot "Tiya - Annual Filings" V5 went live at 16:44 and the first live chat passed.
   - **Ask Sanjeev before G12** whether SIB-05's WhatsApp button should follow the same Support-first model instead of the G3c routing to the five handlers (C82–C84).
   - Don't change G3c without his answer.
5. **Lessons from SIB-04 for the SIB-05 handler briefing:**
   - Calls are not logged in CRM, so only notes count as evidence.
   - Customers who start on WhatsApp must get a reply inside that chat, not only a phone call.
   - Grading RM Lead Quality is what feeds Meta through CAPI.
   - Support parks spam on "Lost Records" (…117753968) and leaves the status blank. Spam should be closed as Lost with reason "Bot Created/Spam".

**SIB-04 on 13 Oct** (from the scorecard)

| | CTWA | Form | Total |
|---|---|---|---|
| Spend | ₹13,774 | ₹8,672 | ₹22,446 |
| Leads | 123 | 22 | 145 |
| Valid | 32 | 5 | 37 |
| Cost per valid | ₹430 | ₹1,734 | ₹607 |

Also: 4 progressed, 0 deals. 30 lost, of which 19 were "Inquired by Mistake".

## Next, in order

1. **SIB-04 morning checks (read-only)**
   - **a. Placements.** Full-day 14 Oct spend on Audience Network and Marketplace should be ₹0 for ad sets 120246968316940449 (CTWA) and 120246968737470449 (Form).
     - On 13 Oct, ₹11.72 of AN spend leaked after the change, most likely propagation lag.
     - If AN is above ₹0 on 14 Oct, ask Sanjeev to confirm that Advertising settings › Placement controls still shows the 4 exclusions as "Defined".
     - Append the result to the Placement-Controls log.
   - **b. Scorecard and speed-to-lead list.** Use the method in the 13 Oct scorecard. The paid segment is Lead_Source "Advt - WhatsApp", "Advt - Facebook" or "Advt - Instagram" with Meta_Campaign "SIB-04 Annual Filings".
   - **c. CAPI sweep.** Confirm it ran every 2 hours and that the count of Meta_CAPI_Sent = true is rising.
2. **SIB-05 G9**, as soon as Sanjeev says the test leads are in. Use the checklist in step 1 of the 12 Oct G11 resume prompt. Add one check: on the WhatsApp-button phone test, confirm the routing matches Sanjeev's answer to point 4 above.
3. **SIB-05 G11**
   - Get Sanjeev's decisions A–E, update the claims review, and finalise the designer brief.
   - When images arrive, review every on-image claim before G12.
   - Try again to open Press Note 2 (2026) and S.O. 2174(E) / 3030(E) on a government site.
   - Add S.O. 3030(E) to spec section 1 and to the section 8 legal stop.
4. **SIB-05 G12** on Sanjeev's go:
   - Create campaign "SIB-05 India Entry" switched OFF.
   - Build 3 ad sets per spec section 3, then the 6 ads, and a preview pack.

   **G13:** Sanjeev publishes.
5. **Dated SIB-04 items**
   - **15 Oct (Thu): Swati's tracker is due:** https://docs.google.com/spreadsheets/d/1zEdc9Ey6vxMH7d1cUssW7yj8DOxH5SeEg9ZDKzNnSRw/edit
     - Read it and roll the root causes into the loss-bucket diagnosis (sales-process bucket).
     - List every lead marked "CRM updated? = No" and every row left blank.
   - **17 Oct morning: placement stop-loss review.** Compare 14–16 Oct cost per CRM valid lead against the thresholds (CTWA ₹662, campaign ₹914). The method is in the Placement-Controls log.
   - **28 Oct:** MGT-7 creative.
   - **31 Oct:** propose pausing the ads that quote 30 Oct (C1, C5, LLP-C1). Keep watching MCA circulars.
6. **Pending Sanjeev decisions.** Raise each once; don't push.
   - **Spam auto-close workflow:** when Product becomes "Spam Junk Promo and Competitor", set Lead_Status to Lost and Why_Disqualified to "Bot Created/Spam" if it is empty. Optionally, a dry-run clean-up of the ~139 parked spam leads with blank status.
   - **Lead "."** (1123581000946463283): Pavneet marked it spam with no evidence. Swati is checking.
   - **Untagged lead Srinivas Poojary** (…946435741): still to be checked and tagged.
   - **Watchdog filters:** add "Advt - WhatsApp" to the watchdog and scorecard paid-segment filters. This is a desktop-only step.
   - **Virendra Sharma** (1123581000946567286) stays on the admin account by Sanjeev's choice. No action.

## Owner IDs
COQL returns surnames only. Every ID below has the prefix 1123581000.

| ID | Name |
|---|---|
| 900978001 | Priyam Tiwari |
| 898222001 | Tarun Kumar |
| 900455002 | Amit Kumar 3 |
| 899805001 | Mahima Sehrawat |
| 900792006 | Gaurav Pandey |
| 057363001 | Sudip Manna |
| 893487006 | Krishna Gupta |
| 037468001 | Shubendu Banerjee |
| 012023007 | Suman Khowal |
| 904230019 | Anish Singh |
| 005632013 | Praveen Singh |
| 754062001 | Rishika Singh |
| 744835001 | Pragya Agrawal |
| 757738001 | Pavneet Kaur |
| 033869514 | Foziya Ansari |
| 458244001 | Karishma Singh |
| 245845885 | Swati Dhoundiyal (Support) |
| 117753968 | "[customer name redacted] Lost Records" |
| 006825001 | Sanjeev Kumar (admin) |

## Hard rules

- **Meta.** Never activate or publish a Meta campaign. Never move money, never top up, never enter passwords, never call ads_activate_entity.
- **Changes.** Any pause, budget, audience, placement or creative change needs Sanjeev's explicit approval. Make one change at a time, with before/after evidence and a logged stop-loss.
- **Copy.** Ad copy, on-image text and website text need Sanjeev's OK on the exact text.
- **Code.** Show code, a diff or the exact text before saving any production function, template or workflow.
- **CRM edits with the connector:**
  - Pass `trigger: []` and skip assignment rules.
  - Mass writes need a dry run and approval.
  - Don't delete CRM records.
  - Don't edit the 11 older LeadChain chains.
- **Emails and messages on Sanjeev's behalf.** Draft first, confirm the recipient, and send only on his yes. The Gmail connection sends from one@setindiabiz.com; cc sanjeev@setindiabiz.com when he asks. Google Drive files are owned by sanjeev@setindiabiz.com.
- **SIB-05 claims.** Ads never say "100% FDI allowed", "no approval needed", "set up in X days" or "no need to visit India". No LLP ad may quote ₹100 a day as the filing fee. Quote government fees from the current rules only.
- **Browser.** If the browser permission check refuses a Setup page or a click, hand that step to Sanjeev.

## Tool notes

- **Meta connector**
  - Label read-only checks as read-only (advertiser_job "report_measure_or_look_up"). On 13 Oct, a breakdown read labelled with an old change request was blocked by the permission check.
  - A breakdown by publisher_platform × hour returns nothing.
- **Large CRM results**
  - Large COQL and timeline results are saved to files; parse them with Python.
  - getTimelines shows who changed a lead's owner and where the change came from (crm_ui, workflow or custom_function).
- **Browser:** the notes in the 12 Oct G11 resume prompt still apply.

## Output

End with a short report (done / open / who), a new dated change log, and the prompt for the session after.
