Run a question-diagnosis pass on the following input:

$ARGUMENTS

Use the `diagnostician` agent directly.

`/diagnose` is the question-qualification mode.
It should:
- determine whether the input question is already in a tractable scientific form
- detect specific form failures before deeper scrutiny begins
- preserve the scientist's intent while stripping policy binaries, false unities, hidden comparators, or compressed causal chains
- output a minimally repaired question set with explicit dependency structure when repair is needed

Use this when:
- the question sounds broad, binary, policy-loaded, or rhetorically inherited from a field
- you want to know whether scrutiny is being aimed at the right empirical object
- you want the minimum surgery needed before `scrutinize`, `explore`, or `reframe`

Required properties:
- stay Claude-native
- no appeals to consensus, authority, or government guidance
- preserve scientific intent rather than substituting a new research agenda
- prefer the minimum repair that makes the question tractable
- make every repair explicit and reversible

Return the Diagnostician artifact exactly as produced.
