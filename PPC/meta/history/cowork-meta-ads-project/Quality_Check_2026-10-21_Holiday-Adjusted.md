# Holiday-adjusted lead quality check, 21 Oct 2026 (~11:20 IST)

Asked by Sanjeev: "check if the quality has improved. as there was holiday yesterday the agents would not have worked on the leads". Read-only. Continues `Lead_Quality_Watch_Log.md` (21 Oct 09:41 run).

## Method
- CRM pull: 566 paid leads (Advt - Facebook / Instagram / WhatsApp), created 10–21 Oct; file /tmp/meta_leads_10_21oct.csv (session only).
- Because of the 20 Oct holiday, rates are taken on **worked leads only** (status moved past blank / Establishing Contact). Unworked leads are shown separately and do not count against the ads.
- Junk = Why_Disqualified in {Inquired by Mistake, Wrong Info, Job Seeker, Bot Created/Spam, Language Issue} or any quality field "Invalid…". Valid = any quality field "Valid…" (not "Product Not Ready") or status Valid Lead / Negotiation / Proposal Sent / Payment Pending.
- Cohorts: **Before** 12–16 Oct (SIB-04 open-audience ad sets live) vs **After** 17–19 Oct (Directors-only SIB-04, tightened guardrails). 20–21 Oct shown only for volume (mostly unworked).
- Spend: account level (Meta connector).

## Result: quality has improved sharply

| Account level | Leads | Worked | Junk (of worked) | Valid (of worked) | Spend | ₹/lead | ₹/valid so far |
|---|---|---|---|---|---|---|---|
| Before 12–16 Oct | 346 | 242 (70%) | 151 (62%) | 52 (21%) | ₹38,265 | ₹111 | ₹736 |
| After 17–19 Oct | 113 | 55 (49%) | 5 (9%) | 44 (80%) | ₹27,552 | ₹244 | ₹626 (ceiling; 51% still unworked) |

| Campaign / path | Before: worked → junk / valid | After: worked → junk / valid |
|---|---|---|
| SIB-04 WhatsApp | 181 → 134 / 18 (74% / 10%) | 7 → 2 / 2 (29% / 29%) |
| SIB-04 Form | 35 → 15 / 11 (43% / 31%) | 7 → 2 / 4 (29% / 57%) |
| #IND1 Incorporation | 16 → 1 / 14 | 26 → 1 / 25 (4% / 96%) |
| SIB-02 Trademark | 10 → 1 / 9 | 15 → 0 / 13 (0% / 87%) |

- Raw cost per lead doubled (₹111 → ₹244) while junk fell from 62% to 9% of worked leads — the trade Sanjeev set on 16 Oct ("good quality consistently, cost will come down").
- The 5 junk "after" leads: 3 Inquired by Mistake (incl. …948913248, already flagged as an RM mislabel), 1 Wrong Info, 1 Invalid - Incorrect Details (#IND1).
- SIB-04 Directors n is small (14 worked); the formal stop-loss read stays on 23 Oct.

## Holiday effect
- Only 5 pre-20-Oct leads were touched on 20 Oct; 17 so far today (to ~11:10).
- 20–21 Oct: 44 leads, 37 unworked. The 5 SIB-04 WhatsApp chats of 20 Oct are all unworked.
- 183 paid leads created up to 19 Oct are still unworked (>24 h).
- Swati tracker (161 leads, deadline today): Agent Summary shows 0 checked / 0 CRM-updated; CRM shows 132 of the 161 still blank or Establishing Contact (29 moved by agents).

## Funding
- No top-up since ₹25,000 on 18 Oct 22:12. 09:41 run estimated ~₹0.9k credit left; ₹2,334 spent today by ~11:10 and ads still delivering. Delivery will stop once the balance is used. Top-up is human-only.

## Recommendations (not executed)
1. Top up (about ₹19.4k for 2 days incl. GST). Confirm: no `account_spend_limit_reached` at 22 Oct run, 21 Oct spend ≥ ₹7.5k.
2. No ad changes. Hold everything as is; the quality fix is working. Sales team to clear the 183 unworked leads and the 20 Oct WhatsApp chats before the 23 Oct Directors read. Confirm: unworked >24 h ≤ 100 on 22 Oct.
