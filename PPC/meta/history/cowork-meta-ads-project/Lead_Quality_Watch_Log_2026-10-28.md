
## 2026-10-28 (Wed) — run 09:42 IST (CRM-only: Meta Ads connector still needs reconnecting, 2nd day)

**Meta read NOT done:** Meta Ads connector sign-in still lapsed → no spend, `ads_get_errors`, funding/activity log, targeting read-back or placement spend. No cost-per-valid today.
**DELIVERY LIKELY STOPPED (inferred from CRM):** last paid lead 27 Oct 17:59; **0 paid leads since (≈16 h)** vs 8 by 09:35 yesterday. 27 Oct total 26 leads (full days run 39–45). Most likely the 26 Oct top-up ran out ~18:00 on 27 Oct (`account_spend_limit_reached` pattern of 18 and 24 Oct); can't confirm without Meta. Top-up is human-only.
**Source guard:** 0 leads with Meta_Campaign set and wrong Lead_Source (559 leads, 14–28 Oct). 0 paid leads without Meta_Campaign (…952869002 now stamped). **Lead_Channel empty: 11 (was 25)** — 27 Oct only 3 of 22 #IND1/SIB-02 (#IND1 1, SIB-02 2); 26 Oct 4; 22 Oct 4. Mostly backfilled; LeadChain still misses some.

| Campaign × path | Yday n | junk | valid | unw | 7d (21–27) n | junk | valid | unw | Matured (18–24) n | junk | valid | unw |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SIB-04 WhatsApp | 1 | 0% | 0% | 100% | 13 | 8% | 38% | 54% | 15 | 13% | 40% | 33% |
| SIB-04 Form | 1 | 0% | 100% | 0% | 19 | 0% | 47% | 53% | 34 | 3% | 50% | 29% |
| #IND1 Form | 15 | 0% | 53% | 47% | 73 | 4% | 51% | 36% | 95 | 5% | 52% | 27% |
| SIB-02 Form (orig + Copy) | 7 | 0% | 71% | 29% | 53 | 2% | 68% | 32% | 74 | 1% | 68% | 27% |
| SIB-05 Form | 2 | 0% | 50% | 50% | 6 | 0% | 50% | 50% | 4 | 0% | 50% | 50% |

- Top Why_Disqualified matured: SIB-04 WA Inquired by Mistake 2, Duplicate 1, Pricing 1. SIB-04 Form Avoiding Call 3, Other CA 2. #IND1 Avoiding Call 5, Other CA 5, Inquired by Mistake 4. SIB-02 Avoiding Call 3, Other CA 3.
- **Trend: improving.** 7d valid: SIB-02 55% → 68%, #IND1 46% → 51%, SIB-04 Form 50% → 47%, WA 38% flat. Matured: SIB-04 WA junk 20% → 13%, Form valid 46% → 50%, SIB-02 66% → 68%, #IND1 52% flat. Every campaign junk ≤ 15% and matured valid ≥ 40%.
- **Directors SIB-04, 17–27 Oct:** 63 leads, 6 junk (10%), 28 valid (44%), 20 unworked. Worked 43: 18 Valid, 6 Proposal Sent, 1 Negotiation, 2 Postponed, 16 Lost. Junk-type rejects 6/43 = 14% (≤ 25%) → KEEP holds.
- **SIB-05:** 6 CRM leads, 3 Valid, 0 junk, 3 Establishing Contact (2 since 23 Oct). Country split still not possible (no Meta read).
**Guardrail audit: NOT RUN** (no Meta read, 2nd day). Last fresh read 26 Oct: Directors Form PASS; Directors WA, #IND1 FLAG `frequently_in`; SIB-02 Copy FLAG `geo: 1` + `frequently_in`; SIB-05 ×3 PASS.
**WhatsApp signals (27 Oct):** 1 Advt-WhatsApp lead (…953231011, 17:59): WhatsApp-form opener (OPC, FY 2025-26 only), prefixed instagram.com/p/, correctly Advt-sourced, Ad code ACR. 0 coded, 0 Indian script, 0 Social-WhatsApp. Duplicate Record note. SYNC GAP (SalesIQ #61924 not ended); RM called twice, no answer.
**Speed:** **119** paid leads > 24 h unworked (was 116): SIB-04 46, #IND1 44, SIB-02 26, SIB-05 3. Owners: Sudip Manna 19, [customer name redacted] Lost Records 14, Praveen Singh 11, Dipanshu Saini 9, Krishna Gupta 8, Saksham Pathak 8, Tarun Kumar 8, Anish Singh 7, Anshu Yadav 6, Rama Dwivedi 6.
**Recommendations (not executed):**
1. Check the Meta balance now and top up if dry (≈ ₹19.4k for 2 days with SIB-05 paused first, ≈ ₹28.8k with it on); reconnect the Meta Ads connector. Confirm: paid CRM leads resume today and a full Meta read at the 29 Oct run.
2. TLs to clear the 119-lead backlog (Sudip Manna 19 first) and the 2 SIB-05 leads untouched since 23 Oct (most expensive leads in the account). Confirm: unworked > 24 h ≤ 100 tomorrow.
