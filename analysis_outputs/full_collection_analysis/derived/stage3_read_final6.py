"""Stage 3, final reads to the 1,200 cap: unread coin-pattern rows (broad pull) and three more AG-positive YouTube comments."""
import reader as R, pandas as pd, os, warnings; warnings.filterwarnings("ignore")
C = pd.read_csv(os.path.join(R.HERE, "stage3_counterevidence_candidates.csv"), dtype=str, keep_default_na=False)
d = R.idx(); have = set(R.reg().evidence_id)
coins = d[d.evidence_id.isin(set(C[C.search=="coins"].evidence_id) - have)]
R.show("S3/coins", coins.head(3), maxchars=450)
ag = d[d.evidence_id.isin(set(C[C.search=="ag_positive_words"].evidence_id) - set(R.reg().evidence_id)) & (d.file=="yt_comments")]
R.show("S3/ag_positive_words", ag.sample(min(3, len(ag)), random_state=20260929), maxchars=450)
print("BUDGET", R.budget(), "/", R.CAP)
