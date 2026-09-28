# Reddit broad Flash results

- Complete: 2,098/2,098 rows (100 source posts, 1,998 comments); 248/248 requests succeeded.
- Google start 2026-09-26 16:58:32 UTC; end 17:02:43 UTC. Runtime 4 minutes 11 seconds.
- Estimated Batch cost $0.6173055: 618,713 input tokens and 205,487 output tokens, no thinking tokens reported. Usage-based calculation, not a billing-statement reconciliation.
- All 17 original columns, values and row order preserved. Six Flash columns appended. Original and duplicate SHA-256 match.
- Input limited to title and text, including explicitly labeled thread and immediate-parent context. No other AI used, no paid retries and no substitute research analysis.
- Evidence IDs, response completeness, context mapping and original-cell preservation checks passed.

## Quick QA

Spot checks: source rows 1, 2, 3, 201, 501, 506, 901, 1301, 1701 and 2098. Four additional missing-parent comments checked: 9, 24, 25 and 28. These four summaries stayed with the commenter's contribution and did not invent agreement with an absent parent. This is a limited sample, not a full accuracy audit.

- Row 506 has no Reddit ID, URL or date. Its source_title hash is a LOCAL evidence ID. It remains unverified and must not be counted as confirmed January-2025-onward evidence. Model confidence describes its text interpretation, not source verification. The output retains the source's final update resolving the authenticity dispute rather than presenting the earlier scam suspicion as established fact.
- 49 comments lack their immediate parent in the source. Missing context remains explicitly unavailable; thread context is not proof of a commenter's opinion.
- Taxonomy review: row 501 concerns gold bars but is routed to Coins. Review bullion versus numismatic collecting before using that bucket's totals. Output was not silently corrected.
- Wording review: row 3 shortens "Star Wars toy set" to "Star Wars set," which could be misunderstood as a filming set. Preserve the original text for that detail; add a keep-item-nouns rule to a future prompt if needed.

## Budget And Files

Recorded total across four completed files: $1.506502125. Conservative cap accounting: $0.97124475 before this run + $0.6173055 = $1.58855025 against the $10 limit. The former $8.39 reservation was a padded allowance, not an actual charge.

Final: FINAL_100_Reddit_conversations_1998_comments_Flash_Batch_communities_topics.csv

Completion monitor paused. No next dataset launched by this check. Originals, raw responses, request mapping, source duplicate and earlier versions remain intact.
