# For the "SalesIQ - Tia SalesIQ" project — from Meta Ads, 16 Oct 2026

Paste this into the SalesIQ project.

**Sanjeev approved both items on 16 Oct 2026** ("Ok approved all proposed changes, go ahead"). The Meta Ads project has **not** touched any bot, plug, assignment rule or Desk function. These changes are yours to make.

The evidence is in the Meta Ads project: `SIB-04_Junk_Diagnosis_2026-10-16.md` (sections 3–5).

## 1. Annual Filings bot (61466000026786012, [phone redacted]): add a qualifying question before an RM gets the chat

**Problem:** 27% of SIB-04 WhatsApp leads from 9–15 Oct were junk (62 of 229), with half still unworked. The main reasons:

| Reason | Leads |
|---|---|
| Inquired by Mistake | 46 |
| Job Seeker | 5 |
| Wrong Info | 6 |
| Bot / Spam | 3 |

RM notes include:
- "not having any company"
- "do not run any business"
- "searching Work From Home, 10th pass"
- "Loan enquiry"
- a data vendor
- language barrier

The pre-filled message is no filter. Chats opening with the coded "[ACR-C1]"-type text were 26% junk; chats opening with Meta's standard greeting were 27%.

**Ask:** make the first bot question something like:

> "Are you a director or partner of a company or LLP?" Yes / No / I want to start one

- **Yes:** continue the current flow (entity, years) and route to the LG-11 owner as now.
- **No:** send a polite close and mark the lead with a disposition (e.g. `Why_Disqualified = 'Not Eligible'` or a "Not a company owner" tag). It should not land in an RM's queue as a working lead.
- **I want to start one:** route to Incorporation (INC) instead.

**Keep:** first-touch stamping (Advt - WhatsApp, SIB-04, ACR) must still happen on chat open, so lead counts stay complete for ad reporting.

**Also seen, possibly a field-mapping bug.** Several `sib_wa_lead` notes show the Year field holding an entity answer, e.g.:
- "Entity: Private Limited | Year: One Person Company ("
- "Entity: Private Limited | Year: Private Limited"

Examples: leads 1123581000946554044 and 1123581000946554409.

## 2. Trademark and Incorporation bots: treat an ad link as the ad signal when the code is missing

**Finding on the ACR number (9–15 Oct):** about 53% of ad chats (122 of 229 leads) opened with Meta's standard greeting, not the coded pre-filled message:
- "Hello! Can I get more info on this?"
- Hindi, Gujarati and other translations of the same greeting

Every one of these messages still starts with the ad's own link: `https://fb.me/...` or `https://www.instagram.com/p/...`.
- Each link is consistently either coded or standard; no link mixes the two.
- So some renderings of each ad do not carry the custom message, probably the Reels and Stories versions. The Meta side is checking this.

**Risk for TM and INC:** your handover note says a chat without a code is filed as organic "Social - WhatsApp". If the TM and INC ads behave like ACR, about half of real ad chats would be filed as organic. That would understate ad results and keep them out of the CAPI loop.

**Ask:** in `sib_adcode` (or before `sib_wa_lead`), apply these rules in order:
1. **Code present** (TM-Cx / INC-Cx): as now.
2. **No code, but the first message contains `fb.me/` or `instagram.com/p/`:** file as an ad chat.
   - Use the bot's default code for that number, e.g. "TM-UNK" / "INC-UNK".
   - Set Lead_Source "Advt - WhatsApp" and the campaign stamp.
   - Ad-level attribution stays unknown.
3. **Neither:** organic, as now.

**Please tell the Meta Ads project once both are live**, so the 22 Oct read of the SIB-04 audience change can take the bot change into account.
