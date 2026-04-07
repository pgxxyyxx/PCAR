Run a reframing analysis on the following question:

$ARGUMENTS

Use the `coordinator` agent in `REFRAME` mode.

Mode objective:
- test whether the question, variable, or decomposition is wrong or too shallow
- identify the better object of inquiry if the current one is defective
- preserve the original question, but do not privilege it if a stronger formulation emerges

Required properties:
- stay Claude-native
- no appeals to consensus, authority, or government guidance
- use first principles and primary evidence
- challenge the frame before converging inside it
- prioritize the better question over the better answer
- do not force numerical or substantive closure inside the original frame if the reframed object is stronger

Return:
- whether the original question is well-posed
- best reformulation
- why the original question is shallow, malformed, or compressive if applicable
- hidden dimensions or latent variables
- most important hidden assumption
- main alternative formulations of the object of inquiry
- strongest answer inside the original frame
- strongest answer after reframing
- strongest discriminating measurement or test

Preferred artifact shape:
- Diagnosis
- Why the original question is shallow
- Best reformulated question
- Strongest answer inside original frame
- Strongest answer after reframing
- Main alternative formulations
- Most important hidden assumption
- Best discriminating test

Write state to `sessions/`.
