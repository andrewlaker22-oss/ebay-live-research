import reader as R, pandas as pd
S="SN"; d=R.idx()
for p,n in [("reddit:t3_1tbjxra",8),("reddit:t3_1nzw8nl",6),("reddit:t3_1s8y9k4",4),("reddit:t3_1q53zhu",4)]:
    R.show(S+"/reddit_thread", R.reddit_thread(p, max_comments=n), maxchars=500)
# YouTube sneakers_auth lane titles + comments
t=R.sel(file="yt_titles"); t=t[t.lane=="sneakers_auth"]
R.show(S+"/yt_titles", t.sample(min(8,len(t)),random_state=20260928), maxchars=200)
c=R.sel(file="yt_comments"); c=c[c.lane=="sneakers_auth"]
R.show(S+"/yt_comments", c.sample(12,random_state=20260928))
