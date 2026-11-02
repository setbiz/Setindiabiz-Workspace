# Weekly Review Standard

A weekly review passes if a fresh reader can see what happened, why, and exactly what will change, and can check that every number is real.

## Required sections
1. **Data provenance**: for each platform, the source (connector or CSV), date range, comparison period, pull timestamp, and any platform with missing data.
2. **Scorecard vs KPI**: spend, clicks, CTR, CPC, conversions, CPL, CPA, qualified leads (CRM). Shown per platform and blended, against target and the previous period.
3. **Tracking health**: tag or CAPI status and anomalies (sudden drops to zero, duplicated conversions).
4. **What changed and why**: diagnosis using actual drivers (search terms, placements, audiences, creatives, auction metrics). Hypotheses are labelled as hypotheses.
5. **Due reviews**: every `changelog.md` entry whose "Review on" date has passed, with the outcome measured and moved into `shared/learnings.md`.
6. **Proposed actions**: each one has a platform, the exact change, the data that justifies it, expected impact, risk, whether it is reversible, and a review date. Actions are ranked by expected impact.
7. **Needs human decision**: budget increases, new campaigns, pausing top campaigns, and anything that touches compliance.

## Failing conditions (Blockers)
- An invented or unsourced number.
- An action that isn't justified by data in the document.
- More than 3 simultaneous structural changes to one campaign (learning-phase risk) without a stated reason.
