# Pilot Specs — approved direction 9 Jul 2026
Goal fit: all four pilots attack cost-per-VALID (not raw CPL) and the #1 loss driver (Avoiding Call, 45% of June losses). Launch ONE at a time; judge on cost/valid; every Meta build needs explicit approval before go-live. NOTE: ad-level creation via API is blocked (leadgen-ToS error 1815089) — builds go via Ads Manager in browser.

## Pilot 0 — WhatsApp auto-follow-up on form leads (Zoho-side, NO Meta change) — DO FIRST
**What:** the moment a paid lead lands (Lead_Source in 'Advt - Facebook'/'Advt - Instagram'), auto-send a WhatsApp acknowledgement: brand intro + what happens next + call-slot link/reply prompt. Kills the form-and-forget gap while keeping LeadChain/CAPI attribution untouched.
**Build:** Zoho workflow on Lead create (criteria: the two paid sources) → WhatsApp send via the connected provider. Template = utility category, e.g.: "Hi {{Name}}, thanks for your enquiry about {{Service}} with SetIndiaBiz. Your relationship manager will call you within working hours today. Reply 1 for a callback slot, 2 for details on WhatsApp." No pricing/guarantee claims in template (keeps it compliance-safe and approval-easy).
**Stamp for measurement:** set a field (reuse an existing unused field or add `WA_Ack_Sent_At` datetime) so the daily task can report coverage %.
**Success metric (14d):** Avoiding-Call share of losses ↓ from ~45% baseline; Establishing-Contact >48h count ↓. Cost: template messages only (~₹0.12–0.35/msg).
**Inputs needed from Sanjeev:** (1) which WhatsApp provider/number is live for outbound (Tiya's WABA? SalesIQ? WATI/AiSensy?), (2) confirm the lead form discloses WhatsApp contact (add opt-in line on next form edit to be safe under WhatsApp Business Policy), (3) approve template text.

## Pilot 1 — Call ads on Trademark (Meta build, browser route)
**What:** new campaign "#IND3C — TM Call Ads Pilot", OUTCOME_LEADS with call conversion location; audience = clone of TM SA interests; schedule 10:00–18:00 IST Mon–Sat (tele-team live answer); creative reuses the "start your application process within 24 hours" positioning (defensible wording — keep; ₹1,999 professional fee + govt fee shown separately; TM-A e-filing fee ₹4,500 individuals/startups/MSME vs ₹9,000 others — Trade Marks Rules 2017, First Schedule).
**Budget:** ₹1,000/day, 7-day pilot. **Stop-loss:** 3-day cost per call (≥15s) > ₹400, or spend > ₹1,500 with zero calls → pause.
**Attribution:** calls land as live inbound — use a DEDICATED number so the tele-team logs "Meta Call Ad" as source (no LeadChain path exists for calls). Manual Zoho lead creation SOP for answered calls, Lead_Source value to be decided (suggest adding 'Advt - Facebook' + a Meta_Ad_Type='call' stamp, or a new taxonomy value — Sanjeev to pick).
**Inputs needed:** dedicated phone number + who answers + go/no-go.

## Pilot 2 — Click-to-WhatsApp (CTWA) on Company Registration — AFTER Pilot 0 proves WA handling
**What:** ad set in IND1 (or new campaign "#IND1W") with WhatsApp conversion location; INSA interest audience; conversation-starter flow: "Which business type? Pvt Ltd / LLP / OPC" → qualification in chat.
**Why gated:** WA leads bypass LeadChain → without capture they'd be invisible to Zoho/CAPI (same reason Meta's click-to-message suggestion was rejected 4 Jul). Capture path exists in principle: Tiya already writes WhatsApp chats to Zoho with phone identity (V44). Needed: (1) Tiya/inbox coverage for ad-initiated chats on the WABA number, (2) stamp `CTWA_Click_ID` (referral payload ctwa_clid) on the lead, (3) taxonomy decision: 'Advt - WhatsApp' value or map into 'Advt - Facebook'/'Advt - Instagram' by placement, (4) update CAPI gates + daily-task segment if a NEW Lead_Source value is added (they filter on the two Advt values — a third value would silently undercount).
**Budget when live:** ₹1,500/day, 7 days. **Stop-loss:** 3-day cost per started conversation > ₹200 or CRM-captured% of conversations < 70%.

## Pilot 3 — Website conversions retest (gated to ~end July)
**Gate:** CAPI ValidLead ≥ 50/week steady AND P9 quality-optimisation switch done on C1 Daytime INSA. The paused web assets exist (C1 Daytime/24Hr Web ad sets, "#IND 2 — Business Registration - Website" OUTCOME_SALES campaign) — rebuild fresh against the ValidLead event rather than reactivating stale structures.
**Best products:** DPIIT + company registration (research-heavy); landing pages on setindiabiz.com with form → LeadChain/webform → Zoho (attribution intact via UTM + fbclid → 'Advt - Facebook'/'Advt - Instagram' stamping already handled by the QA sweep rules).
**Budget when live:** ₹1,500/day, 14 days (web needs longer learning). **Stop-loss:** 7-day cost/valid > 1.5× account average.

## Sequence & review
Pilot 0 now (Zoho-side) → Pilot 1 next week → Pilot 2 once WA capture verified → Pilot 3 at CAPI gate. The consolidated daily task (08:00 IST) carries a monitor line per pilot. Review each at day 7 against its stop-loss; kill fast, scale only the winner into the 150×150 portfolio.
