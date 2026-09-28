import reader as R, pandas as pd, warnings; warnings.filterwarnings("ignore")
from strat import strat
S="AB"; d=R.idx()
cl=pd.read_csv("other_emerging_rows_clustered.csv",dtype=str,keep_default_na=False)
def pick(cluster, n, sec):
    ids=set(cl[cl.cluster_first_match==cluster].evidence_id)
    c=R.sel(file=["tt_direct","tt_comm"]); c=c[c.evidence_id.isin(ids)]
    print(f"== {cluster}: unread pool {len(c)}"); R.show(S+"/"+sec, strat(c,n))
pick("Vintage and secondhand clothing / thrift", 12, "thrift/tt")
pick("Patches, pins, buttons and battle jackets", 9, "patches/tt")
pick("Physical media (Blu-ray/DVD/steelbook/VHS/CD/vinyl/books)", 9, "physmedia/tt")
pick("Automotive: parts, cars, motorcycles", 12, "pna/tt")
# P&A Reddit + YouTube
auto=r"\bcar parts?\b|auto parts?|motorcycle|\bengine\b|\boem\b|junkyard|fitment|\bturbo\b|alternator|carburet|headlight|bumper|\bhonda\b|\btoyota\b|\bbmw\b|harley"
c=R.sel(file=["rd_broad","rd_ebay","yt_titles","yt_comments"], text=auto); print("pna reddit/yt pool", len(c), c.file.value_counts().to_dict())
R.show(S+"/pna/reddit_yt", strat(c,8,col="score"), maxchars=400)
