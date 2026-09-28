"""Seeded view-stratified sampler over a candidate frame: low / mid / high thirds by views (or score)."""
import pandas as pd
def strat(c, n, col="views", seed=20260928):
    if len(c)<=n: return c
    v=pd.to_numeric(c[col],errors="coerce").fillna(-1)
    c=c.assign(_v=v).sort_values("_v")
    k=len(c)//3
    parts=[c.iloc[:k], c.iloc[k:2*k], c.iloc[2*k:]]
    per=[n//3, n//3, n-2*(n//3)]
    out=[p.sample(min(m,len(p)),random_state=seed) for p,m in zip(parts,per)]
    return pd.concat(out).drop(columns="_v")
