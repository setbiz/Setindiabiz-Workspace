# SIB-05 India Entry: G12 build sheet (prepared 16 Oct 2026, ~15:00 IST; decisions recorded 14:58)

**Status: prepared, not built.** Nothing in Meta has been created or changed. G12 runs only on Sanjeev's explicit go, after G11 (images) is clear and G9 (test leads) has passed. G13 (publish) is Sanjeev's, after the account is funded.

Sources for every value below: spec v5 §3 (`SIB-05_India_Entry_Build_Spec_2026-10-10.md`), approved copy §4 (`SIB-05_G11_Creative_Copy_and_Claims_Review_2026-10-12.md`), decisions D16, D21–D31, and read-only connector reads on 16 Oct (pages, Instagram account, live ad sets SIB-04 Form 120246968737470449 and SIB-02 Form 120247048085540449). Copy in §4 checked word for word against the claims review §4 on 16 Oct.

## 1. Decisions (Sanjeev, 16 Oct 14:58: "agree to all four")

| # | Decision | Recorded as | Why |
|---|---|---|---|
| B1 → **D28** | **Build route** | **Campaign through the connector; ad sets and ads in Ads Manager in Sanjeev's own Chrome (Claude in Chrome), as SIB-04 was built on 9 Oct.** Everything read back through the connector. Sanjeev's Chrome with the Claude extension must be open and logged in to Meta for the build | The connector's creative tool has no lead-form field, so it cannot attach form 4073050519663550 to a creative that uses separate 4:5 and 9:16 images; API writes to lead ads have failed with error 1815089 (Lead Ads terms) since July, and the connector still reads `leadgen_tos_accepted = false` for both Pages (16 Oct); on 15 Oct the #IND1 lead ads (one just edited from Claude's built-in browser) showed the same terms error, while SIB-04's form ads built in Sanjeev's Chrome run clean |
| B2 → **D29** | **9:16 not ready** | **Wait for Vipin's 9:16 re-layout**; no feeds-only launch | G9 and funding are also open, so waiting costs nothing today |
| B3 → **D30** | **AI disclosure** ("Ad includes media created or edited with AI") | **Tick it on all six ads if the photos were made or edited with AI.** Default if Sanjeev does not say otherwise: tick it (the scenes look AI-composited, and SIB-04 ACR-C5 set the same precedent) | Meta applies the label where rules require it, which per Meta's tool notes includes California and New York, both inside the US targeting. It must be set when the ad is built |
| B4 → **D31** | **End date** | **30 days after publish**, set on the publish date | So the 30-day test cannot run on by accident |

## 2. Campaign (connector, draft)

| Field | Value |
|---|---|
| Name | SIB-05 India Entry |
| Objective | OUTCOME_LEADS |
| Buying type | AUCTION |
| Special ad categories | none |
| Budget | **Campaign budget (CBO) ₹4,000 a day** = 400000 (paise). GST 18% is charged on top by Meta. (D1) |
| Bid strategy | LOWEST_COST_WITHOUT_CAP (highest volume) |
| Status | Draft, then set **PAUSED** in the draft and read back (connector stages new objects as ACTIVE; see SIB-04 C40) |

## 3. Ad sets (Ads Manager, Sanjeev's Chrome), three, identical except name and ads

| Field | Value | Why |
|---|---|---|
| Names | `SIB-05 \| India Entry \| Form \| INTL` (E1, E2) · `SIB-05 \| Subsidiary \| Form \| INTL` (S1, S2) · `SIB-05 \| Branch-Liaison \| Form \| INTL` (B1, B2) | Spec §3; "SIB-05" prefix drives reporting |
| Conversion location | Instant forms | |
| Performance goal | Maximise number of leads (LEAD_GENERATION) | Spec §3. Later option, not now: Conversion leads (QUALITY_LEAD) once Meta's CRM integration is set up, per the June CAPI runbook |
| Form | **SIB-05 India Entry Form v1, 4073050519663550** | G7 |
| Page / Instagram | Setindiabiz Private Limited **627814417091714** / **setindiabiz_official 17841473603642746** | Connector read 16 Oct |
| Locations (hard) | United States, United Arab Emirates, Singapore, South Korea, Japan, Australia, Canada. "People living in or recently in". **No location expansion** (SIB-02 has `individual_setting.geo = 1`; do not copy it) | D16 |
| Minimum age (hard) | **25** under Audience controls (not just a suggestion; SIB-04 C42 note) | D26 |
| Languages (hard) | **English (US), English (UK), Japanese, Korean**. Keys 6 and 24 confirmed from Meta's docs; Japanese and Korean picked by name in Ads Manager, then keys read back through the connector. If Korean is not offered, stop and ask Sanjeev | D26; prep log 16 Oct |
| Advantage+ audience | On, with suggestions below | Spec §3 |
| Audience suggestions | Job titles: Founder, Chief executive officer, Managing Director, Chief financial officer, Owner, Partner, Managing Partner, Chairman, Vice President, plus India Desk titles searchable by name (Country Manager, Head of International, General Counsel, Finance Director, Head of Legal). Interests: Foreign direct investment, Doing business in India, International business, Global expansion, Subsidiary, Joint venture (search by name), plus Senior management, Board of directors, Investment, Trade. Industry: Business Decision Makers. Behaviours: Small business owners, Facebook Page admins | Saved audience SAV-10 (India Desk). IDs already used in the account: CEO 103113219728224, CFO 112558655421889, Founder 849873341726582, Managing Director 874842615892965, Owner 110722838955052, Partner 108731319151154, Managing Partner 143212149039647, Chairman 108616345829139, Vice President 112451425436956; Business Decision Makers 6262428231783; Small business owners 6002714898572; Facebook Page admins 6015683810783 |
| Placements | Advantage+ placements limited to **Facebook and Instagram** only: no Threads, Messenger or Audience Network. Account-level controls already exclude Audience Network, Marketplace and right column; do not add them back | Spec §3; SIB-02 includes Threads, so do not copy SIB-02 here |
| Budget | none at ad-set level (CBO) | |
| Schedule | Start on publish; **end 30 days after publish** (D31) | |
| Status | Saved unpublished; **each ad set PAUSED in the draft** | 12:45 prompt |

## 4. Ads (Ads Manager), six, two per ad set

Common settings for every ad:
- Format: single image, **placement asset customisation**: 4:5 image for Feeds, Explore and profile/search; 9:16 image for Stories and Reels.
- CTA button: **Get quote**. Form 4073050519663550.
- Identity: Page 627814417091714, Instagram setindiabiz_official (the API left this blank on SIB-04; check it is set).
- Advantage+ creative: **all enhancements off** (0 of 5 and 0 of 3), music off, translation off, AI text/image/video generation off, "show summary"/interactive experiences off, multi-advertiser ads off.
- Lead nurture follow-up channels: **Messenger and Instagram unticked** (WhatsApp stays as the form's completion button, D22).
- AI disclosure: **ticked** per D30, unless Sanjeev says the photos are not AI-made or AI-edited.
- Text exactly as below (claims review §4, approved 13 Oct). Any change goes back to Sanjeev.

| Ad | Ad set | 4:5 image | 9:16 image | Headline | Description |
|---|---|---|---|---|---|
| E1 `SIB-05 \| E1 \| India entry \| Form` | India Entry | DAHX_Sw46n4 p1 | 9:16 p1 | Set up your business in India | Subsidiary, branch or liaison office |
| E2 `SIB-05 \| E2 \| Structures \| Form` | India Entry | p2 | p2 | Which India structure fits you? | Compare the three routes |
| S1 `SIB-05 \| S1 \| From USD 499 \| Form` | Subsidiary | p3 | p3 | Indian subsidiary from USD 499 | Government fees extra, at cost |
| S2 `SIB-05 \| S2 \| After incorporation \| Form` | Subsidiary | p4 | p4 | Your India compliance, one contact | Incorporation, FEMA and annual filings |
| B1 `SIB-05 \| B1 \| Liaison office \| Form` | Branch-Liaison | p5 | p5 | Open a liaison office in India | 3 years' profits, USD 50,000 net worth |
| B2 `SIB-05 \| B2 \| Branch office \| Form` | Branch-Liaison | p6 | p6 | Open a branch office in India | 5 years' profits, USD 100,000 net worth |

**Primary text (word for word):**

E1: Planning to set up in India? We help foreign companies choose between an Indian subsidiary, a branch office and a liaison office, then handle the filings with the Registrar of Companies and the reporting under India's foreign exchange rules (FEMA). Setindiabiz has served 25,000+ businesses from offices in Delhi, Noida, Mumbai, Bengaluru and Hyderabad. Answer three short questions and our India-entry team will contact you.

E2: Subsidiary, branch office or liaison office? A subsidiary is an Indian company. A branch office generally needs a profit-making record over the last five financial years and net worth of at least USD 100,000. A liaison office generally needs a three-year profit-making record and net worth of at least USD 50,000; it cannot carry on business in India and is funded from abroad. Tell us your plans and we will suggest the route that fits.

S1: Set up your Indian subsidiary from USD 499. The fee covers consultation and our services up to the Certificate of Incorporation. Government fees, stamp duty and digital signature costs are extra, billed at actual cost. Registered office and a resident director are arranged separately. We check your sector's foreign investment route and conditions first.

S2: Incorporation is the first step. A foreign-owned Indian company reports each issue of shares to its foreign investor on Form FC-GPR within 30 days of the issue, then files its accounts and annual return with the Registrar of Companies every year. Setindiabiz handles incorporation and the compliance that follows, with one point of contact.

B1: Want a presence in India before you trade? A liaison office can represent your company and promote trade and technical or financial collaboration with Indian businesses. It cannot carry on business in India and is funded from abroad. Eligibility: generally a profit-making record over the last three financial years and net worth of at least USD 50,000. We prepare the application, which is filed through an authorised bank in India.

B2: A branch office lets your company carry out the activities the RBI permits for branches in India. Eligibility: generally a profit-making record over the last five financial years and net worth of at least USD 100,000. Applicants in some sectors and from some countries need prior RBI approval. We check eligibility and prepare the application.

## 5. Build order (on go only)

1. Export the 12 PNGs from Canva (4:5 at 1080×1350, 9:16 at 1080×1920) after Vipin's final save; check each export against §5 once more; save to `G:\My Drive\0. Claude Cowork\Meta Ads\SIB-05 Creatives` through the device bridge (Sanjeev's PC). No go needed for export.
2. Campaign through the connector (§2); set PAUSED in the draft; read back.
3. In Sanjeev's Chrome (Claude in Chrome; Sanjeev logs in if needed): three ad sets under that campaign (§3), each PAUSED.
4. Six ads (§4); upload the PNGs in Ads Manager.
5. Read back every object through the connector (`object_state=draft`): names, form ID, locales, age_min 25, countries, placements, copy word for word, enhancements opted out, Instagram identity, AI disclosure. Fix anything off before reporting.
6. Preview pack: every ad in Feed, Stories and Reels, sent to Sanjeev.
7. Hand over for G13. **Never click Publish, "Review and publish" or "Preview to publish".** Publishing may sweep other drafts in the account (the TM and INC WhatsApp drafts are PAUSED, so they cannot spend).

If a permission check refuses a step, leave the screen ready and hand that step to Sanjeev.

## 6. After publish (G13)

- Set the end date to 30 days after the publish date if Ads Manager did not keep it (D31).
- Claude reads back the live spec, then checks the first real leads against the G9 checklist (owner, Tag FB-FDI, Lead Channel, Product, Description, Select_Country, Meta_* fields, Lead_Source **not** "Meta Ads", booking email).
- Stop-loss and measurement per spec §8: capture stop (2 spend days, 0 CRM leads); day 7 country check (watch Japan and South Korea separately, D26) and frequency check; day 30 go/no-go on cost per qualified meeting. Legal stop on any change to Press Note 2 (2026) or the NDI Rules touching land-border investment.
