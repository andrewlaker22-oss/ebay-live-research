# RESUME_HERE (compact recovery note)

Updated: 2026-09-28, after Stage 3 (cloud session, branch `main-3dv76t`).
Current stage: Stage 4 (REPORT_full_collection.md, OVERVIEW_full_collection.md) starting.
Source manifest: eight CSVs in `finalized/` (sha256 in `enrichment_v2_20260927/supporting/source_manifest.json`); derived lookup `derived/unified_evidence_index.csv`.
Completed outputs: `stage1_coverage.md`; `stage2_provisional.md` + `stage2_notes_running.md`; `reviewed_evidence.csv` (register, 1,200 unique rows); `stage3_evidence_checks.md`; `claim_ledger.csv` (54 claims: 37 F, 17 H, 394 cited IDs, all resolved and all in the register); `derived/stage3_*.py` (counterevidence search, reads, recounts, ID resolver, quote check, ledger builder) with `stage3_recounts.json`, `stage3_id_resolution_report.json`, `stage3_quote_check.json`, `stage3_counterevidence_candidates.csv`; root `RESEARCH_CHECKPOINT.md` v7 (v4, v5, v6 preserved here).
Reading budget: 1,200 / 1,200 unique rows read (100 control; 85 Stage 3 counterevidence). No budget remains: Stage 4 cites only registered rows.
Blockers: none. No paid calls, scraping or enrichment were run.
Exact next action: write `REPORT_full_collection.md` (coverage statement; seven blocks per community and subcommunity with Stage 3 corrections; cross-cutting section; claim appendix generated from `claim_ledger.csv`; enrichment proposals) and `OVERVIEW_full_collection.md`; run `derived/stage3_id_resolution.py` over both; write checkpoint v8 with the checker handoff list; commit and push.
