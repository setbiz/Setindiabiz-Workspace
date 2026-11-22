# Consolidated Goldfish review: Google relaunch plan v1 (Trademark + Annual Filing), 22 Nov 2026

Reviewers: performance critic (PC), measurement skeptic (MS), budget CFO (CFO), compliance (CR), customer lens (CL). Individual reports are in this folder.
**Verdict: v1 is not approvable.** It has 7 Blockers across the reviews. The arithmetic is correct; the inputs, the kill rules and the build-sheet completeness are not.

## Elephant checks run after review (Zoho COQL, won deals closed 1 Nov 25–21 Nov 26)
| Service | Won ≤ threshold | Won > threshold | Reading |
|---|---|---|---|
| TM Filing in India (threshold ₹4,500) | 492 deals, avg ≈ ₹2,129 (Meta ads 34 of 36, avg ≈ ₹2,009; organic Google 232, avg ≈ ₹2,186) | 245 deals, avg ≈ ₹15,000 | A typical TM sale is fee-only ≈ ₹2,100. v1's ₹5,953 was inflated by larger deals → **break-even ≈ ₹1,050/won at 50% margin [calc]** |
| Annual Filing (threshold ₹9,000) | 254 organic avg ≈ ₹5,525; 36 Facebook avg ≈ ₹3,949 | 278 organic avg ≈ ₹22,982; 19 Facebook avg ≈ ₹25,075 | Half the deals sit in the package range. Conservative basis ≈ ₹5,500 → **break-even ≈ ₹2,750/won [calc]**; larger deals are upside |

## Themes and resolution proposed by the Elephant
| # | Theme | Findings | Proposed resolution in v2 |
|---|---|---|---|
| A | Unit economics overstated (govt fee / bundles in AOV; margin unconfirmed; targets assume ~10% lead→won) | CFO-1/2/3/4, MS-2, PC-1/2 | Rebase on ₹2,100 TM / ₹5,500 AF; owner confirms margin; targets = break-even × stated lead→won (3.7% baseline). At those numbers TM break-even CPL ≈ ₹39 → **park Trademark**; AF break-even CPL ≈ ₹102 (3.7%) to ₹220 (8%) |
| B | Attribution: no Zoho rule maps `utm_source=google`+`cpc` to `Advt - Google`; only gclid does; paid leads may land as `SEO - Google` | MS-1, PC-4, CFO-10, MS-7 | New launch gate: Zoho classifier rule for google+cpc ahead of the organic step (Zoho change, owner approval) + G4 test lead **without** gclid. Define the lead→deal link for UTM_Campaign |
| C | Kill rules looser than break-even; no won-based gate for AF before 31 Jan; 0-won case undefined | MS-3/4/5, PC-3, CFO-6/7/8 | Thresholds = 2× target CPL at day 7, 1.5× at day 14; QL-based gate on 15 Dec; won/QL gate on 30 Dec; January only on fresh owner approval |
| D | Keywords not listed; due-date group is research intent; no shared negatives; 40% junk tolerance | PC-5/6, CR-8 | Full keyword list in §9; due-date group dropped or capped at ₹40; shared list `GADS_Neg_Domestic` (Dec-25 junk + MCA portal terms: mca portal, mca login, mca.gov.in, v3 login); junk tolerance ≤ 15%; daily search-term review days 1–3 |
| E | Copy: trust 3/5 on all ads; partial-price lines; deadline wording; audit not mentioned; jargon | CL-1…9, CR-2/3/5/6/7/10 | Rewrite the AF ads and patch the TM callouts: every price line "+ GST + ROC/Govt fee"; pinned disclaimer + offer combined; proof point "Offices in 4 Indian Cities"; "Accounts must be audited first"; FY-specific GC 05/2026 wording; pause AOC-4 deadline assets 30 Dec 23:59 |
| F | Website fixes cited as mitigations but not gates (portal link, strike-through prices, ₹1,999 vs ₹2,000; LP "Licensed TM Attorneys") | CR-4, CR-9, CL-10 | Gate G5: W3/W4/W5 live; add the LP "Licensed TM Attorneys" fix to the website request |
| G | Budget mechanics: 29 days not 28; 2× daily overspend; 2-week funding ₹39k not ₹30–35k; "monthly" mislabel | MS-11, PC-10, CFO-5/11/12 | Correct the figures; fund prepaid in tranches tied to checkpoints; end dates on every campaign |
| H | Ad schedule 09:00–19:00 vs desk 09:30–18:30; justified with Meta data | MS-9, PC-9, CL-10 | Mon–Sat 09:30–18:30; drop "Today" from the CTA |
| I | Cannibalisation of organic Google (852 won/yr) | PC-8, CFO-10 | 8-week `SEO - Google` baseline for AF; total Google-sourced won is the guard metric; no bidding on terms where the site ranks top 3 (Search Console check) |
| J | Factual fixes in plan text | MS-6 (GA4 counting not yet synced), MS-12 (84 leads span 12 months; 76 Dec–Jan), CR-8 ("passed review" is false for AF), CR-1 (verbatim copy missing) | Correct the wording; paste the verbatim copy of every ad into §9 |

Elephant note on CR-1: the account read-back on 22 Nov confirms the TM ads no longer contain "Free TM Search", "18,000+" or "Attorney-Drafted", and every AF ad carries "not affiliated with MCA" (as the last description, **not pinned**). The finding stands: the plan must carry the copy verbatim, and the AF disclaimer should be pinned.

## Decisions for the owner (needed before v2)
| # | Decision | Elephant recommendation |
|---|---|---|
| R1 | Scope: Annual Filing only now; Trademark stays paused until GCLID + attribution are live and AF has read out | **Annual Filing only** |
| R2 | Gross margin on professional fees for Annual Filing (and TM) | Owner to state the % |
| R3 | Launch gates: Zoho google+cpc rule, W1 (GCLID) and W3–W5 live before enabling | Require the Zoho rule + W3–W5; W1 strongly preferred |
| R4 | AF budget ₹1,000/day to 30 Dec (≤ ₹38k incl. 2× days), January by fresh approval | Yes |
| R5 | Due Date Searches ad group | Drop for now |
| R6 | Named sales owner + 2-working-hour call-back | Owner to name |
