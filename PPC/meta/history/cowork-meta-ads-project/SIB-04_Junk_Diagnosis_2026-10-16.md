# SIB-04 (ACR) junk-lead diagnosis — 16 Oct 2026

Read-only. **No Meta or CRM changes were made.** This continues `SIB-04_Junk_Quality_Resume_Prompt_2026-10-15.md`.

**Sources:**
- Meta connector: targeting specs, ad and creative reads, gender and region breakdowns for 9–15 Oct.
- Zoho CRM COQL, pulled 16 Oct about 11:30 IST: 1,549 leads created since 9 Oct, 388 "Tiya - Annual Filings" chat notes, and 1,606 FB/IG leads from 1 Jul to 24 Aug as history.

## Answer

The junk is not caused by placements or by the ad copy. Two things cause it:

1. **SIB-04 is the only campaign with none of the three hard audience limits** that CCFS, Incorporation and Trademark all use: English language, a city list, and (in most of them) a minimum age of 25.
   - With Advantage+ audience on, SIB-04's 15 director/LLP lists are only suggestions. Meta can show the ad to anyone in India aged 18 or over, in any app language.
2. **The WhatsApp ad set is optimised for "conversations started".** One tap opens a chat, so Meta finds people who tap, not people who own a company.
   - The form ad set has the same loose audience but asks two questions. It has **0 junk in 38 leads**, against 62 junk in 229 on WhatsApp.

There is **no setting that excludes "housewives" or "illiterate" people directly**:
- Meta removed detailed-targeting exclusions on 31 March 2025.
- The education, job-title and business-owner layers in Trademark and Incorporation never blocked anyone either. Advantage+ audience is on in those ad sets, so those layers are only suggestions.
- What actually filters is the English-language setting (which keeps out people whose Facebook app isn't in English), the city list and the minimum age.

## 1. Settings side by side

Live specs pulled 15 Oct.

| Setting | SIB-04 WhatsApp | SIB-04 Form | #IND4 CCFS | #IND1 24Hr INSA | #IND3 TMF-SA | SIB-02 TM Form |
|---|---|---|---|---|---|---|
| Advantage+ audience | On | On | **Off** | On | On | On |
| Location *(hard limit)* | All India | All India | 19 cities, 25 mi | 18 cities | 30 cities | 30 cities |
| Language *(hard limit)* | **None** | **None** | English (US, UK) | English | English | English |
| Minimum age *(hard limit)* | 18 | 18 | 18 (suggests 21–55) | **25** | **25** | **25** |
| Gender | All | All | Male (hard, A+ off) | All | Male (suggestion only) | Male (suggestion only) |
| Director/LLP lists | 15 lists + lookalike, used as suggestion, expansion on | same | 6 Director lists, hard, no expansion | none | none | none |
| Education / job title / business owner | none | none | none | suggestion only | suggestion only | suggestion only |
| Optimises for | Chats started | On-ad form leads | Dataset Lead event (website + form) | same | same | same |
| Placements | Advantage+ (AN and Marketplace off since 13 Oct) | FB + IG auto | Feed, Stories, Reels | Advantage+ | Advantage+ | FB, IG, Threads (listed) |

What Meta enforces when Advantage+ audience is on:
- **Hard limits:** location, minimum age, languages, custom-audience exclusions.
- **Suggestions only:** age range, gender, detailed targeting, custom-audience inclusions.

Sources: Meta Help, [About audience controls and audience suggestions in Advantage+ audience](https://www.facebook.com/business/help/938372127764391) and [Choose audience settings in Advantage+ campaigns](https://www.facebook.com/business/help/25941857932125812). For the removal of detailed-targeting exclusions on 31 Mar 2025: [Updates to detailed targeting](https://www.facebook.com/business/help/458835214668072).

## 2. Lead quality in CRM

Definitions:
- **Junk** = Why_Disqualified is Inquired by Mistake, Job Seeker, Bot Created/Spam or Wrong Info, or the RM/TL quality field is Invalid.
- **Valid** = Lead_Status is Valid Lead, Negotiation, Proposal Sent or Payment Pending, or a quality field starts with "Valid" (the project's KPI definition).

| Segment | Leads | Junk | Valid | Still unworked |
|---|---|---|---|---|
| SIB-04 WhatsApp, 9–15 Oct | 229 | **62 (27%)** | 41 (18%) | 115 (50%) |
| SIB-04 Form, 9–15 Oct | 38 | **0 (0%)** | 12 (32%) | 24 (63%) |
| #IND1 Incorporation, FB/IG, 1 Jul–24 Aug | 433 | 90 (21%) | 224 (52%) | matured |
| #IND3 Trademark, same window | 559 | 75 (13%) | 319 (57%) | matured |
| #IND4 CCFS, same window | 486 | 64 (13%) | 268 (55%) | matured |

WhatsApp junk is already above every comparator's matured rate, with half the leads still unworked.

### Cost per valid lead, 9–15 Oct (ad-set level)

| Ad set | Spend | Valid leads | Cost per valid |
|---|---|---|---|
| WhatsApp | ₹20,562 | 41 | **₹502** |
| Form | ₹14,660 | 12 | ₹1,222 |
| Campaign | ₹35,222 | 53 | ₹665 |

The campaign is under the 13 Oct baseline of ₹731 and the revert threshold of ₹914. **The placement-controls stop-loss does not trigger on this data.** The formal read is 17 Oct.

**WhatsApp is cheaper per valid lead, so don't switch it off. Tighten its audience instead.**

## 3. Evidence on language and literacy

**16 SIB-04 chats are written in Hindi, Gujarati or Tamil script.**
- They include Meta's own greeting translated into Hindi or Gujarati. Meta sends it in that language only when the person's app language is set to it, so these people were served the ad because SIB-04 has no English limit.
- Outcome: 1 valid, 7 lost, 8 unworked.

**What the RMs' notes and the opening messages say:**
- "अंग्रेजी नहीं आती" ("I don't know English")
- "Tell me hindi"
- "Language Barrier, so marking the lead as lost"
- "she is searching Work From Home, qualification 10th pass"
- "he is not having any company and not even aware about what we are"
- "do not run any business"
- "Loan enquiry"
- a data vendor selling MCA and GST data
- chats containing garbled voice-typed text

**Gender (WhatsApp ad set):**
- Women received 12% of spend but started 20% of chats: ₹62 per chat, against ₹115 for men. The chat optimiser therefore drifts towards cheap taps.
- CRM has no gender field, so junk cannot be tied to gender. Women directors and partners are genuine buyers.

**Age:**
- 18–24-year-olds started 13% of WhatsApp chats.
- In the form ad set they gave 12 of 43 leads, the cheapest at ₹198 each.

## 4. Ruled out

**Placements.**
- Audience Network went to ₹0 from 14 Oct, but WhatsApp junk did not fall. By creation day the junk rate was:

| Day | Junk |
|---|---|
| 10 Oct | 23% |
| 11 Oct | 10% |
| 12 Oct | 42% |
| 13 Oct | 18% |
| 14 Oct | 38% |
| 15 Oct | 21% |

- 14–15 Oct leads are still being worked, so those figures will rise.

**Ad copy.**
- All 8 creatives are in English and addressed to company directors and LLPs: ACR-C1 Deadline, ACR-C2 Cost of delay, ACR-C5 Dates and price, LLP-C1 Form 8, each as a WhatsApp ad and a form ad.
- The statutory references are accurate:
  - AOC-4 within 30 days of the AGM: Companies Act 2013, s.137(1)
  - MGT-7 within 60 days of the AGM: s.92(4)
  - ₹100 a day additional fee: s.403 read with the Companies (Registration Offices and Fees) Rules 2014
  - LLP Form 8 due 30 Oct: LLP Act 2008, s.34 read with LLP Rules 2009, r.24(4)
- Nothing in the copy invites job seekers. The copy is fine; it is simply shown to the wrong people.

**Pre-filled message text.**

| Chat opened with | Leads | Junk |
|---|---|---|
| Our coded message (e.g. "I want to file my company's AOC-4 and MGT-7 [ACR-C1]") | 81 | 26% |
| Meta's standard "Hello! Can I get more info on this?" | 122 | 27% |

People send the pre-filled text without meaning it. The text does not filter anyone.

## 5. Side finding — matters for the TM and INC WhatsApp ads

**About 53% of ACR chats (122 of 229 leads) arrived with Meta's standard greeting, not our coded message.**
- Each ad short link (fb.me/… or instagram.com/p/…) is either always coded or always standard; none mixes the two.
- So some renderings of each ad do not carry the custom message. They are probably the Reels and Stories versions that Meta creates as separate posts, but this needs checking in Ads Manager. The message template is not readable through the API.
- **Why it matters:** the SIB-04 bot stamps "ACR" on everything, so there is no harm here. The new **Trademark and Incorporation bots file any chat without a code as organic ("Social - WhatsApp")**. If their ads behave the same way, more than half of their ad chats will be counted as organic.
- **Possible fix for the SalesIQ project:** the first message always starts with the ad's fb.me or instagram.com/p link, which can serve as the ad signal when no code is present.

## 6. Recommended changes (need Sanjeev's approval, one at a time)

**Change 1 — WhatsApp ad set only: add English language and minimum age 25 as hard limits.**
- Advantage+ audience stays on.
- This brings SIB-04 in line with #IND1, #IND3-SA and SIB-02.
- Leave the Form ad set unchanged as the control group.
- **Do it on 17 Oct**, after the placement stop-loss read, so the 14–16 Oct window stays clean.
- Best done by Sanjeev in Ads Manager. An API targeting edit force-pauses the ad set, and reactivation is his. Expect a learning reset.
- **Stop-loss (3 days, 17–19 Oct, read on 20 Oct morning):**
  - Revert if WhatsApp cost per valid rises above ₹628 (₹502 + 25%).
  - Success if the WhatsApp junk rate on leads created in the window is at or below 15% and cost per valid is held.
  - Expect fewer and dearer chats. Judge on CRM, not on Meta's chat count.

**Change 2 — only if junk is still above 15% after Change 1.**
- Limit location to the 19 CCFS cities.
- This trades away genuine smaller-town directors, which is why it is second.

**Not a Meta change; for the SalesIQ project:**
- Have the Annual Filings bot ask "Are you a director or partner of a company or LLP?" (Yes/No) before handing the chat to an RM.
- This stops junk reaching the sales team without cutting reach.
- Owned by the SalesIQ project. Not touched here.

**Options for Sanjeev, not recommended by default:**
- **Male only.** Possible as a hard limit only by switching Advantage+ audience off (the CCFS model). It cuts genuine women directors.
- **Exclude past junk numbers.** Upload Lost "Inquired by Mistake" and "Job Seeker" numbers as a custom audience and exclude it. This is a hard limit and Advantage+ can stay on, but the effect is small.

## 7. Next checks

- **17 Oct:** placement stop-loss read for 14–16 Oct, on campaign and ad-set cost per valid.
- **Ads Manager:** preview each WhatsApp ad in Feed, Reels and Stories, and confirm which placements carry the custom message (section 5).
