import reader as R, pandas as pd
S="SN"; d=R.idx()
for v in ["https://www.tiktok.com/@luh.sneakerheads/video/7681421897799617806","https://www.tiktok.com/@murphyr3ps/video/7663598993603169558"]:
    R.show(S+"/tt_comment_group", R.tt_comment_group(v), note="parent+comments")
# Reddit: sneaker-labelled posts (broad + rEbay) and keyword posts
posts=R.sel(file=["rd_broad","rd_ebay"], unit="post")
sn=posts[posts.flash_community.str.contains("Sneakers") | posts.text.str.contains(r"sneaker|jordan|yeezy|dunk|stockx|goat\b", case=False, regex=True)]
print("sneaker reddit posts:", len(sn)); print(sn[["evidence_id","subreddit","score","flash_community"]].to_string())
