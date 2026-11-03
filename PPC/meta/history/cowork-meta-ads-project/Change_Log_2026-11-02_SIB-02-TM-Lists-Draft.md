# Change Log, 2 Nov 2026: Trademark list ad set draft and audience files

**Status:** published by Sanjeev on 2 Nov, about 10:42 IST. Read-back: interest Rs 1,000/day, list Rs 3,000/day, male 25-45, 8 cities, Advantage+ audience off on both, all 22 lists on the list ad set, no drafts left. Delivery was In review at the read-back. Meta added `frequently_in` to both ad sets, so location is frequently in, home and recent, not home and recent as drafted. Rs 25,000 was added on 2 Nov at 08:26 (about Rs 21.2k ad credit, per the 2 Nov watch log).
**Decided by:** Sanjeev Kumar, 2 Nov 2026: 24x7; two ad sets; Male 25-45; Delhi, Mumbai, Pune, Ahmedabad, Noida, Gurugram, Bangalore, Hyderabad; interest Rs 1,000/day; list Rs 3,000/day (revised the same day from Rs 500 and Rs 2,500).

## Draft changes in Ads Manager (campaign SIB-02 Trademark - Copy, 120247094837400449)

| Object | ID | Before | After (draft) |
|---|---|---|---|
| Ad set `SIB-02 \| TM \| Lists \| Form` | 120247318106490449 | Did not exist | Rs 3,000/day, 24x7, no end date |
| Ad `TM-F1 \| Rs1999 + GST \| Form \| Lists` | 120247318110350449 | Did not exist | Reuses creative 1414111734270603, form Trademark V2 1079618781060482 |
| Ad set `SIB-02 \| TM \| Form \| IN - Copy` | 120247094867020449 | Rs 1,200/day; male; age suggestion 25-55; 30 cities; home, recent, frequently_in; Advantage+ audience on; geo automation on | Rs 1,000/day; male 25-45 hard; 8 cities; home, recent; Advantage+ audience off (advertiser request, 2 Nov); interests and placements unchanged (draft; live values unchanged until publish) |

List ad set targeting: Male, 25-45 (hard); 8 cities at 25-mile radius, home and recent; English locales 6 and 24; Feed, Stories and Reels on Facebook and Instagram; Advantage+ audience off (reason: delivers only to customer lists); relaxation off; OFFSITE_CONVERSIONS on LEAD, website and lead form, same as the interest ad set.

Audiences (22): Company Director 2019-20 to 2026-27 (8); LLP 2019-20 to 2025-26 (7); GST 2025-26, GST 2026-27, GST Company, LLP, Firm, Proprietorship, Other Business Types (7). LLP 2026-27 to be added once created.

Read-back on 2 Nov: all three drafts show `active_errors: []`.

Meta message on the interest ad set: targeting_optimization has been removed and Advantage detailed targeting will be applied. Interests may therefore widen; gender, age and cities are hard limits. Publishing changes budget, audience and cities together on an ad set that had exited learning, so expect it back in learning.

## Audience files

Saved to `Raw Data\Meta Upload Files\2026-11-02\` (contains personal data; columns: email, phone, fn, ln, country).

| File | People | Use in Ads Manager |
|---|---|---|
| Add_to_Company_Director_2026-27.csv | 126,939 | Add customers to Company Director 2026-27 |
| New_List_LLP_2026-27.csv | 107,339 | Create new customer list LLP 2026-27 |
| Add_to_GST_2026-27_part1of2.csv | 327,425 | Add customers to GST 2026-27 |
| Add_to_GST_2026-27_part2of2.csv | 327,425 | Add customers to GST 2026-27 |

Use Add customers, not Replace. The files do not hold the earlier uploaded rows, so Replace would shrink the lists.

Cleaning: entity type taken from the CIN or LLPIN, not the folder. Removed nominees, non-individual subscribers and overseas directors. GST: removed cancelled and suspended registrations, tax deductors and government bodies. A phone or email on 6 or more entities was treated as a consultant's and removed: MCA 310 phones and 294 emails; GST 1,485 phones and 12,779 emails. PAN, DIN, date of birth, gender and address are not in the files.

Known gaps: Company and LLP data for 4-30 June, 1-6 July and 17-31 July, and anything after about 29 October.

## Stop-loss

- Keep the list ad set if rejected is 20% or less of worked leads.
- Pause if rejected is above 30%, or 0 CRM leads after Rs 2,000.
- Compare CRM cost per valid lead with the interest ad set after 7 running days.
- Real call-log connectivity check after 14 days.

## Open items

- Next top-up by Sanjeev: credit runs out around 3-4 Nov. Budgets become Rs 15,000/day after publish. Rs 4,000/day of Trademark ads is Rs 4,720/day with 18% GST.
- WhatsApp drafts discarded on 2 Nov on Sanjeev's instruction: `SIB-02 | TM | WhatsApp | IN` (120247099920320449, ad 120247099921540449) and `C1 - INC | WhatsApp | IN` (120247062226170449, ad 120247062314820449). Rebuild if WhatsApp ads are wanted later.
- LLP 2026-27: Sanjeev will create it later; add it to the list ad set then.
- GST upload files may be unnecessary if the five GST lists created on 31 Oct already include data to October.
- Older lists not re-uploaded: the Meta API shows LLP 2024-25 as delivery ACTIVE, status Normal; the meaning of the Outdated label is unverified.
- The creative's legacy body field carries older text ("25,000+ brands"); the served message field carries the current copy. Check the preview before publish.

## Marked for deletion (2 Nov 2026; nothing deleted yet)

Sanjeev chose delete over archive on 2 Nov. Trademark is published. A connector delete of #IND5 staged as a draft and failed with error 2446289 (broken reel), so that draft was discarded. Delete must be done by Sanjeev in Ads Manager: Claude does not click a permanent delete. Claude only ticked the rows; Sanjeev clicked Delete on the campaigns, ad sets and ads in Ads Manager on 2 Nov. Status at 11:03 IST: 4 campaigns remain (SIB-02 - Copy, SIB-04, SIB-05, #IND 1), the Ads tab shows the 15 kept ads, and Meta's delete job was at 14 of 21. Ad sets and ads still being processed show as ARCHIVED through the connector. Deleting a campaign removes its ad sets and ads. Lifetime record saved in `Deleted_Items_Snapshot_2026-11-02.md`.

| Level | Name | ID | State | Lifetime spend | Reason |
|---|---|---|---|---|---|
| Campaign | #IND3 - Trademark | 120243118117990449 | Paused, ended 31 Oct | Rs 1,74,008 | Replaced by SIB-02. Restart ad set spent Rs 0. Ad sets cannot be edited (error 2446289). 3 ad sets, 9 ads |
| Campaign | #IND4 - CCFS | 120244101705120449 | Paused, ended 8 Sep | Rs 2,96,730 | Scheme closed 15 Sep 2026 (MCA General Circular 04/2026). 1 ad set, 4 ads |
| Campaign | #IND5 - DPIIT | 120244221065970449 | Paused, ended 31 Jul | Rs 48,815 | Standing pause since 14 Jul (not converting as sales). 1 ad set, 4 ads |
| Ad set | C1 - Daytime INSA Company INC | 120242110677990449 | Paused 15 Oct | Rs 1,93,342 | 24Hr INSA did better. 2 ads |
| Ad set | C1 - Daytime - LAL1% Director - Company INC | 120242110744990449 | Paused 9 Jul | Rs 1,09,638 | Worst Incorporation ad set. 1 ad |
| Ad set | C1 - 24Hr LAL1% Director - Company INC | 120240924480770449 | Paused 9 Jul | Rs 55,890 | LAL lost to INSA on cost and quality. 1 ad |
| Ad | Ad-1 Lead - Company Registration (in C1 - 24Hr INSA) | 120240912969650449 | Paused | Rs 1,06,042 | Replaced by Ad-2 |

Total removed: 3 campaigns, 8 ad sets, 22 ads. Left: 4 campaigns, 7 ad sets plus the new list ad set, 14 ads plus the new ad.

Not marked: every delivering ad, including low-spend ones (ACR-C5 CTWA Rs 0, ACR-C1 Form Rs 123, SIB-05 S2 Rs 131); review with those campaigns. 47 campaigns are already archived and need no action.

How long Meta keeps deleted items in reports is unverified. CRM lead history does not depend on the Meta objects.

## Names and SIB-04 (2 Nov, about 11:15 IST)

Renames staged as drafts on Sanjeev's instruction ("Properly name campaign, adsets and ads"), read back with no errors, not published:

| Level | ID | Old name | New name |
|---|---|---|---|
| Campaign | 120247094837400449 | SIB-02 Trademark - Copy | SIB-02 Trademark |
| Campaign | 120240912969660449 | #IND 1 — Incorporation | SIB-01 Incorporation |
| Ad set | 120247094867020449 | SIB-02 \| TM \| Form \| IN - Copy | SIB-02 \| TM \| Interest \| Form \| 8C |
| Ad set | 120247318106490449 | SIB-02 \| TM \| Lists \| Form | SIB-02 \| TM \| Lists \| Form \| 8C |
| Ad set | 120240912969640449 | C1 - 24Hr INSA Company INC | SIB-01 \| INC \| Interest \| Form \| 18C |
| Ad | 120247094910200449 | TM-F1 \| Rs1999 + GST \| Form - Copy | TM-F1 \| Rs1999 + GST \| Form \| Interest |
| Ad | 120245819836760449 | Ad-2 Lead - Company Registration | INC-F1 \| Rs2499 + GST \| Form |

The SIB-04 and SIB-05 prefixes stay: the CRM assignment rule and the SalesIQ plug key on them. New leads will carry the new names in Meta_Campaign, Meta_Ad_Set and Meta_Ad_Name; old leads keep the old ones.

**SIB-04 legal stop triggered.** MCA General Circular 05/2026 of 24 Oct 2026 (MCA PDF read in Chrome on 2 Nov) allows FY 2025-26 AOC-4 to be filed by 31 Dec 2026 and MGT-7/7A by 31 Jan 2027 without additional fee. Paragraph 4 as reported: miss those dates and the fee runs from the original due date. It does not extend statutory due dates or AGM time. All 6 live SIB-04 ads still state Rs 100 a day, and four quote the 30 Oct date. The build spec's legal stop and 31 Oct date switch both apply. Pausing needs Sanjeev's go.

GST - Company (120247294345340449) has NOT been added to SIB-04 yet: held until the pause decision and the meaning of "similar fixes" (25-45 and 8 cities, or keep 25-60 and 19 cities) are settled.

## SIB-04 paused (2 Nov, about 11:40 IST)

Sanjeev: "we pause to resume later". Campaign SIB-04 Annual Filings (120246968311680449) set to PAUSED through the connector. This applied live, not as a draft. Read-back: campaign PAUSED, both ad sets CAMPAIGN_PAUSED. Before: ACTIVE. Budgets now total Rs 10,500/day of ad spend.

To resume SIB-04:
1. Confirm General Circular 05/2026 on the MCA site.
2. Write new text for Sanjeev's approval and a new-image brief for Vipin (FY 2025-26 relief to 31 Dec and 31 Jan; earlier years still attract the fee; no 30 Oct date).
3. Sanjeev answers: 25-60 and 19 cities, or 25-45 and 8 cities.
4. Add GST - Company (120247294345340449) to both ad sets, set the WhatsApp ad set's location types to home and recent, and rename both ad sets.
5. Sanjeev publishes and switches the campaign on.

Still open: 7 rename drafts unpublished; the delete job in Sanjeev's Chrome showed 14 of 21 at 11:35; 2 #IND3 ad sets and some ads still read ARCHIVED through the connector.

## Update, 2 Nov about 12:40 IST

- General Circular 05/2026 confirmed from the MCA PDF: paras 2 to 4 as noted in `SIB-04_Copy_Refresh_2026-11-02.md`.
- Delete job ended short. Ads Manager showed 27 ads, not 15. 17 leftover ads were ticked again in Sanjeev's Chrome for him to delete. Campaign list shows 4; live ad-set list shows 8.
- 7 rename drafts still unpublished.
- New SIB-04 text and Vipin's brief drafted in `SIB-04_Copy_Refresh_2026-11-02.md`, awaiting approval.

## Update, 2 Nov about 12:45 IST

Sanjeev approved the SIB-04 text ("Yes approved", 12:41). He did not separately answer age and cities; the recommended setting was used and flagged to him.

Drafts staged, read back with no errors, not published, campaign still paused:

| Ad set | ID | Before | After |
|---|---|---|---|
| SIB-04 WhatsApp | 120247072309210449 | SIB-04 \| ACR \| Directors \| WhatsApp \| 19C; 7 Director lists; frequently in, home, recent | SIB-04 \| ACR \| Directors + GST Co \| WhatsApp \| 19C; 7 Director lists + GST - Company; home, recent |
| SIB-04 Form | 120247072301790449 | SIB-04 \| ACR \| Directors \| Form \| 19C; 7 Director lists; home, recent | SIB-04 \| ACR \| Directors + GST Co \| Form \| 19C; 7 Director lists + GST - Company; home, recent |

Unchanged: men 25-60, 19 cities, Advantage+ audience off, relaxation 0/0, English, Feed, Stories and Reels.

Waiting on Sanjeev: delete the 17 ticked ads; publish (now 9 drafts); send Vipin the image brief. Trademark: at 12:45 Ads Manager showed the interest ad as Preparing, with Rs 23 spent today and Rs 0 on the list ad set.

## Update, 2 Nov: leftover ads cannot be deleted from Ads Manager

Sanjeev's bin showed: "This selection includes an ad that can only be deleted on your Page."

Tested by hovering the bin; nothing was clicked or changed:

| Selection | Bin |
|---|---|
| Group A, #IND3, 8 ads | Disabled, same message |
| Group B, #IND 1, 4 ads | Disabled, same message |
| Group C, CCFS and DPIIT, 5 ads | Disabled, same message |
| One archived ad alone, #C3A TM Ad 2 | Disabled, same message |
| One live ad alone, TM-F1 Lists (control) | Enabled, "Delete" |

The Meta connector reads all 17 as ARCHIVED. Meta's status documentation allows an archived object to change only its name or move to DELETED, so they cannot be switched back on. The message's cause is not confirmed; no Meta document on it was found.

Decision needed: none to protect spend. The 17 ads can stay archived, or Sanjeev can try the Page route. The lifetime record is in Deleted_Items_Snapshot_2026-11-02.md.

## Update, 2 Nov 13:10 IST: SIB-04 image brief emailed to Vipin

Sanjeev's instruction: "u send vipin image request" (13:09). Sent from one@setindiabiz.com to vipin.pathak@hatrotech.com, cc sanjeev@setindiabiz.com. Subject "SIB-04 Annual Filings: 3 new ad images (1:1 and 9:16), needed ASAP". Gmail message 1a19b338c49ecf2b, thread 1a19b338c49ecf2b.

Content: the brief in SIB-04_Copy_Refresh_2026-11-02.md for ACR-C6, C7 and C8, plus new copies only, the 9:16 text limits used for SIB-05 (y = 269 to 1,248 px), and no "due date extended" wording. Six images in all. Review every on-image word against the brief before building.

## Update, 2 Nov about 16:50 IST: SIB-04 image review

Vipin replied 15:45 IST (Gmail 1a19bc18e28d965d): 1:1 DAHZwesJnE4, 9:16 DAHZwRlAiJ8, 3 pages each, correct sizes. Originals not edited. Page 1 = ACR-C7, page 2 = ACR-C6, page 3 = ACR-C8.

Verdict: not clear to build. Passed: dates, circular number, bars and footnote, C7 footer, layout, 9:16 limits on pages 2 and 3. Failed: "due" and "on time" language, which treats the relief dates as statutory due dates (Sec. 137(1) and Sec. 92(4), Companies Act, 2013; General Circular 05/2026, paras 3 and 4); C7 shows Rs 7,499 a year with no turnover limit and against the approved "quote by year" text; C8 footer lacks government fees and the not-affiliated line; 9:16 C8 footer has a semicolon; 9:16 C7 footer ends about 5 px past 1,248 (measured on a 335 px preview, so approximate). C7 and C8 footer gaps came from our brief.

The AI disclosure is a Meta ad setting, not image text, so no image change is needed. Set it when building ACR-C8. On 9 Oct Ads Manager had no such control for the WhatsApp ad.

Fix list saved as a Gmail draft on thread 1a19b338c49ecf2b, not sent. New on-image text needs Sanjeev's OK.
