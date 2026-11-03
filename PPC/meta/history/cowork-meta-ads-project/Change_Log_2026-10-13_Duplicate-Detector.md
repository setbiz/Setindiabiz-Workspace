# Change log — 13 Oct 2026 — "Detect Duplicate Lead": paid leads keep their owner

**Approval:** Sanjeev, ~17:15 IST. The code diff was shown in chat first. Answer to "When a paid lead turns out to be a duplicate, who should own it?": **"Keep assigned owner"**.

## Findings (read-only, before the change)

- Function `detect_duplicate_lead(String leadid)` (id 1123581000902971660, last changed 31 May 2026). Two Leads rules call it:
  - **"Detect Duplicate Lead on Create"** (1123581000902971675), on Create.
  - **"Detect Duplicate Lead"** (1123581000902971669), a field-update rule that repeats when Refresh, Phone, Phone_2, Email or Secondary_Email changes.
- Logic: a COQL search (connection `contact_to_lead`) for any other Lead or any Contact with the same Email or Phone. If found, it sets Duplicate_Status "Yes", sets **Owner = admin account (Sanjeev Kumar, 1123581000006825001)** and adds the note "Duplicate Record(s) Found". This applied to every lead source.
- Paid leads hit since 15 Sep (Duplicate_Status Yes, Advt-*): **6**. All were later moved off the admin account by hand:
  - JAIHIND / Kandukuri Rao 947088110 (13 Oct 16:31; the WhatsApp plug's claim re-ran LG-11 → Praveen Singh);
  - Hafeez 946586197;
  - Pcs Rahul 940432315;
  - Sudarshan Kumar Sharma 940500026;
  - Gopal Gargav 939768120;
  - Swapnil Duddalwar 937910012.
- Still on the admin account: **Virendra Sharma 946567286** (Advt - Facebook, SIB-04, returning customer). On 12 Oct Sanjeev chose not to reassign it, so it is left as is.
- Since 9 Oct, the admin account also holds 9 non-paid leads (Self - Cold Call ×8, Direct ×1). These are unchanged by this fix.

## Change

| # | Time (IST) | Item | Change | Verified |
|---|---|---|---|---|
| D1 | ~17:17 | `detect_duplicate_lead` → **v2** (`Meta Ads/detect_duplicate_lead_v2_2026-10-13.deluge.txt`; v1 kept as `detect_duplicate_lead_v1_2026-05-31.deluge.txt`) | New: `isPaid = Lead_Source startsWith "Advt - "`. For a **paid** duplicate: Duplicate_Status "Yes" and **no Owner change**. The note reads "Paid lead (<source>): kept with its assigned owner. It matches existing record(s) below. Check with the owner of those records before calling. If you merge, keep THIS lead as the master so the ad source stays:" followed by the links. **Non-paid** leads behave exactly as before (moved to the admin account, same note). The search, both rules and the "No" branch are unchanged. Commit message "v2 13 Oct: paid (Advt - ...) duplicates keep assigned owner; flag + note only". | Editor: saved, 0 errors, "Last modified … just now". The CodeMirror value equalled the v2 file before save (2,540 chars). |
| D2 | 17:19 | Test run | Ran on paid duplicate **1123581000947088110** (Advt - WhatsApp, owner Praveen Singh, matches lead 946489676). Status Success, 8.9 s. | Read-back: **Owner still Praveen Singh** (…005632013); Duplicate_Status Yes; new note at 17:19:14 with the paid-lead text and the matching link. Under v1 this run would have moved the lead to the admin account. |

## Notes

- **WhatsApp chats:** the SalesIQ lead is created as "Self - Web Chat", so the create-time check still treats it as non-paid and may park it on the admin account. The A03 plug then claims it as Advt - WhatsApp and re-runs the LG-11 rule, which gives it an owner, as happened with JAIHIND. If the plug matches an older lead or contact instead of claiming, the new chat lead stays on the admin account as a plain duplicate, and the customer stays with the existing record's owner.
- Merging: the note asks reps to keep the paid lead as master. On 11 Oct (R110), a merge into a chat lead dropped the ad source.
- Rollback: Functions › Detect Duplicate Lead › Revisions → the 31 May version, or paste v1 and Save.
