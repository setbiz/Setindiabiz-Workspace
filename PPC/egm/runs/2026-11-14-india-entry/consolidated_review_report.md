# Consolidated Goldfish review — India Entry plan v1 → v2 (14 Nov 2026)

Reviewers: performance critic, measurement skeptic, budget CFO, compliance reviewer and customer lens. Each ran in isolation; their full reports are in this folder. The totals in v1 were 9 Blockers, 42 Majors and 27 Minors, with heavy overlap between reviewers. Below are the distinct findings, what happened to each in v2, and where it lives in the v2 plan (§ numbers).

**Status:** Fixed = changed in v2. Owner = left for the owner to decide (§12). Rejected = finding didn't hold, with the evidence.

## Blockers
| # | Finding (reviewers) | Status | v2 change |
|---|---|---|---|
| B1 | Build sheet leaves decisions to whoever builds it: "brief to follow" copy, "copy SIB-05 targeting", Google cap method not chosen (perf, comp, cust) | Fixed | §9: verbatim copy for every live ad. Meta reuses approved B2/E2 copy and existing images. LinkedIn L1/L2 written. Full Meta targeting IDs listed. One cap mechanism per platform (§5). |
| B2 | Max loss not capped: K1 stops firing after 1 QL (meas, CFO, perf) | Fixed | §5 states the true max loss (≈ ₹1,80,800 = sum of caps). §7 K1/K2 now compare against break-even using spend ÷ (QL+1). |
| B3 | QL counted by current status, so conversion or "Lost" removes it (meas) | Fixed + Owner D5 | §6.1 "ever-QL" definition, with a `QL_Date` stamp. |
| B4 | Zoho mis-attribution: LinkedIn forms, UTM-only clicks, booking links (meas) | Fixed + Owner D5 | §6.2: LinkedIn static mapping, UTM fallback, booking-link procedure. |
| B5 | Website notice ("used only to respond") doesn't cover sending CRM data to ad platforms (comp) | Fixed + Owner D4 | §6.3 G-T 2: until the notice is fixed, offline import by click ID only and enhanced conversions off. |
| B6 | Returning-founder ads sent to a branch/liaison page (cust, perf) | Fixed | Google AG3 and Group B moved to phase 2, gated on LP (c). |

## Majors (merged)
| # | Finding | Status | v2 change |
|---|---|---|---|
| M1 | Google ₹1.2L vs ≈620 US searches/month; it can absorb ≈ ₹23–43k (CFO, perf) | Fixed | Google ₹1,500/day ≈ ₹45.6k. |
| M2 | ₹3L needs ≈5.8 extra wins a month; the whole line wins 1.7/month (CFO, perf) | Fixed | ₹1.8L committed, ₹1.2L in reserve released only under S1. |
| M3 | Spread too thin; ChatGPT/Reddit untested, with policy blocks (CFO, perf, meas) | Fixed | Phase 1 runs 4 platforms. ChatGPT and Reddit wait for the day-30 gate. One Meta ad set. |
| M4 | Allocation against evidence: Meta, the only US-QL platform, gets 15% (perf) | Fixed | Meta ₹60k = largest share, tied with LinkedIn. |
| M5 | 15% QL→won has no source; ₹44k price-only deals change break-even (CFO, meas) | Fixed + Owner D3 | §4 sensitivity table. |
| M6 | Small samples; S1 scales on 3 QL (meas, perf) | Fixed | S1 needs ≥ 5 QL plus a proposal, and the owner releases reserve manually. Small-sample note added. |
| M7 | Kill rules ignore unworked leads (meas, perf) | Fixed | §7: leads must be ≥ 3 working days old, and a checkpoint is deferred if more than 25% are unworked. |
| M8 | Google bid switch mid-test is ambiguous and resets learning (meas, perf) | Fixed | Manual CPC for the whole test; per-ad-group max CPC. |
| M9 | Meta CBO across two audiences + Advantage+ audience repeats SIB-05 drift (meas, perf) | Fixed | One ad set; ABO ₹2,000; Advantage+ audience off. |
| M10 | Price headline can serve without its exclusions; bait-ad risk; GST missing on the LP (comp, cust) | Fixed + Owner D2 | No price in ads in month 1. LP price text adds "GST extra where applicable". |
| M11 | Disclaimer pinned to headline 3 doesn't always show (comp, cust, perf) | Fixed | Disclaimer pinned to description position 1. |
| M12 | "Moving back to India?" implies national origin (Meta Personal Attributes) (comp) | Fixed | Neutral Group B framing, written for phase 2. No visa or layoff references. |
| M13 | "CS & CA-Led" goes beyond the evidence; naming practising members raises CA/CS Act concerns (comp) | Fixed | Approved "CS & CA Experts" wording only. LP check against ICAI/ICSI rules. |
| M14 | US buyers won't know the jargon: FC-GPR, AD bank, BO/LO, DSC (cust) | Fixed | Copy rewritten in plain words ("FDI Reporting to RBI", "authorised bank"). Glossary added to the LP. |
| M15 | No trust proof (cust) | Partly fixed | LP: offices, CIN, how US clients pay. Unevidenced claims stay out. |
| M16 | Holiday-season overlap; too many simultaneous changes (meas) | Fixed | Launch 1 Dec. Meta form v2 and Group B moved out. Seasonal note added. |
| M17 | No capture-rate threshold; SEO cannibalisation check can't detect anything (meas, perf) | Fixed | Capture threshold set at ≥ 90%. SEO check dropped (volume too low). Brand terms stay negative. |
| M18 | Google AG3 terms invite "business ideas" searches; Dec-25 search terms never pulled (perf) | Fixed | Negatives added; build step 0 pulls the Dec-25 search terms. |
| M19 | Microsoft rationale and settings vague; syndicated partners not excluded (perf) | Fixed | §9.4: manual CPC, owned-and-operated search network only. |
| M20 | LinkedIn: no evidence, company size doesn't match Microsoft (perf) | Fixed | Company size 51–1,000 on both. LinkedIn remains a test with kill rules. |
| M21 | "Work email" puts off Group B (cust) | Fixed | LP (c) asks for email, not work email. |

## Rejected (finding didn't hold)
| Finding | Evidence |
|---|---|
| "LinkedIn/X/Reddit connected contradicts the diagnosis" (meas M8, perf) | The owner connected them after the diagnosis. Supermetrics accounts_discovery on 14 Nov returns LIA 506114635, TA 18ce54c2t0g and RDA a2_h6g5l0mhl1xy. |
| "`Advt - LinkedIn` / `Advt - Reddit` / `Advt - ChatGPT` missing from Zoho" (meas, perf) | Zoho Leads `Lead_Source` picklist (getFields, 14 Nov) contains all three. |

## Minors folded in
- Placement waste corrected to ₹8,249.55.
- GST treatment stated.
- Caps are per 30-day test.
- FC-GPR sitelink removed.
- "US time zone" changed to "US morning hours (Eastern)".
- "Written quote first" callout dropped.
- TCPA note added.
- "I am an individual" option added to the form.
- Citation fixes: Advocates Act s.45; Dark Patterns 2023; CPA s.2(47)(ix).
- Primary copies of Press Note 2 (2026) and the S.O.s are flagged as still unopened. No v2 ad relies on them.
- "Free consultation" kept out of ads until the process is documented.
- Cause of the past Google disapprovals still unrecorded. The owner should pull it from the Google policy manager.
