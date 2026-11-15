# egm-zoom-out report: weekly review w/e 2026-11-08

Raw output from the isolated EGM zoom-out subagent (read-only), 9 Nov 2026.

**Context check: passes.** Objective clear (Meta dark since 6 Nov because prepaid funds ran out; neither week can judge the 2 Nov changes). No Blockers.

1. **Major**: Action 1 / §3 Funding / §7.1. The real problem is the funding model (3 interruptions in 14 days; the ₹15,000 top-up on 4 Nov lasted about 1 day). Action 1 treats it as a one-off top-up and mentions the structural fix only in passing. The 7-day sizing has no buffer. Make the payment method, or a top-up rule tied to daily budget with a buffer, the primary decision.
2. **Major**: §3 WhatsApp / Action 4. Before a manual end-to-end test, use the existing attribution system (`shared/lead-source-attribution-runbook.md`). The taxonomy has no `Advt - WhatsApp`. WATI leads map to `Social - WhatsApp`. Rule 7 classifies CTWA_Click_ID-only leads as `Advt - Facebook`. Run one `GROUP BY Lead_Source` query on W leads with `CTWA_Click_ID` set first. State that action 4 is not a gate on funding.
3. **Major**: §3 ChatGPT / Action 7. Rule 4 relabels `utm_source=chatgpt` leads as `AI - ChatGPT`, so an `Advt%` query can show 0 while campaigns run. Do one COQL count of `AI - ChatGPT` W vs P before the dashboard check. Don't set up a CGPTA/CSV pipeline until the channel is confirmed live.
4. **Nit**: Action 2. A Meta campaign spending limit (spend to date + ₹3,078) enforces the cap exactly and needs no tracking. Offer it as the default, with pause as the fallback. Confirm what the cap counts from.
5. **Nit**: §4 items 2–4 and "vs prev" invite conclusions the review says can't be drawn. Cut them to one "directional, not actionable" line.
6. **Nit**: Scorecard uses ₹176 (not adopted) while `kpis.md` says ₹130–135. Label it provisional or use the adopted figure.
7. **Nit**: Action 6 covers action 3. Fold the changelog step into action 6 and keep the revert-or-confirm choice in §7.3.

Keep: action 5 (clear the unworked paid leads), the provenance table, the inconclusive verdicts.
Side note: `shared/business-context.md` lists `Advt - WhatsApp` / `Advt - ChatGPT` as live values, but the runbook taxonomy has neither. Fix this in `shared/`.
