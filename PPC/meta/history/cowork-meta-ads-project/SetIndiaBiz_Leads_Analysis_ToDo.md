# SetIndiaBiz — Leads Analysis To-Do / Backlog

**Generated:** 27 Jun 2026 · **Segment:** PPC Meta Insta · **Source of truth:** Zoho CRM × Meta Ads

Prioritised P0 → P3. Check items off as completed. Items tagged **(human)** must be done by a person per the guardrails (never automate money/payment/campaign mutations).

---

## P0 — Urgent (today)

- [ ] **Restart Meta delivery.** Campaigns are dark since 25 Jun (~15:00): ₹0 spend, 0 impressions, 0 new CRM leads on 26 & 27 Jun. Check campaign status, billing/payment method, and budget caps in Ads Manager. Each dark day ≈ ₹17k of pipeline not generated. **(human)**
- [ ] **Work the 42-lead exception queue** (see `SetIndiaBiz_SpeedToLead_Exceptions_2026-06-27.xlsx`): 6 untriaged + 28 establishing-contact + 8 postponed. Call oldest-first; 3 attempts (call + WhatsApp).
- [ ] **Confirm whether the 25-Jun stop was a pause, billing failure, or policy block** — root-cause so it doesn't recur.

## P1 — Instrumentation (this week — unblocks real speed-to-lead)

- [ ] **Capture first-contact.** Today completed calls attach to Deals/Contacts only (`Who_Id` blank on new leads) — log calls against the Lead, or stamp a `First_Call_Time` field. Without this, lead→first-call latency cannot be measured.
- [ ] **Populate `Lead_Assigned_on`** (empty on every lead) to measure routing lag.
- [ ] **Define the speed-to-lead SLA** (recommend first call within 15 min for paid-social leads) + a daily breach report.
- [ ] **Fix LeadChain attribution** — write campaign/adset/ad IDs to CRM so cost-per-valid can be computed per campaign (today only `Social_Lead_ID` arrives).
- [ ] **Enforce fill SLAs** on `Why_Disqualified` and Deal `Lost_Reasons`/`Reason_For_Loss__s` (Deal lost-reason ~0% filled).

## P2 — Recurring analyses

- [ ] **Daily scorecard** (cost per valid / progressed / committed / won) — automate the morning run.
- [ ] **Speed-to-lead exception list** — run daily once delivery resumes.
- [ ] **Loss-bucket diagnosis vs baseline** — weekly. Watch "Avoiding Call" (44% of all losses = the #1 leak).
- [ ] **Duplicate-lead audit** — dedupe rule (e.g., Suman Jha entered twice; Jeetendra Mishra twice in the 24–25 Jun cohort alone).
- [ ] **Junk / targeting audit** — quantify foreign numbers (+1), bots, job seekers; tie to specific creative/audience before any targeting change.
- [ ] **Owner/RM performance** — valid% → progressed% → won% by owner; coach low responders (exception load is concentrated in a few owners).
- [ ] **Compliance review of live ad creative** — every claim defensible under Companies Act 2013, LLP Act 2008, CGST Act 2017; no false guarantees, no fabricated timelines, accurate MCA/ROC fee references.

## P3 — Deeper / strategic

- [ ] **Campaign-level reallocation** (after attribution live) — shift budget from #IND6 Virtual CFO+GST (₹1,295 CPL) toward #IND3 Trademark / #IND5 DPIIT.
- [ ] **Cohort maturation analysis** (lead→deal lag) to set realistic cost-per-won targets vs the immature 30-day snapshot.
- [ ] **TL Quality field decision** — `Mkt_Leat_Quality` is 96% blank; enforce or retire it.
- [ ] **Timing analysis** — hour-of-day / day-of-week of lead arrival vs contact-success rate.
- [ ] **Geography/serviceability** — review "Non Serving Territory" + "Off Location" leads for excludable areas.

---

*Change discipline: any Meta mutation (budget, audience, creative, status, bid) requires explicit approval, one variable at a time, with before/after screenshot and a logged stop-loss. Never move money — always the human.*
