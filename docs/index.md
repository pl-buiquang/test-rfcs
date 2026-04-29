# Cardiologs RFCs

This site renders the RFC repository for cross-functional readability. Non-GitHub
users can read RFCs here and provide feedback by contacting the RFC Author or CCB
Chair directly.

## What is an RFC?

An RFC (Request for Change) is the SOP-00070 §1 quality record for design
changes to released products. Every RFC is authored as a Pull Request on the
[`test-rfcs` GitHub repository](https://github.com/pl-buiquang/test-rfcs)
and reviewed by the Change Control Board (CCB).

See the [Work Instruction](https://github.com/pl-buiquang/test-rfcs)
for the full process, roles, and quality-record flow.

## Authoring paths

- **Issue Form** (recommended for non-engineers): open a new Issue using the
  "RFC Proposal" template — a Draft PR is created automatically. Edit the
  Issue body to iterate on the RFC.
- **Direct PR** (for engineers): open a PR adding a file under `rfcs/` using
  the [template](https://github.com/pl-buiquang/test-rfcs/blob/main/rfcs/0000-template.md).

## Lifecycle

| Status                | Meaning                                       |
| --------------------- | --------------------------------------------- |
| `status:draft`        | Work in progress, not yet under formal review |
| `status:open-for-review` | Under active CCB review                    |
| `status:accepted`     | Approved for implementation (PR merged)       |
| `status:rejected`     | Not approved (PR closed, rationale recorded)  |
| `status:deferred`     | Parked, with re-evaluation conditions         |
