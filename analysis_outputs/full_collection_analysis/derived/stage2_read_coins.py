import reader as R, pandas as pd, warnings; warnings.filterwarnings("ignore")
from strat import strat
S="CN"; d=R.idx()
num=r"\bcoins?\b|numismat|bullion|silver eagle|morgan dollar|gold coin|\bpcgs\b|\bngc\b|challenge coin|coin collect"
c=R.sel(file=["tt_direct","tt_comm","yt_titles"], text=num); print("tt/yt coin pool", len(c)); R.show(S+"/tt_yt", c, maxchars=300)
posts=R.sel(file=["rd_broad","rd_ebay"], unit="post"); cp=posts[posts.flash_community.str.contains("Coins")|posts.text.str.contains(num,case=False,regex=True)]
print(cp[["evidence_id","subreddit","score","date","flash_community"]].to_string())
