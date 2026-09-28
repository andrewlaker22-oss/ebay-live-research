# 500 TikTok comments: Flash Batch complete

- 500 comments from 50 selected research videos processed with Gemini 3.8 Flash Batch.
- All 500 row identities and required outputs passed structural checks. All 13 original columns were preserved exactly, in the original order, with six new fields appended.
- The original CSV and verified duplicate are unchanged. No data files were deleted.
- Estimated cost from returned API usage: **$0.10929**. Input: 52,220 tokens at $0.375/million. Output: 47,844 tokens at $1.875/million. No additional thinking tokens reported. This is not a billing-statement reconciliation.
- Only comment text, item category and item name were sent as research evidence. IDs are mapping metadata. No videos, author fields or URLs were sent.
- New fields: `flash_community`, `flash_specific_category`, `flash_topic`, `flash_short_summary`, `flash_confidence`, `flash_evidence_row_id`.
- Community labels may use the original item's context; they do not prove that a vague comment expressed an opinion about the community.
- This job is complete. No other CSV was submitted and no repeating monitor was created.

## File

[Completed CSV](C:/Users/andre/Documents/ebay_research/flash_batch_runs/tiktok_comments_500_20260925/FINAL_500_TikTok_comments_50_videos_Flash_Batch_communities_topics.csv)

The original duplicate, requests, raw results, status and preservation checks are in `supporting/`. The full CSV is at this folder's top level.

## Review

Fourteen rows were spot-checked: original comment rows 1, 31, 35, 39, 221, 225, 226, 229, 281, 284, 288, 350, 450 and 500. This is not an exhaustive accuracy audit.

Two wording issues remain in the untouched model output:

- **Comment row 39:** "Wow, $3000 and you pick Applebees? Insane choice." The model says "after having or spending $3,000" and calls it a joke. Neither the money's role nor definite humorous intent is established. Safer reading: the commenter criticizes the Applebee's choice while mentioning $3,000. The model also chooses Unclear rather than retaining the parent item's vintage-clothing context.
- **Comment row 500:** The commenter is nervous about authenticity "for the price they are charging." The model adds **low** prices, which the comment does not establish. Safer reading: concern about authenticity in relation to the asking price, especially for new items.

Useful checks: both ownership/piracy conditionals retained their negation; "I know a guy" stayed vague rather than becoming an unsupported unauthorized-source claim; ambiguous one-word comments stayed low confidence.

Model-reported confidence: 330 high, 108 medium, 62 low. These are self-assessments, not measured accuracy. Low-confidence rows should remain distinguishable when another AI aggregates themes.

No manual corrections were silently applied to the model output. Original text, row IDs and video URLs remain available for checking any summary.

## Preview

| Comment row | Community | Topic | Short summary |
| --- | --- | --- | --- |
| 35 | Other / emerging | price skepticism; market valuation | Commenter questions paying $3,000 for non-luxury jeans that originally retailed under $100. |
| 221 | Other / emerging | piracy; digital ownership | Commenter argues that piracy is not stealing if purchasing digital media does not confer true ownership. |
| 450 | Toys/Collectibles | collecting sentiment; selling advice | Commenter affirms the value of enjoying the collecting phase and suggests selling the collection to fund other hobbies. |

[Processing checklist](C:/Users/andre/Documents/ebay_research/FLASH_PROCESSING_CHECKLIST.md)
