# Scientific Controversy Workflow (SCW)
## A Workflow Layer for Field-Advancing Investigation

Working Paper v1 • April 2026

---

## Abstract

This paper introduces a workflow layer for scientific controversy investigation. Its purpose is not to improve the quality of a single reasoning step, but to determine **which reasoning operations should occur, in what order, on what object**. The motivating problem is that many important scientific questions arrive in malformed form: policy binaries in place of empirical questions, category bundles treated as natural kinds, downstream readouts treated as the true object of uncertainty, and compressed causal chains that hide separable claims. Running high-quality scrutiny on the wrong question produces disciplined irrelevance.

The proposed workflow contains five primary operations: **question diagnosis**, **domain structure mapping**, **assumption inventory**, **evidence independence audit**, and **research agenda construction**. The workflow is designed for bounded live controversies rather than entire disciplines. Its target artifact is not a one-shot answer but a persistent, updatable dossier: what the real sub-questions are, what assumptions are load-bearing, where apparent convergence is fake, and what measurements or analyses would most efficiently move the controversy forward.

This paper is complementary to MAPC rather than a replacement for it. MAPC is a reasoning engine for rigorous epistemic state transitions inside an operation. SCW is a workflow for deciding which operation should run next. The framework is pre-empirical. Its novelty claim is practical rather than theoretical: that explicit workflow control over controversy analysis produces more field-advancing outputs than direct question-answering or undifferentiated literature review.

---

## 1. The Problem

Most research tooling starts too late. It begins after the question has already been accepted as the right object of inquiry. A model is asked to summarize a literature, critique a claim, or suggest experiments. But in many live controversies, the question itself is malformed.

Three recurring failure modes illustrate the problem:

- A **policy binary** stands in for empirical inquiry. "Is MMR safe?" is not a scientific question. It compresses adverse-event causality, subgroup susceptibility, rate estimation, and counterfactual risk into a single rhetorical predicate.
- A **downstream readout** is treated as the real controversy. "What is the Hubble constant?" compresses measurement consistency, model dependence, and new-physics hypotheses into one parameter.
- A **false unit** is treated as if it were natural. "Does saturated fat cause cardiovascular disease?" bundles multiple molecular species, replacement nutrients, population scopes, and causal links into one label.

In each case, the problem is not only that the field is uncertain. The problem is that the field may be uncertain about the wrong object.

This creates a systematic failure mode for both humans and models. Scrutiny gets applied to whatever vocabulary the field inherited from its own history, not necessarily to the object that would most efficiently reduce uncertainty. The result is often impressive reasoning about an ill-formed target.

**The fix is not merely better debate.** The fix is a workflow layer that diagnoses the question, reconstructs the actual investigative object, maps its dependency structure, and only then begins scrutiny.

---

## 2. What This Layer Is

SCW is a workflow layer for scientific investigation. It governs:

1. whether the input question is in tractable form
2. what type of epistemic object is actually under dispute
3. which assumptions are load-bearing
4. whether the evidence base is genuinely independent
5. what next measurement or analysis would most efficiently move the controversy

The workflow is designed for **bounded scientific controversies**, not entire disciplines. Good units of analysis are things like:

- the Hubble tension
- dietary saturated fat and cardiovascular disease
- vaccine-associated febrile seizure susceptibility
- the amyloid hypothesis in Alzheimer's disease

These objects are large enough to matter and small enough to investigate deeply.

The output of SCW is not "the answer." It is a structured investigation artifact:

- the repaired question set
- the controversy structure
- the assumption register
- the evidence dependency graph
- the ranked research agenda

---

## 3. What This Layer Is Not

SCW is not a reasoning engine. It does not itself guarantee rigorous state transitions, disciplined attack logic, or correct hardening behavior. Those are engine-level concerns.

SCW is not a replacement for domain knowledge. If the underlying system cannot recognize that two lines of evidence share a calibration chain, or that a category is hiding multiple mechanisms, the workflow can at best surface uncertainty about that diagnosis.

SCW is not a policy recommender. It is designed to make empirical uncertainty and next research moves explicit, not to collapse them into action guidance.

SCW is not a field-wide ontology. It is controversy-bounded by design. Scaling to larger domains is possible later, but the intended unit is the live dispute, not "physics" or "medicine."

---

## 4. The Five Operations

### 4.1 Question Diagnosis

The first operation asks whether the input is already in a tractable scientific form. This is not reframing in the generative sense. It is **qualification**: the minimum surgery required before deeper analysis begins.

Typical failure modes include:

- `policy_binary`
- `scope_universalization`
- `wrong_abstraction_level`
- `category_error`
- `causal_chain_compression`
- `mechanism_free_association`
- `comparison_without_comparator`
- `anomaly_compression`

The output is:

- an intent diagnosis
- a tractability verdict
- the failure modes present
- the minimum repair actions
- a repaired question set
- a dependency order among the repaired questions

The key constraint is intent preservation. The question must be repaired without silently substituting a different research agenda.

### 4.2 Domain Structure Mapping

Once the question has been qualified, the next step is to identify the structure of the controversy itself. Three recurrent shapes matter:

- **causal chain**: A -> B -> C -> outcome
- **branching controversy**: several separable sub-disputes with dependency order
- **evidence matrix**: entities × outcomes × populations, where each cell may differ

This step determines where scrutiny should be applied. A chain should be attacked link by link. A branching controversy should be resolved in dependency order. An evidence matrix should not be collapsed into a single aggregate verdict.

### 4.3 Assumption Inventory

For each node in the mapped structure, identify the load-bearing assumptions. Classify them as:

- tested and robust
- tested and contested
- untested but acknowledged
- untested and invisible

The last category is usually the highest-value target. Entire controversies often remain live because invisible assumptions were never made explicit enough to test directly.

### 4.4 Evidence Independence Audit

This step asks whether apparent convergence is real. Given a set of supporting evidence lines, what is the minimal set of shared assumptions whose failure would explain the appearance of agreement?

This operation is the clearest separation between SCW and ordinary literature review. Ordinary review counts supporting studies. Independence audit asks whether those studies are correlated through:

- shared measurement instruments
- shared calibration chains
- shared populations
- shared model assumptions
- shared preprocessing or selection logic

The output is a dependency graph of the evidence base, not just a list of papers.

### 4.5 Research Agenda Construction

Only after the first four operations can a research agenda be meaningfully ranked. The agenda should prioritize:

- load-bearing assumptions that remain invisible or weakly tested
- apparent convergences that collapse under dependency audit
- studies or analyses that already appear runnable on existing data
- genuinely decisive new measurements when reanalysis is insufficient

The ranking criterion is not novelty or rhetorical importance. It is expected epistemic value: how much uncertainty would be removed per unit of feasible effort.

---

## 5. Diagnose Is Not Reframe

The strongest operational distinction in the workflow is between **question diagnosis** and **reframing**.

Diagnosis asks:

- Is this question tractable?
- What formal failures does it have?
- What minimum repair is needed?

Reframing asks:

- Even if this question is tractable, is it the right one?
- Is the field's unit of analysis itself limiting progress?
- Would a more upstream, more generative, or less field-bounded question be better?

Diagnosis has a correct-or-incorrect component. A question either does or does not contain a policy binary, a missing comparator, or a category error. Reframing is different. It is a challenge to the field's current carve-up of the object. It is more exploratory, more optional, and more generative.

The workflow therefore treats diagnosis as the default gate and reframing as a separate operation that can be invoked before or after deeper scrutiny.

---

## 6. Relationship to MAPC

MAPC and SCW operate at different levels.

| Layer | Governs | Primary object |
|---|---|---|
| MAPC | quality of individual epistemic state transitions | claims, tensions, alternatives, tests |
| SCW | sequencing of investigative operations | controversy workflow |

MAPC asks: did this reasoning step preserve the right tensions, apply the right attacks, and harden objects at the right time?

SCW asks: was this the right operation to run in the first place?

The systems are complementary. SCW should be able to call MAPC as its reference reasoning engine. But the coupling should remain minimal. MAPC can be used without SCW, and SCW should in principle be able to operate with another engine that conforms to the same state contract.

The clean interface is a shared typed state object:

- questions or sub-questions under active investigation
- tensions
- claims
- alternatives
- tests
- assumptions
- dependency links
- reliability flags

MAPC reads and writes this state at high rigor. SCW reads that state to decide which operation should happen next.

---

## 7. Implementation Implications

If SCW is implemented as commands on top of MAPC, the minimum command set is:

- `/diagnose`
- `/map-structure`
- `/inventory`
- `/audit-independence`
- `/agenda`
- `/reframe`

Not all of these need to exist immediately as separate commands. But they are distinct operations and should be named as such internally even if early implementations are thin.

The most immediate implementation consequences are:

1. **Question qualification must become first-class.** Deeper scrutiny should not be the default first move on an unqualified input.
2. **Per-turn state updates matter.** If engine outputs only prose and the structured state is reconstructed at the end, SCW will not have a reliable handoff surface.
3. **Repaired question sets need explicit dependency order.** One malformed question may decompose into several tractable ones.
4. **Evidence independence must become operational.** The `shares_assumption_with` idea is only useful if it is invoked deliberately, not left as an incidental side effect.

---

## 8. Worked Sketches

### 8.1 Saturated Fat and CVD

The input question appears to be a single causal question. Diagnosis reveals causal-chain compression, category error, and comparison-without-comparator. The repaired question set separates:

- effect of specific SFA subclasses on LDL-related markers
- relationship between those markers and clinical events
- end-to-end causal chain under explicit replacement nutrients
- population and matrix effects

The controversy structure is a causal chain with population modifiers. The research agenda then naturally prioritizes link-breaking tests and subgroup analyses rather than repeating aggregate association studies.

### 8.2 Hubble Tension

The naive question treats H0 as the unit of inquiry. Diagnosis reveals wrong abstraction level and anomaly compression. The repaired structure separates:

- late-universe measurement consistency
- model dependence of early-universe inference
- new-physics proposals conditional on the first two

The controversy structure is branching with dependency order. This immediately changes the research agenda: several attractive new-physics moves become downstream rather than first-order priorities.

### 8.3 MMR Safety

The input question is a policy binary with a category bundle. The repaired question set separates:

- specific adverse events
- specific vaccine components
- specific subpopulations
- causal rate questions rather than "safe/unsafe"

The controversy structure becomes an evidence matrix rather than a binary verdict. This allows a research agenda focused on susceptibility stratification and mechanism where genuine uncertainty remains, while leaving already well-resolved claims out of the live frontier.

---

## 9. The Decisive Test

SCW is also pre-empirical. Its core claim is not that it makes answers sound better. Its claim is that workflow control improves the usefulness of the final artifact.

One minimal experiment would compare three conditions on a set of bounded scientific controversies:

| Condition | Description |
|---|---|
| **A** | Direct scrutiny with a strong reasoning engine, no explicit workflow layer |
| **B** | SCW workflow plus the same reasoning engine |
| **C** | Conventional literature summary and open-ended critique |

Tasks should be selected so that:

- the initial user question is meaningfully malformed or compressed
- there is a live controversy with multiple coherent alternatives
- a forward-moving research agenda is possible

Outputs should be scored on:

- question repair quality
- structure identification quality
- assumption visibility
- evidence independence handling
- usefulness of the proposed research agenda

If condition B does not materially outperform A on these dimensions, then SCW adds little beyond a strong reasoning engine and should be collapsed back into prompt engineering. That is the falsification condition.

---

## 10. Conclusion

MAPC addresses one hard problem in LLM reasoning: how to preserve and harden epistemic state without premature closure. SCW addresses a different one: how to decide what question should actually be investigated, what structure the controversy has, and what sequence of operations should be applied.

The distinction matters because disciplined scrutiny of the wrong object does not advance a field. Scientific controversies often remain stuck not only because the evidence is weak, but because the field has inherited malformed questions and compressed units of analysis from its own history.

The contribution of SCW is therefore modest but practical: make controversy workflow explicit. Diagnose the question. Map the structure. Inventory the assumptions. Audit independence. Then, and only then, build a research agenda.

The framework is pre-empirical and may be wrong. But it states a concrete claim that can be tested: that explicit workflow control over scientific controversy analysis produces more field-advancing outputs than direct critique alone.
