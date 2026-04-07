Run a scrutiny-first analysis on the following question:

$ARGUMENTS

Use the `coordinator` agent in `SCRUTINIZE` mode.

Mode objective:
- take the leading hypotheses and rip them apart
- identify where the evidence base fails, becomes circular, or overclaims
- rely only on first principles and primary evidence, both of which should themselves be scrutinized
- preserve any surviving claims only after the strongest available attacks have failed

Required properties:
- stay Claude-native
- no appeals to consensus, authority, or government guidance
- use first principles and primary evidence only
- treat published primary research as evidence, not as unquestioned ground truth
- preserve epistemic state, not just transcript prose
- do not return tiered verdicts, product taxonomies, or broad answer summaries

Return:
- leading hypotheses under scrutiny
- failure map for each
- where the evidence does not hold up
- the narrow remainder that still survives after scrutiny
- most fragile assumptions
- decisive bottleneck
- best break tests
- update rule

Write state to `sessions/`.
