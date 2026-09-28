"""Stage 1: verify counts, build a unified evidence index, coverage table and Other/emerging profile.
Counting and grouping only. No model calls, no edits to source files.
Run from the project root (paths below are relative to it)."""
import pandas as pd, json, re, os, sys
from collections import Counter

ROOT = os.environ.get("EBAY_ROOT", ".")
FIN = os.path.join(ROOT, "finalized")
OUT = os.path.join(ROOT, "analysis_outputs", "full_collection_analysis", "derived")
os.makedirs(OUT, exist_ok=True)

FILES = {
 "tt_direct":  "FINAL_1007_direct_eBay_TikTok_videos_Flash_Batch_communities_topics.csv",
 "tt_comm":    "FINAL_914_community_TikTok_videos_Flash_Batch_communities_topics.csv",
 "tt_comments":"FINAL_500_TikTok_comments_50_videos_Flash_Batch_communities_topics.csv",
 "rd_broad":   "FINAL_100_Reddit_conversations_1998_comments_Flash_Batch_communities_topics.csv",
 "rd_ebay":    "FINAL_137_rEbay_posts_632_comments_Flash_Batch_communities_topics.csv",
 "yt_titles":  "FINAL_248_YouTube_video_titles_Flash_Batch_communities_topics.csv",
 "yt_comments":"FINAL_1407_YouTube_comments_Flash_Batch_communities_topics.csv",
 "yt_chat":    "FINAL_1435_YouTube_live_chat_rows_Flash_Batch_communities_topics.csv",
}
COMMUNITIES = ["Sports Cards","TCG/Pokemon","Sneakers/Streetwear","Luxury Fashion","Electronics",
               "Toys/Collectibles","Coins","Other / emerging","General marketplace","Unclear"]

def load(k):
    return pd.read_csv(os.path.join(FIN, FILES[k]), dtype=str, keep_default_na=False)

D = {k: load(k) for k in FILES}
ver = {}

# ---- 1. counts and unique IDs
for k, df in D.items():
    ver[k] = {"rows": len(df), "unique_ids": df["flash_evidence_row_id"].nunique()}

# ---- 2. cross-file duplicates (Reddit)
shared = set(D["rd_broad"]["flash_evidence_row_id"]) & set(D["rd_ebay"]["flash_evidence_row_id"])
ver["reddit_shared_ids"] = len(shared)
rb = D["rd_ebay"]
ver["reddit_shared_posts"] = int(rb[rb.flash_evidence_row_id.isin(shared) & (rb.row_type=="post")].shape[0])
ver["reddit_shared_comments"] = int(rb[rb.flash_evidence_row_id.isin(shared) & (rb.row_type=="comment")].shape[0])
all_ids = pd.concat([df["flash_evidence_row_id"] for df in D.values()])
ver["total_rows"] = int(len(all_ids)); ver["total_unique_ids"] = int(all_ids.nunique())

# ---- 3. TikTok comment parents
tc = D["tt_comments"]
d_links = set(D["tt_direct"]["link"]); c_links = set(D["tt_comm"]["link"])
pv = tc["video_url"].unique()
ver["tt_comment_parent_videos"] = len(pv)
ver["tt_comment_parents_in_direct"] = sum(1 for v in pv if v in d_links)
ver["tt_comment_parents_in_comm"] = sum(1 for v in pv if v in c_links)
ver["tt_direct_comm_link_overlap"] = len(d_links & c_links)

# ---- 4. YouTube joins
yv = set(D["yt_titles"]["video_id"]); yc = D["yt_comments"]
ver["yt_comment_videos"] = yc["video_id"].nunique()
ver["yt_comment_videos_in_titles"] = len(set(yc["video_id"]) & yv)
ch = D["yt_chat"]
ver["chat_video_ids"] = ch["video_id"].nunique()
ver["chat_overlap_with_titles"] = len(set(ch["video_id"]) & yv)
ver["chat_event_types"] = dict(Counter(ch["event_type"]))
msgs = ch[ch.event_type=="message"]
ver["chat_messages"] = len(msgs)
ver["chat_owner_or_mod_messages"] = int(((msgs.is_owner.str.lower()=="true")|(msgs.is_moderator.str.lower()=="true")).sum())
ver["chat_member_messages"] = int((msgs.is_member.str.lower()=="true").sum())
ver["chat_streams_with_messages"] = msgs["video_id"].nunique()

# ---- 5. build unified index
rows = []
def labels(s): return [x.strip() for x in s.split(";") if x.strip()]
def add(file_key, r, unit, evidence_id, parent_id, text, author="", date="", extra=None):
    rec = {"file": file_key, "evidence_id": evidence_id, "unit": unit, "parent_id": parent_id,
           "text": text, "author": author, "date": date,
           "flash_community": r["flash_community"], "flash_specific_category": r["flash_specific_category"],
           "flash_topic": r["flash_topic"], "flash_summary": r["flash_short_summary"], "flash_confidence": r["flash_confidence"]}
    if extra: rec.update(extra)
    rows.append(rec)

for k in ["tt_direct","tt_comm"]:
    for _, r in D[k].iterrows():
        add(k, r, "video", r["flash_evidence_row_id"], "", (r["caption"]+" "+r["hashtags"]).strip(),
            author="", date="", extra={"link": r["link"], "views": r["views"], "likes": r["likes"], "comments": r["comments"],
            "shares": r["shares"], "gemini_status": r["status"], "gemini_angle": r["buyer_or_seller_angle"],
            "gemini_item_category": r["item_category"], "gemini_ad_description": r["ad_description"], "gemini_ebay_item": r["ebay_item"]})
for _, r in tc.iterrows():
    add("tt_comments", r, "comment", r["flash_evidence_row_id"], r["video_url"], r["comment_text"],
        author=r["author"], date=r["comment_created_at"], extra={"likes": r["comment_likes"]})
for k in ["rd_broad","rd_ebay"]:
    for _, r in D[k].iterrows():
        unit = "post" if r["row_type"]=="post" else "comment"
        text = (r["title"]+"\n"+r["text"]).strip() if unit=="post" else r["text"]
        add(k, r, unit, r["flash_evidence_row_id"], r["parent_id"] if unit=="comment" else "", text,
            author=r["author"], date=r["posted_at"], extra={"subreddit": r["subreddit"], "bucket": r["bucket"], "post_id": r["post_id"],
            "score": r["score"], "depth": r["depth"], "url": r["url"], "duplicate_of_broad": r["flash_evidence_row_id"] in shared and k=="rd_ebay"})
for _, r in D["yt_titles"].iterrows():
    add("yt_titles", r, "video", r["flash_evidence_row_id"], "", r["title"], author=r["channel"], date=r["date"],
        extra={"lane": r["lane"], "video_id": r["video_id"], "views": r["views"], "url": r["url"]})
for _, r in yc.iterrows():
    add("yt_comments", r, "comment", r["flash_evidence_row_id"], "youtube_video:"+r["video_id"], r["comment_text"],
        author=r["author"], date="", extra={"lane": r["lane"], "video_id": r["video_id"], "video_title": r["video_title"],
        "likes": r["comment_likes"], "is_pinned": r["is_pinned"], "hearted": r["hearted_by_creator"]})
for _, r in ch.iterrows():
    add("yt_chat", r, "chat_"+r["event_type"], r["flash_evidence_row_id"], "youtube_stream:"+r["video_id"], r["message"],
        author=r["author"], date=r["published_at"], extra={"video_id": r["video_id"], "video_title": r["video_title"], "channel": r["channel"],
        "is_owner": r["is_owner"], "is_moderator": r["is_moderator"], "is_member": r["is_member"], "offset": r["offset"]})

idx = pd.DataFrame(rows)
idx["dedup_drop"] = idx.get("duplicate_of_broad", False).fillna(False).astype(bool)
idx["independent"] = idx["unit"].isin(["video","post"])
idx.to_csv(os.path.join(OUT, "unified_evidence_index.csv"), index=False)

# ---- 6. coverage table (dataset x community label), dedup applied, chat system/error excluded
cov = []
for k in FILES:
    sub = idx[(idx.file==k) & (~idx.dedup_drop) & (~idx.unit.isin(["chat_system","chat_error"]))]
    for c in COMMUNITIES:
        m = sub["flash_community"].apply(lambda s: c in labels(s))
        ind = int((m & sub.independent).sum()); dep = int((m & ~sub.independent).sum())
        cov.append({"dataset": k, "community": c, "independent_units": ind, "dependent_units": dep})
cov = pd.DataFrame(cov)
cov.to_csv(os.path.join(OUT, "coverage_by_dataset_community.csv"), index=False)

# ---- 7. Other / emerging profile in TikTok videos
tt = idx[idx.file.isin(["tt_direct","tt_comm"])]
oe = tt[tt.flash_community.apply(lambda s: "Other / emerging" in labels(s))]
ver["other_emerging_videos"] = len(oe)
prof = oe.groupby(["flash_specific_category"]).size().sort_values(ascending=False)
prof.to_csv(os.path.join(OUT, "other_emerging_specific_category_counts.csv"), header=["videos"])
topic = Counter()
for t in oe["flash_topic"]:
    for x in labels(t): topic[x] += 1
pd.Series(topic).sort_values(ascending=False).to_csv(os.path.join(OUT, "other_emerging_topic_counts.csv"), header=["videos"])
oe[["file","evidence_id","flash_specific_category","flash_topic","flash_summary","text","views"]].to_csv(os.path.join(OUT, "other_emerging_rows.csv"), index=False)

# ---- 8. source-text term counts (eBay, live terms) for verification
def has(pat, s): return bool(re.search(pat, s, re.I))
for k in FILES:
    sub = idx[(idx.file==k) & (~idx.dedup_drop) & (~idx.unit.isin(["chat_system","chat_error"]))]
    ver[k]["ebay_in_source_text"] = int(sub.text.apply(lambda s: has(r"\bebay\b", s)).sum())
    ver[k]["live_terms_in_source_text"] = int(sub.text.apply(lambda s: has(r"\blive\b|livestream|whatnot|tiktok ?shop|fanatics live", s)).sum())
    ver[k]["ebay_live_in_source_text"] = int(sub.text.apply(lambda s: has(r"ebay ?live|#ebaylive", s)).sum())
    ver[k]["whatnot_in_source_text"] = int(sub.text.apply(lambda s: has(r"whatnot", s)).sum())
    ver[k]["tiktok_shop_in_source_text"] = int(sub.text.apply(lambda s: has(r"tiktok ?shop|#tiktokshop", s)).sum())

# Reddit dates
for k in ["rd_broad","rd_ebay"]:
    posts = idx[(idx.file==k)&(idx.unit=="post")]
    dts = pd.to_datetime(posts.date, errors="coerce", utc=True)
    ver[k]["post_date_min"] = str(dts.min()); ver[k]["post_date_max"] = str(dts.max()); ver[k]["post_date_blank"] = int(dts.isna().sum())
    ver[k]["posts_pre_2025"] = int((dts < "2025-01-01").sum())
    comments = idx[(idx.file==k)&(idx.unit=="comment")]
    cd = pd.to_datetime(comments.date, errors="coerce", utc=True)
    ver[k]["comments_pre_2025"] = int((cd < "2025-01-01").sum()); ver[k]["comment_date_blank"] = int(cd.isna().sum())
tcd = pd.to_datetime(tc.comment_created_at, errors="coerce", utc=True)
ver["tt_comments"]["comments_pre_2025"] = int((tcd < "2025-01-01").sum()); ver["tt_comments"]["comment_date_blank"] = int(tcd.isna().sum())
ver["tt_comments"]["date_min"] = str(tcd.min()); ver["tt_comments"]["date_max"] = str(tcd.max())

json.dump(ver, open(os.path.join(OUT, "stage1_verification.json"), "w"), indent=2, default=str)
print(json.dumps(ver, indent=2, default=str))
print(cov.pivot(index="community", columns="dataset", values="independent_units"))
print(cov.pivot(index="community", columns="dataset", values="dependent_units"))
print(prof.head(40))
