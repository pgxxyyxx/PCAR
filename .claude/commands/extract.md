Extract the key analyst-relevant structure from the attached paper or the following paper text:

$ARGUMENTS

Use the `extractor` agent directly.

`/extract` is the paper-ingestion mode.
It should:
- identify the paper's core claim, object of study, and decision-relevant contribution
- separate direct evidence from interpretation, speculation, and rhetoric
- pull out methods, datasets, assumptions, caveats, and failure points
- produce a compact analyst handoff that can feed later `scrutinize`, `reframe`, or `explore` work

Use this when:
- a paper PDF or paper text is attached and needs structured extraction
- you want the key things preserved before deeper analysis
- you need a reusable substrate rather than a prose summary
- for multi-paper review, prefer `/lit-review`

Required properties:
- prioritize what the paper actually measures, not what it implies rhetorically
- distinguish direct findings from author interpretation
- surface missing controls, hidden assumptions, and transfer limits
- quote sparingly and only when the exact wording matters
- if the attachment is incomplete or unreadable, say so plainly and extract only what is actually available

Return:
- paper identification
- research question
- exact central claim
- study design
- data and sample
- key measurements
- main findings
- strongest evidence
- main assumptions
- limitations and caveats
- what would need scrutiny next
- analyst handoff
