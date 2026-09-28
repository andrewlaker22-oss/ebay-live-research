"""Stage 2 read script: Sneakers/Streetwear. Seeded, bounded, local only."""
import reader as R, pandas as pd
S="SN"
d=R.idx()
# candidates: label OR keyword in source text
kw=r"sneaker|jordan|yeezy|dunk|nike|adidas|new balance|streetwear|supreme|stockx|goat\b|air max|samba"
# TikTok direct: sample 14 across views (stratify low/high)
c=R.sel(file="tt_direct", community="Sneakers/Streetwear")
lo=c.assign(v=pd.to_numeric(c.views,errors="coerce")).sort_values("v")
R.show(S+"/tt_direct", pd.concat([lo.head(40).sample(6,random_state=1), lo.tail(40).sample(4,random_state=2), lo.iloc[40:-40].sample(4,random_state=3)]).drop(columns="v"))
# UK/DE stated sneaker rows in direct pull
uk=R.sel(file=["tt_direct","tt_comm"], text=r"(?i)\b(uk|london|manchester|germany|deutschland|berlin|anzeige)\b")
uk=uk[uk.flash_community.str.contains("Sneakers")]
R.show(S+"/tt_market_stated", uk.head(6), note="market term in caption")
# TikTok community
c=R.sel(file="tt_comm", community="Sneakers/Streetwear")
lo=c.assign(v=pd.to_numeric(c.views,errors="coerce")).sort_values("v")
R.show(S+"/tt_comm", pd.concat([lo.head(40).sample(5,random_state=1), lo.tail(30).sample(4,random_state=2), lo.iloc[40:-30].sample(3,random_state=3)]).drop(columns="v"))
