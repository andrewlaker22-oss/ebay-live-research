import reader as R, pandas as pd, warnings; warnings.filterwarnings("ignore")
S="CN"; d=R.idx()
for p,n in [("reddit:t3_1llzc73",8),("reddit:t3_1qcvle6",7),("reddit:t3_1vub4yy",5),("reddit:t3_1ufxb7r",5)]:
    R.show(S+"/reddit_thread", R.reddit_thread(p, max_comments=n), maxchars=500)
# remaining Coins-labelled comments not yet read
c=R.sel(file=["rd_broad","rd_ebay"], community="Coins", unit="comment"); print("unread coin-labelled comments", len(c)); R.show(S+"/coin_labelled_comments", c.head(6), maxchars=400)
