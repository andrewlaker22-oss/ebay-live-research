import reader as R, pandas as pd, warnings; warnings.filterwarnings("ignore")
from strat import strat
S="AB"; d=R.idx()
# Nurse Flipper Q&A stream id
nf=d[(d.file=="yt_chat")&(d.video_title.str.contains("Reseller Q&A",case=False,na=False))].video_id.unique(); print("nurse flipper stream", nf)
R.show(S+"/sellerlive/chat_nonhost", R.chat_slice(nf[0], n=14, nonhost_only=True, contiguous=True), maxchars=250)
c=d[(d.file=="yt_chat")&(d.video_id==nf[0])&(d.unit=="chat_message")&((d.is_owner.str.lower()=="true")|(d.is_moderator.str.lower()=="true"))]
R.show(S+"/sellerlive/chat_host", c.sample(3,random_state=20260928), maxchars=250, note="host/mod")
# eBay Live named in Reddit source text (unread)
c=R.sel(file=["rd_broad","rd_ebay"], text=r"ebay ?live"); print("unread reddit ebay-live rows", len(c)); R.show(S+"/sellerlive/reddit_ebaylive", strat(c,8,col="score"), maxchars=450)
# r/TikTokshop thread
posts=R.sel(file="rd_broad", unit="post"); ts=posts[posts.subreddit=="TikTokshop"]; print(ts[["evidence_id","score","date"]].to_string())
