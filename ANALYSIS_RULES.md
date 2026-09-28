# ANALYSIS_RULES.md — evidence rules for the eBay Live community research

Created 2026-09-27 from the checker's audit of the 150-row sample report (revision 2.1). Corrected 2026-09-28 (version 2): the `audio_transcript` field is Gemini output from sampled frames, not speech-to-text. Version 1 is archived at `analysis_outputs/full_dataset_inventory/ANALYSIS_RULES_v1_2026-09-27.md`. These rules apply to every community section, every count and every claim in later passes over the full collection. Division of work: Gemini organises evidence (labels and summaries already produced), Fable synthesises, the checker verifies important claims. No rule here authorises a new paid run, and none permits deleting columns or re-running tagging.

## 1. Source versus AI interpretation

- Name the layer for every quoted or paraphrased detail. The layers are:
  - **Source**: what a person wrote or the platform recorded (caption, hashtags, post text, comment text, chat message, score, likes, views, dates, URLs).
  - **Gemini video interpretation from sampled frames plus metadata**: the 24 September 2026 tagging pass (`gemini-2.5-flash fast-frames`) received sampled video frames and text metadata, not audio. Every field it produced is interpretation: `ad_description`, `visual_description`, `hook`, `first_3_seconds`, `ebay_item`, `notable_text_on_screen`, `claim`, `cta`, `buyer_or_seller_angle`, `ebay_relevance`, `item_category`, `audio`, `sound` and `audio_transcript`. On-screen text read by Gemini is interpretation until the caption confirms it.
  - **`audio_transcript` is not a transcript.** The tagging prompt asked for a verbatim transcript but supplied only frames and metadata. Across the 1,921 TikTok videos, 1,067 entries are explicit placeholders ("[MUSIC / NO CLEAR SPEECH DETECTED]", "unknown from sampled frames", or the prompt's own fallback sentence echoed back) and 12 are blank; the remaining 842 populated entries are Gemini's reconstruction from frames (on-screen captions, subtitles or inference) with no verified audio provenance. Rules: never quote this field as something a creator said; never use it to validate `ad_description` or any other Gemini field (same model, same inputs); use it only to locate rows, and mark any detail drawn from it as "Gemini-read". If a verified transcript source is ever added (a separate audio pass with its own provenance), it gets its own column and its own layer name; the existing column is preserved unchanged.
  - Keep four things separate in every write-up: captions and hashtags (creator's words), audience comments and chat (other people's words), Gemini interpretations (all frame-derived fields), and verified transcripts (none exist yet).
  - **Flash text labels**: `flash_community`, `flash_specific_category`, `flash_topic`, `flash_short_summary`, `flash_confidence`. For TikTok these were produced from text that includes Gemini fields, so Flash agreeing with Gemini is not independent confirmation.
  - **Researcher assignment**: lane names, buckets, search queries, sample selection. A lane name is not evidence of what a video or comment is about (the sample's watches lane was fragrance; its camera lane was a Halloween buyout; its luxury-bags lane was general seller complaints).
- A claim that rests only on Gemini or Flash is marked "Gemini-read" or "AI-coded" in the sentence where it appears, not only in an appendix.
- Gemini mentions eBay far more often than sources do (community TikTok pull: 173 Gemini descriptions versus 8 captions). Never count a Gemini eBay mention as an observed eBay presence.
- A Flash label answers "what product category" at best. It does not establish community membership, speaker role, promotion status or collector identity. Treat label disagreements as classification granularity, not as a measured error rate, unless an error rate was actually measured.

## 2. Accurate denominators

- Every percentage or ratio states numerator, denominator and unit (videos, posts, comments, chat messages, streams).
- Define the denominator before counting. Say whether noise rows, failed rows (`gemini_failed`), bot rows, system or error chat rows, and blank metrics are included or excluded, and apply the same choice everywhere in the document.
- A count that depends on Flash or Gemini labels says "AI-coded". Multi-label fields sum to more than the row count; say so.
- Blank metrics (missing comment counts, missing dates) are unknown, never zero. Exclude them from rankings rather than ranking them last.
- Rank claims ("most shared", "largest") are checked against the full column before they are written.
- Sample proportions describe the sample. They are not population shares and not market opportunity.

## 3. Independent units and conversation counts

- Count independent units (videos, posts, streams) separately from dependent units (comments under a post or video, chat messages within a stream). Ten comments under one video are one video's audience, not ten examples.
- A thread's sampled comments are a selection (top-scored, top-liked, direct replies only, capped per post). The sample can drop opposing views and reply context. Before claiming what "the thread" or "the community" believes, check what was sampled and what was not.
- State the event date separately from the discussion date when they differ (a 2023 shipment discussed in 2026).
- Deduplicate across files before counting: the two Reddit pulls share 39 rows; TikTok comment videos come from both TikTok pulls; YouTube comments and live chat are joined to videos by `video_id`. Use `flash_evidence_row_id` as the join and dedup key; it is unique within each file.

## 4. Explicit, inferred and unknown speaker roles

- Classify each speaker as **explicit** (they say they sell, buy, collect, host), **inferred** (context strongly implies it, and the inference is stated), or **unknown**. Do not force a complete buyer/seller split.
- Bots, moderators, hosts and advertisers are separate roles. Flag automatic moderator comments, `is_owner` and `is_moderator` chat rows, affiliate links and promotional comments, and exclude them from audience-voice counts while keeping them in the record.
- Self-reported figures (earnings, rates, GMV) are one person's claim, reported as such.
- Do not assign identities the text does not give: "insider", "novice", "young", "collector", "not a collector". Describe the behaviour shown instead. A self-description ("I'm not a sneakerhead") may be quoted.

## 5. Promotion versus demand

- A caption promoting an offer (daily breaks in a shop, a live Q&A, a link in bio) confirms an offer and a promotional route. It is not buyer demand, platform ownership of a behaviour, or evidence that another platform lacks it.
- Enjoying a video, asking for a repeat, or bidding chatter is a reaction to content, not approval of buying the product or intent to buy.
- Views, likes, shares and comment counts are attention, not purchase intent.
- A livestream promoted on a platform is not a verified stream hosted on that platform unless the text names the host.
- Live-shaped content ideas (testing on camera, condition inspection, reveals, expert identification) are hypotheses. Prerecorded videos and ordinary listings remain plausible alternatives; say so where the idea is proposed.

## 6. Category versus audience identity

- Product category, community membership and audience identity are different claims. A Taobao tutorial featuring plush relates to toys without proving a collector; an Anker link under an Apple video is Electronics by product and advertising by role.
- Shared vocabulary between two groups (PSA, comps, sniping) does not establish one community or one motivation. Describe observed activities per group and allow overlap; do not assert mutually exclusive audiences.
- A subreddit's purpose (spectacle, seller advice) frames but does not determine what its commenters are.

## 7. Counterevidence and absence

- Every finding row in an appendix carries a counterevidence cell and a limitation cell, even when the entry is "none found".
- Search for contradicting rows before writing a pattern claim. Report the strongest opposing row alongside it.
- Absence in a sample or a search pull is a coverage fact about that pull, not about the community or the platform. Never write "the community does not" or "the platform lacks" from absence alone. The sample's zero rows for coins and watches say nothing about the full collection.
- Do not let a sample's absence validate or refute a client prior (for example, that a category is not a Live priority).

## 8. Full evidence IDs and citations

- Cite the tab or file plus the full `flash_evidence_row_id` (or the platform ID it wraps) for every quoted row, at least once, in an appendix lookup. Abbreviated hashes are for prose only after the full ID has been given.
- Define the row convention explicitly. `rN` = data record N = Excel row N+1 when row 1 is the header. Say so in the document.
- Run an ID resolution check before delivery: every cited ID must resolve to exactly one row in the named file. Resolution proves the citation exists; it does not validate the claim.
- Quote the person's words, not the Flash summary. Use summaries to find rows, then read the row.

## 9. Provenance of the collection itself

- Describe what a dataset is by its columns and selection, not by its filename or lane. Check dates (many are relative strings or blank), failed rows, and which sub-pull a row came from. Check the enrichment record before relying on any AI field: which pass produced it, what inputs it saw, whether the run completed, and what QA was done (`analysis_outputs/full_dataset_inventory/GEMINI_ENRICHMENT_STATUS.md`). Partial or unaudited enrichment is used for navigation only.
- The wider collection includes YouTube replay chat from streams (some are eBay break streams mirrored on YouTube). It does not include native eBay Live buyer chat or eBay transaction data unless a file is shown to contain them.
- Brand posts are excluded from community analysis; they are brand output, not audience voice.

## 10. Process

- Save a checkpoint after each dataset or major stage. Keep verified findings separate from hypotheses. When a correction lands, update every section it touches; move superseded claims to a clearly marked archive rather than leaving them in place.
- Treat prior findings as questions for the next dataset. Look for new behaviours and contradictions, not confirmation.
- No new scraping, downloads or paid model runs without explicit authorisation. Reuse saved results.
