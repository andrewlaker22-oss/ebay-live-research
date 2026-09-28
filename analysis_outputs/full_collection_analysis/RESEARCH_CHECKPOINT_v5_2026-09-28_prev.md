# RESEARCH_CHECKPOINT.md — eBay Live community research

Status (2026-09-28, checkpoint version 5): FULL-COLLECTION analysis started in a new Fable chat (session `session_01Jp13wqvZRaLR8JJFvqAvtH`). Stage 1 (coverage inventory) complete. Stages 2–4 in progress in the same session. No paid processing has run in this session; no source file was modified. Version 4 is preserved at `analysis_outputs/full_collection_analysis/RESEARCH_CHECKPOINT_v4_2026-09-28_prev.md`; earlier versions in `analysis_outputs/ai_strategy_comparison_150_rows/`. Superseded claims live only in the Archive at the end.

Division of work: Gemini organises evidence (labels, summaries, frame-based descriptions already produced). Fable synthesises. The checker verifies important claims. No new scraping, downloads or paid model runs are authorised. Fable usage itself is not free.

## 1. Goal and constraints (unchanged from v4; see that file for the full brief summary)
- Community understanding to help eBay attract shoppers to eBay Live; seven communities (six starting + coins), subcommunities, additional behaviours; seven blocks per section; Live urgent; start on @eBay/@eBayLive; framework Community Opportunity × Business Opportunity × Right to Play; business side not in these datasets; no ranking from community evidence alone; markets US/UK/DE, no inference from volume.
- Evidence rules `ANALYSIS_RULES.md` v2. Enrichment provenance `analysis_outputs/full_dataset_inventory/GEMINI_ENRICHMENT_STATUS.md` plus the partial 27 Sept run (`enrichment_v2_20260927`, STOPPED; 24/481 digests, 10/400 blind, 10/300 control; navigation only).
- Checker corrections carried into this run: 8,378 rows / 8,339 IDs are not independent conversations; `audio_transcript` is not verified speech (1,067 placeholders, 12 blanks, 842 unverified; 45 direct rows different model tag); `flash_evidence_row_id` is a citation key, not a join key; chat types kept separate (1,416/10/6/2/1); owner/mod flags are not proof of host-vs-buyer roles; one shared bounded reading plan (cap 1,200 unique rows incl. 100 control).

## 2. Inputs
- Eight finalized CSVs in `finalized/` (brand posts excluded). Unified derived index: `analysis_outputs/full_collection_analysis/derived/unified_evidence_index.csv` (lookup only, no recode).
- Client originals read in this session: `context_uploads/ebay1.txt`, `context_uploads/ebay12.txt`, strategy email, sprint Q&A PDF (extracted with pypdf).
- Sample report 2.1 and its F1–F29 / H1–H10 are questions (v4 §7), not results.

## 3. Completed steps
1–4. As in v4 (sample analysis, revision 2.1, handoff cleanup, checker 85/100 corrections).
5. 2026-09-28 (this session): folder access verified; rules, inventory, enrichment status, checkpoint, checker feedback and client originals read; partial enrichment inspected (STATUS.json, 05_COVERAGE_AND_QA.json, digests/blind/control counted).
6. Stage 1 done: counts reconciled with DATASET_INVENTORY.md (all match; owner/mod message count 329 vs 330 noted); coverage table dataset × community; "Other / emerging" 683 TikTok videos clustered by rule over existing labels (patches/pins 126, physical media 106, thrift/vintage clothing 104 + most of 78 unassigned, automotive/P&A 88, seller how-to 42, retro games 38, jewelry 29, model trains 26, home 19, other); seller lanes flagged; keyword candidate pools built (watches 183 rows, coins 39, handbags 224, trains 36, blind box 69, cameras 209, P&A 51, Panini 17, other TCGs ≤8 each); reading plan and seeded 100-row control drawn (seed 20260928). Output: `analysis_outputs/full_collection_analysis/stage1_coverage.md` + `derived/`.

## 4. Findings so far
Stage 1 is counting only. Structural findings: (a) the direct-pull "Other" is thrift/vintage clothing, auto parts and seller how-to; the community-pull "Other" is patch/pin, physical-media and model-train hobbies; (b) P&A/automotive content exists in the collection (about 88 direct-pull videos, AI-coded); (c) coins and watches have no or almost no label routing and must be found by keyword (thin pools); (d) other TCGs are barely named in source text; (e) 137/500 TikTok comments predate 2025 (historical only).

## 5. Unresolved questions (carried from v4 §7 Q1–Q14, plus)
- Q15 What is in the model-train, patch/pin and physical-media clusters, and do they connect to eBay or live at all in source text?
- Q16 P&A: what do the automotive rows show (buyer vs seller, condition, fitment, price checks)?
- Q17 Watches: does the 183-row keyword pool contain buyer voice, or is it seller/authentication talk?

## 6. Output paths (this run)
`analysis_outputs/full_collection_analysis/`: `stage1_coverage.md`; `derived/` (stage1_build_index.py, stage1_other_emerging_clusters.py, sampling_plan.py, sampling_plan.json, reader.py, unified_evidence_index.csv, coverage_by_dataset_community.csv, keyword_candidate_pools.csv, other_emerging_*.csv, control_sample_100.csv, stage1_verification.json); `RESUME_HERE.md`; `reviewed_evidence.csv` and `claim_ledger.csv` (created in Stage 2). Later: `stage2_provisional.md`, `stage3_evidence_checks.md`, `REPORT_full_collection.md`, `OVERVIEW_full_collection.md`.

## 7. Exact next step
Stage 2: read routed rows per community section (sports cards → TCG/Pokémon → sneakers → luxury (handbags, watches, vintage designer, fragrance) → electronics → toys (sub-hobbies incl. trains, blind box) → coins → additional behaviours (thrift/vintage, seller-side live economy, patches/pins, physical media, P&A)) plus the 100-row control; register every read row; write `stage2_provisional.md` with F/H per community and evidence IDs; update this checkpoint.

## Archive: superseded claims (do not reuse)
Unchanged from v4 (v1 single thesis; v2 pre-patch counts and identities; v3 transcript and live-term claims). See `RESEARCH_CHECKPOINT_v4_2026-09-28_prev.md` for the full archive text.
