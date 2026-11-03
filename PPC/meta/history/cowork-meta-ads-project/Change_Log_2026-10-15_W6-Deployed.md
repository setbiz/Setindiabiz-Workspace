# Change log — 15 Oct 2026 — W6 live: WhatsApp-click CAPI events + signature diagnostics

**Approval:** Sanjeev, 13:53 ("Yes", prepare W6), then the AskUserQuestion answer "Deploy all four (Recommended)".
**Plan and review:** `Meta Ads/W6_Click_Attributed_CAPI_Draft_2026-10-15.md`.

**Code (live):**
- `Meta Ads/sib_sendMetaCAPI_v3_2026-10-15.deluge.txt` (both copies)
- `Meta Ads/sib_capisweep_v4_2026-10-15.deluge.txt`
- `Meta Ads/sib_wa_click_hook_v1.1_2026-10-15.deluge.txt`

**Previous versions (rollback):**
- `sib_sendMetaCAPI_v2_2026-10-14`
- `sib_capisweep_v3_2026-10-14`
- `sib_wa_click_hook_v1_2026-10-14`

## How each function was changed

1. Before editing, the live code was compared with the project file:
   - Hook: v1, except for IDE formatting.
   - Deals sender: v2.
   - Leads sender: v2 (SHA-256 match).
   - Sweep: v3 (SHA-256 match).
2. The new code was set through the editor's CodeMirror. A SHA-256 check confirmed the buffer equals the file.
3. Saved in the IDE. The IDE then showed "Last modified by Sanjeev Kumar just now", with Save greyed out and no errors.

## Changes

| # | Time (IST) | Function | Change | Verified |
|---|---|---|---|---|
| D1 | ~14:42 | `sib_wa_click_hook` (1123581000947966992) → **v1.1** | Signature diagnostics only. On a mismatch, Signature_Check records `ok-trim` or `mismatch n? c?` (see the W6 doc §2). Intake is unchanged and nothing is rejected. Diagnostic variables are named `nf` / `cf`, so `c` (the createRecord result) is not reused. | Saved. Proof comes with the next real click |
| D2 | ~14:45 | `sib_sendMetaCAPI1` (Deals copy, "SIB Send Meta CAPI Deal", 1123581000911677606) → **v3** | WhatsApp click branch (business_messaging) for Committed and Purchase. Fallback to system_generated. Timeout or unreadable answer → mark, never resend. | Run on Deals / P101453 (1123581000947712654): "Purchase not above last sent Purchase - skipped". No POST |
| D3 | ~14:47 | `sib_sendMetaCAPI` (Leads copy, "SIB Send Meta CAP Lead", 1123581000911606421) → **v3** | Same body; only the first line differs. | Run on Leads / 1123581000946345208 (Advt - WhatsApp, Valid Lead, already ValidLead): "ValidLead not above last sent ValidLead - skipped" |
| D4 | ~14:49 | `sib_capisweep` (1123581000915255380) → **v4** | Same WhatsApp branch for lead events, plus guarded lookup, duplicate-page skip, and a shared cap of 20. | Manual run: "scanning 600 recently-modified leads", "0 events to send", no errors |

## Live state at 14:51

- **Click capture is busy.** At least 10 new real clicks between 13:53 and 14:34, across 4 SIB-04 CTWA ads:

  | Ad ID | Clicks |
  |---|---|
  | 120246969168420449 | 3 |
  | 120246969045870449 | 3 |
  | 120246969544800449 | 2 |
  | 120246968790550449 | 2 |

  All of them came in before D1, so they show the old "mismatch". The next click shows the v1.1 diagnostic.
- **No WhatsApp business_messaging event has been sent yet.** The clicked leads are not graded Valid yet.
- **First live test:** the first clicked lead an RM grades Valid within 7 days. The sweep log should show `CAPI sweep WhatsApp (1) -> {"events_received":1…}`, the lead should show `Meta_CAPI_Event` = ValidLead, and dataset 1442186757791533 should show LeadSubmitted.

## Watch

1. **Next click's Signature_Check.**

   | Value | Next step |
   |---|---|
   | `ok-trim` | Re-paste the secret |
   | `mismatch n0 c1` | The secret is wrong; Sanjeev re-copies it |
   | `mismatch n1 c1` | Re-paste the secret first, then hook v2 if needed |
   | `c0` | Keep record-only |

2. **First WhatsApp send.**
   - If it is rejected, the event falls back automatically. Read the Meta error and fix it.
   - If it shows "unconfirmed", check Events Manager.
3. **Events Manager, dataset 1442186757791533.** There should be no duplicates per record.

## Rollback

- In the IDE → Revisions, restore the 14 Oct version of each function.
- Or paste the 14 Oct project files and save.
- Order: sweep, then Leads sender, then Deals sender, then the hook.

## Later

- **The system_generated paths still use Graph v21.0,** which Meta removes on 21 Jan 2027 (Graph API v26 release note, 29 Jul 2026). Move them to v26.0 as a separate change.
- **Hook v2 and lookup v2** after a real `ok`: enforce the signature, and use only `ok` clicks.

## 15:31 check (scheduled re-check)

**Signature diagnostic.** The first 3 clicks after D1 (14:53, 15:21, 15:25) all show **`mismatch n0 cx`**:
- **n0:** the body is plain ASCII. Meta escapes non-ASCII as `\u…`, so the unicode theory is ruled out.
- **cx:** Meta sends no Content-Length header.
- **No `ok-trim`:** the secret has no stray spaces.

Zoho passed the body unchanged in the 14 Oct test. So the stored `meta_wa_app_secret` is almost certainly not the current App secret of app 1445554577564805.

**Fix (Sanjeev):**
1. Meta App Dashboard → Setindiabiz WA Signals → App settings → Basic → App secret → Show.
2. Paste it into Zoho Setup → Developer Hub → Variables → `meta_wa_app_secret`.

The next click should then show `ok`.

**Delivery today (Meta connector, at 15:31):**

| Campaign | Spend | Impressions |
|---|---|---|
| SIB-04 | ₹2,024.74 | 13,528 |
| #IND1 | ₹380.67 | 870 |
| SIB-02 Trademark | — | — |

- #IND1 is delivering.
- SIB-02 Trademark is ACTIVE (published by Sanjeev), with no spend yet.

**Leads:**
- **Clicks match leads one to one.** 14 `Advt - WhatsApp` leads today against 15 clicks; each lead was created about 2 s after its click. The clicks after 13:45 wait for the 15:45 matcher.
- **No click-linked send yet.** No WhatsApp lead is graded Valid yet: 3 are "Still Evaluating" and 2 are Lost, including Fatema.
- **First #IND1 form lead** (15:25): 1123581000948383116, owner Dwivedi. **Product Name and Product Category are blank**, so `ppc_form_tidy` needs a CONFIG block for the Incorporation V2 form. Not done: it needs approval.
- **Duplicate pairs from LG11.**
  - Ad 120246969544800449 is the SIB-04 LG11 Form ad. It also produces WhatsApp clicks, from the form's WhatsApp button.
  - Two customers became two leads each, seconds apart, with different owners:
    - [phone redacted]: FB lead 1123581000948366178 (Gupta) + WA lead 1123581000948323144 (Manna).
    - [phone redacted]: FB lead 1123581000948317153 (Sehrawat) + WA lead 1123581000948418238 (Singh).
  - These are for the duplicate detector / SalesIQ project to handle.
