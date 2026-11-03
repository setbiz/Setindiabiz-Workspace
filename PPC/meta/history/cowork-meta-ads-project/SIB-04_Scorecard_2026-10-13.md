# SIB-04 scorecard — launch (9 Oct 21:35) to 13 Oct 17:25 IST

Read-only. Spend comes from the Meta connector (ad sets, 9–13 Oct, today partial). Outcomes come from Zoho CRM (Meta_Campaign = "SIB-04 Annual Filings", 145 records) after today's WhatsApp tagging and backfill. Spend is matched to CRM by ad set: WhatsApp leads ↔ CTWA ad set, form leads ↔ Form ad set.

## Scorecard

| | CTWA (WhatsApp) | Form | Campaign |
|---|---|---|---|
| Spend | ₹13,774 | ₹8,672 | ₹22,446 |
| Meta results | 118 conversations | 26 form leads | — |
| CRM leads | 123 (+1 untagged chat) | 22 (19 new + 3 merged into older records) | 145 |
| Valid¹ | 32 (26%) | 5 (23%) | 37 |
| Progressed (Proposal Sent) | 4 | 0 | 4 |
| Committed / Won (deals) | 0 | 0 | 0 |
| Lost | 30 | 0 | 30 |
| Still open: Establishing Contact / blank | 62 / 5 | 11 / 6 | 84 |
| **Cost per valid** | **₹430** | **₹1,734** | **₹607** |
| Cost per progressed | ₹3,444 | — | ₹5,611 |
| Baseline cost per valid (9–13 Oct, 12:00 read) | ₹529 | ₹1,943 | ₹731 |

¹ Valid uses the same rule as the CAPI feed: Lead Status is Valid Lead / Proposal Sent / Negotiation / Payment Pending, **or** RM, TL or CSD quality is one of the four "Valid - …" tiers. Some leads were graded valid and later marked Lost; they are counted as valid.

The improvement over the 12:00 baseline comes mainly from WhatsApp leads that were graded but had not been tagged. It is not a delivery change. 84 leads are still open, so the valid counts will rise.

## Loss diagnosis (30 lost, all WhatsApp)

| Reason | Count | Bucket |
|---|---|---|
| Inquired by Mistake | 19 (63%) | Targeting / placement (accidental taps; Audience Network was excluded today) |
| Job Seeker | 4 | Targeting |
| Wrong Info | 2 | Qualification |
| No Product Offering | 2 | Offer |
| Not Eligible | 1 | Qualification |
| Not Interested | 1 | Natural attrition |
| Non-Compliant | 1 | Qualification |

"Inquired by Mistake" is the metric to watch after the placement change. Read it on 17 Oct together with the stop-loss.

## Speed-to-lead exceptions

**Never touched (status blank, more than 2 h old):**

| Lead | Path | Owner | Created | Age |
|---|---|---|---|---|
| 1123581000946586161 | Form (IG) | Sudip Manna | 10 Oct 20:33 | 69 h |
| 1123581000946488294 | Form (FB) | Sudip Manna | 11 Oct 21:01 | 44 h |
| 1123581000946463322 | Form (FB) | Sudip Manna | 11 Oct 21:53 | 44 h |
| 1123581000946494612 (Ramratan Kedia) | WhatsApp | Suman Khowal | 12 Oct 16:52 | 25 h. The chat was handled and closed by Suman, but the lead was never updated. |
| 1123581000946463283 | WhatsApp | "Lost Records" user | 11 Oct 18:19 | 47 h |
| 1123581000946538530 | WhatsApp | "Lost Records" user | 12 Oct 16:26 | 25 h |
| 1123581000946574748 (Gandhharv Sachdeva) | WhatsApp | Mahima Sehrawat | 13 Oct 14:24 | 3 h |
| 1123581000946442923 | Form (IG) | Anish Singh | 13 Oct 15:20 | 2 h |
| 1123581000946567286 (Virendra Sharma) | Form (FB) | admin account | returning customer | Sanjeev's call (12 Oct) |

**"Establishing Contact" for more than 48 h with no grading (19):**

| Owner | Leads |
|---|---|
| Gaurav Pandey | 5: …345232, …549264, …554044, …554177, …613161 |
| Tarun Kumar | 4: …429364, …442225, …561146, …574255 |
| Amit Kumar 3 | 3: …442337, …561005, …567156 |
| Priyam Tiwari | 3: …564159, …586137, …586836 |
| Anish Singh | 2: …553288, …586197 |
| Krishna Gupta | 1: …463207 |
| Praveen Singh | 1: …538212 |

Many of these show a Modified Time of 13 Oct 13:57. That was today's backfill, not rep activity.

**Other data gaps:**
- One WhatsApp chat is still untagged: Srinivas Poojary 1123581000946435741 (chat #61494, 13 Oct 14:50, "Self - Web Chat", Lost). It arrived on the old bot version before V5.
- Form leads: Meta counts 26, CRM has 22. Two of the gap are in the CRM Recycle Bin (Aniket Srivastava, Hemang Tiwari; 12 Oct open item 7).
- 3 WhatsApp leads sit with the "Lost Records" user. Two are blank and one is Establishing Contact (Znight …575496). Check whether that user is intended for them.

## Recommendations

1. **Sales process, not ads (no Meta change).** Ask the TLs today to:
   - clear Sudip Manna's 3 untouched form leads (44–69 h);
   - grade the 19 leads stuck in "Establishing Contact" for more than 48 h.

   Per the baseline, speed-to-lead is the #1 loss driver. Ungraded leads also never reach Meta as ValidLead.
2. **Hold Meta changes until the 17 Oct stop-loss read.** The placement exclusions are in their 3-day window, and changes go one variable at a time. Candidate for 17 Oct if the gap persists: shift budget from the Form ad set to CTWA. Form costs about 4× more per valid lead (₹1,734 vs ₹430). Confirming metric: campaign cost per CRM valid lead over the 3 days after the shift.
