# Change log: 21 Oct 2026, SIB-05 India Entry ads switched on

**Approval:** Sanjeev, 11:14–11:17 IST. Claude asked "Once your top-up shows, shall I switch on all 6 FDI ads…?"; Sanjeev replied "funded".
**Funding:** ₹20,000 added 21 Oct 11:17 IST (UPI) ≈ ₹16,949 ad credit after 18% GST. With SIB-05 on, daily budgets total ₹12,200 → about 1.4 days. Next top-up needed by ~22 Oct evening.

## Done (connector, ads_activate_entity, one call per ad; no ToS 1815089 error this time)

| Ad | ID | Before | After (read-back ~11:20) |
|---|---|---|---|
| E1 India entry | 120247067863760449 | PAUSED | ACTIVE, delivering (ad set learning) |
| E2 Structures | 120247068331330449 | PAUSED | ACTIVE, IN_PROCESS |
| S1 From USD 499 | 120247068431620449 | PAUSED | ACTIVE, IN_PROCESS |
| S2 After incorporation | 120247068431630449 | PAUSED | ACTIVE, IN_PROCESS |
| B1 Liaison office | 120247068705360449 | PAUSED | ACTIVE, IN_PROCESS |
| B2 Branch office | 120247068705370449 | PAUSED | ACTIVE, IN_PROCESS |

Nothing else changed: campaign 120247067847480449 (CBO ₹4,000/day), 3 ad sets (7 countries, end 31 Dec 2026 23:59 IST), targeting and creatives untouched. TM and INC WhatsApp drafts not published.

## Stop-loss (logged before execution)
- Capture: if CRM FDI leads < 80% of Meta form leads over the first 48 h → pause the campaign and check LeadChain v2 / the unknown lead-deleting job.
- Quality: after ≥10 worked leads, junk > 40% → pause the worst ad set.
- Spend: ₹8,000 spent with 0 CRM leads → pause and review.

## Open
1. Booking-link email workflow still fires for form v1 only; v2 leads won't get it. Needs Sanjeev's click in the workflow editor.
2. Unidentified automation deleting new leads as "Sanjeev Kumar" — match Meta FDI leads vs CRM daily.
3. B2 and S2 have no 9:16 image; E1 has no chat greeting (low impact).
