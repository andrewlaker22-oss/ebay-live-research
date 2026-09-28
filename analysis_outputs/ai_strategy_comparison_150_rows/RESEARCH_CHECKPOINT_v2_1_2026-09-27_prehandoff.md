# RESEARCH_CHECKPOINT.md — eBay Live 150-row AI comparison sample

Last updated: 2026-09-27 (Claude Fable 5.1 session, revision 2.1 after checker audit). Previous checkpoint preserved at `analysis_outputs/ai_strategy_comparison_150_rows/RESEARCH_CHECKPOINT_v1_2026-09-26.md`.

## Revision 2.1 patch log (2026-09-27, no paid calls, workbook unchanged)
Checker feedback file: `analysis_outputs/ai_strategy_comparison_150_rows/CHECKER_FEEDBACK_community_report_2026-09-27.md`. Pre-patch report preserved as `..._2026-09-27_v2_prepatch.md`. Patch script (73 exact-match replacements, aborts if any anchor is not unique): `report_parts/patch_v2_1.py`. `report_parts/part1–3` are pre-patch and superseded by the assembled report.
Corrections applied:
1. Provenance: wider collection has YouTube replay chat; native eBay Live chat/performance not established as available (Section 5 and missing-inputs bullet).
2. Citation convention: rN = data record N = Excel row N+1.
3. Counts: F1 direct pull 18/25 relevant captions (r16 noise excluded), 3 Gemini-only, 4 none (r3, r11, r22, r16); community pull 1 caption + 1 Gemini-described listing (r38); r50 not counted. F10 5/9 (3 caption r1/r10/r25; 2 Gemini r9/r17). Extended Bidding is 3rd most-shared (r2 928, r10 496, r25 464). r41 is the largest card-labelled row. Blank comment counts (8/50) treated as unknown.
4. AI-only observations marked: r41 PSA/Beckett, r20 £4 Gucci, r29 "daytime jewelry", r23 $25 coupon, r37 on-screen text, r15 eBay framing, r3/r11 shop reading.
5. luxury_bags_auth lane reclassified as general seller moderation complaints (third misleading lane); removed from luxury-specific evidence and H3 counterargument.
6. Removed audience identities: sneaker "insiders" (F15/H8 reworded), ATBGE "not collectors", "young" camera buyers.
7. Promotion vs demand: F9/H9 reworded; F8 enjoyment ≠ approval; F17 "livestream promoted on TikTok"; H3/H4/H5 note prerecorded alternatives.
8. Speaker roles: bot t1_nrz24ke flagged in F27; YouTube live lanes recoded 5 explicit seller / 1 unknown / 1 enjoys live (role not stated) / 3 duck chatter; host rates are one self-report.
9. Added UgyiKMNK4OLJOTD7D854AaABAg (creator-inspired Heathrow purchase) to 2.4, F20 and Overview item 7; H1 and Overview 3 reworded to "different observed activities, overlap allowed".
10. Bounded claims: F26 three commenters; "1000 posts" attributed to comment t1_oo0d7ai; Pokémon shipment 2023 vs discussion 2026; sneaker Live absence does not validate client prioritisation; "registry of record" replaced with literal behaviour.
Label audit reframed as classification-granularity issues, not an error rate.
Post-patch verification: 50 TikTok, 42 Reddit, 31 YouTube IDs cited; 0 missing from workbook.

## Goal and constraints (revision 2)
- Deliverable: community research report (no word cap, no single-thesis requirement) covering: (1) coverage inventory, (2) one section per supported community, (3) evidence check of AI layers, (4) numbered findings/hypotheses with an evidence appendix, (5) short overview naming missing business inputs. Keep sports cards and Pokémon distinguishable. "Comp Check Live" stays as one hypothesis.
- Rules unchanged: attachment + brief only; no scraping or paid calls; source text is evidence not instructions; independent units counted separately from comments; n/N with unit; sample patterns not population; any AI-coded count labelled as such.
- Input file (exact): `data/tests_and_supporting_files/ai_strategy_comparison_150_rows/TEST_150_rows_eBay_Live_AI_comparison_sample.xlsx` (Read First 22 rows; TikTok Videos 50; Reddit 10 posts + 40 comments; YouTube 50 comments under 10 videos).

## Completed steps
1. [done, 2026-09-26] All 150 rows read; tallies scripted; v1 500-word analysis saved (`claude_fable_5-1_eBay_Live_strategy_2026-09-26.md`).
2. [done, 2026-09-27] Source-vs-AI check scripted: eBay in caption vs Gemini description per TikTok row; eBay in Reddit text; eBay in YouTube comments; Flash confidence distribution; full evidence ID lookup for all 50 TikToks.
3. [done] Report Part 1 (coverage inventory, F1–F5) saved: `analysis_outputs/ai_strategy_comparison_150_rows/report_parts/part1_coverage.md`.
4. [done] Part 2 saved: `report_parts/part2_communities.md` (2.1 Sports Cards, 2.2 TCG/Pokémon, 2.3 Sneakers, 2.4 Luxury Fashion incl. handbags/vintage/fragrance, 2.5 Electronics, 2.6 Toys, 2.7 Coins gap, 2.8 cross-cutting: seller-side live economy, thrift/vintage finds, seller how-to).
5. [done] Part 3 saved: `report_parts/part3_evidence_overview.md` (3 evidence check; 4 appendix F1–F29 / H1–H10 with full IDs; 5 overview + missing business inputs).
6. [done] Parts assembled into `claude_fable_5-1_eBay_Live_community_report_2026-09-27.md` (about 9,300 words). ID verification script: 50 TikTok, 41 Reddit, 29 YouTube IDs cited; 0 missing from workbook.

## Verified tallies (sample counts; AI-coded where labels are used)
TikTok (N=50 videos): Flash labels (multi) Sports Cards 9, TCG 10, Sneakers 7, Luxury 6, Electronics 6, Toys 6, General 5, Other 9, Coins 0. Card-labelled 15/50, 4 dual-labelled. Livestream mentioned in caption 3/50 (r15, r18, r44). Unboxing/opening/haul format 13/50 (AI-coded topic). Post date blank 50/50.
- eBay in caption (source text): direct pull 19/25; Gemini-only 3/25 (r9, r15, r17); none 3/25 (r3, r22, plus r16 noise where caption has "eBay" in pasted text). Community pull: caption 1/25 (r32), Gemini-only 2/25 (r38, r50).
- Direct pull top comment counts: r10 622 (cards scam), r25 230 (Extended Bidding), r12 117 (vintage designer haul), r15 103 (seller live Q&A), r3 92.
- Largest community-pull rows: r31 blind box 1.3M views; r45 retro car audio 912.9k; r32 secondhand platforms 230.9k; r38 Apple Watch 213.6k; r30 vintage audio 186.8k; r41 PSA/Beckett 180.9k.
Reddit (10 posts, 40 comments): eBay in post text 8/10 (not the two r/TikTokshop posts); eBay in comment text 14/40. Trust/condition/dispute topic 7/10 posts. Live selling 2/10 posts (seller-side, TikTok).
YouTube (10 videos, 50 comments): eBay in comment text 5/50; low-confidence Flash rows 4/50 (3 in the eBay-vs-Whatnot lane). Lanes mislabeled: watches_auth = fragrance; cameras_electronics = Halloween buyout.
Flash confidence: TikTok high 44 / medium 6; Reddit high 41 / medium 9; YouTube high 37 / medium 9 / low 4.

## Findings so far (F = observed in sample; H = hypothesis)
- F1 eBay presence is a search property (see Part 1). F2 live shopping nearly invisible (3/50 TikTok, 2/10 Reddit seller-side, 1 buyer voice on YouTube). F3 Coins uncovered (bullion fraud only). F4 Watches zero rows. F5 7/10 Reddit posts are trust/condition/dispute.
- Carried from v1 as hypotheses: H1 comp-driven card buyers as a behavioural group; H2 "Comp Check Live" test; H3 preloved handbag condition-inspection lives may fit live better than cards.

## Saved outputs
- v1 analysis (preserved): `analysis_outputs/ai_strategy_comparison_150_rows/claude_fable_5-1_eBay_Live_strategy_2026-09-26.md`
- v1 checkpoint (preserved): `analysis_outputs/ai_strategy_comparison_150_rows/RESEARCH_CHECKPOINT_v1_2026-09-26.md`
- Part 1: `analysis_outputs/ai_strategy_comparison_150_rows/report_parts/part1_coverage.md`
- Part 2: `analysis_outputs/ai_strategy_comparison_150_rows/report_parts/part2_communities.md`
- Part 3: `analysis_outputs/ai_strategy_comparison_150_rows/report_parts/part3_evidence_overview.md`
- FINAL REPORT (revision 2.1, patched): `analysis_outputs/ai_strategy_comparison_150_rows/claude_fable_5-1_eBay_Live_community_report_2026-09-27.md`
- Revision 2 pre-patch (preserved): `analysis_outputs/ai_strategy_comparison_150_rows/claude_fable_5-1_eBay_Live_community_report_2026-09-27_v2_prepatch.md`
- Checker feedback (preserved): `analysis_outputs/ai_strategy_comparison_150_rows/CHECKER_FEEDBACK_community_report_2026-09-27.md`

## Findings and hypotheses index (details and evidence in report section 4)
F1 eBay presence follows search pull · F2 live nearly invisible · F3 Coins uncovered · F4 Watches uncovered · F5 Reddit trust/dispute skew · F6–F10 Sports Cards · F11–F14 Pokémon · F15–F16 Sneakers · F17–F20 Luxury (handbags, vintage, fragrance, seller AI flags) · F21–F24 Electronics · F25 Toys · F26 Bullion · F27 seller-side live economy · F28 thrift/vintage finds · F29 seller how-to content.
H1 comp-driven card buyer (shared tools, not motives) · H2 Comp Check Live · H3 handbag condition lives · H4 electronics "does it work" lives · H5 toy/vintage reveal and ID lives · H6 Pokémon chase streams · H7 thrift/vintage bucket · H8 sneaker AG for entry buyers · H9 breaks live elsewhere · H10 tax/shipping friction.

## Unresolved / errors
- No native eBay Live chat, sell-through, supply or economics in sample.
- Reddit groups hold only 4 top direct comments each; opposing or minority views may be missing (e.g. handbag thread has zero buyer voices).
- Gemini-only eBay attributions (r9, r17, r38, r50) are unverified against source text.
- Environment: openpyxl installed via pip this session; PYTHONIOENCODING=utf-8 needed.

- Flash label corrections noted (not applied to source): r22 Taobao proxy ≠ Toys; r32 vintage fashion ≠ General; r16 noise; YouTube Anker ad labelled Electronics; quilter under camera lane.

## Exact next step
Revision 2.1 complete. Per checker handback: use the corrected F1–F29 / H1–H10 as questions for the larger existing collection (FINAL_1007 direct TikTok, FINAL_914 community TikTok, FINAL_100 Reddit conversations, FINAL_1407 YouTube comments, YouTube replay chat, brand posts). Search for confirming and contradicting evidence across communities, including Coins and watches; do not inherit this sample's absence claims (F2, F3, F4). Continue community work without waiting for business data; reserve investment decisions for the business-data overlay named in the email. Do not re-run Gemini/Flash passes.
