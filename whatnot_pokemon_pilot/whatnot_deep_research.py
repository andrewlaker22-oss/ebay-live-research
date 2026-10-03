"""
whatnot_deep_research.py
Runs ONE Gemini Deep Research task for the Whatnot / Pokemon livestream-shopping pilot and saves the report.

What it does
  1. Reads research_prompt.md from the same folder as this script.
  2. Starts one background Deep Research interaction (this is the step that costs money).
  3. Saves the interaction ID immediately, so a crash never loses a paid run.
  4. Checks the status every 20 seconds, for at most --max-minutes (default 70). The loop always ends.
  5. Saves the final report as Markdown plus the raw API response as JSON, both next to this script.

Setup (Windows, once)
  pip install -U google-genai
  setx GEMINI_API_KEY "your-key-here"      (then open a NEW terminal so the key is visible)

Run
  cd C:\\Users\\andre\\OneDrive\\Desktop
  python whatnot_deep_research.py --dry-run          (free: shows the prompt and settings, calls nothing)
  python whatnot_deep_research.py                    (starts one paid run)
  python whatnot_deep_research.py --resume <ID>      (free to check: re-attaches to a run already started)

Safety
  - One run per execution. It never retries a failed run on its own.
  - The status loop has a hard cap on how many times it checks, so it cannot run forever.
  - Network hiccups are tolerated up to 5 in a row, then it stops and prints the resume command.
"""

import argparse
import datetime as dt
import json
import os
import sys
import time

AGENT_STANDARD = "deep-research-preview-04-2026"
AGENT_MAX = "deep-research-max-preview-04-2026"
POLL_SECONDS = 20
MAX_CONSECUTIVE_ERRORS = 5
HERE = os.path.dirname(os.path.abspath(__file__))
PROMPT_FILE = os.path.join(HERE, "research_prompt.md")
DONE_STATES = {"completed"}
STOP_STATES = {"failed", "cancelled", "canceled", "incomplete", "requires_action"}


def stamp():
    return dt.datetime.now().strftime("%Y%m%d_%H%M%S")


def log(msg):
    print(f"[{dt.datetime.now().strftime('%H:%M:%S')}] {msg}", flush=True)


def load_prompt():
    if not os.path.exists(PROMPT_FILE):
        sys.exit(f"Cannot find {PROMPT_FILE}. Put research_prompt.md in the same folder as this script.")
    with open(PROMPT_FILE, encoding="utf-8") as f:
        text = f.read().strip()
    if len(text) < 200:
        sys.exit("research_prompt.md looks empty or truncated. Check the file.")
    return text


def get_client():
    try:
        from google import genai
    except ImportError:
        sys.exit("The google-genai package is missing. Run:  pip install -U google-genai")
    if not (os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")):
        sys.exit("No API key found. Run:  setx GEMINI_API_KEY \"your-key\"  then open a new terminal.")
    client = genai.Client()
    if not hasattr(client, "interactions"):
        sys.exit("Your google-genai version has no Interactions API. Run:  pip install -U google-genai")
    return client


def to_jsonable(obj):
    for attr in ("model_dump", "to_dict", "dict"):
        fn = getattr(obj, attr, None)
        if callable(fn):
            try:
                return fn()
            except Exception:
                pass
    return {"repr": repr(obj)}


def extract_report(interaction):
    """Return (report_text, citation_lines). Citations are best effort: field names vary across preview versions."""
    outputs = getattr(interaction, "outputs", None) or []
    texts = [getattr(o, "text", None) for o in outputs]
    texts = [t for t in texts if t]
    report = texts[-1] if texts else ""
    cites = []
    for o in outputs:
        for field in ("annotations", "citations", "sources"):
            for a in getattr(o, field, None) or []:
                url = getattr(a, "url", None) or getattr(a, "uri", None) or (a.get("url") if isinstance(a, dict) else None)
                title = getattr(a, "title", None) or (a.get("title") if isinstance(a, dict) else None)
                if url:
                    line = f"- {title or 'source'}: {url}"
                    if line not in cites:
                        cites.append(line)
    return report, cites


def save_outputs(interaction, agent, started_at):
    base = os.path.join(HERE, f"whatnot_pokemon_report_{stamp()}")
    report, cites = extract_report(interaction)
    header = (
        f"<!-- Gemini Deep Research | agent: {agent} | interaction: {getattr(interaction, 'id', '?')} | "
        f"started: {started_at} | saved: {dt.datetime.now().isoformat(timespec='seconds')} -->\n\n"
    )
    with open(base + ".md", "w", encoding="utf-8") as f:
        f.write(header + (report or "(No report text was returned. Check the JSON file.)"))
        if cites:
            f.write("\n\n## Sources returned by the API\n\n" + "\n".join(cites) + "\n")
    with open(base + "_raw.json", "w", encoding="utf-8") as f:
        json.dump(to_jsonable(interaction), f, indent=2, default=str)
    usage = getattr(interaction, "usage", None)
    log(f"Report saved:  {base}.md")
    log(f"Raw response:  {base}_raw.json")
    if usage:
        log(f"Usage reported by the API: {usage}")
    log(f"Report length: {len(report.split())} words; API-listed sources: {len(cites)}")


def poll(client, interaction_id, agent, started_at, max_minutes):
    max_checks = max(1, int(max_minutes * 60 / POLL_SECONDS))
    errors = 0
    last_status = None
    for check in range(1, max_checks + 1):
        try:
            interaction = client.interactions.get(interaction_id)
            errors = 0
        except Exception as e:
            errors += 1
            log(f"Status check failed ({errors}/{MAX_CONSECUTIVE_ERRORS}): {e}")
            if errors >= MAX_CONSECUTIVE_ERRORS:
                log("Too many errors in a row. The run may still be going on Google's side.")
                log(f"Resume later (no new charge):  python whatnot_deep_research.py --resume {interaction_id}")
                return 2
            time.sleep(POLL_SECONDS)
            continue
        status = str(getattr(interaction, "status", "unknown")).lower()
        if status != last_status:
            log(f"Status: {status}")
            last_status = status
        elif check % 15 == 0:
            log(f"Still {status} ({check * POLL_SECONDS // 60} min elapsed)")
        if status in DONE_STATES:
            save_outputs(interaction, agent, started_at)
            return 0
        if status in STOP_STATES:
            log(f"The run ended with status '{status}'. Error detail: {getattr(interaction, 'error', None)}")
            with open(os.path.join(HERE, f"whatnot_pokemon_FAILED_{stamp()}_raw.json"), "w", encoding="utf-8") as f:
                json.dump(to_jsonable(interaction), f, indent=2, default=str)
            log("Raw response saved for diagnosis. Nothing was retried automatically.")
            return 1
        time.sleep(POLL_SECONDS)
    log(f"Stopped checking after {max_minutes} minutes. The run may still finish on Google's side.")
    log(f"Resume later (no new charge):  python whatnot_deep_research.py --resume {interaction_id}")
    return 3


def main():
    ap = argparse.ArgumentParser(description="Run one Gemini Deep Research task for the Whatnot/Pokemon pilot.")
    ap.add_argument("--dry-run", action="store_true", help="Show the prompt and settings without calling the API.")
    ap.add_argument("--max", action="store_true", help="Use the Deep Research Max agent (more sources, costs more).")
    ap.add_argument("--resume", metavar="INTERACTION_ID", help="Re-attach to a run that was already started.")
    ap.add_argument("--max-minutes", type=float, default=70, help="How long to keep checking (default 70).")
    args = ap.parse_args()

    agent = AGENT_MAX if args.max else AGENT_STANDARD
    prompt = load_prompt()

    if args.dry_run:
        print(prompt)
        print("\n" + "-" * 60)
        log(f"DRY RUN. Agent: {agent}. Prompt: {len(prompt.split())} words. Check limit: {args.max_minutes} min.")
        log("No API call was made and nothing was charged.")
        return 0

    client = get_client()
    started_at = dt.datetime.now().isoformat(timespec="seconds")

    if args.resume:
        log(f"Re-attaching to interaction {args.resume} (no new run is started).")
        return poll(client, args.resume, agent, started_at, args.max_minutes)

    log(f"Starting ONE paid Deep Research run with agent {agent}.")
    try:
        interaction = client.interactions.create(input=prompt, agent=agent, background=True)
    except Exception as e:
        log(f"Could not start the run: {e}")
        log("Check the agent name, your API key, and that billing is enabled. Nothing was retried.")
        return 1
    interaction_id = interaction.id
    id_file = os.path.join(HERE, "last_interaction_id.txt")
    with open(id_file, "w", encoding="utf-8") as f:
        f.write(f"{interaction_id}\n{agent}\n{started_at}\n")
    log(f"Run started. Interaction ID: {interaction_id} (saved to last_interaction_id.txt)")
    log("Deep Research usually takes 5 to 30 minutes. You can close this window and resume later with --resume.")
    return poll(client, interaction_id, agent, started_at, args.max_minutes)


if __name__ == "__main__":
    sys.exit(main())
