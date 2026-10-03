# RESEARCH_CHECKPOINT.md — eBay Live community research

Status (2026-09-28, checkpoint version 9): FULL-COLLECTION analysis DELIVERED as provisional, checker-pending documents, in a cloud Claude Code session on branch `main-3dv76t` of `andrewlaker22-oss/ebay-live-research` (pull request #1). Stages 1–4 complete; a post-delivery claim support check (v9) verified that every cited row's read text supports the claim it is cited for, and applied corrections C20–C26. Version 8 preserved at `analysis_outputs/full_collection_analysis/RESEARCH_CHECKPOINT_v8_2026-09-28_prev.md` (v4–v7 alongside; earlier versions in `analysis_outputs/ai_strategy_comparison_150_rows/`). No paid processing ran in this session; no source file was modified; no field was recoded; the 1,200-row reading ceiling was not exceeded (the support check re-read cited rows within their read windows only). Superseded claims live only in the Archive at the end.

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
8. Stage 3 (this session): counterevidence pools and 85 reads (register 1,200/1,200); recounts; ID resolver; quote check; `claim_ledger.csv`; `stage3_evidence_checks.md` (C1–C19); checkpoint v7. Commit `a98bc9d`.
9. Stage 4 (this session): `REPORT_full_collection.md`; `OVERVIEW_full_collection.md`; appendix rendered from the ledger; ID resolver over the report; checkpoint v8. Commit `15d43fc`.
10. Claim support check (this session, after the user's instruction to generate citations from source records and verify support, not only resolution): `derived/stage3_claim_support_check.py` re-read all 303 cited rows inside their read windows (`derived/cited_rows_read_window.txt`), required a key phrase from each row to be present, counted distinct authors per claim and marked shared Reddit rows. Result 303/303; 53 claims supported (8 with notes), 1 code-count claim. Corrections C20–C26 applied to ledger statements (rebuilt), report, overview and evidence checks (§10). Ledger gains three columns.

## 4. Findings (all checker-pending; the ledger is authoritative)
- eBay Live in source text: 51 rows in all eight files, all read; 22 direct-pull captions (13 paid-partnership from 12 creators; 8 seller announcements or a tool ad; 1 hashtag-only mention), 0 community-pull captions; four first-person buyer accounts, all friction; one positive explicit seller account; no unpaid positive buyer account (Q19 closed as "none in these pulls").
- Whatnot buyers describe the same frictions about Whatnot (XC-F3).
- Authentication: 297 rows; defenders and complaints in the same threads across cards, sneakers, watches and handbags; no AG in coins/bullion.
- Community-pull captions naming eBay: 8/914 (1/62 cards, 0/87 Pokémon, 0/88 sneakers, 1/61 luxury, 1/188 electronics, 1/137 toys, 4/316 other); the two train captions are two creators, one of whom posts three of the four cited train captions.
- Breaks: one breaker promotes into TikTok Shop; YouTube eBay break streams from 4 channels 26–1,317 views vs rip entertainment from 2 channels 19,754–542,529.
- Coins nearly absent (18 rows); P&A eBay-native with no live link (one cited wholesale caption never names eBay); Premier League, match-worn, Fanatics Live, Riftbound absent from pulls.
- Full list: 54 claims in `claim_ledger.csv` and `stage3_evidence_checks.md` §7.

## 5. Unresolved questions (for the checker and the user)
- Q19 closed as a pull fact. Q20: 206 unread authentication rows (proposal P6). Q21: `retro_gaming_collectibles` lane unread (P7). Buyer-vs-seller split inside the P&A cluster; whether break buyers watch on YouTube or on eBay; host platform of the TikTok "Mega live alert" Chanel auction; the eBay Live UK Chanel unboxing video content (P8).
- Client tensions reported, not resolved: sneakers (call vs sprint Q&A); coins green shoot (no community evidence either way).
- Business inputs missing: Live GMV, buyer counts, repeat rates, supply, return rates, notification opt-outs, native eBay Live chat.

## 6. Output paths
`analysis_outputs/full_collection_analysis/`: `REPORT_full_collection.md`; `OVERVIEW_full_collection.md`; `claim_ledger.csv`; `stage3_evidence_checks.md`; `stage2_provisional.md`; `stage2_notes_running.md`; `stage1_coverage.md`; `reviewed_evidence.csv`; `RESUME_HERE.md`; `RESEARCH_CHECKPOINT_v4…v8_2026-09-28_prev.md`; `derived/` (index and Stage 1 tables; `reader.py`, `strat.py`, `stage2_read_*.py`; `stage3_counterevidence_search.py` + candidates CSV; `stage3_read_counterevidence.py`; `stage3_read_final6.py`; `stage3_recounts.py` + `.json`; `stage3_id_resolution.py` + report JSON; `stage3_quote_check.py` + `.json`; `stage3_build_claim_ledger.py`; `stage3_claim_support_check.py` + `stage3_claim_support_report.json` + `cited_rows_read_window.txt`; `stage4_render_appendix.py` + `claim_appendix.md`).

## 7. Exact next step
Checker verification of the 54 claims, starting with XC-F1, XC-F2, SC-F2, PK-F2, LX-W-F1, CN-F2 and AB-SL-F1, using the ledger's Full evidence IDs, Support check and Distinct authors columns and `derived/stage3_claim_support_report.json`. Then join to the business-side inputs. Any further reading (P6–P9) needs an explicit budget decision from the user; no reading budget remains in this run.
Previous next step (done): Stage 4 and the support check.

## Archive: superseded claims (do not reuse)
Unchanged from v7 for v1–v3 items and the Stage 2 statements superseded at v7 (see v7). Added at v9 (superseded first-delivery wording): "the other 9 [eBay Live captions] are sellers or hosts announcing their own shows" (one is a hashtag-only mention); "eBay break streams… next to entertainment rip videos" without channel counts (4 channels vs 2); "model trains name eBay in 2 captions" without creators (2 creators, one posting 3 of 4 cited captions); "Pop Mart itself" as a maker (unverified handle); "parts sellers routing to eBay stores" including the wholesale caption local_21b424cb… (it never names eBay); two AU sneaker buyers (t1_ns0iwn6 and t3_1pcpv9c are one person); two r/Watches commenters (t1_p5gb6s4 and t1_p5gbcao are one person).
