# RESEARCH_CHECKPOINT.md — eBay Live community research

Status (2026-09-28, checkpoint version 7): FULL-COLLECTION analysis, resumed in a cloud Claude Code session on branch `main-3dv76t` of `andrewlaker22-oss/ebay-live-research` after the local session (`session_01Jp13wqvZRaLR8JJFvqAvtH`) ran out of context. Stage 1, Stage 2 and Stage 3 complete; Stage 4 starting. Version 6 preserved at `analysis_outputs/full_collection_analysis/RESEARCH_CHECKPOINT_v6_2026-09-28_prev.md` (v4, v5 alongside; earlier versions in `analysis_outputs/ai_strategy_comparison_150_rows/`). No paid processing has run in this session; no source file was modified; no field was recoded. Superseded claims live only in the Archive at the end.

Division of work: Gemini organises evidence (labels, summaries, frame-based descriptions already produced). Fable synthesises. The checker verifies important claims. No new scraping, downloads or paid model runs are authorised. Fable usage itself is not free.

## 1. Goal and constraints (unchanged from v4; see that file for the full brief summary)
- Community understanding to help eBay attract shoppers to eBay Live; seven communities (six starting + coins), subcommunities, additional behaviours; seven blocks per section; Live urgent; start on @eBay/@eBayLive; framework Community Opportunity × Business Opportunity × Right to Play; business side not in these datasets; no ranking from community evidence alone; markets US/UK/DE, no inference from volume.
- Evidence rules `ANALYSIS_RULES.md` v2. Enrichment provenance `analysis_outputs/full_dataset_inventory/GEMINI_ENRICHMENT_STATUS.md` plus the partial 27 Sept run (`enrichment_v2_20260927`, STOPPED; navigation only).
- Checker corrections carried: 8,378 rows / 8,339 IDs are not independent conversations; `audio_transcript` is not verified speech; `flash_evidence_row_id` is a citation key, not a join key; chat types kept separate (1,416/10/6/2/1); owner/mod flags are not proof of host-vs-buyer roles; one shared bounded reading plan (cap 1,200 unique rows incl. 100 control).

## 2. Inputs
- Eight finalized CSVs in `finalized/` (brand posts excluded). Unified derived index: `analysis_outputs/full_collection_analysis/derived/unified_evidence_index.csv` (lookup only, no recode).
- Client originals: `context_uploads/ebay1.txt`, `context_uploads/ebay12.txt`, strategy email, sprint Q&A PDF (read in the local session; summarised in v4 §1).
- Sample report 2.1 and its F1–F29 / H1–H10 are questions (v4 §7), not results.

## 3. Completed steps
1–4. As in v4 (sample analysis, revision 2.1, handoff cleanup, checker 85/100 corrections).
5–6. As in v6 (folder access, rules and originals read; Stage 1 coverage: counts reconciled, coverage table, "Other / emerging" clusters, keyword pools, reading plan, seeded 100-row control).
7. Stage 2 (local session): 1,115 unique rows read; `stage2_provisional.md` with F/H per community; `stage2_notes_running.md`; register `reviewed_evidence.csv`.
8. Stage 3 (this session, 2026-09-28): code-retrieved counterevidence pools for every search listed at the end of Stage 2 (`derived/stage3_counterevidence_search.py`, candidates in `derived/stage3_counterevidence_candidates.csv`); 85 further unique rows read and registered (`derived/stage3_read_counterevidence.py`, `stage3_read_final6.py`), bringing the register to exactly 1,200; every Stage 2 number recounted with denominator on deduplicated units (`derived/stage3_recounts.py` → `stage3_recounts.json`); ID resolver written and run (`derived/stage3_id_resolution.py`: 603 unique cited tokens across stage2_provisional.md, stage2_notes_running.md and claim_ledger.csv, 602 resolve to exactly one row, 1 is a documented Stage 2 typo); quote provenance check (`derived/stage3_quote_check.py`); `claim_ledger.csv` built (`derived/stage3_build_claim_ledger.py`: 54 claims, 37 findings, 17 hypotheses, 394 cited full IDs, every cited row present in the register, status checker-pending); `stage3_evidence_checks.md` written with the corrections list and the numbered claim list for the checker.

## 4. Findings so far (all checker-pending; the ledger is the authoritative statement of each)
Stage 3 confirmed the shape of Stage 2 and corrected several particulars:
- eBay Live in source text: 51 rows across all eight files name it (22 direct-pull TikTok captions, 0 community-pull; 13 YouTube titles; 10 broad-Reddit rows; 5 YouTube comments; 1 r/Ebay row), all 51 read. 13/22 captions carry a paid-partnership tag; the other 9 are sellers or hosts announcing shows. Four first-person buyer accounts, all reporting friction. New: one explicit positive seller account (a comics business "sells a lot on eBay live streams and we do well"), one title-only creator row (Chanel bag unboxed from eBay Live UK, 61 views), and the same frictions (3–5 second sudden-death auctions, notification pressure, hype buying) described by explicit Whatnot buyers about Whatnot (XC-F3).
- Authentication: 297 rows name it; positive buyer-voice AG rows exist in cards (creases caught, appeal approved), sneakers (r/Sneakers AU buyers choosing eBay for photos plus AG), watches (regular Japan-sourced watch buyer trusting AG) and handbags (two LV purses). Stage 2's "AG barely named by handbag buyers" holds for Reddit handbag threads only.
- Community-pull captions naming eBay: 8/914, now all read: 2 model-train captions, a 287k-view patch jacket built from eBay finds, vintage pins from eBay, a Nikon Coolpix, a sports-card "investing #ebay" caption, a designer-bag collection (#ebay #mercari), a secondhand-platforms list. So "blind box and trains never name eBay" and "eBay absent from patch/pin captions" are withdrawn (see Archive).
- Break promotion: the seven "daily breaks in our TikTok Shop" captions are one creator (burtonbreaks). Channel-run eBay break streams on YouTube: 10 titles, 26–1,317 views; entertainment rip videos in the same lane 19,754–542,529.
- Coins: reproducible pattern gives 18 rows (16 read); one explicit numismatic buyer comment (cleaned coin sold as XF; NGC) and one Whatnot coin seller; otherwise bullion fraud. Numismatic community voice remains nearly absent from these pulls.
- Absent in the pulls: Premier League (0 rows), match-worn (0), memorabilia (1), Riftbound (0), Fanatics Live (0), DE-stated sneaker rows (0). Absence is a pull fact.
- eBay's own channel appears in the YouTube titles file (3 titles: sellers webinar, seller panel, eBay Live UK promo): brand output inside a community file; excluded from audience voice.

## 5. Unresolved questions (carried from v4 §7 Q1–Q14 and v6 Q15–Q19, updated)
- Q15 (model-train, patch/pin, physical-media clusters): partly answered. Trains and patches name eBay as a sourcing venue in a few captions; physical media once; none names live selling. Still unknown: how large these buyers are.
- Q16 (P&A rows): builders buying engines and parts on eBay; sellers routing to eBay stores; Reddit freight/fitment/return friction; no live mention. Buyer-vs-seller split in the 88-video cluster not counted by hand (12 read).
- Q17 (watches): answered for Reddit and YouTube comments (buyer and seller voice, AG-positive and seller-protection-negative); TikTok remains thin.
- Q18 (coins pool): resolved. Stage 1's 39-row pool is superseded by the 18-row reproducible pattern.
- Q19 (unpaid positive eBay Live buyer account): none found in the 51 rows naming eBay Live nor in the live-buyer keyword pool; the nearest are a positive seller account and a title-only Chanel unboxing.
- Q20 (new): 206 of the 297 authentication rows are unread; a hand audit of them would let the positive/negative AG balance be stated as a count rather than as examples (analyst time, no model cost).
- Q21 (new): the `retro_gaming_collectibles` YouTube comment lane (93 comments) was not read except one row; the Stage 2 counterevidence item used the wrong lane name (`retro_gaming`).

## 6. Output paths (this run)
`analysis_outputs/full_collection_analysis/`: `stage1_coverage.md`; `stage2_provisional.md`; `stage2_notes_running.md`; `stage3_evidence_checks.md`; `reviewed_evidence.csv` (register, 1,200 unique IDs); `claim_ledger.csv`; `RESUME_HERE.md`; `RESEARCH_CHECKPOINT_v4/v5/v6_2026-09-28_prev.md`; `derived/` (Stage 1 scripts and tables; `stage2_read_*.py`, `strat.py`, `reader.py`; `stage3_counterevidence_search.py`, `stage3_counterevidence_candidates.csv`, `stage3_read_counterevidence.py`, `stage3_read_final6.py`, `stage3_recounts.py`, `stage3_recounts.json`, `stage3_id_resolution.py`, `stage3_id_resolution_report.json`, `stage3_quote_check.py`, `stage3_quote_check.json`, `stage3_build_claim_ledger.py`). Stage 4 will add `REPORT_full_collection.md` and `OVERVIEW_full_collection.md`.

## 7. Exact next step
Stage 4: write `REPORT_full_collection.md` (coverage statement with the required table; one section per community and subcommunity with the seven blocks, Stage 3 corrections applied; cross-cutting section: trust and authentication, seller-side live economy, creator-to-purchase pathways, platform roles by community; claim appendix generated from `claim_ledger.csv`; enrichment proposals) and `OVERVIEW_full_collection.md` (at most two pages; observed versus hypothesised; what the community evidence says to each business-side input; missing business inputs; no ranking). Run the ID resolver over both, write checkpoint v8 with the checker handoff list, commit and push.
Previous next step (done): Stage 3.

## Archive: superseded claims (do not reuse)
Unchanged from v4 for v1–v3 (single thesis; pre-patch counts and identities; transcript and live-term claims). Added at v7, superseded Stage 2 statements:
- "Breaks are promoted to TikTok Shop by breakers" (plural): the seven captions are one creator, burtonbreaks.
- "eBay-branded break streams (views 26–606)": the range over the 10 channel-run eBay break titles is 26–1,317.
- "Blind box and model trains never name eBay in read rows" / "trains: no eBay": two train captions name eBay as the buying venue; one blind-box caption names eBay as the too-expensive benchmark.
- "Patches/pins: eBay absent from read captions": two community captions name eBay as the source of a vintage jacket, patches and pins.
- "AG is rarely named by handbag buyers" as a general statement: true of the Reddit handbag threads read; one YouTube commenter praises AG after buying two LV purses.
- "Numismatic collecting is not represented" (absolute): one explicit numismatic buyer comment exists (t1_n04bfny); the community remains nearly absent.
- Stage 1's "39-row coins/numismatic pool" and "183-row watches pool": patterns unrecorded; reproducible counts are 18 and 178.
- "Fragrance: 7 rows in the whole collection": reproducible pattern gives 14 rows.
- Stage 2 notes cite `local_98348833…` (typo for `local_9834883a…`) and `local_218e99db…` (displayed but never registered); neither is cited in the ledger.
