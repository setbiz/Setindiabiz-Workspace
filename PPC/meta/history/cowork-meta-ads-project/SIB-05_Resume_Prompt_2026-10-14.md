You are continuing two Setindiabiz Meta jobs in the "Meta Ads - Optimisation" project:
- **SIB-05 India Entry (FDI Services)** is being built. This is the main job.
- **SIB-04 Company Annual Filings** is live and needs daily checks only.

**Order set by Sanjeev on 13 Oct (~19:54):**
1. Desk tickets for chat leads come first. Run `Meta Ads/Desk_Tickets_Resume_Prompt_2026-10-14.md` until T1–T7 are settled.
2. Then return to this prompt for SIB-05.
3. After SIB-05, plan the Incorporation (INC) and Trademark (TMF) campaigns. That prompt's step 5 lists what to read.

Zoho CRM is crm.zoho.com (US DC, org 36264019; Setup URLs use /crm/setindiabiz/). SalesIQ portal is salesiq.zoho.com/wwwsetindiabizcom/. The Meta account is SETINDIABIZ 152154124583473. Meta tool calls use client_model "claude-opus-5-5".

## Read first (project docs)

- `Meta Ads/Change_Log_2026-10-13_SIB-05-G11-Decisions.md`: R129–R136, C88–C90, open items 1–11. **Start here.**
- `Meta Ads/SIB-05_G11_Creative_Copy_and_Claims_Review_2026-10-12.md`: copy APPROVED 13 Oct; section 5 is the final designer brief.
- `Meta Ads/SIB-05_India_Entry_Build_Spec_2026-10-10.md` (**v5**): D21–D23, section 1 law (now with S.O. 3030(E) and S.O. 4870(E)), section 5 CRM/SalesIQ state, section 7 go list, section 8 legal stop.
- `Meta Ads/SIB-05_Resume_Prompt_2026-10-12_G11.md`: G12 steps and browser notes still apply.
- SIB-04: `Meta Ads/SIB-04_Scorecard_2026-10-13.md` (method), `Meta Ads/Change_Log_2026-10-13_Placement-Controls.md` (stop-loss), `Meta Ads/Change_Log_2026-10-13_CAPI-Sweep-v2.md`, `Meta Ads/SIB-04_Agent_Investigation_2026-10-13.md`.

## State at 13 Oct 2026, 19:07 IST

**SIB-05**
- **G11:** Sanjeev answered A–E and approved the exact copy and on-image text (~18:53). B: S1 adds "Registered office and a resident director are arranged separately." C: footer "Government fees extra, billed at cost." D: keep "CS & CA Experts" (FDI team has a qualified CS and CA). E: E1 CTA "Get a quote". **Brief emailed 19:32 to the designer Vipin Pathak (vipin.pathak@hatrotech.com), cc Sanjeev** (Gmail thread 1a1359139e2d73dc), with the Canva working set https://www.canva.com/d/O-YqiSOcjJszClW and folder PPC 2026 https://www.canva.com/folder/FAHXTwdMxJ4. The working set (DAHXTezZ4Nk) was moved into PPC 2026 at ~19:34 so Vipin can open it through the folder share (C92); if he reports view-only access, Sanjeev changes his permission on the folder in Canva. No design content changed. **Sizes changed at ~19:49 (follow-up on the same thread): 4:5 (1080×1350) for feed + 9:16 (1080×1920) for Stories/Reels, 12 images, no 1:1.** At G12, use the 4:5 image for feed placements and the 9:16 image for Stories/Reels (placement asset customisation).
- **Chat model (D22):** Support-first, as SIB-04. …508 channel department is **Customer Support**; SalesIQ rule C84 is **off** (kept).
- **PG-02 (D23):** Gaurav Pandey (user disabled 18:27) removed. Handlers: Foziya Ansari 033869514, Karishma Singh 458244001, Rishika Singh 754062001, Shubendu Banerjee 037468001; default Pavneet Kaur 757738001.
- **G9:** 0 leads on the form at 19:05. Waiting for Sanjeev to submit the three test leads.
- G12 and G13 not started.

**SIB-04 (13 Oct to 18:50, read-only)**
- Audience Network still trickled after the 12:30 exclusion: ₹423.34 today, +₹0.42 since 18:31. Marketplace stopped at ₹1.22. Form ad set clean.
- CAPI: 36 paid leads since 6 Oct marked sent; 2 graded valid at 18:46–18:47 (…946568358, …946574748) were waiting for the 20:00 run. A check was scheduled for 20:10 on 13 Oct; read its result in the change log or chat, and re-check if missing.
- Speed-to-lead: Sudip Manna's 3 form leads untouched (45–70 h); 21 leads > 48 h in Establishing Contact.
- Gaurav Pandey's 3 remaining SIB-04 leads (…946345169, …946520407, …946590157) sit on his disabled user.

## Next, in order

1. **SIB-04 morning checks (read-only)**
   - **a. Placements.** Full-day 14 Oct spend by publisher_platform × platform_position for ad sets 120246968316940449 (CTWA) and 120246968737470449 (Form). Pass = Audience Network ₹0 and Marketplace ₹0. If AN > ₹0, ask Sanjeev to confirm Advertising settings › Placement controls still shows the 4 exclusions as "Defined". Append the result to `Change_Log_2026-10-13_Placement-Controls.md` (read it, add the section, write the whole doc back).
   - **b. Scorecard and speed-to-lead for 13 Oct full day**, same method as the 13 Oct scorecard. Paid segment: Lead_Source "Advt - WhatsApp", "Advt - Facebook" or "Advt - Instagram" with Meta_Campaign "SIB-04 Annual Filings".
   - **c. CAPI sweep.** Confirm the 2 leads above were sent at 20:00 and that Meta_CAPI_Sent = true keeps rising; backlog query (valid or progressed, not sent) should hold only leads graded since the last even hour.
2. **SIB-05 G9**, as soon as Sanjeev says the test leads are in. COQL `Meta_Lead_Form = 'SIB-05 India Entry Form v1'`, then getRecord and getTimelines for each. Check:
   - owner is one of the four PG-02 handlers or Pavneet (default); a "Direct" test lead that duplicates an existing record may move to admin (…006825001): expected;
   - Tag FB-FDI; Lead Channel "Advt"; Lead Source "Direct";
   - Product and Product Cat after ~2 min (subsidiary / not sure → FDI - Subsidiary Incorporation / FDI; branch → Branch Office Registration of Foreign Company / BO-LO-PO);
   - Description "<Q1>, <Q3>"; Select_Country (record what "Other" does); Meta_* fields;
   - timeline shows workflow "SIB-05 India Entry - booking email"; Sanjeev confirms the email arrived with the owner's name;
   - **WhatsApp-button phone test: the chat lands with a Customer Support operator** (not the FDI handlers). Record whether SalesIQ creates a "Self - Web Chat" lead and whether the duplicate detector parks it on admin.
   Sanjeev deletes the test leads afterwards.
3. **SIB-05 G11**
   - Watch the Gmail thread 1a1359139e2d73dc for Vipin's reply or questions; any wording question goes to Sanjeev.
   - When images arrive, read each in Canva and check every on-image word against claims review section 5 before G12.
   - Retry the government copies: Press Note 2 (2026) on dpiit.gov.in (site loads in the built-in browser; Acts and Policies search found nothing — try Documents › Orders and Notices or Gazettes and Notifications) and S.O. 2174(E), 3030(E), 4870(E) on egazette.gov.in.
4. **SIB-05 G12** on Sanjeev's go after the image review: create campaign "SIB-05 India Entry" switched OFF; 3 ad sets per spec section 3; then the 6 ads (two per ad set) with the approved text exactly; Advantage+ creative enhancements off; preview pack. **G13:** Sanjeev publishes.
5. **Dated SIB-04 items**
   - **15 Oct:** Swati's tracker https://docs.google.com/spreadsheets/d/1zEdc9Ey6vxMH7d1cUssW7yj8DOxH5SeEg9ZDKzNnSRw/edit — roll root causes into the sales-process bucket; list every "CRM updated? = No" row and every blank row.
   - **17 Oct morning:** placement stop-loss review (14–16 Oct cost per CRM valid lead vs CTWA ₹662, campaign ₹914).
   - **28 Oct:** MGT-7 creative. **31 Oct:** propose pausing C1, C5, LLP-C1 (they quote 30 Oct). Keep watching MCA circulars.
6. **Pending Sanjeev decisions — raise each once, don't push:** spam auto-close workflow (+ optional dry-run clean-up of ~139 parked spam leads); lead "." (…946463283); untagged Srinivas Poojary (…946435741); add "Advt - WhatsApp" to the watchdog and scorecard filters (desktop step); new owners for Gaurav's 3 SIB-04 leads; substantiation for USD 499, 25,000+, CS & CA names. Virendra Sharma (…946567286) stays on admin.

## Owner IDs (prefix 1123581000; COQL returns surnames only)

| ID | Name |
|---|---|
| 900978001 | Priyam Tiwari |
| 898222001 | Tarun Kumar |
| 900455002 | Amit Kumar 3 |
| 899805001 | Mahima Sehrawat |
| 900792006 | Gaurav Pandey (**disabled 13 Oct**) |
| 807737001 | Aman Raj (Sales RM, reports to Himanshu Singh) |
| 807726001 | Shubham Kumar (Sales RM, reports to Himanshu Singh) |
| 778219001 | Shivam Chauhan (Sales RM, reports to Himanshu Singh) |
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

Others seen on SIB-04 leads, not yet resolved: …804800001 (Jain), …838091001 (Das), …340174041 (Singh), …879624001 (Singh), …919146001 (Yadav), …900716015 (Bisht).

LG-11 (SIB-04) has 14 users (read 13 Oct 19:05): Praveen Singh, Suman Khowal, Foziya Ansari, Shubendu Banerjee, Sudip Manna, Pragya Agrawal, Rishika Singh, Himanshu Singh, Krishna Gupta, Tarun Kumar, Mahima Sehrawat, Amit Kumar 3, Priyam Tiwari, Anish Singh.

## Hard rules

- **Meta.** Never activate or publish a Meta campaign. Never move money, never top up, never enter passwords, never call ads_activate_entity.
- **Changes.** Any pause, budget, audience, placement, creative, CRM-rule or SalesIQ change needs Sanjeev's explicit approval, one change at a time, with before/after evidence and a logged stop-loss where relevant.
- **Copy.** Ad copy, on-image text and website text need Sanjeev's OK on the exact text. The SIB-05 text approved 13 Oct is in the claims review; any change goes back to him.
- **Code.** Show code, a diff or the exact text before saving any production function, template or workflow.
- **CRM edits with the connector:** pass `trigger: []` and skip assignment rules; mass writes need a dry run and approval; don't delete CRM records; don't edit the 11 older LeadChain chains.
- **Emails and messages on Sanjeev's behalf.** Draft first, confirm the recipient, send only on his yes. Gmail sends from one@setindiabiz.com; cc sanjeev@setindiabiz.com when he asks.
- **SIB-05 claims.** Never "100% FDI allowed", "no approval needed", "set up in X days" or "no need to visit India". No LLP ad may quote ₹100 a day as the filing fee. Quote government fees from current rules only.
- **Browser.** If the permission check refuses a Setup page or a click, hand that step to Sanjeev. Reset any viewport emulation to desktop when done.

## Tool notes

- Meta connector: label read-only checks as read-only (advertiser_job "report_measure_or_look_up"). A publisher_platform × hour breakdown returns nothing.
- CRM Setup in the built-in browser: set the viewport to 1366×900, reset afterwards. Assignment-rule user chips: the remove icon has zero size until hover; clicking the `lyte-drop-remove` inside `li[data-value="<userId>"]` by JS works, then verify the chips before Save.
- SalesIQ settings: open /wwwsetindiabizcom/settings/home and navigate from there.
- Large COQL and timeline results may come back inline; use GROUP BY and narrow filters rather than pulling all rows.

## Output

End with a short report (done / open / who), a new dated change log, and the prompt for the session after.
