# Prompt changes for direct-eBay TikTok videos

Only this 1,007-row source is authorized. Previous outputs and prompts stay intact.

Evidence sent: caption, ad_description, ebay_item. All original columns remain in the duplicated output; IDs are control metadata. No video files, metrics, transcripts or other columns are sent.

## Lessons from the 500-comment QA

- Row 39: do not invent what $3,000 represents or assume humor. Preserve item context where useful.
- Row 500: a concern about a price does not mean the price is low. Never invent cheap/expensive.
- Preserve negation, conditions, uncertainty, speaker and direction of a claim.
- Ambiguous fragments and uncertain translations require low confidence, not invented meaning.

## Checklist-specific flags for this file

- These are videos, not viewer comments. Do not describe creator content as audience sentiment.
- Existing AI descriptions are secondary text, not verified video observations. No new video analysis is being performed.
- Missing descriptions: rely on the caption/item when usable, otherwise mark unclear.
- eBay search selection does not establish eBay relevance, endorsement or representativeness.
- Preserve explicit sponsorship/AD; do not turn promotions into independent recommendations.
- Authenticity claims are claims, not proof. Asking price is not completed sale; revenue is not profit.
- Use seven client communities when supported, with Other / emerging and Unclear available. Ordinary clothes and vintage denim are not automatically Luxury Fashion; physical game media are not hardware.
- No neighboring-row context leakage. No strategy recommendations.

## Quick QA after completion

Verify 1,007 unique evidence IDs, six new columns, every original cell and column order, source/copy hashes, valid community/confidence values, and all API response statuses. Spot-check diverse rows including missing descriptions, ads, ordinary clothing, coins versus currency, hardware versus games, vague text, authenticity and price claims. Record limitations explicitly; do not silently rewrite model outputs or launch paid retries.
