# eBay Live community research: what the 150-row sample can and cannot say

Model: Claude Fable 5.1. Date: 2026-09-27. Input: `TEST_150_rows_eBay_Live_AI_comparison_sample.xlsx` (tabs: Read First, TikTok Videos, Reddit Conversations, YouTube Comments). No browsing, scraping or paid model calls were used. The earlier one-thesis version (2026-09-26) is preserved alongside this file; its "Comp Check Live" idea appears here as hypothesis H2, not as the recommendation.

How to read citations: `TikTok Videos r12` means row 12 of the TikTok Videos tab (its full flash_evidence_row_id is in the appendix). `reddit:t3_…` and `youtube_comment:…` are the full IDs from the Reddit and YouTube tabs. Findings are numbered F1…; hypotheses are numbered H1…. Every count that relies on Gemini or Flash labels says "AI-coded".

## 1. Coverage inventory

### 1.1 What the sample is, in independent units

| Tab | Independent units | Dependent units | Source text present | AI layers |
|---|---|---|---|---|
| TikTok Videos | 50 videos (25 from direct-eBay searches, 25 from community searches) | none (no viewer comments included; comment counts are metrics only) | caption, link, views/likes/comments/shares. Post date blank for 50/50 | Gemini video interpretation (ad_description, ebay_item, hook, first_3_seconds); later Flash text labels (community, category, topic, summary, confidence) |
| Reddit Conversations | 10 posts | 40 comments (the 4 highest-scored available direct replies per post) | title, full post text, comment text, score, date, URL | Flash labels per row |
| YouTube Comments | 10 videos (titles are context only, not evidence) | 50 comments (5 highest-liked per video) | comment text, likes, video views, comment URL. Publish dates blank | Flash labels per row; lane names were assigned by the researcher |

Two lane names do not match their content and should not be used as category evidence: `watches_auth` is a fragrance video (fake Amouage), and `cameras_electronics` is a vintage Halloween store-buyout video. There are therefore zero watch rows and zero camera rows on the YouTube tab.

### 1.2 Community coverage (AI-coded labels, checked against source text)

Counts below are Flash community labels, which are multi-label, so they sum to more than 50. They describe what the sample contains, not market size or opportunity. Reddit and YouTube comments are listed separately from the posts and videos they sit under.

| Community | TikTok videos (of 50) | Reddit post groups (of 10) | YouTube videos with comments (of 10) | Can the sample describe it? |
|---|---|---|---|---|
| Sports Cards | 9 (5 direct-eBay, 4 community) | 1 (r/baseballcards, also labelled TCG) + 4 comments | 1 (mystery packs) + 5 comments | Yes: rituals, price mechanics, trust, seller promotion |
| TCG / Pokémon | 10 (5 direct, 5 community); 4 of these also carry the Sports Cards label | 1 (r/pokemoncardcollectors) + 4 comments, plus the dual-labelled baseball group | 1 (buying at full market value on eBay) + 5 comments | Yes: chase and play motivations, grading, scarcity, theft |
| Sneakers / Streetwear | 7 (3 direct, 4 community) | 1 (r/Sneakers) + 4 comments | 1 (StockX vs GOAT vs eBay) + 5 comments | Partly: buyer platform preference and collection display, no live behaviour |
| Luxury Fashion | 6 (3 direct, 3 community): handbags 4, vintage designer clothing 1, designer buttons 1 | 1 (r/eBaySellerAdvice, seller-side handbags) + 4 comments | 2 lanes: luxury_bags_auth (seller-side AI flags) + fragrance; 10 comments | Handbags yes (mostly seller view of buyers); vintage clothing thinly; watches not at all |
| Electronics | 6 (3 direct, 3 community): vintage digital cameras 3, vintage audio 1, retro car audio 1, Apple Watch mod 1 | 1 (r/Ebay, seller dispute over a camera) + 4 comments | 1 (Apple mystery boxes) + 5 comments; the camera lane is mislabeled | Partly: vintage/retro tech and camera buyers; nothing on mainstream consumer electronics buying |
| Toys / Collectibles | 6 (3 direct, 3 community): blind box, Marvel Legends, Transformers, plush, model trains, Sanrio via Taobao | 1 (r/ATBGE Senna model; spectators, not collectors) + 4 comments | 1 (vintage GI Joe haul) + 5 comments, plus 2 collectible-ID comments under the Halloween buyout video | Partly: several distinct sub-hobbies with 1 or 2 rows each |
| Coins | 0 | 1 (r/Gold, fake bullion) + 4 comments | 0 | No. One bullion-fraud thread; no numismatic collector behaviour at all |
| General marketplace / live-selling economy | 5 | 3 (two r/TikTokshop seller threads, one counterfeit-label buyer thread) + 12 comments | 2 (eBay vs Whatnot vs Tilt; TikTok Shop live auction seller) + 10 comments | Yes for seller-side live economics; almost nothing buyer-side |
| Other / emerging (vintage finds and small collectibles) | 9: vintage jewelry lot, Baggu bag resale, designer buttons, workwear name patches, police patches, morale patches, secondhand platform guide, plus 2 noise rows | 0 (1 comment) | 1 video (vintage store buyout) + 5 comments | Suggests a "thrift and vintage finds" behaviour that cuts across labels |

Key coverage facts:

- **F1. eBay presence is a property of the search, not of the communities.** In the 25 direct-eBay TikToks, 19 captions mention eBay in the creator's own words and 3 more mention it only in the Gemini description (r9, r15, r17); r3 (Skechers) has no eBay mention anywhere and r16 is unrelated meme noise whose caption contains "eBay" inside pasted Wikipedia text. In the 25 community TikToks, 1 caption mentions eBay (r32, a hashtag) and Gemini reports an eBay listing on screen in 2 (r38, r50). Absence of eBay in community rows says nothing about whether those communities use eBay.
- **F2. Live shopping is nearly invisible in the sample.** 3 of 50 TikTok captions mention a livestream (r15 seller Q&A, r18 a pricing tool "for pricing during whatnot, TikTok and eBay live stream", r44 "Come to my live stream check the condition"). 2 of 10 Reddit posts concern live selling, both from the seller side on TikTok. On YouTube, the two live lanes hold 10 comments: 1 buyer-voiced view of live selling, 6 seller or would-be-seller voices, 3 stream-ritual chatter ("duck race"). No row shows a buyer describing a purchase on eBay Live.
- **F3. Coins is uncovered.** The single Coins group is gold bullion fraud (reddit:t3_1llzc73). The client's request for coin collectors cannot be answered from this sample; that is a collection gap, not evidence of low potential.
- **F4. Watches is uncovered.** Zero rows. The client's handbags-versus-watches distinction cannot be tested here.
- **F5. Trust, condition and dispute dominate the Reddit posts.** 7 of 10 post groups are about authenticity, condition, packaging, theft or a return dispute (baseball AG packaging, Pokémon theft, sneaker platform trust, handbag condition disputes, camera return, fake bullion, counterfeit label). This reflects the Reddit selection (eBay-term searches surface complaints) as much as the communities.
