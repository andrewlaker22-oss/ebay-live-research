"""Sampling plan for the bounded reading run. Seed 20260928.
Control: 100 rows total, stratified by dataset, drawn from rows OUTSIDE the keyword screen used for routed selection
(live/whatnot/tiktok shop/authentic/fake/scam/break/rip-n-ship/ebay live) and outside the seven client-community labels
where possible (Other/General/Unclear preferred; falls back to any row if a stratum is short). Chat system/error rows,
duplicate r/Ebay rows and host/moderator chat rows are excluded from the control pool."""
import pandas as pd, json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
d = pd.read_csv(os.path.join(HERE, "unified_evidence_index.csv"), dtype=str, keep_default_na=False)
d = d[~d["dedup_drop"].isin(["True","true"])]
d = d[~d["unit"].isin(["chat_system","chat_error","chat_membership","chat_super_chat"])]
SEED = 20260928
KEY = r"\blive\b|livestream|whatnot|tiktok ?shop|authentic|counterfeit|\bfake\b|\bscam|\bbreaks?\b|rip.?n.?ship|ebay ?live|fanatics"
SEVEN = ["Sports Cards","TCG/Pokemon","Sneakers/Streetwear","Luxury Fashion","Electronics","Toys/Collectibles","Coins"]
def labels(s): return [x.strip() for x in s.split(";") if x.strip()]
pool = d[~d["text"].str.contains(KEY, case=False, regex=True, na=False)]
pool = pool[~((pool.file=="yt_chat") & ((pool.is_owner.str.lower()=="true")|(pool.is_moderator.str.lower()=="true")))]
STRATA = {"tt_direct":15,"tt_comm":15,"tt_comments":10,"rd_broad":20,"rd_ebay":10,"yt_titles":8,"yt_comments":12,"yt_chat":10}
picked = []
for f, n in STRATA.items():
    sub = pool[pool.file==f]
    outside = sub[~sub.flash_community.apply(lambda s: any(c in labels(s) for c in SEVEN))]
    take = outside.sample(n=min(n, len(outside)), random_state=SEED)
    if len(take) < n:
        extra = sub[~sub.evidence_id.isin(take.evidence_id)].sample(n=n-len(take), random_state=SEED)
        take = pd.concat([take, extra])
    picked.append(take.assign(control_stratum=f, outside_seven_labels=take.evidence_id.isin(outside.evidence_id)))
ctrl = pd.concat(picked)
ctrl[["evidence_id","file","unit","parent_id","control_stratum","outside_seven_labels","flash_community"]].to_csv(os.path.join(HERE,"control_sample_100.csv"), index=False)
# overlap with the partial enrichment control (10 completed rows)
enr = os.path.join(os.environ.get("EBAY_ROOT","."), "enrichment_v2_20260927","FOR_FABLE","03_CONTROL_ENRICHMENT.jsonl")
enr_ids = []
if os.path.exists(enr):
    enr_ids = [json.loads(l)["evidence_id"] for l in open(enr, encoding="utf-8") if l.strip()]
plan = {"seed": SEED, "cap_unique_rows": 1200, "control_reserve": 100, "control_strata": STRATA,
        "control_keyword_screen": KEY, "control_pool_size": int(len(pool)), "control_selected": int(len(ctrl)),
        "control_outside_seven_labels": int(ctrl.outside_seven_labels.sum()),
        "overlap_with_enrichment_control_completed_rows": sorted(set(enr_ids) & set(ctrl.evidence_id)),
        "routed_reading_plan_by_dataset": {
            "tt_direct": 190, "tt_comm": 160, "tt_comments": 110, "rd_broad": 300, "rd_ebay": 90,
            "yt_titles": 90, "yt_comments": 150, "yt_chat": 110},
        "routed_selection_rule": "Per community section: candidate rows = label-routed rows (AI-coded) UNION keyword hits in source text; "
                                 "deduplicated; seeded random sample within candidates with deliberate inclusion of low-view/low-score rows, "
                                 "contradicting keyword hits, parent/context rows and every dataset that has candidates. Not most-liked-first.",
        "read_definition": "A row counts as read only when its source text was printed and read in this run (register: reviewed_evidence.csv). "
                           "Text longer than the print limit (350 chars for comments/chat/captions, 900 for posts/titles context) is marked truncated."}
json.dump(plan, open(os.path.join(HERE,"sampling_plan.json"),"w"), indent=2)
print(json.dumps(plan, indent=2))
print(ctrl.groupby(["control_stratum","outside_seven_labels"]).size())
