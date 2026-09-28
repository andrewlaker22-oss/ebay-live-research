# Dataset inventory: eight finalized non-brand datasets

Date: 2026-09-27; corrected 2026-09-28 (version 2: the `audio_transcript` field is Gemini frame-based output, not speech-to-text; version 1 archived as `DATASET_INVENTORY_v1_2026-09-27.md`). Method: column and count profiling only (`inventory_script.py`, raw output in `inventory_out.txt`). No content reading, no model calls, no files changed. Brand posts (`FINAL_1117_brand_posts…`) are excluded from community analysis as brand output. Rules applied: [ANALYSIS_RULES.md](../../ANALYSIS_RULES.md). Enrichment provenance and QA status per file: [GEMINI_ENRICHMENT_STATUS.md](GEMINI_ENRICHMENT_STATUS.md).

All files live in `finalized/`. Every row carries `flash_evidence_row_id`; it is unique within each file and is the join and dedup key. Across the eight files there are 8,378 rows and 8,339 unique IDs: the 39 duplicates are the rows the r/Ebay Reddit pull reused from the broad Reddit pull (7 posts + 32 comments).

## 1. Summary table

| # | File | Independent units | Dependent units | Source-text fields | AI layers present | Dates | Relation to 150-row sample |
|---|---|---|---|---|---|---|---|
| 1 | FINAL_1007_direct_eBay_TikTok_videos | 1,007 videos (1,007 unique links) | none (metrics only) | caption, hashtags, views/likes/comments/shares. No verified transcript exists | Gemini frame-based video fields (ad_description, visual_description, hook, first_3_seconds, ebay_item, notable_text_on_screen, claim, cta, buyer_or_seller_angle, ebay_relevance, item_category, audio, and `audio_transcript`, which is frame-derived, not speech-to-text); Flash labels | post date blank 1,007/1,007; track date 2026-09-24 only | 25 sample videos come from here |
| 2 | FINAL_914_community_TikTok_videos | 914 videos (914 unique links; 0 shared with file 1) | none | as file 1. No verified transcript exists | as file 1 | post date blank 914/914 | 25 sample videos |
| 3 | FINAL_500_TikTok_comments_50_videos | 50 parent videos (13 from file 1, 37 from file 2) | 500 comments (10 per video), 500 unique comment IDs | comment_text, likes, comment_created_at, author | Flash labels; parent video's Gemini item_category/ebay_item carried over | comments 2021-03-08 to 2026-09-25 | 0 sample rows: entirely new to the analysis |
| 4 | FINAL_100_Reddit_conversations_1998_comments ("broad") | 100 posts, 20 subreddits, 6 buckets | 1,998 comments (mean 20 per post, max 30; nested to depth 4) | title, text, score, upvote_ratio, posted_at, url, author, parent_id, depth | Flash labels | posts 2025-01-21 to 2026-09-18 (1 blank) | all 50 sample Reddit rows come from here |
| 5 | FINAL_137_rEbay_posts_632_comments | 137 posts, r/Ebay only, 7 buckets | 632 comments (mean 4.6, max 5) | as file 4 | Flash labels | posts 2025-09-26 to 2026-09-25 | 4 sample rows also appear here (they are among the 39 shared rows) |
| 6 | FINAL_248_YouTube_video_titles | 248 videos, 194 channels, 12 lanes | none | title, views, channel, duration, url | Flash labels on titles | relative strings only ("10d ago", "Streamed 9h ago"): no absolute dates | 0 sample rows (sample used titles as context only) |
| 7 | FINAL_1407_YouTube_comments | 192 of the 248 videos have comments | 1,407 comments (mean 7.3 per video, max 10), 1,407 unique IDs | comment_text, likes, reply_count, author, is_pinned, hearted_by_creator | Flash labels | published blank 1,407/1,407 | 50 sample comments |
| 8 | FINAL_1435_YouTube_live_chat_rows (replay chat) | 15 video IDs, of which 6 are error-only rows; 9 streams have chat; 0 overlap with files 6 and 7 | 1,416 chat messages + 10 system + 6 error + 2 membership + 1 super chat | message, author, offset, is_owner, is_moderator, is_member, super_chat | Flash labels (low confidence on 405 rows, short messages) | published_at up to 2026-09-25 | 0 sample rows: entirely new |

Independent units after dedup: 1,921 TikTok videos; 230 Reddit posts (237 minus 7 shared); 248 YouTube videos plus 9 chatted streams. Dependent units after dedup: 500 TikTok comments; 2,598 Reddit comments (2,630 minus 32 shared); 1,407 YouTube comments; 1,416 chat messages.

## 2. Per-dataset notes (counts are exact; labels are AI-coded)

### 2.1 TikTok direct-eBay videos (1,007)
- Pull: `ebay_expanded_search_fast_frames`, all "Research downloads". Gemini status: 1,001 done, 6 failed (no Gemini fields for those 6). Model field: 956 rows `gemini-2.5-flash fast-frames`, 45 rows `gemini-2.5-flash` (a different run variant; treat its provenance as unconfirmed).
- The `audio_transcript` field is Gemini output from sampled frames and metadata, not audio. Direct pull: 479 rows "[MUSIC / NO CLEAR SPEECH DETECTED]", 49 "unknown from sampled frames", 6 blank; 473 populated entries of unverified provenance (189 longer than 150 characters). The `audio` field is likewise interpretation (361 "no clear speech", 154 "Talking head", 139 "unknown from sampled frames").
- eBay in source text: 684/1,007 captions or hashtags. Gemini-derived eBay mentions, for navigation only: 270/1,007 in the frame-derived transcript field; 145/1,007 in Gemini-read on-screen text; 791/1,007 in Gemini descriptions. Only the caption/hashtag count is "observed".
- Live-related terms in caption or hashtags (source only): 45/1,007 videos, of which "eBay Live" 22, "TikTok Shop" 9, "Whatnot" 5. (The version-1 figure of 54 included frame-derived Gemini fields and is withdrawn.)
- Gemini `buyer_or_seller_angle` (interpretation): buyer 475, reseller 156, seller 141, buyer+collector 57, collector 38, unclear 34, other combinations. Navigation aid only.
- Flash community (multi-label): Other/emerging 367, Electronics 157, Sneakers 145, Luxury 144, Toys 118, General marketplace 77, TCG/Pokémon 77, Sports Cards 19, Unclear 9. Confidence high 899, medium 99, low 9.
- Metrics: comments blank for 116 videos (unknown, not zero); views present for all.

### 2.2 TikTok community videos (914)
- Same pipeline; 908 done (all `gemini-2.5-flash fast-frames`), 6 failed. No links shared with the direct pull.
- `audio_transcript` placeholders: 504 "[MUSIC / NO CLEAR SPEECH DETECTED]", 32 "unknown from sampled frames", 3 rows echoing the prompt's fallback sentence ("Known transcript if provided in metadata/context, otherwise…"), 6 blank; 369 populated entries of unverified provenance (119 longer than 150 characters). The echoed fallback sentence is direct evidence that the model was asked for a transcript it could not hear.
- eBay in source text: 8/914 captions or hashtags. Gemini-derived, navigation only: 3/914 in the frame-derived transcript field; 1/914 on-screen; 173/914 Gemini descriptions. The 173-versus-8 gap is the clearest measure of Gemini's tendency to add eBay framing; never count Gemini eBay mentions as presence.
- Live-related terms in caption or hashtags (source only): 33/914 videos, of which "TikTok Shop" 24, "Whatnot" 3, "eBay Live" 0. (The version-1 figure of 45 mixed source and Gemini fields and is withdrawn.) The community pull's live signal is TikTok Shop promotion; the direct pull's is eBay Live mentions.
- Gemini angle: collector 338, buyer 191, unclear 80, seller 74, collector+buyer 55, collector+reseller 51, reseller 28.
- Flash community: Other/emerging 316, Electronics 188, Toys 137, Sneakers 88, TCG/Pokémon 87, Sports Cards 62, Luxury 61, Unclear 25, Coins 1, General 1. Confidence high 875, medium 35, low 4. Comments blank 58.
- "Other / emerging" is the largest label in both TikTok pulls (683 of 1,921 videos carry it). Its contents are unknown until profiled; this is where the sample's thrift-and-vintage pattern (H7) would show up if it exists at scale.

### 2.3 TikTok comments (500 under 50 videos)
- First and only TikTok audience-voice dataset. 10 comments per video. Parent videos: 13 direct-pull, 37 community-pull; parent Gemini categories are mostly sneakers (9), toys/collectibles (6), trading cards (5), electronics (4), clothing (3), bags (2).
- eBay named in 6/500 comments; live terms in 0/500.
- Flash community: Sneakers 114, Toys 97, Other 83, Electronics 55, TCG 50, Luxury 49, Unclear 34, General 12, Sports Cards 10. Confidence high 330, medium 108, low 62 (many short comments).
- Comment dates span 2021 to 2025-09, so some comments are years older than the collection.

### 2.4 Reddit broad conversations (100 posts, 1,998 comments)
- Buckets (researcher-assigned search groups): trust_scams_authenticity 25, competitor_platform_live 25, general_viral 15, cards_collectibles 14, luxury_authentication 13, vintage_finds_nostalgia 8.
- Subreddits by post count: Ebay 22, whatnotapp 10, PokemonTCG 8, TikTokshop 8, IsMyPokemonCardFake 6, baseballcards 5, Flipping 4, mildlyinfuriating 3, Superstonk 3, technology 3, sportscards 2, Watches 2, eBaySellerAdvice 2, rolex 2, handbags 2, Sneakers 2, and 5 single-post subreddits. r/whatnotapp (10 posts) is the largest competitor-native community source in the whole collection and was absent from the 150-row sample.
- eBay named in 88/100 posts and 443/1,998 comments. Live terms in 26/100 posts and 177/1,998 comments.
- Comments are nested (depth 0: 1,008; 1: 513; 2: 267; 3: 111; 4: 53), so reply context exists here, unlike the sample's direct-replies-only selection.
- Flash community (posts): General 22, TCG 22, Sports Cards 18, Other 17, Luxury 12, Electronics 9, Toys 5, Sneakers 3, Coins 2, Unclear 2. Watches: 2 r/Watches + 2 r/rolex posts sit inside luxury_authentication. Coins: 2 posts and 34 comments labelled Coins.

### 2.5 Reddit r/Ebay (137 posts, 632 comments)
- Buckets: general_recent 25, authenticity_fakes 24, fees_payments_holds 22, buyer_seller_pain 19, collectibles_cards 18, shipping_delivery 15, current_recent 14. Dates 2025-09-26 to 2026-09-25: this is the most recent Reddit material.
- Live terms in only 3 posts and 4 comments: this pull is about marketplace operations, not live.
- Flash community (posts): General 63, Other 26, TCG 17, Electronics 10, Luxury 10, Toys 7, Sports Cards 6, Sneakers 2, Unclear 2, Coins 2.
- Dedup: 7 posts and 32 comments are the same rows as in the broad pull (identical evidence IDs). Count them once.

### 2.6 YouTube video titles (248)
- 12 lanes, roughly 20 videos each (pokemon_cards_auth 33, buyer_experience 17, retro_gaming 19, tiktok_shop_live 19). Two lanes were excluded from the buyer-focused sample by design: reseller_what_sold (20) and reseller_sourcing (20).
- eBay in 150/248 titles; live terms in 45; "Whatnot" in 28, "TikTok" in 18, "eBay Live" in 13 titles.
- Titles are creator framing, not audience voice. Dates are relative strings and cannot be converted reliably.
- Lane names are not content evidence (see ANALYSIS_RULES.md §1): the sample found three lanes whose selected video did not match the lane name.

### 2.7 YouTube comments (1,407 under 192 videos)
- Up to 10 top comments per video; 56 of the 248 videos have none. Lane distribution follows the video list (pokemon_cards_auth 237, reseller_what_sold 192, buyer_experience 141, reseller_sourcing 135, luxury_bags_auth 111, sports_cards_breaks 101, whatnot_vs_ebay_live 101, sneakers_auth 98, retro_gaming 93, cameras_electronics 69, tiktok_shop_live 69, watches_auth 60).
- eBay in 159/1,407 comments; live terms in 72/1,407. No comment dates.
- Flash community: General 412, Other 227, TCG 225, Unclear 138, Sports Cards 137, Luxury 113, Sneakers 111, Electronics 64, Toys 62. Confidence high 1,080, medium 236, low 91.

### 2.8 YouTube live replay chat (1,435 rows, 9 streams with chat)
- What it is: replay chat captured from YouTube streams. Several are eBay break streams mirrored on YouTube; one is a Whatnot auction stream; one is an eBay reseller Q&A. It is not native eBay Live chat, but it is the closest thing in the collection to live-audience voice.
- Streams and message counts (messages; of which host or moderator; of which eBay named):
  - LIVE Pokemon RIP N SHIP, Nostalgia Nomics: 247; 60 host/mod; 2 eBay. 98 messages from channel members.
  - Thur Night eBay Breaks (Signature Class / Bowman Chrome), Cams Cards: 249; 58; 20.
  - Discord Breaks (eBay Returns Wed), Cams Cards: 249; 50; 14.
  - eBay 2025 Bowman Chrome FIVE CASE Pick Your Player Break, Best Card Breaks: 205; 0 flagged host/mod; 2.
  - Live eBay Reseller Q&A, The Nurse Flipper: 248; 66; 12. 120 member messages. Seller-audience stream.
  - Bidding on Pokémon Card Auctions LIVE, Slab Hunting on Whatnot, Cloud Shape Interpreting: 113; 34; 0.
  - 2022 Bowman Draft Jumbo 2-Box Break, Grand Salami Sports Cards: 65; 60 host/mod; 5 audience messages only.
  - Triple Header Break Night, Flying V Sports Cards & Breaks: 39; 0; 0.
  - Buyaparcel eBay LIVE Spotlight on Dewalt, £1 Auctions: 1 message (owner). Effectively empty; UK retailer stream.
  - 6 further video IDs returned only an error row (no title, no chat).
- Speaker roles: 330 of 1,416 messages are from the channel owner or moderators (explicit host role); 221 are from channel members; 148 distinct non-host authors. Apply ANALYSIS_RULES.md §4: host messages are not audience voice.
- Flash community: Sports Cards 777, TCG 319, Unclear 153, General 149, Other 36. Flash confidence is low on 405 rows and medium on 458: chat lines are short and labels are weak here.
- 16 system/error rows were excluded from Flash interpretation by the processing run; keep them excluded.

## 3. Deduplication and joining rules
1. Reddit: drop the 39 rows in file 5 whose `flash_evidence_row_id` also appears in file 4 (7 posts, 32 comments), or count them once under the broad pull.
2. TikTok comments (file 3) join to their parent video by `video_url` = `link` in file 1 or 2. Do not count a parent video twice when it appears in a video-level tally and a comment-level tally.
3. YouTube comments (file 7) join to titles (file 6) by `video_id`; all 192 commented videos are in the 248 list. Live chat (file 8) shares no `video_id` with files 6 or 7: it is a separate set of streams.
4. The 150-row sample is a strict subset of files 1, 2, 4, 5 (shared rows) and 7. Sample findings about TikTok comments, YouTube titles and live chat do not exist; those three datasets are new ground.
5. Independent units for any claim are videos, posts or streams. Comments and chat messages are always reported as "N comments under M videos/posts" or "N messages across M streams".

## 4. What the full collection adds that the sample lacked
- Audience voice on TikTok (500 comments), reply-nested Reddit threads (depth up to 4), competitor-native communities (r/whatnotapp 10 posts, r/TikTokshop 8, r/Flipping 4), watch communities (r/Watches, r/rolex, watches_auth lane), coin-labelled rows (Reddit 4 posts + 43 comments AI-coded; TikTok 1), seller-focused YouTube lanes (reseller_what_sold, reseller_sourcing), and replay chat from eBay-branded break streams and a Whatnot auction stream.
- No verified transcripts. The `audio_transcript` column is frame-derived Gemini output (1,067 placeholders, 12 blanks, 842 populated entries of unverified provenance across 1,921 videos) and cannot be used to check Gemini's other fields. Creator speech is unobserved in this collection; captions and hashtags are the only creator-authored text for TikTok.
- Absolute dates remain weak: no TikTok post dates, no YouTube comment dates, relative YouTube video dates. Only Reddit and live chat carry usable timestamps.
