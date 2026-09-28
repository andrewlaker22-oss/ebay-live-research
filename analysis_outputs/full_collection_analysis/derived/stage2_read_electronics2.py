import reader as R, pandas as pd, warnings; warnings.filterwarnings("ignore")
from strat import strat
S="EL"; d=R.idx()
# one TikTok comment group (retrobox24 = retro tech likely; jonnyshops)
R.show(S+"/tt_comment_group", R.tt_comment_group("https://www.tiktok.com/@retrobox24/video/7442748922990218551"))
# Reddit: viral general (t3_1ojc3n1 20k), r/Ebay electronics (t3_1r91qdw 2216, t3_1rp5h81 801), r/whatnotapp electronics
for p,n in [("reddit:t3_1r91qdw",5),("reddit:t3_1rp5h81",4),("reddit:t3_1r6l7fu",4),("reddit:t3_1ojc3n1",3)]:
    R.show(S+"/reddit_thread", R.reddit_thread(p, max_comments=n), maxchars=450)
t=R.sel(file="yt_titles"); R.show(S+"/yt_titles", pd.concat([strat(t[t.lane=="cameras_electronics"],4), strat(t[t.lane=="retro_gaming"],3)]), maxchars=200)
c=R.sel(file="yt_comments"); c=c[c.lane.isin(["cameras_electronics","retro_gaming"])]; R.show(S+"/yt_comments", c.sample(8,random_state=20260928))
