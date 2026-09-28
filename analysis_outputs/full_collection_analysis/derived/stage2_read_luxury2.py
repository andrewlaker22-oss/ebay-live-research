import reader as R, pandas as pd, warnings; warnings.filterwarnings("ignore")
S="LX"; d=R.idx()
# handbag Reddit: r/handbags x2, r/Ebay luxury posts (mix high/low score)
for p,n in [("reddit:t3_1sbzdvx",5),("reddit:t3_1shwwz7",5),("reddit:t3_1oe3rv0",6),("reddit:t3_1tvx3x9",6),("reddit:t3_1uuzsyt",3),("reddit:t3_1w7wp8u",3)]:
    R.show(S+"/handbags/reddit_thread", R.reddit_thread(p, max_comments=n), maxchars=450)
# TikTok comment group: isobellorna (2026)
R.show(S+"/handbags/tt_comment_group", R.tt_comment_group("https://www.tiktok.com/@isobellorna_/video/7647481702427708694"))
