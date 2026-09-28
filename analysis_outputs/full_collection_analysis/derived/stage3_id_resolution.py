"""ID resolution check (ANALYSIS_RULES.md section 8). Every evidence ID cited in the named documents must resolve to
exactly one row in the named source file. Handles full flash_evidence_row_id values and the abbreviated prose forms
used in the Stage 2 documents (a local_ hash prefix followed by an ellipsis, a bare Reddit t3_/t1_ id, a YouTube
comment id prefix followed by an ellipsis, a bare 11-character YouTube video id, and a chat reference video_id:offset).
Resolution proves the citation exists; it does not validate the claim.
Usage: python stage3_id_resolution.py <doc.md> [<doc2.md> ...]   (or no args: the Stage 2 and 3 documents)
Writes stage3_id_resolution_report.json next to this script and prints a summary."""
import re, sys, os, json, pandas as pd
HERE = os.path.dirname(os.path.abspath(__file__))
IDX = pd.read_csv(os.path.join(HERE, "unified_evidence_index.csv"), dtype=str, keep_default_na=False)
ALL = IDX.evidence_id.tolist()
FILE_OF = dict(zip(IDX.evidence_id, IDX.file))
CHAT = IDX[IDX.file == "yt_chat"]
YT_VIDEO_IDS = set(IDX[IDX.file.isin(["yt_titles","yt_comments","yt_chat"])].video_id)
PAT = [
 ("full", re.compile(r"\b(tiktok_video:local_[0-9a-f]{64}|tiktok_comment:\d+|reddit:t[13]_[a-z0-9]+|youtube_comment:[A-Za-z0-9_\-]{20,}|youtube_video:[A-Za-z0-9_\-]{11}|youtube_live:[A-Za-z0-9_\-]{11}:\d+)")),
 ("local_prefix", re.compile(r"(?<![:\w])(local_[0-9a-f]{6,63})(?:…|\.\.\.)")),
 ("reddit_bare", re.compile(r"(?<![:\w])(t[13]_[a-z0-9]{5,9})\b")),
 ("ytc_prefix", re.compile(r"(?<![:\w])(Ug[A-Za-z0-9_\-]{5,40})(?:…|\.\.\.)")),
 ("chat_ref", re.compile(r"(?<![:\w])([A-Za-z0-9_\-]{11}):(\d{1,4})\b")),
 ("yt_video_bare", re.compile(r"(?<![:\w/=])([A-Za-z0-9_\-]{11})(?![:\w])")),
]
def resolve(kind, tok):
    if kind == "full":
        m = [tok] if tok in FILE_OF else []
    elif kind == "local_prefix":
        m = [i for i in ALL if i.startswith("tiktok_video:" + tok)]
    elif kind == "reddit_bare":
        m = [i for i in ALL if i == "reddit:" + tok]
    elif kind == "ytc_prefix":
        m = [i for i in ALL if i.startswith("youtube_comment:" + tok)]
    elif kind == "chat_ref":
        # prose form video_id:N refers to the chat evidence ID youtube_live:<video_id>:<chat_row>
        m = [i for i in ALL if i == "youtube_live:" + tok]
    elif kind == "yt_video_bare":
        m = [i for i in ALL if i == "youtube_video:" + tok] or ([f"stream:{tok}"] if tok in YT_VIDEO_IDS else [])
    # the 39 Reddit rows shared by the broad and r/Ebay pulls carry one evidence ID in two files: one evidence row
    return sorted(set(m))
def run(docs):
    report = {"documents": {}, "totals": {"tokens": 0, "unique_tokens": 0, "resolved_unique": 0, "ambiguous": 0, "unresolved": 0}}
    seen = {}
    for doc in docs:
        text = open(doc, encoding="utf-8").read()
        found = {}
        for kind, rx in PAT:
            for mm in rx.finditer(text):
                tok = mm.group(1) if kind != "chat_ref" else mm.group(1) + ":" + mm.group(2)
                if kind == "yt_video_bare" and (tok in found or not any(ch.isdigit() for ch in tok) or tok.lower() == tok and "_" not in tok and "-" not in tok):
                    continue  # skip ordinary words; a bare YouTube id must contain a digit, a hyphen/underscore or mixed case
                if kind == "yt_video_bare" and not (tok in YT_VIDEO_IDS):
                    continue
                found.setdefault(tok, kind)
        rows = []
        for tok, kind in found.items():
            m = seen.get(tok) or resolve(kind, tok); seen[tok] = m
            status = "resolved" if len(m) == 1 else ("ambiguous" if len(m) > 1 else "unresolved")
            files = sorted(set(IDX[IDX.evidence_id == m[0]].file)) if len(m) == 1 else []
            rows.append({"token": tok, "kind": kind, "status": status, "matches": m[:5], "file": "+".join(files), "shared_reddit_row": len(files) > 1})
        st = {"tokens": len(rows), "resolved": sum(r["status"]=="resolved" for r in rows), "ambiguous": sum(r["status"]=="ambiguous" for r in rows), "unresolved": sum(r["status"]=="unresolved" for r in rows)}
        report["documents"][os.path.basename(doc)] = {"summary": st, "problems": [r for r in rows if r["status"] != "resolved"], "rows": rows}
        print(f"{os.path.basename(doc)}: {st}")
        for r in rows:
            if r["status"] != "resolved": print("   ", r["status"], r["kind"], r["token"], r["matches"][:3])
    allrows = {r["token"]: r for dd in report["documents"].values() for r in dd["rows"]}
    report["totals"] = {"unique_tokens": len(allrows), "resolved_unique": sum(r["status"]=="resolved" for r in allrows.values()), "ambiguous": sum(r["status"]=="ambiguous" for r in allrows.values()), "unresolved": sum(r["status"]=="unresolved" for r in allrows.values())}
    print("TOTALS", report["totals"])
    json.dump(report, open(os.path.join(HERE, "stage3_id_resolution_report.json"), "w"), indent=1)
    return report
if __name__ == "__main__":
    base = os.path.join(HERE, "..")
    docs = sys.argv[1:] or [os.path.join(base, f) for f in ["stage2_provisional.md", "stage2_notes_running.md"]]
    run(docs)
