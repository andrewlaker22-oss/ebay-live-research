"""Stage 3 counterevidence reads (<=85 new unique rows, seed 20260928). Priority order below; each batch is a
seeded sample from the unread hits of the named search in stage3_counterevidence_search.py, choosing across
files where the pool spans several. Every printed row is registered in reviewed_evidence.csv under S3/<search>."""
import reader as R, pandas as pd, os, warnings; warnings.filterwarnings("ignore")
from strat import strat
C = pd.read_csv(os.path.join(R.HERE, "stage3_counterevidence_candidates.csv"), dtype=str, keep_default_na=False)
d = R.idx()
def pool(search):
    ids = set(C[C.search == search].evidence_id) - set(R.reg().evidence_id)
    return d[d.evidence_id.isin(ids)]
def pick(search, n, per_file=None, seed=20260928):
    p = pool(search)
    if per_file:
        parts = []
        for f, k in per_file.items():
            q = p[p.file == f]
            parts.append(q if len(q) <= k else q.sample(k, random_state=seed))
        p = pd.concat(parts)
    elif len(p) > n:
        p = p.sample(n, random_state=seed)
    return p.head(n)
plan = [
 ("comm_captions_ebay", 8, None, 400),
 ("ebay_live_unpaid", 9, None, 500),
 ("whatnot_buyer", 7, None, 500),
 ("live_buyer", 6, None, 500),
 ("blindbox_ebay_live", 1, None, 400),
 ("trains_ebay_live", 3, None, 400),
 ("other_tcg", 6, None, 400),
 ("fanatics", 1, None, 400),
 ("panini", 7, {"tt_comm": 4, "yt_titles": 2, "rd_broad": 1}, 400),
 ("memorabilia", 6, {"tt_direct": 2, "tt_comm": 1, "rd_broad": 1, "rd_ebay": 1, "yt_comments": 1}, 400),
 ("de", 8, {"tt_direct": 4, "tt_comm": 2, "rd_broad": 1, "yt_comments": 1}, 400),
 ("ag_positive_words", 12, {"rd_broad": 4, "rd_ebay": 3, "yt_comments": 3, "tt_direct": 2}, 450),
 ("ebay_praise", 9, {"tt_direct": 3, "yt_comments": 3, "rd_broad": 2, "rd_ebay": 1}, 400),
 ("coins", 2, {"rd_ebay": 2}, 450),
]
for search, n, per_file, mc in plan:
    rows = pick(search, n, per_file)
    print(f"\n=== S3/{search}: {len(rows)} rows ===")
    R.show("S3/" + search, rows, maxchars=mc)
print("BUDGET", R.budget(), "/", R.CAP)
