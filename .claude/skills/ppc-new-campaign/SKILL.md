---
name: ppc-new-campaign
description: Plan a new Setindiabiz PPC campaign, platform test or major restructure with the full Elephant-Goldfish flow (brainstorm → draft → Goldfish review → resolve → approve → build PAUSED). Interactive.
---

# New Campaign / Test Planning with EGM

Use this for anything new: a new platform (e.g. ChatGPT Ads, Reddit), a new service campaign, a restructure, or a budget shift above 20%. For routine weekly tweaks use `ppc-weekly-cycle`.

EGM artifact directory: `PPC/egm/runs/<YYYY-MM-DD>-<slug>/`

1. **Brainstorm.** Run `/egm:egm-brainstorm <slug>`. Context to give it: `PPC/shared/*`, the platform folder, and the relevant `shared/learnings.md` entries. Its Goldfish challenge the idea before any plan exists. Output: `concepts_brief.md`.
2. **Draft.** Run `/egm:egm-draft` on the brief. Tell it to follow `PPC/egm/templates/campaign-plan-template.md` and `PPC/egm/standards/campaign-plan-standard.md`. Output: `design_draft.md` (the campaign plan).
3. **Built-in EGM review.** Run `/egm:egm-review design_draft.md`. Its zoom-out and comprehension stages work as-is for plans. The implementation-readiness stage checks the build sheet. Treat "codebase" findings as not applicable.
4. **PPC Goldfish review.** Run `/egm:egm-review-loop` with:
   - TargetFile: `design_draft.md`, SemanticTarget: `full file`
   - Reviewers: `PPC/egm/reviewers/ppc_performance_critic.md`, `PPC/egm/reviewers/measurement_skeptic.md`, `PPC/egm/reviewers/budget_cfo.md`, `PPC/egm/reviewers/compliance_reviewer.md`, `PPC/egm/reviewers/customer_lens.md`
   - Standards: campaign-plan → `PPC/egm/standards/campaign-plan-standard.md`; compliance and customer → `PPC/egm/standards/ad-copy-standard.md`
   - GoldfishContext: `PPC/shared/`, `PPC/<platform>/`
5. **Resolve.** Run `/egm:egm-resolve`. The human decides on each finding.
6. **Approve.** The human approves the final plan. Save it as `PPC/<platform>/campaigns/<YYYYMM>-<slug>.md`.
7. **Build.** Only after approval, create the entities through the connector (where one exists) exactly as in the build sheet, all **PAUSED**. Show the human a preview, then activate on their explicit OK. Log the launch in `changelog.md` with the review date from the plan.
