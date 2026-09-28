# RESEARCH_CHECKPOINT.md — eBay Live community research

Status (2026-09-28, checkpoint version 4): sample analysis closed at revision 2.1. Handoff cleanup done and corrected after the checker's 85/100 review: transcript provenance fixed, client brief read in this session, Gemini enrichment inventoried, full-analysis prompt written and saved. The full-collection analysis has NOT been executed and no paid processing has run. Prior checkpoints are archived (see §8). Superseded claims live only in the Archive section at the end.

Division of work: Gemini organises evidence (labels, summaries and frame-based descriptions already produced). Fable synthesises. The checker verifies important claims. No new scraping, downloads or paid model runs are authorised.

## 1. Goal and constraints
- Client assignment (read in full this session from `context_uploads/ebay1.txt`, `context_uploads/ebay12.txt`, the strategy email, and the sprint Q&A PDF): community understanding that helps eBay attract shoppers to eBay Live. Cover the six starting communities plus coins, meaningful subcommunities (handbags ≠ watches; toys is a catch-all), and additional behaviours the collection supports. Explain motivations, frustrations, rituals, buying behaviour, platform differences, where eBay and competitors already appear, sellers and creators, and concrete content opportunities. Live is the urgent focus; start on @eBay and @eBayLive; dedicated handles are a possible byproduct, not the assignment. Decision framework from the email: Community Opportunity × eBay Business Opportunity × eBay Right to Play; the business side is not in these datasets.
- Sprint Q&A facts worth carrying: eBay Live right-to-win categories CCG/STC, enthusiast toys, sneakers, luxury fashion/accessories; maintain low-ASP fashion, CCG singles, coins, electronics; P&A biggest core category, not on Live; named seller-creators Vookum, Tanner & Co, BlackGold Sports Cards, Linda's Stuff; Live metrics LV and QLV; DE seller Discord exists. The call said sneakers probably not a Live focus; the Q&A lists sneakers as right-to-win: report the tension.
- Evidence rules: `ANALYSIS_RULES.md` version 2 (transcript correction). Enrichment provenance: `analysis_outputs/full_dataset_inventory/GEMINI_ENRICHMENT_STATUS.md`.
- Markets US, UK, DE; no dataset is balanced; no market inference from volume.

## 2. Inputs
- Sample (closed): `data/tests_and_supporting_files/ai_strategy_comparison_150_rows/TEST_150_rows_eBay_Live_AI_comparison_sample.xlsx`; rN = data record N = Excel row N+1.
- Full collection (inventoried, not analysed): eight non-brand CSVs in `finalized/`, profiled in `analysis_outputs/full_dataset_inventory/DATASET_INVENTORY.md` (version 2). Brand posts excluded.
- Ready-to-run prompt: `analysis_outputs/full_dataset_inventory/FULL_ANALYSIS_PROMPT.md`.

## 3. Completed steps
1. 2026-09-26: sample read; v1 analysis.
2. 2026-09-27: revision 2 report; checker audit; 73 patches → revision 2.1; ID check 50/42/31, 0 missing.
3. 2026-09-27: handoff cleanup: ANALYSIS_RULES v1, DATASET_INVENTORY v1, checkpoint v3.
4. 2026-09-28: checker 85/100 corrections. (a) `audio_transcript` verified as frame-derived Gemini output: 1,067 placeholders, 12 blanks, 842 unverified entries across 1,921 videos; rules, inventory and this checkpoint corrected; nothing deleted or re-run. (b) Client call, internal discussion, email and sprint PDF read by this session. (c) Gemini enrichment inventoried (two layers, per-file QA, costs, gaps, priced proposals). (d) Live-term counts recomputed on source fields only. (e) Full-analysis prompt written.

## 4. Sample tallies (revision 2.1, unchanged)
TikTok (50): eBay in caption, direct pull 18/25 relevant (r16 noise excluded), Gemini-only 3/25 (r9, r15, r17), none 4/25 (r3, r11, r22, r16); community 1/25 caption (r32), 1/25 Gemini-described listing (r38), r50 editorial only. Livestream in caption 3/50 (r15, r18, r44; r44 host platform not stated). Labels (AI-coded, multi): Sports Cards 9, TCG 10 (4 dual), Sneakers 7, Luxury 6, Electronics 6, Toys 6, General 5, Other 9, Coins 0. eBay by caption: Sports Cards 3/9 (+2 Gemini = 5/9), Pokémon 4/10 (+1 Gemini), Sneakers 1/7, Luxury 3/6, Electronics 3/6, Toys 2/6. Shares direct pull: r2 928, r10 496, r25 464. r41 largest card-labelled row (180,900 views). Blank comment counts 8/50 = unknown.
Reddit (10 posts + 40 comments): eBay in post text 8/10; trust/condition/dispute 7/10; live 2/10 posts (seller-side); bot t1_nrz24ke; handbag thread 0 buyer voices.
YouTube (50 comments/10 videos): live lanes: 5 explicit seller, 1 unknown, 1 enjoys live (role not stated), 3 duck chatter; three mislabeled lanes (watches = fragrance; cameras = Halloween buyout; luxury bags = general seller complaints); low-confidence 4/50.

## 5. Findings and hypotheses index (revision 2.1 wording; evidence table in report §4)
F1 eBay presence follows the search pull · F2 live shopping nearly invisible; no buyer describes an eBay Live purchase · F3 Coins: bullion thread only (sample gap) · F4 Watches: zero rows (sample gap) · F5 7/10 Reddit posts trust/condition/dispute · F6 sports cards: breaks/rips, journey, auction skill, risk · F7 AG packaging thread · F8 mystery-pack thread mixed (enjoyment ≠ approval) · F9 breaker promotes TikTok Shop breaks; tool names Whatnot/TikTok/eBay Live (promotion, not demand) · F10 eBay in 5/9 sports-card TikToks (3 caption, 2 Gemini) · F11 Pokémon: opening preferred to buying (one row) · F12 grails, theft; stolen card on eBay, cert-number advice (2023 shipment, 2026 discussion) · F13 players vs collectors, grading scepticism, retail scarcity · F14 market-value buying; tax/shipping friction (one comment) · F15 non-sneakerhead's question drew 4 pro-eBay replies; 2 YouTube comments criticise authentication (expertise unclear) · F16 sneaker content display/drops/restoration; 3 promos; no live · F17 only buyer-facing live invite = handbag condition check, promoted on TikTok · F18 handbag sellers describe buyers (no buyer voices) · F19 vintage designer hauls and platform tiers · F20 fragrance rules; creator-inspired Heathrow purchase; general AI-removal complaints · F21 vintage digicam finds with price; scam anxiety · F22 retro-tech spectacle; Facebook groups · F23 mystery-box gamble audience · F24 high-value electronics returns · F25 toys: reveal, mail day, display, expert ID, resale oracle, proxy; spectator thread · F26 three bullion commenters; poster on eBay authentication · F27 live economy seller-side only (1 bot; host rates one self-report) · F28 thrift/vintage finds cross labels · F29 seller how-to content.
H1 different observed activities, shared vocabulary, overlap allowed · H2 Comp Check Live · H3 handbag condition lives (prerecorded alternative) · H4 electronics test lives (same) · H5 reveal/ID lives (same) · H6 Pokémon chase streams · H7 thrift/vintage bucket · H8 newcomer AG messaging testable · H9 breaks may be served via TikTok Shop/Whatnot; eBay Live position unknown · H10 tax/shipping friction.

## 6. Full collection: inventory summary (version 2)
- 8,378 rows; 8,339 unique evidence IDs (39 duplicates = r/Ebay rows reused from broad pull: 7 posts, 32 comments).
- Independent units after dedup: 1,921 TikTok videos; 230 Reddit posts; 248 YouTube videos; 9 chatted streams. Dependent: 500 TikTok comments (50 videos); 2,598 Reddit comments; 1,407 YouTube comments (192 videos); 1,416 chat messages (330 host/moderator).
- Source fields for TikTok are caption, hashtags and metrics only. All video-content fields, including `audio_transcript`, are Gemini frame-based interpretation. No verified transcripts exist. Gemini names eBay in 173/914 community descriptions versus 8/914 captions.
- Live terms in caption/hashtags (source only): direct 45/1,007 (eBay Live 22, TikTok Shop 9, Whatnot 5); community 33/914 (TikTok Shop 24, Whatnot 3, eBay Live 0). Reddit broad: 26/100 posts, 177/1,998 comments; r/Ebay 3/137 posts. YouTube comments 72/1,407; titles 45/248 (Whatnot 28, TikTok 18, "eBay Live" 13).
- Dates: no TikTok post dates; no YouTube comment dates; relative YouTube video dates; Reddit 2025-01 to 2026-09; chat to 2026-09-25.
- New relative to the sample: TikTok comments, YouTube titles, replay chat (all absent from the sample); r/whatnotapp 10 posts, r/TikTokshop 8, r/Flipping 4, r/Watches 2, r/rolex 2; Coins-labelled rows (Reddit 4 posts + 43 comments AI-coded; TikTok 1); seller lanes reseller_what_sold and reseller_sourcing; "Other / emerging" is the largest TikTok label (683/1,921), unprofiled.

## 7. Investigation questions for the full collection (findings as questions)
Q1 (F2, F27) buyer voice about live: r/whatnotapp, r/TikTokshop, competitor_platform_live bucket (25 posts), 177 live-term comments, YouTube live lanes (170 comments), 9 chat streams non-host messages, TikTok live-term captions (45 + 33). Roles explicit/inferred/unknown.
Q2 (F9, H9, F8) what break-stream participants say: 1,086 non-host chat messages; sports_cards_breaks lane (20 videos, 101 comments); TikTok Shop break captions.
Q3 (F3) coins: 4 Reddit posts + 43 comments labelled Coins, 1 TikTok; numismatic vs bullion; challenge coins flagged.
Q4 (F4) watches: r/Watches, r/rolex (4 posts), watches_auth lane (20 videos, 60 comments; verify content).
Q5 (F17, F18, H3) handbags: r/handbags, luxury_authentication bucket (13 posts), luxury_bags_auth lane (20/111), TikTok Luxury 144 + 61; buyer voices on condition.
Q6 (F11, F13, H1, H6) Pokémon vs sports cards: PokemonTCG 8, IsMyPokemonCardFake 6, baseballcards 5, sportscards 2, pokemon_cards_auth 33/237, TikTok TCG 77 + 87, Sports Cards 19 + 62; other TCGs by name.
Q7 (F15, F16, H8) sneakers: r/Sneakers 2, sneakers_auth 20/98, TikTok Sneakers 145 + 88, TikTok comments Sneakers 114.
Q8 (F21–F24, H4) electronics: TikTok Electronics 157 + 188, cameras_electronics 20/69.
Q9 (F25, H5) toys: TikTok Toys 118 + 137, TikTok comments Toys 97, retro_gaming 19/93; trains.
Q10 (F28, H7) thrift/vintage: vintage_finds_nostalgia 8 posts, r/Flipping 4, "Other / emerging" 683 videos profiled by flash_specific_category (no model run).
Q11 (F29) seller economics: reseller lanes 40/327, Nurse Flipper chat 248, r/Ebay fees_payments_holds 22.
Q12 (F1) eBay in community-pull content on its own terms: 8 captions.
Q13 (F5, F7, F12, F26) trust: authenticity_fakes 24, trust_scams_authenticity 25; buyer vs seller; AG praise vs complaint.
Q14 creator-to-purchase pathways ("bought", "picked up", "got it from" tied to a creator or stream).

## 8. Saved outputs
- Sample report 2.1: `analysis_outputs/ai_strategy_comparison_150_rows/claude_fable_5-1_eBay_Live_community_report_2026-09-27.md` (pre-patch copy, patch script, checker feedback, v1 analysis alongside).
- Rules: `ANALYSIS_RULES.md` (v2); v1 archived in `analysis_outputs/full_dataset_inventory/`.
- Inventory: `analysis_outputs/full_dataset_inventory/DATASET_INVENTORY.md` (v2); v1 archived alongside; `inventory_script.py`, `inventory_out.txt`.
- Enrichment status: `analysis_outputs/full_dataset_inventory/GEMINI_ENRICHMENT_STATUS.md`.
- Prompt: `analysis_outputs/full_dataset_inventory/FULL_ANALYSIS_PROMPT.md`.
- Prior checkpoints: `analysis_outputs/ai_strategy_comparison_150_rows/RESEARCH_CHECKPOINT_v1_2026-09-26.md`, `_v2_1_2026-09-27_prehandoff.md`, `_v3_2026-09-27_handoff.md`.

## 9. Unresolved issues
- No native eBay Live chat, transaction or category data in any file; replay chat is YouTube chat from streams (some eBay-branded).
- No verified transcripts; creator speech is unobserved for TikTok. 45 direct-pull rows carry a different Gemini model tag (variant unconfirmed). 12 TikTok videos have no Layer A fields.
- No measured accuracy audit for any AI field; Flash confidence is self-reported. Low-confidence rows concentrated in chat (405) and TikTok comments (62).
- Reddit broad row 506 unverified as 2025-onward; 49 comments lack parents; 39 r/Ebay rows on older prompt provenance.
- Dates weak outside Reddit and chat.
- Environment: pandas, openpyxl, pypdf available; PYTHONIOENCODING=utf-8 needed; long scripts must be saved to files before running.

## 10. Exact next step
Await the user's decision to run `FULL_ANALYSIS_PROMPT.md`. When approved, start at Stage 1 (coverage inventory and the "Other / emerging" profile, both counting-only), save `stage1_coverage.md`, update this checkpoint, then proceed. Proposals P2–P5 in GEMINI_ENRICHMENT_STATUS.md remain unapproved; P1 needs no approval.

## Archive: superseded claims (do not reuse)
- v1 (2026-09-26): single thesis "comp-driven card buyers" and "Comp Check Live" as recommendation; now H1, H2. "Sports and Pokémon behave as one hobby" → different observed activities, overlap allowed.
- v2 (pre-patch): 19/25 captions (→18/25); 6/9 sports-card eBay (→5/9); Extended Bidding most-shared (→third); PSA/Beckett second-largest (→largest); 1 buyer/6 seller/3 ritual split (→5 explicit seller, 1 unknown, 1 role not stated, 3 chatter); "registry of record"; sneaker "insiders"; luxury-specific AI flags; native eBay Live chat in wider corpus (→YouTube replay chat only); "five Flash errors" (→granularity issues); PSA/Beckett, £4 Gucci, "daytime jewelry", $25 coupon, Speedy 20 text as source (→Gemini-read); r50 as listing (→editorial); sample "agrees" with client sneaker view (removed); blank counts "zero or unknown" (→unknown).
- v3 checkpoint and ANALYSIS_RULES v1 / DATASET_INVENTORY v1 (2026-09-27): described `audio_transcript` as a machine speech-to-text transcript usable to check Gemini on-screen claims; claimed "machine transcripts for 1,909 videos"; live-term counts of 54/1,007 and 45/914 that mixed Gemini fields with source fields; stated the sample gaps as if they might extend to the collection. All withdrawn in version 2 documents and this checkpoint. Client-brief statements in v3 came from the Read First tab; this version's come from the originals.
