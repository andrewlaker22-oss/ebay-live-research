import reader as R, pandas as pd, warnings; warnings.filterwarnings("ignore")
from strat import strat
S="LX"; d=R.idx()
bag=r"handbag|birkin|kelly\b|chanel|louis vuitton|\blv\b|gucci|prada|hermes|hermès|purse|bag charm|coach\b|dior"
c=R.sel(file="tt_direct", text=bag); c=c[c.flash_community.str.contains("Luxury")]
print("direct handbag pool", len(c)); R.show(S+"/handbags/tt_direct", strat(c,10))
c=R.sel(file="tt_comm", text=bag); print("comm handbag pool", len(c)); R.show(S+"/handbags/tt_comm", strat(c,8))
tc=d[(d.file=="tt_comments")&(d.flash_community.str.contains("Luxury"))]
print(tc.groupby("parent_id").size().sort_values(ascending=False).head(8).to_string())
posts=R.sel(file=["rd_broad","rd_ebay"], unit="post")
lx=posts[posts.text.str.contains(bag, case=False, regex=True) | posts.flash_community.str.contains("Luxury")]
print(lx[["evidence_id","subreddit","score","date","flash_community"]].to_string())
