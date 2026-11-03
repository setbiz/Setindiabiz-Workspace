# Resume prompt — W6 live + relaunch follow-ups (15 Oct 2026, 14:55 IST)

Paste this into a new session in the "Meta Ads - Optimisation" project.

---

You are continuing the SetIndiaBiz Meta Ads work for Sanjeev. Read these project docs first:
- `Meta Ads/W6_Click_Attributed_CAPI_Draft_2026-10-15.md`: what W6 changes, the review, the test, rollback and the signature diagnosis.
- `Meta Ads/Change_Log_2026-10-15_W6-Deployed.md`: what was deployed and what to watch.
- `Meta Ads/Change_Log_2026-10-15_IND1-Relaunch-SIB-02-Draft.md`: the Incorporation relaunch and the Trademark SIB-02 draft.
- `Meta Ads/CTWA_Click_Capture_Resume_Prompt_2026-10-15.md`: IDs, and the click-capture background.

## Where things stand

### 1. W6 is LIVE (deployed 14:42–14:49)
Record: `Meta Ads/Change_Log_2026-10-15_W6-Deployed.md`. Live code:
- `sib_sendMetaCAPI_v3_2026-10-15` (both copies)
- `sib_capisweep_v4_2026-10-15`
- `sib_wa_click_hook_v1.1_2026-10-15`

Guard tests passed and the sweep run showed no errors.

To watch:
- The Signature_Check value on the first click after 14:42 (meaning table in the W6 doc §2).
- The first business_messaging send, on the first clicked lead graded Valid within 7 days.
- Events Manager, dataset 1442186757791533: no duplicates.

### 2. Click capture is busy
At least 13 real SIB-04 clicks by 14:34, across 4 CTWA ads. All before 14:42 show "mismatch" (old hook). The 2-hourly matcher links them to leads.

Already matched:
- 1123581000948418152 (Fatema)
- 1123581000948408098

### 3. Incorporation #IND1
Ad-2 was switched on by Sanjeev at 13:48 and was PENDING_REVIEW. Check that it passed review and is delivering.
Stop-loss: pause if 3-day CPL is above ₹440, or after 2 spend-days with 0 CRM leads.

### 4. Trademark SIB-02
Draft built (Form ad, approved copy). Sanjeev publishes it from his own Chrome.
Stop-loss after publish: pause if 3-day CPL is above ₹340, or after 2 spend-days with 0 CRM leads.

### 5. Open items for Sanjeev
- Funds: ₹25,000 lasts until about Saturday. Prepaid account; funding is human-only.
- Reconnect the Meta connector with `pages_manage_ads`. The Lead Ads ToS read fails without it.
- Optional: re-copy the App secret of app 1445554577564805 into `meta_wa_app_secret`, with no spaces.
- IPR Zobot on +91 95994 81905 (Tiya project) before any SIB-02 CTWA ad set.

### 6. When the first IND1 / SIB-02 form leads arrive
Check the owner and Product Name / Category. Add a `ppc_form_tidy` CONFIG block only if Product Cat comes in blank.

## Hard rules (unchanged)

**Meta**
- Never activate or publish a Meta campaign, and never call `ads_activate_entity`.
- Never move money or top up.
- Any Meta change needs explicit approval. One variable at a time, with before/after screenshots and a logged stop-loss.
- Ad copy needs Sanjeev's OK on the exact text.

**Zoho CRM**
- Show the code or diff before saving any production function, template or workflow. Ask before each CRM write.
- CRM edits made through the connector pass `trigger: []`.
- Never delete CRM records with the connector.
- Don't edit the older LeadChain chains.

**Secrets**
- Never read, print or handle secrets or tokens: `meta_wa_verify_token`, `meta_wa_app_secret`, `meta_wa_access_token`, `meta_capi_access_token`.
- The webhook URL is a credential; never write it into docs.

**Off limits**
- Never touch Zoho Social.
- The SalesIQ project owns the bot, plugs, Desk rules and `RM_Lead_Ticket`.

**Browser**
- If the browser safety check refuses a step, hand that step to Sanjeev.
