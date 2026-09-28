# Inventory of the eight finalized non-brand datasets. Counts only; no content reading, no model calls.
import pandas as pd, re, os, sys, openpyxl
from collections import Counter
ROOT = r"C:\Users\andre\Documents\ebay_research"
os.chdir(os.path.join(ROOT, "finalized"))
out = open(os.path.join(ROOT, "analysis_outputs", "full_dataset_inventory", "inventory_out.txt"), "w", encoding="utf-8")
def P(*a):
    s = " ".join(str(x) for x in a); print(s); out.write(s + "\n")
rd = lambda f: pd.read_csv(f, dtype=str, keep_default_na=False, encoding="utf-8-sig")
D = rd("FINAL_1007_direct_eBay_TikTok_videos_Flash_Batch_communities_topics.csv")
C = rd("FINAL_914_community_TikTok_videos_Flash_Batch_communities_topics.csv")
TC = rd("FINAL_500_TikTok_comments_50_videos_Flash_Batch_communities_topics.csv")
R1 = rd("FINAL_100_Reddit_conversations_1998_comments_Flash_Batch_communities_topics.csv")
R2 = rd("FINAL_137_rEbay_posts_632_comments_Flash_Batch_communities_topics.csv")
YV = rd("FINAL_248_YouTube_video_titles_Flash_Batch_communities_topics.csv")
YC = rd("FINAL_1407_YouTube_comments_Flash_Batch_communities_topics.csv")
YL = rd("FINAL_1435_YouTube_live_chat_rows_Flash_Batch_communities_topics.csv")
eb = lambda s: s.str.contains("ebay", case=False, na=False)
lv = lambda s: s.str.contains(r"\blive\b|livestream|whatnot|tiktok shop", case=False, na=False, regex=True)
def labs(df):
    c = Counter()
    for v in df["flash_community"]:
        for l in str(v).split(";"):
            if l.strip(): c[l.strip()] += 1
    return dict(c.most_common())
def sec(t): P("\n" + "=" * 8, t)

for name, df in [("TikTok DIRECT 1007", D), ("TikTok COMMUNITY 914", C)]:
    sec(name)
    P("unique links:", df["link"].nunique(), "dup links:", len(df) - df["link"].nunique())
    pd_ = df.loc[df["post date"] != "", "post date"]
    P("post date present:", len(pd_), "| range:", pd_.min() if len(pd_) else None, "->", pd_.max() if len(pd_) else None)
    P("track date range:", df["track date"].min(), "->", df["track date"].max())
    P("source:", Counter(df["source"]).most_common(8))
    P("pulled_as:", Counter(df["pulled_as"]).most_common(15))
    P("status:", Counter(df["status"]).most_common(4), "| audio_transcript nonempty:", (df["audio_transcript"].str.len() > 0).sum(), "| notable_text nonempty:", (df["notable_text_on_screen"].str.len() > 0).sum())
    P("eBay in caption+hashtags:", (eb(df["caption"]) | eb(df["hashtags"])).sum(), "| eBay in transcript:", eb(df["audio_transcript"]).sum(), "| eBay in on-screen text:", eb(df["notable_text_on_screen"]).sum(), "| eBay in ad_description (Gemini):", eb(df["ad_description"]).sum())
    P("live/whatnot/tiktok shop in caption|hashtags|transcript|onscreen:", (lv(df["caption"]) | lv(df["hashtags"]) | lv(df["audio_transcript"]) | lv(df["notable_text_on_screen"])).sum())
    P("ebay_relevance (Gemini):", Counter(df["ebay_relevance"]).most_common(8))
    P("buyer_or_seller_angle (Gemini):", Counter(df["buyer_or_seller_angle"]).most_common(8))
    P("flash_community (multi, AI-coded):", labs(df))
    P("flash_confidence:", Counter(df["flash_confidence"]).most_common())
    P("comments blank:", (df["comments"] == "").sum(), "views blank:", (df["views"] == "").sum())
sec("TikTok direct vs community overlap")
P("shared links:", len(set(D["link"]) & set(C["link"])))
sec("TikTok COMMENTS 500")
P("videos:", TC["video_url"].nunique(), "| comment_id unique:", TC["comment_id"].nunique())
vids = set(TC["video_url"]); P("of those videos in DIRECT:", len(vids & set(D["link"])), "in COMMUNITY:", len(vids & set(C["link"])))
P("comment_created_at range:", TC["comment_created_at"].min(), "->", TC["comment_created_at"].max())
P("item_category of parent videos (Gemini):", Counter(TC.drop_duplicates("video_url")["item_category"]).most_common(10))
P("eBay in comment_text:", eb(TC["comment_text"]).sum(), "| live terms:", lv(TC["comment_text"]).sum())
P("flash_community:", labs(TC)); P("confidence:", Counter(TC["flash_confidence"]).most_common())
for name, df in [("REDDIT broad 100 convos", R1), ("REDDIT r/Ebay 137 posts", R2)]:
    sec(name)
    P("row_type:", Counter(df["row_type"]).most_common())
    Po = df[df["row_type"] == "post"]; Cm = df[df["row_type"] != "post"]
    P("unique post_id (posts):", Po["post_id"].nunique(), "| comments per post: mean %.1f max %d" % (len(Cm) / max(1, Po["post_id"].nunique()), Cm.groupby("post_id").size().max()))
    P("bucket:", Counter(Po["bucket"]).most_common(12))
    P("subreddits (posts):", Counter(Po["subreddit"]).most_common(20))
    P("posted_at range (posts):", Po["posted_at"].min(), "->", Po["posted_at"].max())
    P("eBay in post title/text:", (eb(Po["title"]) | eb(Po["text"])).sum(), "/", len(Po), "| eBay in comments:", eb(Cm["text"]).sum(), "/", len(Cm))
    P("live terms in posts:", (lv(Po["title"]) | lv(Po["text"])).sum(), "| in comments:", lv(Cm["text"]).sum())
    P("depth:", Counter(df["depth"]).most_common(6))
    P("flash_community (posts):", labs(Po)); P("flash_community (comments):", labs(Cm)); P("confidence:", Counter(df["flash_confidence"]).most_common())
sec("Reddit overlap between pulls")
P("shared post_id:", len(set(R1["post_id"]) & set(R2["post_id"])), "| shared comment_id:", len((set(R1["comment_id"]) & set(R2["comment_id"])) - {""}))
sec("YOUTUBE VIDEOS 248")
P("unique video_id:", YV["video_id"].nunique(), "| lane:", Counter(YV["lane"]).most_common(25))
dt = YV.loc[YV["date"] != "", "date"]
P("type:", Counter(YV["type"]).most_common(), "| date present:", len(dt), "range:", dt.min() if len(dt) else None, "->", dt.max() if len(dt) else None)
P("eBay in title:", eb(YV["title"]).sum(), "| live terms in title:", lv(YV["title"]).sum())
P("flash_community:", labs(YV))
sec("YOUTUBE COMMENTS 1407")
P("videos with comments:", YC["video_id"].nunique(), "| of which in 248 list:", len(set(YC["video_id"]) & set(YV["video_id"])), "| lane:", Counter(YC["lane"]).most_common(25))
P("comments per video: mean %.1f max %d" % (len(YC) / YC["video_id"].nunique(), YC.groupby("video_id").size().max()))
P("published present:", (YC["published"] != "").sum(), "| comment_id unique:", YC["comment_id"].nunique())
P("eBay in comment_text:", eb(YC["comment_text"]).sum(), "| live terms:", lv(YC["comment_text"]).sum())
P("flash_community:", labs(YC)); P("confidence:", Counter(YC["flash_confidence"]).most_common())
sec("YOUTUBE LIVE CHAT 1435")
P("videos:", YL["video_id"].nunique(), "| in 248 list:", len(set(YL["video_id"]) & set(YV["video_id"])), "| in comments videos:", len(set(YL["video_id"]) & set(YC["video_id"])))
P("event_type:", Counter(YL["event_type"]).most_common(), "| stream_status:", Counter(YL["stream_status"]).most_common())
P("rows per video:", YL.groupby("video_id").size().describe()[["min", "50%", "max"]].to_dict())
for t in YL.drop_duplicates("video_id")[["video_id", "video_title", "channel"]].itertuples(index=False):
    P("   ", t[0], "|", t[1][:80], "|", t[2])
P("super_chat rows:", (YL["super_chat_amount"] != "").sum(), "| members:", (YL["is_member"].str.lower() == "true").sum(), "| owner/mod msgs:", ((YL["is_owner"].str.lower() == "true") | (YL["is_moderator"].str.lower() == "true")).sum())
P("eBay in message:", eb(YL["message"]).sum(), "| live terms:", lv(YL["message"]).sum(), "| flash_community:", labs(YL)); P("confidence:", Counter(YL["flash_confidence"]).most_common())
P("published_at range:", YL["published_at"].min(), "->", YL["published_at"].max())
sec("150-row sample -> full-file membership")
wb = openpyxl.load_workbook(os.path.join(ROOT, r"data\tests_and_supporting_files\ai_strategy_comparison_150_rows\TEST_150_rows_eBay_Live_AI_comparison_sample.xlsx"), read_only=True)
sid = set()
for ws in wb.worksheets:
    for r in ws.iter_rows(values_only=True):
        for c in r:
            if isinstance(c, str) and re.match(r"(tiktok_video|reddit|youtube_comment):", c): sid.add(c)
for name, df in [("D", D), ("C", C), ("TC", TC), ("R1", R1), ("R2", R2), ("YV", YV), ("YC", YC), ("YL", YL)]:
    P(name, "sample ids present:", len(sid & set(df["flash_evidence_row_id"])))
P("sample reddit ids in R2 only:", len((sid & set(R2["flash_evidence_row_id"])) - set(R1["flash_evidence_row_id"])))
sec("evidence id uniqueness across all eight")
allids = pd.concat([df["flash_evidence_row_id"] for df in [D, C, TC, R1, R2, YV, YC, YL]])
P("total rows:", len(allids), "| unique ids:", allids.nunique(), "| blank ids:", (allids == "").sum())
out.close()
