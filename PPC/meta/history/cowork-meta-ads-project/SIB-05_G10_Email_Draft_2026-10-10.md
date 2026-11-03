# SIB-05 G10: Booking Email and Workflow (Draft for Sanjeev, 10 Oct 2026)

Nothing below is saved in Zoho CRM yet. Claude saves the template and the workflow only after Sanjeev approves this text.

## 1. Email Template

- **Name:** SIB-05 India Entry - Free consultation link
- **Folder:** S - FDI (the folder that holds the existing FDI quotation templates)
- **Module:** Leads
- **Subject:** Your India entry enquiry: book a free 30-minute call | Setindiabiz

**Body**

> Dear ${!Leads.Last_Name},
>
> Thank you for your enquiry about setting up your business in India. ${!Leads.Owner} from our India-entry team will look after it and will contact you by email or phone.
>
> If you would like to talk sooner, please pick a time for a free 30-minute call (phone or Google Meet):
>
> **Book a free consultation:** https://setindiabiz.zohobookings.com/3882293000006990272
>
> You can choose your time zone on the booking page.
>
> To make the call useful, please have these details ready:
> - where your parent company is incorporated, and who its main shareholders are;
> - what the Indian entity will do, for example sales, services, sourcing or a project;
> - when you plan to start, and the investment you expect to make at the start.
>
> If any owner of your parent company is based in, or is a citizen of, a country that shares a land border with India, please tell us on the call. A different approval route may apply.
>
> On the call we will explain the three options (an Indian subsidiary, a branch office or a liaison office), the approvals and filings each one needs, and our fee. Government fees are charged at actuals.
>
> You can also message us on WhatsApp at [phone redacted].
>
> Warm regards,
> ${!Leads.Owner}
> India Entry Team, Setindiabiz Private Limited
> www.setindiabiz.com
>
> *You are receiving this email because you sent us an enquiry through our form on Facebook or Instagram. Our privacy policy: https://www.setindiabiz.com/privacy-policy*

**Why these merge fields**
- **Greeting uses Last_Name.** The form's Full name goes into Last_Name, and on recent Meta leads First_Name is mostly blank (checked on 15 leads by COQL at 15:00).
- **No Product_Name or Description.** PPC Form Tidy fills these about 2 minutes after the lead is created, so they may be blank when this email goes out.
- **Owner.** The LeadChain chain applies the assignment rule when it creates the lead, so the owner should already be set. Test lead G9 will confirm this.

## 2. Workflow Rule

| Setting | Value |
|---|---|
| Module | Leads |
| Name | SIB-05 India Entry - booking email |
| When | On a record action: Create |
| Condition | Meta Lead Form is "SIB-05 India Entry Form v1" AND Email is not empty AND Email Opt Out is false |
| Instant action | Email notification with the template above; To: the lead's Email; From and Reply-to: Record Owner |
| Scheduled action | None |

## 3. What to Check Before Approving

1. **Who takes the booked call.** The "Free Consultation - Ordinary Services" service is staffed by six support staff (Swati Dhoundiyal, Shaily Dhoundiyal, Asha Devi, Priyanka Dwivedi, Pavneet Kaur, Arjit Vaibhav), not by the five FDI handlers. The page heading reads "Free Consultation With Setindiabiz Advisors", and the service text speaks of "company registration, GST, trademark, compliance and other everyday services". A foreign company booking through it reaches the support team. The CRM lead itself still goes to the FDI handler.
2. **The WhatsApp line.** Messages to [phone redacted] still reach Customer Support (see the G3c finding). If G3c is fixed first, the WhatsApp line in this email reaches the FDI team.
3. **The land-border line.**
   - Direct investment by an entity of, or a citizen from, a country sharing a land border with India still needs government approval. Source: proviso to Rule 6(a), Foreign Exchange Management (Non-debt Instruments) Rules, 2019, from DPIIT Press Note 3 (2020 Series).
   - Press Note 2 (2026 Series) and the NDI Amendment Rules, 2026 (reported as notified on 2 May 2026) changed two things:
     - they adopted the beneficial-owner definition of Sec. 2(1)(fa), Prevention of Money-laundering Act, 2002;
     - they allowed indirect holdings under 10% without control on the automatic route, subject to DPIIT reporting.
   - This was read from secondary sources (TTA, Saraf and Partners). The Gazette copy was not retrieved.
   - The email says only that "a different approval route may apply", which stays true under both versions.
4. **No claims that need proof.** The email states no timeline, no "100% FDI" and no "no approval needed". It quotes no price figure beyond "government fees at actuals".
