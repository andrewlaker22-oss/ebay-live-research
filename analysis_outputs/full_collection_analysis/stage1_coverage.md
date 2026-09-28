# Stage 1: Coverage inventory (full collection, eight non-brand datasets)

Date: 2026-09-28. Run: full-collection analysis, new Fable chat, following `FABLE_NEW_CHAT_FULL_ANALYSIS_PROMPT.md`. Method: counting and grouping with code only (`derived/stage1_build_index.py`, `derived/stage1_other_emerging_clusters.py`, `derived/sampling_plan.py`). No model calls, no scraping, no edits to any source file. Rules: `ANALYSIS_RULES.md` v2. Brand posts excluded.

Working environment note: this session has no shell on the Windows machine, so the eight CSVs and supporting files were staged (copied) into the analysis workspace and all outputs are written back to `analysis_outputs/full_collection_analysis/`. Originals were not modified.

## 1. Verification against DATASET_INVENTORY.md (all reconciled, no discrepancies)

| Check | Inventory says | Recomputed this run | Status |
|---|---|---|---|
| Rows / unique `flash_evidence_row_id` across eight files | 8,378 / 8,339 | 8,378 / 8,339 | match |
| Duplicates = r/Ebay rows reused from broad pull | 39 (7 posts, 32 comments) | 39 (7 posts, 32 comments) | match |
| TikTok direct vs community link overlap | 0 | 0 | match |
| TikTok comment parents | 50 videos: 13 direct, 37 community | 50: 13 / 37 | match |
| YouTube comment videos present in titles file | 192/192 | 192/192 | match |
| Live chat video IDs; overlap with titles | 15; 0 | 15; 0 | match |
| Chat event types | 1,416 message + 10 system + 6 error + 2 membership + 1 super chat = 1,435 | same | match |
| Chat owner/moderator-flagged messages | 330 | 329 (flag test `is_owner` or `is_moderator` == true on message rows) | 1-row difference; the inventory figure may include one non-message event row. 329 is used from here on |
| eBay in source text (substring, per inventory definition) | direct 684/1,007; community 8/914; TT comments 6/500; Reddit broad 88 posts + 443 comments; r/Ebay 275/730 non-duplicate rows; YT titles 150/248; YT comments 159/1,407; chat 50/1,419 | identical | match |
| Live terms in source text (inventory regex `\blive\b|livestream|whatnot|tiktok shop`) | direct 45; community 33; TT comments 0; Reddit broad 203; r/Ebay 7; YT titles 45; YT comments 72; chat 9 | identical | match |
| Reddit post dates | broad 2025-01-21 to 2026-09-18 (1 blank, record 506); r/Ebay 2025-09-26 to 2026-09-25 | identical; 0 posts or comments pre-2025 in either pull | match |
| TikTok comment dates | 2021-03 to 2026-09 | 2021-03-08 to 2026-09-25; 137/500 comments are dated before 2025-01-01 | new detail: 137 pre-2025 comments are historical context, excluded from current-behaviour counts |

Unit definitions used everywhere below: independent units = TikTok videos, Reddit posts, YouTube videos, chatted streams. Dependent units = TikTok comments, Reddit comments, YouTube comments, chat messages. The 39 duplicate r/Ebay rows are counted once (under the broad pull). Chat system/error rows are excluded; membership (2) and super chat (1) events are tracked but not interpreted.

Unified index: `derived/unified_evidence_index.csv` (8,378 rows, one per source row, with file, unit type, parent key, source text, dates, role flags and the existing AI labels). It is a derived lookup table, not a recode: no label was changed.

## 2. Coverage table: dataset x community label (AI-coded routing, dedup applied)

Labels are Flash `flash_community` labels. They are multi-label, so columns sum to more than the row counts. A label routes a row to a section; it does not establish community membership, role or promotion status.

Independent units (videos, posts):

| community | tt_direct (1,007 videos) | tt_comm (914) | rd_broad (100 posts) | rd_ebay (130 posts after dedup) | yt_titles (248) |
|:--|--:|--:|--:|--:|--:|
| Sports Cards | 19 | 62 | 18 | 4 | 23 |
| TCG/Pokemon | 77 | 87 | 22 | 15 | 29 |
| Sneakers/Streetwear | 145 | 88 | 3 | 2 | 18 |
| Luxury Fashion | 144 | 61 | 12 | 8 | 18 |
| Electronics | 157 | 188 | 9 | 9 | 16 |
| Toys/Collectibles | 118 | 137 | 5 | 7 | 17 |
| Coins | 0 | 1 | 2 | 2 | 0 |
| Other / emerging | 367 | 316 | 17 | 25 | 29 |
| General marketplace | 77 | 1 | 22 | 63 | 109 |
| Unclear | 9 | 25 | 2 | 2 | 4 |

Dependent units (comments, chat messages):

| community | tt_comments (500) | rd_broad (1,998) | rd_ebay (600 after dedup) | yt_comments (1,407) | yt_chat (1,419 non-system rows) |
|:--|--:|--:|--:|--:|--:|
| Sports Cards | 10 | 362 | 16 | 137 | 777 |
| TCG/Pokemon | 50 | 515 | 59 | 225 | 319 |
| Sneakers/Streetwear | 114 | 37 | 11 | 111 | 0 |
| Luxury Fashion | 49 | 191 | 29 | 113 | 0 |
| Electronics | 55 | 118 | 40 | 64 | 3 |
| Toys/Collectibles | 97 | 72 | 27 | 62 | 7 |
| Coins | 0 | 34 | 9 | 0 | 0 |
| Other / emerging | 83 | 302 | 59 | 227 | 36 |
| General marketplace | 12 | 526 | 374 | 412 | 149 |
| Unclear | 34 | 70 | 7 | 138 | 137 |

Chatted streams (9) are the independent units behind the chat column; they are not labelled per stream.

Keyword candidate pools (source text only, independent i / dependent d), used to widen routing beyond labels: see `derived/keyword_candidate_pools.csv`. Headline pools: watches 183 rows (TikTok 28 videos, Reddit 15 posts + 87 comments, YouTube 8 titles + 41 comments); coins/numismatic 39 rows (TikTok 6 videos, Reddit 10 posts + 18 comments, 1 YouTube title, 4 YouTube comments); handbags 224; trains 36 (35 community TikTok videos); blind box / designer toys 69 (52 community TikTok videos, 13 TikTok comments); cameras 209; automotive/P&A 51; Panini/Premier League 17 (7 community TikTok, 7 YouTube titles); other TCGs by name are rare in source text (One Piece 4 rows, Lorcana 1, Magic 8, Yu-Gi-Oh 4, Riftbound 0); Fanatics 2; Discord 21; Facebook 36; Instagram 33; UK-market terms 75; DE-market terms 53.

## 3. "Other / emerging" in the two TikTok pulls: 683 videos profiled

Rule-based grouping of the existing `flash_specific_category` and `flash_topic` labels (`derived/stage1_other_emerging_clusters.py`; per-row assignment in `derived/other_emerging_rows_clustered.csv`). The clusters are AI-coded labels grouped by keyword rule; nothing was re-coded and no video was watched. First-match cluster counts (a video is assigned to the first matching rule):

| Cluster | Videos | Direct pull | Community pull | Note |
|---|--:|--:|--:|---|
| Patches, pins, buttons, battle jackets | 126 | 2 | 124 | Almost entirely the community pull: battle-jacket and morale/police patch collecting, pinback buttons, sewing buttons. Includes rows the Flash QA noted as challenge coins routed here (3 rows tagged "patches; challenge coins"). |
| Physical media (Blu-ray, DVD, steelbook, VHS, vinyl, books) | 106 | 18 | 88 | Steelbook/4K collectors; a community-pull cluster. |
| Vintage and secondhand clothing / thrift | 104 | 88 | 16 | Direct-pull eBay-term videos: vintage dresses, t-shirts, hauls. This is where the sample's thrift/vintage pattern (H7) sits at scale; a further 78 "unassigned" rows are mostly apparel hauls and vintage fashion, so the real thrift/vintage cluster is nearer 150-180 videos. |
| Automotive: parts, cars, motorcycles | 88 | 85 | 3 | P&A appears in the collection through eBay-term searches (auto parts, engines, motorcycles). Relevant to the client's "later opportunity" question. |
| Reselling / seller how-to / marketplace ops | 42 first-match (168 any-match) | 41 | 1 | Seller-side content in the direct pull. Flag for role review. |
| Video games and retro gaming | 38 | 11 | 27 | Overlaps with Electronics-labelled retro tech. |
| Jewelry and body jewelry | 29 | 25 | 4 | Ordinary jewelry; the Flash QA already flagged over-broad Luxury routing elsewhere. |
| Model trains | 26 (28 any-match) | 0 | 26 | Community pull only. The client mentioned toy trains trending in the US; the collection has a real cluster to read. |
| Home, kitchen and decor | 19 | 17 | 2 | Pyrex, glassware, furniture finds. |
| Beauty, fragrance, personal care | 10 | 9 | 1 | |
| Sewing, craft, notions | 6 | 5 | 1 | |
| Sports memorabilia and equipment | 4 (34 any-match) | 3 | 1 | Most memorabilia rows match another rule first (patches, jerseys). |
| Military/police memorabilia, challenge coins | 3 (31 any-match) | 1 | 2 | |
| Music gear, pets/plants/food, other | 4 | 4 | 0 | |
| Unassigned (mixed) | 78 | 59 | 19 | Mostly apparel hauls/vintage fashion (see thrift), plus in-game/virtual items (Roblox, about 8 rows), outboard motors, fine art, proxy-buying services. |

Reading: the two pulls put different things in "Other / emerging". The direct (eBay-term) pull's Other is thrift/vintage clothing, auto parts, seller how-to and general finds; the community pull's Other is patch/pin, physical-media and model-train hobbies that the seven client labels do not cover. Both are worth a section: "Thrift, vintage and finds" (direct) and "Additional enthusiast hobbies: patches/pins, physical media, model trains" (community).

## 4. Seller-oriented sampling lanes flagged for role review

- YouTube titles: `reseller_what_sold` (20 videos) and `reseller_sourcing` (20); 327 of 1,407 YouTube comments sit under those two lanes. Read as seller talk unless a comment states otherwise.
- YouTube chat: The Nurse Flipper "Live eBay Reseller Q&A" (248 messages, 66 host/mod, 120 member messages): a seller-audience stream.
- Reddit r/Ebay (130 posts after dedup) is largely marketplace operations (fees_payments_holds 20 posts, shipping_delivery 13, buyer_seller_pain 18): posters are often sellers but also buyers; r/Flipping (4 posts), r/eBaySellerAdvice (2). r/whatnotapp (10) and r/TikTokshop (8) can hold buyers and sellers; role is read from the text, not the subreddit.
- TikTok: 159/1,921 captions contain seller words (resell, flipping, what sold, sourcing, my shop); Gemini's `buyer_or_seller_angle` calls 591/1,921 seller or reseller (interpretation only, navigation).
Rule applied in Stage 2: speaker role recorded as explicit, inferred or unknown per row; hosts, moderators, bots and advertisers excluded from audience-voice counts.

## 5. Partial 27 September enrichment: inspected, usable only as navigation

`enrichment_v2_20260927/STATUS.json`: STOPPED (`ValueError: result.findings[2].kind: invalid enum`), usage estimate $0.264 with $0.039 reserved/uncertain, $8 cap unspent. Completed: 24 conversation digests of 481 groups (12 of the 24 are revised pilot "quality2" outputs, 12 are first post-pilot digests; 11 superseded pilot v1 outputs are excluded), 10 blind-check rows of 400 (all Reddit broad; 4/10 exact label-set agreement; agreement is not accuracy), 10 control rows of 300 (no unexpected live signals). `final_integrity_checked` is null. Digests cover, among others, the two largest chat streams (Best Card Breaks GKYH-awLpo0, 205 rows; Whatnot Pokémon auction RHonjdvsRRY, 113 rows), 9 Reddit threads, 5 TikTok comment groups and 8 YouTube comment groups. Two digest findings carry `exclude_until_checked` flags (a PO-box/authentication paraphrase; bare-number chat lines that must not be counted as bids). None of the 10 completed enrichment control rows overlaps this run's 100-row control. Use: digests as an index to those 24 groups only; every claim still rests on source rows read here.

## 6. Reading plan under the shared cap (seed 20260928; `derived/sampling_plan.json`)

Cap: at most 1,200 unique source rows read in this run, of which 100 are the control. "Read" means the row's source text was printed and read in this run and logged in `reviewed_evidence.csv`; a label-routed count is never a read count. Text is printed up to 350 characters (comments, chat, captions) or 900 (posts, titles context); longer rows are marked truncated in the register.

| Dataset | Independent units | Dependent units | Routed to each community (AI-coded) | Planned read under caps | Control sample | Not read |
|---|--:|--:|---|--:|--:|---|
| TikTok direct-eBay | 1,007 videos | 0 | see §2 | up to 190 | 15 | remainder: captions unread, all video content unwatched |
| TikTok community | 914 videos | 0 | see §2 | up to 160 | 15 | as above |
| TikTok comments | 50 videos | 500 comments | see §2 | up to 110 comments (+ parents counted in video rows) | 10 | remainder |
| Reddit broad | 100 posts | 1,998 comments | see §2 | up to 300 rows incl. parents | 20 | remainder |
| Reddit r/Ebay | 130 posts | 600 comments | see §2 | up to 90 | 10 | remainder |
| YouTube titles | 248 videos | 0 | see §2 | up to 90 (context) | 8 | remainder |
| YouTube comments | 192 videos | 1,407 comments | see §2 | up to 150 | 12 | remainder |
| YouTube replay chat | 9 streams | 1,416 messages | see §2 | up to 110 messages | 10 | remainder |
| Total | | | | up to 1,100 | 100 | |

Selection rule per section: candidates = label-routed rows UNION source-text keyword hits for that community (so watches, coins, trains, Panini etc. are found even where labels missed them); deduplicated; seeded random sample within candidates, deliberately including low-view/low-score rows, keyword hits that could contradict a hypothesis, parent and immediate-parent context, and every dataset that has candidates. Not most-liked-first. Evidence is reused across sections through the single register. Control: 100 rows stratified by dataset (15/15/10/20/10/8/12/10), drawn from rows outside the keyword screen (`live|livestream|whatnot|tiktok shop|authentic|counterfeit|fake|scam|break(s)|rip n ship|ebay live|fanatics`) and outside the seven client-community labels (all 100 satisfy both), excluding chat host/moderator rows, system/error rows and duplicate r/Ebay rows. Actual read counts are reported in Stage 3 and in the report's coverage statement.

## 7. Discrepancies and open points before Stage 2

- Owner/moderator chat count 329 vs 330 in the inventory (see §1); no effect on findings.
- Coins: only 1 TikTok video labelled Coins and 4 Reddit posts + 43 comments (AI-coded); keyword search adds 6 TikTok videos, 10 Reddit posts, 1 YouTube title, 4 YouTube comments. Numismatic evidence will be thin; the section will say how thin and what was searched.
- Watches: no label exists; the 183-row keyword pool (r/Watches, r/rolex, `watches_auth` lane, 28 TikTok captions) is the route.
- Other TCGs are barely present in source text (One Piece 4 rows, Lorcana 1, Magic 8, Yu-Gi-Oh 4, Riftbound 0); the TCG section will name what exists rather than infer sub-community sizes.
- P&A/automotive exists in the direct pull (about 88 videos, AI-coded cluster) and will get a short additional-behaviours subsection.

Checkpoint saved: `RESEARCH_CHECKPOINT.md` (project root, version 5) and `RESUME_HERE.md` in this folder.
