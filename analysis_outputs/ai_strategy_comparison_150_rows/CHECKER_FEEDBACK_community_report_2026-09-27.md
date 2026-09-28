# Checker feedback: revised Fable community report

Checked 2026-09-27. No paid calls or source changes.

## Verdict

The revised structure fits the client brief substantially better: community sections, behavioral differences, platform roles, concrete content opportunities, and hypotheses distinguished from findings. Preserve that work. Correct the issues below before extending its conclusions to the full corpus. This is a targeted evidence audit, not verification of the downloaded videos or of platform policies.

Reviewed the complete revised report, all 50 TikTok captions and their metrics/labels, all 50 Reddit source rows, all 50 YouTube comments, selected Gemini interpretation fields, the sample methodology, and the previously reviewed client call/email. The original report and workbook are unchanged.

Files:
- Report: `claude_fable_5-1_eBay_Live_community_report_2026-09-27.md` in this folder.
- Workbook: `C:\Users\andre\Documents\ebay_research\data\tests_and_supporting_files\ai_strategy_comparison_150_rows\TEST_150_rows_eBay_Live_AI_comparison_sample.xlsx`.
- Client call: `C:\Users\andre\Documents\ebay_research\context_uploads\ebay1.txt`.
- Internal discussion: `C:\Users\andre\Documents\ebay_research\context_uploads\ebay12.txt`.
- Email copy: `C:\Users\andre\Documents\ebay_research\data\tests_and_supporting_files\local_llm_cleanup_pilot_20260925\supporting\original_copies\context_uploads\strategy_email.txt`.

## What holds up

- Inventory: 50 TikTok videos, 10 Reddit posts plus 40 comments, 50 YouTube comments under 10 videos.
- All extracted cited IDs resolve: 50 TikTok, 41 Reddit, 29 YouTube. Resolution alone does not validate the associated claim.
- TikTok label totals: Sports Cards 9, TCG/Pokemon 10, Sneakers 7, Luxury 6, Electronics 6, Toys 6, General 5, Other 9. Labels overlap; these are AI-label counts.
- Separating sports cards and Pokemon is useful for this brief. The source captions support different activities, including release-day pulls, collection-building, pack chasing and deck customization. They do not establish mutually exclusive audiences or motives.
- Handbag condition inspection has a direct source-caption invitation to a livestream. Seller descriptions of condition disputes provide useful supporting context, with buyer motivations remaining second-hand.
- GI Joe accessory completion and identification, vintage patches' personal histories, and eBay finds are useful concrete behaviors to pursue.
- The sample contains no substantive numismatic-collector evidence. The YouTube watches lane is fragrance and the camera lane is a vintage buyout. These sample gaps do not establish gaps across the full collection.
- Reddit sampling retained four selected direct comments per post. It was not a Gemini-generated replacement of the full thread text.

## Required corrections

### 1. Correct the wider-data provenance

Section 5 says the Read First tab establishes that native eBay Live chat exists in the wider corpus. It does not. Read First lists material absent from this sample; that is not an inventory of collected material. Our collected replay chat came from YouTube.

Replacement: "The wider collection includes YouTube replay chat. Native eBay Live buyer chat and transaction performance have not been established as available."

### 2. Fix the citation row convention

The report says r12 means row 12 of the worksheet, but its r1 is the first data record, Excel row 2. Every TikTok rN reference is displaced by one if a checker follows the stated convention.

Define rN as a data-record index with Excel row N+1, or use actual worksheet coordinates consistently. Retain full evidence IDs. The unique full-ID lookup is a genuine improvement over the previous abbreviated IDs.

### 3. Correct the counts and ranks

- F10: eBay appears in source captions for 3 of 9 Sports Cards-labelled videos, data rows 1, 10 and 25. Two additional rows, 9 and 17, have Gemini-only eBay attribution. Combined source-or-AI presence is 5/9, not 6/9. Do not describe all five as source-confirmed.
- F1: 19/25 direct-pull captions literally contain eBay, including the unrelated Tesla-text row 16. Excluding that incidental mention leaves 18/25 relevant caption mentions; three further records have Gemini-only attribution, and four have no relevant eBay attribution. Alternatively report 18/24 among retained records if excluding the noise row from the denominator, and explain the exclusion. Do not report 19 relevant captions plus classify the same noise record as absent.
- Sports section: Extended Bidding has 464 shares, third in the direct-eBay sample behind the Pokemon opening post (928) and scam story (496). It is not the most-shared direct-eBay row.
- The PSA/Beckett row has 180,900 views, the highest among the 15 card-labelled TikToks, not second-highest.
- Eight missing TikTok comment counts are unknown. Do not alternate between treating them as zero and unknown for calculations.

### 4. Keep AI-only observations consistently identified

The sports section presents the PSA/Beckett news as source text unless marked. Its caption is only "He used to work there!" plus hashtags; the acquisition and reaction come from Gemini's interpretation (data row 41, Excel row 42).

Other insufficiently marked examples: the GBP4 Gucci joke (data row 20), YSL's "daytime jewelry" attribution (29), and the USD25 shipping coupon detail (23). These details may be correct, but are not established by the supplied source captions.

Data row 50 has no Gemini-described eBay listing. Gemini editorially associates a sneaker collection with eBay's marketplace potential. The coverage inventory and F1 must not count that as an observed listing on screen. Of the two claimed community-pull on-screen eBay listings, only data row 38 actually has that description, and it is still unverified video interpretation.

### 5. Correct a third misleading YouTube lane

The `luxury_bags_auth` video is "How To Avoid eBay Counterfeit Listing Removal From AI." Its selected comments do not establish handbag/luxury sellers. One is about relisting a purchased video, and the others discuss expensive merchandise or listing photos without identifying a category.

Keep these as general seller moderation complaints. Do not use the lane name to turn them into luxury-specific evidence in F20 or the handbag Live counterargument. Also attribute claims of authentic merchandise and erroneous removal to the commenters; they were not independently verified.

### 6. Remove unsupported audience identities

F15/H8 call skeptical YouTube commenters sneaker "insiders" and recommend targeting entry buyers instead. The Reddit questioner explicitly says they are not a sneakerhead. The YouTube comments do not establish expertise or experience. One criticizes a place used to authenticate shoes; the text alone does not identify which place or platform.

Replacement: "One novice's Reddit question received four recommendations for eBay. Two sampled YouTube comments criticized authentication; the commenters' expertise and the target of one criticism are unclear." Newcomer-oriented messaging remains a testable idea, not an established segmentation finding.

Similarly, do not infer that ATBGE commenters cannot also be collectors, or that vintage-camera creators are young, from these text fields. Describe the behavior shown rather than assigning identities.

### 7. Distinguish promotion, entertainment and buyer demand

F9/H9: a caption promoting daily TikTok Shop breaks confirms an offer and promotional route. PriceHUD names Whatnot, TikTok and eBay Live together. Neither proves buyer demand, platform ownership of the ritual, or that eBay Live is absent from that behavior.

F8: mixed reactions to a mystery-pack video are supported. Enjoying the video or asking the creator to repeat it is not necessarily approval of buying mystery packs personally.

F17: the handbag invitation occurs in a TikTok caption, but does not explicitly name the platform hosting the stream. Say "a livestream promoted on TikTok," not a verified TikTok-hosted stream.

Treat live testing, inspection and expert-identification ideas as hypotheses. Prerecorded demonstrations and ordinary listings remain plausible alternatives. This does not diminish their value as content ideas.

### 8. Fix speaker and bot counts

The TikTok Shop Reddit group includes the automatic moderator comment `reddit:t1_nrz24ke`, explicitly stating it is a bot. F27's eight comments are not eight human seller voices.

In the ten comments under the two YouTube live-related videos, five explicitly discuss selling, opening a shop, tracking seller profit or hosting sales. A sixth discusses TikTok's audience size without establishing the speaker's role. The "FaceTime between buyers and sellers" comment expresses enjoyment but does not establish that its author is a buyer. The remaining three are duck-related chatter; a giveaway mechanism is not verified by those comments alone.

Use explicit, inferred and unknown speaker roles instead of forcing a complete 1-buyer/6-seller split. Describe the single host's rate/GMV claims as self-reported examples, not knowledge of what live hosts generally cost.

### 9. Recover a highly relevant creator-to-purchase example

The fragrance section omits `youtube_comment:UgyiKMNK4OLJOTD7D854AaABAg` (YouTube Comments, Excel row 29). The commenter says they got into Amouage through the channel and later bought their first proper niche fragrance at Heathrow, thanking the creator for the inspiration.

This is particularly relevant to the client's interest in creator roles, discovery and pathways to commerce. It is one self-reported purchase influenced by a creator, at a different retailer. It demonstrates neither an eBay sale nor a Live conversion. Include it with that limitation.

The sports/Pokemon distinction should also allow overlaps: both sets contain opening/reveal behavior. "Different observed activities within each community" is better supported than "shared tools but not a motivation."

### 10. Bound claims about community knowledge and absence

F26 should say three sampled commenters criticize drilling or discuss return conditions. Their statements do not verify eBay policy or establish what bullion buyers generally know. The packaging claim about "1000 posts" comes from a comment, not the original post.

The Pokemon loss account describes a shipment in 2023, although the discussion is dated 2025 onward. Distinguish the event date from the discussion date when describing current experiences.

The absence of Live in seven sneaker videos cannot validate the client's existing prioritization. The sample can describe what was observed; it cannot establish that Live would not fit.

"eBay as the hobby's registry of record" overstates one stolen-card listing and advice to notify customer service. Use the literal behavior: a reported stolen card appeared for sale on eBay and a commenter recommended alerting eBay with certification numbers.

## Label audit correction

An Anker promotion can correctly be categorized as Electronics while being unsuitable as organic audience opinion. Product category, community membership, speaker role and promotion status are separate fields. A Taobao tutorial involving plush can also be related to Toys/Collectibles without proving a collector identity. Present these as classification-granularity and interpretation issues, not automatically as demonstrated label errors. The count of "five Flash errors" is not a measured error rate.

## Recommended handback

Patch the report and its checkpoint using these corrections; retain the existing originals/version history. No new paid pass is needed to make these changes. Preserve the community structure and practical ideas. Do not expand the narrative length merely to incorporate caveats.

Then use the corrected findings and hypotheses as questions for the larger existing collection. Search for confirming and contradicting evidence across communities, including Coins and watches; do not inherit the mini-sample's absence claims. Continue community work without waiting for business data, while reserving commercial investment decisions for the business-data overlay requested in the email.
