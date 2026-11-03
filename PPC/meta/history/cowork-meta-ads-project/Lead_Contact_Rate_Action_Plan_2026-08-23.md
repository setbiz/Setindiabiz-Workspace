# Meta Lead Form → Contact Rate: Diagnosis & Action Plan
**SetIndiaBiz · 23 August 2026 · prepared for Sanjeev**

Data basis: 421 paid-Meta leads created 9–20 Aug 2026 (`Lead_Source` = 'Advt - Facebook' + 'Advt - Instagram'), and all 286 Zoho Call records org-wide for 9–23 Aug 2026.

---

## 1. What the data actually says

| Lead_Status (n=421) | Count | % |
|---|---:|---:|
| Lost | 156 | 37.1% |
| Valid Lead | 94 | 22.3% |
| **Establishing Contact (never advanced)** | **91** | **21.6%** |
| Proposal Sent | 57 | 13.5% |
| Postponed | 21 | 5.0% |
| Negotiation / Payment Pending | 2 | 0.5% |

| Why_Disqualified (of 156 Lost) | Count | % of losses |
|---|---:|---:|
| **Avoiding Call** | **71** | **45.5%** |
| Other CA | 26 | 16.7% |
| Not Interested | 18 | 11.5% |
| Inquired by Mistake | 9 | 5.8% |
| Language Issue | 7 | 4.5% |
| Wrong Info | 7 | 4.5% |
| No Product Offering | 6 | 3.8% |
| Plan Drop / Pricing | 8 | 5.2% |
| Off Location / Not Eligible | 4 | 2.6% |

**Never reached = 71 "Avoiding Call" + 85 stuck ≈ 37–38% of every lead bought.** Add "Other CA" and "Postponed" and you arrive at the ~50% you described.

The 85 leads still sitting in *Establishing Contact* are a **median 8.8 days old** and **none is younger than 3.8 days**. They are not in progress. They are abandoned.

### The finding that changes the conversation

Zoho holds **286 call records for the entire organisation across 15 days**.

- Only **33 of the 421 leads (7.8%)** have any logged call at all.
- **175 of 286 (61%)** are `Overdue` — scheduled follow-up calls that were never made or never closed.
- Of the 90 `Completed` calls: **median duration 12 seconds**, 53% are ≤15 seconds, 24 are 0 seconds. **Only 21 calls in 15 days lasted more than a minute.**
- Where first-contact latency can be computed at all (n=18, small): **median 13.7 hours**, p90 71.6 hours, **zero within 5 minutes**, one within an hour.

Telephony is not writing back to the CRM. So "the customer doesn't respond" is currently an untested assertion — there is no record of how many times, at what hour, or on what channel anyone tried. A 12-second ring-out is being recorded as "Avoiding Call".

### Segment detail

- **27% of leads arrive 19:00–08:00 IST** (outside RM hours). No-contact 40.7% vs 38.0% in-hours — real, but not the main driver.
- LeadChain batch-sync is no longer distorting arrival times (max 3 leads in any one minute), so `Created_Time` is a fair proxy for form-submit.
- By campaign: **CCFS worst** — Avoiding Call 22.0%, no-contact 42.1%, and it is 56% of all leads. Incorporation 35.3% no-contact. Trademark 33.8%.
- Routing defect persists: three small non-RM queues sit at 50–86% stuck (`Singh-…5632013` 12/14, Santosh Kumar — Gold Team, not inbound RM — 9/14, `Gupta-…7006` 8/16). Among the real RM queues, Anish Singh 38.6% stuck is the outlier; Gaurav Pandey 0% and Aditya Bisht 4.5% show the target is achievable at full volume.

**Diagnosis bucket: sales-process, not targeting.** This matches the standing baseline (~51% of losses are sales-process).

---

## 2. Action plan, in priority order

### 1 · Ship the WhatsApp auto-response (P0 — approved 9 Jul 2026, still not built)
Meta lead form → Zoho workflow → WhatsApp utility template within **60 seconds** of submission, from a dedicated verified WABA number.

Someone fills the form on a phone, inside Instagram, and then receives a call from an unknown 10-digit mobile 13 hours later. Instant WhatsApp from a named business is the single highest-leverage change available.

- **Blocked on you:** WABA provider (Zoho's own WhatsApp for CRM, Interakt, Wati or Gupshup), a dedicated number, template approval.
- **Confirming metric:** ≥25% of new leads reply on WhatsApp within 30 minutes, measured over 14 days.

### 2 · Codify a contact cadence in the CRM, not in people's heads
Six attempts across five days and at least two channels, at varied times of day:

| # | When | Channel |
|---|---|---|
| 1 | T + 5 min | Call |
| 2 | T + 15 min | WhatsApp |
| 3 | T + 4 h | Call (different time band) |
| 4 | Day 2 morning | Call |
| 5 | Day 3 evening | Call |
| 6 | Day 5 | WhatsApp + email, then close |

**"Avoiding Call" may only be selected after 6 documented attempts on ≥2 channels.** Enforce with a validation rule on `Why_Disqualified`.

### 3 · Connect a cloud dialer so every dial is recorded
Zoho Voice, Exotel, Knowlarity or Ozonetel — whichever your team will actually use — writing a Call record with duration, disposition and recording against the **Lead**.

- **Confirming metric:** ≥95% of paid-Meta leads carry at least one Call record.
- Until this exists, no speed-to-lead target can be enforced and every RM can attribute the gap to lead quality.

### 4 · SLA and auto-escalation on *Establishing Contact*
Zoho workflow:

- **> 4 working hours** → alert the owner and their manager
- **> 24 hours** → auto-reassign to a pooled queue
- **> 72 hours** → auto-move to a nurture sequence, out of the active pile

And fix routing so inbound Meta leads never land on admin or non-RM accounts. This owner-queue problem has surfaced on every watchdog run since 6 July under a different name each time — it is a missing rule, not a personnel issue.

### 5 · Cover the 19:00–08:00 window
27% of leads arrive when nobody is working. Two options — **run one, not both**, or the effect is unattributable:

- **(a) Preferred:** instant WhatsApp (covered by #1) plus a hard rule that overnight leads are called at 09:15 the next morning, before anything else.
- **(b)** Narrow the Meta delivery schedule so you stop buying leads you cannot work. Only do this if 30-day data shows out-of-hours leads are materially worse on **cost per won deal** — not on cost per valid lead.

### 6 · Ad-side changes — small, and only after the above land
- Add the **review / confirm step** to the CCFS instant form (Meta's higher-intent form option). CCFS carries 56% of leads and the worst Avoiding Call rate at 22.0%. *Note: the 13 Aug decision was no changes to CCFS delivery settings — a form-level change is separate from the campaign, but confirm before executing.*
- **Set caller expectation** in the ad and on the thank-you screen: "Our advisor will call you from 0120-XXXXXXX within 15 minutes." A named, expected caller ID is the cheapest answer-rate lift available.

---

## 3. Caller ID and compliance

- Calling from an ordinary 10-digit mobile gets the number spam-labelled in Truecaller and answer rates collapse. A single branded, published, searchable business line is worth more than any script change. TRAI's **1600 numbering series** mandate for service and transactional calls is currently directed at BFSI entities and does **not** bind SetIndiaBiz — but the direction of travel is that unidentified numbers get answered less.
- Keep the consent trail clean. The Meta lead form must carry an explicit consent line and a link to the privacy notice. That is what makes the outbound call a consented business communication under the **TCCCPR 2018**, and gives you notice-and-consent evidence under the **DPDP Act 2023** read with the **DPDP Rules 2025** (notified 14 Nov 2025; legacy-data revalidation by 13 Nov 2026; full enforcement from ~13–14 May 2027). WhatsApp follow-up specifically needs opt-in captured at form level plus a Meta-approved template.
- Follow-up messaging must not promise statutory timelines you do not control (MCA / GST processing) — the same accuracy rule that governs ad copy under the Companies Act 2013, LLP Act 2008 and CGST Act 2017.

---

## 4. What I would do this week

**#1 and #4.** Both are Zoho-side, need no Meta change, and do not disturb the CCFS / TM end-date decisions still open from 13 Aug.

**The one decision blocking progress:** the WABA provider and dedicated number for P0. That has been the blocker since 9 July.

---

*Caveats: first-contact latency is computed on only 18 leads — the direction is clear, the precise median is not. Loss buckets use a created-date cohort (9–20 Aug), not modified-date; do not compare directly against modified-date readings in earlier watchdog runs.*
