---
rfc_id: 0000
title: "RFC Template"
author: "<First Last>"
team: "<owning team>"
tier: standard
status: draft
date_created: 2026-04-29
date_last_updated: 2026-04-29
tags: []
---

# RFC-0000: RFC Template

> This file is the canonical template referenced by Appendix A of the WI.
> Do not edit the rfc_id or filename — copy this file as
> `rfcs/XXXX-short-title.md` for new RFCs.

## Summary

One-paragraph explanation of the proposed change.

## Problem / Motivation

Why is this change needed? What problem does it solve or what opportunity does
it address? Include enough context for a reader unfamiliar with the topic.

## Approach

Describe how you intend to solve the problem. Implementation details can be as
rough or as detailed as needed. Include diagrams, pseudocode, API designs, or
architecture drawings as appropriate.

## Impact Triage

For each domain, indicate Yes or No. If Yes, briefly describe the impact and
any actions needed. If No, provide a brief justification.

| Domain                              | Impact? | Description / Justification |
| ----------------------------------- | ------- | --------------------------- |
| Design & Development File (DDF)     |         |                             |
| Device function                     |         |                             |
| Intended use                        |         |                             |
| Device performance                  |         |                             |
| Device safety / risk management     |         |                             |
| Regulatory requirements / filings   |         |                             |
| User needs / requirements           |         |                             |
| Labeling (IFU, labels)              |         |                             |
| Usability                           |         |                             |
| Cybersecurity                       |         |                             |
| Verification & Validation           |         |                             |
| Training (internal or external)    |         |                             |

## Who Does This Apply To?

Is there a need for feature flags? Is this for all users or a subset? How will
this be activated?

## Testing Strategy

How will the change be verified? Link to test plans or describe the approach.

## Pending Questions

List any unresolved questions you would like reviewers to address.

## Resources

Links to related RFCs, design mocks, technical documents, external references.

## Implementation Approach

Tick one and briefly describe:

- [ ] Bundled into a Level Release (specify target version if known)
- [ ] Bundled into a Service Pack
- [ ] Implemented as a project (own release vehicle)
- [ ] Other (describe)

## CCB Decision

_Filled by the CCB Chair at decision time. Until then, leave as "Pending"._

- **Decision**: Pending | Accept | Reject | Defer
- **Decision date**: YYYY-MM-DD
- **Approvers**: (filled from PR review state at decision time)
- **Rationale**: (mandatory for Reject and Defer; optional for Accept)
- **Re-evaluation conditions** (Defer only):
- **Linked Change Control**: CC_YY_XX (filled when assigned to a release)
