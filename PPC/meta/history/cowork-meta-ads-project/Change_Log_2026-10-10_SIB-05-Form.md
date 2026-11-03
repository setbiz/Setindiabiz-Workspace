# Change log: SIB-05 India Entry, lead form and routing (10 Oct 2026, 14:15–15:15 IST)

Follows `Change_Log_2026-10-10_SIB-05-CRM.md` (R86–R94, C74–C76). Spec: `Meta Ads/SIB-05_India_Entry_Build_Spec_2026-10-10.md` (v3). Privacy text: `Meta Ads/Privacy_Policy_EU_UK_Notice_Draft_2026-10-10.md`.

## Sanjeev's decisions (14:15)

| # | His words | Effect |
|---|---|---|
| D14 | "Privacy Text is confirmed"; "We have zoho signed" | 18.6 stands; edit to be published |
| D15 | "We will keep leads indefinitely and delete as per our own requirements" | 18.7 rewritten to state criteria (GDPR Art. 13(2)(a) allows criteria instead of a period); his OK on the wording requested at 14:22 |
| D16 | "Yes lets launch on non EU UK" | Ad sets target US, UAE, Singapore, South Korea, Japan, Australia, Canada |
| D17 | "ignore optional item" | No change to the CAPI signal for EU/UK leads |
| D18 | "We will use zoho booking url instead of building a page on website" | No website page; Bookings URL in the G10 email |
| D19 | "Yes send whatsapp chats to separate brand 'fdi'" | Read as: route the India Entry Services brand's …508 WhatsApp chats to Sales - FDI |
| D20 | "yes build lead from" | G7 go |

14:23: "loggedin". Sanjeev logged in to WordPress in the built-in browser.

## Sanjeev's decisions (14:39)

| His words | Effect |
|---|---|
| "Ok to wordpress changes" | Privacy edit published (C79) |
| "yes whatsapp will go to FDI Team, keep it private and write routing rule" | Sales - FDI stays Private; a chat-routing rule was tried (R100) |
| "Free Consultation" | G10 uses https://setindiabiz.zohobookings.com/3882293000006990272 |
| "Yes Setup Lead chain" | G8 chain saved (C80) |

## Read-only checks

| # | Item | Finding | Method |
|---|---|---|---|
| R95 | Zoho Bookings | Workspace SETINDIABIZ has 2 active services, each one-on-one for 30 minutes and staffed by the same 6 support staff (Swati Dhoundiyal, Shaily Dhoundiyal, Asha Devi, Priyanka Dwivedi, Pavneet Kaur, Arjit Vaibhav). The services are "Free Consultation - Ordinary Services" (setindiabiz.zohobookings.com/3882293000006990272) and "Expert Consultation - Complex Services (₹499)" (setindiabiz.zohobookings.com/3882293000007242037, paid). No upcoming appointments. No FDI service. | Bookings admin, view only |
| R96 | Leads fields for the LeadChain map | Country is the picklist **Select_Country** (247 values), which contains all 10 form countries but not "Other". Job title fits **Designation** (label "Title", text), which is on no Leads layout. Company is text. Lead_Channel includes "Advt". Product_Category includes "FDI" and "BO-LO-PO". | getFields |
| R97 | SalesIQ WhatsApp channel picker | For …508, "Change Department" lists only Customer Support. Sales - FDI is Private, and the picker shows Public departments only. Chat routing (Settings › Automate) has no rules and offers route-to options: all operators, specific operators, last attendee, CRM lead/contact owner. | SalesIQ settings |
| R98 | WordPress page | Privacy Policy is page 4521 (block editor), last modified 4 Oct 2026 21:07. It has 41 top-level blocks; sections are H2 headings followed by lists. | wp.data in the editor |
| R99 | First SIB-04 live lead | 1123581000946520260 (L483411), created 14:28:28 by the SIB-04 chain. Checks passed: <ul><li>Lead Source "Advt - Facebook" and Lead Channel "Advt";</li><li>Tag FB-ACR;</li><li>owner Priyam Tiwari (LG-11);</li><li>Product "ACR - Company Annual Return" and Product Cat "Annual Filing";</li><li>Description "Private Limited, FY 2025-26 only";</li><li>Meta_Campaign, Meta_Ad_Set and Meta_Ad_Name filled.</li></ul>Lead_Status "Establishing Contact" was set at 14:51:45, 23 minutes after creation. First_Contact_Time is blank. | getRecord 15:00 |
| R100 | SalesIQ chat-routing rule | <ul><li>Form filled: Title "FDI WhatsApp - India Entry Services to FDI team"; Brand India Entry Services; Channels is WhatsApp; Route to: Specific operators.</li><li>The operator picker lists only 9 operators: Amrita Chanchal, Arjit, Asha, Himanshu, Pavneet Kaur, Priyanka, Sanjeev Kumar, Shaily and Swati. These are exactly the 9 members of Customer Support, the …508 channel's department (checked against the department's operator list at 15:10).</li><li>The same 9 appear with brand Compliance & ACR, and none of the five FDI handlers can be picked ("Foziya": "Search not found").</li><li>**Cancelled, nothing saved.** The routing list is still empty.</li></ul> | SalesIQ, 15:00–15:03 |
| R101 | SalesIQ departments | 9 departments. Three are Public: OPS - Jobs (6), Customer Support (9) and **Sales - General Inquery (31)**. Sales - General Inquery includes all five FDI handlers (Foziya Ansari, Gaurav Pandey, Karishma Singh, Rishika Singh, Shubendu Banerjee) and Pavneet Kaur. Sales - FDI (20) is Private. | Departments list and operator list, view only |
| R102 | CRM email templates (Leads) | <ul><li>Folder "S - FDI" holds the 2022 FDI quotation templates. No template for SIB-05 exists.</li><li>The form name is in the field **Meta_Lead_Form**.</li><li>On recent Meta leads First_Name is mostly blank and Last_Name holds the full name.</li></ul> | Templates API GET; COQL |
| R103 | Bookings page | https://setindiabiz.zohobookings.com/3882293000006990272 loads as "Free Consultation - Ordinary Services": 30 minutes, phone or Google Meet, with slots today. The service text names "company registration, GST, trademark, compliance and other everyday services". The time zone can be changed on the page. | Built-in browser, 15:06 |
| R104 | Law on land-border investment | <ul><li>Press Note 3 (2020 Series) is in force as amended by Press Note 2 (2026 Series) and the NDI Amendment Rules, 2026 (reported as notified 2 May 2026).</li><li>Direct investment by an entity of, or a citizen from, a land-border country still needs government approval.</li><li>Beneficial owner now follows Sec. 2(1)(fa) PMLA. Indirect holdings under 10% without control use the automatic route, with DPIIT reporting.</li></ul>Read from secondary sources; the Gazette copy was not retrieved. | Web (tta.in, sarafpartners.com) |

## Changes

| # | Time (IST) | Change | Before | After | Evidence |
|---|---|---|---|---|---|
| C77 | 14:26 | SalesIQ brand **India Entry Services** (61466000023310225) › Flow Controls › Departments responsible for chats | Customer Support | **Customer Support + Sales - FDI** | "Changes saved successfully"; a 14:25 attempt failed with a lost server connection and was redone after reload |
| C78 | 14:35 | Instant Form **"SIB-05 India Entry Form v1"**, Form ID **4073050519663550**, on Page Setindiabiz Private Limited (627814417091714) | 6 forms on the Page | 7 forms; the new form is Active, 0 leads, Restricted | Forms list and details panel; all field values read back before Create (see spec section 4) |

C78 details:
- **Form type:** Higher intent, flexible delivery off.
- **Questions:**
  - Q1 entity: 4 answers, exact CONFIG texts.
  - Q2 parent country: 10 countries + Other.
  - Q3 timeline: 3 answers.
- **Contact fields:** Work email (required, no domain validation), Full name, Phone, Company name, and Job title (optional).
- **Consent and privacy:** privacy link; custom disclaimer "Consent to contact" with a required checkbox.
- **Ending:** "Thank you." with a native Chat on WhatsApp button on [phone redacted]; Messenger off.
- **Settings:** English (US), Restricted.

While building, a short-answer question was added by a mis-click and deleted before saving. A draft was saved at each step.

| C79 | 14:40:21 | WordPress page 4521, www.setindiabiz.com/privacy-policy | Last edited 4 Oct 2026; DPDP-only | <ul><li>Change 1: pointer line in the opening paragraph.</li><li>Change 2: s.4 names the DPDP Act, 2023.</li><li>Change 3: new s.18 "Notice for People in the EU, EEA and UK" (18.1–18.11, 30 blocks, 0 invalid).</li><li>Contact Us renumbered 19 and Acceptance 20.</li></ul> | Saved on Sanjeev's 14:39 OK. A WebFetch first showed the cached old page, so the WP Rocket cache for post 4521 was purged. A logged-out read then showed the new s.18 and 18.7 wording. |
| C80 | 14:42 | LeadChain chain **"FB SIB-05 FDI v1"** on form 4073050519663550 | No chain for the form | Active, 0 leads. Mapping as in spec section 4: <ul><li>Lead ID, Full name → Last_Name, Work email, Phone and Company;</li><li>Q1 + Q3 → Description; Q2 → Select_Country;</li><li>Product Cat "FDI", Lead Channel "Advt", Tag FB-FDI and the SIB-05 assignment rule;</li><li>the six Meta_* fields.</li></ul>**Job title left unmapped**, because Designation is on no layout. | LeadChain list shows the chain Active, created 10 Oct 2026 02:42 PM. Opening the saved chain view was refused by the browser permission check, so G9 checks the rows. |

The SalesIQ routing rule for G3c was filled in but **not saved** (R100).

No Meta campaign, ad set or ad was created. No money was moved. No CRM record was edited or deleted, and no email template or workflow was saved.

## Open

| # | Item | Who |
|---|---|---|
| 1 | **G3c WhatsApp routing.** A routing rule cannot pick the FDI handlers while the …508 channel sits on Customer Support (R100). Choose one option:<ul><li>**A (keeps Sales - FDI Private):** add Sales - General Inquery to the India Entry Services brand, set the …508 channel department to it, then save the routing rule with the five handlers (all five are in that department, R101).</li><li>**B:** a new Public department "India Entry - WhatsApp" with the five handlers and Pavneet Kaur, linked only to India Entry Services, set as the …508 channel department; no rule needed.</li><li>**C:** leave the line with Customer Support.</li></ul> | Sanjeev |
| 2 | G10 email template and workflow: text in `SIB-05_G10_Email_Draft_2026-10-10.md` | Sanjeev approves; Claude saves |
| 3 | G9 test leads (one subsidiary, one branch, one with country "Other"); also confirms the C80 chain rows and the owner merge in G10 | Sanjeev runs, Claude checks |
| 4 | Job title: add "Title" (Designation) to the Leads layout and map it, or leave it unmapped | Sanjeev |
| 5 | G11 creatives with claims review; G12 campaign switched off; G13 publish | Per spec |
| 6 | Bookings service text is written for Indian everyday services, and staffed by support. Consider a short India-entry line or a separate service later | Sanjeev |
