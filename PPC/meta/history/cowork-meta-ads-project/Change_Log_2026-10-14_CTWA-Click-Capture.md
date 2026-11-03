# Change log — 14 Oct 2026 — WhatsApp ad click ID capture (CRM side built)

**Approval:** Sanjeev, 14 Oct: "solve it", then "Build it now (Recommended)" for W1–W5. W6 (sender/sweep) waits for the first captured click.
**Plan:** `Meta Ads/CTWA_Click_Capture_Plan_2026-10-14.md`.
**Code:**
- `sib_wa_click_hook_v1_2026-10-14.deluge.txt`
- `sib_wa_setup_v1_2026-10-14.deluge.txt`
- `sib_wa_click_lookup_v1_2026-10-14.deluge.txt`
- `sib_wa_click_match_v1_2026-10-14.deluge.txt`

## Changes

| # | Time (IST) | Item | Change | Verified |
|---|---|---|---|---|
| W1 | 21:00 | Module **WA Ad Clicks** (`WA_Ad_Clicks`, CustomModule11, id 1123581000947966257) | Administrator profile only, Root teamspace. 14 fields by API: Click_ID (unique), Customer_Phone, Phone_Last10, Clicked_At, Click_Epoch, WABA_ID, Business_Number, Ad_ID, Source_Type, Source_URL, Ad_Headline, Lead (lookup → Leads, related list "WA Ad Clicks"), Match_Status (Unmatched / Matched / Contact / Expired), Signature_Check. | COQL on all fields (204, empty) |
| W2 | 21:02 | Org variables, **empty** | `meta_wa_verify_token` (single line), `meta_wa_app_secret` (single line), `meta_wa_access_token` (multi-line). **Sanjeev pastes the values.** | getVariables |
| W3 | 21:03–21:12 | Function **sib_wa_click_hook** (standalone, id 1123581000947966992, argument `map crmAPIRequest`) | **API Key access enabled.** Copy the URL from Functions → SIB WA Click Hook → Overview → REST API → API Key. The URL is a credential: it is not written in any project doc. | See tests below |
| W4 | 21:16 | Function **sib_wa_setup** (standalone, `String action`) | check / subscribe / dataset. It reads the token from the variable and does not print it. | Saved; returns "token is empty" until filled |
| W5a | 21:15 | Function **sib_wa_click_lookup** (standalone, `String phone`) | Returns the latest click for the phone in the last 7 days, as JSON. | Run on a test phone: returned the test click (ID, account, ad, time, record) |
| W5b | 21:22 | Schedule **SIB WA Click Match - Hourly** → `sib_wa_click_match` | Runs **every 2 hours** (Zoho's form default, kept), first run 21:45. Links clicks to the Lead by phone and fills Lead CTWA_Click_ID / Meta_Ad_ID only if blank, with trigger []. If there is no lead but a Contact exists, the status becomes Contact. After 7 days with no match, the status becomes Expired. | Manual run: "0 unmatched checked" |

## Webhook tests (curl to the API-key URL, 21:13–21:14)

1. **GET** with a wrong verify token returns **403 "forbidden"**. The token is not set yet, so verification cannot pass by accident.
2. **POST**, a Meta-format ad click (phone 910000000000, `ctwa_clid` TEST-…). Returns **200 "ok"**. The record was created with every field correct; the message text was not stored.
3. **POST**, a delivery-status-only notification. Returns 200 "ok" and **nothing stored**.
4. **POST**, the same click again. Not duplicated (Click_ID is unique).
5. **POST**, signed with a temporary dummy secret, Meta-style payload with `\u` and `\/` escapes. **Signature_Check = ok**: Zoho passes the raw body unchanged, so Meta's signature can be enforced later. The dummy secret was cleared straight after.
6. The two TEST records were deleted (Recycle Bin).

Notes:
- IDE "Run" builds its own request object and ignores the typed input. Webhook tests must use the real URL.
- The function returns `content-type` application/json whatever the code sets. Meta compares only the body, which is the raw challenge.

## Meta side (14 Oct, 21:36–22:20 IST; Sanjeev did the clicks Chrome's safety check reserved for him)

| # | Item | Result |
|---|---|---|
| M1 | App **Setindiabiz WA Signals**, ID **1445554577564805**, use case "Connect with customers through WhatsApp", business 629080835992237 | Created by Sanjeev |
| M2 | Webhook | Sanjeev pasted the callback URL and verify token, and Meta verified them. Field **messages** is subscribed (v26.0), set by me. |
| M3 | App settings → Basic | Set by me: privacy policy URL https://www.setindiabiz.com/privacy-policy; data deletion link: the same page; category Business and pages. Sanjeev put the app secret into `meta_wa_app_secret`. |
| M4 | Publish | **Published** (Sanjeev). |
| M5 | System user **SIB WA Signals** (ID 61595138651832, Employee) | Created by Sanjeev. The name "sib-wa-signals" was refused (too many hyphens). Token: never expires, scopes whatsapp_business_management / messaging / manage_events, saved in `meta_wa_access_token`. The WhatsApp account is assigned through Messaging accounts → Setindiabiz - Salesiq → Assign people. In the system-user picker it shows only as "Setindiabiz Private Limited". |
| M6 | `sib_wa_setup` check / subscribe / check | `subscribe`: **success**. The account's subscribed apps are now **Setindiabiz WA Signals** plus **Zoho Social** (191062257579887, SalesIQ's app, override callback push.zohoim.com), which is untouched. |
| M7 | `sib_wa_setup` dataset | No dataset was linked to the WhatsApp account. POST created and linked **dataset 1442186757791533**. The business_messaging events (W6) go there. The web/CRM dataset 1242417817083521 stays as it is; Events Manager has no option to link a WhatsApp account to it. |

Check-in scheduled for 23:06 IST to look for the first real click.

## Next (was: needs Sanjeev, in Meta)

Plan §4, steps 1–4:
1. Create the app.
2. Webhook URL and verify token (paste the token into Zoho first), then subscribe to **messages**.
3. App secret into Zoho, then publish the app.
4. System user and token into Zoho.

Then I run `sib_wa_setup` (check → subscribe → check → dataset), and Sanjeev sends one test click from a phone on a live SIB-04 ad.

## Rollback

- Turn off API Key access on sib_wa_click_hook. This stops all intake at once.
- Deactivate the schedule.
- Delete the functions, the module and the variables if the project is dropped.
- No existing function, field, rule or SalesIQ setting was changed.
