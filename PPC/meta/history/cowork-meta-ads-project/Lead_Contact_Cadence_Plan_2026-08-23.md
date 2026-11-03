# Lead Contact Cadence — Build Plan
**SetIndiaBiz · Meta lead-form leads · 23 August 2026**
Stack: **Interakt** (WhatsApp Business API) + **Tata Tele Smartflo** (cloud telephony) + **Zoho CRM**

---

## 0. Prerequisite finding — read this first

You already own the telephony. It is barely connected.

Across **all 286 Zoho call records org-wide for 9–23 Aug 2026**:

- **50 records came from the dialer** (`Scheduled_In_CRM = False`, real durations, subjects of the form *"Outgoing call to <name> (+91…)"*). Of those 50, **49 belong to one person: Praveen Singh** (`praveen@setindiabiz.com`, Relationship Manager, Sales – Gold Team, user id …005632013). One belongs to Srivastava. **Nobody else's calls reach the CRM at all.**
- The other **222 records are manually-scheduled Zoho activities**, of which **175 (79%) are `Overdue`** — reminders nobody closed. Concentrated on Srivastava (67), Jadhav (29), Pandey (26).
- Even Praveen's dialer log is bleak: **24 of his 50 calls are 0 seconds**, and the median across all completed calls is **12 seconds**.

**So Smartflo is provisioned but effectively unused.** Every other RM is dialling from a personal mobile, which means no log, no duration, no recording, no disposition — and "Avoiding Call" gets selected with zero evidence behind it.

**Nothing else in this plan works until that is fixed.** Step 1 of the rollout is not the cadence — it is getting every inbound RM onto Smartflo click-to-call from inside Zoho.

> Side note worth checking: Praveen Singh holds 14 paid-Meta leads of which 12 sit in *Establishing Contact* (85.7%) — yet he is the only person actually logging calls. That looks like a **status-hygiene** problem, not a calling problem. Different fix: he is working leads without updating `Lead_Status`.

---

## 1. Channel economics (India, 2026)

| Message type | Cost per message | Notes |
|---|---:|---|
| Utility template | **₹0.115** | Business-initiated, transaction/request-specific |
| Marketing template | **₹0.8631** | Up ~10% in 2026 from ₹0.7846 |
| Authentication | ₹0.115 | Not relevant here |
| Service (reply inside the 24h customer-initiated window) | **₹0** | Free once the lead replies |

Meta moved to **per-message** pricing in 2025. Practical consequence for us:

- At ~45 leads/day and 3 templates per lead, worst case (all categorised Marketing) is **≈₹117/day**. Against a ₹250 CPL that is noise. **Cost is not a reason to under-message.**
- Write message 1 as a **confirmation of the enquiry the person just submitted** ("We've received your enquiry for X; your advisor <Name> will call you from <number> at <time>"). That framing has the best chance of being categorised Utility. If Meta categorises it Marketing anyway, proceed — the cost delta is ~₹34/day.
- **The prize is the reply.** The moment a lead replies, a 24-hour free service window opens and the RM can converse at zero marginal cost. Design every template to invite a reply (quick-reply buttons: *"Call me now" / "Call me later" / "Send details on WhatsApp"*).
- If you later run the CTWA pilot (P2), click-to-WhatsApp ads open a **72-hour** free window — a materially better economic structure than lead forms. Worth revisiting after this cadence is live.

---

## 2. The cadence

**Trigger:** Lead created with `Lead_Source` in `('Advt - Facebook', 'Advt - Instagram')`.

| # | Timing | Channel | Actor | Mechanism |
|---|---|---|---|---|
| **0** | **T + 60 seconds** | WhatsApp template 1 (enquiry confirmation + quick replies) | Automated | Zoho workflow → Interakt |
| 1 | T + 5 min | Call attempt 1 | RM | Smartflo click-to-call from the Lead record |
| 2 | T + 30 min | Call attempt 2 | RM | Only if attempt 1 < 30s |
| 3 | T + 4 hours | Call attempt 3 — **different time band** | RM | |
| 4 | Day 2, 10:00–12:00 | Call attempt 4 | RM | |
| 5 | Day 3, 17:00–19:00 | Call attempt 5 — different band again | RM | |
| 6 | Day 5 | WhatsApp template 2 (value + last call offer) + email | Automated | |
| 7 | Day 7 | Close: Lost / *Avoiding Call*, **or** move to nurture | RM | Only now is "Avoiding Call" permissible |

**Out-of-hours leads (19:00–08:00 IST — currently 27% of volume):** WhatsApp template 0 fires immediately regardless of hour. The call clock starts at 09:00; **attempt 1 must be logged by 09:15**, before anything else in the RM's day.

**Varying the time band is not decoration.** Five calls at 11 a.m. on five days is one experiment repeated five times. The bands above are deliberately spread across morning, afternoon and evening.

---

## 3. Rules that make it real

1. **"Avoiding Call" is locked.** A validation rule on `Why_Disqualified` blocks the value unless the lead has **≥5 Smartflo call attempts** and **≥2 WhatsApp touches** logged. Today it is being applied after a 12-second ring-out.
2. **Define a connect.** A **Smartflo call of ≥30 seconds** is a contact. Anything shorter is an *attempt*. Report the two separately — this single definition is what turns "they don't respond" from an opinion into a number.
3. **Escalation, not name-and-shame.** Zoho workflow on `Lead_Status = 'Establishing Contact'`:
   - **> 4 working hours** with no logged attempt → alert owner + manager
   - **> 24 hours** → auto-reassign to a pooled queue
   - **> 72 hours** → auto-move to nurture, out of the active pile

   The stuck-lead owner has changed name on every watchdog run since 6 July. It is a missing rule, not a person.
4. **Fix routing.** Inbound Meta leads must never land on admin or non-inbound accounts. Three small queues currently sit at 50–86% stuck.
5. **Retire the manual "scheduled call" habit** for new leads. 175 overdue reminders in 15 days says the activity record is being used as a sticky note. The cadence should generate the tasks; the RM should only close them.

---

## 4. Instrumentation to build

New fields on **Leads**:

| Field | Type | Populated by |
|---|---|---|
| `First_Attempt_Time` | DateTime | First Smartflo call record |
| `First_Connect_Time` | DateTime | First Smartflo call ≥30s |
| `Attempt_Count` | Number | Rollup of Smartflo call records |
| `WA_Templates_Sent` | Number | Interakt callback |
| `WA_Replied` | Checkbox | Interakt inbound webhook |
| `Speed_To_Lead_Minutes` | Formula | `First_Attempt_Time − Created_Time` |

Add to the daily watchdog (Part A, speed-to-lead section):

- % of leads first-attempted within 15 minutes (in-hours) / by 09:15 (overnight)
- % of leads with ≥1 logged call — the honesty check on Smartflo adoption
- Median attempts before a lead is marked Lost
- WhatsApp reply rate within 30 minutes
- Connect rate (≥30s) by owner and by campaign

---

## 5. Targets — 30 days from go-live

| Metric | Today | Target |
|---|---|---|
| Leads with ≥1 logged call | **7.8%** | **≥95%** |
| First attempt within 15 min (in-hours) | not measurable | ≥80% |
| WhatsApp reply within 30 min | 0 (no WA) | ≥25% |
| Connect rate (≥30s conversation) | not measurable | ≥65% |
| "Avoiding Call" share of losses | **45.5%** | **<25%** |
| Leads stuck in *Establishing Contact* >72h | 85 (median 8.8 days) | <10 |

---

## 6. Rollout

**Week 1 — instrumentation only, no cadence yet.**
Enable Smartflo click-to-call for every inbound RM licence and verify call records land on the Lead. Create the six fields. Submit both WhatsApp templates to Interakt for approval. Add the consent line to all three Meta lead forms.

**Week 2 — cadence live on ONE campaign.**
Use **Trademark** — cleanest volume, best cost/valid, lowest stakes. Measure against the 30-day targets. Do not touch ad settings in the same week or the result is unattributable.

**Week 3 — extend to Incorporation and Annual Return** once Trademark clears ≥80% first-attempt and ≥50% logged-call coverage.

---

## 7. Guardrails

- **One variable at a time.** Do not run the cadence rollout and the ad-side campaign rebuild in the same week.
- **Consent trail.** Every Meta lead form must carry an explicit consent line and a privacy-notice link. That is what makes the outbound call a consented business communication under **TCCCPR 2018**, and supplies notice-and-consent evidence under the **DPDP Act 2023** with the **DPDP Rules 2025** (notified 14 Nov 2025; legacy-data revalidation 13 Nov 2026; full enforcement ~13–14 May 2027). WhatsApp specifically requires opt-in captured at form level plus a Meta-approved template.
- **Caller ID.** Route all outbound through the Smartflo business number, published on the website so it is searchable. A branded, expected number is the cheapest answer-rate lift available. (TRAI's 1600-series mandate for service calls is BFSI-directed and does not bind SetIndiaBiz — but the direction of travel is that unidentified numbers get answered less.)
- **No statutory promises.** WhatsApp and call scripts must not commit to MCA / IP India / GST processing timelines you do not control — the same accuracy rule that governs ad copy under the Companies Act 2013, LLP Act 2008 and CGST Act 2017.

---

## 8. Click-to-WhatsApp ads, office hours only

You raised running CTWA inside office hours. **Agreed — with Interakt now in place this is the right next channel, and office-hours-only is the correct constraint.** The reasoning:

- CTWA opens a **72-hour free messaging window** versus 24 hours for a form-triggered template. Better economics and a much longer runway to convert.
- The lead arrives already *in a conversation*. There is no "will they pick up an unknown number" problem — which is the entire failure mode we are fixing.
- Restricting to office hours is right precisely because CTWA's advantage is a live human replying in minutes. A CTWA lead at 23:00 answered at 10:00 the next morning throws away the whole advantage. **Schedule 10:00–19:00 IST.**

**But do not switch everything over.** Three things must be handled first, and two of them will silently break existing reporting:

1. **`ctwa_clid` stamping.** CTWA conversations must carry the click ID into Zoho or the lead is unattributable to campaign/ad set. Interakt must pass it through; the `CTWA_Click_ID` field already exists on Leads from the 27 Jun build.
2. **Lead_Source taxonomy.** CTWA leads will land as WhatsApp conversations, not form submissions. Adding a new `Lead_Source` value **will break the CAPI conversion gates and every daily-watchdog segment filter**, which currently key on `'Advt - Facebook'` + `'Advt - Instagram'`. Decide the value first, then update the CAPI rules, the watchdog task and the Zoho Analytics scorecard **in the same change**. This is the single most likely way to lose a week of clean data.
3. **Don't collide with the cadence rollout.** Run CTWA as an **A/B against the lead form on one campaign only** — Trademark or Annual Return — after the cadence is live and stable on that campaign. Judge on **cost per won deal**, not cost per lead: CTWA leads will look more expensive per lead and should convert far better.

**Confirming metric:** CTWA cost per won deal ≤ lead-form cost per won deal over 21 days, with median first-reply under 10 minutes.

---

## 9. Open items needing your decision

1. Confirm Smartflo click-to-call is licensed for **all** inbound RMs, not just Praveen Singh — and if it is, why nobody else uses it.
2. Which number becomes the single published outbound caller ID.
3. Who owns the pooled queue that 24-hour-stale leads reassign into.
4. Sign-off on the two WhatsApp template drafts before they go to Meta for approval (I can draft both).
