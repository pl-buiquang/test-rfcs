---
rfc_id: 0001
title: "Example: tighten pacing detector threshold"
author: "Example Author"
team: "A-Team"
tier: standard
status: draft
date_created: 2026-04-29
date_last_updated: 2026-04-29
tags: [example, algorithm]
---

# RFC-0001: Example: tighten pacing detector threshold

> This is a sample RFC included so the docs site has at least one entry to
> render. Delete or replace it before adopting the repo for real use.

## Summary

Tighten the pacing-detector amplitude threshold from 5% to 3% of baseline to
reduce false-positive pacemaker artifact flags on low-amplitude leads.

## Problem / Motivation

Field reports indicate ~2% of Holter recordings on lead-V1-only studies are
incorrectly flagged as paced. Operators must manually un-flag these,
adding ~30 seconds of review time per recording.

## Approach

Lower the threshold from `0.05 * baseline` to `0.03 * baseline` in the
detector and re-run the regression set on the v3 calibration corpus.

## Impact Triage

| Domain                            | Impact? | Description / Justification                                |
| --------------------------------- | ------- | ---------------------------------------------------------- |
| Design & Development File (DDF)   | Yes     | Algorithm spec and detector unit tests must be updated.    |
| Device function                   | Yes     | Pacing-detector behavior changes.                          |
| Intended use                      | No      | No change to intended use.                                 |
| Device performance                | Yes     | Expected: -2% false-positive rate, no sensitivity loss.    |
| Device safety / risk management   | Yes     | Risk file requires re-review for missed-pacing residual.   |
| Regulatory requirements / filings | Yes     | Performance change >5% threshold likely reportable.        |
| User needs / requirements         | No      | No URD change.                                             |
| Labeling (IFU, labels)            | No      |                                                            |
| Usability                         | No      |                                                            |
| Cybersecurity                     | No      |                                                            |
| Verification & Validation         | Yes     | Regression on v3 corpus + targeted low-amplitude subset.   |
| Training                          | No      |                                                            |

## Who Does This Apply To?

All Cardiologs Holter customers. Activated via standard release; no feature
flag.

## Testing Strategy

- Unit tests for the new threshold value
- Regression on v3 calibration corpus (n=2,400)
- Targeted analysis of the 47 misflagged recordings reported by support

## Pending Questions

- Should this ship as a Service Pack (lightweight) or bundled with the next
  Level Release?
- Risk team to confirm acceptable residual missed-pacing rate.

## Resources

- Linear ticket ALG-432
- Field-report dataset: `s3://cardiologs-research/pacing-fp-2026-q1/`

## Implementation Approach

- [x] Bundled into a Level Release (target: v4.7)
- [ ] Bundled into a Service Pack
- [ ] Implemented as a project (own release vehicle)
- [ ] Other

## CCB Decision

- **Decision**: Pending
- **Decision date**:
- **Approvers**:
- **Rationale**:
- **Re-evaluation conditions** (Defer only):
- **Linked Change Control**: CC_YY_XX
