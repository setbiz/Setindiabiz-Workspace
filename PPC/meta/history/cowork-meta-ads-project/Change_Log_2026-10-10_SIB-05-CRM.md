# Change log: SIB-05 India Entry, CRM build and pre-launch checks (10 Oct 2026, 12:58–13:40 IST)

Follows `Change_Log_2026-10-10_SIB-04-PPCFormTidy.md` (R78–R85, C72–C73). Spec: `Meta Ads/SIB-05_India_Entry_Build_Spec_2026-10-10.md` (v2). Code copy: `Meta Ads/ppc_form_tidy.deluge.txt` (v1.1).

## Sanjeev's decisions

- **12:58:** "Lets Start FDI Services".
- **Form questions:** All 10 countries. Instant Form plus a WhatsApp button on the thank-you screen. Round robin over the five PG-02 handlers with the online check, default Pavneet Kaur. Price "From USD 499 · govt fees at actuals". LUT for FY 2026-27 filed. Follow-up by email with a booking link. Keep the EU and UK countries, but check the privacy policy first.
- **13:14:**
  - Drop the land-border ownership question.
  - "I will login into wordpress, you can edit the Privacy Policy."
  - "Ok on all observations and recommendations." Taken as the go for G4–G6 and the privacy fixes.
  - "Subsidiary goes to FDI - Subsidiary Incorporation."
  - "Schedule meeting: check if we already have a page, we will upgrade that page to use zoho bookings."

## Read-only checks

| # | Item | Finding | Method |
|---|---|---|---|
| R86 | SIB-05 products | FDI - Subsidiary Incorporation (1123581000000185013): FDI / FEMA. Branch Office Registration of Foreign Company (1123581000057725451): BO-LO-PO / FEMA. FDI - Liaison Office (1123581000057725457): BO-LO-PO / FEMA. All active. | COQL 13:33 |
| R87 | PPC Form Tidy live code | The function body read from the API (modified 13:17:07) matches the local copy, SIB-05 block included. | Functions API GET |
| R88 | Phone normaliser | "Normalize Lead Phone" (35880000003686001) leaves any number that already has "+" and a country code unchanged. Safe for the ten countries. | Function code |
| R89 | SalesIQ, [phone redacted] | Brand "India Entry Services" (61466000023310225) owns the number (0 WhatsApp users). Both the channel department and the brand's "Departments responsible for chats" are **Customer Support** only. **No Zobot** on this brand: the 3 bots are Tiya - Annual Filings (Compliance & ACR) and Tiya ×2 (Setindiabiz Inquiries). "Sales - FDI" (61466000026678025) has 20 operators, including all five PG-02 handlers and Pavneet Kaur. WhatsApp balance is 10 credits. Effect: a form lead who taps WhatsApp reaches Customer Support, and SalesIQ's own CRM push may create a second "Self - Web Chat" lead (as on 7 Oct for SIB-04). | SalesIQ settings, read only |
| R90 | Booking page | setindiabiz.com has no booking page. Every "Schedule a Call" link in the menus and on /india-entry-services goes to /contact-us ("Request a Call/Quote" form). | Site crawl |
| R91 | Privacy policy (last edited 4 Oct 2026) | DPDP-only. Missing for EU/UK people: representative, GDPR legal bases and legitimate interests, named transfer safeguard, restriction/objection/portability, EU/UK complaint route, whether data is required, profiling. s.4 calls the Act the "Data Protection and Privacy Act". The opening paragraph and ss.10 and 19 treat use of the site as consent. | Page read in full 13:27 |
| R92 | Meta measurement signal | The CRM CAPI functions (`sib_sendMetaCAP_Lead`, `sib_sendMetaCAPI_Deal`) send Meta the lead_id plus SHA-256-hashed email and phone at ValidLead, QualifiedLead, Committed and Purchase (with the deal amount). This must be disclosed to EU/UK people. | Project doc `Zoho_to_Meta_CAPI_Deluge.md` |
| R93 | Law as on 10 Oct | (1) **UK:** Sec. 164A, Data Protection Act 2018 (inserted by Sec. 103, Data (Use and Access) Act 2025), in force 19 June 2026 by SI 2026/82: controllers must facilitate complaints and acknowledge them within 30 days. (2) **EU:** the Digital Omnibus GDPR changes are still in first reading (24 Sep 2026); the current GDPR applies. (3) **India:** DPDP Rules 2025 notified 13 Nov 2025 (G.S.R. 846(E)); notice, consent and rights duties apply from 13 May 2027; no notification shortening this was found. (4) **Transfers:** EDPB Guidelines 05/2021 (v2.0, 14 Feb 2023) treat disclosure by a controller subject to Art. 3(2) to a provider in a third country as a transfer. | legislation.gov.uk; secondary for the rest (listed in spec section 9) |
| R94 | SIB-04 status at 13:35 | Campaign 120246968311680449 ACTIVE, lifetime spend ₹279.74, 1,000 impressions, so funds are in. CRM: no lead for form "SIB-04 ACR Form v1" (test lead 6 deleted; no live lead yet). | Meta connector; COQL |

## Changes

| # | Time (IST) | Change | State | Evidence |
|---|---|---|---|---|
| C74 | 13:16:49 | Leads tag **FB-FDI** created (id **1123581000946556020**) | Live | getTags |
| C75 | 13:17:07 | **PPC Form Tidy** (Deluge record 1123581000946601707): CONFIG block for **"SIB-05 India Entry Form v1"** added. Default product FDI - Subsidiary Incorporation (also for "Not sure yet"); "Branch office" → Branch Office Registration of Foreign Company; "Liaison office" → FDI - Liaison Office. Logic unchanged; no rule change. | Live, not yet exercised (no SIB-05 form exists) | Functions API (R87) |
| C76 | ~13:18–13:26 | Assignment rule **"PPC - SIB-05 India Entry - PG-02"** (id **1123581000946634218**, API PPC_SIB_05_India_Entry_PG_02, Leads). One entry: Product Cat is BO-LO-PO or FDI, **or** Tag is FB-FDI (pattern "1 or 2"). Round robin over Foziya Ansari, Gaurav Pandey, Karishma Singh, Rishika Singh and Shubendu Banerjee, with the online-status check. Default user **Pavneet Kaur** (was "Logged in User"). | Live, not yet exercised | getAssignmentRules 13:26: default_assignee Pavneet Kaur, modified 13:25:59 |

No Meta change for SIB-05, no LeadChain chain opened, no SalesIQ setting changed, no website change, no CRM record edited or deleted, no money moved.

## Sent to Sanjeev for approval (13:33)

`Privacy_Policy_EU_UK_Notice_Draft_2026-10-10.md`. It has three changes:
1. A pointer line in the opening paragraph.
2. The Act's name corrected in s.4.
3. A new s.18 "Notice for People in the EU, EEA and UK" (18.1–18.11), renumbering Contact Us to 19 and Acceptance to 20.

The draft also asks four questions (see Open, items 1–4), and recommends, as optional, sending only the lead reference to Meta for DE, NL and UK leads.

## Open

| # | Item | Who |
|---|---|---|
| 1 | Approve the privacy text; then Claude edits WordPress after Sanjeev logs in. No publishing before the text is approved. | Sanjeev, then Claude |
| 2 | Confirm Zoho's data processing addendum (EU standard contractual clauses plus the UK addendum) is signed; if not, request it from legal@zohocorp.com. 18.6 is not true until then. | Sanjeev |
| 3 | Retention for non-client EU/UK enquiries: 24 months proposed (18.7). A periodic CRM purge follows. | Sanjeev |
| 4 | Art. 27 representative: (a) appoint EU and UK representatives; (b) launch on the 7 non-EU/UK countries and add DE, NL and UK later (recommended); or (c) rely on Art. 27(2)(a). | Sanjeev |
| 5 | Optional: lead reference only (no hashed email or phone) in CAPI events for DE, NL and UK leads. Code diff to be shown before any save. | Sanjeev decides; Claude drafts |
| 6 | Booking page: new /book-a-consultation with the Zoho Bookings embed and the "Schedule a Call" links repointed (recommended), or the embed on /contact-us. Does a Bookings service for India-entry consultations exist? | Sanjeev |
| 7 | G3c: route …508 WhatsApp chats to Sales - FDI (brand departments and channel department). | Sanjeev's go, then Claude |
| 8 | G7–G13 per spec. G7 (Instant Form) waits for the privacy page and the Art. 27 decision. | Per spec |
| 9 | Later, outside this edit: s.16 says the Data Protection Board will act "once established", although it has been in force since 13 Nov 2025; s.4 lists "contractual necessity" as a DPDP legitimate use, which Sec. 7 of the DPDP Act does not contain. | Sanjeev |
