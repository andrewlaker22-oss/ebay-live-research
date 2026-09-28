# Stage 3: Supporting and contradicting evidence checks (full collection)

Date: 2026-09-28. Run: full-collection analysis following `FABLE_NEW_CHAT_FULL_ANALYSIS_PROMPT.md`; rules `ANALYSIS_RULES.md` v2. Session: cloud Claude Code session on branch `main-3dv76t` (the local Stage 1–2 session ran out of context). Status: PROVISIONAL, checker-pending. No paid model calls, scraping, downloads or enrichment ran. No source file was modified and no label field was recoded.

What this stage did, in order: (1) code-retrieved candidate pools for every counterevidence search listed at the end of `stage2_provisional.md`; (2) read 85 more unique rows from those pools (seeded, spread across files), bringing the register to exactly the 1,200-row cap; (3) recounted every number in Stage 2 with its denominator on deduplicated units; (4) wrote and ran an ID resolver; (5) checked quoted phrases against their source rows; (6) built `claim_ledger.csv` (54 claims); (7) archived checkpoint v6 and wrote v7. Scripts and outputs are in `derived/` (`stage3_*.py`, `stage3_*.json`, `stage3_counterevidence_candidates.csv`).

Row convention: every citation here is a full `flash_evidence_row_id` or the abbreviated prose form used in Stage 2 (a `local_` hash prefix, a bare `t3_`/`t1_` Reddit id, a `Ug…` YouTube comment prefix, or `video_id:N` for a chat row). The resolver expands each form to exactly one row; the ledger carries only full IDs. No rN row numbers are used.

## 1. Reading budget

| Dataset | Rows read after Stage 2 | Stage 3 reads | Final rows read | Of which control | Not read |
|---|--:|--:|--:|--:|---|
| TikTok direct-eBay (1,007 videos) | 161 | 12 | 173 | 15 | 834 captions unread; no video watched |
| TikTok community (914 videos) | 164 | 16 | 180 | 15 | 734 captions unread; no video watched |
| TikTok comments (500 under 50 videos) | 100 | 0 | 100 | 10 | 400 |
| Reddit broad (100 posts, 1,998 comments) | 52 posts + 203 comments | 29 comments | 52 posts + 232 comments | 20 | 48 posts, 1,766 comments |
| Reddit r/Ebay (130 posts, 600 comments after dedup) | 34 posts + 63 comments | 5 posts + 2 comments | 39 posts + 65 comments | 10 | 91 posts, 535 comments |
| YouTube titles (248) | 89 | 4 | 93 | 8 | 155 |
| YouTube comments (1,407 under 192 videos) | 109 | 16 | 125 | 12 | 1,282 |
| YouTube replay chat (1,416 messages, 9 streams) | 141 | 0 | 141 | 10 | 1,275 (all 9 streams sampled; the Buyaparcel stream has 1 host message, unread) |
| Total | 1,115 | 85 | 1,200 | 100 (94 rows drawn as control + 6 already read) | |

"Read" means the row's source text was printed (350 to 500 characters; longer rows marked truncated in the register) and read in this run. Label-routed counts are never read counts. Seed 20260928 throughout; the final three AG rows used seed 20260929 because the pool had been partly consumed.

Stage 3 reads by search (all registered under `S3/<search>` in `reviewed_evidence.csv`): community-pull captions naming eBay 8; eBay Live rows without a promo tag 9; Whatnot first-person buying 7; live/stream first-person buying 5; blind-box rows naming eBay/Whatnot/live 1; train rows naming eBay/Whatnot/live 2; other TCGs 6; Fanatics 1; Panini/stickers 5; memorabilia/jersey/autograph 6; DE-market terms 8; authentication with positive words 15; eBay with buyer-praise phrases 9; coin pattern 3. Total 85.

## 2. Counterevidence searches and what they found

Candidate pools are source-text regex hits over the deduplicated index (system/error chat rows excluded); "read before" counts rows already in the register from Stages 1–2. Full per-search numbers are in `derived/stage3_counterevidence_candidates.csv` and the console output of `stage3_counterevidence_search.py`.

| Search (from the end of Stage 2) | Hits | Read before | Read now | Result and effect on claims |
|---|--:|--:|--:|---|
| Community-pull captions naming eBay | 8 of 914 | 0 | 8 | By label: Sports Cards 1/62, TCG 0/87, Sneakers 0/88, Luxury 1/61, Electronics 1/188, Toys 1/137, Other 4/316. Content: two model-train captions (first N-scale loco "importing random stuff on eBay", local_99a07423…; an Aristocraft unit bought "sold untested" and tested on camera, local_3cc532cf…), a 287k-view custom patch jacket built from a $25 vintage Lee jacket and patches from eBay (local_b441c945…), vintage pins from eBay (local_11c6d089…), a Nikon Coolpix "sourced from ebay" (local_ce987d6e…), "cards you buy can be investments… #ebay" (local_332a15b5…), a designer-bag collection "#ebay #mercari" (local_5afb86bf…), "Underrated Secondhand and Vintage Platforms… #ebay" (230.9k, local_6fd13074…). Corrections C3, C4; SC-F1, EL-F1, TY-F1, AB-PP-F1 amended. |
| eBay Live in source text, no promo tag | 38 of 51 | 29 | 9 | All 51 eBay Live rows are now read. New rows: an explicit positive SELLER ("our business sells a lot on eBay live streams and we do well… our prices are always fmv (Comics)", t1_p50mp5r, r/Ebay); "eBay live will do well for sellers while it's still highly promoted… artifical supply/demand" (t1_p56yrbz); "Everytime I think I have a sale it's a notification for eBay live" (UgxbPcydBm_M7LfisLt4AaABAg, 11 likes); "thinkin about whatnot or ebay live but i dont think i have the energy" (UgyHUtciql40VkPuLnx4AaABAg); a pinned creator comment comparing eBay Live, Whatnot and Tilt (UgwEGV5VWEFeN-mMMNd4AaABAg); title "Unboxing a preloved Chanel bag on EBay Live UK!" (P-F3SpVz-CQ, 61 views); three titles from eBay's own channels (d3uHPsnoITc, DjsWZaPwMQs, y-NqOxTOXP0). No unpaid first-person positive BUYER account was found (Q19). Corrections C10, C12; XC-F1, AB-SL-F1, AB-SL-F3 amended. |
| Positive AG rows (authentication + positive words) | 90 of 297 | 27 | 15 | Explicit buyer praise exists: "Just saved me from a purchase… eBay authentication got back to me showing two creases that werent on listing. Got a full refund" (UgySNeVlZQU48YJR_Dd4AaABAg, 15 likes); "I bought my Breitling Avenger off Ebay. I have also bought 2 LV purses… Ebay authentication is great" (UgwAqcvWStAcfOH6nl94AaABAg); "I am regularly buying watches on Ebay, mostly from Japan, and I trust Ebay's authentication service well" (Ugy1zfbMf-NlX2W_69p4AaABAg, 6 likes); AG appeal approved, "impressed with Tim from the leadership team at the Ebay authenticity team" (t1_niwjhum); "ebays money back guarantee" still applies after AG (t1_o64ybsb, 10); an r/Ebay commenter explaining the AG process (t1_ovl1bk3, 60). Promotion also surfaced (a consignment seller's AG praise local_3e70873d…; an #ebaypartner Balenciaga post local_a210513c…) and is marked as such. Correction C5; XC-F2, PK-F2, LX-HB-F2, LX-W-F1 amended. |
| UK Panini / Premier League / stickers | 30 (regex incl. "sticker") | 13 | 5 | "Panini" 12 rows, all US Panini America cards, repacks or breaks except one direct caption on fake World Cup boxes; "Premier League" 0 rows; "match-worn"/"game-worn" 0; "memorabilia" 1. New SC-F5 (absence in pull). |
| Memorabilia / match-worn / jersey / autograph | 33 | 12 | 6 | Rows are jerseys as apparel, "custom jersey added to cart", a rugby jersey comment, an AG-sticker explanation (t1_ovl1bk3). No memorabilia buyer voice. SC-F5. |
| DE-stated rows | 50 (loose regex) / 18 (tight) | 12 | 8 | The loose pattern matched Romanian and Spanish rows; the tight pattern (Germany, Deutschland, #Anzeige, ebay.de, modellbahn, German) gives 18 rows collection-wide. One r/whatnotapp comment lists Whatnot as live in Germany, the UK and eight other countries (t1_omyw8vx; one person's claim). No DE-stated sneaker, card or luxury buyer row. XC-F5. |
| Blind-box rows naming eBay/Whatnot/live | 1 | 0 | 1 | A Smiski collector "couldn't justify some of the prices I was seeing on eBay" and bought via Mercari/JPfans (local_4472cc81…): eBay as the price benchmark, sale lost. Correction C3; TY-F1. |
| Train rows naming eBay/Whatnot/live | 3 | 0 | 2 (+1 via the first search) | Two genuine train captions name eBay (above); the third hit is a Lionel Messi caption (false hit). Correction C3; TY-F1, TY-H2 amended. |
| YouTube `retro_gaming` lane comments | 0 | – | – | The comments file names the lane `retro_gaming_collectibles` (93 comments); the Stage 2 item used the wrong name. One such comment was read through the praise search (seller shipping tips, 382 likes, Ugz2G3PtLGmLzU4WuXh4AaABAg). The lane remains unread (Q21). |
| Other TCGs named | 13 | 7 | 6 | One Piece 4 rows, Lorcana 1, MTG 8, Yu-Gi-Oh 4, Riftbound 0. One r/IsMyPokemonCardFake seller: fake-claim abuse "happens so often with Pokemon card sales. I rarely ever have this happen with MTG, Lorcana, One Piece" (t1_o9yqku1). Yu-Gi-Oh rows are r/Sneakers buyers of Yu-Gi-Oh Nikes who chose eBay for AG (t1_ns0iwn6 AU-stated, t1_ns19b9p). New PK-F5; SN-F1 amended. |
| Fanatics | 2 | 1 | 1 | "PSA & Fanatics not being able to be sued…" (one comment). Fanatics Live: 0 rows. PK-F5. |
| eBay with buyer-praise phrases, no promo tag | 130 | 22 | 9 | Unpaid buyer joy exists outside AG: refurbished Wii "off of ebay… how i've missed these console sounds" (local_dfb628f8…, 45.4k); "Girls don't walk, run on Ebay… #digitalcameras #ebayfinds" (local_2346635f…); men's style "eBay/ thrift pickups" (local_145097e1…); "I've sold many watches on eBay and never had an issue" (t1_p5gv32z, seller). EL-F1, LX-W-F1, LX-HB-F3 amended. |
| Whatnot with first-person buying verbs | 7 | 0 | 7 | Explicit Whatnot buyer: "As a buyer I just want to buy stuff and move on. I don't want to get emails or notifications" (t1_omvn0rt, 10); a flipper who saw a Whatnot seller move a $92 tray of glass for $15 total, "I'd rather just make my money on eBay" (t1_no39bxl); how Whatnot auctions run, "watch different shows… as a buyer" (t1_nseqlli, t1_nsfnog7); an LV wallet bought on Whatnot, resold on eBay, judged counterfeit by eBay's authenticator a year later (t3_1qpssd0, 52). New XC-F3; SC-F4, LX-HB-F2 amended. |
| Live/stream with first-person buying verbs | 10 | 4 | 5 | "Did I bid $10 or did it jump to $30 in the half second… Loads of seller do 5s or less" sudden-death complaint about Whatnot (t1_owwn39k); a reseller who buys from live mega-shows to flip "because many buyers go on hype" (t1_oeva9nx); a heavy sneaker buyer ("ordered over 200 pairs the past year") on AG hub delays of up to 30 days (Ugy-N4vfOHdqoFxnakZ4AaABAg); an r/Ebay buyer with a roach-infested Xbox (t3_1wphbkz, 2026-09-24). XC-F3, SN-F1, EL-F1. |
| Coin pattern | 18 | 13 | 3 | One explicit numismatic buyer: "a seller sold me a cleaned coin as XF and refused a return because it was past a month after I got it back from NGC… the seller was able to remove [my review]" (t1_n04bfny, r/Gold, 32); a Whatnot coin seller wanting spot-price repricing (t1_oygq7h6); a Home Shopping Network comparison (t1_p515n9w). 16 of 18 read. Correction C7; CN-F1 amended. |
| TikTok captions with "break(s)" | 25 (incl. 8 YouTube titles) | 17 | 1 | "$500 Panini Repack vs $100 FlavorBurst Repack… Find your daily breaks located in our tiktok shop" (local_a45d15cb…, 447.9k). The seven "daily breaks… TikTok Shop" captions are all @burtonbreaks. Correction C1; SC-F2 amended. |

## 3. Corrections to Stage 2 (applied in `claim_ledger.csv`; superseded wording archived in `RESEARCH_CHECKPOINT.md` v7)

- C1. "Breakers promote breaks into TikTok Shop (3 burtonbreaks captions)" → seven captions, one creator (burtonbreaks), 4 of 7 read; the count is by code.
- C2. YouTube channel-run eBay break streams "26–606 views" → 10 titles, 26 to 1,317 views (the 1,317 is a Topps Marvel Vault case break). Entertainment rip and mystery-box videos in the same lane: 19,754 to 542,529; the eBay-titled mystery-box videos 21,060 to 74,669.
- C3. "Blind box and trains never name eBay in read rows" → withdrawn: two train captions name eBay as the buying venue (one shows the "sold untested, tested on camera" ritual); one blind-box caption names eBay as the too-expensive benchmark.
- C4. "Patches/pins: eBay absent from read captions" → withdrawn: a 287k-view patch-jacket caption and a vintage-pins caption name eBay as the source.
- C5. AG framed as mostly complaint → positive explicit-buyer AG rows exist in cards, sneakers, watches and handbags (rows in §2). Handbags: "AG rarely named by handbag buyers" holds for the Reddit handbag threads read, not for the YouTube watches-lane commenter.
- C6. Whatnot-sourced fake caught by eBay's authenticator on resale (t3_1qpssd0): AG can act on items that entered through a competitor.
- C7. Coins: Stage 1's 39-row pool (pattern unrecorded) → 18 rows by the recorded pattern (broad Reddit 9, r/Ebay 7, community TikTok 2; 0 elsewhere). "Numismatic collecting is not represented" → nearly absent; one explicit numismatic buyer comment exists.
- C8. Fragrance "7 rows" → 14 rows by the pattern fragrance|perfume|cologne|parfum (7 are YouTube comments under one watches-lane video).
- C9. Watches "183-row keyword pool" (Stage 1, pattern unrecorded) → 178 by the pattern recorded in `stage3_recounts.py`.
- C10. Three YouTube titles in the community titles file come from eBay's own channels (channel "ebay": sellers webinar d3uHPsnoITc, seller panel DjsWZaPwMQs; channel "eBay Live UK": y-NqOxTOXP0). They are brand output and are excluded from audience voice; they are 3 of the 13 titles naming eBay Live.
- C11. New cross-cutting finding XC-F3: the frictions eBay Live buyers describe are also described by Whatnot buyers about Whatnot (sudden-death 3–5 s auctions, swipe-bid jumps, notification pressure, hype buying).
- C12. AB-SL-F1 "eBay Live reception largely hostile" → still true of the r/Ebay seller-heavy threads read, but one explicit seller reports selling well on eBay Live at fair market value (comics), and one commenter attributes eBay Live's current seller results to front-page promotion.
- C13. Stage 2 notes cite `local_98348833…` for "Current Sneaker Rotation"; the row is `tiktok_video:local_9834883a31b26545d1be859a03a72cdb489521b328417a43e7a8249b6d0b8fe1` (typo). It is registered and cited correctly in the ledger.
- C14. Stage 2 notes cite `local_218e99db…` (a child's patch collection) as read; the row is not in the register (it was displayed outside the registering reader). It is not cited in the ledger; the coin-pattern count (2 community captions) stands as a code count.
- C15. Sneakers: Stage 2 had no unpaid buyer praising eBay; r/Sneakers buyers choosing eBay for seller photos plus AG (AU-stated) and a 200-pairs-a-year buyer describing AG hub delays are added to SN-F1.
- C16. UK Panini, Premier League, match-worn and memorabilia: 0, 0, 0 and 1 rows respectively; recorded as SC-F5 (absence in these pulls).
- C17. The Stage 2 counterevidence item "retro_gaming lane comments" used the wrong lane name; the lane is `retro_gaming_collectibles` (93 comments) and remains unread except one row (Q21).
- C18. Quote wording drift found by the quote check (§5): "best way to win an eBay auction EVERY time" is "best ya to win" in the caption; "they move so fast" is "theu move so fast"; "authenticator made a mistake" is the post title "eBay authenticator makes a mistake"; "bought probably 1000 items" is "bought probably a 1000 items"; "$1,000 negotiation" is "$1,000 Sports Card Negotiation for 1/1 Collection GRAIL". Stage 4 quotes verbatim or marks [sic].
- C19. Carried from Stage 1: owner/moderator-flagged chat messages are 329 (inventory said 330); flags are not proof of host role; chat types kept separate (1,416 messages, 10 system, 6 error, 2 membership, 1 super chat).

Corrections found by the claim support check (§10), applied to the ledger and the report after first delivery:
- C20. XC-F1: of the 9 untagged eBay Live captions, one (local_e1a367bc…, "The Infamous Unc Em strikes again! #rgbmew #ebaylivestream") is a hashtag-only mention with no announcement and an unknown role; the other 8 are show announcements or a pricing-tool ad. The 13 tagged captions come from 12 creators (yulingwu posted two).
- C21. SC-F2: the 10 channel-run eBay break titles come from 4 channels (Bomber Sports Cards 5, Roper's Rips 3, Best Card Breaks 1, SD Breaks 1); the entertainment titles from 2 channels (TRIKE Sports Cards 3, Wayne Collection 3). Units are titles, creators are fewer.
- C22. TY-F1 and TY-H2: the train captions naming eBay come from two creators; idktrains posted three of the four cited train captions (including the KATO layout and a "check this out on my shop" caption). The Pop Mart-themed caption local_0e1abd6b… is from the handle popmartunboxing.us, not verifiably Pop Mart itself; the report no longer says "Pop Mart itself".
- C23. EL-F2: both what-sold rows are one creator (finestflips).
- C24. AB-PA-F1: local_21b424cb… ("Wholesale of auto parts for Audi…") does not name eBay in its caption; it is in the eBay-term pull but is not an "eBay store routing" row. Statement corrected.
- C25. Same person cited twice: t1_ns0iwn6 and t3_1pcpv9c are one r/Sneakers poster (one AU buyer, not two); t1_p5gb6s4 and t1_p5gbcao are one r/Watches commenter. The watch-repair caption local_d21a49d8… is hashtags only; "repair" is inferred from the handle.
- C26. Shared Reddit rows: seven cited rows exist in both Reddit files (t3_1oe3rv0, t1_nkykxsw, t1_nkynsy1, t3_1om8vct, t3_1qjabr7, t3_1u2j162, t3_1u5s64o). Each carries one evidence ID, is counted once, and is now marked in the ledger's "Shared Reddit rows cited" column.

## 4. Recounts with denominators (deduplicated units; `derived/stage3_recounts.json`)

| Number in Stage 2 | Recount | Numerator / denominator / unit | Status |
|---|---|---|---|
| 22 TikTok captions name "eBay Live", all in the direct pull | 22 | 22 / 1,007 direct-pull videos; 0 / 914 community-pull videos (caption + hashtags, source text) | confirmed |
| "at least 13 of the 21 read carry a promo tag" | 13 of 22 tagged; 9 untagged | regex on caption text; each of the 13 read and confirmed | confirmed and completed (all 22 read) |
| three highest-view eBay Live captions all tagged (9.8M / 7.3M / 1.2M) | yes | views are platform metrics; tags in caption text | confirmed |
| four first-person eBay Live buyer accounts across 8,378 rows | 4 | 4 rows / 51 rows naming eBay Live / 8,339 unique rows; all 51 read | confirmed (no fifth found) |
| Sports-Cards-labelled community videos naming eBay | 1 | 1 / 62 SC-labelled community videos (label AI-coded; eBay in caption is source) | new count |
| Other labels, community pull, naming eBay | TCG 0/87; Sneakers 0/88; Luxury 1/61; Electronics 1/188; Toys 1/137; Other 4/316 | as above | new counts |
| eBay in captions, direct vs community | 684 / 1,007; 8 / 914 | source text | confirmed |
| burtonbreaks TikTok Shop captions "3" | 7 | 7 / 1,921 captions (break + TikTok Shop); 1 creator; 4 read | corrected (C1) |
| break + Whatnot; break + eBay captions | 2; 1 | / 1,921 | new |
| eBay break stream views 26–606 vs 74k–542k | 26–1,317 (10 titles) vs 19,754–542,529 (rip/mystery, 8 titles) and 1,031 (one battle video) | sports_cards_breaks lane, 20 titles, 14 naming eBay; views are platform metrics, none blank | corrected (C2) |
| other TCGs: One Piece 4, Magic 8, Yu-Gi-Oh 4, Lorcana 1, Riftbound 0 | same | rows / 8,339 | confirmed |
| Fanatics Live 2 rows | "fanatics" 2; "fanatics live" 0 | rows / 8,339 | clarified |
| coins pattern: TikTok direct 0, community 2, comments 0, YT 0, chat 0, Reddit broad 9, r/Ebay 7 | same (18) | rows / 8,339; 16 read | confirmed; Stage 1's 39 superseded (C7) |
| Flash Coins label: 1 TikTok video, 4 Reddit posts, 43 comments | same | AI-coded | confirmed |
| fragrance 7 rows | 14 | pattern fragrance|perfume|cologne|parfum / 8,339 | corrected (C8) |
| watches pool 183 | 178 | recorded pattern / 8,339 | corrected (C9) |
| 137/500 TikTok comments pre-2025 | 137 | comment_created_at < 2025-01-01 / 500 comments | confirmed |
| chat: 1,416 messages; 330 host/mod; 221 members; 148 non-host authors; 50 naming eBay | 1,416; 329; 218; 148; 50 | message rows only; flags as recorded | 329 and 218 replace 330 and 221 |
| per-stream chat counts (Stage 1 table) | Nostalgia Nomics 247/60/2; Cams Cards Thu 249/58/20; Cams Cards Discord 249/50/14; Best Card Breaks 205/0/2; Nurse Flipper 248/66/12; Whatnot Pokémon 113/34/0; Grand Salami 65/60/0; Flying V 39/0/0; Buyaparcel 1/1/0 | messages / host-mod flagged / naming eBay | confirmed |
| authentication rows | 297 (broad Reddit 141, r/Ebay 67, YouTube comments 37, titles 26, TikTok direct 25, TikTok comments 1); 91 read | pattern authenticity guarantee|ebay auth|authenticat / 8,339 | new |
| r/whatnotapp 10 posts; r/Ebay 22 broad posts | same | subreddit field, broad pull posts / 100 | confirmed |
| Panini 7 community + 7 YouTube titles (Stage 1 pool 17) | "panini" 12 (community 6, titles 4, direct 1, YT comment 1); Premier League 0 | / 8,339 | Stage 1 pool included "premier league"/"sticker" variants; 0 Premier League rows |
| UK 75, DE 53 (Stage 1 pools) | UK 72; DE 18 (tight); AU 57; Japanese eBay 40 | recorded patterns / 8,339 | replaced by recorded patterns (C-XC-F5) |
| Platform mentions | Whatnot 181; TikTok Shop 70; Vinted 49; Depop 42; Poshmark 41; GOAT 36; StockX 26; Mercari 24; Discord 21; Facebook Marketplace 15; TCGplayer 11; Chrono24 3; Purse Forum 1 | substring / 8,339 | new (XC-F4) |
| read counts per dataset (Stage 2 paragraph) | see §1 | register | confirmed for Stage 2; updated for Stage 3 |
| control 100 rows (94 new + 6 already read) | 94 rows carry CONTROL as their first section; 6 control rows had been read under a routed section | register | confirmed |

Scores, likes and views quoted in Stage 2 for individual rows are platform metrics copied from the row; the ledger's metrics column re-reads each cited row's score, likes or views from the index so the checker can compare.

## 5. Quote provenance check (`derived/stage3_quote_check.py`, output `stage3_quote_check.json`)

Every double-quoted phrase in `stage2_provisional.md` that starts with a word character (123 phrases after excluding mis-paired prose fragments) was searched, whitespace-normalised and case-insensitive, in the source text of registered rows, with ellipses split into parts that must co-occur in one row. Result: 88 phrases match a registered row's source text verbatim; 1 matches an unregistered row only ("does it work", a hypothesis label that happens to occur in t1_oy4j16b, not a quote); 34 did not match. Of the 34, 17 are labels, format names, hypothesis names or client-call phrases, not source quotes ("Other / emerging", "AG handling and packaging", "sealed vs ripped", "probably not going to be a big focus", "green shoot", "search with me / finds", "Live eBay Reseller Q&A" is a stream title held in `video_title`, not in the message field). The other 17 were traced by keyword to their rows: all sit in caption, comment or post text (none in a Gemini field) and differ only by dropped emoji, hashtag spacing ("#autodemolizione#ebay#ricambiusati" in the caption), an apostrophe ("ILL TAKE THEM"), a Spanish paraphrase ("precio y donde lo consigo" rendered as "price and where to buy"), or a silently corrected typo (C18). No Stage 2 quote was found to come from `audio_transcript`, `ad_description` or any other AI field.

## 6. ID resolution (`derived/stage3_id_resolution.py`, output `stage3_id_resolution_report.json`)

| Document | Cited tokens | Resolve to exactly one row | Ambiguous | Unresolved |
|---|--:|--:|--:|--:|
| stage2_provisional.md | 83 | 83 | 0 | 0 |
| stage2_notes_running.md | 266 | 265 | 0 | 1 (`local_98348833…`, typo, C13) |
| claim_ledger.csv | 426 | 425 | 0 | 1 (the same typo, quoted inside a limitation cell) |
| Unique across the three | 603 | 602 | 0 | 1 |

The 39 Reddit rows shared by the broad and r/Ebay pulls carry one evidence ID that appears in two files; the resolver counts each as one row and flags it as shared. Resolution proves that a citation exists; it does not validate the claim. The resolver will be re-run over `REPORT_full_collection.md` and `OVERVIEW_full_collection.md` before delivery.

Ledger integrity: 54 claims (37 findings, 17 hypotheses); 394 cited full IDs; every cited ID resolves to one row and is present in the reading register (the builder refuses to write otherwise); independent parent counts computed per claim (video, post or stream behind each cited row).

## 7. Numbered claim list for the checker (all checker-pending; statements, IDs, provenance, denominators, counterevidence and limitations are in `claim_ledger.csv`)

1. XC-F1 eBay Live in source text is promotion and seller announcements; 22/1,007 direct captions (13 tagged), 0/914 community; 51 rows in all, all read; 4 buyer accounts, all friction.
2. XC-F2 Authentication is the shared trust topic with community-specific shape; positive explicit-buyer AG rows exist in cards, sneakers, watches and handbags.
3. XC-F3 Whatnot buyers describe the same live-format frictions as eBay Live buyers.
4. XC-F4 Platform-mention counts reflect search buckets, not share of voice.
5. XC-F5 Market statements: UK 72, AU 57, DE 18, Japanese-eBay 40 rows; nothing about size follows.
6. SC-F1 Two eBay relationships in sports cards (absent from hobby-pull captions, 1/62; comp and transaction venue in the eBay pull and on Reddit).
7. SC-F2 Break promotion: 7 TikTok Shop captions from one creator; channel-run eBay break streams 26–1,317 views vs entertainment 19,754–542,529.
8. SC-F3 The one first-person eBay Live sports-card buyer account: friction, completed purchase.
9. SC-F4 Whatnot buyer voice mixed; seller voice reports low viewership and low prices.
10. SC-F5 UK Panini, Premier League, match-worn: absent from these pulls (12 Panini rows are US cards).
11. SC-H1 On-camera AG handling segment (test design in ledger).
12. SC-H2 Live comp-check segment (no buyer asks for it).
13. PK-F1 Pokémon hobby-pull attention is opening/hit-rate/grading; eBay absent (0/87).
14. PK-F2 Reddit eBay is a Pokémon dispute venue with AG defenders and a UK wish for AG.
15. PK-F3 Audience price-checks with TCGplayer and chat questions; no audience row names eBay as the comp.
16. PK-F4 eBay Live Pokémon presence is partner content and seller announcements.
17. PK-F5 Other TCGs barely present (One Piece 4, Lorcana 1, MTG 8, Yu-Gi-Oh 4, Riftbound 0; Fanatics 2).
18. PK-H1 "Open it or keep it sealed" live vote (prerecorded series already own it).
19. PK-H2 UK "AG for cards" message (one comment).
20. SN-F1 eBay in sneaker content: seller promotion, #ad AG posts, fake/AG-confusion threads, plus unpaid buyers choosing eBay for photos and AG; 0/88 hobby-pull captions.
21. SN-F2 Legit-checking is the ritual; trust contested platform by platform.
22. SN-F3 UK and AU statements exist; no DE-stated sneaker row.
23. SN-H1 Legit-check/AG walkthrough series (risk: read as #ad).
24. SN-H2 Streetwear outfit audiences differ from sneaker collecting.
25. LX-HB-F1 eBay as vintage/preloved find venue with shared vetting know-how; Japanese-eBay how-to genre.
26. LX-HB-F2 Handbag authentication is community-run; AG contested as seller protection; one positive YouTube buyer; Whatnot-sourced fake caught on resale.
27. LX-HB-F3 "Never sell luxury on eBay" is a loud r/Ebay seller theme.
28. LX-HB-H1 "How I vet a listing" live format.
29. LX-HB-H2 Preloved-luxury live auctions promoted on TikTok; one eBay Live UK Chanel unboxing title.
30. LX-W-F1 Watch voice on Reddit and YouTube comments: seller-protection doubts, AG trusted by buyers and one seller, regular Japan-sourced buying.
31. LX-W-H1 Authenticator-led live watch segment (Vookum caveat).
32. LX-VD-F1 Vintage designer clothing is finds and label education; fragrance thin (14 rows).
33. EL-F1 Four electronics strands; 1/188 hobby-pull captions name eBay; unpaid buyer joy rows exist.
34. EL-F2 "What sold today" reseller format reaches large audiences; seller education.
35. EL-H1 Live "does it work" test segment.
36. EL-H2 Retro-tech buying route is TikTok Shop and links.
37. TY-F1 Five toy hobbies with different venues; trains and pins name eBay in a few captions; blind box names eBay as too expensive once.
38. TY-F2 Purchase intent in comments ("ILL TAKE THEM") names no platform.
39. TY-F3 Whatnot's Labubu explainer: 12.1M views, top comments reject the hobby.
40. TY-H1 "Collection goes up for sale live".
41. TY-H2 Model trains: discovery question, eBay named as buying venue twice.
42. CN-F1 Numismatic voice nearly absent (18 pattern rows; one explicit numismatic buyer); label routes bullion fraud.
43. CN-F2 Silver-coin stream buyer account: over-quoting vs solds, 10-second auctions.
44. CN-H1 Sold-comp on screen for coin streams.
45. AB-TV-F1 Vintage/secondhand clothing is the largest direct-pull "Other" cluster; eBay named by buyers and resellers; Vinted/Depop/Poshmark alongside.
46. AB-TV-H1 "Vintage brands to search" as a live finds show.
47. AB-PP-F1 Patches/pins hobby cluster; eBay named as source in two captions; TikTok Shop and Etsy as maker routes.
48. AB-PM-F1 Physical-media completion rituals; eBay once in 16 read captions.
49. AB-PA-F1 P&A is eBay-native in the eBay pull (engines, parts, scrapyards) with freight/fitment/return friction.
50. AB-PA-H1 P&A live as fitment Q&A (no evidence either way).
51. AB-SL-F1 eBay Live voice: partner posts, seller comparisons, four friction buyer accounts, r/Ebay "force feed", one positive seller.
52. AB-SL-F2 Whatnot as liquidation venue per its sellers; eBay Live clientele judged "more intelligent" (seller opinion).
53. AB-SL-F3 Nurse Flipper chat is seller talk; 3 YouTube titles are eBay's own channels.
54. AB-SL-H1 Buyer-side trust mechanics for Live (comp on screen, no mid-auction change, promise enforcement, notification opt-out).

## 8. Proposals (none approved; none run)

- P1–P5 as in `GEMINI_ENRICHMENT_STATUS.md` §4 (P1 done in Stage 1 at $0).
- P6 (new, analyst time, $0 model cost): hand-read the 206 unread authentication rows and code each as positive, negative or mixed with speaker role, so the AG balance per community becomes a count with a denominator instead of examples.
- P7 (new, analyst time): read the 93 `retro_gaming_collectibles` comments and the 40 remaining Whatnot-first-person rows; both pools were only sampled.
- P8 (new, scoping needed): the eBay Live UK Chanel unboxing (P-F3SpVz-CQ) and the eBay Live seller webinar titles are the only creator- and brand-side eBay Live videos in the collection; watching them is outside this run (video content was never watched) and would need its own provenance rule.

## 10. Claim support check (`derived/stage3_claim_support_check.py`, output `stage3_claim_support_report.json`)

An ID that resolves proves a citation exists; it does not prove the row supports the claim. After first delivery, every row cited in `claim_ledger.csv` (303 unique rows: 394 citations plus counterevidence) was re-read in its read window (the first `read_chars` characters printed in this run, from `reviewed_evidence.csv`; the dump is `derived/cited_rows_read_window.txt`) and given a key phrase, the specific words that make the row support the claim it is cited for. The script checks that each phrase is present inside that window, so a citation cannot rest on text beyond what was read. Result: 303 of 303 rows carry their phrase; 53 claims supported (8 of them with notes), 1 claim is a code count with no cited rows (XC-F4). The notes are corrections C20 to C26 above. The script also counts distinct authors per claim (TikTok creator handle from the link, Reddit author, YouTube channel, comment or chat author) and marks shared Reddit rows; both are new ledger columns. Repeated creators inside a claim's evidence are now visible: burtonbreaks (SC-F2), yulingwu (XC-F1), idktrains (TY-F1, TY-H2), finestflips (EL-F2), improvthismoment (LX-W-F1), DeGuyWithDeOpinion (SN-F1 and PK-F5), Bomber Sports Cards, Roper's Rips, TRIKE and Wayne Collection (SC-F2). Reading stayed within the 1,200-row register: no new row was read for this check.

## 9. Unresolved after Stage 3 (carried to `RESEARCH_CHECKPOINT.md` v7 §5)

Q19 (no unpaid positive first-person eBay Live buyer account found in 51 rows); Q20 (206 unread authentication rows); Q21 (retro_gaming_collectibles lane unread); the buyer-vs-seller split inside the 88-video P&A cluster; whether break buyers watch on YouTube or on eBay (chat never says); host platform of the TikTok "Mega live alert" Chanel auction.
