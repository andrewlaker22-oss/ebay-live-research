HANDOFF FOR THE NEXT CHAT (written 5 Oct 2026)

WHO AND WHAT
- User: Andy (they/them). Works on eBay Live community research (eBay x VaynerMedia). Andy's manager is Carly.
- Repo: andrewlaker22-oss/ebay-live-research, branch main-3dv76t, PR #1 open. Everything below is committed there.
- Standing preferences:
  1. Never give code that can loop forever; every loop must end.
  2. Python files go to C:\Users\andre\OneDrive\Desktop. Always give the run commands as:
       cd C:\Users\andre\OneDrive\Desktop
       python <file>.py
  3. Lead with context and the main question, then item by item. Don't drift into micro-details (see the repurposer skill).

THE MAIN LENS (every piece of work must serve this)
eBay is pushing Live top-down: ad campaign, homepage, notifications, Promoted Stores ads to Live pages. Whatnot and TikTok LIVE scaled behaviour that already existed in communities. For each community:
- Q1. Is live buying already happening there, and on which platform?
- Q2. Who drives it: creators, sellers, partners?
- Q3. Is there an opening for eBay Live, or is eBay pushing into empty space?
Phase anchor question: did Whatnot and TikTok LIVE succeed by discovering a new consumer need, or by finding a better way to sell something communities were already doing? What does that mean for eBay Live?

Carly's strategy points (from eBay Live's "10 reasons" Slack thread):
- People may not go looking for live shopping, so deliver live content into feeds they already use.
- Grow the whole live-shopping category, not just win existing live shoppers.
- Check whether the current measure (viewers watching 60+ seconds) predicts buying.
Andy's view: this doesn't negate their point about top-down vs bottom-up.

THE PHASES (Andy chose to start with Phase 1)
- Phase 0: research-tool survey. Dropped; Gemini was chosen, now replaced by Claude doing the research.
- Phase 1: How Whatnot took off (2019–2022). Did it capture existing collector behaviour or create new demand? Covers Funko Pops (the start), sports cards (reportedly the largest early category) and Pokémon. Tests the four reasons: existing demand; creators and sellers bringing audiences; discovery and marketing; buying inside the stream (bidding, payment, shipping, trust). IN PROGRESS.
- Phase 2: The first creators and sellers who moved over. Card breakers, Instagram Live auctioneers, YouTube pack openers. Did they bring audiences, or did Whatnot create new stars? Whatnot reportedly recruited respected community sellers.
- Phase 3: How TikTok LIVE turned attention into income. Gifting, battles, NPC streams, then TikTok Shop U.S. in 2023. When did attention become money, and when did selling join it?
- Phase 4: From niche hobby to broad shopping habit. Whatnot spread into sneakers, food, wholesale and 35+ categories. Did each category bring its own community, or did existing buyers cross over? This is the parallel to eBay Live entering cameras and luxury.
- Phase 5: The downside story. Compulsive spending, fast auctions, notification pressure (Reddit buyers; WSJ, Aug 2026). Keeps the success story honest and tells eBay what not to copy.
- Phase 6: What the behaviour looks like today. The current TikTok/Reddit community work belongs here, used to test what the history found, not to count captions with no story.
- Phase 7: People who don't shop live. Is the barrier discovery or lack of interest? Interviews with three groups: live shoppers, watched-but-never-bought, never tried. Does 60+ seconds of watching predict bidding or buying (needs eBay analytics)?
- Phase 8: What it means for eBay Live. Where eBay can capture existing behaviour (cards, via creator partners) vs where it would have to create the habit (cameras); top-down vs bottom-up.

PHASE 1: WHERE IT STANDS
- Prompt: whatnot_pokemon_pilot/research_prompt.md, rewritten as Phase 1 (whole Whatnot story; answer first; leads L1–L13). Also usable as a Gemini Deep Research prompt via whatnot_deep_research.py (one run, 20s polling, 70-min cap, --dry-run / --max / --resume, never retries). Handoff: whatnot_pokemon_pilot/HANDOFF_whatnot_pokemon_pilot.md.
- Andy then said: "I want you [Claude] to do the research for phase one. I give up on ChatGPT." So the next chat should do Phase 1 research itself, following research_prompt.md.
- Blocker: the cloud environment's network allowlist blocked direct page reads (sensortower.com, techcrunch.com, en.wikipedia.org, research.contrary.com, web.archive.org, blog.teamwhatnot.com, si.com). Only WebSearch summaries worked. Andy is changing Network access to Full (or Custom with those domains). First step next chat: test WebFetch on https://sensortower.com/blog/live-stream-shopping-2022. If it is still blocked, tell Andy and either continue on search summaries (marking each fact "seen via search summary only") or ask them to start a new session.

Findings so far (from search summaries; NOT yet verified on the original pages):
- Founded 2019 by Grant LaFontaine and Logan Head as a Funko Pop resale marketplace (YC).
- First livestream (2020): half the founders' Funko collection listed as buy-it-now, half sold live. The live half sold out in about 2.5 hours for about $5,000. LaFontaine had seen Disney pin collectors running auctions on Instagram Live, a platform ill-equipped for bidding and payment.
- Dec 2020: $4M seed (Scribble, Wonder, YC). TechCrunch title: "Whatnot raises $4M as it gets into livestreamed auctions and Pokémon cards" (techcrunch.com/2020/12/17/...). Pokémon arrived alongside live auctions.
- Mar 2021: $20M Series A led by Connie Chan (a16z), TechCrunch 4 Mar 2021. Planned new categories: comics, vintage video games.
- May 2021: $50M Series B led by YC Continuity (Anu Hariharan), TechCrunch 25 May 2021. Sports-card sales up 80x since that category launched at the start of 2021, with "millions of dollars in monthly sales" from live breaks. $75M raised in total. Press release calls Whatnot "the largest live shopping platform in the US".
- Sensor Tower, June 2022: Whatnot had a 35% share of downloads among the top U.S. live-shopping apps (Jan–May 2022). Top apps had 2.3M installs, up 77% year over year. Whatnot's ad spend was $3.8M Jan–May 2022, up 414% from $739K.
- Breaking (box breaks) grew during COVID in 2020–21 as hobby shops sold opened product to stream viewers and live sports paused (Wikipedia "Breaking (trading cards)").
- Early read: Whatnot captured existing collector behaviour (Instagram Live auctions, box breaks) and fixed the buying mechanics, then poured money into ads. Confirm before stating it.

Still to research for Phase 1:
- Sept 2021 Series C (about $150M, unicorn; "30x" claim; sports cards the largest category?).
- Sports Illustrated, May 2020, on card-opening livestreams.
- The Pokémon boom timeline (2020–21: Logan Paul, Target pausing card sales in May 2021, etc.).
- Competitors that existed then (Loupe, PopShop Live, etc.) and why Whatnot won.
- Seller recruitment.
- Whatnot's 2024 State of Livestream Selling report: survey July 2024, n=3,334, with 66/53/46/43/21%. Page 15? Does it explain first joining or only continued watching?
- EMARKETER: 43% of U.S. adults never used live shopping and not interested (Aug 2024); 21.7% of digital buyers.
- Whatnot's Jan 2026 letter: about $3B in 2024, $8B+ in 2025 GMV; marketing up 10x; new buyers up 285%.
- Fortune, 7 Aug 2026: "100 investor rejections... $20 billion".
Output format and leads table are in research_prompt.md: answer first, then timeline, the four reasons, the communities, eBay implications, leads table, gaps, source log.

SKILLS
- repurposer (created this chat; .claude/skills/repurposer/SKILL.md, plus a .skill package Andy can install). Use it whenever reviewing another AI's work or giving feedback.
  1. Find the main lens: restate the user's 1–3 main questions in their own words.
  2. Read each item through the lens: which question does it serve, what is the "so what", is it drift? Drift means precision that wouldn't change the answer, caveats outweighing findings, side topics, polish before the answer, or answering an adjacent question.
  3. Write in this order:
     - CONTEXT FIRST: main questions; where the work is aimed vs where it should be; 2–4 global changes.
     - ITEM BY ITEM, in the work's order: Serves Q? / So what / Fix (or Cut) / Test.
     - CLOSE: "Answers so far" per question, plus the single next step.
     Be direct about misdirection, credit the strongest item, keep micro-fixes out, match length to the work. If the feedback is for pasting to another AI, address it to "You".
- Other relevant skills: anthropic-skills:ebay-live-community-research, anthropic-skills:social-video-collect-and-tag, anthropic-skills:deep-research, anthropic-skills:pptx, anthropic-skills:skill-creator.

HISTORY OF THIS CHAT (condensed)
1. Finished Stages 3 and 4 of the eBay Live full-collection community research, all checker-pending, in analysis_outputs/full_collection_analysis/:
   - REPORT_full_collection.md (v2)
   - OVERVIEW_full_collection.md (leads with a per-community table)
   - claim_ledger.csv (54 claims)
   - stage3_evidence_checks.md (corrections C1–C40)
   - RESEARCH_CHECKPOINT.md v11
   Rules: ANALYSIS_RULES.md v2 (provenance, denominators, speaker roles, promotion is not demand, 1,200-row reading ceiling).
2. Applied the checker's corrections: the coin poster was an observer, not a buyer; watch and ring rows were mis-filed; "supported" was renamed to a phrase check; parent counts fixed; the overview no longer leads with risks.
3. Stopped GitHub check-ins at Andy's request.
4. Read Andy's ChatGPT chat export (37-page PDF) on the rise of Whatnot and TikTok LIVE. Built a Gemini Deep Research pilot (prompt, script, handoff). Decisions: Gemini, public data only, about $20 budget, output in chat.
5. Reviewed another AI's collector dashboard (v1 → v3 QA template); judged v3 "good enough" as a QA gate.
6. Explained Carly's "10 reasons" for eBay Live.
7. Reviewed the four-hypotheses deck. Lesson: give context first ("aimed at the wrong target"), then slide by slide. This led to the repurposer skill.
8. Reviewed "eBay_collector_pilot_Live_questions_REVISED_v3" (5 slides: card breaks; Fanatics Live partners; cameras, where TikTok Shop posts take 70.9% of views and 0/49 captions mention live; G7X alternatives; answers so far). Verdict: framed on Q1–Q3 but aimed at what 50 captions say, not where live buying happens.
   - Strongest slide: Fanatics Live paying hobby creators, with eBay Live absent.
   - Biggest underplayed finding: camera buying happens via TikTok Shop video, not live.
   - Next step: look at the live platforms directly.
9. Andy disliked the direction and asked for the phases to be rewritten around history and success. Phases 1–8 above were listed; Andy picked Phase 1. The prompt was rewritten and pushed.
10. Andy asked Claude to do Phase 1 research itself. Research started, hit the network block, and Andy is fixing access.

NEXT STEP
Confirm web access. Then run Phase 1 research per research_prompt.md:
- 10–15 sources; verify leads L1–L13 on the original pages.
- Deliver in chat, answer first.
- Save the report as whatnot_pokemon_pilot/PHASE1_report.md and commit to main-3dv76t.
- Don't start Phase 2 until Andy reviews.
