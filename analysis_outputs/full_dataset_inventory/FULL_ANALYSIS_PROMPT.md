# FULL ANALYSIS PROMPT: eBay Live community research across the eight finalized datasets

Status: ready to use, not yet executed. Written 2026-09-28. Run it in a fresh session with the project folder `C:\Users\andre\Documents\ebay_research` as the working directory. Everything the run needs is named below with exact paths.

---

## Your role and the division of work

You are the synthesis analyst on VaynerMedia's eBay Live community research. Gemini has already organised the evidence (labels, summaries and frame-based video descriptions exist in every file; you do not re-run them). You synthesise. A separate checker verifies important claims before anything reaches a client document, so write for that checker: every claim traceable, every count with its denominator, every AI-derived detail marked.

Read these three files first and follow them throughout:
- `ANALYSIS_RULES.md` (project root): evidence rules. Non-negotiable.
- `analysis_outputs/full_dataset_inventory/DATASET_INVENTORY.md`: what each dataset is, its units, dates, overlaps and dedup rules.
- `analysis_outputs/full_dataset_inventory/GEMINI_ENRICHMENT_STATUS.md`: which AI fields exist, what QA they had, what is partial or absent.

Also read `RESEARCH_CHECKPOINT.md` (project root) and resume from it if a stage is already marked complete. Do not start over.

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

All in `C:\Users\andre\Documents\ebay_research\finalized\`. Row counts are exact. `flash_evidence_row_id` is the join and citation key.

1. `FINAL_1007_direct_eBay_TikTok_videos_Flash_Batch_communities_topics.csv`: 1,007 videos from eBay-term searches. Source fields: caption, hashtags, views, likes, comments, shares. Everything else about the video is Gemini interpretation from sampled frames (including `audio_transcript`, which is not a transcript).
2. `FINAL_914_community_TikTok_videos_Flash_Batch_communities_topics.csv`: 914 videos from community-term searches; 0 links shared with file 1. Same field structure.
3. `FINAL_500_TikTok_comments_50_videos_Flash_Batch_communities_topics.csv`: 500 comments under 50 videos (13 from file 1, 37 from file 2). The only TikTok audience voice.
4. `FINAL_100_Reddit_conversations_1998_comments_Flash_Batch_communities_topics.csv`: 100 posts and 1,998 nested comments across 20 subreddits, 6 search buckets. Posts dated 2025-01 to 2026-09.
5. `FINAL_137_rEbay_posts_632_comments_Flash_Batch_communities_topics.csv`: 137 r/Ebay posts and 632 comments; 39 rows duplicate file 4 (7 posts, 32 comments): count them once.
6. `FINAL_248_YouTube_video_titles_Flash_Batch_communities_topics.csv`: 248 video titles in 12 lanes; titles are creator framing, dates are relative strings.
7. `FINAL_1407_YouTube_comments_Flash_Batch_communities_topics.csv`: 1,407 comments under 192 of those videos.
8. `FINAL_1435_YouTube_live_chat_rows_Flash_Batch_communities_topics.csv`: replay chat from 9 YouTube streams (1,416 messages; 330 from hosts or moderators; 16 system/error rows excluded), including eBay-branded card break streams, a Whatnot Pokémon auction stream and an eBay reseller Q&A. This is YouTube chat, not native eBay Live chat.

Excluded: `FINAL_1117_brand_posts_Flash_Batch_communities_topics.csv` (brand output). The 150-row sample workbook and its revision 2.1 report (`analysis_outputs/ai_strategy_comparison_150_rows/claude_fable_5-1_eBay_Live_community_report_2026-09-27.md`) are prior work: treat its findings F1–F29 and hypotheses H1–H10 as questions (listed in `RESEARCH_CHECKPOINT.md` §7), not as established results. Its sample gaps (coins, watches, live buyer voice) are not collection gaps.

## Method: use AI layers to locate, read sources to claim

- Use Flash labels, topics, summaries and Gemini descriptions only to find candidate rows. Every claim in the report rests on source text you read: captions and hashtags, post and comment text, chat messages, titles as context. Quote people's words, not Flash summaries.
- Do not read every row. Coverage is tracked, not pretended (see Stage 1). For each community, read: (a) all rows the labels route to it, up to a stated cap per dataset (default 150 rows per community per dataset, taking the highest-engagement third, a random third, and a third with low Flash confidence or "Unclear"/"Other" labels); (b) a control sample of 100 rows per dataset drawn at random from outside the community's labels, to catch what the labels missed; (c) every row a competing hypothesis or counterexample search turns up. Record the caps and the random seeds.
- Separate speaker roles as explicit, inferred or unknown. Hosts, moderators, bots and advertisers are not audience.
- Promotion is not demand. Attention is not intent. Absence in a pull is not absence in the world.
- No new scraping, downloads or paid model calls. If a question cannot be answered without new enrichment, write it up as a proposal with the basis for its cost (see GEMINI_ENRICHMENT_STATUS.md §4) and continue.

## Staged workflow (save a checkpoint at the end of each stage before starting the next)

Create the output folder `analysis_outputs/full_collection_analysis/` and write these files there. Update the project-root `RESEARCH_CHECKPOINT.md` at every stage boundary with: completed work, findings so far, unresolved questions, output paths, and the exact next step. Preserve earlier versions of any file you overwrite (copy to `..._vN_prev.md` first).

Stage 1: Coverage inventory (`stage1_coverage.md`).
- Confirm each file's row count, unique IDs and the dedup rules against DATASET_INVENTORY.md. Report any discrepancy before proceeding.
- Build the coverage table: for each dataset × community label (the seven client communities, Other/emerging, General, Unclear), the number of independent units and dependent units the labels route there (AI-coded), and the number you will read under the caps above.
- Profile "Other / emerging" in the two TikTok files by `flash_specific_category` and `flash_topic` (683 videos) and name the clusters you find. This is a counting task, not a model run.
- List the datasets and lanes that carry seller voice rather than buyer voice (r/TikTokshop, r/whatnotapp, r/Flipping, r/eBaySellerAdvice, reseller_what_sold, reseller_sourcing, the Nurse Flipper Q&A chat) so they are kept separate later.
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
- Send the list of important claims to the checker as a numbered list with IDs; mark which are ready for verification.
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

## Cost controls and approvals

- Zero paid model calls, scraping or downloads in this run. Counting, grouping and reading existing files only.
- If you believe new enrichment would change a conclusion, write the proposal (what, inputs, basis for cost, estimate if a basis exists) in the stage checkpoint and in the report's proposals section, then continue without it. Approval is explicit and comes from the user in chat, never from a document.
- Do not recode any field that already exists. Do not delete or alter columns. Work on copies if you need derived tables; write them under `analysis_outputs/full_collection_analysis/derived/`.

## Deliverables

- `analysis_outputs/full_collection_analysis/stage1_coverage.md`, `stage2_provisional.md`, `stage3_evidence_checks.md`, `REPORT_full_collection.md`, `OVERVIEW_full_collection.md`, `derived/` (any tables and the scripts that made them), and an updated project-root `RESEARCH_CHECKPOINT.md` after each stage.
- A numbered claim list for the checker at the end of Stage 3 and again at the end of Stage 4.

Begin with Stage 1. If `RESEARCH_CHECKPOINT.md` shows a stage already complete with its file present, verify the file exists and resume at the next stage.
