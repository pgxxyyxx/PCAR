# Progressive Crystallization
## Epistemic State Transition as the Unit of AI Reasoning

Working Paper v3 • April 2026

---

## Abstract

Multi-agent AI reasoning systems are typically organized around the wrong unit. The conversational turn, in which one agent speaks and another responds, is a communication primitive, not a reasoning primitive. This paper argues that the more productive unit is the **epistemic state**: a structured, mutable object containing claims, tensions, assumptions, dependency links, and tests, each with lifecycle status. Reasoning is then state transformation: each operation reads the current state, applies pressure, and writes a new state. The key design decision is **when state should harden**, that is, when a loose tension earns the right to become a typed, structured claim. We propose one trigger: a tension hardens when it can generate discriminative predictions with an externally checkable procedure. Most other decisions in multi-agent reasoning design, including operator choice, agent roles, and mode selection, are shaped by this commitment, though operator and mode choices also shape what state transitions are possible. The argument is grounded in truth maintenance systems, formal argumentation theory, and blackboard architectures, from which the state-object idea is imported. The adaptive hardening policy is the contribution under test. No empirical validation exists. We propose the minimal experiment that would support or falsify the claim.

---

## 1. The Wrong Unit

Most multi-agent reasoning systems pass messages. One agent proposes a hypothesis. Another attacks it. A third synthesizes. The transcript grows. But the epistemically important structure is not represented anywhere except implicitly in prose that must be re-parsed every turn. Which assumption was attacked, which claim survived and why, which evidence lines turned out to share a hidden dependency, what observation would revive a weakened alternative: none of this is tracked as structured state.

This means every round partially reconstructs the reasoning state from scratch. A claim that survived a strong attack and a claim that was never attacked look identical in the transcript. A dependency between two evidence lines that was discovered in round 3 may be forgotten by round 7. The system accumulates words without accumulating structure.

The problem is not context window size. A million-token window still contains flat text. The problem is that the **objects of reasoning**, including claims, tensions, assumptions, dependency links, tests, and revival conditions, are not first-class objects in the system. They exist only as patterns in prose, which means the system cannot operate on them directly. It cannot filter by status, check staleness, trace justification chains, or detect when the same hidden assumption supports three apparently independent evidence lines.

**The fix is simple to state.** Make epistemic objects first-class. Give them types, lifecycle states, and dependency links. Store them in a structured state object that persists across operations. Reasoning becomes state transformation: read the current epistemic state, apply an operation such as attack, audit, reframe, or test, and write the updated state. The transcript is a log. The state is the reasoning.

This is not a new idea. Truth maintenance systems (de Kleer, 1986) maintain beliefs with justification trails and dependency tracking under contradiction. Formal argumentation frameworks (Dung, 1995) model reasoning as attack graphs where the admissible set, meaning what survives all available attacks, is computed over the structure. Blackboard architectures (Engelmore and Morgan, 1988) use shared structured state with specialist agents contributing to different regions. Progressive crystallization imports the state-object idea from these traditions and instantiates it on LLM-based multi-agent systems. The import is the easy part.

---

## 2. The Hard Part: When to Harden

If the state-object idea were the whole contribution, this paper would be a reimplementation memo. The hard part is the **phase transition policy**: when should a loose, exploratory thought earn the right to become a typed, structured claim?

This matters because formalization has costs. The valuable content of early-stage reasoning is often not a well-formed claim. It may be a tension between two framings, a half-seen analogy, a suspicion that apparent evidence convergence is fake, or an intuition that the question itself is wrong. These are pre-object states. Forcing them into `{type: "claim", status: "proposed"}` too early may capture the content while killing the generative ambiguity that made the thought productive.

Too little structure and the system drifts, forgets, and loops. Too much structure and premature ontological commitment collapses the search space. The frontier is not maximum formalization but **adaptive formalization**: the minimum structure required to preserve the epistemic energy of a thought, which changes as the thought matures.

**The honest qualification.** The claim that early formalization hurts LLM reasoning is borrowed from classical AI, where it was established for rule-based systems. LLMs switch between formal and informal registers fluidly. Whether the formalization trap applies with comparable severity to LLM-based reasoning is an open empirical question. If it does not, and if always-formal state works as well as adaptive state, then the hardening policy is unnecessary and this paper reduces to "use structured state between agents." That would be useful engineering but not a contribution.

### 2.1 The Hardening Trigger

We propose one trigger: **a tension hardens when it can generate discriminative predictions.**

Operationally, three conditions must be jointly satisfied:

1. **Competing hypotheses imply mutually exclusive observable outcomes** under specified conditions.
2. **An externally checkable procedure exists**, such as a tool call, dataset query, verifier check, or auditable observation protocol, that would produce different results under the competing hypotheses.
3. **The procedure is worth running**, meaning it would meaningfully update the state rather than merely confirm what is already settled. This is a heuristic priority judgment, not a formal information-gain calculation. We do not have a formal model for this condition and do not claim one.

Before this threshold, the system maintains the tension in loose representation: a natural-language description with labeled competing positions but no typed schema. After the threshold is crossed, the tension crystallizes into structured claims with explicit dependency links and specified tests.

The trigger is designed to prevent two failure modes. Hardening too early, before a discriminative test exists, produces unsupported objects: formally typed claims that look precise but cannot be tested. Hardening too late, after the reasoning has moved on, loses structure that should have been preserved.

### 2.2 Three Phases

| Phase | Regime | Representation |
|---|---|---|
| Exploration | Loose | Tensions, fragments, competing framings, unresolved paradoxes, expressed as natural language with labeled positions |
| Pressure testing | Medium | Explicit assumptions, contradiction links, attack nodes, dependency structure, candidate tests |
| Operationalization | Hard | Typed claims with evidence classes, failure maps, decision branches, executable test specifications, update rules |

The phase model is not prescriptive per object. A single reasoning state may contain objects at all three phases simultaneously. A well-explored tension with a clear discriminative test sits at Phase 3 while a newly discovered category wobble remains at Phase 1. The state is heterogeneous by design.

### 2.3 What Adaptive Hardening Buys

If the hardening policy works, it produces three things that conversation-based reasoning does not.

**Preserved epistemic structure.** Every claim carries its attack history, justification trail, and dependency links. A claim that survived three attacks is a different object than a claim that was never attacked. The system knows the difference.

**Computable operations on reasoning.** The system can filter all tensions by status, find all claims that depend on a given assumption, identify which evidence lines share a calibration chain, and detect when the same bottleneck has persisted for N rounds without progress. These operations are trivial on structured state and intractable on prose.

**Explicit lifecycle tracking.** A tension can be live (unresolved, under active pressure), dissolved (resolved with justification), reframed (replaced by a better question), or frontier (declared irreducible as a genuine tradeoff rather than a failure of analysis). Each status means something different for what happens next. Prose conflates all of these into "we discussed it."

---

## 3. Downstream Design Choices

The following implementation choices shape the state-transition framework in practice but are not the core argument. Operator and mode choices partly determine what state transitions are possible, so "downstream" does not mean "unimportant." It means that the state-object commitment comes first and these choices are made in service of it.

**Operators** are any operations that read epistemic state and write updated epistemic state. Useful ones include tension preservation, frame audit, failure mapping, dependency audit, and discriminative test generation. The specific set is a design parameter that will vary by domain.

**Mode selection** governs which operator sequences apply. Scrutiny mode prioritizes failure-finding. Reframing mode prioritizes replacing malformed questions. Exploration mode maps the space of live alternatives.

**Meta-cognitive gating** monitors the reasoning state for signatures of premature convergence and forces level changes before crystallization is permitted. This faces a circularity challenge because the gating process may share failure modes with the reasoning process. Mitigations include operating on metadata patterns rather than content, or replacing LLM-based gating with simple heuristics.

**Multi-agent structure** is not inherently required. Multiple agents currently help because single models are unreliable at maintaining disciplined state transitions over long arcs, but optimal agent count should decrease as single-model reasoning improves.

---

## 4. What This Is and Is Not

**What it is.** A concrete architectural commitment, specifically epistemic state objects as the unit of reasoning with adaptive hardening, instantiated on LLM multi-agent systems. It is an engineering proposal grounded in established formal traditions (TMS, argumentation theory, blackboard architectures) with one novel mechanism, the adaptive hardening policy, that is specified but untested.

**What it is not.** It is not a paradigm shift. It is not primarily a theoretical contribution, since the theoretical part, namely when exactly to harden, is the part that is formally underspecified. It is not a validated system. The operators and mode selection are design choices rather than core theoretical contributions.

**What is genuinely novel.** The specific claim that adaptive formalization timing, controlled by a discriminative-prediction trigger, outperforms both always-formal and never-formal strategies for LLM reasoning. This is a testable empirical claim. It may be wrong.

**What is imported, not invented.** Structured epistemic state with justification trails (de Kleer, 1986), attack graphs and admissibility (Dung, 1995), shared specialist state (Engelmore and Morgan, 1988), defeasible belief revision (Alchourrón et al., 1985), delayed equivocality reduction (Weick, 1995), irreducible tradeoff surfaces (Snowden and Boone, 2007).

---

## 5. The Decisive Test

The framework is pre-empirical. One minimal experiment can strongly constrain the core claim.

**Three conditions:**

| Condition | Description |
|---|---|
| **A** | Full framework: typed epistemic state with adaptive hardening and multi-agent structure |
| **B** | Structured state passing: agents exchange JSON state objects with a fixed schema (always-formal) and multi-agent structure |
| **C** | Single agent: equivalent task instructions, chain-of-thought, no structured state |

**Task requirements.** Reasoning chains of five or more steps, ground truth or expert-rated correct answers, tasks where premature closure is penalized because shallow analysis systematically misses the answer, and tasks not recoverable by retrieval alone.

**Metrics.** Expert-rated rubric covering constraint coverage, alternatives considered, logical consistency, calibration, and state maintenance across reasoning steps.

| Result | Update |
|---|---|
| A outperforms B by more than 0.3 SD | Adaptive hardening has value beyond structured state. Core claim survives. |
| A within 0.5 SD of B | Adaptive hardening adds nothing. The contribution reduces to "use structured state." Hardening policy is unnecessary. |
| B within 0.5 SD of C | Structured state adds nothing. The problem diagnosis is wrong. Multi-agent state loss is not the bottleneck. |
| A within 0.5 SD of C | The entire architecture is epiphenomenal. Invest in better single-agent prompting. |

**Secondary test, conditional on A outperforming B.** Compare the adaptive hardening trigger against always-formal, never-formal, fixed-interval, and disagreement-triggered hardening. If any fixed rule matches the adaptive trigger, the specific trigger mechanism is unnecessary even though hardening policy matters.

These thresholds are provisional and require calibration from a pilot study. But the experimental structure is committed: if always-formal structured state matches adaptive crystallization, the hardening policy, which is the paper's actual contribution, is dead.

---

## 6. The Open Frontier

There is an irreducible tension underneath the state-transition argument that this paper cannot resolve.

**Is reasoning quality primarily bottlenecked by state management or by the cognitive operations that read and write state?**

If the bottleneck is state management, meaning premature closure, lost dependencies, and mode errors, then the state-transition architecture matters and will produce measurable gains. If the bottleneck is the quality of the operations themselves, meaning weak failure analysis, shallow latent variable search, and inability to distinguish verbal from ontological disagreement, then better state management decorates the failure without correcting it.

These two positions produce identical symptoms. A model that resolves a contradiction too quickly could lack either control discipline or analytical capability. The decisive test in Section 5 provides partial evidence: if the full framework outperforms the structured-state-only condition, something about the control policy matters beyond mere state representation. But even a positive result leaves open how much of the gain comes from state structure versus the quality of what the agents do within that structure.

A third factor is the training signal. A model with strong capabilities and good state management may still collapse tensions prematurely if trained to reward smooth coherence over maintained uncertainty. This precedes architecture.

We preserve this frontier. By the argument of this paper, it should harden only when someone can specify an experiment that distinguishes among state management, base capability, and training signal as the binding constraint on reasoning quality. That experiment does not yet exist in a clean form.

---

## 7. Conclusion

The argument is simple. Multi-agent reasoning systems are typically organized around conversational turns. They should be organized around epistemic state objects. Reasoning is state transformation. The interesting design question is when state should harden from loose exploration to structured claims. We propose that it should harden when a tension can generate discriminative predictions with an externally checkable procedure. Most other decisions, including operators, modes, gating, and agent count, are shaped by this commitment.

This is an architectural commitment with one novel empirical claim: that adaptive hardening beats fixed formalization. The claim is testable, pre-empirical, and may be wrong. The test that would kill it is specified. The test has not been run. That is the honest position.

---

## References

Alchourrón, C. E., Gärdenfors, P., and Makinson, D. (1985). On the logic of theory change: Partial meet contraction and revision functions. *Journal of Symbolic Logic*, 50(2), 510-530.

de Kleer, J. (1986). An assumption-based TMS. *Artificial Intelligence*, 28(2), 127-162.

Dung, P. M. (1995). On the acceptability of arguments and its fundamental role in nonmonotonic reasoning, logic programming and n-person games. *Artificial Intelligence*, 77(2), 321-357.

Engelmore, R. and Morgan, T., editors (1988). *Blackboard Systems*. Addison-Wesley.

Snowden, D. J. and Boone, M. E. (2007). A leader's framework for decision making. *Harvard Business Review*, 85(11), 68-76.

Weick, K. E. (1995). *Sensemaking in Organizations*. Sage Publications.
