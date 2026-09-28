"""Stage 4: renders claim_ledger.csv into the report's claim appendix and splices it into REPORT_full_collection.md
at the marker line '<!-- CLAIM_APPENDIX -->' (the marker is kept so the step can be re-run). Also writes
derived/claim_appendix.md on its own. No content is generated here: every cell comes from the ledger."""
import os, csv, re
HERE = os.path.dirname(os.path.abspath(__file__))
LED = os.path.join(HERE, "..", "claim_ledger.csv"); REP = os.path.join(HERE, "..", "REPORT_full_collection.md")
rows = list(csv.DictReader(open(LED, encoding="utf-8")))
def cell(s): return s.replace("|", "\\|").replace("\n", " ")
def ids(s):
    # one full ID per line inside the cell keeps the table readable and every ID copy-pasteable
    return "<br>".join(f"`{i.strip()}`" for i in s.split(";") if i.strip()) if s and s != "none found" else "none found"
hdr = "| Claim ID | F/H | Statement | Source file(s) | Full evidence IDs (flash_evidence_row_id) | Provenance | Calculation and denominator | Independent parent count | Speaker roles | Counterevidence (IDs) | Limitation | Status | Support check | Distinct authors behind cited rows | Shared Reddit rows cited |\n|---|---|---|---|---|---|---|--:|---|---|---|---|---|---|---|\n"
body = "".join(f"| {r['Claim ID']} | {r['F/H']} | {cell(r['Statement'])} | {cell(r['Source file(s)'])} | {ids(r['Full evidence IDs (flash_evidence_row_id)'])} | {cell(r['Provenance'])} | {cell(r['Calculation and denominator'])} | {r['Independent parent count']} | {cell(r['Speaker roles'])} | {ids(r['Counterevidence (IDs)'])} | {cell(r['Limitation'])} | {r['Status']} | {cell(r.get('Support check',''))} | {cell(r.get('Distinct authors behind cited rows',''))} | {ids(r.get('Shared Reddit rows cited','none'))} |\n" for r in rows)
intro = (f"Generated from `claim_ledger.csv` ({len(rows)} claims: {sum(r['F/H']=='F' for r in rows)} findings, {sum(r['F/H']=='H' for r in rows)} hypotheses) by `derived/stage4_render_appendix.py`. "
         "Every ID is a full `flash_evidence_row_id`; every cited row was read in this run and resolves to exactly one row in the named file (`derived/stage3_id_resolution.py`). "
         "Provenance vocabulary: source caption (creator caption and hashtags), comment text, chat message, title context, Gemini-read, AI-coded. A count that depends on Flash or Gemini labels says AI-coded. Blank metrics are unknown, not zero. Status is checker-pending for every row: nothing is verified by the checker or approved by the client. The last three columns come from `derived/stage3_claim_support_check.py`: whether a key phrase from each cited row's read window supports the claim (with notes), how many distinct creators, posters or channels stand behind the cited rows, and which cited Reddit rows exist in both Reddit files (one evidence ID each, counted once).\n\n")
app = intro + hdr + body
open(os.path.join(HERE, "claim_appendix.md"), "w", encoding="utf-8").write(app)
if os.path.exists(REP):
    t = open(REP, encoding="utf-8").read()
    marker = "<!-- CLAIM_APPENDIX -->"
    if marker in t:
        t = re.sub(re.escape(marker) + r".*?(?=\n## |\Z)", lambda m: marker + "\n" + app, t, count=1, flags=re.S)
        open(REP, "w", encoding="utf-8").write(t); print("appendix spliced into REPORT_full_collection.md")
print(f"claim_appendix.md: {len(rows)} rows")
