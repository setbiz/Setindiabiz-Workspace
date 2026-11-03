# Resume prompt: WhatsApp ad click ID capture (paste into a new session in "Meta Ads - Optimisation")

You are continuing work for Sanjeev Kumar (Setindiabiz) as the Meta Ads operator. On 14 Oct 2026 we built capture of the click-to-WhatsApp click ID (`ctwa_clid`), so CRM outcomes for WhatsApp-ad leads can be sent to Meta and credited to the ads. **Everything is live except the last step (W6).** Read these project docs first:

- `Meta Ads/CTWA_Click_Capture_Plan_2026-10-14.md`: why, design, event mapping, risks.
- `Meta Ads/Change_Log_2026-10-14_CTWA-Click-Capture.md`: what was built, tests, Meta-side steps.
- `Meta Ads/Change_Log_2026-10-14_CAPI-All-Signals.md`: earlier the same day: sender v2, sweep v3, the `Meta_CAPI_Event` once-per-stage guard.
- Code: `sib_wa_click_hook_v1`, `sib_wa_setup_v1`, `sib_wa_click_lookup_v1`, `sib_wa_click_match_v1` (all `_2026-10-14.deluge.txt`); `sib_sendMetaCAPI_v2_2026-10-14.deluge.txt`; `sib_capisweep_v3_2026-10-14.deluge.txt`.

## Why this was needed (one paragraph)

SalesIQ never receives `ctwa_clid`: it keeps only the ad's post link at the start of the first message. So our own Meta app listens to the same WhatsApp account alongside SalesIQ. Meta sends the first message after an ad click, with `referral.ctwa_clid`, to a Zoho CRM function. The function stores the click, and CAPI events for that lead or deal can then be sent as `business_messaging` with the click ID.

## What is live (IDs)

**Meta**
- App **Setindiabiz WA Signals**, ID **1445554577564805**: published; webhook verified; field `messages` subscribed (v26.0).
- WhatsApp account (Meta now calls these "Messaging accounts") **Setindiabiz - Salesiq**, ID **2287130705376253**. It holds all 8 SalesIQ numbers, including SIB-04's [phone redacted].
  - Subscribed apps: ours, plus **Zoho Social** 191062257579887 (SalesIQ's app, override callback push.zohoim.com). Never touch Zoho Social.
- System user **SIB WA Signals**, ID 61595138651832, Employee:
  - token never expires; scopes whatsapp_business_management / messaging / manage_events;
  - assigned the WhatsApp account via Messaging accounts → Setindiabiz - Salesiq → Assign people.
- **WhatsApp dataset 1442186757791533**, created and linked to the WhatsApp account by `POST /{WABA}/dataset`. All business_messaging events go here.
  - The web/CRM dataset **1242417817083521** is unchanged and still gets the system_generated events (`meta_capi_access_token`).

**Zoho CRM** (Zoho One Enterprise, 121 users)
- Module **WA Ad Clicks** (`WA_Ad_Clicks`, id 1123581000947966257), Administrator only.
  - Fields: Click_ID (unique), Customer_Phone, Phone_Last10, Clicked_At, Click_Epoch, WABA_ID, Business_Number, Ad_ID, Source_Type, Source_URL, Ad_Headline, Lead (lookup), Match_Status (Unmatched / Matched / Contact / Expired), Signature_Check.
- Function **sib_wa_click_hook** (id 1123581000947966992, `map crmAPIRequest`). REST API with API key, enabled under Functions → SIB WA Click Hook → Overview → REST API. **The URL is a credential: never write it into docs.**
  - GET answers the verify challenge. POST stores only messages with `referral.ctwa_clid`. The signature is recorded in Signature_Check, not enforced.
- Function **sib_wa_setup** (`String action`): check / subscribe / dataset; never prints the token.
- Function **sib_wa_click_lookup** (`String phone`): returns a JSON string of the latest click in the last 7 days for the last 10 digits of the phone, or "{}".
- Schedule **SIB WA Click Match - Hourly** → `sib_wa_click_match`. Actually runs **every 2 hours** (Zoho's form default, kept).
  - Links click → Lead by phone; fills Lead CTWA_Click_ID / Meta_Ad_ID only if blank (trigger []); Contact / Expired statuses.
- Org variables, filled by Sanjeev: `meta_wa_verify_token`, `meta_wa_app_secret`, `meta_wa_access_token`. Never read them out or print them.

**Tested on 14 Oct (synthetic posts with curl):**
- the click was stored and no message text was kept;
- a delivery receipt was ignored;
- a repeated click was not stored twice;
- a wrong verify token got 403;
- the HMAC signature matched (Zoho passes the raw body).

## Where it stopped

At 22:20 IST on 14 Oct there were no real clicks yet (only minutes after subscribing). **Step 1 tomorrow:**

1. Run COQL on `WA_Ad_Clicks` (all fields).
2. Check the hook function's Analytics and Failures tabs in Zoho: invocations since 22:17 IST, 14 Oct, show that Meta is delivering.
3. Read the outcome:
   - **Clicks present with Signature_Check = ok**: capture works. Check Ad_ID against live SIB-04 ad IDs (Meta connector) and that the match job linked them to leads.
   - **Invocations but no clicks**: traffic arrives but no ad clicks yet. Wait, or ask Sanjeev to tap a live SIB-04 ad and send the pre-filled message.
   - **No invocations at all**:
     - check the app is still Published;
     - check `messages` is still subscribed (developers.facebook.com → app → Use cases → WhatsApp → Customize → Configuration);
     - run `sib_wa_setup` with action "check".

## Next steps after capture is confirmed (ask Sanjeev before each CRM write; show the change first)

1. **W6: send click-attributed events.** Applies to sender v3 (both copies: `sib_sendMetaCAPI` for Leads, `sib_sendMetaCAPI1` for Deals) and sweep v4.
   - **When:**
     - Leads: lead's Lead_Source = "Advt - WhatsApp" and `standalone.sib_wa_click_lookup(phone)` returns a click from the last 7 days.
     - Deals: use the contact's phone.
   - **What to send:** a `business_messaging` event:
     - `messaging_channel: "whatsapp"`;
     - `user_data {whatsapp_business_account_id, ctwa_clid}`;
     - POST to `/1442186757791533/events` with `meta_wa_access_token`.
   - **Event names:** ValidLead → **LeadSubmitted**; QualifiedLead → QualifiedLead; Committed → **InitiateCheckout**; Purchase → Purchase (+ value, INR).
   - **Otherwise, or if Meta rejects it:** fall back to today's system_generated event on dataset 1242417817083521.
   - **One send per stage per record**, via the existing `Meta_CAPI_Event` guard, so nothing is double counted. Meta does not dedupe business_messaging events.
   - **Test** on the first real clicked lead when it is graded.
2. **Enforce the signature**: hook v2 returns 200 but stores nothing when Signature_Check ≠ ok. Do this only after real clicks show "ok".
3. **Note to the SalesIQ project:**
   - Clicks whose lead is "Social - WhatsApp" mean the visitor edited the pre-filled message, so the ad code was lost. Fixing Lead_Source is their call.
   - Our app now listens on the same WhatsApp account.
4. Still open from before: update the desktop daily watchdog (three paid-Meta sources; new Purchase baseline of about 1–2 a day).
5. Optional later:
   - Meta's `automatic_events` webhook field;
   - choosing dataset 1442186757791533 in CTWA ad sets that optimise for LeadSubmitted / Purchase. That's a Meta change and needs approval.

## Working rules and gotchas learned

- **Never handle secrets.** Sanjeev pastes tokens, the app secret, the verify token and the webhook URL himself.
- In Chrome, the safety check blocks me from these, so Sanjeev clicks:
  - creating the app;
  - publishing it;
  - creating system users and assigning assets.
- Meta UI quirks:
  - WhatsApp accounts are now "Messaging accounts".
  - The system-user asset picker shows WhatsApp accounts as "Setindiabiz Private Limited", so assign them from the account's own page instead.
  - System-user names can't contain several hyphens.
  - Business Settings → Apps asks for a passkey re-login.
- Zoho quirks:
  - The IDE's Run builds its own `crmAPIRequest` and ignores typed input, so test the webhook with curl against the real URL. The workspace can reach www.zohoapis.com.
  - Paste code with `document.querySelector('.CodeMirror').CodeMirror.setValue(...)`, then Save.
  - Telephony "Call is missed" pop-ups appear in Sanjeev's CRM session; just dismiss them.
- The CRM connection that can run COQL on Leads and Contacts from CRM functions is `contact_to_lead` (v3 endpoint).
- The SalesIQ project owns the bot, plugs, Desk rules and `RM_Lead_Ticket`. Don't change those.
