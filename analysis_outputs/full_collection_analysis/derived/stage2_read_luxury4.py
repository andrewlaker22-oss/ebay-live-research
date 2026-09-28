import reader as R, pandas as pd, warnings; warnings.filterwarnings("ignore")
from strat import strat
S="LX"; d=R.idx()
fr=r"fragrance|perfume|cologne|parfum"
c=R.sel(file=["tt_direct","tt_comm","rd_broad","rd_ebay","yt_titles"], text=fr); print("fragrance pool", len(c), c.file.value_counts().to_dict())
R.show(S+"/fragrance", strat(c,6), maxchars=400)
vd=r"vintage (designer|chanel|gucci|dior|prada|ysl|versace|armani|burberry|moschino)|archive (fashion|piece)|designer (vintage|clothing|clothes)|raf simons|rick owens|margiela|helmut lang"
c=R.sel(file=["tt_direct","tt_comm"], text=vd); print("vintage designer pool", len(c))
R.show(S+"/vintage_designer/tt", strat(c,8))
