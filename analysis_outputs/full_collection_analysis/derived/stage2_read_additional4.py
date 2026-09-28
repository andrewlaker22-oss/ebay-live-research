import reader as R, pandas as pd, re, warnings; warnings.filterwarnings("ignore")
from strat import strat
S="AB"; d=R.idx()
for i in ["reddit:t3_1pttt05","reddit:t1_omuylg3","reddit:t1_ocus8sv"]:
    print(i, "FULL:", re.sub(r"\s+"," ",d[d.evidence_id==i].iloc[0].text)[:1500]); print()
for p,n in [("reddit:t3_1wfp5sj",5),("reddit:t3_1pttt05",4),("reddit:t3_1ph5dqy",5)]:
    R.show(S+"/sellerlive/reddit_thread", R.reddit_thread(p, max_comments=n), maxchars=450)
t=R.sel(file="yt_titles"); t=t[t.lane.isin(["tiktok_shop_live","whatnot_vs_ebay_live"])]; R.show(S+"/sellerlive/yt_titles", strat(t,5), maxchars=200)
c=R.sel(file="yt_comments"); c=c[c.lane.isin(["whatnot_vs_ebay_live","tiktok_shop_live"])]; R.show(S+"/sellerlive/yt_comments", c.sample(6,random_state=20260928))
