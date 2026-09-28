# NEW FABLE CHAT: Run the full-collection eBay community analysis

Prepared 2026-09-28 for a NEW Fable chat. You do not need the earlier conversation. The user authorizes you to begin this bounded analysis now and continue through the stages below without asking permission after the inventory. No new external paid API calls, collection or enrichment are authorized. Your own Fable usage may still cost money: do not describe this analysis as free.

## Start here: access, history and corrections

Project root: `C:\Users\andre\Documents\ebay_research`. Every relative path below resolves from that root. This is a Windows local project, not a website. Verify you can read it before proceeding. If this chat cannot access local files, stop and ask the user to connect this project folder; do not pretend you opened files or reconstruct results from this prompt. Do not request API keys.

What happened:
- Apify collected targeted TikTok, Reddit, YouTube and YouTube replay-chat research. About 1,900 TikTok videos were downloaded and tagged by Gemini; a later Flash text pass added community/category/topic/summary labels.
- An early 150-row comparison sample pushed analysts toward one winning community and an overconfident cards thesis. That was NOT the client's assignment.
- Fable revised the sample into community sections, then a checker corrected counts, speaker identities, unsupported source attribution and missing counterevidence. Revision 2.1 is useful prior work, not a full-collection conclusion.
- The eight non-brand files were inventoried and persistent analysis rules written. Brand social posts are intentionally excluded for now. Do not reintroduce them or the earlier roughly 8,100-brand-post claim.
- The user already spent too much on repeated analysis. Use code for coverage/calculations and selective source review for synthesis. Do not launch a fresh exhaustive row-by-row model pass.

Final checker feedback to incorporate while working, not as another preparation-only project:
1. The main inventory totals are verified: 8,378 rows and 8,339 unique evidence IDs. This is not 8,339 independent conversations.
2. The TikTok `audio_transcript` column is not verified speech. Current inventory reports 1,067 explicit placeholders, 12 blanks and 842 other populated entries without verified audio provenance. Most tagging used sampled frames plus metadata, not audio. Forty-five direct-pull rows have a different model tag; their audio provenance remains unconfirmed. Say "no verified transcripts established in the inspected evidence," not "audio processing never happened anywhere." Never quote these fields as creator speech or use them to corroborate another Gemini interpretation.
3. The existing enrichment-status document MISSES the separate 27 September targeted-enrichment run. Inspect the partial run described below before assuming all enrichment is complete or absent.
4. `flash_evidence_row_id` identifies an evidence record for citation/deduplication. It is NOT a universal parent-child join key. Join comments to posts/videos with the verified parent ID, video ID or canonical URL for each schema.
5. Live-chat types reconcile as 1,416 regular messages + 10 system + 6 error + 2 membership + 1 superchat = 1,435 rows. Keep message types separate. Owner/moderator flags are not proof that every flagged author is a host, nor that every other author is a buyer.
6. Replace the earlier multiplicative reading caps with the shared, bounded review plan below. Do not read the same sources repeatedly for each community or hypothesis.

Correct working rules and checkpoint notes as needed, preserving earlier versions. Do not spend a separate turn polishing the handoff.

## Partial Gemini enrichment: inspect before use

Folder: `enrichment_v2_20260927`.
- Read `STATUS.json` and `FOR_FABLE/05_COVERAGE_AND_QA.json` first.
- Last checked status: STOPPED, `ValueError: result.findings[2].kind: invalid enum`.
- Last recorded completion: 24 digest jobs done; 1 blind-check job done; 1 control job done. Those are JOB counts, not necessarily row counts. One digest remained inflight in the saved state. Most planned work was pending.
- Recorded usage estimate: $0.2640562, with $0.03935642 reserved/uncertain, not confirmed additional spend. The $8 cap was an allowance, not money spent.
- Do not resume, retry, repair the paid runner, switch models, or assume final integrity passed.
- Available files: `FOR_FABLE/01_CONVERSATION_DIGESTS.jsonl`, `02_BLIND_LABEL_CHECK.jsonl`, `03_CONTROL_ENRICHMENT.jsonl`, `04_SOURCE_EVIDENCE_AND_EXISTING_LABELS.jsonl`, `05_COVERAGE_AND_QA.json`, `READ_ME_FIRST.md`, `CLIENT_AND_ANALYSIS_BRIEF.md`, `research_tools.py`.
- Validate completion/provenance and review flags before using any digest. Excluded, superseded or unfinished outputs must not support findings. A digest is an index to collected source evidence, not a second independent source.
- README descriptions of 400 blind rows, 300 control rows or all conversation groups describe intended scope; do not report them as completed.
- Use local indexed lookups or code to retrieve relevant groups. Do not dump the 11 MB source JSONL into your context. Inspect any helper before running it; only local, read-only retrieval is authorized.
- Blind-label agreement is not accuracy. Previous Fable coding is a comparison set, not ground truth.

## What to deliver in this run

A broad, provisional community report grounded in all eight datasets' coverage, with selective source review honestly disclosed; an evidence appendix; and a short overview. The user wants the client questions answered, not another handoff saying analysis is ready to start. Continue automatically until these deliverables exist or a real access/usage blocker stops you. Important claims remain checker-pending, not client-approved.

---

## Your role and the division of work

You are the synthesis analyst on VaynerMedia's eBay Live community research. Existing Gemini labels and summaries provide navigation across the files; frame-based descriptions apply to TikTok videos, and conversation enrichment is partial. Do not rerun these layers. You synthesise. A separate checker verifies important claims before anything reaches a client document, so write for that checker: every claim traceable, every count with its denominator, every AI-derived detail marked.

Read these three files first and follow them throughout:
- `ANALYSIS_RULES.md` (project root): evidence rules. Non-negotiable.
- `analysis_outputs/full_dataset_inventory/DATASET_INVENTORY.md`: what each dataset is, its units, dates, overlaps and dedup rules.
- `analysis_outputs/full_dataset_inventory/GEMINI_ENRICHMENT_STATUS.md`: which AI fields exist, what QA they had, what is partial or absent.

Also read `RESEARCH_CHECKPOINT.md` (project root). Match any completion entry to its dataset scope, output file and source manifest before resuming. Finished SAMPLE analysis or enrichment stages are not finished FULL-COLLECTION analysis. Preserve useful prior work; do not start over or skip unfinished stages.

## The client assignment (read the originals; this is a pointer, not a substitute)

Originals: client call transcript `context_uploads/ebay1.txt`; internal team discussion `context_uploads/ebay12.txt`; strategy email `data/tests_and_supporting_files/local_llm_cleanup_pilot_20260925/supporting/original_copies/context_uploads/strategy_email.txt`; client sprint Q&A `context_uploads/eBay x VaynerMedia_September Sprint Questions_Shared.pdf` (extract text with pypdf; the page text is one line per page).

What the client asked for, in their own framing:
- Community understanding that helps eBay attract shoppers to eBay Live: where communities spend attention, how they behave per platform, what content earns attention, who the authoritative voices are, how commerce and Live already show up, where eBay already participates and where competitors play instead.
- Start with sports cards, TCG/Pokémon, sneakers/streetwear, luxury fashion, electronics, toys/collectibles. The client added coins ("a big focus and green shoot for Live", unsure how much of that community is on social). The client said toys/collectibles is a catch-all with many sub-communities, that handbags and watches are different communities, and that sneakers are probably not a big Live focus but heat there should be fed back to the Live team. P&A (parts and accessories) is eBay's biggest core category, not on Live yet, and is a later opportunity.
- The sprint Q&A lists eBay Live's stated right-to-win categories as CCG/STC (collectible card games and sports trading cards), enthusiast toys, sneakers, and luxury fashion/accessories, with low-ASP fashion, CCG singles, coins and electronics as maintain categories. Note the tension with the call's remark on sneakers and report it rather than resolving it.
- Live is the urgent near-term focus (first three to six months). The directional plan is to deploy on the core handles @eBay and @eBayLive first; dedicated handles are a possible byproduct of proven series, live sessions and demand, not the starting assumption. Be choiceful about channels: show up where the behaviour already has a retail angle.
- The client wants concrete content examples by community and platform, not category names; wants more content and less preciousness; wants to know what sellers and creators produce versus what eBay produces. Named Live sellers who are also strong creators: Vookum, Tanner & Co, BlackGold Sports Cards, Linda's Stuff.
- The strategy email says: do not come back with six audits that all say "opportunity". The decision framework is Community Opportunity × eBay Business Opportunity × eBay Right to Play. The business side (GMV, growth, Live traction, buyer dynamics, supply, competitive position, headroom, economics) is not in these datasets. Your job is the community side, written so it can be joined to the business side. Do not manufacture a ranking from community evidence alone; do say what the community evidence would support or argue against if the business data came in a given way.
- Markets: US, UK, Germany. No dataset is geographically balanced; report market signals only where a row states its market, and never infer market differences from volume.

Internal discussion points to test, not to adopt: luxury entry via eBay finds and accessories; handbags/shoes/accessories over apparel for live because of sizing; trust in eBay's authentication versus Discord/Whatnot; eBay as a price "fact check" for cards; unboxing as where card attention sits and Whatnot's buy-the-pack-open-live model; TCG sub-communities (Pokémon strongest, One Piece rising, Yu-Gi-Oh declining, Lorcana as fandom); UK Panini stickers and Premier League cards; memorabilia and match-worn shirts; Fanatics Live as a sports competitor; toy trains trending in the US.

## Inputs: the eight finalized community datasets (brand posts excluded)

All in `C:\Users\andre\Documents\ebay_research\finalized\`. Row counts are exact. `flash_evidence_row_id` is the record citation/deduplication key; use source-specific parent IDs, video IDs or canonical URLs for parent-child joins.

1. `FINAL_1007_direct_eBay_TikTok_videos_Flash_Batch_communities_topics.csv`: 1,007 videos from eBay-term searches. Source fields: caption, hashtags, views, likes, comments, shares. Creative-description fields are AI interpretations, mostly from sampled frames (including unverified `audio_transcript`). IDs, file paths and operational metadata are not creative interpretations. Check field provenance rather than treating every remaining column alike.
2. `FINAL_914_community_TikTok_videos_Flash_Batch_communities_topics.csv`: 914 videos from community-term searches; 0 links shared with file 1. Same field structure.
3. `FINAL_500_TikTok_comments_50_videos_Flash_Batch_communities_topics.csv`: 500 comments under 50 videos (13 from file 1, 37 from file 2). The only TikTok audience voice.
4. `FINAL_100_Reddit_conversations_1998_comments_Flash_Batch_communities_topics.csv`: 100 posts and 1,998 nested comments across 20 subreddits, 6 search buckets. Usable post dates cover 2025-01 to 2026-09; broad source record 506 lacks a verified Reddit ID/URL/date and must not count as confirmed current evidence.
5. `FINAL_137_rEbay_posts_632_comments_Flash_Batch_communities_topics.csv`: 137 r/Ebay posts and 632 comments; 39 rows duplicate file 4 (7 posts, 32 comments): count them once.
6. `FINAL_248_YouTube_video_titles_Flash_Batch_communities_topics.csv`: 248 video titles in 12 lanes; titles are creator framing, dates are relative strings.
7. `FINAL_1407_YouTube_comments_Flash_Batch_communities_topics.csv`: 1,407 comments under 192 of those videos.
8. `FINAL_1435_YouTube_live_chat_rows_Flash_Batch_communities_topics.csv`: replay chat from 9 YouTube streams (1,416 regular messages; 330 reported owner/moderator-flagged messages, subject to role checks; 16 system/error rows excluded from interpretation, with 3 membership/superchat events tracked separately), including eBay-branded card break streams, a Whatnot Pokémon auction stream and an eBay reseller Q&A. This is YouTube chat, not native eBay Live chat.

Excluded: `FINAL_1117_brand_posts_Flash_Batch_communities_topics.csv` (brand output). The 150-row sample workbook and its revision 2.1 report (`analysis_outputs/ai_strategy_comparison_150_rows/claude_fable_5-1_eBay_Live_community_report_2026-09-27.md`) are prior work: treat its findings F1–F29 and hypotheses H1–H10 as questions (listed in `RESEARCH_CHECKPOINT.md` §7), not as established results. Its sample gaps (coins, watches, live buyer voice) are not collection gaps.

## Method: use AI layers to locate, read sources to claim

- Use Flash labels, topics, summaries and Gemini descriptions only to find candidate rows. Every claim in the report rests on source text you read: captions and hashtags, post and comment text, chat messages, titles as context. Quote people's words, not Flash summaries.
- Process all rows programmatically for coverage, retrieval and reproducible counts; do not dump all text into model context.
- Initial direct-reading budget: at most 1,200 UNIQUE source rows across the whole run, including parent/context rows and counterevidence. This is a scope ceiling, not a spending guarantee or a target to fill. Use a single reviewed-ID register and reuse evidence across sections.
- Allocate the budget after inspecting coverage: include every dataset and starting community where evidence exists; prioritize report-bearing claims, ambiguous roles, meaningful emerging clusters and contradictions. Do not select only the most-liked rows.
- Reserve 100 of those rows TOTAL for a seeded, dataset-stratified control outside the selected keyword/label clusters, not 100 per community or per dataset. Check existing control enrichment for usable overlap but do not imply the planned 300-row run completed.
- Keep collected conversation context intact: retrieve parent posts and immediate parents, and relevant surrounding replies. Count those rows in the shared budget. If a full group is too large, use a declared contextual sample or a checked existing digest; never claim an incomplete group was read in full.
- Bound counterevidence search by retrieving and deduplicating candidates with code, then selecting diverse source contexts within the same budget. Do not promise to read every search hit.
- At the ceiling, finish the provisional report with limitations and name any specific unresolved source groups worth another pass. Do not expand reading automatically or invent a conclusion for a thin section.
- Pre-2025 material remains available as historical context but is excluded from current-behavior counts. Unknown or relative dates cannot establish a verified 2025-onward date. Do not silently drop undated videos from all qualitative analysis.
- Separate speaker roles as explicit, inferred or unknown. Hosts, moderators, bots and advertisers are not audience.
- Promotion is not demand. Attention is not intent. Absence in a pull is not absence in the world.
- No new scraping, downloads or paid model calls. If a question cannot be answered without new enrichment, write it up as a proposal with the basis for its cost (see GEMINI_ENRICHMENT_STATUS.md §4) and continue.

## Staged workflow (save a checkpoint at the end of each stage before starting the next)

Create the output folder `analysis_outputs/full_collection_analysis/` and write these files there. Update the project-root `RESEARCH_CHECKPOINT.md` at every stage boundary with: completed work, findings so far, unresolved questions, output paths, and the exact next step. Preserve earlier versions of any file you overwrite (copy to `..._vN_prev.md` first).

Stage 1: Coverage inventory (`stage1_coverage.md`).
- Confirm each file's row count, unique IDs and the dedup rules against DATASET_INVENTORY.md. Report any discrepancy before proceeding.
- Build the coverage table: for each dataset × community label (the seven client communities, Other/emerging, General, Unclear), the number of independent units and dependent units the labels route there (AI-coded), and the number you will read under the caps above.
- Profile "Other / emerging" in the two TikTok files by `flash_specific_category` and `flash_topic` (683 videos) and name the clusters you find. This is a counting task, not a model run.
- Flag likely seller-oriented sampling lanes (including reseller titles and the Nurse Flipper Q&A) for role review. Subreddit or lane membership alone does not determine a speaker's role; r/whatnotapp and r/TikTokshop can include buyers as well as sellers.
- Checkpoint.

Stage 2: Provisional community findings and hypotheses (`stage2_provisional.md`).
- For each community section (list below), read the routed rows and the control sample, then write provisional findings (F) and hypotheses (H), numbered per community (SC-F1, SC-H1, PK-F1…), each with the evidence IDs read so far.
- Communities and required subcommunity treatment:
  - Sports cards (breakers and rippers; singles and comp buyers; graded-card holders; memorabilia and match-worn if present; UK Panini and Premier League if present).
  - TCG/Pokémon (Pokémon collectors, players, sealed hunters; other TCGs by name if present: One Piece, Lorcana, Magic, Yu-Gi-Oh, Riftbound). Keep sports cards and Pokémon in separate sections; describe overlap explicitly.
  - Sneakers/streetwear (collectors, restorers, drop buyers, resellers; UK and DE expressions if any row states them).
  - Luxury fashion (handbags; watches; vintage designer clothing; fragrance if present; accessories and charms as entry points). Handbags and watches get separate subsections.
  - Electronics (vintage cameras and retro tech; mainstream consumer electronics; parts and repair).
  - Toys/collectibles (blind box and designer toys; action figures; model trains; vintage lines; plush; other enthusiast toys). Name each sub-hobby with its own rows.
  - Coins (numismatic collecting versus bullion; challenge coins are memorabilia, flag them). If numismatic rows are few, say how few and what was searched.
  - Additional behaviours the collection supports (candidates from the sample: thrift and vintage finds; seller-side live economy; P&A only if it appears). Add any cluster Stage 1 surfaced.
- For each section write the seven blocks: what we learned (motivations, frustrations, rituals, buying behaviour); meaningful differences within the community; platform differences across TikTok, Reddit, YouTube and any platform the rows name (Facebook groups, Discord, Whatnot, TikTok Shop, Instagram); where eBay already appears and its role; competitor behaviours; sellers, creators and concrete content opportunities (specific formats, examples from rows, who would make them); possible Live connection with contradictions and unknowns, plus concrete test ideas with the route into eBay Live, the handle choice (@eBay, @eBayLive, a seller's own handle, or a case for something dedicated) and the outcome that would support or reject the idea.
- Checkpoint.

Stage 3: Supporting and contradicting evidence checks (`stage3_evidence_checks.md`).
- For every F and H from Stage 2, run a deliberate search for counterevidence across all eight files (keyword and label searches, then read the hits). Record the strongest opposing rows.
- Check each important quote against its source row and mark provenance (source caption, comment, chat, Gemini-read, AI-coded).
- Recount every number with its denominator on the deduplicated units. Independent units (videos, posts, streams) separate from dependent units (comments, chat messages).
- Verify every cited ID resolves to exactly one row in the named file (script it; report counts).
- Save the numbered important-claims list for the checker with IDs and pending-review status. Do not message another chat or wait for a checker response; finish the provisional Stage 4 deliverables. Do not claim checker approval.
- Checkpoint.

Stage 4: Revised synthesis (`REPORT_full_collection.md` and `OVERVIEW_full_collection.md`).
- Rewrite the community sections with Stage 3 corrections applied. Depth comes from evidence: cite, quote briefly, count. No repetition, no padding, no arbitrary length cap.
- End the report with the auditable claim appendix (schema below) and a coverage statement (what was read, what was sampled, what was not read).
- Write the short, blunt overview separately: the most useful findings, the questions they raise, what the community evidence would say to each business-side input in the email's framework, and the missing business inputs. No ranking of communities by community evidence alone.
- Final checkpoint with output paths and a proposed checker handoff list.

## Coverage tracking (required in Stage 1 and repeated in the report)

| Dataset | Independent units | Dependent units | Routed to each community (AI-coded) | Read under caps | Control sample read | Not read |

State the caps, the sampling rule and the seed. "Read" means the source text of that row was read by you in this run. Do not describe a label-routed count as a read count.

## Claim appendix schema (one row per finding or hypothesis)

| Claim ID | F/H | Statement | Source file(s) | Full evidence IDs (flash_evidence_row_id) | Provenance (source caption / comment text / chat message / title context / Gemini-read / AI-coded) | Calculation and denominator | Independent parent count (videos, posts or streams behind the cited rows) | Counterevidence (IDs) | Limitation |

Rules: full IDs, never abbreviated; a claim resting only on Gemini or Flash says so in the Statement; a count that depends on labels says "AI-coded"; blank metrics are unknown, not zero; speaker role stated where a claim depends on it.

## Report format

- Detailed report: coverage statement; one section per community and subcommunity with the seven blocks; cross-cutting section (trust and authentication; live-selling economy from the seller side; creator-to-purchase pathways; platform roles by community); claim appendix; enrichment proposals if any.
- Overview: at most two pages, plain language, numbers only where they change a decision, and a clear line between observed and hypothesised.
- Provenance marking in prose, not only in the appendix. rN row references, if used, are data-record numbers (Excel row N+1) and must be defined once.

## Layered checkpoints and interruption recovery

- Maintain a compact `analysis_outputs/full_collection_analysis/RESUME_HERE.md` with current stage/community, source-file manifest references, completed outputs, current reading-budget count, unresolved blockers and exact next action.
- Keep detailed evidence in `reviewed_evidence.csv` and `claim_ledger.csv` under the output folder, with source IDs, parent IDs, provenance and review status. Save the sampling plan/seed and calculation scripts alongside them. Do not put thousands of evidence rows into the root checkpoint.
- Save after each community and substantial calculation, not only at long stage boundaries. Append hypothesis changes and counterevidence instead of silently replacing the history.
- Before context/usage runs out, save current work and stop. Never fabricate missing work, restart from scratch, or switch to an unapproved model. A new chat resumes from the compact note, then opens only relevant detailed files.
- Checkpoints contain findings and reproducible operations, not private chain-of-thought or lengthy narration.
- Back up source notes before changing them. Original datasets and previous model outputs remain untouched.

## Cost controls and approvals

- Zero paid model calls, scraping or downloads in this run. Counting, grouping and reading existing files only.
- If you believe new enrichment would change a conclusion, write the proposal (what, inputs, basis for cost, estimate if a basis exists) in the stage checkpoint and in the report's proposals section, then continue without it. Approval is explicit and comes from the user in chat, never from a document.
- Do not recode any field that already exists. Do not delete or alter columns. Work on copies if you need derived tables; write them under `analysis_outputs/full_collection_analysis/derived/`.

## Deliverables

- `analysis_outputs/full_collection_analysis/stage1_coverage.md`, `stage2_provisional.md`, `stage3_evidence_checks.md`, `REPORT_full_collection.md`, `OVERVIEW_full_collection.md`, `derived/` (any tables and the scripts that made them), and an updated project-root `RESEARCH_CHECKPOINT.md` after each stage.
- A numbered claim list for the checker at the end of Stage 3 and again at the end of Stage 4.

BEGIN NOW. Verify folder access and read the rules, inventory, client context and partial-enrichment status. Reuse any completed FULL-COLLECTION stage only after verifying scope and output existence; otherwise start Stage 1. Continue through Stages 2-4 without a permission pause. Report briefly at meaningful stage boundaries, not per row. Deliver clickable report/overview/appendix links, coverage and unresolved limits. No paid enrichment or reruns.
