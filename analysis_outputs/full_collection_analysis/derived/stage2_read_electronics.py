import reader as R, pandas as pd, warnings; warnings.filterwarnings("ignore")
from strat import strat
S="EL"; d=R.idx()
cam=r"camera|camcorder|point and shoot|film camera|dslr|canon|nikon|fujifilm|sony a|cybershot"
c=R.sel(file="tt_direct", text=cam); print("direct camera pool",len(c)); R.show(S+"/cameras/tt_direct", strat(c,8))
retro=r"retro|vintage tech|ipod|walkman|gameboy|game boy|nintendo|ps2|ps1|n64|crt|vhs|minidisc|flip phone|nokia|blackberry"
c=R.sel(file="tt_comm", text=retro); c=c[c.flash_community.str.contains("Electronics")]; print("comm retro pool",len(c)); R.show(S+"/retro/tt_comm", strat(c,8))
c=R.sel(file="tt_direct", community="Electronics"); c=c[~c.text.str.contains(cam+"|"+retro, case=False, regex=True)]
print("direct other electronics pool",len(c)); R.show(S+"/mainstream_parts/tt_direct", strat(c,8))
tc=d[(d.file=="tt_comments")&(d.flash_community.str.contains("Electronics"))]
print(tc.groupby("parent_id").size().sort_values(ascending=False).head(6).to_string())
posts=R.sel(file=["rd_broad","rd_ebay"], unit="post"); el=posts[posts.flash_community.str.contains("Electronics")]
print(el[["evidence_id","subreddit","score","date","flash_community"]].to_string())
