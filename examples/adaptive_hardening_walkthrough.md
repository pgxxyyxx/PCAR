# Adaptive Hardening Walkthrough

This is a minimal worked example showing the lifecycle the repo is now trying to support:

`loose_tension -> structured_tension -> candidate_claim -> crystallized_claim`

with operational test promotion tracked separately:

`none -> specified -> runnable`

## Question

Does exposing intermediate reasoning improve model faithfulness, or only the appearance of faithfulness?

## Round 1: Loose Tension

The system has not yet earned a stable claim. It only has a live unresolved split:

- visibility may help the model revise itself
- visibility may only help the verifier or user

At this stage the object should remain loose. The point is to preserve the tension without pretending the system already knows what exact claim is under test.

Expected state move:

- create `t1` as a `loose_tension`
- do not create a claim yet
- do not promote a test yet

## Round 2: Structured Tension

The same tension now has stable identity. The competing positions are clearer and worth preserving structurally:

- Position A: visible steps improve the model's own faithfulness
- Position B: visible steps improve only external trust or verification

This is representational hardening, not yet claim crystallization.

Expected state move:

- promote `t1` from `loose_tension` to `structured_tension`
- still avoid claim crystallization
- still avoid runnable test promotion

## Round 3: Candidate Claim Plus Specified Test

Once the structured tension supports a cleaner hypothesis, the system can promote a candidate claim:

- `c1`: intermediate reasoning visibility improves faithfulness only when the model can revise against the visible steps

At the same time, the system can promote a test specification without claiming the result is already crystallized:

- `x1`: compare direct answer, CoT shown only to user, and CoT plus self-critique loop on accuracy, calibration, and overtrust gap

This is the key separation:

- the claim deserves structure
- the test deserves specification
- neither point alone means the claim is already crystallized

Expected state move:

- keep `t1` as `structured_tension`
- create `c1` as `candidate_claim`
- create `x1` as `specified`

## Round 4: Crystallized Claim

Only once the state contains both:

- an explicit hardening rationale
- a discriminating procedure that is decision-relevant and runnable

should the claim be promoted to `crystallized_claim`.

At this point:

- `t1` can dissolve because the split is no longer only a loose tension
- `c1` can become `crystallized_claim`
- `x1` can become `runnable`

Expected state move:

- `t1`: `structured_tension -> dissolved`
- `c1`: `candidate_claim -> crystallized_claim`
- `x1`: `specified -> runnable`

## Why This Example Matters

This example is intentionally small. Its job is not to prove the framework works. Its job is to make the implementation target concrete.

The important distinction is:

- **representational hardening**: this object deserves stable structure
- **operational hardening**: this object deserves a specified or runnable test

The system should not collapse those into one step.

## Reference Data

The matching static state snapshots live in:

- [`examples/adaptive_hardening_snapshots.json`](./adaptive_hardening_snapshots.json)
