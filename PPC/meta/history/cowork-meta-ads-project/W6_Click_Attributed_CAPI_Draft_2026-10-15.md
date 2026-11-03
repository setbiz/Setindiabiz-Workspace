# W6: WhatsApp-click CAPI events and signature check — 15 Oct 2026 (DEPLOYED)

**Status:** **deployed 14:42–14:49 IST.** Sanjeev chose "Deploy all four". Record: `Change_Log_2026-10-15_W6-Deployed.md`.
Sanjeev, 13:53: "Yes" (to "Shall I prepare the W6 code now?").
Plan: `CTWA_Click_Capture_Plan_2026-10-14.md` §2 and §3 (W6).

**Code (live):**

| Live file | Replaces |
|---|---|
| `Meta Ads/sib_sendMetaCAPI_v3_2026-10-15.deluge.txt` | `sib_sendMetaCAPI_v2_2026-10-14` (both copies) |
| `Meta Ads/sib_capisweep_v4_2026-10-15.deluge.txt` | `sib_capisweep_v3_2026-10-14` |
| `Meta Ads/sib_wa_click_hook_v1.1_2026-10-15.deluge.txt` | `sib_wa_click_hook_v1_2026-10-14` |

## 1. Why now

Click capture works on real traffic. Three real SIB-04 clicks on 15 Oct (13:09, 13:19, 13:53), all on ad 120246969168420449 ("LLP Form 8 due 30 Oct 2026"):
- WA_Ad_Clicks 1123581000948400037 → lead 1123581000948418152 (Fatema), Matched.
- WA_Ad_Clicks 1123581000948396034 → lead 1123581000948408098, Matched.
- WA_Ad_Clicks 1123581000948395061 (…7655): Unmatched until the next 2-hourly match.

The two matched leads have CTWA_Click_ID and Meta_Ad_ID filled. They are not graded yet, and Meta_CAPI_Event is blank.

## 2. What changes

### Sender v3 (`sib_sendMetaCAPI` for Leads, `sib_sendMetaCAPI1` for Deals; same body, only the first line differs)

- **New WhatsApp branch.** It applies when the source is `Advt - WhatsApp`, the WhatsApp token is set, and the customer's phone has a click in WA_Ad_Clicks from the last 7 days. The phone is checked in this order: WhatsApp_Number, then Phone, then Mobile, using the last 10 digits.
- **The event goes to dataset 1442186757791533** (Graph v26.0, token `meta_wa_access_token`).
  - It uses `action_source: business_messaging` and `messaging_channel: whatsapp`.
  - `user_data` holds only `whatsapp_business_account_id` and `ctwa_clid`, with no email or phone.
  - Event names: ValidLead → **LeadSubmitted**, QualifiedLead → QualifiedLead, Committed → **InitiateCheckout**, Purchase → Purchase (value, INR).
- **Deals use the branch only for Committed and Purchase.** A Deal's QualifiedLead stays system_generated. The converted Lead has usually sent its own QualifiedLead already, and Meta does not dedupe business_messaging events.
- **How Meta's answer is handled:**

  | Meta's answer | What the function does |
  |---|---|
  | Accepted | Marks the stage |
  | Error (rejected) | Falls back to the unchanged v2 system_generated event on dataset 1242417817083521 |
  | Timeout or unreadable answer | Marks the stage and never resends it (a rare loss rather than a double count) |

- **No click, a failed lookup, or an empty token** → unchanged v2 behaviour.
- **Meta_CAPI_Event keeps the CRM name** (ValidLead, QualifiedLead, Committed, Purchase), so one rank guard covers both channels.
- **Facebook and Instagram sources:** no change. The only edit there is that event_time is taken once into a variable; the value is the same.

### Sweep v4 (`sib_capisweep`)

- **Same rule for leads.** `Advt - WhatsApp` leads with a click in the last 7 days go in one business_messaging POST per run: ValidLead → LeadSubmitted, QualifiedLead → QualifiedLead.
- **If Meta rejects that POST,** those leads join the normal system_generated POST in the same run. A timeout or unreadable answer is marked and not resent.
- **The cap of 20 now counts both lists together.**
- **A lead that appears twice in the 600 scanned leads is taken once.** Pages are read while leads change, so this can happen. It also applies to Facebook and Instagram leads, where Meta's event_id dedupe used to catch it.
- **Only leads that also have the normal match keys** (lead_id, email or phone) take the WhatsApp path, so a fallback is always possible.
- **Failed marks are logged** for WhatsApp leads.

### Hook v1.1 (`sib_wa_click_hook`): signature diagnostics only

Intake is unchanged and nothing is rejected. On a mismatch, `Signature_Check` (20-character field) now records the reason:

| Value | Meaning | Next step |
|---|---|---|
| `ok-trim` | The stored secret has a stray space or line break around it | Sanjeev re-pastes the secret cleanly |
| `mismatch n0 c1` | The body is plain ASCII and arrived unchanged, so the secret is wrong | Sanjeev re-copies the App secret of app 1445554577564805 |
| `mismatch n1 c1` | The body arrived unchanged but holds non-ASCII text (emoji, ₹). Either the secret is wrong, or Meta signs the `\u`-escaped form | Re-paste the secret first. If it still mismatches, hook v2 hashes the escaped form |
| `mismatch n? c0` | Zoho changed the body before the function saw it | The signature can't be enforced on this endpoint. Keep record-only; the secret URL and API key remain the gate |
| `cx` / `cu` | No Content-Length header, or Zoho's encoder is not UTF-8 | That part can't be read |

The secret is never logged or stored, only these flags.

## 3. Signature mismatch: diagnosis so far

1. All 3 real clicks show `mismatch`. The 14 Oct synthetic test signed with a dummy secret showed `ok`, and its body had `\u` and `\/` escapes. So the HMAC code is right, and Zoho passed that body unchanged.
2. That leaves two causes:
   - **(a) The stored secret** is not the app's current App secret: a copy slip, a stray space, the wrong app, or the secret was reset after pasting.
   - **(b) The real payloads carry non-ASCII text.** The referral includes the ad's own text, which likely has ₹ and emoji. Meta's docs say the signature is computed on the `\u`-escaped form of the payload. If the body arrives as raw UTF-8, or Zoho re-encodes it, the hashes differ.
3. Hook v1.1 tells (a) from (b) on the next click. Separately, Sanjeev can re-copy the App secret (Meta App Dashboard → App settings → Basic → App secret → Show) and paste it into `meta_wa_app_secret` with no spaces. I never see it.
4. Until a real click shows `ok`, the hook stays record-only, and the lookup does not filter on Signature_Check. After `ok`: hook v2 enforces the check (403 on mismatch) and the lookup uses only `ok` clicks. Without that, anyone holding the URL and key could plant click rows.

## 4. Review

An independent review of the first draft blocked it on three points, all fixed in these drafts:
- A. The lookup call was not guarded. A lookup error would have killed the whole sweep run, Facebook and Instagram events included.
- B. A timeout fell back to system_generated, which could report the same stage twice.
- C. A lead could appear twice across the scanned pages, which would send it twice.

Also fixed:
- The WhatsApp token is read before any lookup, so emptying it switches the branch off.
- The Deal QualifiedLead double count.
- A WhatsApp lead with no fallback keys could have jammed the batch.
- The hook's non-ASCII test now ignores tabs and line breaks, and checks that the encoder is UTF-8.

Not changed (older behaviour, logged):
- Results of `updateRecord` in the sender are logged but not retried.
- Lead and Deal guards remain separate.

## 5. Deploy steps (after OK; one function at a time)

| # | Function | Check |
|---|---|---|
| D1 | `sib_wa_click_hook` → v1.1 (optional, diagnostic) | The next real click shows the new Signature_Check value |
| D2 | `sib_sendMetaCAPI1` (Deals, id 1123581000911677606) → v3 | Save OK. Run on deal P101453 (1123581000947712654): "Purchase not above last sent Purchase - skipped" |
| D3 | `sib_sendMetaCAPI` (Leads, id 1123581000911606421) → v3 | Save OK. Run on lead 1123581000946345208: "ValidLead not above last sent ValidLead - skipped" |
| D4 | `sib_capisweep` (1123581000915255380) → v4 | Save OK. Manual run: "scanning 600 …", no errors |

**Live test:** the first of the three clicked leads to be graded Valid within 7 days of its click. The sweep log should show `CAPI sweep WhatsApp (1) -> {"events_received":1,…}`, the lead should show Meta_CAPI_Event = ValidLead, and Events Manager → dataset 1442186757791533 should show LeadSubmitted.

**Stop-loss:**
- If the first event is rejected, it falls back automatically, so nothing is lost. I read the error and fix it.
- If Events Manager shows duplicate LeadSubmitted or Purchase events for one record, restore the previous revisions.

**Rollback:** IDE → Revisions → restore 14 Oct v2 (both sender copies), v3 (sweep) and v1 (hook). Or paste the 14 Oct files and save.

## 6. Later (separate changes)

- **The existing system_generated paths use Graph v21.0,** which Meta removes on **21 Jan 2027** (Graph API v26 release note, 29 Jul 2026). Move them to v26.0 well before then, as a one-variable change.
- **Hook v2 and lookup v2** (signature enforcement and filter) after a real `ok`.
