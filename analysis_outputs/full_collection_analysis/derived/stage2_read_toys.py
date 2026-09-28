import reader as R, pandas as pd, warnings; warnings.filterwarnings("ignore")
from strat import strat
S="TY"; d=R.idx()
subs={
 "blindbox":r"blind box|labubu|pop ?mart|sonny angel|smiski|designer toy|skullpanda|hirono|crybaby|molly\b|dimoo|bearbrick|be@rbrick|kaws",
 "action_figures":r"action figure|figure\b|figures\b|funko|hot toys|neca|mcfarlane|gi joe|g\.i\. joe|transformers|marvel legends|star wars",
 "trains":r"\btrain(s)?\b|lionel|hornby|märklin|marklin|ho scale|n scale|model railway|model railroad|bachmann",
 "vintage_lines":r"vintage toy|80s toy|90s toy|polly pocket|my little pony|cabbage patch|barbie|hot wheels|matchbox|lego|beanie bab|tamagotchi|furby",
 "plush":r"plush|plushie|squishmallow|jellycat|build-a-bear|stuffed animal",
}
for k,pat in subs.items():
    c=R.sel(file=["tt_direct","tt_comm"], text=pat)
    c=c[c.flash_community.str.contains("Toys") | (k=="trains")]
    n={"blindbox":9,"action_figures":7,"trains":9,"vintage_lines":8,"plush":4}[k]
    print(f"== {k}: pool {len(c)} (direct {int((c.file=='tt_direct').sum())}, comm {int((c.file=='tt_comm').sum())})")
    R.show(S+"/"+k+"/tt", strat(c,n))
tc=d[(d.file=="tt_comments")&(d.flash_community.str.contains("Toys"))]
print(tc.groupby("parent_id").size().sort_values(ascending=False).head(8).to_string())
posts=R.sel(file=["rd_broad","rd_ebay"], unit="post"); ty=posts[posts.flash_community.str.contains("Toys")|posts.text.str.contains(subs["blindbox"]+"|"+subs["trains"]+"|funko|lego", case=False, regex=True)]
print(ty[["evidence_id","subreddit","score","date","flash_community"]].to_string())
