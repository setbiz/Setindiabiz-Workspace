# Campaign Plan: Google Ads · Company Annual Filing · Nov–Dec 2026 (APPROVED v2)

Status: **APPROVED by owner 23 Nov 2026 (A1–A3).** It resolves the Goldfish review (`consolidated_review_report.md`) with the owner's decisions of 23 Nov: R1 Annual Filing only; R3–R5 yes; margin 60%; Google leads are called within 2 hours by sales managers assigned by the CRM round-robin rule. Nothing is live. Campaign 24528891318 exists and is **PAUSED**.
Labels: [data] = from a connector (source and date given) · [calc] = arithmetic on [data] · [est] = estimate.

## 1. Objective
Win private-limited-company **annual filing (AOC-4, MGT-7/7A, ADT-1, annual compliance packs)** clients in India from Google Search, during the MCA GC 05/2026 no-additional-fee window. Success is judged on Zoho CRM won deals and revenue.
**Out of scope:** Trademark (24046453436) stays PAUSED. It is revisited only after GCLID capture and the Zoho attribution fix are live and this campaign has read out (break-even ≈ ₹1,260 per won deal at 60% margin is not achievable at current click costs [calc]).

## 2. Current state
- **Google, 1 Nov 2025 – 22 Nov 2026** [data: Supermetrics AW; Zoho COQL 22 Nov]: two Dec-25 campaigns (Trademark, Subsidiary) spent ₹99,927. `Advt - Google` produced 84 leads in that period, 76 of them created Dec 2025 – Jan 2026: 63 Lost, 18 never worked, 0 deals. No annual-filing campaign has run on this account in that period.
- **This campaign** [data: Supermetrics, 22 Nov]: Search only, partners off, presence geo India, en + hi, Maximize Clicks with an ₹80 CPC cap, ₹1,000/day, UTM suffix, 36 campaign negatives, 4 ad groups and 5 RSAs. All are in review: **not yet approved by Google**.
- **Conversion goal** [data: owner UI check, 22 Nov 22:40]: "Submit lead form" is the only account-default goal. GA4 `form_submission` is its only Primary action. The GA4 counting change to once per session was made on 22 Nov; the Google Ads sync to "One per click" is **not yet confirmed**.
- **Annual Filing won deals, closed 1 Nov 2025 – 21 Nov 2026** [data: Zoho COQL, 23 Nov; won = Won / W-* stages]:

| Source | Won ≤ ₹9,000 (package range) | Won > ₹9,000 |
|---|---|---|
| SEO – Google (organic) | 254 · avg ≈ ₹5,525 [calc] | 278 · avg ≈ ₹22,982 [calc] |
| Advt – Facebook | 36 · avg ≈ ₹3,949 [calc] | 19 · avg ≈ ₹25,075 [calc] |
| All sources | 1,251 deals, ₹1,90,96,393 in total | |

Caveat: whether `Amount` includes the ROC fee is unconfirmed (the ROC fee is ₹200–600 per form, so the effect is small). Lead_Source was migrated in 2026.

## 3. Approach and why it should work
- **Search, phrase and exact match only, India, people located there.** This fixes the Dec-25 failure, where broad match bought portal and research queries ([data] audit §2).
- **Maximize Clicks with an ₹80 CPC cap.** No conversion bidding until offline import exists and there are at least 30 CRM-qualified leads in 30 days.
- **Ad schedule Mon–Sat 09:00–18:00 IST.** This sits inside desk hours of 09:30–18:30 (`business-context.md`), and leads from 09:00–09:30 are called at opening. Google leads are assigned to sales managers by the CRM round-robin rule and called within 2 hours (owner, 23 Nov).
- **Copy:** every price line is complete ("+ GST + ROC fee"). The disclaimer and the offer share the pinned description 1. Proof point "Offices in 4 Indian Cities" (backed by addresses in `business-context.md`). "Accounts must be audited first" is stated. Statutory facts carry their provisions (§8).
- **Why this service:** it is the largest won category (₹1.91 cr from 1,251 deals in 12 months), organic Google already converts it (532 won), and demand peaks at the GC 05/2026 deadline (AOC-4 by 31 Dec 2026).

## 4. Unit economics (margin 60%: owner, 23 Nov)
| | Value |
|---|---|
| AOV basis (conservative: package-range deals, organic Google) | ₹5,525 [calc]. Larger deals are upside, not counted |
| Break-even cost per won deal = AOV × 60% | **₹3,315** [calc] |
| Target cost per won deal | **≤ ₹2,500** (≈ 75% of break-even) |
| Lead→won assumption | 3.7% (Facebook baseline [data]) to 8% [est] |
| Break-even CPL at 3.7% / 8% | ₹123 / ₹265 [calc] |
| **Target CPL (CRM lead)** | **≤ ₹200** [est: midpoint, to be replaced by actuals at day 14] |
| Target cost per QL (Valid Lead + Proposal) | ≤ ₹600 [est: assumes ≈ 1 in 3 leads qualify] |
| Expected CPC | ₹30–80 [est, no history] → at a 5% click→lead rate, CPL ≈ ₹600–1,600 [est]. **The plan only works if click→lead is ≥ 15–20%** or lead→won is well above 8%. The day-7 and day-14 gates test exactly this |

## 5. Budget and cap
- **₹1,000/day from launch to 30 Dec 2026, 23:59.** End date set on the campaign.
- Max spend if launched 1 Dec: 30 days × ₹1,000 = ₹30,000 planned. Google can spend up to 2× on a day but caps the month at 30.4 × daily, so **≤ ₹31,000 hard ceiling** [calc]. If launched earlier, add ₹1,000 per extra day.
- **January 2027 (MGT-7 window to 31 Jan) only with fresh owner approval** at the 30 Dec review.
- **Funding:** prepaid in tranches. Add ₹15,000 before launch (≈ 14 days), then ₹15,000 after the day-14 checkpoint passes. Balance today ≈ ₹4,630.

## 6. Measurement
- **Primary metric:** Zoho won deals and won ₹ for leads with `Lead_Source = Advt - Google` **or** (`UTM_Source = google` and `UTM_Medium = cpc`) with `UTM_Campaign = Search | Company Annual Filing | India`, created on or after launch. Deals are linked to their lead through lead conversion (Deal ← Contact ← converted Lead). The weekly cycle pulls deals through that link and does not rely on deal-level UTM.
- **Leading metrics:** CRM leads, QL rate, unworked %, CPC, junk share of search terms (§7).
- **Event:** GA4 `form_submission` (Primary). Platform conversions are diagnostic only.
- **Attribution fix (gate G4):** add a rule to the Zoho Lead Source classifier: `utm_source=google` and `utm_medium=cpc` → `Advt - Google`, evaluated before the organic `SEO - Google` step. It needs owner approval for the Zoho workflow change. Then test with one lead carrying no gclid.
- **GCLID (W1):** with the landing-page session. Launch does not wait for it, but no budget increase and no Trademark relaunch happen until it is live.
- **Reconciliation:** each Monday (`ppc-weekly-cycle`), Google form conversions vs Zoho leads by UTM_Campaign. A gap of more than 30% is investigated before any change.
- **Guard metric (cannibalisation):** weekly `SEO - Google` Annual Filing leads and won deals against the 8-week pre-launch baseline. If organic falls by more than 20% while paid rises, the owner reviews keyword overlap.

## 7. Launch gates and kill / scale rules (pre-registered)
**Gates (all required before enabling):**
G1 · All enabled ads approved by Google, with no government-documents disapproval.
G2 · Account funded with ≥ ₹15,000.
G3 · Round-robin assignment covers `Advt - Google` leads (owner confirmed 23 Nov). Unworked % is checked at day 7.
G4 · Zoho google+cpc rule live, and a test lead with no gclid lands as `Advt - Google` with UTM_Campaign filled.
G5 · Website fixes live on `/company-annual-return`: official-portal line with mca.gov.in link (W3); no strike-through prices on the page (W4).
G6 · Statutory facts in the copy re-checked on the day of launch: GC 05/2026 on mca.gov.in; Companies Act 2013 ss. 92, 137, 164(2)(a), 403; Companies (Registration Offices and Fees) Rules 2014 fee table.

**Rules (spend counted from launch):**
- **Day 3:** review search terms. Add negatives. Pause any keyword with more than ₹1,000 spend and 0 leads.
- **Day 7 or ₹7,000, whichever comes first:** pause if CRM leads < 5 (CPL > ₹1,400), or if more than 15% of spend went to junk terms after negatives (junk = any term containing the §9 negative tokens, or MCA-portal or research tokens: login, portal, due date, last date, format, pdf, status), or if unworked leads > 25%.
- **Day 14 or ₹14,000:** pause if CPL > ₹400 (2× target), or if QL < 25% of leads.
- **15 Dec:** pause if cost per QL > ₹1,200 (2× target).
- **30 Dec 23:59:** the campaign ends. Readout on 5 Jan (allowing a 7-day close lag): cost per won deal for leads created up to 30 Dec, closed up to 5 Jan. Continue into January (MGT-7 copy only) **only if** cost per won ≤ ₹3,315 and the owner approves.
- **AOC-4 deadline assets:** the ad group "ROC Annual Filing – GC 05/2026" is paused on **29 Dec 23:59**, because a lead after that can't be filed by 31 Dec.
- **Scale:** none in this phase. Budget stays at ₹1,000/day.
- **Any disapproval:** pause that ad and send the policy text to the owner. No re-appeals, and no consultation-only page (circumvention risk).

## 8. Risks
| Risk | Mitigation | Provision / policy (re-check at G6) |
|---|---|---|
| Account-level government-documents block. Annual Filing ads have never been approved on this account | G1. Ads stay paused until approved | Google Ads "Government documents and official services" (answer/13156083; answer/6368711), read 22 Nov 2026 |
| Implied government affiliation | Pinned D1 "Private firm, not affiliated with MCA"; callout; LP disclaimer + mca.gov.in link (G5); negatives for MCA-portal searches | Emblems and Names (Prevention of Improper Use) Act 1950 s. 3; CPA 2019 s. 2(28) |
| Price claims / drip pricing | Every price line ends "+ GST + ROC fee", matching `/company-annual-return` (Essential ₹4,599, Extended ₹5,999, Complete ₹7,999, single form from ₹2,999, ADT-1 ₹1,500; "GST & ROC Fee on Actual") [data: LP fetch 22 Nov] | CPA 2019 s. 2(28); CCPA Guidelines for Prevention of Misleading Advertisements 2022; CCPA Dark Patterns Guidelines 2023 (drip pricing) |
| Deadline claim | FY-specific wording citing GC 05/2026. States that older years still pay and AGM dates are not extended. Deadline ad group ends 29 Dec | MCA General Circular 05/2026 (24 Oct 2026), owner-verified 2 Nov; secondary sources agree (compliance report) |
| Late-fee and disqualification facts | ₹100/day per form | Companies Act 2013 s. 403 + Companies (Registration Offices and Fees) Rules 2014. Disqualification after 3 consecutive years' non-filing: s. 164(2)(a). Audited accounts precede AOC-4: s. 137 with ss. 129, 143 |
| ROC fee range ₹200–₹600 | Shown as a range by share capital, as on the LP | Companies (Registration Offices and Fees) Rules 2014, fee table (re-check) |
| "100% Online Process" callout | Owner confirmed fully online delivery (22 Nov, changelog) | ASCI Code Ch. I (substantiation) |
| Lead handling | Round robin + 2 h call (G3); schedule inside desk hours | — |
| Organic cannibalisation | §6 guard metric. No bidding on the brand | — |
| Personal data | No list uploads. Enhanced Conversions and offline import only after the privacy notice is updated (W6) | IT Act 2000 s. 43A + SPDI Rules 2011 r. 4–5 (in force); DPDP Act 2023 ss. 5, 6, 8 (phased, ≈ May 2027, verify) |

## 9. Build sheet (changes to campaign 24528891318; apply PAUSED, enable only after G1–G6 and owner OK)
**Campaign settings:** keep the name "Search | Company Annual Filing | India" (the UTM {campaign} value). End date **2026-12-30**. Budget ₹1,000/day. Maximize Clicks, CPC cap ₹80. Search only, partners off, PRESENCE, IN, en + hi. AI Max off; final URL expansion off. URL suffix unchanged. **Ad schedule:** Mon–Sat 09:00–18:00.
**Callouts (replace):** Private Professional Firm · AOC-4 Certification · CA/CS Expert Team · AGM Papers Included · 100% Online Process · Offices in 4 Indian Cities
**Shared negative list (new) `GADS_Neg_Domestic_202611`**, attached to this campaign, phrase match: mca portal · mca login · mca.gov.in · mca v3 · mca21 · v3 portal · due date · last date · extended date · format · sample · pdf · download · free · login · status check · challan · notes · course · job · salary · assignment · meaning · udyam · gst. The 36 campaign-level negatives stay.
**Ad groups**
1. **AOC-4 and MGT-7 Forms** (200646712965). Keywords (phrase): aoc 4 filing · aoc 4 filing fees · mgt 7 filing · mgt 7a filing · aoc 4 and mgt 7 · adt 1 filing. Rewrite RSA 832341096172:
   - H: AOC-4 & MGT-7 Filing Help · MGT-7 / MGT-7A Filing · Single Form Filing Available · ADT-1 ₹1,500 + GST + ROC Fee · Packs ₹4,599 + GST + ROC Fee · AOC-4 Certification Included · Offices in 4 Indian Cities · CA/CS Team Files for You · Avoid ₹100/Day Additional Fee · Private Professional Firm
   - D1 (pinned): Private firm, not affiliated with MCA. 1 form from ₹2,999 + GST + ROC fee.
   - D2: ROC fee ₹200-₹600 per form, based on share capital. GST applies on our fee.
   - D3: Accounts must be audited first. Audit is not in the price; ask us for a quote.
   - D4: Late filing attracts ₹100 per day per form. Our CA/CS team prepares and files.
   - Paths: aoc-4 / mgt-7.
2. **ROC Annual Filing** (202355735037). Keywords: roc filing (phrase + exact) · company annual filing · company annual return filing · roc annual filing · roc filing for pvt ltd company · roc filing fees · roc compliance (all phrase). Rewrite RSA 832341064927:
   - H: ROC Annual Filing for Pvt Ltd · AOC-4 & MGT-7 Filing Help · Packs ₹4,599 + GST + ROC Fee · AGM Papers Included · AOC-4 Certification Included · Company Annual Return Filing · Offices in 4 Indian Cities · CA/CS Team Files for You · Keep Directors Qualified · Avoid ₹100/Day Additional Fee · Private Professional Firm
   - D1 (pinned): Private firm, not affiliated with MCA. Packs from ₹4,599 + GST + ROC fee.
   - D2: Essential pack: AGM papers, AOC-4 and MGT-7/7A. Accounts must be audited first.
   - D3: Not filing for 3 years in a row can disqualify directors for 5 years. File on time.
   - D4: ROC fee ₹200-₹600 per form, based on share capital. GST applies on our fee.
   - Paths: roc / annual-filing.
   - **Move RSA 832341064930 (deadline copy) out:** remove it from this group and rebuild it in group 4.
3. **Annual Compliance** (204780133080). Keywords (phrase): annual compliance for private limited company · annual compliance of private limited company · private limited company compliance · pvt ltd annual compliance · company compliance services. Rewrite RSA 832341064945:
   - H: Pvt Ltd Annual Compliance · Annual Compliance Packs · Packs ₹4,599 + GST + ROC Fee · AGM Papers + AOC-4 + MGT-7 · Complete Pack With Company ITR · AOC-4 Certification Included · Offices in 4 Indian Cities · CA/CS Team Files for You · Private Professional Firm
   - D1 (pinned): Private firm, not affiliated with MCA. Packs from ₹4,599 + GST + ROC fee.
   - D2: Essential ₹4,599, Extended ₹5,999, Complete ₹7,999 with company ITR. GST, ROC fee extra.
   - D3: Accounts must be audited first. Accounting and audit are not in the packs.
   - D4: Not filing for 3 years in a row can disqualify directors for 5 years. File on time.
   - Paths: annual / compliance.
4. **ROC Annual Filing – GC 05/2026** (new; same keywords as group 2; paused 29 Dec 23:59). New RSA:
   - H: FY25-26 AOC-4: No Extra Fee · FY25-26 MGT-7: No Extra Fee · ROC Annual Filing for Pvt Ltd · AOC-4 & MGT-7 Filing Help · Packs ₹4,599 + GST + ROC Fee · Offices in 4 Indian Cities · Private Professional Firm
   - D1 (pinned): Private firm, not affiliated with MCA. Packs from ₹4,599 + GST + ROC fee.
   - D2: MCA GC 05/2026: no extra fee for FY 2025-26 AOC-4 by 31 Dec 2026, MGT-7 by 31 Jan.
   - D3: Older years still pay ₹100 per day per form. AGM due dates are not extended.
   - D4: Accounts must be audited first. Audit is not in the price; ask us for a quote.
   - Paths: roc / fy-2025-26.
5. **Due Date Searches** (201017866703): **stays PAUSED** (R5). Its ad 832283615649 stays paused.

All final URLs are `https://www.setindiabiz.com/company-annual-return`. Character limits checked (headlines ≤ 30, descriptions ≤ 90). Note on approvals: rewriting the copy re-triggers Google review, so G1 applies to the new copy.

**Trademark 24046453436:** no change; stays PAUSED. Later fixes noted from the review: replace the callouts "Fee ₹1,999 + GST" → "₹1,999 + GST + Govt Fee" and "Filed Within 24 Hrs" → "Filed 24 Hrs After Docs". Fix the LP "Licensed TM Attorneys" claim (Trade Marks Act 1999 s. 145; Advocates Act 1961).

## 10. Review dates + changelog
- Day 3 (search terms), day 7, day 14, 15 Dec, 29 Dec (deadline group off), 30 Dec (end), 5 Jan 2027 (readout).
- On launch, log: "Enabled Annual Filing per `google-ads/campaigns/202611-gads-annual-filing.md`; approver owner; gates G1–G6 met (evidence links); review <launch + 7>".
- Each Monday the weekly cycle adds spend, CRM leads, QL, won and the rule outcome to `changelog.md`.

## Owner approvals requested
A1 · Approve this plan (v2) as the launch plan.
A2 · Approve applying §9 now (all PAUSED: copy rewrite, new group 4, shared negative list, schedule, end date) so Google can review the new copy while the gates are being met.
A3 · Approve the Zoho classifier change in §6 (google + cpc → `Advt - Google`).
