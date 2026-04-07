# Progressive Crystallization

Claude Code prompt system for state-first reasoning on questions where premature closure is expensive.

## The Problem

Most AI reasoning fails in a way that is easy to miss. It does not usually fail by producing nonsense. It fails by producing something clear, plausible, internally consistent, and prematurely complete.

That is a serious failure mode for hard questions: scientific disputes, strategy, architecture, diligence, policy tradeoffs, historical reconstruction, and other problems where multiple coherent stories can exist at the same time. In those settings, the first answer that sounds organized is often not the answer you actually want. It may be operating at the wrong level, holding the wrong variable fixed, treating dependent evidence as independent, or smoothing over a tension that should have remained live.

Standard multi-agent setups help, but they often still reason through conversation. One agent says something, another responds, a third summarizes, and the transcript grows. What gets lost is the actual reasoning state: which assumption was attacked, which contradiction survived, which evidence lines turned out to share a hidden dependency, what would change the result, and what still has not earned closure.

Progressive Crystallization is an attempt to address that problem.

## What Progressive Crystallization Is

Progressive Crystallization, or PC, treats reasoning as an evolving epistemic state rather than a sequence of isolated turns.

The central idea is simple:

- the transcript is a log
- the state is the reasoning

Instead of relying on the model to repeatedly reconstruct its own reasoning from prose, the system tries to preserve explicit objects across rounds: tensions, alternatives, assumptions, dependency structure, tests, residuals, and update rules. Different operations then apply different kinds of pressure to that state.

The name comes from the intended process. The system does not begin by forcing clean, rigid claims. It begins with looser objects: half-formed alternatives, objections, hidden assumptions, suspected circularities, frame errors, and unresolved tensions. Those objects are preserved and pressed on. Only the parts that survive that pressure, or become experimentally differentiable, are allowed to harden into more structured artifacts. That hardening process is the crystallization.

## What This Repo Is

This repo is not a standalone application. It is a Claude Code prompt-and-agent scaffold for running that style of reasoning.

It gives you:

- user-facing Claude Code commands for different reasoning modes
- agent prompts for the underlying roles in the loop
- a working paper describing the conceptual argument behind the system
- a generated `sessions/` directory where structured state and transcripts are written during use

If you clone this repo, you are getting a reusable reasoning scaffold, not a packaged product.

## What This Repo Contains

- [`.claude/commands/`](./.claude/commands): user-facing Claude Code commands
- [`.claude/agents/`](./.claude/agents): agent prompts used by the command system
- [`papers/progressive_crystallization_v3.md`](./papers/progressive_crystallization_v3.md): current working paper
- [`schemas/epistemic_state_schema.json`](./schemas/epistemic_state_schema.json): minimal transitional object model and lifecycle reference
- [`scripts/validate_state.py`](./scripts/validate_state.py): validator for state files and lifecycle consistency
- [`sessions/`](./sessions): generated runtime output; ignored for Git except for a placeholder

The system treats reasoning as an evolving epistemic state rather than a sequence of isolated turns. The goal is to preserve tensions, assumptions, dependency structure, tests, and residuals across rounds instead of reconstructing them from transcript prose every time.

## How It Works

The commands in this repo correspond to different kinds of pressure you might want to apply to a hard question.

- [`/scrutinize`](./.claude/commands/scrutinize.md) is for breaking the current story: attack the strongest hypotheses, inspect evidence quality, and find the weak points.
- [`/reframe`](./.claude/commands/reframe.md) is for diagnosing whether the question itself is malformed, shallow, or hiding the real variable.
- [`/explore`](./.claude/commands/explore.md) is for opening serious alternative space before collapsing to a verdict.
- [`/crystallize`](./.claude/commands/crystallize.md) is the orchestrator that decides when to scrutinize, reframe, or explore.
- [`/escalate`](./.claude/commands/escalate.md) is a frame-breaker that forces the next first-principles question when the reasoning is converging too smoothly.
- [`/extract`](./.claude/commands/extract.md) is for turning an uploaded paper into analyst-grade structured takeaways for downstream scrutiny or exploration.

Underneath those commands is a state-first architecture. The next round is supposed to begin from the current epistemic map, not from “what was just said.” That is the core design choice.

## Commands

- [`/scrutinize`](./.claude/commands/scrutinize.md): attack the leading hypotheses, evidence lines, and assumptions
- [`/reframe`](./.claude/commands/reframe.md): diagnose and replace a malformed or shallow question
- [`/explore`](./.claude/commands/explore.md): map live model space and produce a research agenda
- [`/crystallize`](./.claude/commands/crystallize.md): orchestrate the full loop across modes
- [`/escalate`](./.claude/commands/escalate.md): force the next frame-breaking first-principles question
- [`/extract`](./.claude/commands/extract.md): ingest a paper into analyst-grade structured takeaways

## How To Use It

1. Clone the repo.
2. Open it in Claude Code.
3. Ask Claude Code to run one of the commands above against your question or uploaded paper.
4. Review generated output under [`sessions/`](./sessions).

The repo does not ship as a standalone application. It is a prompt-and-agent scaffold intended to be used from within Claude Code.

## Runtime Output

Runs write structured state and transcripts under [`sessions/`](./sessions). That directory is treated as generated output and is ignored by Git by default.

If you want to publish example runs, copy only curated outputs into a separate folder such as `examples/` rather than committing all local sessions.

You can validate a state file with:

```bash
python3 scripts/validate_state.py sessions/state.json
```

## Working Paper

The current paper draft is [`papers/progressive_crystallization_v3.md`](./papers/progressive_crystallization_v3.md).

It argues that epistemic state transition, not the conversational turn, is the right unit of AI reasoning, and that the main open design question is when loose tensions should harden into structured claims.

## What Good Use Looks Like

This framework is most useful when:

- the first plausible answer is likely to be at the wrong level
- several coherent positions can survive initial inspection
- evidence independence matters
- premature closure is expensive
- you care not just about the answer, but about what survived, what failed, and what would change the result

It is much less useful for:

- simple factual lookups
- shallow questions
- situations where speed matters more than depth
- tasks where the bottleneck is missing information rather than reasoning quality

## License

This repo is released under the [MIT License](./LICENSE).

## Limits

This framework can impose structure and pressure. It cannot create domain competence the underlying model does not have.

If the model cannot recognize circular evidence, distinguish genuine tests from fake ones, or separate real constraints from rhetoric, the system can still produce well-structured wrong answers.
