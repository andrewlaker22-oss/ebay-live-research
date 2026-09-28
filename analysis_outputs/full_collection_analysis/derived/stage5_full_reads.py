"""Checker handback (2026-09-28): full-text re-read of already-registered rows needed to resolve the corrections.
No new unique row is read; each ID below is already in reviewed_evidence.csv. The full read is appended to the
register under section S5/fullread with read_chars = full length, so the register records what was actually read."""
import reader as R, pandas as pd, re, warnings; warnings.filterwarnings("ignore")
IDS = ["reddit:t3_1vub4yy", "youtube_comment:UgzrDtVVH-e2hHYihvR4AaABAg", "reddit:t1_p56jodo", "reddit:t1_ocus8sv",
       "reddit:t1_njn3ck9", "reddit:t1_opkfisj", "reddit:t1_p7yaxpk", "reddit:t3_1qpssd0", "reddit:t1_n04bfny",
       "reddit:t3_1pttt05", "youtube_comment:UgzfGt8L5RoXYTzy7Ul4AaABAg", "reddit:t3_1wfp5sj", "reddit:t1_p9o48gb",
       "reddit:t1_p9ojy91", "reddit:t1_p7xb529", "reddit:t1_pa2yhrf", "reddit:t1_p50jtgt", "reddit:t1_p56yrbz",
       "reddit:t3_1s5ae92", "youtube_comment:UgxbPcydBm_M7LfisLt4AaABAg", "reddit:t1_p50mp5r", "reddit:t1_p4zsiqf"]
d = R.idx(); reg = set(R.reg().evidence_id)
missing = [i for i in IDS if i not in reg]
assert not missing, f"not registered (would be new reads): {missing}"
rows = d[d.evidence_id.isin(IDS)].drop_duplicates("evidence_id")
for i in IDS:
    r = rows[rows.evidence_id == i].iloc[0]
    t = re.sub(r"\s+", " ", r.text).strip()
    print(f"\n[{i}|{r.file}|r/{r.subreddit} score={r.score} author={r.author} date={r.date[:10]}|len={len(t)}]\n{t}")
R.show("S5/fullread", rows, maxchars=5000, note="checker handback: full text of an already-registered row")
print("BUDGET (unique IDs)", R.budget(), "/", R.CAP)
