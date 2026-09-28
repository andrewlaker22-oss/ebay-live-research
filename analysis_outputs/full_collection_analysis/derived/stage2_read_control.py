import reader as R, pandas as pd, warnings; warnings.filterwarnings("ignore")
ctrl=pd.read_csv("control_sample_100.csv",dtype=str,keep_default_na=False)
d=R.idx(); rows=d[d.evidence_id.isin(ctrl.evidence_id)]
already=set(R.reg().evidence_id); print("control rows already read in routed sections:", len(set(ctrl.evidence_id)&already))
for f in ["tt_direct","tt_comm","tt_comments","rd_broad","rd_ebay","yt_titles","yt_comments","yt_chat"]:
    R.show("CONTROL/"+f, rows[rows.file==f], maxchars=220, note="control")
