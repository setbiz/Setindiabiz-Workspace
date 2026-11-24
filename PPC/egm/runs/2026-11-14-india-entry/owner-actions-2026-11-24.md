# India Entry: owner action pack (24 Nov 2026)

Based on your answers in the decisions page (31 answers, 24 Nov) and your chat replies: no price in ads for now; launch Google and Meta on 25 Nov after you OK the previews.

## Status at a glance
| Item | State |
|---|---|
| Google `GADS_Search_IndiaEntry_US_Intent_202612` (24465038588) | Paused · 25 Nov–24 Dec · Branch-Liaison ad **approved** · original Subsidiary ad **disapproved** (Government documents & official services) · new advisory Subsidiary ad in review |
| Meta `META_Leads_IndiaEntry_US_Founders_202612` (120247551239970449) | Draft, not published · ₹60,000 cap · ad set 25 Nov–25 Dec · B2 + E2, no errors |
| Microsoft `MSADS_Search_IndiaEntry_US_Intent_202611` (689153594) | Created, paused · ₹500/day · Microsoft forced Enhanced CPC · negatives need a check in the UI |
| LinkedIn lead form "IE US v1" | Not created: the LinkedIn connection needs reconnecting with write access (step 1) |
| LinkedIn images | Brief emailed to Vipin 24 Nov, due 26 Nov |
| Site tags (GTM-WKF7QJSK) | GA4 G-95WXRV0791 ✓ · Google Ads AW-726050223 ✓ · Meta Pixel 1242417817083521 (PageView + Lead) ✓ · Microsoft UET ✓ · X pixel ✓ · **LinkedIn Insight Tag ✗** · Reddit pixel ✗ |

---

## 1. Reconnect LinkedIn in Supermetrics (2 minutes)
Open: https://api.supermetrics.com/v2/datasource/login/renew/4tejs8ad8cu2xy7baoacdx4c and sign in with the LinkedIn account that manages ad account 506114635. Accept the extended (campaign management) permissions. Then tell me and I'll resend the lead-form link.

## 2. LinkedIn audience (you chose to build it; about 15 minutes, after Vipin's images arrive)
Campaign Manager › account 506114635 "setindiabiz" (not Juriskps):
1. Campaign group `LI_IndiaEntry_US_202611`, total budget ₹60,000, end date 30 days after start.
2. Campaign `LI_LeadGen_IndiaEntry_US_DecisionMakers_202611`, objective **Lead generation**.
3. Audience: Location **United States** · Seniority **Owner, Partner, CXO, VP, Director** · Job function **Business Development, Entrepreneurship, Operations, Finance** · Company size **51–200, 201–500, 501–1,000** · Industries **Software Development; IT Services and IT Consulting; Manufacturing; Financial Services; Pharmaceutical Manufacturing**. Audience expansion **off**. LinkedIn Audience Network **off**.
4. Format: single image. Daily budget ₹2,000, Maximum delivery.
5. Ads (Vipin's images): **L1** intro text "Expanding to India? Choose the right structure first. Setindiabiz helps foreign companies set up an Indian subsidiary, branch office or liaison office, then handles the company filings and the FDI reporting to the Reserve Bank of India. Setindiabiz is a private professional services firm, not a government agency. Government fees extra, billed at cost." Headline "Set up your company in India". **L2** intro = the E2 Meta text + " Setindiabiz is a private firm, not a government agency." Headline "Which India structure fits you?". Lead form: "IE US v1" (once created).
6. Leave the campaign **paused** and tell me. I'll check it before go-live.

## 3. Install the LinkedIn Insight Tag (in GTM, about 5 minutes)
GTM container GTM-WKF7QJSK › Tags › New › "LinkedIn Insight" template › Partner ID from Campaign Manager › Analyze › Insight Tag › trigger **All Pages** › Submit/Publish. Without it, LinkedIn can't record website conversions or build retargeting audiences. Lead Gen Form leads still work.

## 4. Zoho workflows (you chose to do these; steps below)
**4a. QL Date stamp** (field already created on Leads and Deals)
Setup › Automation › Workflow Rules › Create Rule › Module **Leads** › name "Stamp QL Date".
- When: **Record action › Create or Edit** › "Repeat this workflow whenever a lead is edited" ✓.
- Condition: (Lead Status **is** Valid Lead, Need Analysis, Proposal Sent, Negotiation, Payment Pending) **AND** (QL Date **is empty**).
- Instant action: **Field update** › QL Date = **Execution Date** (date the rule ran).
- Save. Then Setup › Customization › Modules › Leads › **Lead Conversion Mapping** › map Leads.QL Date → Deals.QL Date › Save.

**4b. UTM fallback in the lead-source function**
Setup › Developer Hub › Functions › `autoClassifyLeadSource` › Edit. Find the line `// 2) PAID META via URL utm` and paste this block **just above it** (after the twclid block):
```
	else if(urlText.contains("utm_medium=cpc") && urlText.contains("utm_source=google"))
	{
		newSource = "Advt - Google";
	}
	else if(urlText.contains("utm_medium=cpc") && urlText.contains("utm_source=bing"))
	{
		newSource = "Advt - Microsoft";
	}
	else if(urlText.contains("utm_medium=cpc") && urlText.contains("utm_source=linkedin"))
	{
		newSource = "Advt - LinkedIn";
	}
	else if(urlText.contains("utm_medium=cpc") && urlText.contains("utm_source=reddit"))
	{
		newSource = "Advt - Reddit";
	}
	else if(urlText.contains("utm_medium=cpc") && urlText.contains("utm_source=chatgpt"))
	{
		newSource = "Advt - ChatGPT";
	}
```
Save. Test once: Leads › create a test lead with First Page Visited `https://www.setindiabiz.com/india-entry-services?utm_source=bing&utm_medium=cpc` → Lead Source should become **Advt - Microsoft**. Delete the test lead.

**4c. LinkedIn leads → Zoho (you chose LeadChain).** In LeadChain, create a chain for LinkedIn form "IE US v1": map name, email, company, job title, country, and the custom question → Description. Static values: Product Cat **FDI**, Lead Source **Advt - LinkedIn**, Tag **FB-FDI** (so the India Entry assignment rule picks it up). If LeadChain has no LinkedIn source, use Zoho CRM › Marketplace › LinkedIn Lead Gen Forms.

## 5. Google Ads ↔ Zoho (you chose the native integration)
Zoho CRM › Setup › Marketplace › Google › **Google Ads** › Connect › choose account **1859576856** › tick "Import offline conversions". Map the stage **Lead Status = Valid Lead** → conversion "IE – Qualified lead" (create it as an offline "Import" conversion action in Google Ads first, counting **One**). Leave enhanced conversions **off** until the privacy update (step 6) is live.

## 6. Privacy update: prompt for your website session
Copy everything between the lines into the website session:

---
Update setindiabiz.com so that enquiry data may be used to measure our ads, with the legal basis in place. Do not change anything else on the site.
1. **Enquiry forms** (all forms, including /india-entry-services and /indian-subsidiary-registration): replace "Details used only to respond to your enquiry" with: "We use your details to respond to your enquiry. We may also share limited, hashed information (such as email or phone) with advertising platforms like Google, Meta and LinkedIn to measure how our ads perform. See our Privacy Policy." Link "Privacy Policy" to /privacy-policy.
2. **Privacy policy** (/privacy-policy): add a section "Advertising measurement" covering: the platforms (Google, Meta, Microsoft, LinkedIn); what's shared (hashed email/phone, ad click IDs, enquiry status); why (to measure and improve ad performance); that data isn't sold; how to opt out (email help@setindiabiz.com); retention matching the existing policy. Keep the existing EU/UK section 18.
3. Cite the governing law in the policy: Information Technology Act, 2000 s.43A and the Information Technology (Reasonable Security Practices and Procedures and Sensitive Personal Data or Information) Rules, 2011, r.4 and r.5. Note that the Digital Personal Data Protection Act, 2023 notice and consent provisions apply from 13 May 2027 under the DPDP Rules, 2025 (G.S.R. 846(E)); check the current commencement on meity.gov.in before publishing.
4. Fix two existing items: s.16 should say the Data Protection Board is constituted (Board provisions in force from 13 Nov 2025), and s.4 should not list "contractual necessity" as a DPDP legitimate use (s.7 of the DPDP Act has no such ground).
5. Show me the before and after text for approval before publishing.
---

## 7. Landing-page edits (from your answers)
- **C2:** USD 499 is the correct subsidiary price → update the Subsidiary page (it still shows Basic $349 / Silver $499 / Gold $799).
- **C3:** change "GST applies" to **"GST extra where applicable"**.
- **C5:** add near the form: "US clients: book a call 9 AM–1 PM ET (7:30–11:30 PM IST)" · "Invoices in USD; pay by wire or card" · the "independent consultancy, not a government body" line above the fold.
- **B3:** open Zoho Bookings slots **7:30–11 PM IST** for India Entry (evening only, as you chose).
- **E9:** new page "Starting a company in India from the US" (needed before phase 2). It should include an FAQ on foreign-citizen and OCI founders and when a founder becomes resident; no visa or layoff wording.

## 8. B2 image fix (you chose to do it)
Canva › "Ads 4:5 (1080×1350)" page 6 and "SIB-05 India Entry – 9:16 Stories/Reels" page 6: move the photo left (or crop the sign) so "BRANCH OFFICE" isn't cut off. Tell me when it's done and I'll swap the image in the Meta draft.

## 9. Microsoft checks in the UI (2 minutes)
ui.ads.microsoft.com › campaign 689153594:
- Ad groups › Keywords › **Negative keywords**: confirm the list is there (the connector couldn't read it back).
- Settings › **End date 24 Dec 2026**.
- Settings › Networks › **Microsoft sites and select traffic (owned & operated) only**.
- Bidding shows **Enhanced CPC** (Microsoft forced it). That's acceptable: max CPC stays ₹400 per ad group.
- **Conversion Tracking › UET tag** shows "Tag active"; add a goal "IE – Website lead" (destination URL contains the form thank-you page).

## 10. Go-live (needs your explicit "go")
When you say **"go Google + Meta"**, I will:
- **Google:** enable campaign 24465038588. The Branch-Liaison ad is approved; the Subsidiary ad group serves only if the advisory ad gets approved.
- **Meta:** publish draft campaign 120247551239970449 (B2 + E2). Spend is capped at ₹60,000.
- Log both, and check delivery and the first leads after 24 hours.
Microsoft and LinkedIn follow when steps 1–3 and 9 are done.
