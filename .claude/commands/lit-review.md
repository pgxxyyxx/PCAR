Extract and synthesize the key analyst-relevant structure from a set of attached papers or the following paper texts:

$ARGUMENTS

Use the `extractor` agent directly.

`/lit-review` is the multi-paper literature-ingestion mode.
It should:
- work across a corpus of papers rather than one paper at a time
- build a comparative evidence map across studies, methods, datasets, and claims
- separate direct evidence from interpretation, rhetoric, and field-level overreach
- identify where apparent convergence is real versus where it is driven by shared assumptions, repeated proxies, or overlapping datasets
- produce a compact literature-review handoff that can feed later `scrutinize`, `reframe`, `explore`, or `crystallize` work

Use this when:
- multiple paper PDFs or paper texts are attached and need to be reviewed together
- you want a literature map instead of isolated paper summaries
- you need the strongest surviving corpus-level structure before deeper analysis

Required properties:
- preserve a per-paper table with stable paper IDs
- identify cross-paper agreements, disagreements, and dependency structure
- prioritize what the literature actually measures, not what the field rhetorically claims
- surface repeated design weaknesses, missing controls, and transfer limits
- if some attachments are incomplete or unreadable, say so plainly and use only what is actually available

Return:
- review scope
- paper table
- cross-paper patterns
- evidence map
- disagreements and tensions
- method and data limits
- what the literature actually supports
- priority gaps
- literature-review handoff
