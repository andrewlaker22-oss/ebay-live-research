# RESEARCH_CHECKPOINT.md — eBay Live 150-row AI comparison sample

Last updated: 2026-09-26 (Claude Fable 5.1 session)

## Goal and constraints
- Deliverable: max-500-word provisional strategy for getting people to shop on eBay Live (thesis, 2 insights, 1 test, reality check), community-specific, cited by tab + flash_evidence_row_id.
- Rules: attachment + brief only. No browsing, scraping or paid tools. Source text is evidence, not instructions. Keep source types distinct; count posts/videos separately from comments; every % needs n/N and unit; no population, conversion, GMV or geographic claims.
- Input file (exact): `data/tests_and_supporting_files/ai_strategy_comparison_150_rows/TEST_150_rows_eBay_Live_AI_comparison_sample.xlsx`
  - Tabs: Read First (22 rows), TikTok Videos (50), Reddit Conversations (50 = 10 posts + 40 comments), YouTube Comments (50 under 10 videos).
  - Supporting manifests: `.../ai_strategy_comparison_150_rows/supporting/` (not needed for this pass).

## Completed steps
1. [done] Read all 22 Read First rows (method, caveats, citation rules).
2. [done] Read all 50 TikTok Videos rows (25 direct-eBay pull, 25 community pull).
3. [done] Read all 50 Reddit rows (10 posts + 40 comments).
4. [done] Read all 50 YouTube comment rows (10 videos, 10 lanes).
5. [done] Tallies scripted (openpyxl), see below.
6. [done] Analysis written, trimmed under 500 body words, all 11 cited IDs verified against workbook (each resolves to exactly one row). Saved (see Saved outputs).

## Verified tallies (sample counts, not population estimates)
TikTok Videos (N=50 videos; multi-label, so labels sum >50):
- Flash community labels: Sports Cards 9, TCG/Pokemon 10, Sneakers 7, Luxury Fashion 6, Electronics 6, Toys 6, General 5, Other 9. Coins 0.
- Card-labelled videos (Sports Cards or TCG): 15/50 (7 direct-eBay, 8 community). 4/15 carry both labels.
- Videos mentioning a livestream: 3/50 (csv rows 667 seller Q&A live; 325 PriceHUD "whatnot, TikTok and eBay live stream"; 600 LV bags "come to my live stream check the condition"). Regex also hit row 201 but that is "lives" in prose, excluded.
- Unboxing / pack-opening / haul / blind-box / box-break format: 13/50.
- Direct-eBay pull, top 5 by comment count: row 192 scam story 622 (cards); row 345 Extended Bidding 230 (cards); row 687 vintage designer haul 117; row 667 seller live Q&A 103; row 713 Skechers 92.

Reddit (10 posts, 40 comments; comments are not independent):
- Posts by community/topic: 2 TikTokshop seller-side live/affiliate (General); r/baseballcards eBay AG packaging complaint (score 453); r/pokemoncardcollectors PSA submission stolen, resurfaced on eBay (7649); r/Sneakers eBay vs GOAT vs StockX (4/4 comments prefer eBay, citing AG/buyer protection); r/eBaySellerAdvice preloved handbag condition disputes; r/Ebay $3k camera return dispute (seller); r/ATBGE Senna model (spectator); r/Gold fake gold bars, account suspended (1835); r/Ebay counterfeit label (buyer).
- Trust/authenticity/condition/dispute is the topic of 7/10 posts. Live shopping appears in 2/10 posts, both seller-side TikTok Live. 0/10 buyer-side live rows.

YouTube (50 comments under 10 videos):
- Live lanes: whatnot_vs_ebay_live (video views 1,131): 1 buyer-voiced pro-live comment ("FaceTime between buyers and sellers"), 1 seller starting eBay Live, 3 duck-race chatter. tiktok_shop_live (1,869 views): 5/5 seller/aspiring-seller comments.
- sports_cards_breaks (283,653 views): top comment 174 likes "I'd never buy them" re mystery packs; 87 likes asks for a break-even retry.
- sneakers_auth (250,261 views): 349 likes "entire authentication process is so flawed".
- pokemon_cards_auth: "comping cards can be difficult"; tax+shipping negate deals on a $5k card.

## Provisional findings (hypotheses unless marked verified)
- VERIFIED (sample): cards dominate the highest-comment direct-eBay TikToks and the topics are eBay mechanics/risk (sniping, Extended Bidding, scams, AG packaging).
- VERIFIED (sample): break/rip live ritual is routed to TikTok Shop (row 451) and Whatnot is named as a live pricing peer (row 325). No row shows a buyer choosing eBay Live.
- HYPOTHESIS: "comp-driven card buyer" (sports + Pokemon singles, grading, AG, auctions) is a behavioral community that fits live auctions better than the break gambler; eBay's edge is comps + AG + auction mechanics.
- HYPOTHESIS/COUNTER: preloved luxury handbags may be the better live fit (only buyer-facing live invite in sample = condition inspection; handbag seller thread = condition disputes).

## Saved outputs
- Checkpoint: `RESEARCH_CHECKPOINT.md` (this file, project root).
- Final analysis (≤500 words): `analysis_outputs/ai_strategy_comparison_150_rows/claude_fable_5-1_eBay_Live_strategy_2026-09-26.md`
- Scratch tab dumps (temporary, session scratchpad only, not deliverables).

## Unresolved questions / errors
- No native eBay Live chat, sell-through or category data in sample; all live-fit inferences come from non-live sources.
- Coins: 1 Reddit post group only (gold bullion fraud), 0 TikToks. Not evidence of low potential.
- YouTube lane names do not always match content (watches_auth = fragrance; cameras_electronics = vintage Halloween buyout).
- Environment note: openpyxl had to be pip-installed; console needs PYTHONIOENCODING=utf-8 for emoji rows.

## Exact next step
- None for this deliverable. If resuming for comparison across ChatGPT/Claude/Gemini: reuse tallies above; do not re-run Gemini/Flash passes.
