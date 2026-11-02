# PPC Operating Plan — Elephant-Goldfish Model (EGM)

**Goal:** a repeatable loop that **plans → evaluates → improves** Setindiabiz's ads on 7 platforms. One agent with full context (the Elephant) does the work. Fresh, isolated agents with no context (the Goldfish) attack it before any rupee moves. A human approves.

> EGM is Google's open-source plugin (Apache-2.0, "not an officially supported Google product"). It was built for software design docs. This repo adapts it to PPC through EGM's support for custom reviewers and standards in `egm-review-loop`.

## 1. Pieces

| Piece | Where | Role |
|---|---|---|
| Elephant | The Claude Code session in this repo | Holds context (`CLAUDE.md`, `shared/`, changelogs, learnings), pulls data, drafts |
| EGM built-in Goldfish | Plugin: `egm-zoom-out`, `egm-comprehension`, `egm-design`, `egm-style`… | Simplicity / clarity checks on plans |
| **PPC Goldfish** | `PPC/egm/reviewers/` | Media-buyer critic, measurement skeptic, compliance (India law and platform policy), customer lens, CFO |
| Standards | `PPC/egm/standards/` | Pass/fail bar: campaign plan, weekly review, ad copy |
| Templates | `PPC/egm/templates/` | What the Elephant drafts from |
| Skills | `.claude/skills/ppc-weekly-cycle`, `ppc-new-campaign` | The orchestrated workflows |
| Run artifacts | `PPC/egm/runs/<date>-<slug>/` | Data, drafts, every reviewer report, consolidated report |

## 2. How each EGM command is used

| EGM command | PPC use | When |
|---|---|---|
| `/egm:egm-brainstorm` | Pressure-test an idea (new platform, new service, new angle) before planning | New campaigns/tests |
| `/egm:egm-draft` | Write the campaign plan section by section, using our template | New campaigns/tests |
| `/egm:egm-review` | Built-in 5-stage review: zoom-out, comprehension, critic, readiness of the build sheet | New campaigns/tests |
| `/egm:egm-review-loop` | **The core.** Runs our 5 PPC reviewers against our standards | Every plan, weekly review, ad-copy batch |
| `/egm:egm-resolve` | Human goes through the findings: accept, reject or defer | After every review |
| `/egm:egm-drift-report` | Compares docs with *code*, so it applies only to `scripts/`. Account drift (documented structure vs live account) is a separate monthly step done with the connectors | Monthly |
| `/egm:egm-bootstrap` | Not needed (no large codebase) | — |

## 3. The automatic loop

```
 Every Monday (scheduled task, unattended)                 You (≈15 min)                   Claude (on your OK)
 ┌────────────────────────────────────────────┐   ┌──────────────────────────────┐   ┌─────────────────────────────┐
 │ 1 Pull 7 platforms + Zoho (Supermetrics,   │   │ Read draft PR on phone/web   │   │ Apply ONLY approved actions  │
 │   Meta connector)                          │──▶│ /egm:egm-resolve or comment  │──▶│ via connectors, new = PAUSED │
 │ 2 Elephant drafts weekly review + actions  │   │ "apply approved actions"     │   │ Log in changelog + review on │
 │ 3 5 Goldfish review in parallel (isolated) │   └──────────────────────────────┘   └──────────────┬──────────────┘
 │ 4 Consolidated report, Blockers removed    │                                                      │
 │ 5 Commit → draft PR → notify               │◀─────── next Monday: due "Review on" items are ─────┘
 └────────────────────────────────────────────┘         measured → shared/learnings.md (the "improve" step)
```

**Automatic:** data pull, analysis, drafting, Goldfish review, consolidation, the PR, the notification, and evaluating past changes into learnings.
**Never automatic:** any change to an ad account, any budget increase, any new campaign or activation. These need your explicit approval (`PPC/CLAUDE.md`, rule 6).

## 4. Cadence

| Cadence | What | How |
|---|---|---|
| Weekly (Mon) | Evaluate + improve | Scheduled task runs `/ppc-weekly-cycle` |
| Monthly (1st working day) | Cross-platform budget reallocation proposal + account-drift check + CRM reconciliation | Scheduled task: monthly variant, reviewed by the CFO + measurement Goldfish |
| On demand | New campaign / platform test / restructure | `/ppc-new-campaign` (interactive EGM flow) |
| Quarterly | Channel strategy (which of the 7 platforms to keep or scale) | `/egm:egm-review-loop` with `heilmeier-standard` + CFO + zoom-out |
| One-time (after migration) | Baseline audit per platform from imported ChatGPT/Cowork history + live data | `/ppc-new-campaign` style review per platform |

## 5. Setup checklist

1. ☐ **Push this repo to GitHub** (private). Scheduled cloud runs and PRs need it.
2. ☐ **Install EGM** (you run this; Claude was not allowed to enable third-party plugins on its own):
   ```bash
   claude plugin marketplace add google/elephant-goldfish-model
   ```
   ```bash
   claude plugin install egm@egm
   ```
   For scheduled cloud runs, also put both commands in the cloud environment's **setup script**, or add the plugin to `.claude/settings.json` (`extraKnownMarketplaces` + `enabledPlugins`) yourself. The PPC reviewers in `PPC/egm/reviewers/` work even without the plugin, because `ppc-weekly-cycle` dispatches them directly.
3. ☐ **Supermetrics logins** (https://hub.supermetrics.com): LinkedIn Ads, X Ads, Reddit Ads, ChatGPT Ads (early access), Zoho CRM. Already connected: Google Ads, Microsoft Advertising, Facebook Ads.
4. ☐ **Fill `PPC/shared/`**, especially AOV and lead→sale % per service. Without these the CFO reviewer will block budget decisions.
5. ☐ **Create the scheduled tasks** (Claude does this once 1–4 are done): weekly on Monday morning IST, monthly on the 1st working day. Connectors granted: Meta Ads, Supermetrics, Zoho CRM.

## 6. Guardrails
- Goldfish are read-only and get no summary of the Elephant's reasoning, only files. That's what makes the review independent.
- A same-context "review" doesn't count. If subagents are unavailable, the run stops.
- Every number cites its source. A reviewer who finds an unsourced number raises a Blocker.
- Compliance findings cite the Act, section, rule or code clause, and anything that may have been amended is re-verified.
