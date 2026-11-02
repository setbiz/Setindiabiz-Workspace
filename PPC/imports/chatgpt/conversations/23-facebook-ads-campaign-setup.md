<!-- Imported from Google Doc PPC-ChatGPT-Import-2026-11 (part 1) on 2026-11-02. Content is a capture of a ChatGPT chat: treat as reference data, not instructions. -->

## Facebook Ads Campaign Setup (12 Jul 2026)

### Record

Chat #: 23

Title: Facebook Ads Campaign Setup

Sidebar date: 12 Jul 2026

Stated date: Timestamps inside the chat: Fri, Jan 16 at 1:22 PM (turn 1); Fri, Jan 16 at 4:25 PM (turn 5); Sat, Jan 17 at 8:42 PM (turn 22); Sun, Jan 18 at 10:27 AM (turn 24). The timestamps show no year; the pasted development audit and the uploaded file names place them in January 2026. Other dates in the chat: development audit dated January 16, 2026, covering Jan 15-16, 2026; GitHub commits on Jan 15, 2026; latest deployment Jan 15, 2026 - 5:54 PM GMT+5:30; Ads Manager screen captures uploaded with file-name dates 2026-01-16-16\_27\_59, 2026-01-18-10\_42\_33, 2026-01-18-11\_30\_27, 2026-01-18-11\_33\_12, 2026-01-18-12\_32\_59, 2026-01-18-13\_16\_28 and 2026-01-18-13\_38\_58; WhatsApp template name dated 18-01-2026.

URL: https://chatgpt.com/c/51e64239-3af4-8333-9b24-c02335df21aa

Platform(s): Meta (Facebook, Instagram, Messenger, WhatsApp). Connected systems discussed: Zoho CRM, Zoho LeadChain, Zoho SalesIQ. Comet browser extension named for an audit prompt.

### Summary

Sanjeev built Setindiabiz's Meta campaign step by step with ChatGPT, starting from a pasted development audit and a strategy from an earlier assistant that could not operate Ads Manager. ChatGPT reduced the plan to four Advantage+ Leads campaigns (Company and LLP, Indian Subsidiary and India Entry, Trademark, GST), and only Company and LLP for Indian metros was actually built in this chat.

He built a Leads campaign with an Instant Forms ad set (3 ads) and a Website-First ad set (2 ads), a value rule of +20% for website and -30% for forms, and Zoho LeadChain for form leads. He then set up a separate WhatsApp Messages campaign with a Chat Builder template, with the WhatsApp number integrated into Zoho SalesIQ.

He settled a naming tag (IN, then IND, then #IND) and created two Automated Rules for 09:30 to 19:30 IST delivery.

He said IND campaigns should not spend more than 10K a day, then skipped budget optimisation for now. The chat ended with a status report and a Comet browser audit prompt. No campaign performance data appears in the chat.

### Decisions made and why

Turn 1, in the conversation he pasted from an earlier assistant: asked for a new campaign using Meta's AI models such as Andromeda, run in auto mode, targeting people actively looking for Setindiabiz services, for Company Registration (Indian major metros), Indian Subsidiary Registration (foreigners), Trademark Registration (foreigners) and GST Registration and Return Filing (India major cities). He preferred all options: Direct Lead Form, Visit to landing pages and WhatsApp chats. Creatives were ready.

Turn 1, pasted: replied Yes Ok to that assistant's plan of ₹160,000/month across 4 campaigns. That assistant could not then create the campaigns.

Turn 2: work step by step, with ChatGPT giving instructions and Sanjeev implementing them. At turn 3 he asked whether ChatGPT could do it as an AI agent and was told it could not.

Turn 4: skip tracking verification and go to campaign setup, because he had verified tracking earlier.

Turns 5 to 8: accepted Website and instant forms as the conversion location, because Meta did not offer all three surfaces in one option, and connected the existing Setindiabiz JS dataset rather than creating a new pixel, because a new pixel would fragment tracking (ChatGPT's reason).

Turn 10: keep ₹2,500 per day for the company registration campaign instead of ₹1,300. His reason, stated at turn 33 for the same figure: keep approx 20 sales staff busy.

Turn 11: accepted minimum age 24 with no upper cap, because Meta offered only a minimum age in this flow.

Turn 18: keep ads in Draft until all ads were built. Published at turn 21 after errors were cleared.

Turn 22: proposed adding Jammu and Kashmir and North East, looking for locations with less competition and likely business.

Turn 23: create that alternate ad set only after all ads are created.

Turns 26 to 29: did not use Website and calls (ChatGPT advised against it because calls would dilute the learning signal and make attribution messy). Accepted value rules of +20% for website and -30% for forms in place of the -90% then on his screen, to prefer website conversions without stopping forms.

Turn 32: chose a separate WhatsApp Messages campaign, to avoid mixing objectives.

Turn 33: for WhatsApp he preferred ₹2,500 per day so that approx 20 sales staff remain busy, with ₹1,500 to ₹2,000 acceptable because other campaigns will be created.

Turn 34: run in working hours, 9:30 am to 7:30 pm, on all campaigns, because most leads come during the day and that is when the team works.

Turn 35: use Automated Rules with daily budgets (Method B) rather than lifetime budgets with ad scheduling.

Turns 40, 55 and 56: India naming tag moved from IN to IND to #IND. Reason: rule conditions offer contains, not starts with, and a unique tag keeps rules away from future USA campaigns (raised at turn 38).

Turn 45: exclude WhatsApp Status placement until 9:16 creatives exist, because the creatives are square.

Turns 48 to 50: use Zoho SalesIQ and Zobot for WhatsApp messages, with the WhatsApp number integrated into SalesIQ.

Turn 53: use all three WhatsApp angles (pricing, register today, trust or online) and work on timing after the ads are created.

Turn 61: used All paused campaigns on the ON rule because that was the only option in his dropdown.

Turn 63: apply the business hours rules to all #IND campaigns.

Turn 64: should not spend more than 10K for IND campaigns in a day. No reason given.

Turn 65: skip budget optimisation for now, so the spend cap options were not taken up.

### Changes made in ad accounts

Only actions Sanjeev reported, or that ChatGPT read from his uploaded screens, are listed. Where a turn has no timestamp of its own, the date range comes from the timestamps either side of it.

  

Before the build (turn 1, pasted): the earlier assistant reached Ads Manager but campaign creation was blocked by browser extension restrictions, so it created nothing. The Jan 15, 2026 work (Meta Conversions API settings, Zoho CRM environment variables, PR #2542 merged and deployed) was made in the website code, not in the ad account.

  

Fri Jan 16 (turns 5 to 11): Leads campaign and one ad set created in ad account SETINDIABIZ (152154124583473), conversion location Website and instant forms, dataset Setindiabiz JS and conversion event Lead, after the existing dataset was connected to the ad account (Sanjeev confirmed it was selectable at turn 8). Campaign daily budget ₹2,500 kept. Minimum age set to 24. Ads moved to Ad level at turn 12. Sanjeev was told at turn 9 to replace India with the metro list; turn 10 ChatGPT asked him to confirm it; his next message moved on to age.

  

Fri Jan 16 to Sat Jan 17 (turns 12 to 21): Instant Form built; ChatGPT read the form C1 | Company+LLP | Higher Intent | v1 as selected on Ad 1 (turn 16). Three form ads built: Pricing, Register Today and 100% Online. Publishing first failed for all three with link field errors (turn 20). Website URLs were added, errors cleared and Sanjeev reported Ads Published (turn 21).

  

By Sat Jan 17 (turn 23): Zoho LeadChain configured for the first ad, per Sanjeev.

  

Sun Jan 18 from 10:27 AM (turns 24 to 31): second ad set duplicated. Value rules created: +20% for website and -30% for form (Sanjeev, turn 29). Website ads published (Sanjeev, turn 31). His campaign screen at turn 24 showed Daily budget ₹3,500; the chat does not say whether it was changed.

  

Sun Jan 18 (turn 41): campaign, ad sets and ads renamed; ChatGPT read from his screen: campaign IN | C1 | Company+LLP | Leads | …, ad sets IN | C1 | Web | Metros | Website-First and IN | C1 | Forms | Metros | Broad, ads W1/W2 and F1/F2/F3.

  

Sun Jan 18 (turns 42 to 47): WhatsApp campaign created at about 11:30 per file names, objective Engagement, Ad set budget. Ad set moved from Conversion location Website at ₹800/day (turn 43) to Message destinations with WhatsApp selected at ₹2,000/day (turn 44). WhatsApp Status unticked and the warning cleared (Sanjeev, turn 47).

  

Sun Jan 18 (turns 48 to 52): WhatsApp number integrated with Zoho SalesIQ (Sanjeev, turn 50). Chat Builder template created with welcome message, business hours and FAQ buttons (ChatGPT read this from his screen at turn 52, about 13:38 per file name).

  

Sun Jan 18 (turn 54): he wrote Create all the three ads, which ChatGPT treated as the three WhatsApp ads being created. Publication was not separately confirmed; the turn 65 report says the WhatsApp workstream was initiated.

  

Jan 18 or later (turns 55 to 62): two Automated Rules created at campaign level. ChatGPT read both from his screen at turn 62: ON applies to All paused campaigns, Turn on campaigns, campaign name contains #IND; OFF applies to All active campaigns, Turn off campaigns, campaign name contains #IND. The ON rule name on screen still said 19:29.

  

Not done in the chat: Tier 2, J\&K and North East ad set; campaigns for Indian Subsidiary, Trademark and GST; spend cap rules.

### Metrics and results

No campaign results (spend, impressions, leads, cost per lead) appear in this chat. Every figure below is an account or setup fact, or an estimate.

  

From Sanjeev's data or his Ads Manager screens:

Budget remaining: ₹1,431,574.38; 1 active campaign and some draft campaigns (turn 1, read from Ads Manager by the earlier assistant in the pasted conversation).

Development audit, turn 1: Build Duration: 13m 7s; Error Rate: 0.0%; PR #2542.

Company campaign daily budget on screen: ₹2,500 (turns 6, 9, kept at turn 10); ₹3,500 (turn 24).

WhatsApp ad set daily budget on screen: ₹800/day (turn 43); ₹2,000/day (turn 44).

Staff and hours: approx 20 sales staff (turn 33); start at 9:30 am and work until 7:30 pm (turn 34).

Spend limit stated: not more than 10K for IND Campaigns in a aday (turn 64).

Meta's rule screen, as quoted by ChatGPT at turn 57: “If the start and end time are the same, then the rule will run once per day within 30–60 minutes after the set time.”

  

Earlier assistant's benchmarks and estimates (pasted in turn 1, not Sanjeev's data):

Lead Form: conversion rate 2-4%, cost per result ₹800-2000.

Landing Page Visits: conversion rate 3-5%, cost per result ₹600-1500.

WhatsApp Chat: conversion rate 1-3%, cost per result ₹1500-4000.

Set cost per lead target: ₹1000-1500. Cost per Lead Target: ₹1200.

Audience Size: Should show 5-10M people; launch checklist says audience size 5-20M.

Daily budget ₹200-700 per day per ad set.

Key metrics table: Cost per Lead ₹800-1500; Lead Quality 70%+ qualified; Landing Page CTR 2-5%; WhatsApp Response Rate 40%+; Impressions 10K+ daily.

  

ChatGPT's estimates and benchmarks (not Sanjeev's data):

Turn 1: Conversion volume per campaign is ≥50/week for Andromeda; “This single question increases lead quality by \~30%.”

Turn 4: ₹1,300 per day (\~₹40,000 / month).

Turn 10: ₹2,500/day is roughly ₹75,000/month.

Turn 31: proposed pause threshold Cost per result (Lead) \> ₹1,800 AND Results ≥ 3.

Turn 32: Benchmarks (India): Good start: ₹40–₹120 per conversation; ₹200+ consistently after 20 conversations means change creative, copy or targeting.

Turn 33: WhatsApp conversation started around ₹60–₹150; ₹1,500/day → \~10 to 25 conversations/day; ₹2,000/day → \~13 to 33 conversations/day; ₹2,500/day → \~16 to 41 conversations/day.

Turn 41: scale to ₹2,500/day if cost per WhatsApp conversation is ≤ ₹120.

Turn 64: keep total #IND daily budgets around ₹8,000–₹8,500 for a hard ₹10k cap; C1 ₹2,500/day plus WA1 ₹2,000/day totals ₹4,500/day; spend cap example ₹2,600.

### Verbatim assets

Assets run in turn order. Each label gives type, turn and author. A label says FINAL only where the chat confirms what was used, or where it is the last version given (and then it says so).

  

Full prompt with pasted development audit and earlier assistant conversation, turn 1, Sanjeev

  

help me build a ROBUST FACEBOOK ADS CAMPAIN, REFER BELOW

  

DEVELOPMENT AUDIT & INTEGRATION SUMMARY - Jan 15-16, 2026

TO: Development Team

FROM: [Your Name]

DATE: January 16, 2026

RE: GitHub Commits & Integration Changes (Past 24 Hours)

  

OVERVIEW

Over the past 24 hours, I completed a comprehensive audit and implementation of our Meta Ads and Zoho CRM integrations in the NextJS project. Below is a detailed breakdown of all changes made to the GitHub repository.

  

KEY GITHUB COMMITS (Jan 15, 2026)

1\. Zoho CRM Integration Setup

Commit: e51ecd5542b3426e7bd6b8b6aea05aed4d192ef5

Time: Jan 15, 1:01 PM GMT+5:30

Message: "Add Zoho CRM integration environment variables"

What was done:

  

Added Zoho CRM OAuth credentials to .env.local

Configured the following environment variables:

  

ZOHO\_ORG\_ID - Organization identifier

ZOHO\_OAUTH\_TOKEN - API access token

ZOHO\_REFRESH\_TOKEN - Token refresh mechanism

ZOHO\_API\_DOMAIN - Set to India endpoint (https://www.zohoapis.in)

ZOHO\_WEBHOOK\_SECRET - Webhook security

ZOHO\_CLIENT\_ID & ZOHO\_CLIENT\_SECRET - OAuth credentials

  

Status: ✅ COMPLETE - Ready for production deployment

  

2\. Zoho CRM Setup Guide Documentation

Commit: 23815de23cbdc8c46e125c50470e726b2dfb1653

Time: Jan 15, 1:03 PM GMT+5:30

Message: "docs: Add comprehensive Zoho CRM integration setup guide"

What was done:

  

Created ZOHO\_SETUP\_GUIDE.md with step-by-step instructions

Documented all required environment variables

Included API domain setup for different regions

Added security best practices for webhook handling

Provided examples and expected value formats

  

Status: ✅ COMPLETE - Reference documentation created

  

3\. Meta Conversions API Configuration

Commit: e51ecd5542b3426e7bd6b8b6aea05aed4d192ef5

Time: Jan 15, 1:01 PM GMT+5:30

Message: "Add Zoho CRM integration environment variables" (also includes Meta config)

What was done:

  

Configured Meta Conversions API tokens in .env.local:

  

NEXT\_PUBLIC\_PIXEL\_ID - Pixel identifier

NEXT\_PUBLIC\_PIXEL\_ACCESS\_TOKEN - Token for pixel

NEXT\_PUBLIC\_BUSINESS\_ACCOUNT\_ID - Business account (629080835992237)

NEXT\_PUBLIC\_CONVERSIONS\_API\_VERSION - Set to v18.0

META\_CONVERSION\_API\_TOKEN - Server-side API token

  

Status: ✅ COMPLETE - Meta Pixel connected

  

4\. ESLint & Build Configuration Fix

Commit: 1ccde9a952c7237566e22bfa6ffe830ef8228e09

Time: Jan 15, 3:00 PM GMT+5:30

Message: "fix: Disable ESLint rules causing build failure and move conversion tracking to root layout for all pages"

What was done:

  

Updated .eslintrc.json to disable conflicting rules

Moved conversion tracking initialization to root layout (app/(home)/layout.tsx)

Ensured Meta pixel and Conversion API fires on all pages

Fixed TypeScript/ESLint compilation errors

  

Status: ✅ COMPLETE - Build now passes successfully

  

5\. Type Exports Fix for Zoho Integration

Commit: 256799e08f477b721b16b0cc281f41fe19fb96ea

Time: Jan 15, 3:27 PM GMT+5:30

Message: "fix: Use 'export type' for type-only re-exports in Zoho integration"

What was done:

  

Fixed TypeScript strict mode issues in Zoho integration module

Changed regular exports to export type for type-only exports

Ensured proper module resolution

Eliminated unnecessary runtime imports

  

Status: ✅ COMPLETE - TypeScript strict mode compliant

  

6\. ConversionTracker Component Removal

Commit: 8ede22213a20117091990ccf429eafd697d2009a

Time: Jan 15, 3:39 PM GMT+5:30

Message: "fix: Remove unused ConversionTracker import that was causing build failure"

What was done:

  

Removed unused ConversionTracker component import from app/(home)/layout.tsx

This import was causing build failures

Conversion tracking now handles via direct Meta pixel and Conversions API calls

Simplified the layout component structure

  

Status: ✅ COMPLETE - Removed redundant code

  

7\. Final Merge to Production

Commit: 300299d43f1f18fee2b2a036793ae83a0e2469e7

Time: Jan 15, 5:51 PM GMT+5:30

Message: "Merge pull request #2542 from setbiz/sibDeveloper"

What was done:

  

Merged all integration changes to main branch

PR #2542 completed and merged

All changes ready for production deployment

  

Status: ✅ DEPLOYED - Now live on production

  

CURRENT STATE OF CODEBASE

Environment Variables Configured:

Meta Conversions API:

\- NEXT\_PUBLIC\_PIXEL\_ID

\- NEXT\_PUBLIC\_PIXEL\_ACCESS\_TOKEN

\- NEXT\_PUBLIC\_BUSINESS\_ACCOUNT\_ID

\- NEXT\_PUBLIC\_CONVERSIONS\_API\_VERSION

\- META\_CONVERSION\_API\_TOKEN

  

Zoho CRM Integration:

\- ZOHO\_ORG\_ID

\- ZOHO\_OAUTH\_TOKEN

\- ZOHO\_REFRESH\_TOKEN

\- ZOHO\_API\_DOMAIN

\- ZOHO\_WEBHOOK\_SECRET

\- ZOHO\_CLIENT\_ID

\- ZOHO\_CLIENT\_SECRET

  

Other:

\- INTERNAL\_API\_SECRET

\- NEXT\_PUBLIC\_API\_URL

Build Status: ✅ PASSING

Latest Deployment: Jan 15, 2026 - 5:54 PM GMT+5:30

Build Duration: 13m 7s

Error Rate: 0.0%

Status: PRODUCTION READY

  

META ADS ACCOUNT CONFIGURATION

Account Details:

  

Business Portfolio: Setindiabiz Private Limited (ID: 629080835992237)

Ad Account: SETINDIABIZ (ID: 152154124583473)

Active Pixel: Setindiabiz JS (ID: 1242417817083521)

Conversion API: Active (Signals Gateway)

Status:\*\* ✅ FULLY OPERATIONAL

  

INTEGRATION STATUS SUMMARY

ComponentStatusDetailsMeta Pixel✅ ActiveConnected and receiving eventsConversion API✅ ActiveServer-side tracking operationalZoho CRM Integration✅ ConfiguredEnvironment variables set, ready for useNextJS Build✅ PassingNo errors, deployed to productionVercel Deployment✅ ProductionLive on www.setindiabiz.comESLint/TypeScript✅ CompliantStrict mode enabled and passing

  

IMPORTANT NOTES FOR DEVELOPERS

Do NOT Modify:

  

.env.local values for Meta and Zoho credentials (these are sensitive)

Production environment variables on Vercel without testing first

  

When Adding New Features:

  

Ensure conversion tracking calls are made (pixel + API)

Test Zoho CRM data submission on staging before production

Keep ESLint rules updated as per our configuration

  

Testing Recommendations:

  

Test Meta pixel events using Meta's Test Events feature

Verify Zoho CRM records are created for new leads

Check Vercel logs for any API failures

Monitor Events Manager for proper event volume

  

Documentation:

  

Refer to ZOHO\_SETUP\_GUIDE.md for Zoho integration details

All environment variables documented in this guide

See .env.local for current configuration

  

NEXT STEPS

  

Monitor production for the next 48 hours

Verify conversion data is flowing to Meta and Zoho

No immediate action required - system is fully operational

Report any issues in team chat if events aren't tracking properly

  

QUESTIONS OR ISSUES?

If you encounter any of the following:

  

Build failures related to Meta/Zoho integrations

Events not tracking in Events Manager

Zoho CRM records not being created

TypeScript compilation errors

  

Please check:

  

Environment variables are properly set in Vercel

.env.local has correct tokens and IDs

Network requests in browser DevTools (check API calls)

Console messages for any integration errors

  

Last Updated: January 16, 2026

By: [Your Name]

Next Review: After first campaign launch

  

You can now copy this entire text and paste it into an email to Anshu\!Conversation compactedConversation summaryWell can you setup ads for meI can help you set up ads for Meta Ads\! However, I need some clarification about what you'd like to do.

Are you looking to:

  

Create a new ad campaign - If so, I'll need details like:

  

What product/service are you promoting?

What's your target audience (location, age, interests, etc.)?

What's your budget?

What's the campaign goal (awareness, conversions, traffic, etc.)?

  

Set up ad account structure - Creating ad sets, audiences, or creative assets?

Configure conversion tracking - Set up pixels or conversion events for your ads?

Connect to your existing setup - Linking your ads to the Meta Conversions API and Zoho CRM integration we just verified?

  

Since we just verified that your Meta Conversions API is active and working with the "Setindiabiz JS" pixel (ID: 1242417817083521), any ads you create will automatically track conversions through that setup and sync with your Zoho CRM.

Let me know what you'd like to set up, and I'll guide you through it\!I would like to create a new campaign that takes advantage of all ai models of meta like androimeda and run that ads in auto mode and target those people which is actively looking for setindiabiz services, in particular i would like to setup campaigns for the following products

Company Registration - Indian Major Metros

Indian Subsidiary Registration - Target foreigners

Trademark Registration - Target Foreigners

GST Registration and Return Filing - Targeting India Major Cities

Creatives are ready and i will upload, you create everything I would prefer all options, Direct Lead Form, Visit to landing pages, Whatsapp chatswhat you think is best. The url of landing pages are as under, plan cxampaign for all of thesehttps://www.setindiabiz.com/lp/company-registrationhttps://www.setindiabiz.com/lp/llp-registration"https://www.setindiabiz.com/lp/trademark-registrationhttps://www.setindiabiz.com/lp/gst-registrationhttps://www.setindiabiz.com/lp/startup-india-dpiit-recognitionhttps://www.setindiabiz.com/lp/indian-subsidiary-registrationhttps://www.setindiabiz.com/lp/india-entry-servicesI appreciate the detailed request\! However, I need to be transparent about what I can and cannot do here.

What I can help with:

  

Planning the campaign structure and strategy

Setting up the account architecture, ad sets, and targeting parameters

Configuring conversion tracking to Zoho CRM

Creating the organizational structure in Meta Ads Manager

  

What I cannot do:

Creating and launching actual ad campaigns requires explicit user permission because:

  

Campaigns spend real money - This is a financial transaction that requires your direct authorization

Publishing to the public - Ads are published content that affects your brand

Account modifications - Creating campaigns modifies your ad account structure

  

Here's what I recommend:

Let me first create a detailed campaign strategy document that outlines:

  

Campaign Structure for each product:

  

Company Registration (Indian metros)

Indian Subsidiary Registration (foreigners)

Trademark Registration (foreigners)

GST Registration (major cities)

Plus the other landing pages you provided

  

Campaign Objectives Comparison:

  

Lead Form submissions

Landing page visits

WhatsApp chat initiations

Pros/cons of each for your services

  

Targeting Strategy:

  

Audiences for each product

AI model recommendations (Andromeda advantage)

Budget allocation suggestions

Ad placement optimization

  

Meta AI Features:

  

How to enable Advantage+ campaigns

Andromeda model utilization

Auto-optimization settings

  

Then you can:

  

Review and approve the strategy

Upload your creatives

Give me explicit permission to create the campaigns in Meta Ads Manager

Monitor performance in real-time

  

Would you like me to create this detailed campaign strategy plan first? Once you review and approve it, we can proceed with actual setup.alright6 stepsPerfect\! I'm now in your Meta Ads Manager. I can see you have:

  

Account: SETINDIABIZ (152154124583473)

Budget remaining: ₹1,431,574.38

1 active campaign and some draft campaigns

  

Now let me create a comprehensive campaign strategy document for your 4 main products. Here's the detailed plan:

  

ð SETINDIABIZ META ADVERTISING CAMPAIGN STRATEGY

CAMPAIGN OVERVIEW

Total Campaigns: 4 main product campaigns

Campaign Duration: Ongoing (with optimization phases)

Total Budget Available: ₹1,431,574.38

Suggested Monthly Allocation: ₹150,000 - ₹200,000 (scalable based on performance)

  

CAMPAIGN 1: COMPANY REGISTRATION - INDIAN MAJOR METROS

Product: Company Registration

Target Audience: Entrepreneurs, business owners, startups in India's major metros (Delhi, Mumbai, Bangalore, Hyderabad, Chennai, Pune, Ahmedabad)

Landing Page: https://www.setindiabiz.com/lp/company-registration

Campaign Structure:

  

Campaign Name: Company Registration - Metro Cities

Campaign Objective: Leads (Lead Form) + Conversions (Landing Page Visit) + Messages (WhatsApp)

Budget: ₹40,000/month (split across 3 ad sets)

  

Ad Sets (3 variations):

Ad SetObjectiveAudiencePlacementBudgetCompany Reg - Lead FormLead GenerationEntrepreneurs, Business Owners (Age 25-55, Major Metros, Income: Upper Middle+)Facebook/Instagram Feed, Stories₹15,000Company Reg - Landing PageTraffic/ConversionsInterested in Business Services, Previously visited setindiabiz.comFacebook/Instagram Feed, Stories, Reels₹15,000Company Reg - WhatsAppDirect MessagesEngaged audiences, High purchase intentInstagram Stories, Facebook Stories, Messenger₹10,000

Targeting Details:

  

Locations: Delhi, Mumbai, Bangalore, Hyderabad, Chennai, Pune, Ahmedabad

Age: 25-55 years

Interests: Business Registration, Startups, Entrepreneurship, Company Formation, Legal Services

Lookalike Audiences: Based on existing CRM contacts (from Zoho)

Exclusions: Page followers (if they're already engaged), past converters

  

AI Model: Andromeda (Advantage+ Campaigns)

  

Enable automatic creative optimization

Allow platform to test different audiences

Use broader targeting (let AI narrow down)

Meta will rotate best-performing creative versions

  

CAMPAIGN 2: INDIAN SUBSIDIARY REGISTRATION - TARGET FOREIGNERS

Product: Indian Subsidiary Registration

Target Audience: Foreign companies, international entrepreneurs, NRIs, expats looking to expand to India

Landing Page: https://www.setindiabiz.com/lp/indian-subsidiary-registration

Campaign Structure:

  

Campaign Name: Indian Subsidiary Registration - Global

Campaign Objective: Leads + Conversions + Messages

Budget: ₹40,000/month

  

Ad Sets (3 variations):

Ad SetObjectiveAudiencePlacementBudgetSubsidiary - Lead FormLead GenerationExpats, NRIs, International Business (Age 28-60, English speakers, US, UK, Canada, Australia, Middle East)LinkedIn-like audience (Business interests)₹15,000Subsidiary - Landing PageTraffic/ConversionsPeople interested in India market entry, business expansion, foreign investmentFacebook/Instagram Feed, Stories₹15,000Subsidiary - WhatsAppDirect MessagesHigh-value prospects, international business ownersMessenger, WhatsApp, Instagram Direct₹10,000

Targeting Details:

  

Locations: USA, UK, Canada, Australia, UAE, Singapore, Germany, France (countries with active business interest in India)

Age: 28-60 years

Languages: English (primary)

Interests: International Business, India Business, Company Expansion, Foreign Investment

Lookalike Audiences: Based on Zoho CRM contacts from foreign countries

  

AI Model: Andromeda (Advantage+ Campaigns)

  

Global audience optimization

Language-based ad variations

Currency optimization for international payments

  

CAMPAIGN 3: TRADEMARK REGISTRATION - TARGET FOREIGNERS

Product: Trademark Registration

Target Audience: International companies, product brands, foreign entrepreneurs protecting intellectual property

Landing Page: https://www.setindiabiz.com/lp/trademark-registration

Campaign Structure:

  

Campaign Name: Trademark Registration - International

Campaign Objective: Leads + Conversions + Messages

Budget: ₹35,000/month

  

Ad Sets (3 variations):

Ad SetObjectiveAudiencePlacementBudgetTrademark - Lead FormLead GenerationBusiness owners, Brand owners, IP-conscious entrepreneurs (Age 25-60, International, High income)Business-focused placements₹12,000Trademark - Landing PageTraffic/ConversionsPeople interested in IP protection, brand registration, trademark servicesFacebook/Instagram₹12,000Trademark - WhatsAppDirect MessagesPremium audience, high-value clientsWhatsApp, Messenger₹11,000

Targeting Details:

  

Locations: USA, UK, Canada, Australia, EU countries, Singapore, Middle East

Age: 25-60 years

Interests: Intellectual Property, Brand Management, Trademark Protection, Business Law

Audience Type: Lookalike from premium Zoho CRM contacts

  

AI Model: Andromeda (Advantage+ Campaigns)

  

Premium audience targeting

International payment optimization

High-value lead filtering

  

CAMPAIGN 4: GST REGISTRATION & RETURN FILING - MAJOR INDIAN CITIES

Product: GST Registration and Return Filing

Target Audience: Small businesses, traders, shop owners, service providers in major Indian cities

Landing Page: https://www.setindiabiz.com/lp/gst-registration

Campaign Structure:

  

Campaign Name: GST Registration & Filing - Major Cities

Campaign Objective: Leads + Conversions + Messages

Budget: ₹45,000/month

  

Ad Sets (3 variations):

Ad SetObjectiveAudiencePlacementBudgetGST - Lead FormLead GenerationShop owners, traders, business owners (Age 30-65, Major cities, Income Middle class+)Facebook/Instagram Feed₹16,000GST - Landing PageTraffic/ConversionsSmall business owners, traders, service providersFacebook Feed, Stories, Reels₹16,000GST - WhatsAppDirect MessagesExisting business owners, high compliance intentWhatsApp, Messenger, Instagram Direct₹13,000

Targeting Details:

  

Locations: Delhi NCR, Mumbai, Bangalore, Hyderabad, Chennai, Pune, Ahmedabad, Kolkata, Jaipur

Age: 30-65 years

Interests: Business Accounting, GST Compliance, Tax Services, Bookkeeping, Trader, Small Business

Lookalike Audiences: Based on Zoho CRM clients in GST category

  

AI Model: Andromeda (Advantage+ Campaigns)

  

Seasonal optimization (GST filing deadlines)

High-frequency targeting for compliance-conscious audience

  

ADDITIONAL LANDING PAGES - SECONDARY CAMPAIGNS (Optional)

You also provided these landing pages:

  

Startup India DPIIT Recognition: https://www.setindiabiz.com/lp/startup-india-dpiit-recognition

LLP Registration: https://www.setindiabiz.com/lp/llp-registration

India Entry Services: https://www.setindiabiz.com/lp/india-entry-services

  

Recommendation: Create smaller secondary campaigns (₹15,000-20,000/month each) for these, or include them as additional ad variations within the main campaigns above.

  

ð¯ STRATEGIC RECOMMENDATIONS

1\. Objective Comparison - Which is BEST for Setindiabiz?

ObjectiveBest ForConversion RateCost per ResultRecommendationLead FormDirect captures, instant Zoho CRM sync2-4%₹800-2000✅ PRIMARY - Best for your business modelLanding Page VisitsLonger consideration cycle, education3-5%₹600-1500✅ SECONDARY - Good for brand awarenessWhatsApp ChatDirect engagement, high conversion1-3%₹1500-4000✅ TERTIARY - For premium services

My Recommendation: Use ALL THREE in this ratio:

  

50% Budget → Lead Form (Direct Zoho CRM integration)

35% Budget → Landing Page Visits (SEO & brand authority)

15% Budget → WhatsApp (Premium high-touch service)

  

ð¤ META AI FEATURES TO ENABLE

Andromeda Model Benefits:

✅ Automatic audience optimization - AI finds best-fit customers

✅ Creative rotation - Tests different ad variations

✅ Real-time bidding - Adjusts bids based on conversion likelihood

✅ Cross-platform optimization - Balances Facebook, Instagram, Messenger, WhatsApp

✅ Seasonal adjustments - Learns from your business patterns

Advantage+ Campaign Setup:

  

Provide 3-5 creative variations per campaign

Allow Meta to choose audience automatically

Set cost per lead target: ₹1000-1500

Enable conversions optimization (synced to Zoho)

  

ð BUDGET ALLOCATION SUMMARY

CampaignMonthly BudgetLead FormLanding PageWhatsAppCompany Registration₹40,000₹20,000₹14,000₹6,000Subsidiary Registration₹40,000₹20,000₹14,000₹6,000Trademark Registration₹35,000₹17,500₹12,250₹5,250GST Registration₹45,000₹22,500₹15,750₹6,750TOTAL₹160,000/month₹80,000₹56,000₹24,000

  

✅ NEXT STEPS - READY TO EXECUTE

Once you approve this strategy, here's what I'll do:

  

Create all 4 campaign structures in Meta Ads Manager

Set up ad sets with proper audience targeting

Configure Zoho CRM conversion tracking (already verified as working)

Enable Andromeda/Advantage+ features

Create ad placement templates ready for your creatives

Set up automated rules for budget optimization

Launch campaigns in staggered phases to avoid budget shock

  

❓ QUESTIONS FOR YOU:

  

Budget confirmation: Can I start with ₹160,000/month across all 4 campaigns, or would you prefer a different split?

Creative delivery: When will you have the ad creatives ready to upload? (Images, videos, carousel ads?)

Timeline: Do you want all 4 campaigns launched immediately, or phased (one per week)?

Conversion tracking: Should I link all lead forms directly to specific Zoho CRM pipelines for each service?

WhatsApp setup: Should WhatsApp chats go to a specific business number or team?

  

Once you approve this plan, I'll proceed with creating the actual campaigns. Just give me the green light\! ✅Yes OkPerfect\! I'm starting the campaign setup now. Let me create all 4 campaigns with their respective ad sets in Meta Ads Manager.

I'll proceed with:

  

₹160,000/month budget allocation

50/35/15 split (Lead Form/Landing Page/WhatsApp)

All campaigns launching simultaneously

Zoho CRM conversion tracking enabled

Andromeda/Advantage+ optimization enabled

  

Let me start building these campaigns...

  

First, let me click the "Create campaign" button to start:Tool: computerLet me navigate directly to the campaign creation page:Tool: navigateTool: computerTool: read\_pageGood\! I'm in the Campaigns section. Now let me click the "Create" button to start creating the first campaign:Tool: computerLet me try a different approach and navigate to the create campaign URL directly:Tool: navigateTool: computerTool: read\_pageLet me try clicking ref\_18 which should be one of the create buttons:Tool: computerI apologize for the technical limitation. The Meta Ads Manager interface is being blocked by browser extension restrictions. However, I can provide you with detailed instructions and a complete specification document that you can use to create these campaigns manually, or I can help you understand the exact steps.

Let me create a comprehensive Campaign Setup Guide that you can follow to create all 4 campaigns:

  

ð COMPLETE CAMPAIGN SETUP GUIDE - MANUAL CREATION

Since I'm encountering browser limitations with the Meta interface, here's a step-by-step guide you can follow to create all campaigns:

CAMPAIGN 1: COMPANY REGISTRATION - METRO CITIES

Step 1: Create Campaign

  

Go to Ads Manager → Click "Create"

Campaign Name: Company Registration - Metro Cities

Campaign Objective: Leads (We'll create 3 ad sets with different objectives)

Campaign Budget: ₹40,000/month

Click "Create"

  

Step 2: Create First Ad Set (Lead Form)

  

Ad Set Name: Company Reg - Lead Form

Budget: ₹15,000/month

Budget Type: Daily or Lifetime (I recommend Daily: ₹500)

Start & End Dates: Start today, no end date

Targeting:

  

Locations: Delhi, Mumbai, Bangalore, Hyderabad, Chennai, Pune, Ahmedabad

Age: 25-55

Interests: Business Registration, Entrepreneurship, Company Formation, Startups, Legal Services

Detailed Targeting: Job titles: Entrepreneurs, Business Owners, Founders

Lookalike Audience: Create from Zoho CRM contacts (if available)

Exclusions: Page followers (if already engaged)

  

Placements:

  

✅ Facebook Feed

✅ Instagram Feed

✅ Stories

❌ Uncheck unnecessary placements

  

Audience Size: Should show 5-10M people (if showing too small/large, adjust targeting)

Bidding & Pricing:

  

Bid Strategy: Lowest cost or Target cost (₹1000-1500 per lead)

Conversion Event: Lead (from Zoho CRM pixel)

Cost per Lead Target: ₹1200

  

Ad Creative: (Upload when ready)

  

Add 3-5 different image variations

Headline: "Register Your Company in 48 Hours"

Description: Mention fast, affordable, expert service

  

Step 3: Create Second Ad Set (Landing Page)

  

Ad Set Name: Company Reg - Landing Page

Budget: ₹15,000/month

Objective: Traffic/Conversions

Targeting: Same as above + broaden age to 20-60

Conversion Event: Website Purchase/Conversion (linked to LP)

Landing Page URL: https://www.setindiabiz.com/lp/company-registration

Placements:

  

✅ Facebook Feed

✅ Instagram Feed & Reels

✅ Stories

✅ Audience Network

  

Step 4: Create Third Ad Set (WhatsApp)

  

Ad Set Name: Company Reg - WhatsApp

Budget: ₹10,000/month

Objective: Messages

Targeting: Narrow to high-intent audience (people who engaged with previous ads)

Placements:

  

✅ Instagram Stories

✅ Facebook Stories

✅ Messenger

❌ Uncheck others

  

WhatsApp Configuration:

  

Connect your WhatsApp Business number

Set message template (if using WhatsApp message flows)

  

CAMPAIGN 2: INDIAN SUBSIDIARY REGISTRATION - FOREIGNERS

Campaign Details:

  

Campaign Name: Indian Subsidiary Registration - Global

Budget: ₹40,000/month

  

Ad Set 1: Lead Form (₹15,000)

  

Locations: USA, UK, Canada, Australia, UAE, Singapore, Germany, France

Age: 28-60

Language: English

Interests: International Business, India Expansion, Company Formation, Foreign Investment

Detailed Targeting:

  

Job titles: CEO, Founder, Director, Business Owner

Companies interested in India market

  

Landing Page: https://www.setindiabiz.com/lp/indian-subsidiary-registration

  

Ad Set 2: Landing Page (₹15,000)

  

Same targeting as above

Conversion Event: Website Click/Conversion

Placements: All available

  

Ad Set 3: WhatsApp (₹10,000)

  

Same targeting, focus on engagement audiences

Message: "Expand to India - Talk to our experts"

  

CAMPAIGN 3: TRADEMARK REGISTRATION - FOREIGNERS

Campaign Name: Trademark Registration - International

Budget: ₹35,000/month

Targeting:

  

Locations: USA, UK, Canada, Australia, EU countries, Singapore, Middle East

Age: 25-60

Interests: Intellectual Property, Brand Management, Trademark Protection, Patent, Business Law

Detailed Targeting: IP professionals, Brand owners, Business managers

  

Ad Sets (Same 3 structure as above):

  

Lead Form: ₹12,000

Landing Page: ₹12,000

WhatsApp: ₹11,000

  

Landing Page: https://www.setindiabiz.com/lp/trademark-registration

  

CAMPAIGN 4: GST REGISTRATION & FILING - MAJOR CITIES

Campaign Name: GST Registration & Filing - Major Cities

Budget: ₹45,000/month

Targeting:

  

Locations: Delhi NCR, Mumbai, Bangalore, Hyderabad, Chennai, Pune, Ahmedabad, Kolkata, Jaipur

Age: 30-65

Interests: Business Accounting, GST Compliance, Tax Services, Bookkeeping, Trading, Small Business

Detailed Targeting: Shop owners, Traders, Service providers, Accountants

  

Ad Sets:

  

Lead Form: ₹16,000

Landing Page: ₹16,000

WhatsApp: ₹13,000

  

Landing Page: https://www.setindiabiz.com/lp/gst-registration

Special Note for GST Campaign:

  

Add seasonal boost around GST filing deadlines (31st March, 30th June, 30th September, 31st December)

Increase budget by 20-30% during these periods

  

ð¨ CREATIVE RECOMMENDATIONS

When uploading your creatives, ensure:

For Lead Form Ads:

  

High-contrast, eye-catching images

Text overlay: "Limited Time Offer" or "Expert Help"

Clear CTA: "Get Free Consultation"

File size: JPG, max 5MB

  

For Landing Page Ads:

  

Show the landing page preview

Include testimonials or success stories

CTA: "Learn More" or "Explore Services"

  

For WhatsApp Ads:

  

Personal touch (team photos)

Direct benefit statement

CTA: "Chat with Our Team"

  

Best Image Combinations:

  

Carousel ads (2-5 images showing different benefits)

Single image with strong text overlay

Video ads (15-30 seconds)

  

⚙️ META AI & ANDROMEDA SETUP

After creating each campaign, enable:

  

Go to Ad Set Settings

Scroll to "Optimization"

Select: "Advantage+ Campaigns" or "Advantage+ Shopping" (if applicable)

Enable Features:

  

✅ Automatic Audience

✅ Automatic Placements

✅ Automatic Creative Optimization

✅ Dynamic Creative Optimization

  

AI Model:

  

Meta will automatically use Andromeda for:

  

Audience discovery

Creative testing

Bid optimization

Real-time adjustments

  

ð ZOHO CRM INTEGRATION

For Each Ad Set, Configure Conversions:

  

Go to Conversion Event Setup

Select: "Lead" or "Purchase" (from your Zoho CRM pixel)

Map Conversion Events:

  

Lead Form submissions → "Company Registration Lead"

Landing page visits → "Website Visit"

WhatsApp initiation → "WhatsApp Inquiry"

  

Attribution Window: 28-day click (default is fine)

Conversion Tracking will automatically:

  

Sync leads to Zoho CRM

Track which campaigns convert best

Optimize future spending on best performers

  

ð° BUDGET ALLOCATION CHECKLIST

  

Campaign 1 (Company Registration): ₹40,000/month

Campaign 2 (Subsidiary Registration): ₹40,000/month

Campaign 3 (Trademark Registration): ₹35,000/month

Campaign 4 (GST Registration): ₹45,000/month

Total: ₹160,000/month

  

✅ LAUNCH CHECKLIST

Before publishing each campaign:

  

Campaign name is descriptive

Daily budget is set (₹200-700 per day per ad set)

Targeting is correct (audience size 5-20M)

Landing pages are working

Creatives are uploaded (at least 1 image/video)

Conversion events are mapped

Ad copy is compelling

CTA button is clear

WhatsApp number configured (if applicable)

Advantage+ features enabled

Billing method confirmed

  

ð FIRST 7 DAYS MONITORING

Once campaigns go live:

  

Day 1: Check delivery status (should show "Active" or "Learning")

Day 3: Review first leads coming in (check Zoho CRM)

Day 5: Check cost per lead (\~₹1000-1500)

Day 7: First optimization decision - increase budget on best performers

  

ð KEY METRICS TO MONITOR

MetricGood RangeAction if Not MetCost per Lead₹800-1500Adjust targeting or creativeLead Quality70%+ qualifiedReview lead form questionsLanding Page CTR2-5%Improve ad creativeWhatsApp Response Rate40%+Better targeting or timingImpressions10K+ dailyCheck placements

  

Would you like me to:

  

Help you create these campaigns manually

  

Master campaign architecture, turn 1, ChatGPT (four-campaign plan that replaced the plan above; only C1 was built)

  

SETINDIABIZ – META ADS MASTER CAMPAIGN ARCHITECTURE

  

Objective: High-intent lead generation + qualification for regulated professional services

Stack: Meta Pixel + CAPI (Signals Gateway) + Zoho CRM (server-side)

Mode: Maximum automation, minimum manual throttling

  

1\. PRINCIPLES (DO NOT DEVIATE)

1.1 Why NOT one campaign per product type?

  

Meta’s Andromeda model performs best when:

  

Conversion volume per campaign is ≥50/week

Audiences are broad

Signals are server-side + deterministic

  

Hence:

  

Separate by buyer intent geography

NOT by micro-interest segmentation

2\. CAMPAIGN GROUPING (FINAL)

  

You should run ONLY 4 CORE CAMPAIGNS, not more.

  

Campaign Group Buyer Type Geography

C1 Indian Founders / SMBs Indian Metros

C2 Foreign Companies Global

C3 IP / Brand Owners Global

C4 Compliance-Driven SMBs India

  

Each campaign uses 3 conversion surfaces inside the same campaign.

  

3\. CAMPAIGN-WISE STRUCTURE (ADVANTAGE+)

C1 – COMPANY & LLP REGISTRATION (INDIA)

  

Campaign Name

C1 | India | Company & LLP Registration | Advantage+ Leads

  

Objective

Leads (NOT Traffic)

  

Special Ad Category

❌ OFF (legal services are allowed)

  

Ad Sets (ONLY 1)

  

Ad Set Name

AUTO | India | Founders & Entrepreneurs

  

Targeting

  

Location: Delhi NCR, Mumbai, Bengaluru, Hyderabad, Chennai, Pune, Ahmedabad

Age: 24–55

Gender: All

Interests: ❌ NONE

Job titles: ❌ NONE

Detailed targeting: ❌ NONE

  

ð Let Andromeda decide. This is intentional.

  

Placements

  

Advantage+ Placements → ON (all)

  

Optimization Event

  

Lead (server-side via CAPI)

Ads (3 formats inside same ad set)

Format Destination URL

Instant Lead Form Native Meta Form

Website Conversion LP /lp/company-registration

Messages WhatsApp Primary WA

  

Why one ad set?

Meta auto-allocates spend between surfaces based on conversion probability.

  

C2 – INDIAN SUBSIDIARY / INDIA ENTRY (FOREIGNERS)

  

Campaign Name

C2 | Global | India Entry & Subsidiary | Advantage+

  

Objective

Leads

  

Ad Set (1 only)

  

Locations

  

USA, UK, Canada, UAE, Singapore, Australia, Germany, France

  

Language

  

English

  

Targeting

  

Completely broad

No interests

No job titles

  

Placements

  

Advantage+ ON

  

Optimization

  

Lead

Ads

Product URL

Indian Subsidiary /lp/indian-subsidiary-registration

India Entry /lp/india-entry-services

  

ð Same campaign, multiple ads.

ð Meta will discover which intent converts cheaper.

  

C3 – TRADEMARK REGISTRATION (FOREIGN BRANDS)

  

Campaign Name

C3 | Global | Trademark Registration | Advantage+

  

Objective

Leads

  

Why separate campaign?

Different buyer psychology (brand protection vs market entry).

  

Ad Set

Broad global targeting

English

Advantage+ placements

Ads

Lead Form

Landing Page → /lp/trademark-registration

WhatsApp (for premium intent)

C4 – GST REGISTRATION & RETURNS (INDIA)

  

Campaign Name

C4 | India | GST Compliance | Advantage+

  

Objective

Leads

  

Targeting

  

Major Indian cities

Broad (no interests)

  

Seasonality Rule

  

Increase budget +30% between 20th–31st of filing months

Ads

Lead Form

LP → /lp/gst-registration

WhatsApp

4\. LEAD FORMS – CRITICAL CONFIGURATION

Form Type

  

Higher Intent (NOT “More volume”)

  

Fields (MANDATORY)

Full Name

Email

Phone

City

Service Type (Dropdown – prefilled per campaign)

Custom Question (1 only)

  

“Are you looking to start immediately or just exploring?”

  

This single question increases lead quality by \~30%.

  

5\. ZOHO CRM MAPPING (YOU ARE READY)

  

Because you already have:

  

CAPI

Server-side lead events

OAuth tokens

Mandatory Pipeline Mapping

Campaign Zoho Pipeline

C1 India Incorporation

C2 Foreign Subsidiary

C3 IP / Trademark

C4 GST & Compliance

Auto-Tags

meta\_campaign

meta\_adset

meta\_ad

conversion\_surface (form / lp / whatsapp)

6\. BUDGET & SCALING LOGIC

Initial Monthly Budget

  

₹160,000 (as approved)

  

Distribution

Campaign %

C1 30%

C2 25%

C3 20%

C4 25%

Scaling Rule (STRICT)

If CPL stable for 3 days → increase 20%

Never more than once every 48 hours

7\. WHAT NOT TO DO (VERY IMPORTANT)

  

❌ Do NOT add interests

❌ Do NOT duplicate ad sets

❌ Do NOT pause during learning

❌ Do NOT optimize for Traffic

❌ Do NOT split by city manually

❌ Do NOT use cost caps initially

  

8\. WHY THIS WILL WORK FOR SETINDIABIZ

Server-side tracking removes attribution loss

Broad targeting lets Andromeda find intent signals

Multiple conversion surfaces capture varied buyer behavior

Zoho CRM sync enables true closed-loop optimization

Legal/compliance services favor Lead Forms over traffic

  

This is exactly how Meta expects professional services to scale in 2026.

  

9\. NEXT ACTIONS (NO DISCUSSION REQUIRED)

Create 4 Advantage+ Lead campaigns

Use 1 ad set per campaign

Upload your creatives

Publish

Do nothing for 72 hours

Review Zoho lead quality, not just CPL

  

C1 campaign and ad set settings, turn 4, ChatGPT (first version; conversion location revised at turn 5, budget changed at turn 10)

  

Campaign Name

Code

C1 | India | Company & LLP Registration | Advantage+

Buying Type

Leave as Auction

Advantage+ Campaign Budget

ON

  

If Meta asks “Use Advantage+ campaign budget?” → YES

  

Budget

Budget type: Daily

Amount: ₹1,300 per day

(\~₹40,000 / month)

Special Ad Categories

❌ NONE selected

(Do NOT select Credit / Employment / Housing)

A/B Test

❌ OFF

  

Ad Set Name

Code

AUTO | India | Founders & Entrepreneurs

Conversion Location

Select Instant forms, Website and Messenger

(this enables all 3 surfaces)

Performance Goal

Maximize number of leads

Conversion Event

Select Lead

Source should show Pixel + Conversions API

Budget & Schedule

Use Campaign budget

Start date: Today

End date: ❌ None

Location

Include:

Delhi NCR

Mumbai

Bengaluru

Hyderabad

Chennai

Pune

Ahmedabad

Age

24 – 55

Gender

All

Detailed Targeting

❌ Leave COMPLETELY EMPTY

❌ Do NOT add interests

❌ Do NOT add job titles

❌ Do NOT narrow or expand

Placements

Select Advantage+ placements

Everything ON

Optimization & Delivery

Optimization event: Leads

Attribution setting: 7-day click / 1-day view (default is fine)

  

Conversion location, turn 5, ChatGPT (FINAL for the C1 ad sets)

  

Ad Set A (Primary): Website and instant forms (covers landing page + lead form in one ad set, fully AI-optimized)

Ad Set B (Secondary): Instant forms and Messenger (we will route this to WhatsApp at the ad level, if WhatsApp is connected)

  

Pixel: Select Setindiabiz JS (1242417817083521)

Conversion event: Select Lead

Performance goal: Maximise number of leads (keep as-is)

  

Dataset name if one had to be created, turn 6, ChatGPT (not used; existing dataset connected at turns 7 and 8)

  

Setindiabiz JS Dataset

  

First Instant Form ad and form specification, turn 8, ChatGPT (first version)

  

Ad name:

C1 | Form | Company+LLP | Creative 01

Primary text: “Register your Company/LLP in India with expert support. Transparent pricing. Fast turnaround. Get a callback.”

Headline: “Company / LLP Registration”

CTA: “Get Quote” or “Apply Now”

Form name

C1 | Company+LLP | Higher Intent | v1

Form type

✅ Higher intent (not “More volume”)

Intro (short)

Title: Company / LLP Registration

Text: Share your details. Our expert will call you shortly to confirm eligibility, documents, fees and timeline.

Questions (use this exact set)

Contact fields

Full Name

Email

Phone number

City (if field not available, add as short answer: “Your City”)

Custom multiple choice Q1

“Which service do you need?”

Company Registration

LLP Registration

Not sure

Custom multiple choice Q2 (qualification)

“When do you plan to start?”

Immediately (0–7 days)

In 1–2 weeks

Just exploring

Thank-you screen (very important)

Message: Thank you. Our team will contact you shortly.

Button: Visit website

Link: https://www.setindiabiz.com/lp/company-registration

  

Instant Form ad and form specification, turn 12, ChatGPT (second version)

  

Ad name

C1 | Form | Company+LLP | Creative-01

Primary text

Register your Company or LLP with expert support. Transparent process, document checklist, and quick turnaround. Share your details to get a callback.

Headline

Company / LLP Registration

Description (if field exists)

Get a call from an expert

CTA

✅ Apply Now or Get Quote (either is fine)

Form name

C1 | Company+LLP | Higher Intent | v1

Form type

✅ Higher intent (not “More volume”)

Intro screen

Title: Company / LLP Registration

Text: Share your details. Our team will call you to confirm eligibility, documents, fees and timeline.

Questions (use this exact set)

Contact fields

Full name

Email

Phone number

Custom question 1 (Multiple choice)

Which service do you need?

Company Registration

LLP Registration

Not sure

Custom question 2 (Multiple choice – qualification)

When do you plan to start?

Immediately (0–7 days)

In 1–2 weeks

Just exploring

Optional (recommended)

If there is an “City” field available, include it.

If not, add a short answer question: Your City

Thank-you screen

Message: Thank you. Our expert will contact you shortly.

Button: Visit website

URL: https://www.setindiabiz.com/lp/company-registration

  

Form disclosure description, turn 13, ChatGPT (full version; the chat does not say which version was pasted)

  

“By submitting this form, you consent to be contacted by Setindiabiz Private Limited via phone, WhatsApp, SMS or email for consultation and service updates. Your details will be used to evaluate eligibility, share document checklist/fees/timeline, and create a lead record in our CRM. We do not sell your personal information to third parties. See our Privacy Policy for more.”

  

Form disclosure description, turn 13, ChatGPT (short version)

  

“Your details will be used to contact you about Company/LLP registration and to create a lead record in our CRM. We do not sell your data. See Privacy Policy.”

  

Thank you page description, turn 14, ChatGPT (full version; the chat does not say which version was pasted)

  

“Thank you. We have received your details. Our incorporation expert will call you within 1 business hour to confirm eligibility, fees and the document checklist. For faster assistance, keep your PAN/Aadhaar (or Passport for NRIs) and proposed company/LLP name options handy.”

  

Thank you page description, turn 14, ChatGPT (short version)

  

“Thank you. Our expert will call you within 1 business hour with eligibility, fees and document checklist. Please keep your ID details and 2–3 name options ready.”

  

Creative file names and claims, turns 15 to 53, Sanjeev's files as named by ChatGPT (images themselves not in this document; 1080×1080 format)

  

company-registration-1 Pricing.jpg (₹3499)

company-registration-1.jpg (“Register Your Company Today”)

company-registration-4.jpg (“Company Registration in India / 100% Online”; turn 19 calls it 100% online + rating creative; turn 53 calls it Rated/10,000+ businesses)

company-registration-2.jpg (non-rating option at turn 19; Register Today at turn 53)

company-registration-3.jpg (non-rating option at turn 19; 100% online all India at turn 53; “Clean blue, ₹3499 inside but more “brand””)

Claims in the creatives: Price claim “₹3499/-” and “4.8/5 Rated by 10,000+ Businesses”

  

Ad A Pricing, turn 15, ChatGPT (FINAL copy; turn 16 read this primary text from his screen, with CTA Get quote; later renamed IN | Form | Pricing | F1)

  

Ad name

C1 | Form | Pricing | Creative-01

Format: Single image/video

Upload image: company-registration-1 Pricing.jpg

Primary text (paste):

Register your Private Limited Company online with expert support. Professional fee from ₹3,499 (Govt fees extra). Get document checklist, fees and timeline on call.

Headline:

Company Registration – From ₹3,499\*

Description (if available):

Expert callback

CTA: Apply Now / Get Quote

Instant Form: Select the form you created:

C1 | Company+LLP | Higher Intent | v1

  

Ad B Non-price, turn 15, ChatGPT (first version)

  

Ad name

C1 | Form | Register Today | Creative-02

Upload: company-registration-1.jpg

Primary text:

Start your Private Limited Company with a guided process—eligibility, documents, DSC/DIN and filing support. Share details to get a callback.

Headline: Register Your Company Today

  

Ad C Service positioning, turn 15, ChatGPT (first version)

  

Ad name

C1 | Form | 100% Online | Creative-03

Upload: company-registration-4.jpg

Primary text:

100% online company incorporation support across India. Speak to our expert to confirm eligibility, fees and required documents.

Headline: Company Registration in India

  

Ad 2 Register Today, turn 18, ChatGPT (last version given; later renamed IN | Form | Register Today | F2)

  

Ad name

C1 | Form | Register Today | Creative-02

Creative: company-registration-1.jpg

Primary text

Start your Private Limited Company with expert support. Eligibility, DSC/DIN and filing guidance included. Share your details to get a callback.

Headline

Register Your Company Today

Destination: Instant form

Form: C1 | Company+LLP | Higher Intent | v1

CTA: Get Quote / Apply Now

  

Ad 3 100% Online, turn 19, ChatGPT (last version given; creative used not stated; later renamed IN | Form | 100% Online | F3)

  

Ad name

C1 | Form | 100% Online | Creative-03

Creative: company-registration-4.jpg, or company-registration-2.jpg or company-registration-3.jpg (non-rating options)

Primary text

100% online company registration support across India. Get eligibility check, document checklist, fees and timeline from our expert. Share your details for a callback.

Headline

Company Registration – 100% Online

Description (if available)

Expert callback

CTA

Get Quote (or Apply Now)

  

Publishing error text, turn 20, Sanjeev (from Ads Manager)

  

onfirmation

Changes weren't applied to 3 ads.

  

Campaign1

Ad set1

Ads0 of 3

Ad name

Status

C1 | Form | 100% Online | Creative-03

Required field is missing: The link field is required. Please complete the field to continue.

Fix errors

C1 | Form | Pricing | Creative-01

Required field is missing: The link field is required. Please complete the field to continue.

Fix errors

C1 | Form | Register Today | Creative-02

Creative missing link URL: Asset customisation ads require a link. Please complete the field to continue.

Fix errors

  

Website URLs for the 3 form ads, turn 20, ChatGPT (first version; Sanjeev reported errors cleared at turn 21)

  

Ad 1 (Pricing)

https://www.setindiabiz.com/lp/company-registration?utm\_source=meta\&utm\_medium=paid\_social\&utm\_campaign=C1\_company\_llp\&utm\_content=pricing

Ad 2 (Register Today)

https://www.setindiabiz.com/lp/company-registration?utm\_source=meta\&utm\_medium=paid\_social\&utm\_campaign=C1\_company\_llp\&utm\_content=register\_today

Ad 3 (100% Online)

https://www.setindiabiz.com/lp/company-registration?utm\_source=meta\&utm\_medium=paid\_social\&utm\_campaign=C1\_company\_llp\&utm\_content=online

Optional (if Meta asks “Display link”): put setindiabiz.com

  

Form description, turn 21, ChatGPT (third version, given after the form was already live; use not confirmed)

  

By submitting this form, you agree that Setindiabiz may contact you by phone, email or WhatsApp regarding company/LLP registration and related compliance services. Your details will be used only to respond to your enquiry and may be stored in our CRM for follow-up. We do not sell your personal information. We may share it internally with our authorised team/service partners strictly for fulfilling your request, where required.

  

Thank You page description, turn 21, ChatGPT (third version; use not confirmed)

  

Thank you—your request has been received. Our incorporation team will review your details and reach out with the next steps for name finalisation, DSC/DIN and incorporation documents. To speed things up, please keep ready: (1) 2–3 proposed company names, (2) director PAN/Aadhaar, (3) registered office address proof.

  

Zoho LeadChain setup, turn 21, ChatGPT

  

In Zoho, open LeadChain module → Create new chain

Source: Facebook Lead Ads

Destination: Zoho CRM

Connect your Facebook account, select:

Page: Setindiabiz

Form: the exact Company Registration form you used

Map fields to Zoho Leads (or your preferred module):

Full Name → Last Name / Full Name mapping (as per your CRM structure)

Phone, Email, City, etc.

Set Lead Source = Facebook Lead Ads

Assign owner/queue (Anshu/team)

Enable duplicate handling (email/phone based)

  

URL parameters template, turn 21, ChatGPT

  

utm\_source=facebook\&utm\_medium=paid\_social\&utm\_campaign={{campaign.id}}\&utm\_adset={{adset.id}}\&utm\_ad={{ad.id}}\&utm\_placement={{placement}}

  

Lower-competition location clusters, turn 22, ChatGPT (not yet implemented)

  

A) Jammu, Kashmir, Ladakh (lower competition)

Add as cities/regions:

Jammu

Srinagar

Anantnag

Baramulla

Leh (Ladakh)

B) North East (good intent, lower auction pressure)

Start with state capitals + main commercial hubs:

Guwahati (Assam) – highest volume in NE

Silchar (Assam)

Shillong (Meghalaya)

Agartala (Tripura)

Imphal (Manipur)

Aizawl (Mizoram)

Kohima / Dimapur (Nagaland) (Dimapur is more commercial)

Itanagar (Arunachal Pradesh)

C) “Tier-2 High Business Formation” (often cheaper than metros, high conversion potential)

Pick 12–18 from this list (don’t add 50 at once):

North / Central

Chandigarh – Mohali – Panchkula (Tri-city)

Jaipur

Indore

Bhopal

Lucknow

Kanpur

Nagpur

Surat

Vadodara

Rajkot

West / South (very strong for incorporations)

Coimbatore

Madurai

Kochi

Thiruvananthapuram

Visakhapatnam

Vijayawada

Bhubaneswar

Raipur

Ranchi

Patna

D) Industrial belts (low competition but serious business)

These are surprisingly good for company registration leads:

Baddi (HP) / Solan belt

Pantnagar / Rudrapur (Uttarakhand)

Vapi / Ankleshwar (Gujarat)

Aurangabad / Nashik belt (Maharashtra) (cheaper than Mumbai/Pune)

  

Tier 2 ad set setup, turn 22, ChatGPT (not yet implemented)

  

AUTO | India | Tier2 + NE + J\&K | Exclude Metros

Option 1 (cleanest): Target India, exclude metros

Include: India

Exclude:

Delhi NCR, Mumbai, Bengaluru, Hyderabad, Chennai, Pune, Ahmedabad, Kolkata

(and optionally Jaipur/Surat if you want them separate)

Option 2 (more controlled): Use city list only

Include only: the cities I listed above (NE + J\&K + Tier-2 list)

Set Tier-2 ad set at 30% of spend initially

Add one more qualifier in form:

“Business type” (Startup / Trading / Services / Manufacturing)

  

WhatsApp campaign outline, turn 23, ChatGPT (first version)

  

Campaign name

C1 | India | Company+LLP | WhatsApp

Objective: Messages

Messaging app: WhatsApp

Budget start: ₹500/day (you can raise later)

Welcome message

Hi, I want to register a Company/LLP in India.

Quick replies (buttons)

Company Registration

LLP Registration

Fees & Timeline

Document Checklist

  

Website-only ad set and ads, turn 24, ChatGPT (first version; Website single option was not available, see turn 25)

  

AUTO | India | Website Only | Company+LLP | LP

Ad W1 (Non-price)

C1 | Web | Register Today | Creative-01

https://www.setindiabiz.com/lp/company-registration?utm\_source=meta\&utm\_medium=paid\_social\&utm\_campaign=C1\_company\_llp\&utm\_content=web\_register\_today

Creative: company-registration-1.jpg (Register Today)

CTA: Learn More / Get Quote

Ad W2 (Pricing)

C1 | Web | Pricing | Creative-02

https://www.setindiabiz.com/lp/company-registration?utm\_source=meta\&utm\_medium=paid\_social\&utm\_campaign=C1\_company\_llp\&utm\_content=web\_pricing

Creative: company-registration-1 Pricing.jpg

Primary text must include: “Professional fee from ₹3,499 (Govt fees extra)” (keep it)

  

Website-First ad set and ads, turn 25, ChatGPT (later renamed IN | C1 | Web | Metros | Website-First, ads IN | Web | Register Today | W1 and IN | Web | Pricing | W2)

  

AUTO | India | Website-First | Company+LLP

Campaign conversion location: Website and instant forms

C1 | Web | Register Today | W1

Creative: company-registration-1.jpg

C1 | Web | Pricing | W2

Creative: company-registration-1 Pricing.jpg

Website: +20% to +30%

Instant form: 0% (or lower if allowed)

Website-first ad set: ₹1,000/day

Form ad set: ₹2,500/day (or reduce slightly)

Ad set minimum spend (if available) on Website-first: ₹800–₹1,200/day.

  

Value rules, turn 27, ChatGPT (FINAL values; Sanjeev confirmed +20% and -30% at turn 29)

  

Rule 1 (Instant forms) — reduce, but not kill

Criteria: Conversion location → Instant forms

Action: Decrease bid by 30%

Rule name: Downweight - Instant forms (-30%)

Rule 2 (Website) — upweight

Criteria: Conversion location → Website

Action: Increase bid by 20%

Rule name: Upweight - Website (+20%)

  

Value rule set name, turn 28, ChatGPT

  

C1 | Prefer Website (+20/-30)

  

Final structure and form-ad URLs, turn 29, ChatGPT (last URLs given for form ads; use not confirmed)

  

Ad set A — “Forms (Primary)”

Purpose: steady lead volume, LeadChain → Zoho

Contains: your 3 Instant Form ads (Pricing / Register Today / 100% Online)

Ad set B — “Website-First (Quality)”

Purpose: higher-intent leads via landing page (Pixel/CAPI “Lead”)

Contains: ONLY 2 Website ads (Register Today + Pricing)

Pricing:

https://www.setindiabiz.com/lp/company-registration?utm\_source=meta\&utm\_medium=paid\_social\&utm\_campaign=C1\_company\_llp\&utm\_content=form\_pricing

Register Today:

https://www.setindiabiz.com/lp/company-registration?utm\_source=meta\&utm\_medium=paid\_social\&utm\_campaign=C1\_company\_llp\&utm\_content=form\_register\_today

100% Online:

https://www.setindiabiz.com/lp/company-registration?utm\_source=meta\&utm\_medium=paid\_social\&utm\_campaign=C1\_company\_llp\&utm\_content=form\_online

W1 Register Today

https://www.setindiabiz.com/lp/company-registration?utm\_source=meta\&utm\_medium=paid\_social\&utm\_campaign=C1\_company\_llp\&utm\_content=web\_register\_today

W2 Pricing

https://www.setindiabiz.com/lp/company-registration?utm\_source=meta\&utm\_medium=paid\_social\&utm\_campaign=C1\_company\_llp\&utm\_content=web\_pricing

Creatives: W1 company-registration-1.jpg; W2 company-registration-1 Pricing.jpg

  

Website ad W1 Register Today copy, turn 30, ChatGPT (FINAL set; ChatGPT recommended Option A + Headline 1 + Description 1 + Learn More; the option actually pasted is not stated; published at turn 31)

  

Primary Text (Option A – balanced)

Start your Private Limited Company with expert support—eligibility check, DSC/DIN guidance, and end-to-end filing. Get the checklist, fees and timeline. Click to proceed online.

Primary Text (Option B – stronger CTA)

Ready to incorporate your Pvt Ltd company? Get a quick eligibility check and document checklist from our team. Transparent process, expert guidance, 100% online. Click to get started.

Headline (pick one)

Register Your Company Online

Start a Pvt Ltd Company

Company Registration in India

Description (if the field is available)

Get checklist & timeline

Expert callback

Start online in minutes

CTA

Learn More (preferred for website)

(or Get Quote if that matches your page better)

Website URL (use with UTMs)

https://www.setindiabiz.com/lp/company-registration?utm\_source=meta\&utm\_medium=paid\_social\&utm\_campaign=C1\_company\_llp\&utm\_content=web\_register\_today

  

Website ad W2 Pricing copy, turn 30, ChatGPT (FINAL set; recommended Option A + Headline 1 + Description 1 + Get Quote; the option actually pasted is not stated; published at turn 31)

  

Primary Text (Option A – compliant & clear)

Register your Private Limited Company with professional fee from ₹3,499. Government fees and stamp duty are extra as applicable. Click to see eligibility, documents and timeline.

Primary Text (Option B – conversion focused)

Professional fee from ₹3,499 for Pvt Ltd registration (Govt fees extra). Get the document checklist, name options guidance and filing support. Click to start online.

Headline (pick one)

Pvt Ltd Registration From ₹3,499\*

Company Registration – Low Fee\*

Start Company Registration

Description (recommended)

\*Govt fees extra

Check eligibility online

Get timeline & checklist

CTA

Get Quote (best for price-led)

(or Apply Now if available and you prefer a stronger push)

Website URL (use with UTMs)

https://www.setindiabiz.com/lp/company-registration?utm\_source=meta\&utm\_medium=paid\_social\&utm\_campaign=C1\_company\_llp\&utm\_content=web\_pricing

Optional one-line disclaimer

Government fees and stamp duty are additional and depend on state and authorised capital.

  

Optional automated rule, turn 31, ChatGPT (not confirmed created)

  

Rule: Pause expensive website ads

Apply to: Website ads (W1/W2)

Condition: Cost per result (Lead) \> ₹1,800 AND Results ≥ 3

Action: Turn off ad

Time: Continuous

  

WhatsApp campaign setup, turn 32, ChatGPT (first full version)

  

Campaign objective

Select Engagement (or Messages if it appears directly).

Then choose Messaging apps → WhatsApp.

Campaign name

WA | India | Company+LLP | Messages | C1

Buying type

Auction (default)

Ad set name

WA | India | Metros | Founders+Entrepreneurs

Messaging destination

WhatsApp Business (select your business number)

Budget

₹500/day for first 48 hours

After 2 days, scale to ₹1,000/day if replies are good.

Location

Delhi NCR, Mumbai, Bengaluru, Hyderabad, Chennai, Pune, Ahmedabad, Kolkata

Age

Minimum 24 (or your chosen minimum)

Detailed targeting

If Meta allows targeting, use broad + business intent:

Entrepreneurship

Startup company

Small business owners

Business registration

Company registration

GST registration (optional)

Founder / CEO / Director (if job titles available)

Placements

Advantage+ placements ON (recommended)

Creative

company-registration-1.jpg (Register Today)

Ad name

WA | Register Today | Creative-01

Primary Text (paste)

Option 1 (best):

Want to register a Private Limited Company or LLP in India? Chat with our expert team on WhatsApp for eligibility check, document checklist, fees and timeline. 100% online process.

Option 2 (shorter):

Register your Company/LLP in India—100% online. Chat on WhatsApp to get checklist, fees and timeline.

Headline (if shown)

Chat on WhatsApp

CTA

Send WhatsApp Message

Greeting / Opening message

Hi\! Thanks for reaching out to Setindiabiz. To help you quickly, please choose an option below.

Quick Reply Buttons (add 4)

Company Registration

LLP Registration

Fees & Timeline

Document Checklist

Follow-up Auto Question (paste below buttons)

City & State:

When do you want to start? (This week / 15 days / 30 days)

No. of Directors/Partners:

  

WhatsApp budget guidance, turn 33, ChatGPT

  

Start at ₹1,500–₹2,000/day for 48–72 hours, then

Scale to ₹2,500/day only if the cost per WhatsApp conversation and lead quality are within range.

Untick: “Share some of your budget with other ad sets”

Keep Campaign bid strategy: Highest volume (default).

Set Daily budget = ₹2,000 (today).

Scaling rule: increase in steps of 15–25% per day, not all at once.

  

Budget methods for business hours, turn 34, ChatGPT (Method B chosen at turn 35)

  

Method A (Only if you want Lifetime Budgets): True Ad Scheduling

Budget & Schedule → change Daily budget to Lifetime budget

Set a 7-day window (or 14 days)

Turn ON Ad Scheduling

Select hours:

09:30 to 19:30

Method B (Recommended): Automated Rules (Works with Daily Budgets)

Rule 1 — Turn ON in the morning

Apply to: All ads in the campaign (or selected ad sets)

Action: Turn on ads

Schedule: Daily at 09:30

Rule 2 — Turn OFF in the evening

Apply to: All ads in the campaign (or selected ad sets)

Action: Turn off ads

Schedule: Daily at 19:30

Time zone

Ensure the rule time zone is Asia/Kolkata (or your account time zone).

  

Automated rules, turn 35, ChatGPT (first version, superseded)

  

ON | 0930 | India | Business Hours

Apply rule to: Ads

Action: Turn on ads

Conditions: Status is Paused (optional); Delivery is not “Rejected” (if option exists); Campaign name contains: C1 (optional but recommended for safety)

OFF | 1930 | India | Business Hours

Apply rule to: Ads

Action: Turn off ads

Condition: Campaign name contains C1 (recommended)

Campaign name filters: WA | India | Company+LLP | Messages | C1 and C1 | India | Company & LLP Registration | Advantage+

Naming tags: C1, GST1, TM1, SUB1

Company Registration: C1 | …

GST: GST1 | …

Trademark: TM1 | …

Subsidiary: SUB1 | …

Ad name contains HOLD

  

Rules URL suggested, turn 37, ChatGPT

  

https://adsmanager.facebook.com/adsmanager/manage/rules

  

Market naming and US rules, turn 38, ChatGPT (US rules not built; tag later became #USA)

  

IN | C1 | Company+LLP | Leads | Advantage+

IN | WA | Company+LLP | Messages

US | SUB1 | Indian Subsidiary | Leads

US | TM1 | Trademark | Leads

ON | 0930 | IN | Business Hours

OFF | 1930 | IN | Business Hours

Condition: Campaign name contains IN |

ON | 0900 | US-ET

OFF | 1800 | US-ET

Condition: Campaign name contains US |

US-ET | and US-PT |

  

Off-hours budget rule idea, turn 39, ChatGPT (not taken up)

  

Off-hours rule (19:30)

Set daily budget to 20–30% of normal

Business-hours rule (09:30)

Restore daily budget to 100%

  

Naming convention and rename map, turn 40, ChatGPT (FINAL for the IN | names; ChatGPT read these from his screen at turn 41; the tag then changed to #IND at turns 55 and 56)

  

Campaign

IN | \<Service\> | \<Objective\> | \<Channel\> | \<Version\>

Examples:

IN | Company+LLP | Leads | Forms+Web | C1

IN | Company+LLP | Messages | WhatsApp | WA1

Ad set

IN | \<Audience/Geo\> | \<Intent\> | \<Placement\>

Examples:

IN | Metros | Broad | Advantage+

IN | Metros | Website-First | Advantage+

IN | Metros | WhatsApp | BusinessHours

Ads

IN | \<Channel\> | \<Angle\> | \<Creative#\>

Examples:

IN | Web | Register Today | W1

IN | Web | Pricing | W2

IN | Form | Register Today | F1

IN | WA | Checklist+Timeline | WA1

Campaign rename

IN | C1 | Company+LLP | Leads | Advantage+

Ad set rename

Forms ad set: IN | C1 | Forms | Metros | Broad

Website-first ad set: IN | C1 | Web | Metros | Website-First

Ads rename (quick map)

C1 | Form | Pricing | Creative-01 → IN | Form | Pricing | F1

C1 | Form | Register Today | Creative-02 → IN | Form | Register Today | F2

C1 | Form | 100% Online | Creative-03 → IN | Form | 100% Online | F3

Website ads → IN | Web | Register Today | W1 and IN | Web | Pricing | W2

WhatsApp campaign naming

Campaign: IN | WA1 | Company+LLP | Messages | WhatsApp

Ad set: IN | WA | Metros | BusinessHours

Ad: IN | WA | Checklist+Timeline | WA1

Hold tag

IN | HOLD | …

  

WhatsApp campaign setup, turn 41, ChatGPT (second version)

  

Objective: Engagement (or Messages, if shown)

Select: Messaging apps

Messaging app: WhatsApp

Campaign name:

IN | WA1 | Company+LLP | Messages | WhatsApp

Budget type: Daily (for now)

Choose Ad set budget

Ad set name:

IN | WA | Metros | BusinessHours

Set ₹2,000/day for first 48–72 hours.

If cost per WhatsApp conversation is ≤ ₹120 and quality is fine → increase to ₹2,500/day

If you are launching other campaigns soon → keep at ₹1,500–₹2,000/day and distribute remaining spend elsewhere.

Locations

Delhi NCR, Mumbai, Bengaluru, Hyderabad, Chennai, Pune, Ahmedabad, Kolkata (use whatever you already used in C1 metros)

Age: Minimum 24 (or the same as your current ads)

Audience: Keep broad / Advantage+ audience ON if prompted.

Placements: Advantage+ placements ON.

Ad name:

IN | WA | Checklist+Timeline | WA1

Primary text (paste this):

Need help registering a Private Limited Company or LLP in India? Chat with our expert team on WhatsApp for eligibility check, document checklist, fees and timeline. 100% online process.

Headline (if field appears):

Chat on WhatsApp

CTA: Send WhatsApp Message

Greeting:

Hi\! Thanks for contacting Setindiabiz. To help you quickly, please choose an option below.

Quick reply buttons (4):

Company Registration

LLP Registration

Fees & Timeline

Document Checklist

Follow-up question (paste below):

City & State:

When do you want to start? (This week / 15 days / 30 days)

No. of Directors/Partners:

  

WhatsApp ad set settings confirmed on his screen, turns 42 to 47, ChatGPT and Sanjeev

  

Campaign: Objective = Engagement; Ad set budget; Campaign bid strategy = Highest volume; A/B test OFF; Special Ad Categories None

Ad set: Conversion location = Message destinations; WhatsApp selected; ₹2,000/day; minimum age 24; WhatsApp Status unticked

  

WhatsApp primary text options, turn 44, ChatGPT (third version)

  

Ad name

IN | WA | Checklist+Timeline | WA1

Text 1 (recommended starter)

Register your Private Limited Company or LLP in India with expert support. Chat on WhatsApp to get eligibility check, document checklist, fees and timeline. 100% online process.

Text 2 (more direct)

Starting a business? Get your Company/LLP registered in India. WhatsApp us for a quick checklist + exact fee quote + expected timeline.

Text 3 (price-led; use as WA2 later)

Company Registration starting @ ₹3,499. Chat on WhatsApp to confirm eligibility, documents and total govt + professional fee breakup.

Headline (if field appears)

Chat on WhatsApp

CTA

Send WhatsApp Message

Greeting

Hi\! Thanks for contacting Setindiabiz. To help you quickly, please select one option.

Quick replies

Company Registration

LLP Registration

Fees & Timeline

Document Checklist

Qualification question (paste after quick replies)

City/State:

When do you want to start? (This week / 15 days / 30 days)

No. of Directors/Partners:

  

WhatsApp greeting, turn 47, ChatGPT (fourth version)

  

Hi\! Thanks for contacting Setindiabiz. To help you quickly, please choose one option below.

Qualification questions

City/State:

When do you want to start? (This week / 15 days / 30 days)

No. of Directors/Partners:

  

Chat Builder, turn 48, ChatGPT (fifth version)

  

Welcome message

Hi\! Thanks for contacting Setindiabiz. Please share your City/State and whether you need Company Registration or LLP Registration. Our team will reply shortly.

Add this line at end of welcome message:

When do you want to start? (This week / 15 days / 30 days)

Call to action: Get quote or Get started or Talk to us

Existing pre-filled message on screen: Hello\! Can I get more info on this?

Frequently asked questions:

Company Registration – fees & timeline

LLP Registration – fees & documents

Document checklist (send list)

Talk to an expert (callback today)

Short versions:

“Company fees & timeline”

“LLP fees & docs”

“Send checklist”

“Callback today”

Template name:

IN | WA1 | Start Conversations | 18-01-2026

  

Chat Builder, turn 50, ChatGPT (sixth version)

  

Welcome message

Hi\! Welcome to Setindiabiz. Please reply with:

1 = Company Registration

2 = LLP Registration

(Our team works 9:30 AM–7:30 PM IST. Outside hours, share details and we will call back.)

Suggested messages (Frequently asked questions)

1 - Company Registration

2 - LLP Registration

Fees & timeline

Send document checklist

If Meta forces Pre-filled message:

1 - Company Registration

Call to action: Get quote / Get started

Template name:

IN | WA1 | Company+LLP | StartConv | 18-01-2026

  

Zobot and SalesIQ specification, turn 50, ChatGPT (recommended; not confirmed built)

  

Name it like:

Zobot - Meta WA - Company/LLP

Trigger on first inbound message containing: 1, 2, “Company”, “LLP”, “fees”, “checklist”

Trigger on any new conversation, then route by keyword

First 4 questions:

Service selection (Company vs LLP)

City/State

Timeline (This week / 15 days / 30 days)

Phone + Email (or just Phone, then email later)

Within business hours (09:30–19:30 IST):

Bot collects 3–4 fields → assigns to available agent → “Connecting you to an expert now.”

Outside business hours:

Bot collects details → “Thanks. Our team will call you tomorrow between 9:30 AM–11:30 AM IST.”

Routing to 20 sales staff

Round-robin / load-balancing to your sales team

Priority to leads that selected “This week”

CRM creation:

Lead Source = Meta - WhatsApp

Campaign = IN | WA1 | Company+LLP

Service Interested = Company / LLP

City/State, Timeline

WhatsApp number (as phone)

Owner assignment (same as SalesIQ routing)

Hidden field / tag in the bot:

SourceCampaign = IN\_WA1

Adset = Metros\_BusinessHours

USA: Create a separate campaign prefix US | WA1 | …

  

Chat Builder, turn 51, ChatGPT (FINAL as last version given; turn 52 read a welcome message with business hours and FAQ buttons from his screen; turn 65 lists 1 - Company Registration, 2 - LLP Registration and Fees & timeline)

  

Hi\! Welcome to Setindiabiz. Please reply with:

1 = Company Registration

2 = LLP Registration

Also share your City/State + when you want to start (This week / 15 days / 30 days).

(Team hours: 9:30 AM–7:30 PM IST. Outside hours, share details and we will call back.)

Call to action

Get quote (preferred)

If “Get quote” is not available, choose “Get started”.

Frequently asked questions

1 - Company Registration

2 - LLP Registration

Question no. 3

Fees & timeline

Question no. 4

Send document checklist

Trigger rules (recommended)

If message contains “1” or “Company Registration” → Flow A (Company)

If message contains “2” or “LLP Registration” → Flow B (LLP)

If message contains “Fees” → show fee range + ask 2 questions

If message contains “Checklist” → send checklist + ask city + timeline

CRM Lead: Lead Source: Meta - WhatsApp; Campaign: IN | WA1 | Company+LLP; Service: Company / LLP; City/State + Timeline; Owner: based on routing

  

WhatsApp ad text options, turn 52, ChatGPT

  

Description Option 1 (best, neutral):

“Share your city & requirement. Our team replies 9:30 AM–7:30 PM IST.”

Description Option 2 (more direct):

“Get checklist + fees + timeline on WhatsApp. Reply in minutes during business hours.”

Primary Text options:

“Register your Private Limited Company or LLP with Setindiabiz. Chat on WhatsApp for fees, timeline and document checklist.”

“Starting a business? Get step-by-step guidance for Company/LLP registration. Message us on WhatsApp to begin.”

“Need MCA filing support for Company/LLP registration? WhatsApp us—our team shares checklist + estimated timeline.”

“Quick assistance on Company/LLP registration. Message on WhatsApp—share your city and requirement.”

(If you want a pricing angle) “Private Limited Company registration starting ₹3,499. WhatsApp to get exact fee breakup + checklist.”

Headlines:

“Company/LLP Registration”

“Get Fees & Checklist”

“Start on WhatsApp”

URL parameters:

utm\_source=meta\&utm\_medium=whatsapp\&utm\_campaign=IN\_WA1\_CompanyLLP\&utm\_content={{ad.name}}

Bot intents: “Company Registration”, “LLP Registration”, “Fees & timeline”, “Send document checklist”

Entity preference (Pvt Ltd / LLP / Not sure)

Timeline (immediately / 1 month / exploring)

Tag: After-hours WA lead

  

Three WhatsApp ads, turn 53, ChatGPT (FINAL as last version given; Sanjeev said Yes to all three angles; trust creative choice T1, T2 or T3 not stated)

  

Ad 1 — Pricing angle

Ad name: IN | WA1 | Pricing | A1

Creative: company-registration-1 Pricing.jpg (₹3,499)

Primary Text (paste):

Private Limited Company registration starting at ₹3,499.

Chat on WhatsApp to get exact fee breakup, timeline and document checklist.

Share your City/State to begin.

Headline: Chat on WhatsApp

Description: Fees + checklist + timeline (9:30 AM–7:30 PM IST).

  

Ad 2 — “Register Today” urgency angle

Ad name: IN | WA1 | RegisterToday | A2

Creative: company-registration-2.jpg (Register Today)

Primary Text (paste):

Register your Company or LLP with Setindiabiz.

Message us on WhatsApp for step-by-step guidance and document checklist.

Share your City/State + when you want to start.

Headline: Start on WhatsApp

Description: Fast response during business hours.

  

Ad 3 — Trust/Online/All-India service angle

Ad name: IN | WA1 | 100Online | A3

Creative: choose ONE of these as the trust creative:

company-registration-4.jpg (Rated/10,000+ businesses), OR

company-registration-3.jpg (100% online all India), OR

company-registration-1.jpg (same style as pricing but no price)

Primary Text (paste):

100% online Company/LLP registration — All-India service.

Chat on WhatsApp to get checklist, fees and expected timeline.

Our team will guide you end-to-end.

Headline: Company/LLP Registration

Description: Share your city & requirement on WhatsApp.

  

Destination: WhatsApp

CTA: Send WhatsApp message

Chat template: Use the same template you already built (Company / LLP / Fees / Checklist)

  

Business hours rules, turn 54, ChatGPT (superseded)

  

IN | BusinessHours | OFF | 19:30 IST

Apply rule to: Campaigns; Select campaigns starting with IN |; Action: Turn off campaigns; Conditions: none; Run rule: Daily; Time: 7:30 PM

IN | BusinessHours | ON | 09:30 IST

Apply rule to: Campaigns; Action: Turn on campaigns; Daily; 9:30 AM

  

Business hours rules, turn 55, ChatGPT (superseded)

  

IND | BusinessHours | OFF | 19:30 IST

Campaign name → contains → IND |

Daily window 19:30 to 20:00 (or 19:30 to 19:59)

IND | BusinessHours | ON | 09:30 IST

Daily window 09:30 to 10:00 (or 09:30 to 09:59)

Campaign name does not contain US |

  

Campaign name examples with #IND, turn 56, ChatGPT

  

#IND | C1 | Company+LLP | Leads | Advantage+

#IND | C1 | Web | Metros | Website-First

#IND | WA1 | Company+LLP | Messages | WhatsApp

  

Business hours rules, turn 56, ChatGPT (superseded on times)

  

#IND | BusinessHours | OFF | 19:30 IST

Apply rule to: All active campaigns; Action: Turn off campaigns; Campaign name → contains → #IND; Daily; 19:30–20:00 (or 19:30–19:59)

#IND | BusinessHours | ON | 09:30 IST

Apply rule to: All active campaigns; Action: Turn on campaigns; Campaign name contains #IND; Daily window 09:30–10:00

  

Custom schedule notes, turns 57 to 60, ChatGPT

  

Turn 57: OFF Start: 19:30 End: 19:30; ON 09:30 to 09:30; suggested buffer ON rule time = 09:00, OFF rule time = 19:00 (not used)

Turn 58: OFF rule 19:30 → 19:30; ON rule 09:30 → 19:29; do not use 19:30 → 09:29

Turn 59: his rule was at 07:30 → 07:30 and named IND|…; change to 19:30 → 19:30 and #IND | BusinessHours | OFF | 19:30 IST; ON rule #IND | BusinessHours | ON | 09:30-19:29 IST

Turn 60: 19:29 not selectable; ON window 09:30 → 19:00

  

Business hours rules, turns 61 to 63, ChatGPT and his screen (FINAL settings; he confirmed they apply to all #IND at turn 63)

  

Rule 1 — ON (Business Hours)

#IND | BusinessHours | ON | 09:30-19:00 IST

Apply rule to: All paused campaigns

Condition: Campaign name contains #IND

Action: Turn on campaigns

Schedule: Custom; Mon–Sun; 09:30 to 19:00

Rule 2 — OFF (After Hours)

#IND | BusinessHours | OFF | 19:30 IST

Apply rule to: All active campaigns

Condition: Campaign name contains #IND

Action: Turn off campaigns

Schedule: Custom; Mon–Sun; 19:30 to 19:30

Rule name still shown on screen at turn 62 and in the report at turn 65: #IND | BusinessHours | ON | 09:30-19:29 IST

Tag examples, turn 62: #IND | C1 | Company+LLP | Leads | Adv+ and #USA | C1 | Company+LLP | Leads | Adv+

Tag examples, turn 63: #IND | Trademark | Leads | WA and #IND | GST | Leads | Forms

  

Budget allocation and spend cap rule, turn 64, ChatGPT (not implemented; skipped at turn 65)

  

C1 Leads campaign: ₹2,500/day

WA1 WhatsApp campaign: ₹2,000/day

Total = ₹4,500/day

When you add another #IND campaign, allocate ₹1,500–₹2,000/day

Rule name:

#IND | SpendCap | OFF | C1 | ₹2600

Action: Turn off campaigns

Conditions:

Campaign name contains #IND

Campaign name contains C1 (or WA1 etc.)

Amount spent → today → greater than ₹2,600

Schedule:

Continuously

Hold tag: #HOLD

Campaign name does not contain #HOLD

  

Status report, turn 65, ChatGPT (full text)

  

Below is a structured status report covering (i) what has been completed, (ii) what this setup is likely to achieve, and (iii) the recommended next actions.

  

1\) Executive summary

  

You have successfully set up and published a Company & LLP Registration lead-generation program in Meta Ads Manager with:

  

Two lead capture routes:

  

Instant Forms (Meta lead form)

Website leads (landing page / website-first)

  

Multiple creatives / angles deployed (pricing, register-today, 100% online, etc.)

  

India business-hours control implemented via Automated Rules using the campaign naming tag #IND:

  

Auto ON during working hours

Auto OFF after working hours

  

WhatsApp campaign workstream initiated, including Click-to-WhatsApp “Chat Builder” welcome message and FAQ quick replies.

  

2\) What we have done so far (detailed)

A. Campaign structure and naming discipline

You agreed to a consistent naming pattern and the India marker tag:

Use #IND in campaign names so automated rules can target India campaigns only.

You now have separate ad sets and ads under the Company/LLP campaign with clear labels such as:

IN | C1 | Web …

IN | C1 | Forms …

IN | WA1 … (WhatsApp messages)

  

This will matter later for:

  

easier reporting,

rule-based automation,

scaling into additional campaigns (GST, Trademark, etc.).

B. Conversion locations and dataset

You faced a “no dataset” / pixel creation prompt earlier, then later the Dataset (pixel) is visible (example: “Setindiabiz JS”).

You confirmed and proceeded with:

Website and instant forms (multiple conversion locations)

Performance goal: maximizing conversions/leads

  

This is a practical setup because:

  

Forms deliver volume quickly.

Website leads help build a higher-intent pipeline (usually better quality but lower volume initially).

C. Ads created & published (Forms + Website)

You created multiple ads (3 key creatives) and resolved publishing errors related to:

missing link field / link URL required (asset customisation ads require link)

Ads are now published and no longer stuck in “draft” because required fields were corrected.

D. Creatives provided/used

  

You shared multiple square creatives (1:1). Key angles present:

  

“Register Company @ ₹3499/-” (price anchor)

“Register Your Company Today”

“100% Online / All India Service”

Trust-ish message (“Rated” style creative) – though note: if you claim ratings, you should be able to substantiate if asked.

  

At this stage, the assets are usable for:

  

Feed placements (FB/IG)

Some Reels placements may underperform unless 9:16 versions exist (you already fixed WhatsApp Status placement warning by unticking it).

E. WhatsApp message flow (Click-to-WhatsApp)

You configured the Chat Builder welcome message.

You set quick reply options such as:

“1 - Company Registration”

“2 - LLP Registration”

“Fees & timeline”

You also stated:

WhatsApp number is integrated with Zoho SalesIQ

You can build Zobot flows for WhatsApp

  

So the WhatsApp campaign can be made operational with:

  

Meta “start conversation” message template + quick replies

Zoho SalesIQ bot handling first-level qualification (or routing to agents)

F. Business-hours automation rules (India)

  

You successfully created two automated rules in Meta:

  

#IND | BusinessHours | ON | 09:30-19:29 IST

  

Applies to: All paused campaigns

Action: Turn on campaigns

Condition: campaign name contains #IND

Schedule: custom per day (09:30–19:00 in UI; you couldn’t select 19:29)

  

#IND | BusinessHours | OFF | 19:30 IST

  

Applies to: All active campaigns

Action: Turn off campaigns

Condition: campaign name contains #IND

  

This effectively enforces your operational window (daytime working hours) for India campaigns.

  

Note: Meta’s rule time picker is often in 30-min blocks; this is normal.

  

3\) What this setup is likely to achieve

A. Primary outcome: steady inbound leads within office hours

  

Instant Forms typically produce:

  

Higher lead volume

Lower cost per lead

Mixed intent quality (requires strong qualification + fast follow-up)

  

Website leads typically produce:

  

Lower volume at first

Better intent quality (user has taken more effort)

Better downstream conversion rate if landing page + follow-up are strong

  

With both running together, Meta will naturally try to allocate delivery to whichever yields cheaper “results” unless you constrain it.

  

B. Operational benefit: leads arrive when staff is available

  

Your 09:30–19:30 timing is aligned to:

  

immediate callbacks

higher connect rates

lower lead wastage

  

This alone can materially improve the effective cost per converted sale (even if CPL stays similar).

  

C. WhatsApp adds a “fast conversation” channel

  

WhatsApp campaigns generally:

  

increase contact-to-conversation rate

reduce friction vs forms

require strong scripting + bot handoff to avoid “chatty but unqualified” leads

  

Because you have Zoho SalesIQ, you’re positioned to:

  

qualify automatically

assign to agents

track conversation outcomes

4\) What we plan to do next (recommended sequence)

Step 1 — Confirm tracking + lead delivery integrity (1-time check)

  

Even though you verified tracking earlier, we should do a quick operational check:

  

Submit one test lead from each source:

Instant Form

Website form / website event (if used)

WhatsApp “start conversation”

Confirm:

lead appears in Meta leads center

lead reaches Zoho (Lead Chain)

WhatsApp chat reaches SalesIQ inbox / bot trigger works

  

Deliverable: “End-to-end verified” so scaling is safe.

  

Step 2 — Finalize WhatsApp bot flow (SalesIQ)

  

Implement a minimal, high-converting bot flow:

  

Bot goal: collect minimum qualifiers before human handover:

  

City

Type of entity: Pvt Ltd / LLP

Timeline: \<7 days / 7–15 days / 15+ days

WhatsApp consent + best time to call

  

Then:

  

assign to a sales queue

auto-create lead/ticket in Zoho (if that’s part of your SalesIQ setup)

Step 3 — Landing page optimisation for Website-first ads

  

For Website-first to work well, you need:

  

a dedicated landing page (fast load)

clear offer, checklist, timeline, document list

short form (name, phone, city, entity type)

WhatsApp CTA as backup

  

We will also prepare the exact ad copy variations for website placements (Feed/Reels) so Meta can rotate.

  

Step 4 — Reporting structure and quality feedback loop

  

Set up a lightweight daily review:

  

Spend

Leads by source (Form / Website / WhatsApp)

Cost per lead

Contact rate (connected / not connected)

Qualified leads

Booked consultations

Closures

  

This is how you ensure the campaign improves week over week.

  

Step 5 — Expand with alternate geo-ad set (low competition regions)

  

You previously discussed J\&K and North East.

After stability of the main campaign:

  

create a separate ad set targeting lower-competition regions

keep budget controlled

compare lead quality vs metros

5\) Immediate next action (tell me what you want to do now)

  

Choose one for the next step:

  

End-to-end verification (test lead from each channel and check Zoho + SalesIQ)

SalesIQ WhatsApp bot (I will give the exact bot question flow + routing rules + fallback messages)

Website landing page + ad copy pack (I will write the final website ad text variants and the landing page structure)

  

Reply with 1 / 2 / 3, and also confirm: are you running Forms + Website + WhatsApp simultaneously from Day 1, or do you want to phase them (e.g., Forms first, WhatsApp next)?

  

Comet browser extension audit prompt, turn 66, ChatGPT (FINAL, full text)

  

You are my Ads Operations Auditor. Your job is to open Meta Ads Manager in my browser and conduct a COMPLETE AUDIT of my current setup for Company/LLP Registration lead generation in India, including Website + Instant Forms + WhatsApp (Messages).

  

IMPORTANT RULES

1\) Do NOT publish, duplicate, delete, or edit anything unless I explicitly ask after your audit report.

2\) Do NOT change budgets, bids, targeting, creatives, or forms during the audit.

3\) If you see any errors/warnings, document them precisely and propose fixes, but do not apply fixes automatically.

4\) Maintain confidentiality. Do not reveal any sensitive IDs, tokens, phone numbers, or customer data in your report.

  

AUDIT SCOPE (CHECK EVERYTHING)

A) ACCOUNT / BUSINESS SETTINGS (read-only checks)

\- Confirm the ad account name and business manager being used.

\- Confirm timezone and currency.

\- Check if there are any account-level spend limits, payment issues, restrictions, or policy warnings.

  

B) CAMPAIGN STRUCTURE & NAMING (India controls)

\- Identify all campaigns relevant to India lead gen.

\- Verify naming convention: India campaigns should include the tag "#IND" (or the chosen tag).

\- List all campaigns containing "#IND" and summarize: objective, status, budget type (Campaign budget vs Ad set budget), daily budgets, and any draft/pending changes.

  

C) AUTOMATED RULES (Business Hours)

\- Navigate to Automated Rules and find rules related to "#IND".

\- Verify two rules exist and are ENABLED:

1\) BusinessHours ON: turns ON campaigns during business hours.

2\) BusinessHours OFF: turns OFF campaigns after hours.

\- For each rule, capture:

\- Rule name

\- Applied to: (All active campaigns / All paused campaigns etc.)

\- Condition: campaign name contains "#IND"

\- Schedule: day-by-day timing and timezone

\- Next run/start time

\- Any conflicts or edge cases

\- Validate that the rules will NOT affect non-India campaigns (e.g., USA campaigns) by confirming the condition is "#IND" based.

  

D) CAMPAIGN-LEVEL SETTINGS (C1 India Company/LLP Registration)

For the primary India campaign(s):

\- Objective: Leads (confirm)

\- Buying type: Auction (confirm)

\- Advantage+ settings enabled/disabled (note)

\- Budget strategy: Campaign budget vs Ad set budget (note)

\- Daily budget amounts and any maximum spend behavior

  

E) AD SET AUDIT (each ad set under the India campaign)

For every ad set under the campaign:

1\) Delivery & optimization

\- Conversion location: Website / Instant forms / Messenger / WhatsApp / Calls (confirm exact choice)

\- Performance goal and conversion event

\- Dataset / Pixel selection (confirm dataset name)

\- Attribution settings and any related warnings

2\) Audience / targeting

\- Locations included/excluded (India states/metros vs NE/J\&K etc.)

\- Age settings (note if only minimum age is available; record what minimum is set)

\- Advantage+ audience settings / broad targeting settings

\- Language settings (if any)

3\) Placements

\- Advantage+ placements vs manual placements

\- Confirm WhatsApp Status placement is OFF if creatives are not 9:16 (note current status)

\- Flag any placement warnings

4\) Budget & schedule at ad set level (if applicable)

\- If ad set budgets used, record daily budget and any schedule

5\) Value rules / bid adjustments (if used)

\- Identify any value rules (e.g., +20% website, -30% forms) and verify they apply correctly.

\- Document where they are applied and whether they could distort learning or delivery.

  

F) AD-LEVEL AUDIT (all ads under each ad set)

For each ad:

\- Status: Active / In draft / errors / pending review

\- Creative format: single image / carousel

\- Check the creative assets used (file/thumbnail)

\- Primary text, headline, description, CTA button

\- Destination:

\- Website URL (present? correct? UTM parameters if used?)

\- Instant form selected (correct form name?)

\- WhatsApp destination (correct number / account?)

\- Advantage+ creative enhancements: identify what is ON (text variations, image improvements, auto-cropping, etc.)

\- Flag any policy risk:

\- Price claims (“₹3499/-”) — ensure offer clarity

\- Rating claims (“4.8/5 rated by 10,000+ businesses”) — must be substantiable

\- Any misleading wording

\- Flag any missing required field errors (e.g., link URL missing)

\- Confirm ads are not duplicated unintentionally in a way that causes internal competition (same ad repeated across multiple ad sets without intent).

  

G) INSTANT FORM AUDIT (Lead form quality & compliance)

For each Instant Form in use:

\- Form type: More volume vs Higher intent (note)

\- Questions asked (Name, Phone, City, etc.)

\- Privacy policy link present and correct

\- “Description” field on form and thank-you page:

\- Confirm it exists

\- Confirm it clearly states how data will be used/shared

\- Thank-you screen:

\- Confirm call-to-action is set (e.g., visit website, call, WhatsApp)

\- Lead delivery setup:

\- Check CRM integration status if visible (Zoho lead chain mentioned by user)

\- Confirm lead delivery is not failing or disconnected

  

H) WEBSITE TRACKING AUDIT (for website-first ads)

\- Navigate to Events Manager (if available) and check:

\- Dataset/pixel status: active/inactive, last received event

\- Conversion events: Lead / Submit form / Contact etc.

\- Any AEM / attribution / domain verification warnings

\- Confirm website URL used in ads is correct and loads.

\- Check if there are any obvious mismatches (e.g., optimizing for event that has no recent activity).

  

I) WHATSAPP / MESSAGES AUDIT (Click-to-WhatsApp)

\- Verify WhatsApp destination is correct (business account)

\- Review Chat Builder setup:

\- Welcome message text

\- FAQ quick replies (Company Registration, LLP Registration, Fees & timeline)

\- Any prefilled message configuration

\- Template name conventions

\- Confirm setup aligns with operational workflow:

\- Mention business hours (9:30–7:30 IST)

\- Outside hours fallback message present

\- Note: user has WhatsApp integrated with Zoho SalesIQ and intends to use Zobot.

\- Provide a recommendation checklist for alignment (handoff to human, tagging, lead creation), but do not configure anything.

  

OUTPUT REQUIRED (FINAL REPORT FORMAT)

Deliver a structured report with:

1\) Overall health score (Green/Amber/Red) + top 5 risks

2\) Inventory list:

\- Campaigns (#IND), Ad sets, Ads, Forms, WhatsApp templates, Rules

3\) Issues & warnings (exact text, where found, severity)

4\) Policy/compliance risks (pricing, claims, disclosures)

5\) Optimization opportunities (no changes yet) prioritized:

\- Quick wins (same day)

\- Medium (1–3 days)

\- Strategic (1–2 weeks)

6\) “Action plan next”:

\- Exact steps I should take in Ads Manager in order, with the safest sequence.

  

STOP CONDITION

After you finish the audit, DO NOT click Publish. DO NOT apply changes. Present the report and wait for my approval for any fixes.

  

Notes given with the prompt, turn 66, ChatGPT

  

Use #IND (as you’re doing) rather than plain “IN/IND” because “contains” can catch unintended names. #IND is cleaner and less error-prone.

If Comet can export notes, ask it to include screen names + section headings so you can later find items quickly inside Ads Manager.

### Open items and next steps

Next steps listed in the turn 65 report: (1) end-to-end test lead from Instant Form, website and WhatsApp, checking Meta leads center, Zoho and SalesIQ; (2) finalise the SalesIQ WhatsApp bot flow; (3) landing page optimisation and website ad copy pack; (4) daily reporting and quality feedback loop; (5) alternate geo ad set for lower-competition regions.

Turn 65 question unanswered: reply 1, 2 or 3, and whether Forms, Website and WhatsApp all run from day 1 or are phased.

Comet audit (turn 66): prompt written; no result appears in the chat.

Zoho test lead: asked at turn 23 and again at turns 29 and 31; no result confirmed in the chat.

WhatsApp ads: publication and status, and the outcome of the securities and investments declaration (Review requirements, turns 43 to 47), not confirmed.

Zobot flows for WhatsApp (triggers, business hours branches, CRM lead creation, tags): recommended, not confirmed built.

Naming: whether every India campaign was actually renamed to contain #IND is not confirmed. The turn 65 report still shows IN | names. The rules act only on names containing #IND.

ON rule: renaming from 19:29 to 09:30-19:00 was requested at turns 62 and 63 and is not confirmed; the turn 65 report still shows 19:29. Time zone check (IST) also not confirmed.

#HOLD or similar exclusion in the ON rule: proposed at turns 35, 40 and 64, not done. Without it the ON rule restarts any paused #IND campaign.

Spend cap: the hard or average cap question at turn 64 was left open when he skipped budget optimisation at turn 65. Spend cap rules not created.

Company campaign daily budget: ₹2,500 versus ₹3,500 on screen at turn 24 is unresolved in the chat.

Metro list: the C1 list has 7 cities; the WhatsApp list at turns 32, 41 and 43 adds Kolkata. Actual locations not confirmed.

Campaigns not yet built: Indian Subsidiary and India Entry, Trademark, GST, plus any use of the Startup India DPIIT landing page. US campaigns to use a #USA tag and separate rules.

Tier 2, J\&K and North East ad set: planned for after all ads and stability.

Creatives: 9:16 versions needed before re-adding WhatsApp Status. The 4.8/5 Rated by 10,000+ Businesses claim must be substantiated before use.

Optional rule Pause expensive website ads (turn 31): not confirmed created.

Chat gaps: turn 36 and turn 49 have no ChatGPT reply in the captured text.
