# Multi-Agent Progressive Crystallization (MAPC)

> The first plausible answer to a hard question is almost never the right one. It is usually operating at the wrong level, holding the wrong variable fixed, treating dependent evidence as independent, or smoothing over a tension that should have remained live.

Most AI reasoning does not fail by producing nonsense. It fails by producing something clear, plausible, internally consistent, and prematurely complete. For hard questions, that is often the most expensive failure mode.

**Multi-Agent Progressive Crystallization (MAPC) is a state-first reasoning scaffold for Claude Code.** It turns Claude Code into something closer to an adversarial research team: a builder who steelmans the strongest position, a destructor who attacks the weakest assumption, an auditor who checks both sides for circular reasoning, a falsifier who demands testable predictions, an escalator who refuses to let the analysis settle at the wrong level, and a synthesizer who preserves what survives without smoothing away the tensions.

Eight commands. Twelve agents. All slash commands, all Markdown, all MIT licensed.

**What this is for:**
- **Researchers and analysts** who need to know what actually survives scrutiny, not just what sounds right
- **Technical founders** making high-stakes decisions where the first coherent answer is systematically wrong
- **Anyone working on questions** where multiple coherent positions can coexist and premature closure is expensive

## Quick start

1. Clone this repo and open it in Claude Code
2. Run `/scrutinize Is the Hubble tension more likely new physics or unresolved systematics?` on any hard question
3. Run `/crystallize` to let the system choose its own mode sequence

## Install

```bash
git clone https://github.com/pgxxyyxx/MAPC.git
cd MAPC
```

Open the directory in Claude Code. Claude Code is required; this repo is a prompt scaffold for that environment, not a standalone CLI.
The commands and agents load automatically. No build step, no dependencies, no setup script.
This repository is not a standalone application or CLI. It is a Claude Code prompt scaffold: the commands and agents become available inside Claude Code when the repository is opened there.

## See it work

Illustrative example. The exact runtime artifact format in this repo uses archived markdown logs and structured state files rather than the bracketed inline transcript shown below.

```
You:    /scrutinize Is the Hubble tension more likely to reflect
        new physics or unresolved systematics?

Claude: [ESCALATOR] Reframing the question. "New physics or
        systematics" compresses several separable issues into one
        binary. Better question: which measurements disagree, which
        assumptions are shared across them, and what observations
        would update the balance between cosmological and
        instrument/model explanations?

        [BUILDER] Steelmanning the new-physics case from first
        principles. If late- and early-universe inferences disagree
        after calibration and model assumptions are audited, the
        residual may point to missing structure in the cosmological
        model.

        [DESTRUCTOR] The disagreement is not yet clean evidence for
        new physics. Distance ladders, calibration chains, selection
        effects, and model priors create multiple routes for shared
        systematics to survive as apparent tension.

        [AUDITOR] Several evidence lines are less independent than
        they appear. Distance-ladder steps share calibration logic,
        and cosmological inferences share model assumptions.

        [FALSIFIER] The decisive question is not whether the tension
        exists rhetorically but whether independent measurement routes
        converge once calibration dependencies are relaxed. New data
        from independent probes should update the two explanations
        differently.

        [SYNTHESIZER]
        What survives: there is a real measurement disagreement, but
        its interpretation depends on the independence of the probes.
        Decisive bottleneck: unresolved dependence between calibration
        chains and model assumptions.
        Discriminating test: an observational route with materially
        different systematics that lands consistently with one side.
        Update rule: if independent probes converge on the same offset,
        the case for new physics strengthens; if the offset collapses
        under revised calibration, the systematic explanation gains
        weight.

        State written to sessions/scrutinize_hubble_tension.md
```

The system did not summarize two sides and declare a middle ground. It separated measurement disagreement from interpretation, audited hidden dependencies, identified the binding uncertainty, and specified exactly what evidence would change the verdict. The intended output is structured adversarial reasoning with explicit state, not a conversational compromise.

## The loop

MAPC is a process, not a collection of prompts. Each command applies a different kind of pressure, and the system maintains structured epistemic state across rounds: tensions, claims, alternatives, tests, assumptions, and dependency links, each with lifecycle status and attack history.

The core idea: **the transcript is archival context; the state is the primary object of control.**

| Command | What it does |
|---------|-------------|
| `/diagnose` | Question qualification. Detects malformed, compressed, policy-loaded, or mixed-unit questions and outputs the minimum repaired question set needed before deeper scrutiny. |
| `/extract` | Paper ingestion. Converts an uploaded paper into analyst-grade structured takeaways: what was measured, what was claimed, where the gap is. Feeds into downstream scrutiny or exploration. |
| `/lit-review` | Multi-paper ingestion. Builds a corpus-level evidence map across attached papers: agreements, disagreements, repeated assumptions, method limits, and priority gaps. |
| `/scrutinize` | Attack the leading hypotheses. Find where evidence is circular, overclaimed, or not independent. Preserve only what survives the strongest available attacks. |
| `/reframe` | Challenge whether the current unit of analysis, field boundary, or abstraction level is the right one. Output is a more generative question, not a repaired version of the same one. |
| `/explore` | Map the space of serious live alternatives. Clarify what would have to be true for each to survive. Rank the measurements that would most efficiently move the epistemic state. |
| `/escalate` | Frame-breaker. Forces the next first-principles question when the analysis is converging too smoothly at the wrong level. |
| `/crystallize` | The orchestrator. Decides when to scrutinize, reframe, or explore. The productive default for research-forward tasks: scrutinize first (clear fake certainty), then reframe (replace the question), then explore (map the possibility space). |

## What makes this different

**State, not conversation.** Each round begins from a structured epistemic map, not from the last message. Claims carry attack histories. Evidence lines are checked for shared assumptions. Tensions are preserved as first-class objects that must be resolved or declared irreducible. Nothing quietly disappears between rounds.

**Two-level hardening.** Objects earn structure through two independent gates. Representational hardening promotes a tension into a typed object when it has stable identity, competing positions, and dependency relevance. Operational hardening attaches tests only when discriminative procedures exist. A tension can be structurally important long before it is testable. The system does not collapse those into one decision.

**No appeals to authority.** Every agent operates under a strict constraint: no consensus, no authority, no "experts agree." First principles and primary evidence only. Published research is treated as evidence to be weighed, not as ground truth.

**Explicit update rules.** Every analysis specifies what evidence would change the verdict. Not "more research is needed" but "if X is observed above threshold Y, revise claim Z in direction W."

## What is in this repo

```
.claude/commands/     User-facing Claude Code slash commands
.claude/agents/       Agent prompts (builder, destructor, auditor,
                      falsifier, escalator, synthesizer, coordinator,
                      alternative_builder, extractor, diagnostician,
                      hardening_guard, state_guard)
papers/               Working paper on the framework
schemas/              Minimal object model and lifecycle reference
examples/             Worked example of the hardening lifecycle
sessions/             Generated runtime output (gitignored)
```

## When to use this

**Good fit:**
- The first plausible answer is likely at the wrong level
- Several coherent positions survive initial inspection
- Evidence independence matters and you suspect false convergence
- Premature closure is expensive
- You need to know what survived, what failed, and what would change the result

**Bad fit:**
- Simple factual lookups
- Speed matters more than depth
- The bottleneck is missing information, not reasoning quality

## Working paper

The current paper is [`papers/progressive_crystallization.md`](./papers/progressive_crystallization.md). It argues that the right unit of AI reasoning is not the conversational turn but the epistemic state object, and that the genuinely novel question is when loose tensions should harden into structured claims. The paper is pre-empirical and specifies the result that would kill its own claim.

## Limits

This framework can impose structure and pressure. It cannot create domain competence the underlying model does not have. If the model cannot recognize circular evidence, distinguish genuine tests from fake ones, or separate real constraints from rhetoric, the system will produce well-structured wrong answers.

## Docs

| Doc | What it covers |
|-----|---------------|
| [Working Paper](papers/progressive_crystallization.md) | The conceptual argument: timing policy for formalization in LLM reasoning |
| [Object Model](schemas/epistemic_state_schema.json) | Minimal schema: tension, claim, alternative, test lifecycles |
| [Hardening Walkthrough](examples/adaptive_hardening_walkthrough.md) | Four-round worked example of the promotion ladder |
| [Hardening Snapshots](examples/adaptive_hardening_snapshots.json) | Static state snapshots for the worked example |
| [Runtime State Example](examples/component_attribution_state_example.json) | Tracked sample session state showing canonical IDs, statuses, and test linkage |

The `examples/` directory contains the canonical tracked artifacts. The `sessions/` directory is runtime output and may contain unversioned or throwaway state generated during local use.

## License

MIT. Free forever.
