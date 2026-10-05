# Handoff: Phase 1, how Whatnot took off (2019–2022)

For: the AI (or person) who will run and check this pilot. Owner: Andy. Updated: 5 October 2026 (Phase 1 rewrite; replaces the Pokémon-only pilot).
Read this whole file before doing anything. It is self-contained.

## 1. What Andy wants

Phase 1 of a phased history of live-shopping success. One question: did Whatnot succeed because it discovered a new consumer need, or because it found a better way to sell something collecting communities were already doing? It follows Whatnot's whole early story across Funko Pops, sports cards and Pokémon, and finds out which communities actually drove growth.

Later phases (not part of this run): 2 first creators and sellers who moved over; 3 TikTok LIVE; 4 niche hobby to broad shopping habit; 5 the compulsive-spending side; 6 what the behaviour looks like today; 7 people who don't shop live; 8 implications for eBay Live.

The result is for Andy's own exploration first, read in a chat window. It is not a client deliverable yet. Later it may inform eBay Live, eBay's livestream-shopping product, where Andy works on community research.

## 2. Decisions already made by Andy (do not reopen)

| Decision | Choice |
|---|---|
| Research engine | Gemini Deep Research through the Gemini API (Andy has an existing Gemini API setup) |
| Who runs it | Andy or another AI. The Claude session that wrote this did not run it and spent nothing |
| Communities | Whatnot's whole early story: Funko, sports cards, Pokémon. Replaces the earlier Pokémon-only scope (changed 5 Oct 2026) |
| Data | Public sources only. No Sensor Tower or Similarweb subscriptions |
| Output form | Plain Markdown report readable in chat |
| Budget | About $20 total for experiments. Approve any paid run before starting it |
| Phase 0 tool survey from the earlier ChatGPT chat | Dropped. Gemini was chosen, so no tool comparison is needed |
| TikTok LIVE | Background only; not investigated |

## 3. Where this came from

Andy explored the rise of Whatnot and TikTok LIVE with ChatGPT (an exported chat transcript, October 2026). Useful conclusions from that chat:
- Whatnot did not invent livestream selling. Collectors were already auctioning on Instagram Live; Whatnot added bidding, payment and shipping.
- Mass scraping (Apify) would show what is popular now, not why Whatnot took off. Historical reports, company disclosures, surveys and dated reporting are the better evidence.
- The four growth mechanisms to test: existing product demand; creator and seller relationships; platform discovery and marketing; convenience of buying inside the stream.
- eBay strategy feedback relayed by Andy's manager, Carly: deliver live content into feeds rather than expect people to visit eBay Live; grow the whole live-shopping category; check whether the current measure (viewers watching 60+ seconds) predicts buying.

Warning: the figures in that chat were never verified against original sources (the transcript says so). The prompt therefore lists them as leads L1 to L13 to verify, not as facts.

Related prior work in this repository (`andrewlaker22-oss/ebay-live-research`): a full-collection community report on eBay Live audiences (`analysis_outputs/full_collection_analysis/REPORT_full_collection.md`). Points relevant to Pokémon: hobby-side Pokémon TikTok content is opening, hit-rate and grading content with eBay almost never named (0 of 87 Pokémon-labelled community videos); audiences price-check against TCGplayer; explicit Whatnot buyers on Reddit describe fast auctions, notification pressure and impulse buying alongside a buyer who reports about 1,000 good purchases. Those findings are about 2025–2026 social posts, not 2019–2022 history; use them only as a later cross-check, not as evidence in this pilot.

## 4. Files in this folder

| File | What it is |
|---|---|
| `HANDOFF_whatnot_pokemon_pilot.md` | This document |
| `research_prompt.md` | The exact prompt sent to Gemini Deep Research. Edit here, not in the script |
| `whatnot_deep_research.py` | Python runner: starts one Deep Research task, polls it with a hard time cap, saves the report |

## 5. How to run it (Windows)

Save all three files to the Desktop (`C:\Users\andre\OneDrive\Desktop`), in the same folder.

One-time setup, in Command Prompt or PowerShell:
```
pip install -U google-genai
setx GEMINI_API_KEY "your-key-here"
```
Close that window and open a new one so the key is picked up.

Free check first (no API call, no charge):
```
cd C:\Users\andre\OneDrive\Desktop
python whatnot_deep_research.py --dry-run
```

The paid run (one Deep Research task):
```
cd C:\Users\andre\OneDrive\Desktop
python whatnot_deep_research.py
```

If the window closes or it stops checking before the report is ready, re-attach without starting or paying for a new run (the ID is saved in `last_interaction_id.txt`):
```
cd C:\Users\andre\OneDrive\Desktop
python whatnot_deep_research.py --resume PASTE_INTERACTION_ID
```

Outputs land next to the script: `whatnot_phase1_report_<timestamp>.md` (the report) and `..._raw.json` (the full API response, kept for checking sources).

Script behaviour to know:
- Agent: `deep-research-preview-04-2026`. Adding `--max` uses `deep-research-max-preview-04-2026`, which consults more sources and costs more. Use the standard agent first.
- It checks status every 20 seconds and stops checking after 70 minutes (change with `--max-minutes`). The loop always ends.
- It never retries a failed run by itself, so a failure cannot silently double the bill.

Cost: the earlier ChatGPT chat read Google's documentation as roughly $1 to $3 per standard task and $3 to $7 for Max. That was not re-verified here, and Google's pages were unreachable from this session. Before the paid run: set a spending cap or prepaid billing in Google AI Studio, turn off automatic reload, and check the actual charge in billing after the run before starting another.

## 6. Checking the report (do this before trusting it)

Deep Research can cite real pages for claims those pages do not make. Check these, in order:
1. Lead table (L1 to L13): for every row marked Verified or Corrected, open the URL and find the figure. Start with L1 to L4 (Sensor Tower), L7 to L9 (sports cards and pre-Whatnot streams) and L12 (survey, said to be page 15 of the Whatnot PDF).
2. Survey (section E): confirm the five percentages, the 3,334 sample, the July 2024 date, and whether the report says anything about why people first joined versus why current buyers keep watching.
3. Labels: every figure should say company-reported, independent, estimate or interpretation, with its denominator. Flag any "share of downloads" quietly turned into "share of shoppers", or downloads treated as sales.
4. Causation: flag any sentence saying one thing caused another where the source only shows they happened around the same time.
5. Communities: flag any named seller, creator or category claim (for example "the largest category") that is not backed by a cited source.
6. Scope creep: flag any TikTok investigation or drift past 2022 that does not show how the early pattern played out.
7. Paywalls: anything attributed to a paywalled page the agent could not have read should be marked unverifiable.

Record what you checked as a short list: claim, URL opened, what the page actually says, and the verdict (holds, corrected, unsupported).

## 7. What to hand back to Andy

In chat, plain text:
1. Two or three sentences: did Whatnot mainly capture existing collector behaviour, create new demand, or a mix, and which community drove it?
2. The lead table after your checks (Verified, Corrected, Not found, plus anything your check overturned).
3. The verdicts on the four reasons for success.
4. The top three gaps for a second phase.
5. Actual cost of the run from billing, and any script errors met.

Attach or paste the report file. Do not start Phase 2; Andy reviews first.

## 8. Known risks

- The agent IDs are preview names dated April 2026 and may be renamed. If the run fails with an unknown-agent error, check the current Deep Research model list in Google AI Studio and update `AGENT_STANDARD` at the top of the script.
- The script reads report text and best-effort citations from the API response. Citation fields differ across preview versions; if the report shows no sources, look in the `_raw.json` file.
- The script has not completed a real research run. Tested so far with google-genai 2.28.0: syntax check, dry run, the missing-key message, and a start attempt with a fake key, which reached Google's API and was rejected as an invalid key and handled without a retry. Polling and report saving have not been exercised against a real completed run. Treat the first real run as the test.
- Collaborative planning (where the agent asks you to approve its plan) is deliberately not used, so the run cannot stall waiting for approval. If the API ever returns `requires_action`, the script stops and saves the response.
