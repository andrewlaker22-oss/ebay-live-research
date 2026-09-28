import reader as R, pandas as pd, warnings; warnings.filterwarnings("ignore")
S="TY"; d=R.idx()
for v in ["https://www.tiktok.com/@whatnot/video/7499564422554209582","https://www.tiktok.com/@mlpkingdom/video/7641729046392392991"]:
    R.show(S+"/tt_comment_group", R.tt_comment_group(v))
for p,n in [("reddit:t3_1skd4mg",4),("reddit:t3_1txny14",4),("reddit:t3_1sap033",3),("reddit:t3_1vexsds",3)]:
    R.show(S+"/reddit_thread", R.reddit_thread(p, max_comments=n), maxchars=450)
