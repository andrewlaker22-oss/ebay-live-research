"""Quote provenance check: every double-quoted phrase in stage2_provisional.md (and optionally other documents) is
searched, whitespace-normalised and case-insensitive, in the source text of rows in the reading register. Phrases
with an ellipsis are split and each part must appear in the same row. Output: stage3_quote_check.json and a summary.
A miss means the quote could not be matched to a registered row's source text (paraphrase, typo, or drawn from a
non-source field) and must be checked by hand before it is reused."""
import re, os, sys, json, pandas as pd
HERE = os.path.dirname(os.path.abspath(__file__))
IDX = pd.read_csv(os.path.join(HERE, "unified_evidence_index.csv"), dtype=str, keep_default_na=False)
REG = pd.read_csv(os.path.join(HERE, "..", "reviewed_evidence.csv"), dtype=str, keep_default_na=False)
rows = IDX[IDX.evidence_id.isin(set(REG.evidence_id))].drop_duplicates("evidence_id")
def norm(s): return re.sub(r"\s+", " ", s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')).strip().lower()
texts = {r.evidence_id: norm(r.text) for r in rows.itertuples()}
ALL_TEXT = {r.evidence_id: norm(r.text) for r in IDX.itertuples()}
GEM = {r.evidence_id: norm(r.gemini_ad_description) for r in IDX.itertuples() if r.gemini_ad_description}
def check(doc):
    text = open(doc, encoding="utf-8").read().replace("“", '"').replace("”", '"')
    # a quoted phrase: on one line, starting with a word character, and not a prose fragment between two citations
    quotes = [q for q in re.findall(r'"([^"\n]{10,300})"', text)
              if re.match(r"[\w$#@¿¡]", q) and not re.search(r"\(t[13]_|local_[0-9a-f]{6}|\[caption\]|\[comment\]|\[post\]", q)]
    res = []
    for q in quotes:
        parts = [norm(p) for p in re.split(r"…|\.\.\.|\[\.\.\.\]", q) if norm(p)]
        reg_hits = [eid for eid, t in texts.items() if all(p in t for p in parts)]
        any_hits = reg_hits or [eid for eid, t in ALL_TEXT.items() if all(p in t for p in parts)]
        gem_hits = [] if any_hits else [eid for eid, t in GEM.items() if all(p in t for p in parts)]
        status = "registered" if reg_hits else ("unregistered_row" if any_hits else ("gemini_field" if gem_hits else "MISS"))
        res.append({"quote": q[:140], "parts": len(parts), "status": status, "matched_rows": (reg_hits or any_hits or gem_hits)[:3]})
    n = len(res); m = sum(r["status"] == "registered" for r in res)
    print(f"{os.path.basename(doc)}: {n} quoted phrases, {m} matched to a registered row's source text, {n-m} not matched")
    for r in res:
        if r["status"] != "registered": print(f"   {r['status']}: {r['quote'][:110]} {r['matched_rows'][:2]}")
    return res
if __name__ == "__main__":
    docs = sys.argv[1:] or [os.path.join(HERE, "..", "stage2_provisional.md")]
    out = {os.path.basename(d): check(d) for d in docs}
    json.dump(out, open(os.path.join(HERE, "stage3_quote_check.json"), "w"), indent=1)
