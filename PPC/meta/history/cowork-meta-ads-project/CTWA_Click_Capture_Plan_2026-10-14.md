# WhatsApp ad click ID (ctwa_clid): capture and send — plan, 14 Oct 2026

Sanjeev, 14 Oct: "solve it" (about the open item in `Change_Log_2026-10-14_CAPI-All-Signals.md`: no click ID, so Meta can't credit CRM outcomes to the click-to-WhatsApp ads).

Status: **W1–W5 BUILT and tested 14 Oct 2026, 21:00–21:22 IST** (Sanjeev: "Build it now"); see `Change_Log_2026-10-14_CTWA-Click-Capture.md`. Waiting on Sanjeev's Meta steps (§4). W6 follows the first captured click. The matcher runs every 2 hours, not hourly. Code: `sib_wa_click_hook_v1`, `sib_wa_setup_v1`, `sib_wa_click_lookup_v1`, `sib_wa_click_match_v1` (all `_2026-10-14.deluge.txt`).

## 1. Findings (read only)

| # | Finding | Source |
|---|---|---|
| F1 | SalesIQ never receives the click ID. It keeps only the ad's post link, put in front of the visitor's first message. Of 181 "Compliance & ACR" chats: 130 start with an fb.me link, 40 with an instagram.com/p/ link, 11 with none. The conversation and visitor records hold no `ctwa_clid` or `source_id`. | SalesIQ web API, conversation 61466000026785691 and others |
| F2 | So the bot can't pass it, and the plug's `clid` input stays empty (all 174 WhatsApp leads have a blank CTWA_Click_ID). Waiting on SalesIQ/Zoho won't fix this. | CRM, plug code |
| F3 | All 8 SalesIQ WhatsApp numbers sit in **one WhatsApp account: "Setindiabiz - Salesiq", ID 2287130705376253**. It is owned by Setindiabiz Private Limited, with Zoho as partner (Zoho credit line). The SIB-04 number [phone redacted] is one of them. The others: [phone redacted], [phone redacted], [phone redacted], 95991 99509, [phone redacted], [phone redacted], 95994 81905. | Business Suite, WhatsApp Manager |
| F4 | Because Setindiabiz owns the account, a Setindiabiz app can subscribe to its webhooks next to SalesIQ's. Meta then sends the first message after an ad click, with `referral.ctwa_clid`, `source_id` (ad ID), `source_url` and `headline`, to both apps. | Meta Cloud API webhook docs |
| F5 | Existing Meta apps: "Setindiabiz" (2379539855916311, Facebook Login use case only, in development) and "Zoho Bookings Integration" (Business type, in development). Neither has WhatsApp. Business Settings > Apps asks for a passkey re-login. | developers.facebook.com |
| F6 | A Zoho CRM function can be exposed as a REST URL with an API key and can reply with plain text, which is what Meta's webhook verification needs. No outside server is needed. CRM is Zoho One Enterprise, 121 users, so API calls are not a constraint. | Zoho docs, CRM org |
| F7 | Meta's Conversions API for Business Messaging needs `action_source: business_messaging`, `messaging_channel: whatsapp`, `user_data.whatsapp_business_account_id` and `user_data.ctwa_clid`. The token needs `whatsapp_business_management` and `whatsapp_business_manage_events`. Standard event names only. Meta does not dedupe these. Click attribution is 7 days. | developers.facebook.com/docs/marketing-api/conversions-api/business-messaging |

## 2. Design

```
Customer taps a WhatsApp ad ─► first message ─► Meta sends the webhook to BOTH apps
   SalesIQ app (unchanged): chat, Zobot, plug, CRM lead as today
   "Setindiabiz WA Signals" app ─► Zoho function sib_wa_click_hook
        stores only messages that carry a click ID ─► module WA Ad Clicks
              (click ID, phone, ad ID, post link, headline, time)
Hourly sib_wa_click_match ─► links click to the Lead by phone; fills CTWA_Click_ID / Meta_Ad_ID if blank
CRM stage change (sender v3 / sweep v4) ─► click in the last 7 days for this phone?
        yes ─► business_messaging event with ctwa_clid (Meta credits the ad)
        no  ─► system_generated event as today
```

One event per stage per record, as now (`Meta_CAPI_Event` guard). The channel is chosen per event, so the same sale is never reported twice.

| CRM stage | Today | With a click in the last 7 days |
|---|---|---|
| Valid lead | ValidLead (custom) | **LeadSubmitted** |
| Progressed | QualifiedLead | QualifiedLead (if Meta rejects it, the code falls back to today's event) |
| Payment Wait | Committed (custom) | **InitiateCheckout** |
| Won | Purchase + value | Purchase + value |

## 3. Changes in CRM (each needs Sanjeev's go)

| # | Change | Rollback |
|---|---|---|
| W1 | New custom module **WA Ad Clicks** (`WA_Ad_Clicks`), visible to administrators only. Fields: Click ID (unique), Customer Phone, Phone Last10, Clicked At, Click Epoch, WABA ID, Business Number, Ad ID, Source Type, Source URL, Ad Headline, Lead (lookup), Match Status (Unmatched / Matched / Contact / Expired), Signature Check. | Delete the module |
| W2 | Three org variables, created empty: `meta_wa_verify_token`, `meta_wa_app_secret`, `meta_wa_access_token`. **Sanjeev pastes the values; I don't handle them.** | Delete |
| W3 | Function **sib_wa_click_hook**, REST API with API key. GET answers Meta's verification; POST keeps only ad clicks. No message text is stored or logged. The signature is checked and recorded, not yet enforced. | Disable the REST API |
| W4 | Function **sib_wa_setup** (run by hand): `check`, `subscribe`, `dataset`. Never prints the token. | Delete |
| W5 | Function **sib_wa_click_lookup** and hourly schedule **sib_wa_click_match**. Lead edits use trigger [] and touch only blank CTWA_Click_ID / Meta_Ad_ID. | Delete; clear the two fields |
| W6 | **After the first real click is captured:** sender v3 (both copies) and sweep v4 add the business_messaging branch in §2. | Revisions → 14 Oct v2 / v3 |

## 4. Steps only Sanjeev can do in Meta (they involve logins, secrets or tokens)

1. **Create the app.** developers.facebook.com/apps → Create app → name "Setindiabiz WA Signals" → use case "Connect with customers through WhatsApp" → business portfolio Setindiabiz Private Limited.
   **Do not add, register or migrate any phone number, and ignore the test number.** This app only listens; SalesIQ keeps sending and receiving.
2. **Webhook.** Use cases → WhatsApp → Customize → Configuration:
   - Callback URL = the API-key URL of `sib_wa_click_hook`. Copy it from Zoho: Functions → sib_wa_click_hook → REST API → API Key.
   - Verify token = any long random text. Paste the same text into Zoho org variable `meta_wa_verify_token` first.
   - Verify and save, then subscribe the field **messages** only.
3. **App settings → Basic.**
   - Privacy policy URL: https://www.setindiabiz.com/privacy-policy. Category: Business. Save.
   - Copy the App secret into `meta_wa_app_secret`.
   - Then **Publish** the app (Live). Meta says some webhooks are not sent while an app is in development mode.
4. **System user and token.** Business Settings → System users → Add "sib-wa-signals".
   - Assign assets: the new app (full control), WhatsApp account "Setindiabiz - Salesiq" (full control), dataset "setindiabiz" (manage).
   - Generate token: app = Setindiabiz WA Signals, expiry Never. Permissions: `whatsapp_business_management`, `whatsapp_business_messaging`, `whatsapp_business_manage_events`.
   - Paste the token into `meta_wa_access_token`.
5. Tell me. I then run `sib_wa_setup`:
   - `check`: token app and scopes, apps already on the account;
   - `subscribe`;
   - `check` again: SalesIQ's app and ours should both be listed;
   - `dataset`: we expect 1242417817083521. If Meta returns a different ID, the WhatsApp events go to that one.

## 5. Test

1. Tap a live SIB-04 ad on a phone and send the pre-filled message.
2. A WA Ad Clicks record appears within seconds with the click ID, ad ID and Signature Check = ok.
3. After the next hourly match, the lead shows CTWA_Click_ID and Meta_Ad_ID.
4. After W6, on the next grading of a clicked lead, the log shows `business_messaging … events_received: 1`. Events Manager → dataset → WhatsApp shows the event.

## 6. Risks and limits

- **Only new clicks.** The 174 existing WhatsApp leads can't be backfilled; Meta never sent us their click IDs.
- **Meta access tier.** Meta's page lists partner requirements (advanced access, Ads Management Standard Access). For a business sending events for its own WhatsApp account, standard access should be enough; the first event will show it. If Meta refuses, events keep going as system_generated, so nothing is lost.
- **7-day window.** Stages reached more than 7 days after the click (many sales) go as today's system_generated events, matched on hashed phone.
- **Volume.** Every inbound message and delivery status on all 8 numbers calls the function, but only messages with a click ID are stored. API credits are ample (Enterprise, 121 users).
- **Usernames (BSUID).** Meta is rolling out WhatsApp usernames. A customer using one may arrive without a phone number, and such clicks won't match by phone. Watch the Unmatched count.
- **Organic-coded ad leads.** A click record on a lead whose source is "Social - WhatsApp" means the customer edited the pre-filled message and the ad code was lost. Report these to the SalesIQ project; this build does not touch Lead_Source.
- **Personal data.** Message text passes through the function but is not stored or logged. Only the phone number and ad details of ad clicks are kept, in an admin-only module. The business_messaging events send Meta only the click ID and account ID, with no phone or email. This is in line with the necessity limit on consent in s.6(1) of the Digital Personal Data Protection Act, 2023 (DPDP Rules 2025 notified Nov 2025, obligations phasing in).
