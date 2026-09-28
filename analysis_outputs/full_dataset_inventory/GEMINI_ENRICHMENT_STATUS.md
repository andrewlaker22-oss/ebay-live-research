# Gemini enrichment status: what exists, what was checked, what is incomplete

Date: 2026-09-28. Sources: `flash_batch_runs/*/READ_ME_RESULTS.md`, `flash_batch_runs/*/supporting/completion.json`, `run_design.json`, `PROMPT_QA_FLAGS.md`, `_queue/qa_rules.md`, `FLASH_PROCESSING_CHECKLIST.md`, `AI_HANDOFF_DEEP_EXPORT_2026-09-25.md`, and the tagging prompt in `ebay_research_app.py` (line 784). No new processing. Costs below are the runs' own usage-based estimates, not invoices.

## 1. Two enrichment layers exist

| Layer | When | Model and inputs | Outputs | Coverage | QA on record |
|---|---|---|---|---|---|
| A. Video tagging from sampled frames | 24 Sep 2026 | `gemini-2.5-flash fast-frames`: sampled frames plus text metadata per TikTok video; no audio. 45 direct-pull rows carry model tag `gemini-2.5-flash` without the fast-frames suffix (variant unconfirmed) | ad_description, visual_description, hook, first_3_seconds, visual, ebay_item, colors, audio, camera_angles, claim, cta, humor, talent, format, item_category, ebay_relevance, buyer_or_seller_angle, proof_or_signal, notable_text_on_screen, confidence, audio_transcript | Direct 1,001/1,007 done, 6 failed; community 908/914 done, 6 failed | No results note or spot-check record found for this layer. The handoff export describes the exports and field list only. Known defect: `audio_transcript` was requested as verbatim speech but the model had no audio; 1,067 placeholders, 12 blanks, 842 unverified populated entries. Known bias: eBay named in 173 community descriptions versus 8 captions |
| B. Text labelling, Gemini 3.8 Flash Batch | 25–26 Sep 2026 | Selected text fields only (see per-file inputs below); no video, no metrics; qa_rules.md prompt with negation, attribution and taxonomy rules | flash_community, flash_specific_category, flash_topic, flash_short_summary, flash_confidence, flash_evidence_row_id | 8 non-brand files complete (row-for-row), plus brand posts | Structural checks (row count, ID uniqueness, original-cell preservation, hashes, response status) passed on every file. Meaning checks were small spot samples (5 to 14 rows per file). No file has a measured accuracy rate |

Layer B for TikTok videos was fed Layer A's `ad_description` and `ebay_item` alongside the caption, so Flash labels on TikTok videos inherit Layer A's interpretations and biases.

## 2. Per-file status (Layer B)

| File | Rows | Inputs sent to Flash | Completed | Spot checks | Recorded caveats | Est. cost |
|---|---|---|---|---|---|---|
| TikTok direct-eBay 1,007 | 1,007 | caption, ad_description, ebay_item | 1,007/1,007, 101 requests | Checklist notes spot checks flagged overly broad Luxury routing for ordinary jewelry; no separate results note, only `completion.json` ("spot-check meaning before checking off") and `PROMPT_QA_FLAGS.md` | Search selection is not eBay relevance; existing AI descriptions are secondary text | $0.4087 |
| TikTok community 914 | 914 | caption, ad_description, ebay_item | 914/914, 92 requests | 13 rows | Challenge coins routed to Other/emerging with patches (rows 83, 91); sewing buttons vs collectible pins split | $0.3712 |
| TikTok comments 500 | 500 | comment_text, parent item_category, ebay_item | 500/500 | 14 rows | Row 39 invented humour and money role; row 500 invented "low" prices; community labels borrow the parent item's context | $0.1093 |
| Reddit broad 2,098 | 2,098 | title, text, labelled thread and immediate-parent context | 2,098/2,098, 248 requests | 10 rows + 4 missing-parent comments | Row 506 has no Reddit ID, URL or date (local ID, unverified); 49 comments lack their parent in source; row 501 gold bars routed to Coins; row 3 "Star Wars toy set" shortened | $0.6173 |
| Reddit r/Ebay 769 | 769 | as above | 730 newly processed + 39 reused from broad pull | 5 rows + 2 parent checks | Reused 39 rows were not reprocessed under the newer prompt; firearm account is an allegation | $0.2588 |
| YouTube titles 248 | 248 | title only | 248/248 | 5 rows | Row 187 repeats an unsponsored claim | $0.0519 |
| YouTube comments 1,407 | 1,407 | video_title, comment_text | 1,407/1,407 (a first attempt returned 192 cancellation errors, no output) | 5 rows | Row 1407 "counterfeits" topic on a fan-art comment; row 352 Sneakers inferred from StockX context only | $0.3578 |
| YouTube live chat 1,435 | 1,435 | message with stream context | 1,419 processed; 16 system/error rows retained with exclusion labels | 5 rows + 3 event rows | Bare numbers labelled "auction bid" from context (row 1077) are not confirmed bids; Sports Cards routing inferred from Cams Cards context (row 359); 405 low-confidence rows | $0.3237 |
| Brand posts 1,117 (excluded from community work) | 1,117 | adDescription, Emotion Evidence, overlayText | 1,117/1,117 | 5 rows | Brand output, not audience voice | $0.3086 |

Recorded usage estimate for the eight non-brand files: about $2.50. All nine: $2.807331. Batch rates used: $0.375 per million input tokens, $1.875 per million output tokens (Gemini 3.8 Flash Batch, low thinking).

## 3. What counts as complete, partial or absent

Complete and usable for navigation: Layer B labels on all eight files (row-for-row), Layer A descriptions on 1,909 of 1,921 TikTok videos.

Partial or weak, use with the stated limit:
- Layer A `audio_transcript`, `audio`, `sound`, `notable_text_on_screen`: frame-derived, unverified; navigation only (ANALYSIS_RULES.md §1).
- Flash confidence is self-reported interpretation certainty, not accuracy. Low-confidence rows: TikTok comments 62/500, YouTube comments 91/1,407, live chat 405/1,435.
- 39 r/Ebay rows carry the older broad-pull prompt provenance.
- 12 TikTok videos have no Layer A fields (gemini_failed) and therefore thinner Layer B inputs.
- Reddit broad row 506 is unverified as 2025-onward evidence.

Absent (not enrichment failures, just never collected or produced):
- Verified transcripts or any audio processing for TikTok videos.
- Audience comments for 1,871 of 1,921 TikTok videos (comments exist for 50).
- Comments for 56 of 248 YouTube videos.
- Chat for 6 of 15 live-chat video IDs (error rows).
- Sub-labels inside "Other / emerging" (683 TikTok videos carry it; `flash_specific_category` exists per row and can be profiled without a new run).
- A measured accuracy audit for any Layer A or Layer B field.
- Native eBay Live chat, eBay transaction or category performance data.

## 4. Proposals for missing enrichment (priced where a basis exists; none is approved)

| Proposal | What it would add | Basis for cost | Estimate | Status |
|---|---|---|---|---|
| P1. Profile `flash_specific_category` and `flash_topic` inside "Other / emerging" (683 videos) and cluster them | Reveals whether a thrift/vintage or other unnamed community sits inside the largest label | No model call: counting and grouping existing fields | $0 | Recommended first; no approval needed |
| P2. Text-only sub-labelling of "Other / emerging" TikTok videos with a finer taxonomy (caption + existing description) | New sub-community labels | Same inputs and rates as the 914-row run ($0.371 for 914 rows) | about $0.30 for 683 rows | Requires approval; recode only that label, not fields already held |
| P3. Verified audio transcription of TikTok videos with speech (Layer A tags "Talking head" 259 videos; video files exist at `video_path`) | Creator speech as a source layer | No transcription tool, rate or run design on record | Not priced; needs scoping | Requires scoping and approval |
| P4. Measured accuracy audit of Layer B labels: a random 100-row human check per file | An error rate instead of spot checks | Human time, not model cost | Analyst hours | Recommended before any label-based count is put in a client document |
| P5. Additional comment or chat collection (more TikTok videos, the 56 uncommented YouTube videos, the 6 failed streams) | Audience voice | Scraping, out of scope for this stage | Not priced | Not proposed now |

Do not recode fields that already exist. Do not treat P1 as a paid run. Nothing in this document authorises P2–P5.
