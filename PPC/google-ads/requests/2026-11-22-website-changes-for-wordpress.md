# Website change request from Google Ads (22 Nov 2026), for the WordPress Optimisation work

Why: Google Ads can only bid on real sales when the website passes Google's click ID to Zoho. The landing pages also need to match the ad claims and Google's government-documents policy. Owner approval is needed before any live change.

| # | Page(s) | Change | Reason / provision |
|---|---|---|---|
| W1 | All lead forms (site-wide, incl. `/lp/*`) | Add hidden fields **gclid, gbraid, wbraid** (and keep UTM fields). Fill them from the landing URL, store them in a first-party cookie for 90 days, and send them to new Zoho Leads fields (`GCLID`, `GBRAID`, `WBRAID`) | Needed for Google Ads offline conversion import (Qualified / Won). Today only 6 of 84 Google leads carry a gclid |
| W2 | All lead forms | Fire one GA4 `form_submission` event per real submit, on the thank-you state only, not on field interaction. Pass the hashed email/phone for Enhanced Conversions only if the privacy notice is updated (W6) | The current action counts many per click |
| W3 | `/lp/trademark-registration`, `/lp/company-registration`, `/company-annual-return` | Add one line next to the existing disclaimer: "You can also file directly on the official portal: ipindia.gov.in / mca.gov.in. Government fees are payable as per the applicable rules." with links | Google Ads policy, Government documents & official services (support.google.com/adspolicy/answer/6368711): disclose that we are a private entity and link to the official site when charging for a service the government offers |
| W4 | `/lp/trademark-registration`, `/lp/company-registration` | Remove the strike-through "was" prices (₹2,500→₹2,000, ₹6,499→₹2,499, etc.) unless a genuine earlier selling price can be documented | Consumer Protection Act 2019 s. 2(28); CCPA Misleading Ads Guidelines 2022; ASCI Code Ch. I |
| W5 | `/lp/trademark-registration` | Make the figures consistent: the header "Starting at Rs. 1,999/- + Govt. Fee" vs the Basic pack ₹2,000. Show the govt fee (₹4,500/class for individuals, startups and small enterprises; ₹9,000 others, Trade Marks Rules 2017, First Schedule) and that GST is extra. Keep "13,500+ trademarks" only with evidence on file | Landing-page match with the ads; no drip pricing (CCPA Dark Patterns Guidelines 2023) |
| W6 | Privacy policy + form notice | If W2's Enhanced Conversions are used, update the notice: details are shared with Google for ad measurement | IT Act 2000 s. 43A + SPDI Rules 2011 r. 4–5; DPDP Act 2023 ss. 5–6 (phased, verify on meity.gov.in) |
| W7 | `/lp/*` pages | `noindex` or canonical to the matching service page, if not already set | SEO: avoid duplicate content with service pages |

Not to do: no "consultation-only" page built to get past Google review (circumvention-policy risk).
