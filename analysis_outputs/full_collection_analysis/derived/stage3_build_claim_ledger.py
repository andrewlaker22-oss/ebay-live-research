"""Builds claim_ledger.csv (schema from FABLE_NEW_CHAT_FULL_ANALYSIS_PROMPT.md) from the Stage 2 findings/hypotheses
with Stage 3 corrections applied. IDs may be written abbreviated here; every one is expanded to its full
flash_evidence_row_id through stage3_id_resolution.resolve and the build fails if any does not resolve to exactly
one row. Independent parent counts, files and metrics come from unified_evidence_index.csv. Status is always
checker-pending: nothing here is verified by the checker or approved by the client."""
import os, re, json, csv, pandas as pd, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import stage3_id_resolution as IR
HERE = IR.HERE; IDX = IR.IDX
REG = pd.read_csv(os.path.join(HERE, "..", "reviewed_evidence.csv"), dtype=str, keep_default_na=False)
READ = set(REG.evidence_id)
RC = json.load(open(os.path.join(HERE, "stage3_recounts.json")))
FILE_LABEL = {"tt_direct": "FINAL_1007_direct_eBay_TikTok_videos", "tt_comm": "FINAL_914_community_TikTok_videos", "tt_comments": "FINAL_500_TikTok_comments_50_videos",
              "rd_broad": "FINAL_100_Reddit_conversations_1998_comments", "rd_ebay": "FINAL_137_rEbay_posts_632_comments", "yt_titles": "FINAL_248_YouTube_video_titles",
              "yt_comments": "FINAL_1407_YouTube_comments", "yt_chat": "FINAL_1435_YouTube_live_chat_rows"}
def kind_of(tok):
    if tok.startswith(("tiktok_video:", "tiktok_comment:", "reddit:", "youtube_comment:", "youtube_video:", "youtube_live:")): return "full"
    if tok.startswith("local_"): return "local_prefix"
    if re.fullmatch(r"t[13]_[a-z0-9]+", tok): return "reddit_bare"
    if tok.startswith("Ug"): return "ytc_prefix"
    if re.fullmatch(r"[A-Za-z0-9_\-]{11}:\d+", tok): return "chat_ref"
    if re.fullmatch(r"[A-Za-z0-9_\-]{11}", tok): return "yt_video_bare"
    raise ValueError(tok)
ERRORS = []
def expand(ids):
    out = []
    for tok in ids:
        m = IR.resolve(kind_of(tok), tok)
        if len(m) != 1:
            ERRORS.append(f"ID does not resolve to exactly one row: {tok} -> {m}"); continue
        out.append(m[0])
    return out
def parent_key(r):
    f = r["file"]
    if f in ("tt_direct", "tt_comm"): return "video:" + r["evidence_id"]
    if f == "tt_comments": return "video_link:" + r["parent_id"]
    if f in ("rd_broad", "rd_ebay"): return "post:" + r["post_id"]
    if f == "yt_titles": return "ytvideo:" + r["video_id"]
    if f == "yt_comments": return "ytvideo:" + r["video_id"]
    if f == "yt_chat": return "stream:" + r["video_id"]
    return r["evidence_id"]
def metric(r):
    f = r["file"]
    if f in ("tt_direct", "tt_comm"): return f"views={r['views'] or 'unknown'}"
    if f in ("rd_broad", "rd_ebay"): return f"score={r['score'] or 'unknown'} {r['subreddit']} {r['date'][:10]}"
    if f == "yt_comments": return f"likes={r['likes'] or 'unknown'}"
    if f == "tt_comments": return f"likes={r['likes'] or 'unknown'} {r['date'][:10]}"
    if f == "yt_titles": return f"views={r['views'] or 'unknown'}"
    if f == "yt_chat": return "chat"
    return ""
def describe(full_ids):
    rows = IDX[IDX.evidence_id.isin(full_ids)].drop_duplicates("evidence_id")
    files = sorted(set(rows.file)); parents = set(parent_key(r) for _, r in rows.iterrows())
    unread = [i for i in full_ids if i not in READ]
    return rows, files, len(parents), unread
C = []  # claims
def claim(cid, fh, statement, ids, provenance, calc, counter_ids, limitation, roles=""):
    C.append(dict(cid=cid, fh=fh, statement=statement, ids=ids, provenance=provenance, calc=calc, counter=counter_ids, limitation=limitation, roles=roles))

# ---------------- Cross-cutting ----------------
claim("XC-F1", "F",
 "eBay Live appears in source text as promotion and seller announcements far more than as buyer experience. Of the 22 TikTok captions naming eBay Live (all in the direct pull; 0 in the community pull), 13 carry a paid-partnership tag (#ad, AD, #ebaypartner, #Anzeige) and of the other 9, eight are sellers or hosts announcing their own eBay Live shows or a pricing-tool ad and one is a hashtag-only mention (#ebaylivestream) with no announcement. The 13 tagged captions come from 12 creators (one creator posted two). The three highest-view eBay Live captions (9.8M, 7.3M, 1.2M views) are all tagged. Across all eight files 51 rows name eBay Live in source text, and every one of the 51 was read. Four first-person eBay Live buyer accounts exist (a coin/silver stream, a sealed-box switch, a sports-card queue, a Vookum watch buyer); all report friction and none is an unpaid positive buyer account. This describes these keyword-selected pulls, not eBay Live's buyers.",
 ["local_c67838ae", "local_88af59ae", "local_e9c4f012", "local_da33bf27", "local_8c6ebc99", "local_30074f15", "local_0f95bced", "local_e7440057", "local_c782f692", "local_627a60aa", "local_08c305fe", "local_0a5a262f", "local_57f2669b",
  "local_f7626202", "local_63c645f2", "local_e1a367bc", "local_51ab5800", "local_447635e8", "local_ef973161", "local_8ab883e5", "local_ae88b484", "local_dc672028",
  "t3_1vub4yy", "t3_1pttt05", "t1_nvjpmsu", "UgzrDtVVH-e2hHYihvR4AaABAg", "UgzfGt8L5RoXYTzy7Ul4AaABAg"],
 "source caption (22 captions, promo tag read from the caption text); Reddit post/comment text; YouTube comment text",
 "22 captions naming 'eBay Live' / 1,007 direct-pull videos; 0 / 914 community-pull videos; promo-tagged 13/22 by regex (#ad|ad|#ebaypartner|anzeige|#sponsored|paid partnership|#werbung) on caption text; 51 rows naming eBay Live across 8,339 unique rows (22 TikTok captions, 13 YouTube titles, 10 broad-Reddit rows, 5 YouTube comments, 1 r/Ebay row); 51/51 read. Buyer accounts: 4 rows, 4 independent parents (2 Reddit posts, 2 YouTube comments under 2 videos).",
 ["t1_p50mp5r", "P-F3SpVz-CQ", "t1_p56yrbz"],
 "Counterevidence: one explicit SELLER says a comics business 'sells a lot on eBay live streams and we do well' (t1_p50mp5r); one YouTube title 'Unboxing a preloved Chanel bag on EBay Live UK!' (61 views, creator role unknown, video unwatched) is the only creator-side positive buyer-shaped eBay Live row. Partner posts written in first person are disclosed promotion. The 'ad' token can match ordinary words; the 13 tagged captions were each read and confirmed.",
 "explicit buyers (4 accounts); explicit sellers/hosts (9 untagged captions); partner creators (13 tagged)")
claim("XC-F2", "F",
 "Authentication is the shared trust topic across communities, discussed with a community-specific shape. Cards: Authenticity Guarantee (AG) packaging and condition disputes from both buyers and sellers, alongside explicit AG defenders. Sneakers: legit-checking is the community ritual; AG is praised by explicit buyers and contested in r/Ebay threads. Watches: AG is named as the reason a buyer or seller trusted an eBay transaction. Handbags: vetting is community-run (trusted-seller lists, Purse Forum), with AG named positively by one YouTube commenter and one partner post. Coins/bullion: fraud disputes with no AG at all. Stage 3 correction to Stage 2: positive buyer-voice AG rows exist in cards, sneakers, watches and handbags; AG is not only a complaint topic.",
 ["t3_1todhm0", "t3_1r8eukv", "t3_1u2j162", "t3_1o7ekel", "UgySNeVlZQU48YJR_Dd4AaABAg", "t1_niwjhum", "t1_ovl1bk3",
  "t1_ns0iwn6", "t1_ns19b9p", "t1_odl74kz", "t1_odkd14k", "t3_1s8y9k4", "t3_1q53zhu", "Ugy-N4vfOHdqoFxnakZ4AaABAg",
  "t1_p5ij8ks", "t3_1tz0dbm", "Ugy1zfbMf-NlX2W_69p4AaABAg", "UgwAqcvWStAcfOH6nl94AaABAg",
  "t1_ofgfyui", "t1_opkfisj", "t1_p7yaxpk", "t3_1qpssd0", "local_a210513c",
  "t3_1llzc73", "t1_n03y0q8", "t1_n03l086"],
 "Reddit post/comment text; YouTube comment text; source caption (one #ebaypartner post, marked as promotion)",
 "297 rows name authentication/AG in source text (regex authenticity guarantee|ebay auth|authenticat) across 8,339 unique rows: broad Reddit 141, r/Ebay 67, YouTube comments 37, YouTube titles 26, TikTok direct 25, TikTok comments 1; 91 of the 297 read. Cited rows: 26 across 20 independent parents.",
 ["t1_njn42rr", "t1_o65m5pj", "t1_o64ua2i", "t3_1om25vd"],
 "Counterevidence rows for the positive reading: AG pass/fail inconsistency and AG-passed damaged cards (t1_njn42rr, t1_o65m5pj, t1_o64ua2i, t3_1om25vd). No error rate for AG can be computed from opinions; counts are rows naming the topic, not incidence.",
 "mixed: explicit buyers and explicit sellers; one partner creator")
claim("XC-F3", "F",
 "The frictions that eBay Live buyers describe (auctions ending in seconds, notification pressure, hype buying) are also described by explicit Whatnot buyers about Whatnot: sudden-death auctions of 3 to 5 seconds and swipe bidding jumps, unwanted notifications, and buying on hype. Live-format friction in this collection is not specific to eBay Live.",
 ["t1_owwn39k", "t1_omvn0rt", "t1_oeva9nx", "t1_oydr557", "t1_oyo6r47", "t3_1vub4yy", "t1_p50jtgt"],
 "Reddit comment and post text",
 "7 rows across 5 independent posts (r/whatnotapp 4 comments under 3 posts, r/Flipping 1, r/Ebay 1 post + 1 comment).",
 ["t1_oyfrxmd", "t1_p4zsiqf"],
 "One Whatnot buyer reports about 1,000 purchases and a better experience than eBay (t1_oyfrxmd); one r/Ebay reply says patient buyers get great deals on streams (t1_p4zsiqf). Small numbers; no rate can be inferred.",
 "explicit buyers (Whatnot and eBay Live); one r/Flipping reseller who buys from live sellers to flip")
claim("XC-F4", "F",
 "Platform mentions in source text are shaped by the search buckets, not by share of voice: Whatnot is named in 181 rows (97 in the broad Reddit pull, which has a competitor_platform_live bucket and 10 r/whatnotapp posts), TikTok Shop in 70, Vinted 49, Depop 42, Poshmark 41, GOAT 36, StockX 26, Mercari 24, Discord 21, Facebook Marketplace 15, TCGplayer 11, Chrono24 3, Purse Forum 1, Fanatics 2 (Fanatics Live 0). These counts locate rows; they are not market shares.",
 [], "source text substring counts (all files, dedup applied)",
 "Regex substring counts over 8,339 unique rows (system/error chat rows excluded); see stage3_recounts.json 'platforms'.",
 [], "A row naming a platform may praise, attack or merely mention it. Reddit rows dominate because r/whatnotapp and r/TikTokshop were sampled as subreddits.", "n/a")
claim("XC-F5", "F",
 "Market statements are rare and unbalanced: 72 rows carry UK terms (eBay UK, ebay.co.uk, London, £), 57 carry Australian terms (@ebayau, ebay.com.au, AEST, Aussie), 18 carry German terms (#Anzeige, @eBay Deutschland, modellbahn, Germany), and 40 name Japanese eBay or 'from Japan' (25 in the direct TikTok pull). Nothing about market size follows from these counts.",
 ["local_061e0f6f", "local_e1b518bb", "local_39bd7ce1", "local_4e90086b", "local_e9c4f012", "local_db4809ac", "local_4defa3ab", "local_f59398a7", "t1_omyw8vx"],
 "source caption; Reddit comment text",
 "Regex counts over 8,339 unique rows; see stage3_recounts.json 'markets'. UK 72 (TikTok direct 31, broad Reddit 18, YouTube comments 9, TikTok community 8, r/Ebay 3, YouTube titles 3); AU 57; DE 18; Japan-eBay 40.",
 [], "Term matches are not geolocation: '£' and 'London' can appear in non-UK rows; DE-language captions without a German term are missed. No dataset is geographically balanced.", "n/a")

# ---------------- SC ----------------
claim("SC-F1", "F",
 "Two different eBay relationships in sports-card source text. In the community (hobby-term) TikTok pull the ritual is ripping, pulling, grading and card-show negotiation, and eBay is almost absent from captions: 1 of the 62 Sports-Cards-labelled community videos names eBay ('cards you buy can be investments... #ebay'). In the direct (eBay-term) pull and on Reddit, eBay is the comp/price reference and the transaction venue, and the loudest current topic is AG handling, packaging and seller cancellations.",
 ["local_9cc53f16", "local_496c6391", "local_41e91d56", "local_332a15b5", "t3_1todhm0", "t3_1om25vd", "t3_1u5s64o", "t3_1uvql6e", "t3_1om8vct", "t3_1o6m3c3", "t3_1qkscsr", "t3_1thre78"],
 "source caption; Reddit post text",
 "Community-pull videos labelled Sports Cards (AI-coded): 62; of these 1 names eBay in caption/hashtags (source). Direct-pull captions naming eBay: 684/1,007 (pull selected on eBay terms). Reddit sports-card posts read: 25 of 39 labelled posts (broad 18 + r/Ebay 4 after dedup, plus keyword hits).",
 ["t1_niwjhum", "t1_ovl1bk3", "t3_1r1a00m"],
 "The direct pull is selected on eBay terms, so eBay presence there is by construction. Positive AG rows exist (t1_niwjhum appeal approved; t1_ovl1bk3 explains the AG process). Reddit threads were sampled to about 30 comments each.",
 "creators (captions, role inferred from content); Reddit posters explicit buyers or sellers in the cited disputes")
claim("SC-F2", "F",
 "Break promotion routes to TikTok Shop and to eBay listings, from different actors. Seven TikTok captions read 'Find your daily breaks located in our TikTok Shop', all from one creator (burtonbreaks; 7 of 1,921 captions, 1 creator; 4 of the 7 read, the count is by code). On YouTube, channel-run 'eBay break' streams (10 of the 20 sports_cards_breaks titles, from 4 channels: Bomber Sports Cards 5, Roper's Rips 3, Best Card Breaks 1, SD Breaks 1) have 26 to 1,317 views, while entertainment rip and mystery-box videos in the same lane (from 2 channels, TRIKE Sports Cards and Wayne Collection, 3 titles each) have 19,754 to 542,529 views. Stage 3 corrections: 'breakers' (plural) becomes one creator; the eBay-break view range is 26 to 1,317, not 26 to 606.",
 ["local_a45d15cb", "local_ddb3b62a", "local_475e17cc", "local_345a885e",
  "_rDm8b0LVNQ", "iPU9AoWlaBw", "LPZ7wtjacn4", "EfYNvpJtWmQ", "bElKFZcvfg0", "zlDlWR6W7h0", "sWYyT7Ex69o", "Srwgb5wXrZw", "bPXCFwpSq8c", "tSw3RM7K1xM",
  "Zjj_1OX-Gbs", "FaILPcpLD1s", "SzVWf_A4BUo", "MtNpAZWnn6I", "xeMKnCDtNhM", "QyAXNatU8Mo"],
 "source caption; title context (YouTube titles and view counts are platform metrics)",
 "Captions with 'break(s)' and 'TikTok Shop': 7/1,921 (1 creator); with 'break(s)' and 'Whatnot': 2; with 'break(s)' and 'eBay': 1. sports_cards_breaks lane: 20 titles, 14 name eBay; channel-run eBay break streams 10 titles, views 26 to 1,317; other 10 titles 1,031 to 542,529 views.",
 ["local_d1533050", "t1_p50mp5r"],
 "Views are attention, not buyers. Whether break buyers watch on YouTube or on eBay is not stated in chat. A #whatnotpartner haul caption (local_d1533050) shows Whatnot promotion by a creator too.",
 "creators/sellers (promotion); no buyer voice in this claim")
claim("SC-F3", "F",
 "The only first-person eBay Live sports-card buyer account in the collection describes friction (a pre-loaded listing that could not be bought outside the show, a queue of 50 to 100 items, 15-second auctions, 'not a great experience as a buyer') and a completed purchase with a host who 'was really nice'.",
 ["UgzrDtVVH-e2hHYihvR4AaABAg"], "YouTube comment text",
 "1 comment under 1 video; all 51 rows naming eBay Live were read and no second sports-card buyer account was found.",
 [], "One person's account; the stream, date and seller are not named.", "explicit buyer")
claim("SC-F4", "F",
 "Whatnot buyer voice is explicit and mixed (avoid breaks and impulse buys, 'use the app muted', 'paying double market value to have a pack ripped', counterfeit worries, sudden-death auction and notification complaints) versus 'bought probably 1000 items... better experience than eBay'. Whatnot seller voice reports low viewership ('lucky to have 6 viewers') and low hammer prices, and prefers eBay for singles that sell passively.",
 ["t1_oydr557", "t1_oyo6r47", "t1_oz5yrln", "t1_oyfrxmd", "t1_p1ynv3d", "t1_omvn0rt", "t1_owwn39k", "t1_p7hz8rr", "t1_p7hxipn", "t1_p7nasw9", "t1_no39bxl"],
 "Reddit comment text",
 "11 comments under 6 posts (r/whatnotapp 5 posts, r/Flipping 1). r/whatnotapp has 10 posts and 194 comments in the broad pull (post count from subreddit field).",
 ["t1_nn69yj9"], "One seller says no pre-existing following is needed to do well on Whatnot (t1_nn69yj9). Sampled comments per thread are capped; opposing views may be unsampled.",
 "explicit buyers (t1_oydr557, t1_oyo6r47, t1_oz5yrln, t1_oyfrxmd, t1_p1ynv3d, t1_omvn0rt, t1_owwn39k); explicit sellers (t1_p7hz8rr, t1_p7hxipn, t1_p7nasw9, t1_no39bxl)")
claim("SC-F5", "F",
 "UK Panini sticker, Premier League and match-worn memorabilia sub-communities are not represented in this collection's source text: 'Panini' appears in 12 rows (6 community TikTok captions, 4 YouTube titles, 1 direct caption, 1 YouTube comment), all about US Panini America cards, repacks or breaks except one direct caption about fake World Cup boxes bought on eBay; 'Premier League' appears in 0 rows; 'match-worn' or 'game-worn' in 0 rows; 'memorabilia' in 1 row. This is a coverage fact about the pulls.",
 ["local_0f3f1249", "local_a45d15cb"], "source caption",
 "Regex counts over 8,339 unique rows: panini 12, premier league 0, match.?worn|game.?worn 0, memorabilia 1.",
 [], "Absence in these pulls says nothing about the UK community; the pulls were not designed around Panini stickers.", "n/a")
claim("SC-H1", "H",
 "An on-camera 'AG handling and packaging' segment (seller-hosted live on the seller's handle, clipped to @eBayLive) would address the loudest Reddit sports-card complaint; it could also amplify it. Supporting outcome: fewer AG-packaging complaints under the clip than under a matched non-live AG post; rejecting outcome: the same complaint volume.",
 ["t3_1todhm0", "local_a42343e4", "local_edf5696e", "t1_niwjhum"], "Reddit post text; source caption",
 "Hypothesis; rests on SC-F1 and XC-F2 rows.", ["t1_ovl1bk3"], "No buyer asks for such a segment in any read row. AG process explanations already exist as comments and captions.", "n/a")
claim("SC-H2", "H",
 "A live comp-check segment ('what did this actually sell for') is plausible because creators in the direct pull teach eBay as the comp source; no read buyer row asks for it. Test on a creator's own handle, measured by comp-related questions in chat versus a baseline stream.",
 ["local_496c6391", "local_41e91d56", "t3_1vub4yy"], "source caption; Reddit post text",
 "Hypothesis; 2 creator captions plus 1 buyer account that comp-checked against eBay solds during a live stream.", [], "Comp-check behaviour is stated by creators and the internal team, not requested by buyers in read rows.", "n/a")

# ---------------- PK ----------------
claim("PK-F1", "F",
 "Pokémon attention in the community pull is opening, hit-rate and grading content around the 30th Celebration wave (September 2026), plus retail hunting and scalper resentment. eBay is absent from those captions: 0 of the 87 TCG-labelled community videos name eBay. Buying talk there is retail restocks and drops.",
 ["local_14590272", "local_4b8b0af8", "local_2a99087e", "local_cbfaedb7", "local_de2688c1", "local_d780fa1b", "local_4e77c895"],
 "source caption", "TCG/Pokemon-labelled community videos (AI-coded): 87; naming eBay in caption: 0. Cited: 7 videos read from 44 captions read in the section.",
 ["local_4e90086b", "local_0bfd1c9e", "local_53082fbb"], "Direct-pull Pokémon captions do name eBay as a singles buying and selling venue; the split is by pull design (hobby terms vs eBay terms).", "creators (role inferred)")
claim("PK-F2", "F",
 "On Reddit eBay is a dispute venue for Pokémon: INAD and fake-claim abuse against sellers, seller scams against buyers, and AG condition disputes on both sides. AG also has explicit defenders (a fake Magikarp caught; creases found that the listing hid; the money-back guarantee still applies) and a stated UK wish for AG on cards.",
 ["t3_1pbo9ic", "t3_1qd1fa4", "t3_1u15aox", "t3_1r8eukv", "t3_1u2j162", "t3_1r3ngpa", "t3_1qvaf6c", "t3_1o7ekel", "t1_njn3ck9", "UgySNeVlZQU48YJR_Dd4AaABAg", "t1_o64ybsb", "t1_o64htk9", "t1_o64o8wg"],
 "Reddit post and comment text; YouTube comment text",
 "13 rows across 10 independent parents (9 Reddit posts, 1 YouTube video). Pokémon Reddit posts read: 28 of 37 TCG-labelled posts (broad 22 + r/Ebay 15 after dedup).",
 ["t1_o9yqku1"], "One r/IsMyPokemonCardFake commenter says fake-claim abuse happens far more with Pokémon than with MTG, Lorcana or One Piece (one seller's claim). Reddit is dispute-selected by bucket (trust_scams_authenticity).", "explicit buyers and sellers per row; t1_njn3ck9 UK stated")
claim("PK-F3", "F",
 "Audience price-checking is visible in Pokémon TikTok comments (TCGplayer cited; creator prices challenged) and in replay chat ('whats the price on that one?'). No read Pokémon audience row names eBay as the comp source; creators in the direct pull do.",
 ["tiktok_comment:7686279334882460446", "tiktok_comment:7686267440066134814", "19bmF518whA:1393"], "TikTok comment text; chat message",
 "TCGplayer named in 11 rows collection-wide (TikTok direct 4, community 2, broad Reddit 2, YouTube comments 2, TikTok comments 1). Comment group under the 30th ETB opening: 10 comments read.",
 [], "The TikTok comment IDs for the ETB price challenges are in reviewed_evidence.csv under PK; comment groups are 10 top comments per video, a selection.", "audience (role unknown)")
claim("PK-F4", "F",
 "eBay Live's Pokémon presence on TikTok is disclosed partner content (the 7.3M-view 'Pokémon card shopping on a budget with the help of eBay Live' is tagged) and seller show announcements (30th anniversary launch streams, 'Ruben is on eBay Live with an ETB for a penny'), plus a partner-promoted Pokémon 30th weekend game show. No unpaid caption in either pull describes an eBay Live Pokémon purchase.",
 ["local_88af59ae", "local_da33bf27", "local_8ab883e5", "local_51ab5800", "local_e1a367bc"], "source caption",
 "5 of the 22 eBay Live captions concern Pokémon; 2 tagged, 3 untagged seller announcements.", [], "As XC-F1.", "partner creators; sellers/hosts")
claim("PK-F5", "F",
 "Other TCGs are barely present in source text: One Piece 4 rows, Lorcana 1, Magic 8, Yu-Gi-Oh 4 (one is a Yu-Gi-Oh Nike sneaker thread), Riftbound 0. No sub-community section can be built from them. Fanatics is named in 2 rows and 'Fanatics Live' in 0.",
 ["t1_o9yqku1", "t1_oqnhajy", "t1_oony44l", "t3_1pcpv9c", "UgxYEXDXDWSVi1wR2Jh4AaABAg"], "Reddit comment and post text; YouTube comment text",
 "Regex counts over 8,339 unique rows (stage3_recounts.json 'other_tcg').", [], "Absence in the pulls, not in the world; the pulls were Pokémon-weighted by design.", "n/a")
claim("PK-H1", "H",
 "'Open it or keep it sealed' and hit-rate scepticism are live-format-ready (audience vote, sealed-versus-ripped price comparison), but prerecorded series already own that format. Test: one seller-run live 'sealed vs ripped' session on the seller's handle versus the same seller's prerecorded version, measured by price/condition questions in chat and listing click-through.",
 ["local_14590272", "local_4b8b0af8"], "source caption", "Hypothesis.", [], "No read audience row asks for a live version.", "n/a")
claim("PK-H2", "H", "A UK 'AG for cards' message could land; the evidence is one UK-stated comment.", ["t1_njn3ck9"], "Reddit comment text", "1 comment.", [], "One person.", "explicit UK buyer")

# ---------------- SN ----------------
claim("SN-F1", "F",
 "In the read rows eBay appears in sneaker content as seller promotion and reseller how-to, as disclosed #ad partner posts built on AG (UK and AU creators), and as buyer fake-complaint or AG-confusion threads; it does not appear in community-pull style and rotation captions (0 of 88 Sneakers-labelled community videos name eBay). Stage 3 adds unpaid explicit buyers who prefer eBay for sneakers because of listing photos and AG (r/Sneakers, AU-stated) and a high-volume buyer who reports AG hub shipping delays of up to 30 days.",
 ["local_13d7da97", "local_53a90dd5", "local_7551ae4b", "local_39bd7ce1", "local_e1b518bb", "local_bf98b74d", "local_3663ef62", "t3_1nzw8nl", "t1_niwc5vg", "t3_1s8y9k4", "t3_1q53zhu", "t1_ns0iwn6", "t1_ns19b9p", "Ugy-N4vfOHdqoFxnakZ4AaABAg"],
 "source caption; Reddit post and comment text; YouTube comment text",
 "Sneakers-labelled community videos (AI-coded): 88; naming eBay in caption: 0. Cited: 14 rows across 12 independent parents.",
 ["local_9834883a", "local_70b7ebe2"], "Community-pull style captions were read (12) and none names eBay; the 'Current Sneaker Rotation' caption cited in Stage 2 notes as local_98348833… is a transcription typo for local_9834883a…; the row exists and is registered. t1_ns0iwn6 is the same person as the r/Sneakers poster t3_1pcpv9c (one AU buyer, not two).", "sellers (explicit), partner creators, explicit buyers (t1_ns0iwn6, t1_ns19b9p, Ugy-N4vf…)")
claim("SN-F2", "F",
 "Legit-checking is the community's own ritual (real-vs-fake YouTube series; replica jokes in TikTok comments; a UK first-time buyer 'afraid that I received the rep'); authentication trust is contested platform by platform (StockX fake stories versus loyalty; eBay AG 'broken things passed' versus 'eBay has your back').",
 ["UgxbPBFfSv3Tyf-ofop4AaABAg", "t1_odl74kz", "t1_odkd14k"], "YouTube comment text; Reddit comment text",
 "TikTok comment group IDs are in reviewed_evidence.csv under SN (2 groups, 20 comments, 2026-dated).", ["t1_ns19b9p"], "The full YouTube comment IDs for the StockX rows are in the register; role of YouTube commenters is unknown unless stated.", "mixed")
claim("SN-F3", "F", "UK and AU market statements exist in sneaker rows; no DE-stated sneaker row was found (absence in this pull).", ["local_7551ae4b", "local_e1b518bb", "local_39bd7ce1", "t1_ns0iwn6"], "source caption; Reddit comment text", "4 rows; DE-term rows collection-wide 18, none labelled Sneakers.", [], "Term matching, not geolocation.", "n/a")
claim("SN-H1", "H", "An on-camera legit-check/AG walkthrough series (creator plus authenticator) matches the ritual; the risk is that the audience reads it as more #ad. Test on a legit-check creator's own handle versus @eBay, measured by replica-doubt comments and listing clicks.", ["local_39bd7ce1", "t1_ns19b9p"], "source caption; Reddit comment text", "Hypothesis.", [], "Client tension to report, not resolve: the sprint Q&A lists sneakers as a Live right-to-win category; the call said sneakers are probably not a big Live focus.", "n/a")
claim("SN-H2", "H", "Streetwear outfit audiences (budget rotations, link-seeking, price scepticism) are a different behaviour from sneaker collecting and legit-checking; live selling maps to the latter.", ["local_70b7ebe2"], "source caption", "Hypothesis.", [], "Comment IDs for the wardrobe video are in the register under SN.", "n/a")

# ---------------- LX ----------------
claim("LX-HB-F1", "F", "Handbag buyers and stylists in the direct pull present eBay as the vintage and preloved find venue and share vetting know-how (trusted-seller lists; a Japanese-eBay how-to sub-genre echoed on YouTube and r/handbags). Community-pull bag captions do not name eBay except one collection caption tagged #ebay #mercari (1 of 61 Luxury-labelled community videos).",
 ["local_e355b2cc", "local_0bd4eacd", "local_d6e870d2", "local_71ce9e5c", "local_d0324d97", "local_f59398a7", "local_cdcaeca8", "-TgKIoItPPM", "8ATRm1Bp1sU", "t1_ofgfyui", "local_5afb86bf"],
 "source caption; title context; Reddit comment text", "Luxury-labelled community videos (AI-coded): 61; naming eBay: 1. Japanese eBay named in 40 rows collection-wide (25 direct captions).", [], "Direct-pull presence is by pull construction.", "buyers/stylists (role inferred from caption)")
claim("LX-HB-F2", "F", "Handbag authentication is community-run (Purse Forum, research, trusted-seller lists); AG is rarely named in handbag Reddit rows, and where AG is argued on r/Ebay it is as seller protection, contested both ways. Stage 3 correction: one YouTube commenter (watches_auth lane) says 'Ebay authentication is great' after buying two LV purses, and an r/Ebay seller reports eBay's authenticator determining a Whatnot-bought LV wallet counterfeit a year after resale.",
 ["t1_ofgfyui", "t3_1sbzdvx", "t3_1shwwz7", "t1_opkfisj", "t1_p7yaxpk", "UgwAqcvWStAcfOH6nl94AaABAg", "t3_1qpssd0", "t1_p8kecsh", "local_a210513c", "local_3e70873d"],
 "Reddit comment and post text; YouTube comment text; source caption (one #ebaypartner post and one consignment seller promo, both promotion)", "10 rows across 9 parents.", ["UgwAqcvWStAcfOH6nl94AaABAg"], "The positive AG buyer row sits under a watches video, not a handbag video. Purse Forum is named in 1 row collection-wide.", "explicit buyers (t3_1sbzdvx, t3_1shwwz7, Ugw…); explicit sellers (t1_opkfisj, t1_p7yaxpk, t3_1qpssd0); promotion (2 captions)")
claim("LX-HB-F3", "F", "Seller reluctance to list luxury on eBay (chargebacks, INAD) is a loud, high-score r/Ebay theme ('Never sell luxury items on eBay', score 285).", ["t3_1oe3rv0", "t1_nkykxsw", "t1_nlai4ln"], "Reddit post and comment text", "3 rows, 1 post.", ["t1_nkynsy1", "t1_p5gv32z"], "Same thread: 'Pokemon cards... all go to an Authenticator first which gives me peace of mind'; r/Watches: 'sold many watches on eBay and never had an issue'.", "explicit sellers")
claim("LX-HB-H1", "H", "'How I vet a listing / my trusted sellers' as a live format with an authenticator or preloved seller; a Japanese-seller preloved segment is a concrete, already-viewed content type. Route: seller's own handle first; @eBay clip. Outcome: trusted-seller questions answered in chat; listing saves.", ["local_71ce9e5c", "local_f59398a7"], "source caption", "Hypothesis.", [], "Prerecorded how-tos already serve this.", "n/a")
claim("LX-HB-H2", "H", "Preloved-luxury live auctions are promoted on TikTok ('Mega live alert... #auction #chanel', host platform not stated) and one YouTube title unboxes a Chanel bag bought on eBay Live UK; a seller-run eBay Live handbag auction is testable. Entry-price items (charms, small leather goods) are untested in these rows.", ["local_0ada9f21", "P-F3SpVz-CQ", "local_cec361e6"], "source caption; title context", "Hypothesis; 3 rows.", [], "Host platform of the TikTok 'mega live' unknown; the YouTube video is unwatched (61 views).", "n/a")
claim("LX-W-F1", "F", "Watch community voice lives on Reddit (r/Watches, r/rolex) as expertise and risk management: seller-protection doubts and 'never sell watches on eBay' sentiment alongside AG named as the reason a buyer or seller trusted an eBay transaction. Stage 3 adds two YouTube commenters who buy watches on eBay (one regularly from Japan) and trust AG, and one r/Watches seller with no issues across many sales. TikTok watch rows are few (unboxing, repair).",
 ["t3_1vweez9", "t1_p5gahje", "t1_p5gb6s4", "t1_p5gbcao", "t1_p5ij8ks", "t3_1tz0dbm", "t1_oq7fajb", "t3_1oqfzzy", "t3_1p7d9qr", "t1_nqybkth", "Ugy1zfbMf-NlX2W_69p4AaABAg", "UgwAqcvWStAcfOH6nl94AaABAg", "t1_p5gv32z", "local_ac2e94cb", "local_d21a49d8"],
 "Reddit post and comment text; YouTube comment text; source caption", "15 rows across 10 parents. Watch keyword rows collection-wide (reproducible pattern in stage3_recounts.py): 178 (broad Reddit 85, YouTube comments 41, TikTok community 15, r/Ebay 14, TikTok direct 11, YouTube titles 8, TikTok comments 2, chat 2); Stage 1's 183 used a different, unrecorded pattern.", ["UgzfGt8L5RoXYTzy7Ul4AaABAg"], "One YouTube commenter alleges unhonoured trade-in promises after spending $17K with seller Vookum on eBay Live (one person's unverified claim about a client-named seller). t1_p5gb6s4 and t1_p5gbcao are one commenter; the watch-repair caption is hashtags only (#watchhospital), so 'repair' is inferred from the handle.", "explicit buyers and sellers per row")
claim("LX-W-H1", "H", "An authenticator-led live segment ('what AG checks on a watch') fits the expertise ritual; TikTok reach for watches is unproven here. Route: @eBayLive with a named authenticator or a seller like Vookum; outcome: AG-process questions and AG-listing saves.", ["t1_p5ij8ks", "Ugy1zfbMf-NlX2W_69p4AaABAg", "hWJ0uGyO1Pk"], "Reddit comment text; YouTube comment text; title context", "Hypothesis.", ["UgzfGt8L5RoXYTzy7Ul4AaABAg"], "As LX-W-F1 caveat.", "n/a")
claim("LX-VD-F1", "F", "Vintage designer clothing content is buyer-side finds and label education ('Most vintage designer clothing isn't even designer. Understand licensing'); eBay UK is named by a UK creator. Fragrance is thin: 14 rows name fragrance, perfume or cologne (7 are YouTube comments under one watches_auth-lane video), and fake risk is the only theme.",
 ["local_d886ed8f", "local_061e0f6f", "local_43581f51", "local_714e362b", "local_43dc3f74", "urGSyXd0wCo"], "source caption; title context", "Fragrance regex rows: 14 (YouTube comments 7, TikTok direct 3, broad Reddit 2, r/Ebay 1, YouTube titles 1). Stage 2 said 7 rows; the reproducible count is 14.", [], "Overlaps the thrift cluster (AB-TV).", "creators (inferred)")

# ---------------- EL ----------------
claim("EL-F1", "F", "Electronics splits into four strands: camera and digicam collecting where eBay is the named sourcing venue and Japanese sellers a recurring topic; retro-tech nostalgia (iPods, consoles, hi-fi) where eBay is absent from read community captions (1 of 188 Electronics-labelled community videos names eBay: a Nikon Coolpix sourced for nail photos) and clone consoles sell via TikTok Shop; mainstream electronics where eBay content is scam-anxiety and repair storytelling (a roach-infested Xbox on r/Ebay, 2026-09-24); and reseller sourcing and what-sold content. Stage 3 adds two unpaid buyer-joy captions (a refurbished Wii from eBay, 45.4k views; 'Girls don't walk, run on eBay' for a digicam).",
 ["local_71c0aed9", "local_ced29739", "local_c31e3095", "local_b905f0ac", "local_03bf9280", "local_27a9e453", "local_58c394ee", "local_ffb78543", "local_af01bbb0", "local_d1016b2a", "local_6ef354d1", "local_ce987d6e", "t3_1wphbkz", "local_dfb628f8", "local_2346635f", "t3_1r91qdw", "t3_1ojc3n1", "t1_nm1ytgc"],
 "source caption; Reddit post and comment text", "Electronics-labelled community videos (AI-coded): 188; naming eBay: 1. Cited 18 rows across 17 parents.", ["local_372655cc"], "Retro console 'gamestick' captions are seller/affiliate promotion (TikTok Shop); the 2024 comment group is historical.", "buyers (inferred from caption), resellers (explicit), r/Ebay buyer (explicit)")
claim("EL-F2", "F", "The 'what sold on eBay today' reseller format reaches large TikTok audiences (1.5M views on one read row) and is category-agnostic; it is seller education, not buyer demand. Both read rows are one creator (finestflips).", ["local_03bf9280", "local_1af7f3b9"], "source caption", "2 captions; views are platform metrics.", [], "Two rows; the format's reach is not measured across the pull.", "resellers (explicit)")
claim("EL-H1", "H", "A live 'does it work' test segment (power-on, shutter count, lens fungus) matches condition anxiety in camera and console rows; prerecorded repair and unboxing already serve it. Test on a camera seller's handle; outcome: condition questions answered live and the return rate on live-sold cameras versus listings (business data needed).", ["local_c31e3095", "local_6ef354d1", "t3_1wphbkz", "local_3cc532cf"], "source caption; Reddit post text", "Hypothesis.", [], "The model-train caption local_3cc532cf… shows the same 'sold untested, tested on camera' ritual in another hobby.", "n/a")
claim("EL-H2", "H", "Retro-tech nostalgia attention is large but its buying route in read rows is TikTok Shop and unspecified links; no read row asks for live.", ["local_ffb78543", "local_af01bbb0", "local_27a9e453"], "source caption", "Hypothesis.", ["local_dfb628f8"], "One nostalgia caption does name eBay (refurbished Wii).", "n/a")

# ---------------- TY ----------------
claim("TY-F1", "F", "The toys label covers at least five hobbies with different venues: blind box and designer toys (Pop Mart retail hunts; no eBay in read captions, and the one blind-box caption naming eBay treats it as too expensive and buys via Mercari/JPfans); anime and action figures (eBay as comp and purchase venue, with packaging and scam disputes on r/Ebay); model trains (layouts, shows, hobby shops); vintage lines (eBay as first purchase and lot-buying venue; heavy reseller sourcing); plush (rarity unboxing; thrift-to-eBay resale). Stage 3 correction: model trains do name eBay in 2 community captions from 2 creators (idktrains: a first N-scale locomotive imported via eBay; robertscreations: an Aristocraft unit bought 'sold untested' and tested on camera); idktrains also posts the KATO layout and a 'check this out on my shop' caption, so 3 of the 4 train captions cited are one creator. 1 of 137 Toys-labelled community videos names eBay (vintage pins from eBay).",
 ["local_d18974a6", "local_a379d291", "local_0e1abd6b", "local_631e6ad9", "local_3ca5b7c3", "local_bf4de5e6", "local_4472cc81", "local_cfb33c9b", "local_9aa09393", "local_e46e35fa", "t3_1skd4mg", "t3_1txny14", "t1_opzx1zy", "t1_odxel8c", "local_352f0ba9", "local_4defa3ab", "local_e3650793", "local_45817e9a", "local_99a07423", "local_3cc532cf", "local_13a61846", "local_667ec305", "local_1244835c", "local_7d25e976", "local_17dd2552", "local_1af7f3b9", "local_3135e0e8", "local_24b4ad5a", "local_11c6d089"],
 "source caption; Reddit post and comment text", "Toys-labelled community videos (AI-coded): 137; naming eBay: 1. Train keyword rows: 36 (35 community captions), of which 2 name eBay. Blind-box keyword rows: 69, of which 1 names eBay. Cited 29 rows across 27 parents.", ["local_99a07423", "local_3cc532cf", "local_4472cc81"], "Stage 2's 'blind box and trains never name eBay in read rows' is withdrawn; the counter rows are listed. Roles are inferred from captions.", "collectors/buyers (inferred); resellers (explicit); r/Ebay posters explicit")
claim("TY-F2", "F", "Audience purchase intent shows up in comments as 'ILL TAKE THEM' / 'are you selling these anywhere' under a collection display (My Little Pony, 1.4M views; comments 2026) and as price-and-link demands under product videos; it names no platform.", ["local_6db83504", "tiktok_comment:7641731808408814367"], "TikTok comment text (comment IDs in reviewed_evidence.csv under TY)", "1 parent video, 10 comments read (top comments, a selection).", [], "Comment likes are attention; no purchase is observed.", "audience (role unknown)")
claim("TY-F3", "F", "The Whatnot account's Labubu explainer reached 12.1M views but its top comments reject the hobby ('Grown adults btw'; 'I honestly dont see the hype'): reach is not community.", ["local_7f7b4dda"], "source caption; TikTok comment text (comment IDs in the register under TY; comments 2025)", "1 video, 10 comments read.", [], "Top-comment selection; the video's actual audience is unknown.", "audience (role unknown)")
claim("TY-H1", "H", "'The collection goes up for sale live' (collector's own handle, routed to eBay Live) mirrors the MLP comment reaction; unproven that commenters follow to a marketplace. Outcome: share of chat offers to buy that convert to bids (business data).", ["local_6db83504", "tiktok_comment:7641731808408814367"], "TikTok comment text", "Hypothesis.", [], "One video's comments.", "n/a")
claim("TY-H2", "H", "Model trains: real US community content (shows, HO/O gauge layouts, a #modellbahn tag) with eBay named as a buying venue in 2 captions from 2 creators (one of whom also runs a shop); no live link in read rows. A discovery question (are train buyers on eBay, and what do they check before buying?), not yet a Live format.", ["local_99a07423", "local_3cc532cf", "local_13a61846", "local_4defa3ab"], "source caption", "Hypothesis; trains keyword rows 36.", [], "Stage 2 version said 'no eBay link'; corrected.", "n/a")

# ---------------- CN ----------------
claim("CN-F1", "F", "Numismatic collecting is nearly absent from this collection's source text: the coin pattern (coin, numismatic, bullion, silver eagle, morgan dollar, gold coin, PCGS, NGC, challenge coin) matches 18 rows (broad Reddit 9, r/Ebay 7, community TikTok 2; 0 in the direct TikTok pull, TikTok comments, YouTube titles, YouTube comments or chat), 16 of them read; the 2 TikTok captions are challenge-coin/patch collectors. The Flash Coins label routes 1 TikTok video, 4 Reddit posts and 43 Reddit comments (AI-coded), mostly bullion-fraud disputes (fake gold bars; 'never buy gold from eBay'; a 3-day coin/bullion return window noted around April 2026). Stage 3 adds one explicit numismatic buyer comment (a cleaned coin sold as XF, discovered after NGC grading, negative review removed) and one Whatnot coin seller wanting spot-price repricing.",
 ["local_6bcfb3ca", "t3_1llzc73", "t1_n03y0q8", "t1_n03l086", "t1_n03q3iy", "t3_1ufxb7r", "t1_otwj817", "t3_1qcvle6", "t1_n04bfny", "t1_oygq7h6", "t1_p515n9w"],
 "source caption; Reddit post and comment text", "Coin pattern: 18/8,339 rows; read 16/18. Flash Coins label: 1 video, 4 posts, 43 comments (AI-coded). Stage 1's 39-row pool used an unrecorded broader pattern and is superseded.", [], "The client's 'green shoot' for coins on Live cannot be assessed from community evidence here. Absence in these pulls is not absence of the community. The second challenge-coin caption (tiktok_video:local_218e99dbcc43d15140a9ed1eac16ad3f338c9e05dafe54984ede22b36f859df5) was cited in Stage 2 notes but is not in the reading register; it is counted by code, not cited as read.", "explicit buyers (t3_1llzc73, t1_n04bfny); explicit sellers (t3_1qcvle6, t1_oygq7h6)")
claim("CN-F2", "F", "The collection's clearest first-person eBay Live buyer narrative is from a silver-coin dealer's stream and is negative: host 'market' quotes judged 150 to 200 percent above recent eBay solds, 10-second flash auctions, 'shopping through the original ebay interface is far cheaper' (r/Ebay, 2026-08-21, score 75), with a reply that this is how most streams work and patient buyers can get deals.",
 ["t3_1vub4yy", "t1_p4zsiqf", "t1_p50jtgt", "t1_p56jodo"], "Reddit post and comment text", "1 post + 3 comments (thread of 1 independent parent).", ["t1_p4zsiqf", "t1_p50mp5r"], "One non-collector buyer's account; the seller is not named; the reply comes from an unstated role.", "explicit buyer (self-described non-collector)")
claim("CN-H1", "H", "Coin and bullion live buyers who comp-check against eBay solds distrust hosts who quote above solds; showing the sold-comp on screen would answer the complaint directly. Test on @eBayLive with a coin dealer; outcome: comp-related complaints in chat and post-stream Reddit fall; risk: lower hammer prices (business trade-off).", ["t3_1vub4yy", "t1_oygq7h6"], "Reddit post and comment text", "Hypothesis.", [], "Rests on one buyer account.", "n/a")

# ---------------- AB ----------------
claim("AB-TV-F1", "F", "The largest 'Other' cluster in the direct pull is vintage and secondhand clothing where eBay is named as a buying venue by buyers ('eBay Dress Haul #1950s'; 'my fave vintage brands to search up! #ebayhaul'; a German-language 'finds' caption with 636k views; men's style pickups) and as a resale venue by resellers (a Spanish-language vintage t-shirt reseller, 77k views, 1,704 shares). Vinted, Depop and Poshmark are named alongside eBay in seller captions (Vinted 49 rows, Depop 42, Poshmark 41 collection-wide, mostly TikTok direct).",
 ["local_cabc61bd", "local_9c4a18de", "local_0474b192", "local_db4809ac", "local_8ecc6ac8", "local_cff44bce", "local_13745f76", "local_bcddb583", "local_145097e1", "local_6fd13074", "local_9520b23f", "local_1e0184bc"],
 "source caption", "Cluster: 104 videos first-match plus most of 78 unassigned (AI-coded labels grouped by rule; stage1). 12 captions cited (12 parents).", [], "Cluster boundaries are rule-based over AI labels; the #AD how-to is promotion.", "buyers and resellers (inferred from caption; resellers often explicit)")
claim("AB-TV-H1", "H", "'Vintage brands to search on eBay' is an existing creator format that maps to a live 'search with me / finds' show; sizing is a friction live cannot fix (client call).", ["local_0474b192", "local_6fd13074"], "source caption", "Hypothesis.", [], "None.", "n/a")
claim("AB-PP-F1", "F", "Patches, pins and buttons are a real hobby cluster (124 community videos, AI-clustered) with trading, making and collecting rituals (police/military patches, battle jackets including a UK-stated one, pinback-button makers, HHN trades). Stage 3 correction: eBay is named as the sourcing venue in 2 of the 8 community captions that name eBay (a 287k-view custom patch jacket built from a $25 vintage Lee jacket and patches found on eBay; vintage pins/buttons bought on eBay); TikTok Shop and Etsy are named selling routes for makers. Challenge coins sit here, not in numismatics.",
 ["local_5cc71701", "local_6bcfb3ca", "local_dbb48dcc", "local_a203c31d", "local_0089e5d6", "local_5cdeaba6", "local_c5f13424", "local_b441c945", "local_11c6d089", "local_8a4ab98c"], "source caption", "11 captions cited (11 parents); cluster 124 videos of which 11 read.", ["local_b441c945", "local_11c6d089"], "Stage 2's 'eBay absent from read captions' is withdrawn for this cluster. The child's patch-collection caption cited in Stage 2 notes (local_218e99db…) is not in the register and is not cited here.", "collectors/makers (inferred)")
claim("AB-PM-F1", "F", "Physical-media collectors show completion and premium-edition rituals (4K steelbooks, shelf tours, 'Over 5000 movies'); eBay appears in 1 of 9 read cluster captions (and 0 of 7 control captions in this cluster); no live selling in read rows.", ["local_e4b6e736", "local_4492b026", "local_4a91348f", "local_e4e363d3", "local_8459de44"], "source caption", "Cluster 106 videos (AI-clustered); 16 read (9 routed + 7 control); 1 names eBay.", [], "Small read share of the cluster.", "collectors (inferred)")
claim("AB-PA-F1", "F", "P&A (parts and accessories) appears in the collection as an eBay-native buying and selling behaviour: engines and parts bought on eBay by builders ('I BOUGHT THE EBAY ENGINE!'; 'the ol eBay motor was RIPPING #ebaymotors'; 'best way to win an EBay auction EVERY time... Ek civic cluster', 103k views), parts sellers routing to eBay stores (classic-car parts; an Italian-language scrapyard) plus one wholesale parts caption that sits in the eBay-term pull without naming eBay, with freight, fitment and return friction on Reddit (engine refund dispute, score 219; $2,300 bumper freight). No read row mentions live selling for parts.",
 ["local_1dd1a5d8", "local_daced285", "local_fe0afbcf", "local_b80372ee", "local_a72c7e8c", "local_a4d89264", "local_21b424cb", "local_97b9ca83", "t3_1qjabr7", "t1_o0zedv8", "t1_olpp167"], "source caption; Reddit post and comment text", "Automotive cluster 88 videos (85 direct; AI-clustered); 12 captions read; Reddit P&A keyword rows 13, 8 read. Cited 11 rows across 10 parents.", [], "The direct pull selects on eBay terms, so eBay presence is by construction; the behaviour's size is unknown.", "builders/buyers (inferred), sellers (explicit)")
claim("AB-PA-H1", "H", "Live could serve P&A as 'does it fit / is it the right part' expert Q&A rather than auctions; no community row supports or opposes; a discovery-stage question for the core team.", ["t3_1qjabr7", "local_b80372ee"], "Reddit post text; source caption", "Hypothesis.", [], "No evidence either way.", "n/a")
claim("AB-SL-F1", "F", "The collection's eBay Live voice is (a) paid partner TikTok posts and seller show announcements, (b) seller-side comparisons judging eBay Live by fees, viewers and 'clientele', and (c) four explicit buyer accounts, all reporting friction (auction speed, host pricing, mid-auction item change, post-sale promises). r/Ebay's seller-heavy regulars describe Live as force-fed ('I've had enough of the force feed', score 142; 'I hate eBay live and I hate ai slop', 380; notification bombardment), a YouTube commenter echoes the notification complaint, and one commenter calls eBay Live's demand 'artificial' while promotion lasts. Stage 3 adds one explicit positive seller account (a comics business that 'sells a lot on eBay live streams and we do well').",
 ["t3_1wfp5sj", "t1_p9o48gb", "t1_p9ojy91", "t1_p7xb529", "t1_ocus8sv", "t1_p50jtgt", "t1_pa2yhrf", "t3_1s5ae92", "UgxbPcydBm_M7LfisLt4AaABAg", "t1_p56yrbz", "t1_p50mp5r", "t3_1vub4yy", "t3_1pttt05", "t1_nvjpmsu", "UgzrDtVVH-e2hHYihvR4AaABAg", "UgzfGt8L5RoXYTzy7Ul4AaABAg"],
 "Reddit post and comment text; YouTube comment text", "16 rows across 12 parents. r/Ebay posts after dedup: 130; live terms appear in 3 r/Ebay posts and 4 comments; broad-pull rows naming eBay Live: 10.", ["t1_p50mp5r", "t1_p4zsiqf"], "r/Ebay is a seller-operations subreddit by composition; buyer voice is thin there. Role per row is stated in the roles column.", "explicit or inferred sellers (t3_1wfp5sj, t1_p9o48gb, t1_p9ojy91, t1_p7xb529, t3_1s5ae92, UgxbPcy…, t1_p56yrbz, t1_p50mp5r); explicit buyers (t3_1vub4yy, t3_1pttt05, UgzrDtVVH…, UgzfGt8L5…); unknown (t1_ocus8sv, t1_p50jtgt, t1_pa2yhrf)")
claim("AB-SL-F2", "F", "Whatnot is described by its own sellers as a liquidation venue with chat drama, giveaways and low hammer prices, with eBay for 'the good stuff' and eBay Live's clientele judged 'more intelligent'; small card sellers report very low Whatnot viewership. Seller opinion, not buyer data.", ["t1_omuylg3", "t1_p7hxipn", "t1_no39bxl", "t1_nseqlli"], "Reddit comment text", "4 comments under 4 posts.", ["t1_nn69yj9", "t1_oyfrxmd"], "Counter: a seller says you can build a following on Whatnot itself; a buyer reports a better experience than eBay.", "explicit sellers")
claim("AB-SL-F3", "F", "The Nurse Flipper 'Live eBay Reseller Q&A' replay chat is sellers talking shipping claims, 'eBay versus Whatnot' inventory strategy and Whatnot vacation mode; no buyer voice. YouTube live-selling lanes are seller how-to titles, and 3 of the 248 YouTube titles come from eBay's own channels (a sellers webinar, a seller panel, an eBay Live UK promo), which are brand output inside a community file and are excluded from audience voice.",
 ["wbUy3gK7kFE:690", "wbUy3gK7kFE:708", "wbUy3gK7kFE:709", "Eq1xymBqpnk", "EtOrAojxRqI", "myCuDV9-2-M", "d3uHPsnoITc", "DjsWZaPwMQs", "y-NqOxTOXP0"], "chat message; title context", "Nurse Flipper stream: 248 messages, 66 host/mod-flagged, 20 read. eBay-channel titles: 3/248.", [], "Chat labels are low-confidence; roles inferred from content.", "sellers (inferred from questions); hosts (flagged)")
claim("AB-SL-H1", "H", "Buyer-side trust mechanics for Live (sold-comp on screen, no mid-auction item change, enforcement of on-stream promises, opt-out from notification pushes) are the concrete gaps named by buyers on eBay Live and on Whatnot; a format that visibly addresses them is testable in cards, coins and watches where these accounts sit.", ["t3_1vub4yy", "t3_1pttt05", "UgzrDtVVH-e2hHYihvR4AaABAg", "UgzfGt8L5RoXYTzy7Ul4AaABAg", "t1_owwn39k", "t1_omvn0rt"], "Reddit post and comment text; YouTube comment text", "Hypothesis over 6 buyer rows.", [], "Six people.", "explicit buyers")

# ---------------- write ----------------
rows = []
for c in C:
    full = expand(c["ids"]); counter = expand(c["counter"])
    r, files, npar, unread = describe(full)
    if unread: ERRORS.append(f"{c['cid']}: cited rows not in the register: {unread}")
    rows.append({
        "Claim ID": c["cid"], "F/H": c["fh"], "Statement": c["statement"],
        "Source file(s)": "; ".join(FILE_LABEL[f] for f in files) if files else "counts over all eight files",
        "Full evidence IDs (flash_evidence_row_id)": "; ".join(full),
        "Provenance": c["provenance"], "Calculation and denominator": c["calc"],
        "Independent parent count": npar, "Speaker roles": c["roles"],
        "Counterevidence (IDs)": "; ".join(counter) if counter else "none found",
        "Limitation": c["limitation"], "Status": "checker-pending",
        "Metrics of cited rows (platform metrics; blank = unknown)": "; ".join(f"{i.split(':',1)[1][:22]}: {metric(rr)}" for i, rr in ((x, IDX[IDX.evidence_id==x].iloc[0]) for x in full)) if full else "",
    })
if ERRORS:
    print("\n".join(ERRORS)); raise SystemExit(f"{len(ERRORS)} problems; ledger not written")
out = os.path.join(HERE, "..", "claim_ledger.csv")
with open(out, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print(f"claim_ledger.csv: {len(rows)} claims; {sum(r['F/H']=='F' for r in rows)} findings, {sum(r['F/H']=='H' for r in rows)} hypotheses; cited IDs {sum(len(r['Full evidence IDs (flash_evidence_row_id)'].split('; ')) for r in rows if r['Full evidence IDs (flash_evidence_row_id)'])}")
for r in rows: print(r["Claim ID"], "parents", r["Independent parent count"], "files", r["Source file(s)"][:60])
