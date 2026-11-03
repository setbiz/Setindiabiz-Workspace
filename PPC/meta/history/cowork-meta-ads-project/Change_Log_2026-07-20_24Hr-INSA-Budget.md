# Change Log — 20 Jul 2026 (Monday)
## C1 24Hr INSA Company INC — daily budget +20%

**Approved by:** Sanjeev, 20 Jul 2026 ("Go ahead with changes")
**Executed by:** Meta Ads optimisation operator, 20 Jul 2026
**Entity:** Ad set `120240912969640449` — "C1 - 24Hr INSA Company INC"
**Campaign:** #IND 1 — Incorporation (`120240912969660449`)
**Change type:** Budget, ad-set level (+20%, inside the ±10–20%/day guardrail)
**Variables changed:** ONE (daily budget only)

---

### Before → After (API-verified)

| Field | Before | After |
|---|---|---|
| daily_budget | ₹1,800.00 INR | **₹2,160.00 INR** |
| lifetime_budget | ₹0.00 (n/a) | ₹0.00 (n/a) |
| status | ACTIVE | ACTIVE |
| effective_status | ACTIVE | ACTIVE |
| optimization_goal | OFFSITE_CONVERSIONS | OFFSITE_CONVERSIONS (unchanged) |
| bid_strategy | Highest volume | Highest volume (unchanged) |
| updated_time | 9 Jul 2026 | 20 Jul 2026 |
| child ad `120240912969650449` | ACTIVE | ACTIVE (unaffected) |

---

### ⚠️ Incident during execution — force-pause and recovery

The connector's `ads_update_entity` call returned `status_forced_to_paused: true` and set the
ad set to PAUSED as an undocumented side effect of the budget edit. This was **not** part of the
approved change.

- Detected immediately in the tool response.
- Reactivated via `ads_activate_entity` in the same minute.
- Post-change read-back confirms `status: ACTIVE`, `effective_status: ACTIVE`, child ad ACTIVE.
- **Estimated delivery interruption: under one minute.** No meaningful spend or lead loss expected.

**Operational lesson (carry forward):** every future budget edit through this connector must be
followed by an immediate status read-back, and reactivated if force-paused. Never treat a
`success: true` budget response as sufficient — check `status_forced_to_paused`.

---

### Rationale

3-day window 17–19 Jul 2026:

- CPL ₹208.52 (16 CRM leads on ₹3,336.33) — well under the ₹350 revert threshold
- Valid% 62.5% (10/16) — well over the 40% confirming bar
- INSA combined pacing ₹2,011.69/day vs the ~₹4.3k/day absorption target → staging headroom remains

This is the next +20% staging increment under the Phase-1 plan (9 Jul 2026).

---

### Stop-loss (logged, review Thu 23 Jul 2026)

| Trigger | Action |
|---|---|
| 3-day CPL > ₹350 | REVERT to ₹1,800/day |
| 3-day valid% < 30% | REVERT to ₹1,800/day |
| Spend fails to rise toward ~₹2,160/day within 3 days | Investigate delivery/learning, do not stack another increment |

**Confirming metric:** by Thu 23 Jul 2026, 3-day CPL < ₹350 **and** valid% ≥ 40%, with daily spend
tracking toward ₹2,160. If both hold and combined INSA daily rate is still under ~₹4.3k/day, the
next +20% increment (₹2,160 → ₹2,592/day) becomes eligible for approval.

---

### Not executed (deliberately held)

1. **C1 Daytime INSA increment — HELD.** Valid% 28.6% (4/14, 17–19 Jul) breaches the 30% floor.
   Recheck 23 Jul. Separate open question: ₹51.7k of the ₹190,500 lifetime budget remains with
   11 days to the 30 Jul end date (needs ~₹4.7k/day, running ~₹0.9k) — extend or accept the shortfall.
2. **CCFS-3 creative unpause — NOT DONE.** Ad-level changes are blocked by the leadgen ToS API error
   (1815089) and must go through the browser. Also would have been a second variable in one day.
   Compliance-relevant: live CCFS copy still cites "15 July" while the scheme runs to 31 Aug 2026
   per MCA General Circular 03/2026.
3. **TMF-SA budget ₹150,000 vs approved ₹130,000** — discrepancy flagged, awaiting Sanjeev's confirmation.
4. **#IND5 DPIIT full-campaign pause** — flagged, awaiting confirmation that it was intentional.

No money moved. No payment actions taken. No CRM writes.
