# CLOUD_START_HERE.md — resume the eBay Live community analysis in a cloud session

This repository is a self-contained handoff of the VaynerMedia eBay Live community research. It mirrors the folder structure of the original Windows project (`C:\Users\andre\Documents\ebay_research`), so every relative path in the documents below resolves from this repository root. Wherever a document names the Windows path, read it as this repo root.

## What you are picking up

- The 150-row sample analysis is finished (revision 2.1) and is prior work, not a result.
- The FULL-COLLECTION analysis was running in a local session that ran out of context. Its state is on disk here:
  - Stage 1 complete: `analysis_outputs/full_collection_analysis/stage1_coverage.md` and `derived/`.
  - Stage 2 complete: `analysis_outputs/full_collection_analysis/stage2_provisional.md` (findings and hypotheses per community, seven blocks each) with fuller quotes in `stage2_notes_running.md`; the register of every row read is `reviewed_evidence.csv` (1,115 of a 1,200-row reading budget used, 100-row seeded control included, seed 20260928).
  - Stage 3 (evidence checks) had just started. `claim_ledger.csv` and `stage3_evidence_checks.md` do not exist yet. That is where you resume.
- Checkpoint: `RESEARCH_CHECKPOINT.md` (version 6, written by the local session). Compact recovery note: `analysis_outputs/full_collection_analysis/RESUME_HERE.md`.

## Read in this order

1. `analysis_outputs/full_collection_analysis/RESUME_HERE.md`
2. `RESEARCH_CHECKPOINT.md` (sections 5, 6, 7 first: unresolved questions, output paths, exact next step)
3. `ANALYSIS_RULES.md` (evidence rules, version 2; non-negotiable)
4. `analysis_outputs/full_dataset_inventory/DATASET_INVENTORY.md` and `GEMINI_ENRICHMENT_STATUS.md`
5. `analysis_outputs/full_dataset_inventory/FABLE_NEW_CHAT_FULL_ANALYSIS_PROMPT.md` (the full instructions, including the checker's corrections, the bounded reading plan, community section template, claim-appendix schema and report format). Follow it, but start at Stage 3, not Stage 1.
6. `analysis_outputs/full_collection_analysis/stage2_provisional.md`, including the counterevidence searches listed at its end.

## Where the data is

- `finalized/`: the eight finalized non-brand CSVs (brand posts deliberately excluded). `flash_evidence_row_id` is the citation and dedup key, not a parent-child join key; join by the schema's own parent, video or URL fields.
- `analysis_outputs/full_collection_analysis/derived/unified_evidence_index.csv`: every row's source text, labels, metrics and IDs from all eight files, for lookup and recounting. Do not recode it.
- `enrichment_v2_20260927/` (if present): the partial 27 September targeted-enrichment run (STOPPED). Inspect `STATUS.json` and `FOR_FABLE/05_COVERAGE_AND_QA.json` before using any digest; do not resume or repair it.
- Client originals: `context_uploads/ebay1.txt` (client call), `context_uploads/ebay12.txt` (internal discussion), `context_uploads/eBay x VaynerMedia_September Sprint Questions_Shared.pdf` (extract with pypdf), and the strategy email at `data/tests_and_supporting_files/local_llm_cleanup_pilot_20260925/supporting/original_copies/context_uploads/strategy_email.txt`.
- Flash run QA notes: `flash_batch_runs/*/READ_ME_RESULTS.md`, `flash_batch_runs/_queue/qa_rules.md`.

## Exact next actions (Stage 3, then Stage 4)

1. Run the counterevidence searches listed at the end of `stage2_provisional.md` with code (keyword and label retrieval across all eight files, deduplicated), then read at most 85 more unique source rows, choosing diverse contexts. Add every read row to `reviewed_evidence.csv` with the same columns.
2. Recount every number in `stage2_provisional.md` with its denominator on deduplicated units (independent units: videos, posts, streams; dependent: comments, chat messages). Keep chat message types separate (1,416 regular, 10 system, 6 error, 2 membership, 1 super chat). Owner/moderator flags are not proof of host role.
3. Write `derived/stage3_id_resolution.py`: every cited `flash_evidence_row_id` must resolve to exactly one row in the named file. Report counts.
4. Build `claim_ledger.csv` with the schema in the prompt: claim ID, F/H, statement, source file, full evidence IDs, provenance (source caption / comment / chat / title context / Gemini-read / AI-coded), calculation and denominator, independent parent count, counterevidence IDs, limitation, status (checker-pending).
5. Write `stage3_evidence_checks.md`; update `RESEARCH_CHECKPOINT.md` (copy the current one to `analysis_outputs/full_collection_analysis/RESEARCH_CHECKPOINT_v6_2026-09-28_prev.md` first).
6. Stage 4: `REPORT_full_collection.md` (coverage statement; one section per community and subcommunity with the seven blocks; cross-cutting section; claim appendix; enrichment proposals) and `OVERVIEW_full_collection.md` (short, blunt, observed versus hypothesised, what the community evidence says to each business-side input, missing business inputs, no ranking from community evidence alone). Final checkpoint and a numbered claim list for the checker.
7. Commit and push after each stage so nothing is lost if this session also runs out.

## Standing constraints

- No paid model calls, scraping, downloads or new enrichment. Counting, grouping and reading existing files only. If new enrichment would change a conclusion, write a priced proposal (see `GEMINI_ENRICHMENT_STATUS.md` §4) and continue.
- Preserve originals. Never modify files in `finalized/`. Never recode existing label fields. Archive a file before overwriting it (`..._vN_prev.md`).
- Source text over AI layers: Flash labels and Gemini frame descriptions locate rows; claims rest on captions, post and comment text and chat messages that you read. `audio_transcript` is not speech (frame-derived, 1,067 placeholders). Mark every Gemini-read or AI-coded detail in the sentence where it appears.
- Every count: numerator, denominator, unit. Speaker roles explicit, inferred or unknown. Promotion is not demand; attention is not intent; absence in a pull is not absence in the world. Brand posts stay excluded.
- Cite full `flash_evidence_row_id` values. Run the ID resolver before delivery.
- Checkpoint after each stage. Important claims remain checker-pending until verified.

## Ownership note

Two earlier sessions wrote here: a sample-analysis session (rules, inventory, enrichment status, prompt, this file) and the full-collection session (stages 1–2, register, checkpoint v6). Neither is running now. You own the checkpoint from here.
