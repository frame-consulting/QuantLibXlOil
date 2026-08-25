# QuantLib Upgrade Reviewer Checklist

Use this checklist when reviewing an upgrade run executed with the upgrade-quantlib skill.

## 1) Version and Environment

- [ ] `current_quantlib_version` is explicitly stated and not inferred from an already-upgraded runtime.
- [ ] `new_quantlib_version` is explicitly stated.
- [ ] `installed_quantlib_version` is shown from the active `xloil` environment.
- [ ] Baseline lock checkpoint is present and values are consistent.

## 2) SWIG Evidence

- [ ] SWIG diff command is shown: `git diff --name-status <from> <to> -- SWIG/*.i`.
- [ ] Added/modified/removed SWIG files are listed clearly.
- [ ] If SWIG diff is empty, broader diff inspection is shown and classified (`wrapper-impacting` vs `likely-non-wrapper`).

## 3) Wrapper Mapping and Edits

- [ ] Each changed SWIG file is mapped to the wrapper module (or user confirmation is recorded for ambiguous mapping).
- [ ] Symbol-level changes are documented (added/updated/deprecated/removed).
- [ ] Runtime behavior checks are included where relevant (defaults, handles, pricing engines, fixings).

## 4) Testing

- [ ] Module tests were run for each affected module and results are recorded.
- [ ] Failures were either fixed or explicitly flagged as environment blockers.
- [ ] At least one targeted cross-module regression test is included when shared behavior may be affected.

## 5) Decision Log and Summary Quality

- [ ] Module decisions are recorded (`continued`, `skipped`, `deferred`) when interactive gating is used.
- [ ] UpgradeSummary includes verification evidence with command + output summary.
- [ ] Residual risks/follow-up items are captured (or explicitly `None`).

## 6) Reviewer Sign-off

- [ ] The upgrade scope and evidence are sufficient for merge.
- [ ] Any skipped/deferred modules have an agreed follow-up plan.
