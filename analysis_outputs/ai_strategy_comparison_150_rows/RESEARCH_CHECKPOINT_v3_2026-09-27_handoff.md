# RESEARCH_CHECKPOINT.md — eBay Live community research

Status: revision 2.1 of the 150-row sample report is final and checker-corrected. Handoff cleanup completed 2026-09-27: this checkpoint, [ANALYSIS_RULES.md](ANALYSIS_RULES.md) and the full-collection [DATASET_INVENTORY.md](analysis_outputs/full_dataset_inventory/DATASET_INVENTORY.md) are consistent with each other. Superseded claims live only in the Archive section at the end. Every current section below reflects revision 2.1 numbers.

Division of work: Gemini organises evidence (labels, summaries, transcripts already produced). Fable synthesises. The checker verifies important claims. No new scraping, downloads or paid model runs are authorised at this stage.

## 1. Goal and constraints
- Client goal: get people to visit and shop on eBay Live. Understand communities (motivations, rituals, participation and buying, attention, where eBay already fits) and what content, sellers or creators connect those behaviours to Live. Live is the urgent focus; broader eBay later. Avoid spreading across too many communities or handles. Dedicated handles are a hypothesis, not the assignment. Concrete content examples wanted.
- Markets: US, UK, Germany. No dataset here is geographically balanced; do not infer market differences.
- Evidence rules: [ANALYSIS_RULES.md](ANALYSIS_RULES.md) (source vs AI layers, denominators, independent units, speaker roles, promotion vs demand, category vs identity, counterevidence, full IDs). Apply to every community section.
- Investment decisions need business inputs (performance, supply, economics) that are not in any dataset here; community work continues without them, ranking does not.

## 2. Inputs
- Sample (analysed, closed): `data/tests_and_supporting_files/ai_strategy_comparison_150_rows/TEST_150_rows_eBay_Live_AI_comparison_sample.xlsx`. 50 TikTok videos (25 direct-eBay pull, 25 community pull), 10 Reddit posts + 40 comments, 50 YouTube comments under 10 videos. rN = data record N = Excel row N+1.
- Full collection (inventoried, not yet analysed): eight finalized non-brand CSVs in `finalized/`, profiled in [DATASET_INVENTORY.md](analysis_outputs/full_dataset_inventory/DATASET_INVENTORY.md). Brand posts excluded.
- Client context (read by checker, not by this session): `context_uploads/ebay1.txt` (call), `context_uploads/ebay12.txt` (internal), strategy email copy under `data/tests_and_supporting_files/local_llm_cleanup_pilot_20260925/supporting/original_copies/context_uploads/strategy_email.txt`.

## 3. Completed steps
1. 2026-09-26: all 150 sample rows read; one-thesis 500-word analysis saved (v1).
2. 2026-09-27: community-structured report written (revision 2), assembled from three parts.
3. 2026-09-27: checker audit received; 73 exact-match patches applied (revision 2.1); pre-patch copy preserved; ID resolution re-run (50 TikTok, 42 Reddit, 31 YouTube IDs, 0 missing).
4. 2026-09-27: handoff cleanup. ANALYSIS_RULES.md created. Eight finalized datasets inventoried by counts only (rows, units, dates, source vs AI fields, eBay and live term rates, Flash label distributions, overlaps, sample membership). Checkpoint rewritten; prior checkpoints archived.

## 4. Sample tallies (revision 2.1, verified)
TikTok (N=50 videos, 25 direct + 25 community):
- eBay in caption, direct pull: 18/25 relevant (r16 noise row contains "eBay" in pasted text and is excluded); Gemini-only 3/25 (r9, r15, r17); no relevant attribution 4/25 (r3, r11, r22, r16). Community pull: 1/25 caption (r32); 1/25 Gemini-described listing (r38, unverified); r50 Gemini editorial only, not counted.
- Livestream mentioned in caption: 3/50 (r15 seller Q&A, r18 pricing tool naming "whatnot, TikTok and eBay live stream", r44 handbag "come to my live stream check the condition", host platform not stated).
- Flash community labels (multi, AI-coded): Sports Cards 9, TCG/Pokémon 10 (4 dual-labelled), Sneakers 7, Luxury 6, Electronics 6, Toys 6, General 5, Other 9, Coins 0. eBay present by caption in: Sports Cards 3/9 (+2 Gemini-only = 5/9), Pokémon 4/10 (+1 Gemini-only), Sneakers 1/7, Luxury 3/6, Electronics 3/6, Toys 2/6.
- Shares, direct pull: r2 928, r10 496, r25 464 (third). Views, card-labelled rows: r41 180,900 is the largest. Comment counts blank for 8/50 rows: unknown, excluded from rankings. Post dates blank 50/50.
Reddit (10 posts, 40 comments): eBay in post text 8/10; trust/condition/dispute topic 7/10 posts; live selling 2/10 posts, both seller-side TikTok threads; one sampled comment is the subreddit bot (t1_nrz24ke). Handbag thread has 0 buyer voices.
YouTube (50 comments under 10 videos): the two live lanes hold 10 comments: 5 explicit seller roles, 1 role unknown, 1 enjoys live selling (role not stated), 3 duck-related chatter. Three lanes are misleading: watches_auth is fragrance, cameras_electronics is a Halloween buyout, luxury_bags_auth is general seller moderation complaints. Flash low-confidence rows 4/50.

## 5. Findings and hypotheses (revision 2.1 wording; evidence table in report section 4)
Findings (observed in the sample):
- F1 eBay presence follows the search pull, not the community. F2 live shopping nearly invisible; no buyer describes an eBay Live purchase. F3 Coins: one bullion-fraud thread only. F4 Watches: zero rows. F3 and F4 are sample gaps, not collection gaps. F5 7/10 Reddit posts are trust, condition or dispute.
- F6 Sports cards show four activities (breaks and rips, collecting journey, auction skill, risk). F7 AG raw-card packaging complaint thread. F8 mystery-pack thread mixed (enjoyment is not approval of repacks). F9 a breaker promotes daily breaks via TikTok Shop and a tool names Whatnot, TikTok and eBay Live together (promotion, not demand). F10 eBay in 5/9 sports-card TikToks (3 caption, 2 Gemini-only).
- F11 Pokémon: pack opening preferred to buying the single (one strong row). F12 grails and theft fear; a reported stolen card appeared on eBay and a commenter advised alerting eBay with cert numbers (shipment 2023, discussion 2026). F13 players vs collectors, grading scepticism, retail scarcity. F14 buying at market value; tax and shipping named as friction (one comment).
- F15 Sneakers: a self-described non-sneakerhead's question drew 4 pro-eBay replies; two YouTube comments criticise authentication (expertise and target unclear). F16 sneaker content is display, drops, restoration; three shop promos; no live.
- F17 the only buyer-facing live invite is a handbag condition check, promoted on TikTok. F18 handbag sellers describe deal-seeking, condition-scrutinising buyers (no buyer voices). F19 vintage designer hauls and platform-tier content. F20 fragrance buyers' eBay rules; one creator-inspired purchase at Heathrow (not eBay, not live); general seller complaints about AI removals (not luxury-specific).
- F21 vintage digicam buyers name eBay and price; scam anxiety voiced. F22 retro-tech spectacle; vintage audio community in Facebook groups. F23 Apple mystery-box audience watches for the gamble. F24 high-value used electronics expose sellers to forced returns.
- F25 Toys: reveal, mail day, display, expert ID, resale oracle, proxy buying; a bad-taste spectator thread (collector status unknown). F26 three bullion commenters criticise drilling or describe return conditions; poster says eBay could not explain bullion authentication. F27 live-selling economy visible only from the seller side (one bot among the 8 comments; host rates are one self-report). F28 a thrift-and-vintage-finds behaviour crosses labels. F29 seller how-to content sits in the direct pull.
Hypotheses (untested):
- H1 sports cards and Pokémon show different observed activities with shared vocabulary and shared opening/reveal behaviour; audiences may overlap. H2 "Comp Check Live" seller-hosted singles auction with last-sold prices and AG status on screen. H3 handbag condition-inspection lives (prerecorded videos are an alternative). H4 "does it work" lives for vintage electronics (same). H5 reveal and expert-ID lives for toys and vintage lots (same). H6 Pokémon chase streams. H7 thrift-and-vintage finds deserves its own bucket. H8 newcomer-oriented AG messaging for sneakers is testable. H9 break demand may already be served via TikTok Shop and Whatnot; eBay Live's position unknown. H10 tax and shipping friction on high-value live lots.

## 6. Full collection: inventory summary and dedup rules
Details and per-dataset notes: [DATASET_INVENTORY.md](analysis_outputs/full_dataset_inventory/DATASET_INVENTORY.md); raw counts in `analysis_outputs/full_dataset_inventory/inventory_out.txt`; script `inventory_script.py`.
- Rows 8,378; unique evidence IDs 8,339 (39 duplicates = rows the r/Ebay Reddit pull reused from the broad pull: 7 posts, 32 comments).
- Independent units after dedup: 1,921 TikTok videos (1,007 direct + 914 community, 0 shared links); 230 Reddit posts; 248 YouTube videos; 9 YouTube replay-chat streams with messages (6 more IDs are error-only).
- Dependent units: 500 TikTok comments (under 50 videos: 13 direct, 37 community); 2,598 Reddit comments; 1,407 YouTube comments (under 192 videos); 1,416 chat messages (330 from hosts or moderators).
- Source vs AI: TikTok has captions, hashtags, metrics and machine transcripts (1,909 videos) as source-side fields, plus Gemini video fields and Flash labels. Gemini descriptions mention eBay in 173/914 community videos whose captions mention it in 8/914: never count Gemini eBay mentions as presence.
- Dates: TikTok post dates blank for all 1,921; YouTube comment dates blank; YouTube video dates relative strings; Reddit posts 2025-01 to 2026-09; chat to 2026-09-25.
- Sample membership: 25 + 25 TikTok videos, 50 Reddit rows (all from the broad pull; 4 also in r/Ebay), 50 YouTube comments. TikTok comments, YouTube titles and replay chat contributed nothing to the sample and are new ground.
- New relative to the sample: r/whatnotapp (10 posts), r/TikTokshop (8), r/Flipping (4), r/Watches and r/rolex (2 each), Coins-labelled rows (Reddit 4 posts + 43 comments AI-coded, TikTok 1), two seller-focused YouTube lanes (reseller_what_sold 20 videos/192 comments, reseller_sourcing 20/135), replay chat from eBay-branded break streams (Cams Cards, Best Card Breaks, Grand Salami, Flying V), a Whatnot Pokémon auction stream, an eBay reseller Q&A stream, and "Other / emerging" as the largest TikTok label (683/1,921 videos, contents unprofiled).

## 7. Investigation questions for the full collection (sample findings as questions)
Each question names where to look. Look for new behaviours and contradictions, not confirmation. Absence in the sample does not predict absence here.
- Q1 (F2, F27) Is there buyer voice about live shopping anywhere? Reddit broad bucket competitor_platform_live (25 posts, r/whatnotapp 10, r/TikTokshop 8) and 177 comments with live terms; YouTube comments with live terms (72/1,407) in the whatnot_vs_ebay_live and tiktok_shop_live lanes (101 and 69 comments); the 9 replay-chat streams (non-host messages only); TikTok videos with live terms (54 direct, 45 community). Classify speakers explicit/inferred/unknown.
- Q2 (F9, H9, F8) What do participants in eBay-branded break streams and the Whatnot auction stream actually say and ask? Replay chat, 1,086 non-host messages across 9 streams. Compare with TikTok break captions and the sports_cards_breaks lane (20 videos, 101 comments). Do not treat bids or greetings as purchase intent.
- Q3 (F3) Coins: what is in the 4 Reddit posts and 43 comments labelled Coins (AI-coded), and the 1 TikTok? Is any of it numismatic rather than bullion? Check labels against text.
- Q4 (F4) Watches: r/Watches and r/rolex posts (4) inside luxury_authentication; watches_auth lane (20 videos, 60 comments): confirm the lane's videos are actually about watches before using it.
- Q5 (F17, F18, H3) Handbags: r/handbags (2 posts), luxury_authentication bucket (13 posts), luxury_bags_auth lane (20 videos, 111 comments), TikTok Luxury labels (144 + 61). Are there buyer voices on condition, and any live behaviour?
- Q6 (F11, F13, H1, H6) Pokémon vs sports cards: PokemonTCG (8 posts), IsMyPokemonCardFake (6), baseballcards (5), sportscards (2), pokemon_cards_auth (33 videos, 237 comments), TikTok TCG 77 + 87 and Sports Cards 19 + 62. Do the activities still differ, and where do the same people appear in both?
- Q7 (F15, F16, H8) Sneakers: r/Sneakers (2 posts), sneakers_auth (20 videos, 98 comments), TikTok Sneakers 145 + 88, TikTok comments Sneakers 114 (the largest comment label). Sneakers are the biggest TikTok-comment community in the collection: what do commenters say?
- Q8 (F21–F24, H4) Electronics: TikTok Electronics 157 + 188 (second-largest label), cameras_electronics lane (20 videos, 69 comments). Is the vintage-camera behaviour large, and does mainstream electronics appear?
- Q9 (F25, H5) Toys: TikTok Toys 118 + 137, TikTok comments Toys 97, retro_gaming_collectibles (19 videos, 93 comments).
- Q10 (F28, H7) Thrift and vintage: vintage_finds_nostalgia bucket (8 posts), r/Flipping (4), and above all the "Other / emerging" TikTok label (683 videos): profile its flash_specific_category values to see whether a vintage-finds community sits inside it.
- Q11 (F29, seller economy) Seller-side content and economics: reseller_what_sold and reseller_sourcing lanes (40 videos, 327 comments), the Nurse Flipper Q&A chat (248 messages), r/Ebay fees_payments_holds (22 posts). Keep seller concerns separate from buyer motivations.
- Q12 (F1) Where does eBay appear in community-pull content on its own terms? Only 8 community captions name eBay; check transcripts (3) and on-screen text (1) and ask what those few videos are.
- Q13 (F5, F7, F12, F26) Trust: r/Ebay authenticity_fakes (24 posts) and the broad trust_scams_authenticity bucket (25 posts). Separate buyer from seller voices and AG praise from AG complaints.
- Q14 (cross-cutting) Creator-to-purchase pathways like the Heathrow fragrance comment: search comments and chat for "bought", "picked up", "got it from" tied to a creator or stream.

## 8. Saved outputs
- Sample report, revision 2.1 (current): `analysis_outputs/ai_strategy_comparison_150_rows/claude_fable_5-1_eBay_Live_community_report_2026-09-27.md`
- Revision 2 pre-patch (archive): `..._2026-09-27_v2_prepatch.md`; patch script `report_parts/patch_v2_1.py`; pre-patch parts in `report_parts/` (superseded).
- v1 one-thesis analysis (archive): `analysis_outputs/ai_strategy_comparison_150_rows/claude_fable_5-1_eBay_Live_strategy_2026-09-26.md`
- Checker feedback: `analysis_outputs/ai_strategy_comparison_150_rows/CHECKER_FEEDBACK_community_report_2026-09-27.md`
- Rules: `ANALYSIS_RULES.md` (project root)
- Inventory: `analysis_outputs/full_dataset_inventory/DATASET_INVENTORY.md`, `inventory_out.txt`, `inventory_script.py`
- Prior checkpoints (archive): `analysis_outputs/ai_strategy_comparison_150_rows/RESEARCH_CHECKPOINT_v1_2026-09-26.md`, `RESEARCH_CHECKPOINT_v2_1_2026-09-27_prehandoff.md`

## 9. Unresolved issues
- No native eBay Live buyer chat or eBay transaction data in any file. The replay chat is YouTube chat from streams, some of them eBay-branded break streams; treat as adjacent, not native.
- No absolute dates for TikTok videos or YouTube comments; YouTube video dates are relative strings.
- Flash labels are weak on short text (405 low-confidence chat rows, 62 low-confidence TikTok comments). "Other / emerging" is the largest TikTok label and is unprofiled.
- Gemini eBay framing inflates apparent eBay presence (173 vs 8 in the community pull). Gemini `buyer_or_seller_angle` and `ebay_relevance` are navigation aids only.
- Reddit selection in the sample was direct replies only; the full broad pull has nested replies, so thread-level claims must be re-checked there.
- The client call and email were read by the checker, not by this session; client-requirement statements here come from the Read First tab and the brief.
- Environment: openpyxl and pandas available; console needs PYTHONIOENCODING=utf-8; long inline scripts must be saved to files before running.

## 10. Exact next step
Begin the full-collection pass by answering Q10 and Q1 first, because they cover the largest unknown (the "Other / emerging" label) and the client's core question (any buyer voice about live). Method: use Flash labels and Gemini fields only to locate rows, then read the located source rows (captions, transcripts, post and comment text, chat messages); count independent units with stated denominators; record speaker roles as explicit, inferred or unknown; log counterevidence per question; cite full evidence IDs. Save a checkpoint after each dataset. Hand important claims to the checker before they enter a client document. No new paid processing.

## Archive: superseded claims (do not reuse)
Kept for traceability only. Each was replaced in revision 2.1.
- v1 (2026-09-26): single thesis recommending "comp-driven card buyers" and "Comp Check Live" as the recommendation; now H1 and H2. "Sports and Pokémon behave as one hobby" replaced by different observed activities with overlap allowed.
- v2 (pre-patch): "19/25 direct captions mention eBay" (now 18/25 relevant, r16 excluded); "eBay in 6/9 sports-card TikToks" (now 5/9, 3 caption + 2 Gemini); "Extended Bidding is the most-shared direct-eBay row" (third); "PSA/Beckett row is the second-largest card row" (largest); "1 buyer-voiced, 6 seller, 3 ritual" split of the 10 live-lane comments (now 5 explicit seller, 1 unknown, 1 enjoys live with role not stated, 3 duck chatter); "eBay as the hobby's registry of record" (now the literal behaviour); "sneaker insiders vs entry buyers" (identities removed); "luxury sellers hit AI counterfeit flags" (general seller complaints, no category); "the Read First tab says native eBay Live chat exists in the wider corpus" (wider collection has YouTube replay chat; native eBay Live chat not established); "five Flash label errors" (classification-granularity issues, not an error rate); PSA/Beckett, £4 Gucci, "daytime jewelry", "$25 coupon" and "FINALLY BOUGHT MYSELF" presented as source text (all Gemini-read); r50 counted as a Gemini-described eBay listing (editorial only); "the sample agrees" with the client's sneaker prioritisation (removed); blank comment counts "treated as zero or unknown" (unknown only).
- v2.1 pre-handoff checkpoint: carried a patch log but left the older tallies and unresolved-issues text in place; superseded by this file.
