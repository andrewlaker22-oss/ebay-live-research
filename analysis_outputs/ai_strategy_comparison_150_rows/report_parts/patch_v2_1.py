# Revision 2.1 patch: applies checker corrections (2026-09-27) as exact-match replacements.
# Aborts without writing if any anchor does not occur exactly once.
import os, shutil
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
p = "claude_fable_5-1_eBay_Live_community_report_2026-09-27.md"
arch = "claude_fable_5-1_eBay_Live_community_report_2026-09-27_v2_prepatch.md"
if not os.path.exists(arch):
    shutil.copyfile(p, arch)
t = open(p, encoding="utf-8").read()
E = []
def R(old, new): E.append((old, new))

# header / conventions
R('its "Comp Check Live" idea appears here as hypothesis H2, not as the recommendation.',
  'its "Comp Check Live" idea appears here as hypothesis H2, not as the recommendation. This is revision 2.1, patched on 2026-09-27 after an evidence audit; the pre-patch revision 2 is preserved as `claude_fable_5-1_eBay_Live_community_report_2026-09-27_v2_prepatch.md`.')
R('How to read citations: `TikTok Videos r12` means row 12 of the TikTok Videos tab (its full flash_evidence_row_id is in the appendix).',
  'How to read citations: `TikTok Videos r12` means data record 12 of the TikTok Videos tab, which is Excel row 13 because row 1 is the header (the full flash_evidence_row_id of every record is in the appendix).')
# lanes
R('Two lane names do not match their content and should not be used as category evidence: `watches_auth` is a fragrance video (fake Amouage), and `cameras_electronics` is a vintage Halloween store-buyout video. There are therefore zero watch rows and zero camera rows on the YouTube tab.',
  'Three lane names should not be used as category evidence: `watches_auth` is a fragrance video (fake Amouage), `cameras_electronics` is a vintage Halloween store-buyout video, and `luxury_bags_auth` is a general video about eBay\'s AI counterfeit removals whose sampled comments never identify handbags or luxury. There are therefore zero watch rows, zero camera rows and no identifiable luxury-seller rows on the YouTube tab. These are gaps in this sample, not established gaps in the full collection.')
R('| 2 lanes: luxury_bags_auth (seller-side AI flags) + fragrance; 10 comments |',
  '| 2 lanes: luxury_bags_auth (general seller moderation complaints, no category identified) + fragrance (mislabeled watches lane); 10 comments |')
# F1
R('In the 25 direct-eBay TikToks, 19 captions mention eBay in the creator\'s own words and 3 more mention it only in the Gemini description (r9, r15, r17); r3 (Skechers) has no eBay mention anywhere and r16 is unrelated meme noise whose caption contains "eBay" inside pasted Wikipedia text. In the 25 community TikToks, 1 caption mentions eBay (r32, a hashtag) and Gemini reports an eBay listing on screen in 2 (r38, r50).',
  'In the 25 direct-eBay TikToks, 18 captions mention eBay in the creator\'s own words; a 19th (r16) is unrelated meme noise whose pasted text happens to contain "eBay" and is excluded as irrelevant. 3 more records mention eBay only in the Gemini description (r9, r15, r17), and 4 have no relevant eBay attribution (r3, r11, r22, and the r16 noise row). In the 25 community TikToks, 1 caption mentions eBay (r32, a hashtag) and Gemini describes an eBay listing on screen in 1 (r38, unverified video interpretation); r50\'s Gemini text only editorialises about eBay\'s marketplace potential and is not counted as a listing.')
# F2
R('On YouTube, the two live lanes hold 10 comments: 1 buyer-voiced view of live selling, 6 seller or would-be-seller voices, 3 stream-ritual chatter ("duck race"). No row shows a buyer describing a purchase on eBay Live.',
  'On YouTube, the two live lanes hold 10 comments: 5 explicitly discuss selling, opening a shop, tracking seller profit or hosting; 1 comments on TikTok\'s audience size (role unknown); 1 says they enjoy live selling as buyer-seller "FaceTime" (role not stated); 3 are duck-related chatter whose meaning is not established by the text. No row shows a buyer describing a purchase on eBay Live.')
R('The client\'s handbags-versus-watches distinction cannot be tested here.',
  'The client\'s handbags-versus-watches distinction cannot be tested here. Like Coins, this is a sample gap; the full collection was not checked.')
# 2.1
R('Industry news as community event: "PSA bought Beckett and he\'s THRILLED", captioned "#thehobby" (r41, 180,900 views, the second-largest card row).',
  'Industry news as community event: the caption is only "He used to work there! #sportscards #thehobby"; the PSA-acquires-Beckett news and the "THRILLED" reaction are Gemini\'s reading of on-screen text (r41, 180,900 views, the largest of the 15 card-labelled rows).')
R('(r25, 49,600 views, 230 comments, 464 shares: the most-shared direct-eBay row).',
  '(r25, 49,600 views, 230 comments, 464 shares: third most-shared direct-eBay row, after r2 at 928 and r10 at 496).')
R('two comments are jokes about the creator calling Mark McGwire "Mark" (40 and 14 likes). Repacks',
  'two comments are jokes about the creator calling Mark McGwire "Mark" (40 and 14 likes). Enjoying the video or asking for a repeat is a reaction to the content, not evidence that those viewers buy mystery packs themselves. Repacks')
R('eBay is present, by caption or on-screen text, in 6 of 9 sports-card-labelled TikToks (AI-coded label, source-text check). None of these is eBay Live.',
  'eBay is present in 5 of 9 sports-card-labelled TikToks (AI-coded label): 3 by caption (r1, r10, r25) and 2 only in Gemini\'s reading of on-screen text (r9, r17). None of these is eBay Live.')
R('**Competitor behaviours.** Daily breaks are sold through TikTok Shop (r26). A pricing tool advertises itself "for pricing during whatnot, TikTok and eBay live stream" (r18, caption), which treats the three as peers for live card selling.',
  '**Competitor behaviours.** One breaker\'s caption promotes "daily breaks located in our Tiktok Shop" (r26): this confirms an offer and a promotional route, not buyer demand. A pricing tool advertises itself "for pricing during whatnot, TikTok and eBay live stream" (r18, caption), which names the three together and implies eBay Live card streams exist. Neither row shows which platform card buyers use or prefer.')
R('Breaks are already a live ritual and the sample locates them on TikTok Shop, with Whatnot named as a peer.',
  'Breaks are a live format; in this sample one is promoted through TikTok Shop and a tool names Whatnot, TikTok and eBay Live together. Whether eBay Live already hosts breaks, and for whom, is not shown.')
# 2.2
R('Pokémon rows share infrastructure vocabulary with sports cards (PSA, grading, sniping, scams; 4 of 15 card-labelled TikToks carry both labels, AI-coded), but the motivations in the source text are different enough that the two should be treated as separate communities with a shared toolset.',
  'Pokémon rows share vocabulary with sports cards (PSA, grading, sniping, scams; 4 of 15 card-labelled TikToks carry both labels, AI-coded), and both contain opening and reveal behaviour. The observed activities differ enough (chase, play, retail drops and local shops here; breaks, release-day product and auction mechanics in 2.1) that the two are described separately. This does not establish mutually exclusive audiences or motives.')
R('The r/pokemoncardcollectors post about a PSA submission lost in the mail that later appeared graded and listed on eBay:',
  'The r/pokemoncardcollectors post (discussion dated February 2026) about a PSA submission shipped in 2023, lost in the mail, that later appeared graded and listed on eBay:')
R('The place stolen graded cards surfaced, and the place a victim is told to warn with cert numbers, so eBay is treated as the hobby\'s registry of record.',
  'In one thread, a reported stolen graded card appeared for sale on eBay and a commenter recommended alerting eBay customer service with the certification numbers.')
R('eBay appears, by caption or hashtag, in 4 of 10 Pokémon-labelled TikToks (AI-coded label, source-text check).',
  'eBay appears by caption or hashtag in 4 of 10 Pokémon-labelled TikToks (r1, r2, r10, r18; AI-coded label), plus Gemini-only in r17.')
# 2.3
R('Three rows are store or affiliate promotions rather than community talk: Skechers sizes 40-46 (r3, 151,800 views, no eBay anywhere), Adidas Superstar at a reseller shop (r11), and Jordan 4 Retro with "yellowappfinds … Shopnow link in bio" (r28).',
  'Three rows read as store or affiliate promotions rather than community talk: Skechers sizes 40-46 (r3, 151,800 views, no eBay anywhere), Adidas Superstar at a reseller shop (r11), and Jordan 4 Retro with "yellowappfinds … Shopnow link in bio" (r28). The shop reading of r3 and r11 is Gemini\'s; r28\'s own caption carries the shop-now call.')
R('Sneaker insiders in this sample are sceptical of authentication as theatre; the entry-level buyer on Reddit values the guarantee. These are different people, and the sample cannot say which is more common.',
  'One self-described non-sneakerhead\'s Reddit question received four recommendations for eBay. Two sampled YouTube comments criticised authentication; the commenters\' expertise, and which authenticator or platform the second one means, cannot be identified from the text. Newcomer-oriented messaging is a testable idea (H8), not an established segmentation.')
R('An AG explainer aimed at newcomers like the Reddit poster, not at insiders who will mock it.',
  'An AG explainer aimed at newcomers like the Reddit poster (hypothesis H8).')
R('eBay appears in 1 of 7 sneaker-labelled TikTok captions (AI-coded label, source-text check), plus a Gemini-reported listing in r50.',
  'eBay appears in 1 of 7 sneaker-labelled TikTok captions (r19; AI-coded label). Gemini\'s editorial mention of eBay in r50 describes no listing and is not counted.')
R('The client did not expect sneakers to be an immediate Live priority and the sample agrees: no live behaviour appears in any sneaker row, engagement is display-driven, and the audience most likely to buy on trust (entry buyers) is not the audience producing the content.',
  'No live behaviour appears in any of the 7 sneaker rows and engagement is display-driven. That describes what was sampled; it can neither confirm nor refute the client\'s view that sneakers are not an immediate Live priority.')
# 2.4
R('Self-reward and reveal: "FINALLY BOUGHT MYSELF THE SPEEDY 20", an orange-bag-to-dust-bag unboxing of a new Louis Vuitton (r37, 59,900 views, 311 shares; Gemini interpretation of the unboxing sequence).',
  'Self-reward and reveal: caption "newest addition to my collection #louisvuitton #speedy20"; the on-screen "FINALLY BOUGHT MYSELF THE SPEEDY 20" and the orange-bag-to-dust-bag unboxing sequence are Gemini\'s reading (r37, 59,900 views, 311 shares).')
R('Deal thrill as humour: "Me after buying a £4 Gucci bag on ebay" (r20, 157,300 views; a joke, not a purchase record).',
  'Deal thrill as humour: caption "All rich and whatever #richgirl #ebay"; the "£4 Gucci bag on ebay" line is Gemini-read on-screen text (r20, 157,300 views; a joke, not a purchase record).')
R('This is the only row in the sample where a seller invites buyers to a livestream, and the reason given is condition inspection.',
  'This is the only row in the sample where a seller invites buyers to a livestream, and the reason given is condition inspection. The caption does not say which platform hosts the stream: it is a livestream promoted on TikTok, not a verified TikTok-hosted stream.')
R('Designer buttons as fashion history ("YSL called buttons daytime jewelry", r29, 20,300 views).',
  'Designer buttons as fashion history: the caption discusses YSL\'s buttons and estate sourcing; the "daytime jewelry" phrase comes from Gemini\'s hook field (r29, 20,300 views).')
R('**Seller-side friction (luxury_bags_auth lane).** Sellers report eBay\'s AI removing listings as counterfeit despite original photos:',
  '**Seller-side moderation complaints (lane labelled luxury_bags_auth, but no sampled comment identifies handbags or luxury).** Commenters say eBay\'s AI removed their listings as counterfeit despite original photos; the authenticity of their goods and the error of the removals are their claims, not verified:')
R('One plans to "include videos with my listings" to prove authenticity (UgzzpnENXTubHXc6Hzp4AaABAg).',
  'One plans to "include videos with my listings" to prove authenticity (UgzzpnENXTubHXc6Hzp4AaABAg). Another concerns relisting a video bought new on eBay (UgyxMuJxL5NiTQquLK94AaABAg). These are general seller frustrations and are not used here as luxury-specific evidence.')
R('Health risk (methanol in fakes) is raised. Small but coherent:',
  'Health risk (methanol in fakes) is raised. One commenter says they "got into amouage mainly through this channel" and "Finally got a bottle at Heathrow", thanking the creator "for the inspiration" (UgyiKMNK4OLJOTD7D854AaABAg): a self-reported purchase influenced by a creator, made at an airport retailer, not on eBay and not live. It is the sample\'s clearest creator-to-purchase pathway. Small but coherent:')
R('Against it: high ticket sizes plus a documented dispute culture, sellers who block inquisitive buyers, and AI moderation removing legitimate listings.',
  'Against it: high ticket sizes plus a dispute culture documented from the seller side, sellers who block inquisitive buyers, and general seller complaints about AI listing removals that are not specific to luxury. Prerecorded condition videos and detailed listings remain plausible alternatives to live (H3 is a hypothesis).')
# 2.5
R('Young aesthetic buyers of cheap vintage cameras;', 'Buyers of cheap vintage cameras who unbox, test and decorate them;')
R('Live testing suits the category\'s core anxiety, and dealers with warehouses have inventory.',
  'Live testing addresses the category\'s stated anxiety (hypothesis H4; a prerecorded test video answers the same question), and dealers with warehouses have inventory.')
# 2.6
R('These are not collectors, and the thread says nothing about toy buying behaviour beyond the fact that eBay hosts oddities that go viral.',
  'The subreddit is for spectators of bad taste; whether these commenters also collect is unknown, and the thread says nothing about toy buying behaviour beyond the fact that eBay hosts oddities that go viral.')
R('The reveal ritual is live-native and the expert chat is live-native.',
  'Reveal and expert chat are live-shaped formats (hypothesis H5); prerecorded unboxings and haul videos already carry both.')
# 2.7
R('So: precious-metals buyers on Reddit know eBay\'s return rules well and blame the buyer for breaking them, while the poster reports that eBay\'s high-value team could not say how bullion is authenticated.',
  'So: three sampled commenters criticise the drilling or describe eBay\'s return conditions, and the poster reports that eBay\'s high-value team could not say how bullion is authenticated. None of this verifies eBay policy or establishes what bullion buyers generally know.')
# 2.8
R('a host replies that they made "over $1M" live GMV this year,',
  'a self-described host replies (a single self-report, score 1) that they made "over $1M" live GMV this year,')
R('a commenter closed their shop the same day over forced refunds (t1_ns01h7a).',
  'a commenter closed their shop the same day over forced refunds (t1_ns01h7a); one of that thread\'s four sampled comments is the subreddit\'s automatic moderator bot (t1_nrz24ke).')
R('the eBay-vs-Whatnot-vs-Tilt podcast draws one buyer-flavoured comment, "With the death of the high street live selling is a great way to still have FaceTime between buyers and sellers. I enjoy it" (Ugwt_S7UKKCj9DVEFxR4AaABAg, 2 likes), one seller about to start on eBay Live, and three "duck race" comments that show a stream ritual (giveaway) without saying anything about buying.',
  'the eBay-vs-Whatnot-vs-Tilt podcast draws one comment enjoying live selling as "FaceTime between buyers and sellers" (Ugwt_S7UKKCj9DVEFxR4AaABAg, 2 likes; the commenter\'s role is not stated), one seller about to start on eBay Live, and three duck-related comments whose meaning (a giveaway, an in-joke) is not established by the text.')
R('Net: the sample knows what live hosts cost and what frustrates sellers on TikTok, and almost nothing about why buyers watch or buy.',
  'Net: the sample holds one host\'s self-reported rates and several sellers\' frustrations on TikTok, and almost nothing about why buyers watch or buy.')
R('A $25 shipping-supplies coupon tutorial (r23, 13,000 views), a Russian-language "how to sell on eBay in the US" (r7, 11,200 views), and a reseller inviting peers to a live about promoted-listing percentages (r15, 103 comments).',
  'A shipping-supplies coupon tutorial (r23, 13,000 views; the "$25" detail is Gemini\'s, the caption is "#ebaytips #ebayhowto"), a Russian-language "how to sell on eBay in the US" (r7, 11,200 views), and a reseller inviting peers to a live about promoted-listing percentages (r15, 103 comments; the eBay framing is Gemini-read on-screen text, the caption says reselling).')
# 3.2
R('- r50: that the sneaker collection implies eBay value (Gemini\'s editorial, not the creator\'s).',
  '- r50: Gemini\'s description associates the collection with eBay\'s marketplace potential; no listing is described, so r50 is not counted as an eBay presence.\n- r41: the PSA-acquires-Beckett news and the "THRILLED" reaction are on-screen text as read by Gemini; the caption is "He used to work there! #sportscards #thehobby".\n- r20: the "£4 Gucci bag on ebay" line is Gemini-read on-screen text; the caption is "All rich and whatever #richgirl #ebay".\n- r23: the "$25 coupon" detail is Gemini\'s; the caption is "#ebaytips #ebayhowto".\n- r29: "daytime jewelry" is Gemini\'s hook field; the caption discusses YSL buttons without that phrase.')
R('Flash label issues found while checking (AI-coded labels that should not drive counts without correction):',
  'Classification-granularity and interpretation issues found while checking. These are not a measured error rate: product category, community membership, speaker role and promotion status are separate questions, and a Flash label answers only the first.')
R('- r22 (Taobao proxy tutorial for Sanrio plush and K-beauty) is labelled Toys/Collectibles; the behaviour is proxy shopping for cute goods, not toy collecting.',
  '- r22 (Taobao proxy tutorial for Sanrio plush and K-beauty) is labelled Toys/Collectibles; the products relate to toys, but the behaviour shown is proxy shopping for cute goods and does not establish a collector identity.')
R('- YouTube comment Ugw7_BZXjEmQ32ZkUv14AaABAg (Anker affiliate links) is labelled Electronics with high confidence; it is advertising, not audience voice.',
  '- YouTube comment Ugw7_BZXjEmQ32ZkUv14AaABAg (Anker affiliate links) is correctly Electronics by product, but it is advertising rather than organic audience opinion and is excluded from voice counts.')
R('Metric caveats: TikTok comment counts are blank for 8 of 50 rows (treated as zero or unknown, not as evidence of no discussion).',
  'Metric caveats: TikTok comment counts are blank for 8 of 50 rows and are treated as unknown throughout; they are excluded from comment-based rankings rather than counted as zero.')
# appendix rows
R('| Direct pull: 19/25 captions name eBay, 3/25 Gemini-only (r9, r15, r17), 3/25 none (r3, r22, r16 noise). Community pull: 1/25 caption (r32), 2/25 Gemini-only (r38, r50) |',
  '| Direct pull: 18/25 relevant captions name eBay (r16 noise excluded), 3/25 Gemini-only (r9, r15, r17), 4/25 no relevant attribution (r3, r11, r22, r16). Community pull: 1/25 caption (r32), 1/25 Gemini-described listing (r38, unverified); r50 editorial only |')
R('| 3/50 TikTok captions; 2/10 Reddit posts (seller-side); 1 buyer-voiced comment out of 10 in the two live lanes |',
  '| 3/50 TikTok captions; 2/10 Reddit posts (seller-side); of 10 comments in the two live lanes: 5 explicit seller roles, 1 role unknown (audience size), 1 enjoys live (role not stated), 3 duck chatter |')
R('| Lane is a fragrance video |', '| Lane is a fragrance video; sample gap only |')
R('| One thread; poster asserts "1000 posts of this" without evidence in sample |',
  '| One thread; a commenter (t1_oo0d7ai) asserts "1000 post of this same thing", not verifiable in sample |')
R('| none | Repacks are not sealed-box breaks; 1 video |',
  '| none | Repacks are not sealed-box breaks; enjoying or requesting a video is not approval of buying repacks; 1 video |')
R('| F9 Breaks and live card pricing are located on TikTok Shop and Whatnot | F | r26, r18 (TikTok) | Captions (source) | 2/50 TikToks | none | Two creators; no buyer voice |',
  '| F9 A breaker promotes daily breaks via TikTok Shop; a pricing tool names Whatnot, TikTok and eBay Live together | F | r26, r18 (TikTok) | Captions (source) | 2/50 TikToks | none | Promotion and tool marketing only: not buyer demand, not platform ownership, and not evidence that eBay Live lacks breaks |')
R('| F10 eBay appears in most sports-card TikToks as storefront, auction rules, comps, AG hashtag | F | r1, r9, r10, r17, r25, r48 absent; presence in r1, r9(G), r10, r17(G), r25, r41 absent | Caption or Gemini on-screen text | 6/9 sports-card-labelled rows (AI-coded label; 4 by caption, 2 Gemini-only) | r26, r34, r41, r48 have no eBay | Label multi-coded |',
  '| F10 eBay appears in 5 of 9 sports-card TikToks: storefront, scam hashtag and auction rules by caption; vintage box and sniping tool by Gemini only | F | r1, r10, r25 (caption); r9, r17 (Gemini on-screen text) | Caption or Gemini | 5/9 sports-card-labelled rows (AI-coded label; 3 caption, 2 Gemini-only) | r26, r34, r41, r48 have no eBay | Two of five unverified; label multi-coded |')
R('| 1 post (7,649) + 4 comments; 1 comment advises alerting eBay with cert numbers | none | Outcome unknown; update link not in sample |',
  '| 1 post (7,649) + 4 comments; 1 comment advises alerting eBay with cert numbers | none | Shipment 2023, discussion 2026; outcome unknown; update link not in sample |')
R('| F15 Sneakers: entry buyer thread favours eBay AG; insider YouTube audience mocks authentication |',
  '| F15 Sneakers: a self-described non-sneakerhead\'s question drew 4 pro-eBay replies; two YouTube comments criticise authentication (expertise and target unclear) |')
R('| t1_ns09z15 says StockX has better deadstock prices | Different audiences; sizes unknown |',
  '| t1_ns09z15 says StockX has better deadstock prices | Speaker roles and expertise not established; tiny threads |')
R('| F17 The only buyer-facing live invite is a preloved handbag condition check | F | r44 (TikTok) | Caption (source) | 1/50; 2,362 views | none | Live is on TikTok, not eBay |',
  '| F17 The only buyer-facing live invite is a preloved handbag condition check | F | r44 (TikTok) | Caption (source) | 1/50; 2,362 views | none | Livestream promoted on TikTok; host platform not stated; not eBay Live |')
R('| F20 Fragrance buyers use eBay with self-imposed rules; luxury sellers hit AI counterfeit flags | F | youtube_comment:Ugw9sPoCMBY6yzXWcid4AaABAg, UgwTq0VdNA1gfg7-k3F4AaABAg; UgzwaT7tXCz_qQBtZLN4AaABAg, UgwGUVWGpmKUE7cfHDd4AaABAg, UgzzpnENXTubHXc6Hzp4AaABAg | Comment text | 2/5 and 3/5 comments under two small videos | none | Fragrance lane mislabeled as watches |',
  '| F20 Fragrance buyers describe self-imposed eBay rules and one reports a creator-inspired purchase at Heathrow; separately, sellers under a general video complain of AI listing removals (no category identified) | F | youtube_comment:Ugw9sPoCMBY6yzXWcid4AaABAg, UgwTq0VdNA1gfg7-k3F4AaABAg, UgyiKMNK4OLJOTD7D854AaABAg; UgzwaT7tXCz_qQBtZLN4AaABAg, UgwGUVWGpmKUE7cfHDd4AaABAg, UgzzpnENXTubHXc6Hzp4AaABAg, UgyxMuJxL5NiTQquLK94AaABAg | Comment text | 3/5 fragrance comments; 4/5 seller-complaint comments; both videos small | none | Fragrance lane mislabeled as watches; seller lane mislabeled as luxury; authenticity and purchase claims self-reported; the Heathrow purchase is not eBay and not live |')
R('| none | Young creators; no purchase data |', '| none | No purchase data; creator demographics not inferable |')
R('| F25 Toys: reveal, mail day, display, expert ID, resale oracle, proxy buying; spectators on Reddit |',
  '| F25 Toys: reveal, mail day, display, expert ID, resale oracle, proxy buying; a bad-taste spectator thread on Reddit (collector status unknown) |')
R('| F26 Bullion buyers know eBay return rules and blame the buyer for drilling; poster says eBay cannot authenticate bullion |',
  '| F26 Three sampled bullion commenters criticise the drilling or describe return conditions; poster says eBay\'s high-value team could not explain bullion authentication |')
R('| Poster\'s account of eBay\'s answer is one side | Not coin collecting |',
  '| Poster\'s account of eBay\'s answer is one side | Does not verify eBay policy or general buyer knowledge; not coin collecting |')
R('| 2 posts + 8 comments seller-side; 10 YouTube comments: 1 buyer-flavoured, 6 seller, 3 ritual chatter | Ugwt_S7UKKCj9DVEFxR4AaABAg (buyer enjoys live) | Self-reported earnings unverified |',
  '| 2 posts + 8 comments (1 of the 8 is the subreddit bot t1_nrz24ke); 10 YouTube comments: 5 explicit seller roles, 1 role unknown, 1 enjoys live (role not stated), 3 duck chatter | Ugwt_S7UKKCj9DVEFxR4AaABAg (enjoys live) | Host rate and GMV figures are one self-report |')
R('| H1 A comp-driven card buyer exists across sports and Pokémon, sharing tools (comps, PSA, sniping) but not motivations | H | F6, F10, F13, F14 | Mixed | 4/15 card TikToks dual-labelled (AI-coded) | F11 (ripping preferred to buying), F12 (shipping fear) | Shared vocabulary is not shared behaviour |',
  '| H1 Sports cards and Pokémon show different observed activities with shared vocabulary and shared opening/reveal behaviour; a comp-driven buyer may exist in both | H | F6, F10, F13, F14 | Mixed | 4/15 card TikToks dual-labelled (AI-coded) | F11 (ripping preferred to buying), F12 (shipping fear) | Activities differ; audiences may overlap; not a segmentation |')
R('| F18 dispute culture; F20 AI flags; odour not showable | No buyer voices |',
  '| F18 dispute culture (seller accounts); general AI-removal complaints not luxury-specific; odour not showable; prerecorded condition videos are an alternative | No buyer voices |')
R('| F24 seller risk on high-value returns | No live behaviour observed |',
  '| F24 seller risk on high-value returns; prerecorded test videos answer the same question | No live behaviour observed |')
R('| Blind-box supply is retail; sub-hobbies tiny in sample | Untested |',
  '| Blind-box supply is retail; prerecorded unboxings already carry the ritual; sub-hobbies tiny in sample | Untested |')
R('| H8 Sneaker AG messaging should target entry buyers, not insiders | H | F15 | Reddit; YouTube | 4 vs 2 comments | none | Two tiny audiences |',
  '| H8 Newcomer-oriented AG messaging for sneakers is testable | H | F15 | Reddit; YouTube | 4 vs 2 comments | none | No segmentation established; two tiny threads |')
R('| H9 Break demand exists but its live home is TikTok Shop/Whatnot; eBay Live would be entering, not creating, that ritual | H | F9, F8, F27 | Captions; comments | 2 TikToks, 1 YouTube lane | F8 shows mixed buyer sentiment on repacks only | No break buyer voice |',
  '| H9 Break demand may already be served through TikTok Shop and Whatnot; eBay Live\'s current position in breaks is unknown | H | F9, F8, F27 | Captions; comments | 2 TikToks, 1 YouTube lane | F8 shows mixed viewer reactions to repacks only | Promotion evidence only; no break buyer voice |')
# overview
R('2. The live rituals that exist are located elsewhere and are seller-described: breaks on TikTok Shop, live hosts priced by the hour on TikTok, Whatnot named as a peer. The one buyer-facing live invite is a condition check on preloved handbags.',
  '2. The live activity the sample does show is seller-described: a breaker promoting daily breaks through TikTok Shop, one host\'s self-reported hourly rates on TikTok, a tool naming Whatnot, TikTok and eBay Live together. Buyer demand for any of it is not observed. The one buyer-facing live invite is a condition check on preloved handbags, promoted on TikTok.')
R('3. Sports cards and Pokémon share a toolset (PSA, comps, sniping, scam fear) but not a motivation: the sports rows are about events, product releases and auction skill; the Pokémon rows are about the chase, play, grails and the fear of shipping them. They should be planned as two communities.',
  '3. Sports cards and Pokémon share vocabulary (PSA, comps, sniping, scam fear) and both show opening and reveal behaviour, but the observed activities differ: the sports rows are about events, product releases and auction skill; the Pokémon rows are about the chase, play, grails and the fear of shipping them. Plan them separately while allowing that audiences overlap.')
R('and sellers describe AG-triggered disputes on handbags and AI flags on luxury listings.',
  'and sellers describe AG-triggered disputes on handbags and, under a general video, AI counterfeit removals.')
R('These are content forms, and several are live-shaped, but the sample cannot show they convert.',
  'These are content forms, and several are live-shaped, but the sample cannot show they convert.\n7. The one explicit creator-to-purchase pathway is a fragrance viewer who "got into amouage mainly through this channel" and bought at Heathrow. It shows a creator driving discovery to another retailer; the sample has no equivalent for eBay or for Live.')
R('- Native eBay Live chat and replay chat, which the Read First tab says exist in the wider corpus but are not here.',
  '- Native eBay Live buyer chat and transaction performance, which have not been established as available. The wider collection includes YouTube replay chat, not eBay Live chat.')

bad = [(t.count(o), o[:90]) for o, n in E if t.count(o) != 1]
if bad:
    print("ABORT, anchors not matching exactly once:")
    for b in bad: print(b)
else:
    for o, n in E: t = t.replace(o, n)
    open(p, "w", encoding="utf-8").write(t)
    print("applied", len(E), "patches; words:", len(t.split()))
