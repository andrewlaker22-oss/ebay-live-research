# Checker feedback: full-collection report, PR 1 (received 2026-09-28)

Snapshot reviewed: `738003cd18a3ca39eccdd2fbe4f48b281c58d6e6`. PR: https://github.com/andrewlaker22-oss/ebay-live-research/pull/1. Saved here verbatim as the record of the targeted independent check; the handback corrections are logged as C29–C40 in `stage3_evidence_checks.md` and applied in the v2 deliverables.

## Verdict

Useful provisional community research, with a substantially better structure than the original single-community thesis. Not yet cleared for client use. Make the focused corrections below; do not restart the analysis, expand the sample, or launch paid processing.

This is a targeted independent check, not certification of all 54 claims. I inspected the report/overview, the seven priority claims, underlying source records and selected related hypotheses, counting/support scripts, and the client-call/email framing. I did not watch videos or verify commenters' allegations externally.

## What independently checks out

- The eight local source CSVs contain 8,339 distinct evidence IDs, consistent with the 8,378-row inventory and 39 reused Reddit records.
- The review register has 1,200 unique IDs (1,229 entries including repeated registrations).
- The claim ledger contains 54 claims. Its supporting citations contain 292 unique source IDs; including counterevidence gives 303. All 303 resolve in the local source collection and appear in the review register.
- Source-text searches reproduce 51 eBay Live matches: 22 direct TikTok captions, 13 YouTube titles, 10 broad-Reddit rows, 5 YouTube comments and 1 additional r/Ebay row. These are literal-pattern matches, not an exhaustive count of Live experiences.
- The authentication search reproduces 297 matching rows. This is a keyword count, not a count of verified authentication experiences or a sentiment rate.
- The substantive mixed-AG finding is supported: source records include reported protective interventions and complaints. The watch section includes genuine first-person buyer and seller accounts on both sides.

## Required corrections, highest priority first

### 1. Correct the main Live-buyer claim and preserve mixed evidence

Affected: XC-F1, CN-F2, AB-SL-F1; report sections 2, 3.7, 3.8.5; overview opening and numbers table.

`reddit:t3_1vub4yy` describes entering and WATCHING a coin stream, tracking seven auctions and comparing prices. The writer never says they bought or bid. Their hope of finding a deal does not establish a purchase. Do not count this as one of four explicit buyers or call it the clearest buyer narrative.

Within the four accounts currently cited, three describe a purchase/order and one describes observation. This is a correction to that selected set, not proof there are exactly three buyers in the whole collection.

Read the COMPLETE existing row `youtube_comment:UgzrDtVVH-e2hHYihvR4AaABAg`. The writer eventually won the card and says the host was nice and answered every question, despite criticizing the queue and auction timing. Preserve both parts: a reported purchase, helpful seller interaction, and platform friction. The current register records only 320 characters, before that resolution.

Also distinguish the unsuccessful bidder `reddit:t1_p56jodo` from purchasers. Do not treat every non-host as a buyer or infer seller identity from r/Ebay membership. `reddit:t1_ocus8sv` explicitly says "high-use seller" but the ledger calls the role unknown; several other complaining commenters do not explicitly establish a seller role.

Suggested summary: "The reviewed material contains a small number of first-person Live experiences, including three cited purchase/order accounts and one coin-stream observer. These describe friction; the card buyer also reports winning the item and a helpful host. This selection cannot establish overall buyer sentiment."

The coin poster's percentage wording is ambiguous. Do not convert it into a precise verified markup. Prefer "the observer believed quoted prices were substantially above recent sold listings." The report also misdescribes the cleaned-coin complaint as about price versus sold comps in section 5; that row is about condition/grading disclosure and return handling.

### 2. Fix seller-to-buyer inversion in the UK Pokemon hypothesis

Affected: PK-H2 and its speaker-role field; related Pokemon recommendations.

`reddit:t1_njn3ck9` says: "We need this for UK/so we can sell high value items in peace."

This is seller-oriented demand for protection, not an explicit UK buyer asking for reassurance. Keep it as one commenter expressing a UK seller need. It does not independently establish present UK program availability, buyer demand, or demand for a Live format. Do not recommend a consumer message implying a service is available without verification.

### 3. Keep handbag evidence separate from watches and jewelry

Affected: XC-F2, handbag section 3.4.1, cross-cutting section 4.1 and relevant ledger entries.

- `reddit:t1_opkfisj` explicitly concerns a WATCH: "they will get the money and the watch."
- `reddit:t1_p7yaxpk` belongs to a Tiffany-ring seller thread, as the report itself notes.

Neither establishes a handbag-specific AG dispute. Move these to watches/jewelry or explicitly label them adjacent luxury evidence. Do not describe handbag Reddit sentiment as balanced between these two examples.

Retain actual handbag evidence: `youtube_comment:UgwAqcvWStAcfOH6nl94AaABAg` explicitly mentions buying two LV purses; `reddit:t1_ofgfyui` discusses handbag vetting. The wallet account `reddit:t3_1qpssd0` reports what a subsequent buyer said eBay found, not independently verified counterfeit detection. Keep that attribution.

### 4. Rename the automated support result and check full text only where needed

Affected: overview opening, report appendix description, support-check column and checkpoint claims of verification.

The support script checks author-specified phrases against saved read windows. That verifies phrase presence, not whether the inference, identity, category or causal claim is correct. The errors above passed it.

Of the 303 cited/supporting-or-counterevidence IDs, 87 have a truncated-read flag in the register. This does not make all 87 findings wrong, but "303 supported claims/rows" overstates the test.

Rename the mechanical result "citation/phrase check passed; substantive review pending." Preserve separate substantive checker status. For report-bearing claims involving experience, outcome or sentiment, retrieve the full existing cited record and necessary parent context. Re-reading an already registered ID does not consume another unique-row slot. Do not commission an exhaustive new pass.

Avoid claims such as "no positive account exists in these pulls" based only on literal-pattern searches and clipped records. Use "none established in the reviewed evidence" with the search scope. Likewise, native chat/transaction data is not the ONLY possible source of buyer experience; these social accounts already provide self-reported experiences. First-party data is needed to establish performance, not to permit any buyer research at all.

### 5. Reconcile parent counts and the break-video comparison

The ledger contains internally inconsistent parent totals. Using source post IDs and video IDs on supporting citations:

| Claim | Correct independent source parents | Inconsistency |
|---|---:|---|
| PK-F2 | 9 | Parent field says 9; calculation prose says 10 |
| LX-W-F1 | 7 | Parent field says 7; calculation prose says 10 |
| AB-SL-F1 | 8 | Parent field says 8; calculation prose says 12 |
| TY-F2 | 1 | Parent field says 2; video and its comments are the same parent |
| TY-H1 | 1 | Same TikTok parent counted as 2 |

Generate these figures once from canonical parent keys and reuse them in all renderings. Independent parents do not necessarily mean independent creators or audiences.

SC-F2's ten eBay-named break videos have the stated 26-1,317 view range and four channels. However, the six entertainment videos actually cited (three TRIKE, three Wayne Collection) have 46,992-542,529 views, not 19,754-542,529. The 19,754 endpoint belongs to `youtube_video:S1NuE_wA2Bs`, an additional Wayne Collection title not in that six-video comparison. Either use the cited six consistently or explicitly redefine and cite the comparison set; do not add fresh reading to patch a convenient endpoint.

These titles differ in age, channel and format. Keep the view ranges descriptive, not evidence that prerecorded entertainment is inherently better than live commerce. A title naming "eBay break" does not by itself verify checkout destination or simultaneous native eBay Live broadcasting; qualify those inferences.

### 6. Synchronize the overview with the corrected report

The overview still says all nine untagged eBay Live captions are seller/host announcements; the report already recognizes one hashtag-only row and a pricing-tool ad. Keep those distinct and avoid guessing the hashtag-only author's role.

The overview says every proposed route starts with the seller/creator handle, while the report has @eBayLive-led watch/coin examples and an @eBay comparison. Choose a route per proposal and label it proposed, not observed. Respect the client's core-handle starting direction without imposing one route on all communities.

Do not state "no AG at all" for bullion as a verified policy fact from these comments. This review did not verify current program rules. Phrase it as an evidence limitation or an attributed complaint.

## Client alignment: improve the overview, not the research scope

The client's call asks for community behavior, platform roles, content examples and the division between eBay, sellers and creators. The email asks how those findings can inform investment once business data is available. The report now broadly follows that structure and appropriately does not force a winning community or dedicated handle.

The OVERVIEW still leads with Live complaints and authentication risks. That makes a community-research assignment read like a service-problems audit. Keep those risks, but lead with the community behaviors already supported in the report.

Replace the opening list with a compact community summary. For each starting category plus Coins, give:
- The relevant subcommunity and the behavior/motivation observed.
- One concrete existing content example with a source link/ID.
- A provisional content idea, proposed maker (eBay/seller/creator), platform role and route into Live where justified.
- The main limitation or contradictory evidence.

Do not turn this into seven promises of opportunity. Thin Coins evidence remains a scoped gap. Keep seller concerns distinct from shopper motivations. Use likes, questions and listing saves as diagnostic signals; each shopping test should also name a downstream outcome where measurable, such as referred Live visits and completed purchases, without inventing baselines or thresholds.

The report can offer a conditional action menu without ranking total investment from social data alone. Business inputs should decide scale; they should not become an excuse to stop at a list of unanswered questions. No new collection is needed to make this presentation change.

## Bounded handback to Fable

Apply these corrections to the report, overview, ledger and checkpoint, preserving pre-patch files and appending the correction log. Reuse existing source IDs. Read complete versions only of the cited records needed to resolve the issues above. No new unique-row expansion, video processing, model call or collection is requested.

Re-render the appendix from the corrected ledger. Run mechanical ID/quote/count checks, but label them accurately. Return a short change log and final paths. Keep unreviewed claims provisional. Do not claim this targeted checker review cleared all 54 claims.

Do not spend additional turns monitoring the PR as a substitute for finishing the corrections. This feedback has been saved locally; the checker has not posted it to GitHub, merged the PR, or modified Fable's report.
