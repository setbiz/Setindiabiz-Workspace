# Change log: #IND1 relaunch + SIB-02 Trademark draft (15 Oct 2026, 12:43–14:20 IST)

Account 152154124583473. Request (Sanjeev, 13:06): "company registration and trademark campaign … optimise with new form and also whatsapp ads … first make them live then continue." Decisions taken via question card (~13:40): **Incorporation = "Fix text, then I switch on"** (one-time OK for Claude to switch #IND1 on); **Trademark = "Rebuild as SIB-02"** (draft only; Sanjeev publishes). Exact ad text approved in the same card.

## Morning check (CTWA click capture, Step 1 of the 15 Oct resume prompt)
| # | Finding |
|---|---|
| R1 | `WA_Ad_Clicks` empty. No real clicks yet. |
| R2 | Hook `sib_wa_click_hook`: 370 invocations / 24 h, 370 success, 0 failed → Meta is delivering webhooks. |
| R3 | Cause of no clicks: prepaid balance ran out. SIB-04 delivery stopped ~21:00 IST 14 Oct (before the 22:17 subscription); ₹0 00:00–11:59 15 Oct. Meta billed ₹4,208.88 at 06:41; ₹25,000 added by UPI at 10:24; first impressions 12:00 hour. |
| R4 | 6 SIB-04 ads re-reviewed 01:29–01:37 IST 15 Oct, all approved. |
| R5 | SIB-04 spent ~₹1,186 of ₹4,180 (28%) between 00:00–06:00 IST on 14 Oct — outside chat hours. Flagged, no change. |
Re-check scheduled 15:30 IST (scheduled task "Re-check WhatsApp ad click capture").

## Audit of paused #IND1 / #IND3 (read-only)
- #IND1 (120240912969660449): paused 6 Oct. 24Hr INSA (120240912969640449, ₹2,500/day) carried Ad-2 (120245819836760449, ₹172 CPL 90d); Daytime INSA (120242110677990449, lifetime ₹250k, ₹56.7k left, ends 30 Oct).
- #IND3 (120243118117990449): paused 6 Oct; campaign + both ad sets end **16 Oct 00:00 IST**. TM Ad 2 (creative 1646472523097654) = 82% of TM leads at ₹136.
- CRM: Sept INC/TM form leads routed across ~15 RMs; 2/200 without product. Routing OK.
- **Claims problems found in the live creatives** (vs 7 Oct settled claims): TM "25,000+ brands already protected" (settled: 14,000+ TM applications filed), "Pan-India protection for 10 years", govt fee ₹4,500 without ₹9,000 rate, no "+ GST"; INC "Pvt Ltd in 7 days" without MCA qualifier, no "+ GST", "25,000+ companies registered", "18+ years". All TM images carry Amazon/Flipkart/Meesho logos without the non-affiliation disclaimer. TM Ad 4 image: "Same-day filing", "Protect your brand for 10 years".
- **Meta AI was rewriting the ads**: INC Ad-2 had 4 AI text variants applied (all "in just 7 days!", "All-inclusive package", "25k+ companies registered"), 3 AI-generated videos, overlays stamping "Pvt Ltd in 7 Days - ₹2,499/-" on the image, text improvements, animation. TM Ad 2 the same.
- Old TM ad sets cannot be edited: error 2446289 (a child ad references a deleted reel); Ads Manager does not name the ad.
- Gov't fee check: Trade Marks Rules 2017, First Schedule — TM-A e-filing ₹4,500 (individual/startup/small enterprise), ₹9,000 others; unchanged.

## Changes
| # | Time (IST) | Change | Before | After | Evidence |
|---|---|---|---|---|---|
| C1 | ~13:35 | INC Daytime INSA ad set 120242110677990449 → PAUSED (API, live) | ACTIVE (campaign off) | PAUSED | connector read |
| C2 | 13:37 | TM campaign + 2 ad sets end-date extension to 31 Oct staged (draft) | — | **Discarded 14:10** (blocked by 2446289; TM rebuilt instead) | draft read empty |
| C3 | 13:52 | INC Ad-2 120245819836760449 edited in Ads Manager (built-in browser): primary text + headline per approved copy; AI text variants removed; AI video generation removed; enhancements 0/5, essential 0/3. Published (1 of 1). New creative **2219613962304030** | old text, AI on | Body: "Register your Private Limited company for a professional fee of ₹2,499 + GST. … Typically 5–7 working days after complete documents, subject to MCA processing. … 25,000+ businesses served. … not affiliated with MCA." Title: "Pvt Ltd Registration @ ₹2,499 + GST" | ads_get_creatives exact match |
| C4 | 13:55 | #IND1 campaign 120240912969660449 → ACTIVE (Sanjeev's one-time OK) | PAUSED | ACTIVE; only 24Hr INSA active (₹2,500/day) | connector read |
| C5 | ~14:05 | **SIB-02 Trademark draft** created by duplicating TM Ad 2 into a new campaign: campaign **120247048085410449**, ad set **120247048085540449** "SIB-02 \| TM \| Form \| IN", ad **120247048085600449** "TM-F1 \| Rs1999 + GST \| Form" | — | Draft, VALIDATED, 0 errors | draft read |
| C6 | ~14:06 | SIB-02 ad set (draft): lifetime ₹150k → **daily ₹1,000**; end date removed; dayparting (Mon–Sat 07:00–19:00) removed → 24h; start 15 Oct 14:00 IST. Inherited: website + instant form (form **1079618781060482** "Trademark V2"), Lead-pixel optimisation, TMF-SA targeting (30 cities, interests, male, A+ audience), FB+IG+Threads, no Audience Network | — | as stated | draft read |
| C7 | ~14:12 | SIB-02 ad (draft): approved TM text + headline "Trademark Filing @ ₹1,999 + GST"; AI selling points unapplied; enhancements 0/5, 0/3 | old TM Ad 2 text | link_data.message = approved text; image d4fb9ef89190d1dbef762e23c478f7cc unchanged | draft read |

## ❌ Blocker found after C3/C4 — Lead Ads ToS (error 1815089)
At ~14:15 Ad-2 showed **status PAUSED, WITH_ISSUES**: "Terms of Service Not Accepted: You can't run lead ads until your Facebook Page accepts Facebook's Lead Generation Terms of Service." Old Ad-1 shows the same. SIB-04 form ads (built from Sanjeev's own Chrome) have no error. `ads_get_ad_account_pages`: leadgen_tos_accepted = false for both Pages; facebook.com/legal/leadgen/tos shows "Setindiabiz Private Limited — Accepted". API re-activation refused with 1815089 ("…this connection cannot read its acceptance status: needs pages_manage_ads for this Page … reconnect and grant pages_manage_ads"). An Ads Manager toggle from the built-in browser was blocked by Claude's safety check. **Net: #IND1 campaign is ON but its ad is off → no spend.**

## Open — who
1. **Sanjeev:** in your own Chrome Ads Manager, switch on #IND1 → C1 - 24Hr INSA → **Ad-2** (the corrected one). If the ToS error persists, re-accept at facebook.com/legal/leadgen/tos for Setindiabiz Private Limited.
2. **Sanjeev:** reconnect the Meta Ads connector in claude.ai and grant **pages_manage_ads** for Page 627814417091714 (fixes API-side 1815089 for good).
3. **Sanjeev:** review and publish **SIB-02 Trademark** from your own Chrome ("Review and publish (3)") — publishing from Claude's built-in browser likely trips the same ToS flag. Optional tweaks before publishing: remove Threads; untick Messenger follow-up (lead_nurture b2p_messaging is on, your SIB-04 rule was WhatsApp-only); "Interactive experiences/show summary" still on.
4. **Sanjeev:** funds/auto-pay. ₹25,000 at ~₹12.4k/day gross (SIB-04 + IND1 + SIB-02) ≈ Saturday morning.
5. **SalesIQ Tiya project:** IPR Zobot on +91 95994 81905 calling `sib_wa_lead` (adcode TM-C1, campaign "SIB-02 Trademark", productid TMF, productcat "TM Filing in India", tag FB-TM, ruleid = Lead - General 2026 1123581000823594437 or a new PPC TM rule). **Only then** build the SIB-02 CTWA ad set (₹1,000/day). Same for Startups (+91 95991 99509) before an Incorporation CTWA ad set.
6. Claude: when the first IND1/SIB-02 form leads arrive, check owner + Product Name/Cat; add `Incorporation V2` / `Trademark V2` CONFIG blocks to `ppc_form_tidy` only if Product Cat comes in blank (show code first).
7. Claude: old #IND3 ad sets lapse tonight (intended). Old TM ads (#C3A/#C3B 2–7) stay as they are; no edits possible while the dead reel blocks.

## Stop-loss (logged)
- #IND1 24Hr INSA: pause if 3-day CPL > ₹440 (2× ₹220 ceiling) or 2 spend-days with 0 CRM leads.
- SIB-02 Form: pause if 3-day CPL > ₹340 (2× ₹170 ceiling) or 2 spend-days with 0 CRM leads.
- Day 14 (29 Oct): cost per contacted / valid / progressed lead vs CTWA once live.
