# Start here, Fable

This is targeted Gemini enrichment, NOT the final strategic analysis. Original CSVs are untouched and duplicated.
Brand Posts is excluded. Existing community/topic/category/summary labels were not overwritten or re-generated wholesale.

## Read in this order
1. 05_COVERAGE_AND_QA.json: completion status, exact counts, sample design, cost, pilot review and caveats.
2. 01_CONVERSATION_DIGESTS.jsonl: all COLLECTED discussion groups; never call them complete platform conversations.
3. 02_BLIND_LABEL_CHECK.jsonl: 50 random rows per source tab, source-only; agreement is not accuracy.
4. 03_CONTROL_ENRICHMENT.jsonl: 300 random non-keyword rows; additional Live fields and possible missed signals.
5. 04_SOURCE_EVIDENCE_AND_EXISTING_LABELS.jsonl: exact text, IDs, parent IDs, duplicate locations and date flags to check claims.

## Your job
Continue your saved hypotheses and analysis; do not restart stages A/B. Use digests as an index, not independent evidence.
Do not paste or load the entire source JSONL into your model context. Use the included research_tools.py with your local
code environment: inventory; communities; search --text "eBay Live"; search --community "Coins";
group --id GROUP_ID; evidence --id EVIDENCE_ID; disagreements; control-signals. These commands are free local lookups,
not AI calls. Start with inventory and community coverage, then examine bounded groups and source evidence as needed.
Known pilot issues are listed in 05_COVERAGE_AND_QA.json and attached to affected findings as review_flags. A flag with
exclude_until_checked=true means the model's paraphrase must not support a conclusion until you read its source.
The original model output is preserved; flagged errors are not silently rewritten into apparently clean findings.
Read the underlying sources for report-bearing claims, disagreement, rare communities and unexpected control signals.
Use code for counts, deduplicate distinct parents, and show numerator/denominator/unit. Finding support counts count cited
rows only, not all supporters or unique people. Different findings can cite the same row. Original labels can be wrong.
Unknown dates cannot establish 2025-onward behavior. Exclude pre-2025 from current counts, preserve them as historical context.
Missing reply parents may make stance unclear. YouTube chat is not native eBay Live. Views/bids/greetings are not purchases.
Do not use a single AI agreement percentage to claim validity. Your prior TikTok coding is a comparison, not ground truth.
No full second pass of all rows is scheduled: request only specific unresolved evidence if genuinely necessary.

## Client and output
Use the included CLIENT_AND_ANALYSIS_BRIEF.md, with the following update: do not reread every row sequentially if the
digests and source-linked targeted review suffice. Distinguish machine-processed coverage from direct analyst review.
Community understanding comes first, then provisional opportunities for shopping on eBay Live. Cover the six starting
categories plus Coins and meaningful additional communities. Handles are optional, not the assignment. No fabricated
purchase intent, market size, geography comparisons or causal claims. Write a community report plus numbered claims/
evidence appendix. Save a checkpoint after each community: reviewed IDs, calculations, contradictions, remaining work.
Give the useful findings in plain language; do not produce a deck. Preserve your frozen hypotheses and log changes.
No paid calls or new enrichment without the user's permission.
