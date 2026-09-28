import reader as R, pandas as pd, warnings; warnings.filterwarnings("ignore")
from strat import strat
S="AB"; d=R.idx()
cl=pd.read_csv("other_emerging_rows_clustered.csv",dtype=str,keep_default_na=False)
print(cl.columns.tolist()[:12]); print(cl.iloc[:,-1].value_counts().head(20) if "cluster" not in cl.columns else cl.cluster.value_counts())
