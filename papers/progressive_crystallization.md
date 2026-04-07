# Progressive Crystallization
## A Timing Policy for Formalization in LLM Reasoning Systems

Working Paper v3 • April 2026

---

## Abstract

This paper introduces a timing policy for formalization in multi-agent LLM reasoning: represent hypotheses loosely at first, and promote them into typed state objects only when they earn it. The paper does not claim novelty for stateful reasoning architectures in general, which are well-established in truth maintenance systems, formal argumentation theory, and blackboard architectures. It claims novelty only for an **adaptive hardening policy** that governs when loose reasoning state should become structured and when structured state should become operationally testable. These are two separate decisions. Representational hardening promotes a tension into a typed object when it has stable identity, competing positions, and nontrivial dependency relevance. Operational hardening attaches executable tests only when discriminative, externally checkable procedures exist and are decision-relevant. We define a minimal object model (tension, claim, alternative, and test as primary types, with assumption and dependency link as structural annotations), walk through a concrete four-round example showing the full promotion ladder, and propose a three-condition experiment whose results would support or falsify the core claim. The experiment has not been run. The framework is pre-empirical.

---

## 1. The Problem

Most multi-agent reasoning systems pass messages. One agent proposes a hypothesis. Another attacks it. A third synthesizes. The transcript grows. But the epistemically important structure is not represented anywhere except implicitly in prose that must be re-parsed every turn. Which assumption was attacked, which claim survived and why, which evidence lines turned out to share a hidden dependency, what observation would revive a weakened alternative: none of this is tracked as structured state.

This means every round partially reconstructs the reasoning state from scratch. A claim that survived a strong attack and a claim that was never attacked look identical in the transcript. A dependency between two evidence lines that was discovered in round 3 may be forgotten by round 7. The system accumulates words without accumulating structure.

The problem is not context window size. A million-token window still contains flat text. The problem is that the objects of reasoning, including claims, tensions, alternatives, and tests, are not first-class objects in the system, and the structural relationships between them, including assumptions they depend on and dependency links that connect them, are not explicitly tracked. All of this exists only as patterns in prose, which means the system cannot operate on it directly. It cannot filter by status, check staleness, trace justification chains, or detect when the same hidden assumption supports three apparently independent evidence lines.

The distinction here is not between text and state. In practice, state will still be generated, updated, and sometimes repaired through language. The distinction is between state implicit in prose, where structure must be reconstructed by re-reading, and state explicitly represented and operated on, where structure persists across operations and supports direct computation.

**The fix is simple to state.** Make epistemic objects first-class. Give them types, lifecycle states, and dependency links. Store them in a structured state object that persists across operations. Reasoning becomes state transformation: read the current epistemic state, apply an operation such as attack, audit, reframe, or test, and write the updated state.

This is not a new idea. Truth maintenance systems (de Kleer, 1986) maintain beliefs with justification trails and dependency tracking under contradiction. Formal argumentation frameworks (Dung, 1995) model reasoning as attack graphs where the admissible set, meaning what survives all available attacks, is computed over the structure. Blackboard architectures (Engelmore and Morgan, 1988) use shared structured state with specialist agents contributing to different regions. Progressive crystallization imports the state-object idea from these traditions and instantiates it on LLM-based multi-agent systems. The import is the easy part.

---

## 2. The Hard Part: When to Harden

If the state-object idea were the whole contribution, this paper would be a reimplementation memo. The hard part is the **timing policy**: when should a loose, exploratory thought earn the right to become a typed, structured claim?

This matters because formalization has costs. The valuable content of early-stage reasoning is often not a well-formed claim. It may be a tension between two framings that has not yet resolved into testable alternatives, a suspicion that apparent evidence convergence is fake because every supporting line shares the same hidden assumption, or an intuition that the current question is wrong and a better one exists but has not yet been articulated. These are states that carry reasoning forward but do not yet have stable identity, competing positions, or testable predictions. Forcing them into typed schemas too early may capture the content while closing off the search directions that made the thought productive.

Too little structure and the system drifts, forgets, and loops. Too much structure and premature ontological commitment collapses the search space. The goal is not maximum formalization but **adaptive formalization**: the minimum structure required to preserve the productive potential of a thought, which changes as the thought matures.

**The honest qualification.** The claim that early formalization hurts LLM reasoning is borrowed from classical AI, where it was established for rule-based systems. LLMs switch between formal and informal registers fluidly. Whether the formalization trap applies with comparable severity to LLM-based reasoning is an open empirical question. If it does not, and if always-formal state works as well as adaptive state, then the hardening policy is unnecessary and this paper reduces to "use structured state between agents." That would be useful engineering but not a contribution.

### 2.1 Two Levels of Hardening

The previous version of this paper treated hardening as a single decision. That was a mistake. There are really two separate questions:

1. **When should a tension become a structured object?** (Representational hardening.)
2. **When should the system spend resources testing it?** (Operational hardening.)

These are not the same question, and collapsing them creates a systematic error. A tension might deserve formal representation, because it has stable identity, clear competing positions, and nontrivial dependency relevance, long before it deserves an expensive external check. Conversely, a loosely held intuition might suddenly become testable before it has earned full structural representation. Tying representation to testability would underrepresent important tensions that are structurally central but not yet externally testable, and would overrepresent trivially checkable claims that have little reasoning weight.

**Representational hardening** promotes a tension into a typed object when three conditions hold:

1. The tension has **stable identity**: it can be named, referenced, and attacked across rounds without being re-derived from prose.
2. It has **competing positions**: at least two distinguishable stances that are not merely verbal variants.
3. It has **dependency relevance**: other reasoning objects (claims, tests, alternatives) depend on how this tension resolves.

**Operational hardening** attaches executable tests to a structured object when two additional conditions hold:

4. A **discriminative procedure exists**: a tool call, dataset query, verifier check, or auditable observation protocol that would produce different results under the competing hypotheses.
5. The procedure is **decision-relevant**: running it would meaningfully update the reasoning state rather than merely confirm what is already settled. This is a heuristic priority judgment, not a formal information-gain calculation. We do not have a formal model for this condition and do not claim one.

The two levels are independently valuable. An object can be representationally hardened (promoted to a structured tension or candidate claim) without being operationally hardened (attached to a runnable test). This matters particularly for conceptual analysis, planning under ambiguity, and strategic reframing, where a tension may be structurally central and worth preserving formally even when no external check is available. In such domains, the valid terminal state is often `frontier` rather than `crystallized_claim`: a tension declared irreducible as a genuine tradeoff, with a structural response indicated rather than a test attached. The framework does not require every object to reach operational hardening. It requires only that no object be promoted beyond what the evidence and structure support.

### 2.2 Three Phases

| Phase | Regime | Representation | Transition criterion | Failure mode if entered too early |
|---|---|---|---|---|
| Exploration | Loose | Natural language with labeled positions. No typed schema. | Default starting state. | N/A |
| Pressure testing | Medium | Typed objects with stable IDs, competing positions, dependency links, and attack history. | Representational hardening: stable identity, competing positions, dependency relevance. | Premature ontological commitment. The search space narrows around a decomposition that may be wrong. |
| Operationalization | Hard | Typed claims with specified or runnable tests, update rules, and explicit hardening rationale. | Operational hardening: discriminative procedure exists and is decision-relevant. | Unsupported precision. The claim looks testable but the test is not genuinely discriminative, or the result would not change anything. |

A single reasoning state may contain objects at all three phases simultaneously. A well-explored tension with a clear discriminative test sits at Phase 3 while a newly discovered category wobble remains at Phase 1. The state is heterogeneous by design.

### 2.3 The Object Model

The minimal object model contains four primary types and two structural annotation types.

**Tension.** An unresolved split between competing positions. Lifecycle: `loose_tension` (labeled but untyped), `structured_tension` (typed with stable ID, competing positions, and dependency links; may be under active pressure or dormant), `reframed` (replaced by a better question), `dissolved` (resolved with justification), `frontier` (declared irreducible as a genuine tradeoff, with structural response indicated). A tension at `frontier` is a valid terminal state: it represents a correctly identified permanent tradeoff that does not require or admit external adjudication. Frontier tensions carry a `structural_response` field describing the design choice or tradeoff surface they imply.

**Claim.** A position that has earned structured representation. Lifecycle: `candidate_claim` (structured but not yet testable), `working` (under active refinement; a claim enters `working` when an operator is actively developing or attacking it within a round, and returns to `candidate_claim` when the round ends if it has not yet been crystallized), `crystallized_claim` (attached to a runnable discriminating test and an explicit hardening rationale), `weakened` (partially undermined but not dead; carries a `revival_condition` field specifying what evidence would restore it), `rejected`.

**Alternative.** A competing explanation or mechanism. Lifecycle: `live`, `narrowed` (compressed into a more serious form), `hybridized` (merged with the leading position), `ruled_out_by_first_principles`, `ruled_out_by_measurement`. Alternatives at `narrowed` or `ruled_out` carry a `revival_condition` field specifying what evidence would make them live again.

**Test.** A discriminating procedure. Lifecycle: `proposed`, `specified` (procedure defined but not yet runnable), `runnable` (can be executed now), `sharpened` (refined after partial results), `decisive` (result would resolve the target), `exhausted` (run with null result), `blocked` (cannot currently be executed).

**Assumption** (structural annotation). A load-bearing presupposition that one or more objects depend on. Assumptions are not standalone lifecycle objects. They are annotations attached to tensions, claims, or alternatives via a `depends_on_assumptions` field. Each assumption has a stable ID, a description, and a `status` of `unexamined`, `examined`, or `undermined`. When an assumption is undermined, all objects that depend on it are flagged for re-evaluation.

**Dependency link** (structural annotation). A directed edge between two objects recording that one depends on, supports, attacks, or tests the other. Dependencies are stored as `{source, relation, target}` triples. The `relation` field takes values such as `depends_on`, `supports`, `attacks`, `tests`, `reinterprets`, or `shares_assumption_with`. The last of these is the mechanism for evidence dependency audits: when two evidence lines are discovered to share a hidden assumption, a `shares_assumption_with` link is created, and the apparent independence of those lines is downgraded.

Each primary object carries an `origin_round`, `last_updated_round`, and stable ID. Claims and tests declare their targets. A `crystallized_claim` is invalid unless it has both an explicit hardening decision and a linked discriminating procedure. A `frontier` tension is valid as a terminal state without a linked test, provided it carries an explicit structural response.

### 2.4 Worked Example

Consider the question: *Does exposing intermediate reasoning improve model faithfulness, or only the appearance of faithfulness?*

**Round 1: Loose tension.** The system has an unresolved split: visibility of reasoning steps may help the model revise itself, or it may only help the verifier or user. This is created as `t1` with status `loose_tension`. No claim is created. No test is promoted. The hardening guard decides: stay loose, because competing positions exist only in rough form and no discriminating procedure is specified.

**Round 2: Representational hardening.** The tension now has stable identity. The competing positions are explicit: Position A holds that visible steps improve the model's own faithfulness; Position B holds that visible steps improve only external trust or verification. The hardening guard promotes `t1` from `loose_tension` to `structured_tension`. Still no claim crystallization. Still no test promotion. The object deserves structure but does not yet deserve a test.

**Round 3: Candidate claim plus specified test.** The structured tension now supports a cleaner hypothesis. The system creates `c1` as a `candidate_claim`: intermediate reasoning visibility improves faithfulness only when the model can revise against the visible steps. Simultaneously, it creates `x1` as a `specified` test: compare direct answer, CoT shown only to user, and CoT plus self-critique loop on accuracy, calibration, and overtrust gap. The claim deserves structure. The test deserves specification. Neither alone means the claim is crystallized.

**Round 4: Crystallized claim.** The state now contains both an explicit hardening rationale and a discriminating procedure that is decision-relevant and runnable. The system promotes `c1` to `crystallized_claim`, `x1` to `runnable`, and dissolves `t1` because the split is no longer only a loose tension.

The important point is the separation. Representational and operational promotions happen on independent schedules. Round 2 promotes representation without promoting testing. Round 3 promotes both, but neither promotion alone constitutes crystallization. Round 4 completes the ladder only because both conditions are jointly satisfied.

### 2.5 What Adaptive Hardening Buys

If the hardening policy works, it produces three things that conversation-based reasoning does not.

**Preserved epistemic structure.** Every claim carries its attack history, justification trail, and dependency links. A claim that survived three attacks is a different object than a claim that was never attacked. The system knows the difference.

**Computable operations on reasoning.** The system can filter all tensions by status, find all claims that depend on a given assumption, identify which evidence lines share a calibration chain, and detect when the same bottleneck has persisted for N rounds without progress. These operations are trivial on structured state and intractable on prose.

**Explicit lifecycle tracking.** A tension can be loose, structured, dissolved, reframed, or frontier. Each status means something different for what happens next. Prose conflates all of these into "we discussed it."

---

## 3. Implementation Context

The timing policy in Section 2 does not fully determine the remaining design choices but constrains them. Any operation that reads and writes epistemic state is an **operator**; the specific set varies by domain. **Mode selection** governs which operator sequences apply: scrutiny for failure-finding, reframing for replacing malformed questions, exploration for mapping alternatives. A **meta-cognitive gating** process can monitor for premature convergence, though it faces a circularity challenge because the gating process may share failure modes with the reasoning process. **Multi-agent structure** is not inherently required but currently helps because single models are unreliable at maintaining disciplined state transitions over long arcs.

---

## 4. What This Is and Is Not

**What it is.** A timing policy for formalization in LLM reasoning systems, instantiated as an engineering proposal with a minimal object model and a two-level hardening mechanism. It is grounded in established formal traditions (TMS, argumentation theory, blackboard architectures).

**What it is not.** It is not a paradigm shift. It is not primarily a theoretical contribution, since the theoretical part, namely when exactly to harden, is the part that is formally underspecified. It is not a validated system.

**What is genuinely novel.** The specific claim that adaptive formalization timing, governed by a two-level promotion policy with separate representational and operational triggers, outperforms both always-formal and never-formal strategies for LLM reasoning. This is a testable empirical claim. It may be wrong.

**What is imported, not invented.** Structured epistemic state with justification trails (de Kleer, 1986), attack graphs and admissibility (Dung, 1995), shared specialist state (Engelmore and Morgan, 1988), defeasible belief revision (Alchourrón et al., 1985), delayed equivocality reduction (Weick, 1995), irreducible tradeoff surfaces (Snowden and Boone, 2007).

---

## 5. The Decisive Test

The framework is pre-empirical. One minimal experiment can strongly constrain the core claim.

**Three conditions:**

| Condition | Description |
|---|---|
| **A** | Full framework: typed epistemic state with two-level adaptive hardening and multi-agent structure |
| **B** | Structured state passing: agents exchange JSON state objects with a fixed schema (always-formal) and multi-agent structure |
| **C** | Single agent: equivalent task instructions, chain-of-thought, no structured state |

**Task construction.** We propose constructing 20 tasks from two domains with different evaluation structures. The first domain is scientific hypothesis evaluation: given conflicting evidence, identify what survives scrutiny and what does not. These tasks have ground-truth answers that can be sealed in advance by domain experts, because the question is what the evidence actually supports rather than what policy to adopt. The second domain is multi-constraint policy analysis: given competing objectives, identify the binding tradeoffs and the strongest considerations on each side. These tasks do not have single correct answers. Instead, they have expert-constructed answer keys specifying which constraints are binding, which alternatives must be named, and which tradeoffs are irreducible. The evaluation criterion for policy tasks is completeness and structural accuracy of the tradeoff map, not convergence on a single recommendation. Each task in both domains must satisfy three criteria: reasoning chain length of five or more steps, an answer structure that shallow analysis systematically misses, and non-recoverability by retrieval alone. Tasks are constructed by domain experts before any system runs, with answer keys sealed.

**Metrics.** Each run is scored by three or more independent raters on a rubric with five dimensions, each scored 1 to 5: constraint coverage (did the system identify the binding constraints?), alternatives considered (did it name and evaluate serious competing explanations?), logical consistency (do conclusions follow from stated premises?), calibration (does confidence match evidence strength?), and state maintenance (are important distinctions preserved across reasoning steps rather than lost or conflated?). Inter-rater reliability is measured by Krippendorff's alpha, with a minimum threshold of 0.7 for the experiment to be considered interpretable.

**Two base models** are used to test generality. All conditions are run on both models.

| Result | Update |
|---|---|
| A outperforms B by more than 0.3 SD | Adaptive hardening has value beyond structured state. Core claim survives. |
| A within 0.5 SD of B | Adaptive hardening adds nothing. The contribution reduces to "use structured state." Hardening policy is unnecessary. |
| B within 0.5 SD of C | Structured state adds nothing. The problem diagnosis is wrong. |
| A within 0.5 SD of C | The entire architecture is epiphenomenal. Invest in better single-agent prompting. |

**Secondary test, conditional on A outperforming B.** Compare the adaptive hardening trigger against always-formal, never-formal, fixed-interval, and disagreement-triggered hardening. If any fixed rule matches the adaptive trigger, the specific trigger mechanism is unnecessary even though hardening policy matters.

These thresholds are provisional and require calibration from a pilot study. But the experimental structure is committed: if always-formal structured state matches adaptive crystallization, the hardening policy, which is the paper's actual contribution, is dead.

---

## 6. The Open Frontier

Is reasoning quality primarily bottlenecked by state management or by the cognitive operations that read and write state? If the bottleneck is state management, the architecture matters. If the bottleneck is base capability, better state management decorates the failure without correcting it. A third factor, the training signal, may cause premature convergence regardless of architecture. The decisive test in Section 5 provides partial evidence but cannot fully separate these. We preserve this as an open question.

---

## 7. Conclusion

This paper introduces a timing policy for formalization in LLM reasoning systems: represent hypotheses loosely at first, and promote them into typed state objects only when they earn it through two independent gates. Representational hardening promotes objects when they have stable identity, competing positions, and dependency relevance. Operational hardening attaches tests when discriminative, externally checkable procedures exist and are decision-relevant. The paper does not claim novelty for stateful reasoning architectures in general. It claims novelty only for the two-level adaptive hardening policy. The claim is testable, pre-empirical, and may be wrong. The test that would falsify it is specified. The test has not been run. That is the honest position.

---

## References

Alchourrón, C. E., Gärdenfors, P., and Makinson, D. (1985). On the logic of theory change: Partial meet contraction and revision functions. *Journal of Symbolic Logic*, 50(2), 510-530.

de Kleer, J. (1986). An assumption-based TMS. *Artificial Intelligence*, 28(2), 127-162.

Dung, P. M. (1995). On the acceptability of arguments and its fundamental role in nonmonotonic reasoning, logic programming and n-person games. *Artificial Intelligence*, 77(2), 321-357.

Engelmore, R. and Morgan, T., editors (1988). *Blackboard Systems*. Addison-Wesley.

Snowden, D. J. and Boone, M. E. (2007). A leader's framework for decision making. *Harvard Business Review*, 85(11), 68-76.

Weick, K. E. (1995). *Sensemaking in Organizations*. Sage Publications.
