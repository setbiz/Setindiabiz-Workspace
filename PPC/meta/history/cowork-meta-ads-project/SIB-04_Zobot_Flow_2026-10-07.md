# SIB-04 Zobot "Setindiabiz Compliance" — flow for review (7 Oct 2026)

Status: import file built (`SIB-04_Zobot_Import.zip`, Tiya export format, 23 cards, unpublished). Nothing imported yet.
Brand: Compliance & ACR (app 61466000023310359) — WhatsApp [phone redacted]. All chats treated as SIB-04 ad chats (Meta_Ad_Code "ACR").

## Flow
1. **Welcome** — "Hi %visitor.name%! Thanks for contacting Setindiabiz about annual ROC filings. Three quick questions, then we'll connect you to a compliance expert."
2. **Entity** — Private Limited / One Person Company (OPC) / LLP (typed answer → Private Limited path).
3. **Year** — FY 2025-26 only / FY 2025-26 + earlier years pending / Not sure.
4. **AGM (Pvt Ltd only)** — "Has the AGM for FY 2025-26 been held?" Yes, held / Not yet / Not sure. Not asked for OPC (s.96(1) Companies Act 2013 exempts an OPC from holding an AGM) or LLP (no AGM under the LLP Act 2008).
5. **Plug sib_wa_lead** — phone/name/email from WhatsApp; adcode ACR; campaign "SIB-04 Annual Filings"; productcat "Annual Filing"; tag FB-ACR; ruleid 1123581000945354238; productid = ACR - Company Annual Return (Pvt Ltd, OPC) or LLP Annual Return (ACR) (LLP); answers = one line of the replies. Outputs to wa_matched, wa_recordid, wa_ownerid, wa_owneremail, wa_ownername, wa_status.
6. **Route** — owner email matches one of the 10 SIB-04 rule owners (Pragya, Rishika, Tarun, Mahima, Anish, Amit Kumar 3, Priyam, Gaurav, Suman, Praveen) → forward to that person. Else, an existing Contact (client) → Customer Support. Else → Sales - CACS ACR.
7. **Fallbacks** — owner busy/offline/no answer → Sales - CACS ACR (any of its operators, support staff included — accepted by Sanjeev 18:53) → if nobody is free: "An expert will call you on this WhatsApp number as soon as the team is back online." and close.

Messages make no claims about fees, timelines or outcomes.

## Steps before it can go live (each needs Sanjeev's go)
1. Publish plug `sib_wa_lead` (now Draft).
2. Add Sales - CACS ACR to the Compliance & ACR brand's departments (today only Customer Support), so forward cards can reach it.
3. Import the zip via Zobot › Add › Via import, unpublished. Check the Plugs list for a duplicate `sib_wa_lead` afterwards.
4. In the builder, switch the 10 "A06 Forward to <name>" cards from the department to the named operator (the export format for operator targets is not known, so they import pointing at Sales - CACS ACR).
5. Phone test on [phone redacted], then publish only on an explicit go.

Note: WhatsApp balance shows 10 credits — top-up needed before template messages to form leads.
