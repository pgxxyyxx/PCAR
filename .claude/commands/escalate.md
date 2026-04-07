Run a frame-breaking escalation on the following question or current analysis state:

$ARGUMENTS

Use the `escalator` agent directly.

`/escalate` is the single-question intervention mode.
It should:
- detect whether the discussion is converging inside the wrong frame
- force the next first-principles question instead of summarizing
- expose the missing equation, observable, rate limit, counterfactual, or decision threshold

Use this when:
- the analysis sounds coherent but too smooth
- the argument is staying at the level of analogy or plausibility
- you need the one next question that would materially change the frame
- a prior answer did not specify what would change the result

Required properties:
- stay Claude-native
- do not summarize or arbitrate
- do not appeal to consensus, authority, or literature status
- ask exactly one question
- prefer the escalation modes already defined in the `escalator` agent

Return the Escalator artifact exactly as produced:
- `SHOULD_FIRE`
- `FAILURE_MODE`
- `ESCALATION_MODE`
- `QUESTION`
- `WHY_THIS_IS_REQUIRED`
