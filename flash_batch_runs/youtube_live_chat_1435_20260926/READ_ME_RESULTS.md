# YouTube live chat: completion and quick QA

- Complete: 1,435/1,435 rows, 145 successful requests. Original cells, headers, row order, source hash and evidence IDs passed verification.
- 1,419 rows processed by Gemini; 16 original error/system rows retained with explicit exclusion labels and no AI interpretation. These include source collection errors, not errors in this Gemini run.
- Google runtime: 18:15:07.682 UTC to 18:17:57.349 UTC on September 26, 2026, 169.67 seconds (2m50s).
- Usage: 213,886 input tokens, 129,878 output, 0 thinking. Estimated Batch cost $0.3237285. Completed recorded total $2.49874725; conservative completed/baseline $2.580795375 plus cancelled-attempt hold $2.85 = $5.430795375 before next reservation. These are usage-based estimates, not reconciled invoices.
- Five spread-out samples checked: rows 1, 359, 718, 1077, 1435. Source error excluded; enthusiastic reaction remained nonspecific/low-confidence; 'lol' stayed unclear; numeric message summary remained literal; greeting remained a greeting. No invented purchase or on-screen event in these summaries.
- Nonblocking label caveat: row 1077 message '50' has topic 'auction bid' based on stream context. It is not a confirmed bid, currency amount or purchase. Summary is literal and confidence low. Row 359 Sports Cards routing is inferred from Cams Cards/breaks context, not the reaction itself. Do not turn these labels into confirmed viewer intent.
- Checked all three special audience events: row 508 is a Super Chat greeting; rows 1223 and 1244 are membership events with empty messages. All three summaries preserve event type without inventing purchases. All 16 system/error rows have excluded labels.
- Original and Gemini output untouched. Brief QA is not exhaustive semantic validation. Future prompt flag added for bare numbers versus confirmed bids.
- Final CSV: FINAL_1435_YouTube_live_chat_rows_Flash_Batch_communities_topics.csv
