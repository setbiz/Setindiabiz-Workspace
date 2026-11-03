
## 2026-10-27 (Tue) — run ~09:50 IST (CRM-only: Meta Ads connector needs reconnecting)

**Meta read NOT done:** the Meta Ads connector's sign-in has lapsed, so delivery, spend, `ads_get_errors`, funding/activity log, targeting read-back and placement spend could not be pulled. Supermetrics fallback also failed (trial expired 7 Jul). No cost-per-valid figures today.
**Delivery inferred from CRM:** paid leads resumed 26 Oct 17:21 after 3 dark days (22 leads 26 Oct, 8 by 09:35 today) → account was funded on 26 Oct afternoon (amount unknown). **SIB-05 still live:** 2 new leads today (08:58, 09:35); it was not paused.
**Source guard:** 0 leads with Meta_Campaign set and wrong Lead_Source (541 leads, 14–27 Oct). 1 paid lead with no Meta_Campaign: …952869002 (Advt - Instagram, 26 Oct 23:25). **Lead_Channel empty: 25 (was 12)** — every #IND1/SIB-02 lead since delivery resumed (26 Oct 17, 27 Oct 5) + 3 old. LeadChain fix still not landed.

| Campaign × path | Yday n | junk | valid | unw | 7d (20–26) n | junk | valid | unw | Matured (17–23) n | junk | valid | unw |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SIB-04 WhatsApp | 2 | 0% | 0% | 100% | 13 | 8% | 38% | 54% | 20 | 20% | 40% | 30% |
| SIB-04 Form | 3 | 0% | 0% | 100% | 26 | 0% | 50% | 46% | 37 | 5% | 46% | 27% |
| #IND1 Form | 9 | 0% | 0% | 100% | 67 | 4% | 46% | 36% | 114 | 4% | 52% | 28% |
| SIB-02 Form (orig + Copy) | 8 | 0% | 0% | 100% | 58 | 2% | 55% | 41% | 79 | 1% | 66% | 30% |
| SIB-05 Form | 0 (2 today) | — | — | — | 4 | 0% | 50% | 50% | 4 | 0% | 50% | 50% |

- Top Why_Disqualified matured: SIB-04 WA Inquired by Mistake 4, Duplicate 1, No Product Offering 1. SIB-04 Form Other CA 3, Pricing 1, Inquired by Mistake 1. #IND1 Avoiding Call 7, Other CA 5, Not Interested 4. SIB-02 Avoiding Call 3, Other CA 3.
- **Trend: improving on matured, 7d dipped from new unworked leads.** Matured window is now Directors-only for SIB-04: WA junk 55% → 20%, valid 15% → 40%; Form valid 42% → 46%. SIB-02 matured 59% → 66%, #IND1 53% → 52%. All matured valid ≥ 40%; junk ≤ 5% except SIB-04 WA 20% (4 "Inquired by Mistake", one known RM mislabel). 7d valid dips (#IND1 52 → 46, SIB-02 58 → 55) are the 26 Oct leads not yet worked; 7d junk ≤ 8%.
- **Directors SIB-04, 17–26 Oct:** 64 leads, 6 junk (9%), 25 valid, 23 unworked. Worked 41: 17 Valid, 6 Proposal Sent, 1 Negotiation, 2 Postponed, 15 Lost. Junk-type rejects 6/41 = 15% (≤ 25%) → KEEP holds.
- **SIB-05:** 6 CRM leads (22 Oct 1, 23 Oct 3, 27 Oct 2), 2 Valid, 0 junk, 2 still Establishing Contact since 23 Oct. Day-7 country split due today can't run (no Meta read; only ~2.5 spend days).
**Guardrail audit: NOT RUN** (no Meta read). Last fresh read 26 Oct: Directors Form PASS; Directors WA, #IND1 FLAG `frequently_in`; SIB-02 Copy FLAG `geo: 1` + `frequently_in`; SIB-05 ×3 PASS; no AN/Marketplace/Threads spend.
**WhatsApp signals (26 Oct):** 2 Advt-WhatsApp leads, both WhatsApp-form openers (Pvt Ltd; FY 2025-26 + earlier, FY 2025-26 only), 1 prefixed fb.me, both correctly Advt-sourced, both tagged Ad code ACR. 0 coded, 0 Indian script, 0 Social-WhatsApp. Both carry a Duplicate Record note. Both chats missed (21:16 and 23:12; no operator on the bot forward).
**Speed:** **116** paid leads > 24 h unworked (was 137): SIB-04 47, #IND1 41, SIB-02 26, SIB-05 2. Owners: [customer name redacted] Lost Records 14, Sudip Manna 14, Praveen Singh 11, Krishna Gupta 9, Dipanshu Saini 9, Anish Singh 8, Tarun Kumar 8, Saksham Pathak 7, Amit Kumar 3 6, Anshu Yadav 6.
**Recommendations (not executed):**
1. Reconnect the Meta Ads connector so tomorrow's run can read funding, spend, cost per valid and the guardrail audit. Confirm: full Meta read at the 28 Oct run.
2. SIB-05 is back on at ~₹8.8k per valid vs ₹161–1,277 on India campaigns; if funds are short, pause it first. Confirm: India ad sets get full-day spend and no `account_spend_limit_reached` on 28 Oct.
