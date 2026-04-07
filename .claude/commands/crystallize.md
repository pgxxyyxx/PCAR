Run the progressive crystallization loop on the following question:

$ARGUMENTS

Use the `coordinator` agent to run a Claude-native first-principles reasoning loop in `CRYSTALLIZE` mode.

`/crystallize` is the automatic orchestration mode.
It should decide when to:
- scrutinize the leading hypotheses
- reframe the question
- explore serious alternatives

For questions that explicitly seek:
- a novel research agenda
- real alternatives
- what would move the field
- what the current evidence base is missing

it should bias toward:
- `scrutinize -> reframe -> explore`

Do not assume the current framing is correct.
Do not assume convergence should happen immediately.

Required properties:
- stay Claude-native
- no appeals to consensus or authority
- preserve first-principles reasoning
- preserve epistemic state, alternatives, residuals, and update rules
- use scrutiny, reframing, and exploration in the order most likely to produce the strongest surviving structure or research agenda
- force counterfactual and backward-chaining questions through the escalator when needed

Return:
- the sequence of modes chosen and why
- the sequence of operators used and why
- whether the question had to be reframed
- the strongest surviving structure produced by the sequence
- the most important residual or frontier left open
- the decisive bottleneck
- the best next tests or research actions
- the update rule for what would change the result

Do not invent quantitative contribution estimates, thresholds, or effect shares unless they are:
- directly grounded in cited primary evidence
- explicitly derived from the current reasoning
- or clearly labeled as heuristic placeholders

Write state to `sessions/`.
