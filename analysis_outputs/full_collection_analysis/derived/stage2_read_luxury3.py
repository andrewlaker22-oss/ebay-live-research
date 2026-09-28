import reader as R, pandas as pd, warnings; warnings.filterwarnings("ignore")
from strat import strat
S="LX"; d=R.idx()
# handbags YouTube lane
t=R.sel(file="yt_titles"); t=t[t.lane=="luxury_bags_auth"]; R.show(S+"/handbags/yt_titles", strat(t,5), maxchars=200)
c=R.sel(file="yt_comments"); c=c[c.lane=="luxury_bags_auth"]; R.show(S+"/handbags/yt_comments", c.sample(7,random_state=20260928))
# watches
w=r"\bwatch(es)?\b|rolex|omega|seiko|tudor|cartier|patek|chrono24"
c=R.sel(file=["tt_direct","tt_comm"], text=w); c=c[~c.text.str.contains(r"watch (the|this|full|my|our|till|until|to)|watch out|watching|watch me|watch how|watch as|watch what|watch you|watch it|watch a ", case=False, regex=True)]
print("watch tiktok pool", len(c)); R.show(S+"/watches/tt", strat(c,8))
for p,n in [("reddit:t3_1vweez9",7),("reddit:t3_1p7d9qr",6),("reddit:t3_1tz0dbm",4),("reddit:t3_1oqfzzy",3)]:
    R.show(S+"/watches/reddit_thread", R.reddit_thread(p, max_comments=n), maxchars=450)
t=R.sel(file="yt_titles"); t=t[t.lane=="watches_auth"]; R.show(S+"/watches/yt_titles", strat(t,4), maxchars=200)
c=R.sel(file="yt_comments"); c=c[c.lane=="watches_auth"]; R.show(S+"/watches/yt_comments", c.sample(7,random_state=20260928))
