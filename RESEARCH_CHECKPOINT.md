# RESEARCH_CHECKPOINT.md — eBay Live community research

Status (2026-09-28, checkpoint version 8): FULL-COLLECTION analysis DELIVERED as provisional, checker-pending documents, in a cloud Claude Code session on branch `main-3dv76t` of `andrewlaker22-oss/ebay-live-research`. Stages 1–4 complete. Version 7 preserved at `analysis_outputs/full_collection_analysis/RESEARCH_CHECKPOINT_v7_2026-09-28_prev.md` (v4–v6 alongside; earlier versions in `analysis_outputs/ai_strategy_comparison_150_rows/`). No paid processing ran in this session; no source file was modified; no field was recoded. Superseded claims live only in the Archive at the end.

Division of work: Gemini organises evidence (labels, summaries, frame-based descriptions already produced). Fable synthesises. The checker verifies important claims. No new scraping, downloads or paid model runs are authorised. Fable usage itself is not free.

## 1. Goal and constraints (unchanged from v4; see that file for the full brief summary)
- Community understanding to help eBay attract shoppers to eBay Live; seven communities (six starting + coins), subcommunities, additional behaviours; seven blocks per section; Live urgent; start on @eBay/@eBayLive; framework Community Opportunity × Business Opportunity × Right to Play; business side not in these datasets; no ranking from community evidence alone; markets US/UK/DE, no inference from volume.
- Evidence rules `ANALYSIS_RULES.md` v2. Enrichment provenance `analysis_outputs/full_dataset_inventory/GEMINI_ENRICHMENT_STATUS.md` plus the partial 27 Sept run (`enrichment_v2_20260927`, STOPPED; navigation only).
- Checker corrections carried: 8,378 rows / 8,339 IDs are not independent conversations; `audio_transcript` is not verified speech; `flash_evidence_row_id` is a citation key, not a join key; chat types kept separate (1,416/10/6/2/1); owner/mod flags are not proof of host-vs-buyer roles; one shared bounded reading plan (cap 1,200 unique rows incl. 100 control).

## 2. Inputs
- Eight finalized CSVs in `finalized/` (brand posts excluded). Unified derived index: `analysis_outputs/full_collection_analysis/derived/unified_evidence_index.csv` (lookup only, no recode).
- Client originals: `context_uploads/ebay1.txt`, `context_uploads/ebay12.txt`, strategy email, sprint Q&A PDF (read in the local session; summarised in v4 §1).
- Sample report 2.1 and its F1–F29 / H1–H10 were treated as questions (v4 §7), not results.

## 3. Completed steps
1–4. As in v4 (sample analysis, revision 2.1, handoff cleanup, checker 85/100 corrections).
5–6. As in v6 (Stage 1 coverage).
7. Stage 2 (local session): 1,115 rows read; `stage2_provisional.md`; `stage2_notes_running.md`; register.
8. Stage 3 (this session): counterevidence pools and 85 reads (register 1,200/1,200); recounts (`derived/stage3_recounts.json`); ID resolver; quote check; `claim_ledger.csv` (54 claims, 394 full IDs, all registered); `stage3_evidence_checks.md` (corrections C1–C19, numbered checker list); checkpoint v7. Committed and pushed (`a98bc9d`).
9. Stage 4 (this session): `REPORT_full_collection.md` (coverage statement with the required table; seven blocks for sports cards, Pokémon and other TCGs, sneakers, handbags, watches, vintage designer and fragrance, electronics, toys by sub-hobby, coins, thrift and vintage, patches and pins, physical media, P&A, seller-side live economy; cross-cutting section; business-side framing; proposals P6–P9; claim appendix rendered from the ledger by `derived/stage4_render_appendix.py`); `OVERVIEW_full_collection.md`; ID resolver run over the report (513 tokens, 512 resolve; the one exception is the documented Stage 2 typo quoted in a ledger cell; the resolver's new register check flags one resolved row quoted only as "not registered"); this checkpoint.

## 4. Findings (all checker-pending; the ledger is authoritative)
- eBay Live in source text: 51 rows in all eight files, all read; 22 direct-pull captions (13 paid-partnership, 9 seller announcements), 0 community-pull captions; four first-person buyer accounts, all friction; one positive explicit seller account; no unpaid positive buyer account (Q19 closed as "none in these pulls").
- Whatnot buyers describe the same frictions about Whatnot (XC-F3).
- Authentication: 297 rows; defenders and complaints in the same threads across cards, sneakers, watches and handbags; no AG in coins/bullion.
- Community-pull captions naming eBay: 8/914 (1/62 cards, 0/87 Pokémon, 0/88 sneakers, 1/61 luxury, 1/188 electronics, 1/137 toys, 4/316 other): eBay is a find venue, comp source or dispute venue, not part of the hobby ritual.
- Breaks: one breaker promotes into TikTok Shop; YouTube eBay break streams 26–1,317 views vs rip entertainment 19,754–542,529.
- Coins nearly absent (18 rows); P&A eBay-native with no live link; Premier League, match-worn, Fanatics Live, Riftbound absent from pulls.
- Full list: 54 claims in `claim_ledger.csv` and `stage3_evidence_checks.md` §7.

## 5. Unresolved questions (for the checker and the user)
- Q19 closed as a pull fact. Q20: 206 unread authentication rows (proposal P6). Q21: `retro_gaming_collectibles` lane unread (P7). Buyer-vs-seller split inside the P&A cluster; whether break buyers watch on YouTube or on eBay; host platform of the TikTok "Mega live alert" Chanel auction; the eBay Live UK Chanel unboxing video content (P8).
- Client tensions reported, not resolved: sneakers (call vs sprint Q&A); coins green shoot (no community evidence either way).
- Business inputs missing: Live GMV, buyer counts, repeat rates, supply, return rates, notification opt-outs, native eBay Live chat.

## 6. Output paths
`analysis_outputs/full_collection_analysis/`: `REPORT_full_collection.md`; `OVERVIEW_full_collection.md`; `claim_ledger.csv`; `stage3_evidence_checks.md`; `stage2_provisional.md`; `stage2_notes_running.md`; `stage1_coverage.md`; `reviewed_evidence.csv`; `RESUME_HERE.md`; `RESEARCH_CHECKPOINT_v4/v5/v6/v7_2026-09-28_prev.md`; `derived/` (index and Stage 1 tables; `reader.py`, `strat.py`, `stage2_read_*.py`; `stage3_counterevidence_search.py` + `stage3_counterevidence_candidates.csv`; `stage3_read_counterevidence.py`; `stage3_read_final6.py`; `stage3_recounts.py` + `.json`; `stage3_id_resolution.py` + `stage3_id_resolution_report.json`; `stage3_quote_check.py` + `.json`; `stage3_build_claim_ledger.py`; `stage4_render_appendix.py` + `claim_appendix.md`).

## 7. Exact next step
Checker verification of the 54 claims, starting with XC-F1, XC-F2, SC-F2, PK-F2, LX-W-F1, CN-F2 and AB-SL-F1. Then join to the business-side inputs. Any further reading (P6–P9) needs an explicit budget decision from the user; no reading budget remains in this run.
Previous next step (done): Stage 4.

## Archive: superseded claims (do not reuse)
Unchanged from v7 (v1–v3 items from v4; Stage 2 statements superseded at v7: "breakers" plural for the burtonbreaks captions; eBay-break views "26–606"; "blind box and trains never name eBay"; "patches/pins: eBay absent"; "AG rarely named by handbag buyers" as a general statement; "numismatic collecting is not represented" as an absolute; Stage 1's 39-row coins and 183-row watches pools; "fragrance: 7 rows"; the `local_98348833…` typo and the unregistered `local_218e99db…` citation).
