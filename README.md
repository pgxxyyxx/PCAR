# Progressive Crystallization

Claude Code prompt system for state-first reasoning on questions where premature closure is expensive.

## What This Repo Contains

- [`.claude/commands/`](./.claude/commands): user-facing Claude Code commands
- [`.claude/agents/`](./.claude/agents): agent prompts used by the command system
- [`papers/progressive_crystallization_v3.md`](./papers/progressive_crystallization_v3.md): current working paper
- [`sessions/`](./sessions): generated runtime output; ignored for Git except for a placeholder

The system treats reasoning as an evolving epistemic state rather than a sequence of isolated turns. The goal is to preserve tensions, assumptions, dependency structure, tests, and residuals across rounds instead of reconstructing them from transcript prose every time.

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

## Working Paper

The current paper draft is [`papers/progressive_crystallization_v3.md`](./papers/progressive_crystallization_v3.md).

It argues that epistemic state transition, not the conversational turn, is the right unit of AI reasoning, and that the main open design question is when loose tensions should harden into structured claims.

## License

This repo is released under the [MIT License](./LICENSE).

## Limits

This framework can impose structure and pressure. It cannot create domain competence the underlying model does not have.

If the model cannot recognize circular evidence, distinguish genuine tests from fake ones, or separate real constraints from rhetoric, the system can still produce well-structured wrong answers.
