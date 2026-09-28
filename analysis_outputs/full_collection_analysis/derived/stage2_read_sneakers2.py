import reader as R, pandas as pd
S="SN"; d=R.idx()
# TikTok comment groups with sneaker-labelled comments: list parents
tc=d[(d.file=="tt_comments")&(d.flash_community.str.contains("Sneakers"))]
par=tc.groupby("parent_id").size().sort_values(ascending=False)
print("sneaker-comment parents:", len(par)); print(par.head(12).to_string())
