# HANDOFF_TO_CLOUD_FABLE.md — continuing this research when the local session runs out

Written 2026-09-28 by the sample-analysis session (not the session running the full-collection analysis). This file is a note for the user and for any future session; it does not change the checkpoint or any analysis file.

## Situation
- The full-collection analysis is running in a local Fable session (`session_01Jp13wqvZRaLR8JJFvqAvtH`) that can read `C:\Users\andre\Documents\ebay_research`. As of checkpoint version 6: Stage 1 and Stage 2 complete, Stage 3 (counterevidence searches, recounts, ID resolver, `claim_ledger.csv`) in progress. That session owns `RESEARCH_CHECKPOINT.md`, `RESUME_HERE.md`, `reviewed_evidence.csv`, `claim_ledger.csv` and everything under `analysis_outputs/full_collection_analysis/`.
- A cloud-only Fable chat cannot see this disk. The handoff must travel as files.

## Compact file set to carry forward
1. `analysis_outputs/full_collection_analysis/RESUME_HERE.md` (resume point; read first)
2. `RESEARCH_CHECKPOINT.md` (current version; earlier versions are archived and not needed)
3. `ANALYSIS_RULES.md` (version 2)
4. `analysis_outputs/full_dataset_inventory/DATASET_INVENTORY.md` (version 2)
5. `analysis_outputs/full_dataset_inventory/GEMINI_ENRICHMENT_STATUS.md`
6. `analysis_outputs/full_dataset_inventory/FABLE_NEW_CHAT_FULL_ANALYSIS_PROMPT.md` (the prompt adapted for a new chat)
7. `analysis_outputs/full_collection_analysis/stage1_coverage.md`, `stage2_provisional.md`, and `stage3_evidence_checks.md`, `REPORT_full_collection.md`, `OVERVIEW_full_collection.md` once they exist
8. `analysis_outputs/full_collection_analysis/reviewed_evidence.csv` (register of every row read, with seed and sampling rule) and `claim_ledger.csv` (claims and their status)
9. `analysis_outputs/full_collection_analysis/derived/` scripts (`stage1_build_index.py`, `sampling_plan.py`, `reader.py`, the `stage2_read_*.py` files, `strat.py`)

If the new chat must read or recount rows: `analysis_outputs/full_collection_analysis/derived/unified_evidence_index.csv` (about 6.9 MB) holds every row's source text, labels, metrics and IDs from all eight finalized CSVs. The eight originals in `finalized/` (about 11 MB) are only needed to re-verify IDs against source.

## Two ways to deliver
1. Push the compact set into the Claude Project "ebay research" (Projects tool); any chat opened inside that Project can read them.
2. Attach the files directly to the new chat.

## What to tell the new chat
- Use `FABLE_NEW_CHAT_FULL_ANALYSIS_PROMPT.md` as its instructions, but resume from `RESUME_HERE.md` and the register rather than starting at Stage 1.
- Standing constraints: keep the reading budget count in the register; no paid model calls, scraping or downloads; preserve originals; do not recode fields that already exist; archive a file before overwriting it; checkpoint after each stage.
- Seed, sampling rule, which rows were read and which claims are pending are in `reviewed_evidence.csv` and `claim_ledger.csv`, not in any session's memory.
- When it finishes, it should produce the numbered claim list for the checker as the prompt specifies.

## Sizes to expect
Compact set: well under 1 MB excluding the index. Index: about 6.9 MB. Originals: about 11 MB.
