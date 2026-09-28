# RESUME_HERE (compact recovery note)

Updated: 2026-09-28, after Stage 2.
Current stage: Stage 3 (evidence checks) starting.
Source manifest: eight CSVs in `finalized/` (sha256 in `enrichment_v2_20260927/supporting/source_manifest.json`); derived lookup `derived/unified_evidence_index.csv`.
Completed outputs: `stage1_coverage.md`; `stage2_provisional.md` (F/H per community, seven blocks); `stage2_notes_running.md` (fuller quotes); `reviewed_evidence.csv` (register); `derived/stage2_read_*.py` + `derived/strat.py` (read scripts, seeded); root `RESEARCH_CHECKPOINT.md` v6 (v4, v5 preserved here).
Reading budget: 1,115 / 1,200 unique rows read (100 control included). 85 left for Stage 3 counterevidence reads.
Blockers: none. No shell on the Windows machine: work happens in the workspace copy and files are written back with the device file tools.
Exact next action: run counterevidence searches listed at the end of `stage2_provisional.md` (code-retrieved candidates, read ≤85 rows), recount every number with denominators on dedup units, write `derived/stage3_id_resolution.py` and `claim_ledger.csv`, then `stage3_evidence_checks.md`; then Stage 4 (`REPORT_full_collection.md`, `OVERVIEW_full_collection.md`).
