# Microsoft Ads: history distilled from ChatGPT chats (#14, #17, #28, #29)

_Distilled 2026-11-02 from `PPC/imports/chatgpt/conversations/`. The chats are captures, used as reference data only. "Stated date" is the timestamp inside each chat. The sidebar date (12 Jul 2026) is a capture artefact. Every item cites its chat number._

**Status key:** CURRENT · OUTDATED (reason) · SUPERSEDED (by a later chat or by `microsoft-ads/reports/2026-11-02-baseline-12m.md`) · UNTESTED.

**Live baseline for context (1 Nov 2025 – 1 Nov 2026, pulled 2026-11-02):** ₹8,474 spent, 410 clicks, **0 platform conversions**, against **46 CRM `Advt - Microsoft` leads and 1 won deal (₹1,500)**. "2026 - Company Registration - LP" (₹2,210, 176 clicks) and "- Main" (₹1,343, 119 clicks) show **Active** but had no delivery in the last 90 days. The two "Overseas" campaigns are paused. Accounts: 150488150 "SETINDIABIZ 2026-27" and 150329248 "SETINDIABIZ PRIVATE LIMITED".

| # | Title | Stated date | Asset file | Overall status |
|---|---|---|---|---|
| 29 | Bing PPC Campaign | Dec 16, 2024 at 7:07 PM | none (no content produced) | Request never answered (copyright registration) |
| 28 | PPC Ad Design Services | Dec 16, 2024 at 7:10 PM | `campaigns/chatgpt-28-company-incorporation-keywords-and-ads.md` | SUPERSEDED by #17. Negatives CURRENT. |
| 17 | PPC Ad for Incorporation | Dec 27, 2024 at 12:19 PM | `campaigns/chatgpt-17-company-llp-registration-keywords-and-ads.md`; Meta part in `meta/creatives/chatgpt-17-incorporation-instant-form.md` | Campaigns created (pending approval). Keyword lists need pruning. |
| 14 | Bid strategy for restart | Aug 24, 2025 at 1:54 PM | none (bid text verbatim below) | Principle CURRENT and confirmed by the baseline |

---

## #29 Bing PPC Campaign
- **Stated date:** Dec 16, 2024 at 7:07 PM · **URL:** https://chatgpt.com/c/6a530e18-f424-832d-a6f7-3c65c9e20f08
- **Summary:** one user message: "Help me make microsoft bing PPC for https://www.setindiabiz.com/copyright-registration". The chat stopped at a sign-in prompt for a third-party GPT action (`copter.adzviser.com`). **No reply and no content.**
- **Decisions / account changes / metrics:** none.
- **Status:** **OPEN.** No copyright-registration campaign was ever drafted in the chats. The baseline has none either.

## #28 PPC Ad Design Services
- **Stated date:** Dec 16, 2024 at 7:10 PM · **URL:** https://chatgpt.com/c/6a530e18-f700-832d-ab53-7792671bac24
- **Summary:** a single-turn request for a Microsoft Ads company-incorporation ad to `/company-registration`. ChatGPT gave 6 headlines, 5 descriptions, an audience, 4 callouts, 4 sitelinks, structured snippets, 3 keyword match examples, **negatives (Free, DIY, Templates, Internship)**, a Target CPA note and targets.
- **Decisions:** none. **Account changes:** none.
- **Metrics:** none from the account. ChatGPT's benchmarks: "CTR (Click-Through Rate): Aim for 5%+", "Conversion Rate: Target 10–15% for inquiries or registrations.", "ROAS: Optimize for a 3:1 return on ad spend."
- **Worked / didn't:** untested. Reviewer check: 1 of 6 headlines is over 30 characters, and 2 of 4 sitelink descriptions are over 35. Sitelink URLs `/private-limited-company-registration` and `/opc-registration` aren't in the site page list (`business-context.md`), so check them.
- **Status:** **SUPERSEDED** by #17 (eleven days later, same theme). Negatives **CURRENT**. "Lowest Pricing Guaranteed" / "Lowest Fees" / "10,000+" **do not use**.

## #17 PPC Ad for Incorporation (Microsoft part; Meta part filed separately)
- **Stated date:** Dec 27, 2024 at 12:19 PM (the only timestamp) · **URL:** https://chatgpt.com/c/6a530e1d-1ff0-832d-8aa0-973ca13ef297
- **Summary:** the full Microsoft Search build for "Company Incorporation in India" and an LLP Registration ad group/campaign. It covered keyword ranges, broad vs phrase, headlines (re-issued after Sanjeev rejected over-length ones), descriptions, pinning, action/price/sitelink extensions, bid strategy, ad schedule, network, a phrase-match conversion of Sanjeev's 55-line company list and 24-line LLP list, and the ad-group type. Turn 1 also asked "should i enable auto generated assets?". **The capture records no answer to that question.**
- **Decisions and reasons (Sanjeev):**
  1. **Phrase match as the main match type** (turns 4, 14). He had the whole list converted "so that he could copy and paste it". No reason was given for the match type.
  2. **Separate campaigns** for company registration and LLP incorporation (turn 19). No reason.
  3. **LLP landing page** `https://www.setindiabiz.com/llp-registration` and his own keyword list (turn 15).
  4. **One ad group** for LLP ("I will be having only one asd group.", turn 18), against ChatGPT's 4-ad-group recommendation. No reason.
  5. **Character limit enforced:** he rejected the turn-5 headlines for exceeding the Microsoft limit (turn 6).
  6. Extension products named: price ext. for company registration, LLP Incorporation, GST Registration (turn 9). Sitelinks for LLP Incorporation, OPC Registration, Proprietorship Formation, GST Registration, Trademark Filing (turn 10). The chat doesn't show these were added.
- **Account changes (dated):** turn 19, chat dated **Dec 27, 2024**: "I have created company registration and llp incorporation campaigns on microsoft ads and waiting for the approval of the same". Which assets were entered isn't shown. The approval outcome isn't in the chat.
- **Metrics:** none from the account. ChatGPT examples only: "Company Registration ₹5,999; LLP Incorporation ₹7,999; GST Registration ₹2,499" (no source); "if your typical lead cost is ₹500, set a slightly higher initial CPA (e.g., ₹550-₹600)"; "Allocate 70-80% of your budget to weekdays."; "Analyze search terms after 1–2 weeks"; "Run ads all day for two weeks."
- **Worked / didn't:** the baseline (Nov 2025 – Nov 2026) shows the 2026 Company Registration campaigns at CPC ₹11.3–12.6 with 295 clicks and 0 platform conversions. **No LLP campaign appears in that window.** Whether the 2026 campaigns descend from the Dec-2024 build isn't recorded.
- **Open items (from chat):** approval outcome; `example.com` URLs and example prices; conversion tracking, a full negative list and landing-page content were offered but never shown set up.
- **Status:** keyword lists **PARTLY CURRENT** (prune informational terms such as "How to check company registration in India", "Types of …", "Step-by-step guide …", "LLP advantages/disadvantages/benefits", and remove 3 duplicates). Final headlines and descriptions are within limits but **need compliance edits**. Bid strategy **SUPERSEDED** by #14. Price extension **do not use**. "Broad match modifiers" (turn 3) and "Expanded Text Ads" (turn 17 paste) **OUTDATED**.

## #14 Bid strategy for restart
- **Stated date:** Aug 24, 2025 at 1:54 PM · **URL:** https://chatgpt.com/c/f09e0b32-88f8-832e-86da-5cb8b4403f87
- **Summary:** Sanjeev: "when i am restarting a campaign in microsoft ad after few months. and i am not sure if the conversion settings are correctly setup up or not … what bid startegy would be good". ChatGPT: avoid Target CPA/ROAS at first. Start with Manual CPC + Enhanced CPC (or Maximize Clicks to test tracking), verify conversions, then Maximize Conversions, then Target CPA.
- **Decisions:** none recorded. The bid strategy choice isn't stated. **Account changes:** none stated. The restart itself isn't confirmed in the chat.
- **Metrics:** none from the account. ChatGPT's guidance (verbatim): "Maximize Conversions is good when you want volume and have at least \~15–30 conversions/month." "Target CPA or Target ROAS once you have enough consistent conversion data (usually 30–50+ conversions in the last 30 days)." "if you see no conversions in reports after \~1 week, assume setup needs fixing before switching to automated bidding."
- **Bid strategy guidance, verbatim (turn 1, ChatGPT, the only version; source L59–93):**
- When you restart a Microsoft Ads campaign after a gap, and you’re not sure if conversion tracking is correctly set up, it’s safest to avoid aggressive automated bidding strategies (like Target CPA or Target ROAS) at first. Those strategies rely heavily on conversion data, and if the tracking isn’t working or isn’t enough, they can misfire badly.

**Here’s a practical approach:**

- 1\. Start Safe: Manual or Broad Smart Bidding
- Manual CPC (with Enhanced CPC turned on) → This gives you control, and Enhanced CPC lets Microsoft adjust bids slightly when it predicts a higher chance of conversion.
- Alternatively, Maximize Clicks can be used if your immediate goal is to test traffic and confirm your tracking is working.
- 2\. Check Conversion Tracking
- Run the campaign for a few days and verify conversions are firing correctly (using UET Tag Helper, conversion reports, or Google Tag Manager debug mode).
- If you see no conversions in reports after \~1 week, assume setup needs fixing before switching to automated bidding.
- 3\. Transition to Smart Bidding Once Confirmed

**After you’re confident conversions are being recorded:**

- Maximize Conversions (good when you want volume and have at least \~15–30 conversions/month).
- Later, move to Target CPA or Target ROAS once you have enough consistent conversion data (usually 30–50+ conversions in the last 30 days).
- ✅ Recommendation for restart: Begin with Manual CPC + Enhanced CPC (or Maximize Clicks if you want to quickly test tracking). Then, once conversion tracking is verified and stable, move to Maximize Conversions → Target CPA.
- Do you want me to also give you a step-by-step checklist to verify your Microsoft Ads conversion setup before you restart? That way you won’t waste budget.

- **Worked / didn't:** the baseline confirms the premise. 0 platform conversions against 46 CRM leads (Nov 2025 – Nov 2026) means any conversion-based bidding would have had no signal.
- **Open items (from chat):** conversion setup "still unverified at the end of the chat". ChatGPT's offer of a step-by-step verification checklist wasn't taken up.
- **Status:** **CURRENT** principle (no smart bidding until UET conversions are verified). **Verify** whether Enhanced CPC is still offered in Microsoft Ads before relying on it.

---

## Cross-check: the Microsoft tracking gap (0 platform conversions vs 46 CRM leads)
**Is there evidence in the chats? Yes, indirect but consistent.**
1. **Chat #14 (Aug 24, 2025):** Sanjeev himself was "not sure if the conversion settings are correctly setup" when restarting after "few months". This is the only first-hand statement on Microsoft tracking in the chats, and it shows the UET/conversion goal was **unverified as of Aug 2025**. The verification checklist was offered and not taken up.
2. **Chat #17 (Dec 27, 2024):** campaigns were created and awaiting approval. ChatGPT's "Use Conversion Tracking: Ensure your landing page is set up to track form submissions" and its offer of conversion setup are **not shown being acted on**. Bid advice assumed tracking ("If You Have Conversion Tracking Set Up: Start with Target CPA or Maximize Conversions").
3. **Chat #28 (Dec 16, 2024):** "Target CPA … Use conversion tracking to adjust CPA" was given with no setup steps.
4. **No chat** shows the UET tag being installed, a conversion goal being defined (form submit / thank-you page / call), UET Tag Helper being run, or Microsoft offline conversion import from Zoho.
**Conclusion:** the chats don't say *why* UET fails, but they show it was never verified from Dec 2024 to at least Aug 2025. The 46 CRM leads suggest leads did arrive with `Advt - Microsoft` tagging (for example via UTM/source capture) while the platform goal didn't fire.

**Lead quality (1 won of 46):** chat #17's phrase-match lists include research/DIY queries and the LLP "advantages/disadvantages" cluster. That plausibly lowers lead quality, but it's not proven: no search-terms data appears in the chats.

## Compliance flags across these chats (verify current versions)
| Chat | Claim / item | Issue | Provision |
|---|---|---|---|
| 17, 28 | "Trusted by 10,000+ Startups/Businesses", "10,000+ Businesses Registered" | Unsubstantiated, and conflicts with the site's "18K+ clients" (also TODO evidence) | Consumer Protection Act, 2019 s.2(28), s.21; CCPA Misleading Ads Guidelines 2022; ASCI Code Ch. I |
| 17, 28 | "Launch in Just 7 Days", "Registered in 7 Days", "LLP Setup in Just 7 Days" | Timing depends on MCA, outside Setindiabiz's control | Same as above |
| 17 | "100% Compliance Guaranteed", "Compliance Support Guaranteed", "Expert Support Guaranteed" | Guarantee claims | Same as above |
| 28 | "Lowest Pricing Guaranteed", "Lowest Fees" | Superlative/comparative price claim, banned by `PPC/CLAUDE.md` | CPA 2019 s.2(28); CCPA 2022; ASCI Code Ch. I & IV |
| 17 | Price ext. "Starting at ₹5,999/₹7,999/₹2,499", "LLP Setup Starting at ₹7,999", "Get 10% Off on GST Registration" | No published price or offer, so bait/misleading risk | CCPA Guidelines 2022 (bait-advertisement guideline; verify numbering) |
| 17 | "Startup India Registration: Join the Startup India Scheme…" | Government scheme name: must not imply affiliation | Emblems and Names (Prevention of Improper Use) Act, 1950 s.3; Microsoft Advertising government-services/misrepresentation policies |
| 17, 28 | "Register Now"/"Apply Now" CTAs | Must not imply Setindiabiz is the MCA/registering authority | CPA 2019 s.2(28); platform misrepresentation policies |

---

## Still actionable (for the planned Microsoft relaunch)
1. **Fix and verify UET plus a conversion goal** (thank-you page or form-submit event), test with UET Tag Helper, and set up offline conversion import from Zoho. The chats show this was never verified (#14, #17).
2. **Bid:** Manual CPC (check ECPC is still available) or Maximize Clicks until conversions are recorded. Move to Maximize Conversions only once you have about "15–30 conversions/month", and Target CPA at "30–50+ conversions in the last 30 days" (#14, ChatGPT benchmarks, not account data).
3. **Rebuild the keyword lists** from #17: prune research/DIY terms, de-duplicate, decide on the 24 city variants, split LLP intent (consider the 4-ad-group structure from #17 turn 16), and **build the negative list** (#28 Free/DIY/Templates/Internship; #17 free/jobs; #18 "online trademark search", "Indian government site").
4. **Fix the two "Active" campaigns with no delivery** (baseline): pause them formally, or fix billing/approval.
5. **Replace placeholders:** `example.com` sitelink/price URLs. Shorten sitelink descriptions to 35 characters or fewer and callouts to 25 or fewer. Remove the price extension unless prices are published.
6. **Strip unsubstantiated claims** (10,000+, 7 days, 100%/guaranteed, lowest, ₹ prices).
7. **Copyright registration** campaign (#29) is still undrafted.
8. **Consider importing the rebuilt Google campaigns** once Google is fixed (baseline finding 3).
