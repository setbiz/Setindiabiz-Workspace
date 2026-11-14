# India Entry Email Drip (Zoho Marketing Hub): Plan v1, 14 November 2026

**Status: DRAFT for owner approval. Nothing has been built, imported or sent in Zoho Marketing Hub or Zoho CRM.** Claude builds only on an explicit go that names the item (approval list in section 11).

Companion to the paid plan on branch `ppc/india-entry-2026-11-14` (`PPC/egm/runs/2026-11-14-india-entry/design_draft.md`, v2). That plan launches paid traffic on 1 December 2026 and its §6.4 widens the existing booking email to all India-entry sources. This drip starts from that email, so the two must go live together.

## Open Items Before Approval

1. **Consent and notice.** The website enquiry notice covers follow-up about the enquiry but not general marketing (section 7). Emails 1–5 stay within it. Emails 6 and 7 need the notice and opt-in change in section 7.3 first.
2. **Price evidence.** Email 4A quotes "from USD 499". The paid plan holds every price line until evidence of sales at that price is on file (paid plan §8, decision D2; CCPA bait-advertisement conditions). Email 4A therefore waits on the same evidence; Email 4N (no price) is the fallback.
3. **Booking page.** The only Bookings link on file, "Free Consultation - Ordinary Services" (`https://setindiabiz.zohobookings.com/3882293000006990272`), is staffed by six support staff, not the FDI handlers (G10 draft, §3). A new India-entry service is needed (section 6).
4. **Owner supplies:** the list page, three blog posts, the India Entry WhatsApp number, the sender mailbox and the late-shift decision. All are marked `[[...]]` and listed in section 9.
5. **Citations still on secondary sources** (marked "verify" where used): Rule 13(5), Companies (Incorporation) Rules, 2014 (apostille route); FLA return date; DPDP Rules, 2025 commencement dates (meity.gov.in did not render in this session); CPA 2019 s.2(47)(ix).

## 1. Why a Drip, and the Volume to Expect

India-entry revenue in the last 12 months came entirely from organic search, direct traffic and chat: 20 won deals, ₹16,31,480, none from paid ads (diagnosis, `PPC/reports/cross-platform/2026-11-14-india-entry-diagnosis.md`, §1). On Meta SIB-05, all three qualified leads were from the US, and 4 of 8 leads had not been worked by 14 November (§2a, §5.4). US leads arrive overnight in India, so the first contact is often a day late. The drip's job is narrow: get a US lead onto a call with an FDI handler, then get out of the way.

Volume is small. Zoho CRM (COQL, 14 November 2026) holds 13 leads ever with `Select_Country` = United States in Product Category FDI, and 11 in "Start Company". Expect tens per month once paid traffic starts [est], not hundreds. At that volume, sequencing matters more than send-time testing; A/B tests will not reach significance and are left out.

## 2. Segments and Entry Triggers

All CRM field names below are API names checked on 14 November 2026 (`Product_Category`, `Lead_Status`, `Select_Country`, `Lead_Source`, `Email_Opt_Out`; values from COQL).

### 2.1 Common entry conditions (all segments)

| Condition | Value | Reason |
|---|---|---|
| `Select_Country` | United States | First market (owner, 14 Nov). EU/UK leads stay out: privacy policy s.18.2 makes marketing to them consent-only |
| `Email` | not empty | |
| `Email_Opt_Out` | false | CAN-SPAM s.7704(a)(4) |
| `Lead_Status` | empty or "Establishing Contact" | Any later status means a handler has the lead (section 4) |
| `Converted__s` | false | |
| `IE_Drip_Stop` (new checkbox, section 4.2) | false | |
| `Created_Time` | within the last 30 days at journey launch; new leads thereafter | Older leads were told their details would be used to respond to that enquiry; a first email weeks later stretches that |
| `Lead_Source` | any **except** "Self - Cold Call", "SEO - Zoho Booking" and any imported or purchased list | Cold-call leads never enquired; Booking leads already have a call |

### 2.2 Segments

| Segment | Extra conditions | Who it is | Emails |
|---|---|---|---|
| **A: US company expanding to India** | `Product_Category` = FDI or BO-LO-PO | A US parent company looking at a subsidiary, branch or liaison office | 1, 2A, 3A, 4A or 4N, 5, then 6 and 7 with consent |
| **B: Individual in the US starting a company in India** | `Product_Category` = Start Company or Start LLP | Indian-origin professionals and others planning an Indian company while living in the US. 12 such US leads exist (COQL) | 1B, 2B, 3B, 4N-B, 5, then 6 and 7 with consent |
| **C: Existing company with a FEMA/RBI question** | `Product_Category` = RBI and Fema | A foreign-owned Indian company needing FC-GPR or other reporting | 1C, 6 (sent as a reply to their enquiry), 5 |

Segment B is defined by the service asked for and the country, never by name, ethnicity, visa status or employment history. Copy never mentions layoffs or visas. That follows the paid plan's rule (§1, Meta Personal Attributes policy) and avoids exploiting a reader's circumstances (ASCI Code, Chapter I).

`Select_Country` on Meta leads is the parent company's country (form Q2). On website leads it is set during handling and may be the person's location. The segment rule accepts both; handlers correct the field when they speak to the lead.

## 3. The Emails

Send rules for every email:
- Weekdays only, at **18:30 IST = 8:00 AM US Eastern / 5:00 AM Pacific** (US standard time, 1 November 2026 to 13 March 2027; from 14 March 2027 it becomes 9:00 AM Eastern). Replies then reach the team inside Indian working hours.
- Skip US holidays: 26 November 2026 (Thanksgiving), 25 December 2026 and 1 January 2027. The journey waits to the next working day.
- Day numbers count from lead creation. Email 1 is the existing CRM workflow; Marketing Hub sends from Email 2.
- Merge fields are shown as `{{Field}}` and are swapped for Marketing Hub tags at build. `{{Last_Name}}` holds the full name on Meta and website leads (G10 check, 15 leads); fallback "Hello,". `{{Owner}}` is the lead owner's name; fallback "The India Entry Team".
- Links carry `utm_source=zoho-mh&utm_medium=email&utm_campaign=ie-drip-202612&utm_content=e<n>`. The drip never overwrites `Lead_Source`, so the paid plan's attribution is untouched.
- Every email carries the footer in section 5.

### Email 1: Day 0, booking link (existing CRM workflow, revised)

Lives in Zoho CRM, not Marketing Hub: workflow "SIB-05 India Entry - booking email" (1123581000946398910), template 1123581000946398903. Changes: the condition widens from the SIB-05 form to the section 2.1 entry rules (paid plan §6.4), the Bookings link changes to the new India-entry service, and the section 5 footer is added. Without the footer this email fails CAN-SPAM s.7704(a)(3) and (a)(5).

- **Subject:** Your India entry enquiry: pick a time for a call
- **Preview:** The booking page shows our available times in your own time zone.

> Hello {{Last_Name}},
>
> Thank you for your enquiry about setting up in India. I'm {{Owner}} from the Setindiabiz India Entry team and I will handle it.
>
> The quickest next step is a 30-minute call by phone or Google Meet. Pick a slot here; the page converts our times to your time zone:
>
> [[BOOKINGS-FDI]]
>
> If no slot suits you, reply with two times that work for you and I will confirm one.
>
> It helps if you can tell us on the call:
> - where your parent company is incorporated and who its main shareholders are;
> - what the Indian entity will do: sales, services, sourcing or a project;
> - when you plan to start.
>
> If any shareholder or beneficial owner of your company is a citizen of, or based in, a country that shares a land border with India, please mention it. A different approval route may apply.
>
> Regards,
> {{Owner}}
> India Entry Team, Setindiabiz

**1B (Segment B):** replace the three bullets with: "whether you will hold the shares yourself, and where you expect to live when the company starts; what the company will do; when you plan to start." Drop the land-border paragraph unless a co-founder is involved.

**1C (Segment C):** subject "Your FEMA reporting enquiry: pick a time for a call"; first line "Thank you for your enquiry about RBI and FEMA reporting for your Indian company."; bullets become "the date of each share issue or transfer to a foreign investor; the forms already filed on the FIRMS portal, if any; your company's CIN."

Why no hours in the text: with the team available 9:30 AM to 8:00 PM IST, the overlap with the US East Coast is 9:00 to 9:30 AM Eastern. Stating hours would either understate or overstate coverage (the paid plan's compliance review, finding m1). The booking page shows only real slots.

### Email 2A: Day 2, the three structures (Segment A)

- **Subject:** Subsidiary, branch or liaison office: how the three compare
- **Preview:** What each can do in India and the RBI eligibility test for branch and liaison offices.

> Hello {{Last_Name}},
>
> Foreign companies entering India usually choose one of three structures. Here is how they differ, so that our call can start from your plan.
>
> **Subsidiary.** An Indian private limited company owned by your company. Subject to the foreign investment conditions for your sector, it can trade, invoice and hire in India like any Indian company. It needs at least two directors, one of whom stays in India for at least 182 days in the financial year (Sec. 149(3), Companies Act, 2013), and a registered office in India. It reports each issue of shares to its foreign investor on Form FC-GPR within 30 days of the issue.
>
> **Branch office.** Part of your company, not a separate company. It may carry out only the activities the RBI permits for branches. Your company generally needs a profit-making record over the last five financial years and net worth of at least USD 100,000.
>
> **Liaison office.** A representative office. It cannot carry on business in India and is funded from abroad. Your company generally needs a three-year profit-making record and net worth of at least USD 50,000.
>
> Branch and liaison office applications are filed through an authorised bank in India, and some sectors and countries need prior RBI approval (RBI Master Direction No. 10/2015-16, last updated 18 May 2021).
>
> A longer comparison: [[BLOG-1 structures]]
>
> If you already know which one you want, reply with its name and I will send the document list for it.
>
> Regards,
> {{Owner}}

Sources: RBI Master Direction 10/2015-16 (rbi.org.in, re-read 14 November 2026 by the paid plan's compliance reviewer; no update after 18 May 2021); Reg. 4(1), FEMA 395/2019-RB; Sec. 149(3), Companies Act, 2013. Wording matches the copy approved on 13 October 2026 (D21).

### Email 2B: Day 2, residence and your shares (Segment B)

- **Subject:** Starting an Indian company while you live in the US
- **Preview:** Whether you are resident in India when you invest decides which filings apply.

> Hello {{Last_Name}},
>
> When you set up an Indian company while living in the US, one question shapes the paperwork: are you resident in India when you take the shares?
>
> Under the Foreign Exchange Management Act, 1999, residence depends on your days in India in the previous financial year and on why you are in India or abroad (Sec. 2(v)). While you are resident outside India, the shares you take are foreign investment, and the company reports the issue on Form FC-GPR within 30 days (Reg. 4(1), FEMA 395/2019-RB). An NRI or OCI can instead invest on a non-repatriation basis under Schedule IV of the FEMA (Non-debt Instruments) Rules, 2019; that investment is treated like a resident's.
>
> Two more points come up early. The company needs a director who stays in India for at least 182 days in the financial year (Sec. 149(3), Companies Act, 2013); for a company incorporated mid-year the period applies proportionately. If you will be living in India, you may be able to fill that role yourself. And documents you sign in the US must be notarised and then apostilled before they are filed.
>
> More on this: [[BLOG-3 starting from the US]]
>
> Which route suits you depends on your dates and plans. We can settle it on a 30-minute call: [[BOOKINGS-FDI]]
>
> Regards,
> {{Owner}}

Sources: Sec. 2(v), FEMA, 1999; Reg. 4(1), FEMA 395/2019-RB; Schedule IV, NDI Rules, 2019 (both confirmed in the paid plan's compliance review, 14 November 2026); Sec. 149(3) and its Explanation, Companies Act, 2013; Rule 13(5), Companies (Incorporation) Rules, 2014 (verify on mca.gov.in).

### Email 3A: Day 5, documents (Segment A)

- **Subject:** Documents a US company needs for an Indian subsidiary
- **Preview:** Parent company papers, notarisation and apostille, and two decisions to make early.

> Hello {{Last_Name}},
>
> If you go ahead with a subsidiary, these are the documents we ask a US parent company for. Starting the apostille early saves the most time.
>
> From the parent company:
> - certificate of incorporation or formation, with its bylaws or operating agreement;
> - a board resolution approving the Indian subsidiary, naming who signs for the parent and the initial investment;
> - proof of the parent's registered address.
>
> From each director and signatory: passport and a recent proof of address. Directors living in India also give their PAN.
>
> Documents signed in the US are notarised and then apostilled, because the US is a party to the Hague Apostille Convention.
>
> Three points to settle early:
> 1. A private company needs at least two shareholders (Sec. 3(1)(b), Companies Act, 2013). A wholly owned subsidiary usually has a second shareholder holding one share on the parent's behalf.
> 2. Who will be the resident director (Sec. 149(3)). We can arrange one separately if you don't have one.
> 3. A registered office address in India. Also arranged separately if needed.
>
> The exact list depends on your state and structure. Reply "checklist" and I will send the list for your case.
>
> Regards,
> {{Owner}}

**Before approval:** the FDI team confirms this list against the current SPICe+ requirements. Rule 13(5), Companies (Incorporation) Rules, 2014 sets the notary-and-apostille route for subscribers in Hague Convention countries (secondary sources: ca2013.com, taxclue.in; verify on mca.gov.in).

### Email 3B: Day 5, documents (Segment B)

- **Subject:** Documents for starting your Indian company from the US
- **Preview:** Passport, address proof, notarisation and apostille, and who the second director will be.

> Hello {{Last_Name}},
>
> If you start a private limited company in India from the US, this is what we usually ask for:
> - your passport and a recent proof of your US address;
> - your PAN, if you have one;
> - notarisation and apostille of anything you sign in the US.
>
> A private company needs at least two directors and two shareholders (Secs. 149(1)(a) and 3(1)(b), Companies Act, 2013), and one director must stay in India for at least 182 days in the financial year. Founders often appoint a family member or co-founder who lives in India. If nobody suitable is available, we can discuss options on a call.
>
> The company also needs a registered office address in India from the day it is incorporated (Sec. 12).
>
> Reply "checklist" and I will send the full list for your case, or book a call: [[BOOKINGS-FDI]]
>
> Regards,
> {{Owner}}

### Email 4A: Day 9, what the fee covers (Segment A, subsidiary leads; HOLD until price evidence is on file)

- **Subject:** What our USD 499 subsidiary fee covers, and what it doesn't
- **Preview:** Our fee, the government costs on top, and the items arranged separately.

> Hello {{Last_Name}},
>
> Here is exactly what our price for an Indian subsidiary includes.
>
> Our fee starts at USD 499. It covers consultation and our services up to the Certificate of Incorporation: name approval and preparing and filing the incorporation forms with the Registrar of Companies. [[FDI team: confirm scope list]]
>
> Not included:
> - government filing fees and stamp duty, which depend on the company's capital and the state of its registered office (billed at actual cost);
> - digital signature certificates (billed at actual cost);
> - a registered office address in India (arranged separately);
> - a resident director, if you don't have one (arranged separately);
> - [[OWNER CONFIRM: "USD 50 for each additional promoter", as shown on /india-entry-services]].
>
> Our fee is zero-rated for GST when your company is outside India and pays in foreign currency (Secs. 2(6), 13(2) and 16, IGST Act, 2017). If either condition is not met, GST at 18% is added.
>
> After incorporation the company reports the share issue on Form FC-GPR within 30 days and files annual accounts and an annual return with the Registrar every year. We quote for those separately.
>
> For a written quote for your case, reply to this email or book a call: [[BOOKINGS-FDI]]
>
> Regards,
> {{Owner}}

Why every exclusion is listed in the email: an email is an advertisement under Sec. 2(1), Consumer Protection Act, 2019 ("electronic media, internet or website"), so an incomplete price is a misleading advertisement under Sec. 2(28). The CCPA Dark Patterns Guidelines, 2023 list drip pricing as a dark pattern. The owner's scope statement (14 November) and the approved S1 ad (D21, 13 October) carry the same exclusions. The live `/india-entry-services` page shows "$499/- (Govt Fee On Actual)" with the footnote "Government fee, stamp duty and taxes at actuals. USD 50 for each additional promoter." It does not mention the registered office or resident director; the paid plan's §11.4 already asks for that line on the page.

### Email 4N: Day 9, how fees are worked out (no price; BO-LO-PO leads, and all Segment A leads until 4A is cleared)

- **Subject:** How our India entry fees are worked out
- **Preview:** Our fee, the government costs on top, and what is arranged separately.

> Hello {{Last_Name}},
>
> We quote a fixed professional fee once we know your structure and plan. The quote lists each cost separately:
> - our fee for consultation and the filings;
> - government fees and stamp duty, billed at actual cost (they depend on the state and, for a company, its capital);
> - digital signature certificates, billed at actual cost;
> - a registered office and a resident director, if you need us to arrange them.
>
> Our fee is zero-rated for GST when your company is outside India and pays in foreign currency (Secs. 2(6), 13(2) and 16, IGST Act, 2017); otherwise GST at 18% is added.
>
> For a branch or liaison office, the application goes through an authorised bank in India, and the bank's own charges are separate.
>
> Reply with your structure and the state you have in mind, and I will send a written quote. Or book a call: [[BOOKINGS-FDI]]
>
> Regards,
> {{Owner}}

**4N-B (Segment B):** drop the branch/liaison paragraph; GST line becomes "GST at 18% is added, unless you pay from outside India in foreign currency and the other export conditions are met (Secs. 2(6) and 13(2), IGST Act, 2017)". An individual who has moved to India or pays in rupees owes GST (paid plan compliance review, M4). The website shows "$349/- Pvt Ltd by an Individual"; that figure goes in only if the owner confirms it and its evidence (section 11, D-E3).

### Email 5: Day 14, close the loop (all segments)

- **Subject:** Shall we keep your India enquiry open?
- **Preview:** Reply with one word and we will act on it.

> Hello {{Last_Name}},
>
> I have written a few times about your India enquiry and haven't heard back, so this is my last email about it.
>
> Reply with one word:
> - "call", and I will send times for this week;
> - "later" and a month, and I will write to you then;
> - "close", and we will close the enquiry.
>
> If you would like our occasional notes on India entry and compliance for foreign-owned companies, you can sign up here: [[MARKETING-OPT-IN-FORM]]. We send them only to people who ask.
>
> Regards,
> {{Owner}}

Handlers act on replies: "call" → book; "later" → `Lead_Status` Postponed with a follow-up task on that date; "close" → Lost, reason "Closed by lead". The opt-in link is the only route into Emails 6 and 7 for leads captured before the form change in section 7.3.

### Email 6: Day 21, first-year filings (consent only; Segment C gets it on Day 3 as the answer to their enquiry)

- **Subject:** After incorporation: first-year filings for a foreign-owned Indian company
- **Preview:** FC-GPR within 30 days, then the board, auditor and annual cycle.

> Hello {{Last_Name}},
>
> Incorporation is the first step. A foreign-owned Indian company then has these filings and deadlines in its first year:
>
> | What | When | Provision |
> |---|---|---|
> | Report the share issue to the RBI on Form FC-GPR | Within 30 days of the issue | Reg. 4(1), FEMA 395/2019-RB |
> | First board meeting | Within 30 days of incorporation | Sec. 173(1), Companies Act, 2013 |
> | Board appoints the first auditor | Within 30 days of incorporation | Sec. 139(6) |
> | Declaration that subscribers have paid for their shares | Within 180 days of incorporation | Sec. 10A(1)(a) |
> | Financial statements to the Registrar | Within 30 days of the AGM | Sec. 137(1) |
> | Annual return to the Registrar | Within 60 days of the AGM | Sec. 92(4) |
> | Annual return on foreign liabilities and assets to the RBI | By 15 July each year [verify] | RBI Master Direction on reporting under FEMA [verify] |
>
> A longer guide: [[BLOG-2 post-incorporation compliance]]
>
> We handle these as an annual package for foreign-owned companies. Reply if you would like a quote.
>
> Regards,
> {{Owner}}

### Email 7: Day 35, everything in one place (consent only)

- **Subject:** India entry services and fees in one place
- **Preview:** Subsidiary, branch and liaison office setup and the compliance that follows.

> Hello {{Last_Name}},
>
> Our India entry services, with what each includes and how fees are charged, are on one page: [[LIST-PAGE]]
>
> Three guides on the questions that come up most on our calls:
> - [[BLOG-1 structures]]
> - [[BLOG-2 post-incorporation compliance]]
> - [[BLOG-3 starting from the US]]
>
> When you are ready to talk, book a 30-minute call: [[BOOKINGS-FDI]]
>
> Regards,
> {{Owner}}

After Email 7, consented leads leave the journey. Any later newsletter is a separate list and a separate approval.

## 4. Exit and Branch Rules

### 4.1 Rules in Marketing Hub (eject criteria)

Zoho's journey "eject criteria" can test a lead's field values ([Zoho help: What is eject criteria?](https://help.zoho.com/portal/en/kb/marketing-automation/faqs/lead-journey/articles/what-is-eject-criteria)). Confirm in the Marketing Hub UI at build that the synced CRM fields below are selectable. Sync must run before 18:30 IST each day, so a status change made during the Indian working day stops that evening's email.

| Trigger | Action in the drip | Action in CRM |
|---|---|---|
| `Lead_Status` → Valid Lead | Eject | Handler owns the lead. CRM task to the owner if no proposal within 7 days |
| `Lead_Status` → Proposal Sent, Negotiation or Payment Pending | Eject | None from the drip |
| `Lead_Status` → Postponed | Eject | Handler sets a follow-up date |
| `Lead_Status` → Lost | Eject | If `Marketing_Consent` = true, eligible for a future newsletter list (separate approval). Otherwise nothing |
| `Converted__s` = true | Eject | |
| `IE_Drip_Stop` = true | Eject | See 4.2 |
| Unsubscribe clicked or `Email_Opt_Out` = true | Eject and suppress across Marketing Hub and CRM templates | Opt-out syncs to CRM `Email_Opt_Out` (two-way sync to be confirmed at build) |
| Hard bounce or spam complaint | Eject and suppress | |
| Lead replies | Eject on the reply tag (see 4.2) | Handler answers within one working day |
| Call booked in Zoho Bookings | Eject (via `IE_Drip_Stop`) | Booking linked to the lead |
| No consent at Email 5 | Leaves after Email 5 | None |
| Consent given (opt-in form or checkbox) | Continues to Emails 6 and 7 | `Marketing_Consent` = true, with date and source |

### 4.2 Why a new stop field is needed

FDI deals are created without converting the lead: `Converted__s` is false on all 92 FDI-category leads in the last 12 months (diagnosis §1). An exit rule on "converted" alone would keep emailing clients after they sign. Reply detection in Marketing Hub is also unreliable (community reports, see sources). So the plan adds one CRM checkbox on Leads, **`IE_Drip_Stop`**, set by:
1. a CRM workflow when a Deal is created whose contact email matches the lead's email (a small Deluge function);
2. the handler, by hand, when the lead replies or books a call;
3. the Bookings integration, if it can update the lead (check at build).

The paid plan's own fix (convert the lead into the deal, diagnosis §5.1) would make rule 1 unnecessary. Until sales does that, the checkbox is the safety net.

## 5. Sender, Reply-To and Footer

| Item | Setting |
|---|---|
| From name | `{{Owner}} at Setindiabiz` (fallback "Setindiabiz India Entry") |
| From address | [[SENDER-MAILBOX]], suggested `indiaentry@setindiabiz.com`. One shared address; CAN-SPAM s.7704(a)(1) requires header information that is not misleading, and the From line must identify Setindiabiz |
| Reply-to | The same mailbox, shared by the four PG-02 handlers and logged to CRM. It must keep receiving replies for at least 30 days after each send (s.7704(a)(3)(A)) |
| Domain | Authenticate setindiabiz.com in Marketing Hub (SPF, DKIM) and publish DMARC before the first send. Add the one-click `List-Unsubscribe` header |
| Signature | Name, "India Entry Team, Setindiabiz", www.setindiabiz.com, [[WHATSAPP-NUMBER]] |

**Footer (every email, including Email 1 in CRM):**

> Setindiabiz Private Limited, A-34, Sector 2, Noida, Uttar Pradesh 201301, India.
> You are receiving this email because you asked us about {{enquiry_reason}} on {{Created_Date}} through {{source_label}}. This is a commercial email about our services. [Unsubscribe] with one click. Privacy policy: https://www.setindiabiz.com/privacy-policy
> Setindiabiz is a private professional services firm in India, not affiliated with any government or regulator.

`{{source_label}}` mapping: Advt - Facebook / Advt - Instagram → "our form on Facebook or Instagram"; Advt - LinkedIn → "our LinkedIn form"; Self - Web Chat → "the chat on our website"; all other sources → "our website". The address is the corporate office shown in the site footer and in privacy policy s.19. The registered office (Innov8 CP2, Regal Building, Connaught Place, New Delhi 110001) would also satisfy s.7704(a)(5)(A)(iii); the owner picks the one where post is collected.

## 6. Booking Page and Time Zones

Create a Zoho Bookings service "India Entry Consultation", 30 minutes, staffed by the four PG-02 handlers (Foziya Ansari, Karishma Singh, Rishika Singh, Shubendu Banerjee), time zone shown to the visitor. Slots by staff hours:

| Staff hours (IST) | US Eastern (EST, to 13 Mar 2027) | US Pacific (PST) |
|---|---|---|
| Current, to 20:00 | 19:30–20:00 IST = 9:00–9:30 AM | 6:00–6:30 AM |
| Morning IST | 09:30–11:00 IST = 11:00 PM–12:30 AM (previous day) | 8:00–9:30 PM (previous day) |
| If extended to 23:00 | 19:30–23:00 IST = 9:00 AM–12:30 PM | 6:00–9:30 AM |

Without the 23:00 extension, East Coast leads get a 30-minute morning window and West Coast leads get evening slots from the IST morning. The paid plan (§12, D8) also needs the late-shift name before 1 December. The drip works either way because the page shows only real slots, but booked-call rates will be low without the extension [est].

The current link is named "Free Consultation". Use "free" in the emails only if the call is unconditional: no fee credited later, no deposit, no obligation (CCPA Guidelines for Prevention of Misleading Advertisements, 2022, conditions for "free" claims). The drafts above say "30-minute call" to stay safe.

## 7. Consent and Notice

### 7.1 What the notices say today (checked 14 November 2026)

| Where | Text |
|---|---|
| Homepage and `/contact-us` enquiry forms | "Details used only to respond to your enquiry" + privacy policy link. No checkbox |
| `/india-entry-services` form | "How we handle your details: read our privacy policy." No checkbox |
| Meta form "SIB-05 India Entry Form v1" | "Setindiabiz Private Limited will use these details to respond to this enquiry." Required checkbox: "I agree to be contacted by Setindiabiz by email, phone and WhatsApp about this enquiry." |
| Privacy policy (last updated 16 October 2026) | s.3.4: "With your consent, we also process data for marketing and business development", including "sending promotional communications about our services". s.10.2: consent can be withdrawn "by using unsubscribe links in emails" |

### 7.2 Does the notice cover a marketing drip?

Partly. Our own privacy policy (s.3.4) makes promotional email a consent-based purpose, and no form collects that consent. So:

- **Emails 1–5 are covered** as a response to the enquiry, provided they stay on the service the lead asked about, stop within 14 days, stop on reply or request, and every email offers an unsubscribe. They answer the question asked, give the facts needed to decide, and ask for a call.
- **Emails 6 and 7 are not covered.** They promote services beyond the enquiry (annual compliance) and general content. Sending them on the current notice would contradict "used only to respond to your enquiry" and privacy policy s.3.4. They go only to leads who opt in.

The law behind that split:

| Law | Position on 14 November 2026 | Effect on the drip |
|---|---|---|
| CAN-SPAM Act, 15 U.S.C. 7704 (US recipients) | In force; text unchanged since Pub. L. 108-187 (2003) | No prior consent needed, but every commercial email needs: honest header (a)(1); non-misleading subject (a)(2); working return address or opt-out for 30 days (a)(3); opt-out honoured within 10 business days (a)(4); identification as an advertisement, opt-out notice and a valid postal address (a)(5). The (a)(5)(A)(i) identification can be dropped only with affirmative consent, which these leads have not given, so the footer says "This is a commercial email". Opt-out may not require more than a reply or one web page (16 CFR 316.5). A reply to an enquiry is still commercial, because a transactional message under s.7702(17) needs a transaction already agreed |
| IT Act, 2000 s.43A and SPDI Rules, 2011 | In force | Rule 4 requires a published privacy policy stating purposes; ours says marketing is consent-based. Rule 5(5): information is used for the purpose for which it was collected. Strictly, s.43A and most of r.5 bite on sensitive personal data, and name, email and phone are not SPDI under r.3. The practical risk is departing from our own published policy and notice, which r.4 and the Consumer Protection Act both reach |
| Consumer Protection Act, 2019 | In force | Emails are advertisements (s.2(1)); misleading ones are caught by s.2(28) and s.89, with CCPA powers under s.21. Disclosing personal information given in confidence is an unfair trade practice under s.2(47)(ix) (clause number from secondary sources; verify on indiacode.nic.in) |
| DPDP Act, 2023 and DPDP Rules, 2025 (G.S.R. 846(E), 13 November 2025; corrigendum G.S.R. 892(E), 10 December 2025) | Rules 1, 2 and 17–21 (the Data Protection Board) in force since notification. Rule 4 (consent managers) from one year after notification, i.e. 13 or 14 November 2026. Notice, consent and Data Principal rights from 18 months after, i.e. 13 or 14 May 2027. Sources disagree by a day; meity.gov.in did not render in this session, so verify against the Gazette | From May 2027 the Act applies to this processing even for US leads, because Setindiabiz processes the data in India (s.3(a)). Emails 1–5 then rest on the legitimate use in s.7(a): data voluntarily given for a specified purpose. Emails 6–7 need consent under s.6 after an itemised notice under s.5 and Rule 3, with withdrawal as easy as giving consent (s.6(4)) |
| GDPR / UK GDPR | Not triggered: US-only entry rule | EU/UK leads stay out of the drip (privacy policy s.18.2) |
| TCPA, 47 U.S.C. 227 | Applies to calls and texts, not email | Handler calls to US numbers stay manual (paid plan §6.4) |

### 7.3 Changes needed before Emails 6 and 7 are switched on (and recommended before launch)

1. **Website forms (homepage, `/contact-us`, `/india-entry-services`, the new India-entry pages):** replace the notice with: "We use these details to respond to your enquiry, including a few follow-up emails about it. You can unsubscribe at any time. Privacy policy." Add an **unticked, optional** checkbox: "Send me occasional emails from Setindiabiz about India entry and compliance. I can unsubscribe at any time."
2. **Meta form v2 and the LinkedIn form "IE US v1"** (paid plan §9): the same optional checkbox as a custom question. The required "about this enquiry" checkbox stays as it is.
3. **CRM fields on Leads:** `Marketing_Consent` (checkbox), `Marketing_Consent_Date`, `Marketing_Consent_Source` (form name and notice version). Map them in LeadChain, the website form integration and the LinkedIn mapping.
4. **The opt-in form behind Email 5** (`[[MARKETING-OPT-IN-FORM]]`): a Marketing Hub signup form with the same wording, writing the three fields above.
5. **Privacy policy:** s.3.4 already covers this. Add one line naming Zoho Marketing Hub as the email processor in s.5 if Zoho is not already listed there.

Item 1's first sentence makes the Emails 1–5 basis explicit and is worth doing before launch. Items 1–4 are required before Emails 6 and 7.

## 8. Content Rules and Copy Checks

Every email was checked against these before this draft; the build repeats the check.

| Rule | Provision | How the copy meets it |
|---|---|---|
| No implied government link | Emblems and Names (Prevention of Improper Use) Act, 1950 s.3; CCPA Guidelines 2022 | Footer disclaimer; no "RBI-approved", "MCA-registered", emblem or ministry name used as a badge |
| No legal-practice wording | Advocates Act, 1961 ss.29, 33 and 45; *Bar Council of India v. A.K. Balaji* (2018) 5 SCC 379 | The words lawyer, attorney, law firm, legal advice and counsel do not appear. Credentials are limited to the approved "CS & CA experts" wording (D21) |
| Complete price | CPA 2019 ss.2(1), 2(28); CCPA Misleading Ads Guidelines 2022 (bait ads); CCPA Dark Patterns Guidelines 2023 (drip pricing) | Email 4A lists every exclusion and GST; held until price evidence is on file |
| Honest subjects, no false urgency | 15 U.S.C. 7704(a)(2); Dark Patterns Guidelines 2023 (false urgency) | Each subject states the email's actual content. No "last chance", deadlines or countdowns |
| No timelines or approval promises | Approved claims list (build spec §1) | No "in X days", "100% FDI", "no approval needed" or "no need to visit India" |
| Land-border investors | Press Note 3 (2020) as amended by Press Note 2 (2026); proviso to Rule 6(a), NDI Rules, 2019 as amended by S.O. 2174(E) | Email 1 asks about land-border ownership and says "a different approval route may apply". Government copies still unopened, so no detail is stated |
| No reference to personal circumstances | ASCI Code Ch. I; Meta Personal Attributes policy (for any reuse in ads) | Segment B copy refers only to living in the US and the service asked for |

Review cycle: re-check every cited provision every 90 days, and at once on any change to the NDI Rules, Press Note 3, RBI Master Direction 10/2015-16 or FEMA 395/2019-RB (same legal stop as the build spec §8).

## 9. Placeholder Register (owner supplies)

| Placeholder | Used in | Needed |
|---|---|---|
| `[[BOOKINGS-FDI]]` | 1, 2B, 3B, 4A, 4N, 7 | URL of the new "India Entry Consultation" Bookings service (section 6) |
| `[[LIST-PAGE]]` | 7 | The India entry services list page |
| `[[BLOG-1 structures]]` | 2A, 7 | Subsidiary vs branch vs liaison office |
| `[[BLOG-2 post-incorporation compliance]]` | 6, 7 | FC-GPR and first-year filings |
| `[[BLOG-3 starting from the US]]` | 2B, 7 | Starting an Indian company while living in the US |
| `[[MARKETING-OPT-IN-FORM]]` | 5 | Marketing Hub signup form (section 7.3) |
| `[[SENDER-MAILBOX]]` | section 5 | Shared mailbox to create |
| `[[WHATSAPP-NUMBER]]` | signature | India Entry Services number (kept out of this repo) |
| `[[FDI team: confirm scope list]]` | 4A | Exact services inside the USD 499 fee |
| `[[OWNER CONFIRM: USD 50 per promoter]]` | 4A | Whether the website footnote applies |

Blog and list-page links are checked for SEO basics before they go in: each target page has a unique title and meta description, an H1 matching the topic, and internal links back to `/indian-subsidiary-registration` and `/india-entry-services`.

## 10. What to Measure

Reported weekly alongside the paid plan's Monday report, from Marketing Hub and CRM (aggregates only):
- leads entered, by segment;
- calls booked within 14 days of creation, and from which email;
- replies, unsubscribes, bounces and spam complaints per email;
- leads reaching Valid Lead within 21 days, drip versus pre-drip US leads (directional only; small numbers).

Stop rule: if spam complaints exceed 0.3% of sends in any week (the Gmail bulk-sender ceiling) or unsubscribes exceed 2% on any email [est threshold], pause that email and review it.

## 11. Approvals Needed (nothing is built until each item has a go)

| # | Decision | Recommendation |
|---|---|---|
| D-E1 | Approve segments, entry rules and exit rules (sections 2 and 4) | Approve |
| D-E2 | Approve Emails 1, 2A, 2B, 3A, 3B, 4N, 5 and the footer for launch with the paid plan on 1 December 2026 | Approve after the FDI team confirms the 3A/3B document lists |
| D-E3 | Email 4A price: release only with evidence of sales at USD 499 for this scope (same test as paid plan D2). Decide whether "$349 Pvt Ltd by an Individual" appears in 4N-B | Hold 4A until evidence; no price in 4N-B for now |
| D-E4 | Website, Meta and LinkedIn notice and opt-in changes (section 7.3) and the three consent fields | Approve; required before Emails 6 and 7 |
| D-E5 | CRM: `IE_Drip_Stop` field and the Deal-created workflow; widen the Email 1 workflow and add the footer | Approve |
| D-E6 | New Bookings service staffed by PG-02; late shift to 23:00 IST | Approve both; the late shift decides whether US East Coast leads can book at all |
| D-E7 | Sender mailbox, domain authentication, and which postal address goes in the footer | Create the mailbox; use the Noida address |
| D-E8 | Supply the list page and three blog posts | Owner |

## Sources Opened (14 November 2026)

- 15 U.S.C. 7704: https://www.law.cornell.edu/uscode/text/15/7704
- Setindiabiz privacy policy (last updated 16 October 2026), homepage, `/contact-us` and `/india-entry-services` forms: setindiabiz.com
- Zoho eject criteria: https://help.zoho.com/portal/en/kb/marketing-automation/faqs/lead-journey/articles/what-is-eject-criteria ; reply-ejection community thread: https://help.zoho.com/portal/en/community/topic/how-to-eject-leads-that-reply
- DPDP Rules, 2025 commencement (secondary): https://www.scconline.com/blog/post/2025/11/14/meity-notified-digital-personal-data-protection-rules-2025/ ; https://www.taxmann.com/post/blog/govt-notifies-digital-personal-data-protection-rules/ ; https://www.mondaq.com/india/data-protection/1708164/digital-personal-data-protection-rules-2025-notified
- Rule 13(5), Companies (Incorporation) Rules, 2014 (secondary): https://ca2013.com/rule-13-companies-incorporation-rules-2014/ ; https://taxclue.in/blog/overseas-subscriber-attestation-under-rule-13-three-country-categories
- Zoho CRM COQL on Leads (aggregates only): status, category, country and source counts
- Repo: SIB-05 build spec v5, G10 email draft, G11 approved copy; paid plan v2, compliance review and consolidated review on branch `ppc/india-entry-2026-11-14`
