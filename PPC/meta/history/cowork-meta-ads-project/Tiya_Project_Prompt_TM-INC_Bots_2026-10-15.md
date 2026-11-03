# Prompt for the SalesIQ Tiya project: Trademark and Incorporation WhatsApp bots (15 Oct 2026)

Paste everything below the line into a new chat in the **SalesIQ Tiya** project. Rule ids filled 15 Oct 16:3x (rules created by Sanjeev in Setup and read back).

---

Build two new SalesIQ WhatsApp bots for Meta click-to-WhatsApp ads, by copying the pattern of the live SIB-04 bot **"Tiya - Annual Filings"** (brand Compliance & ACR, number [phone redacted]). Build one bot at a time; show me each bot's flow before saving, and ask before every save or publish.

## What each bot must do (same as SIB-04)

1. On the first message, read the ad code from the pre-filled text (pattern below) and the customer's WhatsApp number.
2. Call the existing plug **`sib_wa_lead`** straight away (claim the lead), with the inputs in the table. Do not change the plug's code — it is shared by every campaign.
3. **Support-first routing** (Sanjeev, 13 Oct and again 15 Oct): every chat, new or existing customer, goes to the **Customer Support** department. Support engages, checks the CRM owner the plug returns, and transfers the chat to that owner. No direct routing to sales, no auto-transfer of missed chats, no CRM task for missed chats.
4. Outside chat hours (Mon–Sat 09:30–19:30 IST) the bot collects name and need, says the team will reply in working hours, and still calls the plug so the lead exists in CRM.
5. Keep the bot short. No price quotes, timelines or guarantees in bot text beyond what is listed under "Allowed claims".

## Inputs for `sib_wa_lead`

| Input | Trademark bot | Incorporation bot |
|---|---|---|
| WhatsApp number / brand | +91 95994 81905 · brand **Trademark & IPR** | +91 95991 99509 · brand **Start Business** |
| `adcode` | from the pre-filled text: TM-C1, TM-C2 … | INC-C1, INC-C2 … |
| `campaign` | `SIB-02 Trademark` | `#IND 1 — Incorporation` (exactly as the form leads are stamped, with the em dash) |
| `productid` | `1123581000103801012` (TMF - Standard TM Filing) | `1123581000069126115` (Incorporation - Pvt Ltd) |
| `productcat` | `TM Filing in India` | `Start Company` |
| `tag` | `FB-TMF` | `FB-INC` |
| `ruleid` | `1123581000948411109` ("PPC - SIB-02 Trademark - PG-09") | `1123581000948411180` ("PPC - INC Incorporation - PG-01") |
| `clid` | the ctwa_clid if SalesIQ exposes it (it has not so far; leave blank — the Meta Ads project captures clicks separately) | same |
| `name`, `phone`, `email`, `answers` | as in SIB-04 | as in SIB-04 |
| `dryrun` | `yes` for the first test, then blank | same |

Blank ad code = organic chat → the plug files it as "Social - WhatsApp" (that is correct; do not force an ad code).

## Allowed claims in bot text (settled 7 and 15 Oct)

- **Trademark:** professional fee ₹1,999 + GST; government fee ₹4,500 per class for individuals, startups and small enterprises (₹9,000 for others), at actuals; free trademark search before filing; 14,000+ trademark applications filed; reply to an examination report is quoted separately; "™ once filed, ® only after registration". Not affiliated with IP India.
- **Incorporation:** professional fee ₹2,499 + GST; typically 5–7 working days after complete documents, subject to MCA processing; 25,000+ businesses served; not affiliated with MCA.
- Never: "guaranteed", "registered in X days", "10 years protection" without "after registration", any government-affiliation wording.

## Checks before go-live (report each OK / NOT OK)

1. Brand **Trademark & IPR** owns +91 95994 81905 and brand **Start Business** owns +91 95991 99509; both numbers are in the "Setindiabiz - Salesiq" WABA and linked to the Facebook Page setindiabiz.official.
2. Each brand's channel department and "Departments responsible for chats" = **Customer Support** only.
3. WhatsApp credit balance (do not top up — Sanjeev only).
4. A dry run of each bot with `dryrun = yes` returns `matched` and no write.
5. One live test per bot from a test phone with a real ad code (e.g. "Hi, I want to register a trademark (TM-C1)"): the CRM lead has Lead_Source **Advt - WhatsApp**, Meta_Ad_Code TM-C1, Meta_Campaign as above, Product Name and Product Cat filled, Tag added, and an owner from the right pool (or Pavneet Kaur if none online). Tell Sanjeev the test lead ids so he can delete them.

## Do not touch

- The SIB-04 and SIB-05 bots, the `sib_wa_lead` code, the CRM assignment rules, LeadChain, and anything in Meta Ads Manager.
- Any secret or token.

When both bots are live, write a short note for the Meta Ads project with: bot names and ids, publish times, test lead ids, and the exact pre-filled message text to use in each ad (with its ad code).
