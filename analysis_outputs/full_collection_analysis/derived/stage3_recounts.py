"""Stage 3 recounts: every number used in stage2_provisional.md, recomputed on deduplicated units with an explicit
denominator, from the unified index (source text) and the register. Output: stage3_recounts.json. Counting only."""
import reader as R, pandas as pd, re, json, os, warnings; warnings.filterwarnings("ignore")
d = R.idx(); reg = R.reg()
base = (~d.dedup_drop) & (~d.unit.isin(["chat_system","chat_error"]))
D = d[base]
T = D.text.str.lower()
def labels(s): return [x.strip() for x in s.split(";") if x.strip()]
def has(lab): return D.flash_community.apply(lambda s: lab in labels(s))
out = {}
# --- units
out["units"] = {
 "tt_direct_videos": int((D.file=="tt_direct").sum()), "tt_comm_videos": int((D.file=="tt_comm").sum()),
 "tt_comments": int((D.file=="tt_comments").sum()), "tt_comment_parent_videos": int(D[D.file=="tt_comments"].parent_id.nunique()),
 "rd_broad_posts": int(((D.file=="rd_broad")&(D.unit=="post")).sum()), "rd_broad_comments": int(((D.file=="rd_broad")&(D.unit=="comment")).sum()),
 "rd_ebay_posts_after_dedup": int(((D.file=="rd_ebay")&(D.unit=="post")).sum()), "rd_ebay_comments_after_dedup": int(((D.file=="rd_ebay")&(D.unit=="comment")).sum()),
 "yt_titles": int((D.file=="yt_titles").sum()), "yt_comments": int((D.file=="yt_comments").sum()), "yt_comment_videos": int(D[D.file=="yt_comments"].video_id.nunique()),
 "chat_messages": int((D.unit=="chat_message").sum()), "chat_membership": int((D.unit=="chat_membership").sum()), "chat_super_chat": int((D.unit=="chat_super_chat").sum()),
 "chat_system": int((d.unit=="chat_system").sum()), "chat_error": int((d.unit=="chat_error").sum()),
 "chat_streams_with_messages": int(D[D.unit=="chat_message"].video_id.nunique()),
 "reddit_dup_rows_dropped": int(d.dedup_drop.sum()), "total_rows": int(len(d)), "total_unique_ids": int(d.evidence_id.nunique()),
}
# --- register (read counts)
rg = reg.drop_duplicates("evidence_id")
out["read"] = {"unique_rows_read": int(len(rg)), "by_file": rg.file.value_counts().to_dict(),
               "by_file_unit": {f"{a}/{b}": int(c) for (a,b),c in rg.groupby(["file","unit"]).size().items()},
               "control_rows": int(rg.section.str.startswith("CONTROL").sum()),
               "stage3_rows": int(rg.section.str.startswith("S3/").sum())}
# --- eBay Live in source text
el = T.str.contains(r"ebay\s*live|ebaylive", regex=True)
promo = T.str.contains(r"#ad\b|\bad\b|#ebaypartner|anzeige|#sponsored|paid partnership|#werbung", regex=True)
out["ebay_live"] = {"rows_all_files": int(el.sum()), "by_file": D[el].file.value_counts().to_dict(),
  "tt_direct_captions": int((el&(D.file=="tt_direct")).sum()), "tt_comm_captions": int((el&(D.file=="tt_comm")).sum()),
  "tt_direct_captions_promo_tagged": int((el&(D.file=="tt_direct")&promo).sum()),
  "tt_direct_captions_no_promo_tag": int((el&(D.file=="tt_direct")&~promo).sum()),
  "rows_read": int(D[el].evidence_id.isin(set(rg.evidence_id)).sum()),
  "yt_titles_from_ebay_channels": D[el&(D.file=="yt_titles")&D.channel.str.lower().str.contains("ebay")][["evidence_id","channel"]].to_dict("records")}
tt_el = D[el&(D.file=="tt_direct")].assign(v=pd.to_numeric(D.views, errors="coerce")).sort_values("v", ascending=False)
out["ebay_live"]["top3_views_promo"] = [{"id": r.evidence_id, "views": r.v, "promo_tag": bool(promo[r.Index])} for r in tt_el.head(3).itertuples()]
# --- eBay in captions
out["ebay_in_captions"] = {"tt_direct": int((T.str.contains("ebay")&(D.file=="tt_direct")).sum()), "tt_comm": int((T.str.contains("ebay")&(D.file=="tt_comm")).sum())}
out["comm_captions_naming_ebay_by_label"] = {lab: {"videos": int((has(lab)&(D.file=="tt_comm")).sum()), "naming_ebay": int((has(lab)&(D.file=="tt_comm")&T.str.contains("ebay")).sum())}
   for lab in ["Sports Cards","TCG/Pokemon","Sneakers/Streetwear","Luxury Fashion","Electronics","Toys/Collectibles","Other / emerging"]}
# --- breaks promotion to TikTok Shop
out["break_promo"] = {"tt_captions_daily_breaks_tiktok_shop": int((T.str.contains(r"daily breaks", regex=True)&T.str.contains(r"tiktok ?shop", regex=True)&D.file.isin(["tt_direct","tt_comm"])).sum()),
                      "tt_captions_break_and_tiktok_shop": int((T.str.contains(r"\bbreaks?\b", regex=True)&T.str.contains(r"tiktok ?shop", regex=True)&D.file.isin(["tt_direct","tt_comm"])).sum()),
                      "tt_captions_break_and_whatnot": int((T.str.contains(r"\bbreaks?\b", regex=True)&T.str.contains("whatnot")&D.file.isin(["tt_direct","tt_comm"])).sum()),
                      "tt_captions_break_and_ebay": int((T.str.contains(r"\bbreaks?\b", regex=True)&T.str.contains("ebay")&D.file.isin(["tt_direct","tt_comm"])).sum())}
# --- YouTube sports_cards_breaks lane views
yt = D[(D.file=="yt_titles")].assign(v=pd.to_numeric(D.views, errors="coerce"))
lane = yt[yt.lane=="sports_cards_breaks"]
eb = lane[lane.text.str.lower().str.contains("ebay")]
out["yt_sports_cards_breaks_lane"] = {"videos": int(len(lane)), "titles_naming_ebay": int(len(eb)),
   "ebay_titled_views_min_max": [None if eb.v.isna().all() else float(eb.v.min()), None if eb.v.isna().all() else float(eb.v.max())],
   "non_ebay_titled_views_min_max": [float(lane[~lane.text.str.lower().str.contains("ebay")].v.min()), float(lane[~lane.text.str.lower().str.contains("ebay")].v.max())],
   "views_blank": int(lane.v.isna().sum()),
   "rows": lane[["evidence_id","v","channel"]].assign(title=lane.text.str[:80]).to_dict("records")}
# --- other TCGs and Fanatics (source text)
def cnt(pat):
    m = T.str.contains(pat, regex=True); return {"rows": int(m.sum()), "by_file": D[m].file.value_counts().to_dict()}
out["other_tcg"] = {k: cnt(p) for k,p in {"one_piece": r"one piece", "lorcana": r"lorcana", "magic_mtg": r"\bmtg\b|magic the gathering|magic: the gathering", "yugioh": r"yu-?gi-?oh", "riftbound": r"riftbound", "fanatics": r"fanatics"}.items()}
# --- coins (Stage 2 pattern)
out["coins"] = cnt(r"\bcoins?\b|numismat|bullion|silver eagle|morgan dollar|gold coin|\bpcgs\b|\bngc\b|challenge coin")
out["coins"]["flash_label_Coins"] = {"tt_videos": int((has("Coins")&D.file.isin(["tt_direct","tt_comm"])).sum()), "reddit_posts": int((has("Coins")&(D.unit=="post")).sum()), "reddit_comments": int((has("Coins")&(D.unit=="comment")&D.file.isin(["rd_broad","rd_ebay"])).sum())}
# --- fragrance
out["fragrance"] = cnt(r"fragrance|perfume|cologne|\bparfum")
# --- watches keyword pool (Stage 1 definition unavailable; reproducible pattern here)
out["watches"] = cnt(r"\bwatch(es)?\b(?!.*(watch (this|the|my|us|me|it|out|video|till|until|as|how|what|him|her|them|live)))|rolex|seiko|omega|breitling|chrono24|watchexchange")
# --- Panini / Premier League / memorabilia
out["panini_premier"] = {"panini": cnt(r"panini"), "premier_league": cnt(r"premier league"), "match_worn": cnt(r"match.?worn|game.?worn"), "memorabilia": cnt(r"memorabilia")}
# --- markets
out["markets"] = {"uk_stated": cnt(r"\buk\b|ebay\.co\.uk|@ebay uk|ebay uk|britain|london|£"), "de_stated": cnt(r"germany|deutschland|#anzeige|ebay\.de\b|ebay deutschland|modellbahn|\bgerman\b"), "au_stated": cnt(r"australia|@ebayau|ebay\.com\.au|aussie|\bau\b|aest"), "japan_ebay": cnt(r"japanese ebay|japan ebay|ebay japan|from japan")}
# --- TikTok comments pre-2025
tc = D[D.file=="tt_comments"]; out["tt_comments_pre2025"] = int((tc.date.str[:4] < "2025").sum())
# --- live chat per stream
ch = d[d.unit=="chat_message"]
host = (ch.is_owner.str.lower()=="true")|(ch.is_moderator.str.lower()=="true")
out["chat"] = {"messages": int(len(ch)), "host_or_mod_flagged": int(host.sum()), "member_flagged": int((ch.is_member.str.lower()=="true").sum()),
   "distinct_nonhost_authors": int(ch[~host].author.nunique()), "naming_ebay": int(ch.text.str.lower().str.contains("ebay").sum()),
   "per_stream": [{"video_id": v, "title": g.video_title.iloc[0][:70] if "video_title" in g else "", "messages": int(len(g)), "host_mod": int(((g.is_owner.str.lower()=="true")|(g.is_moderator.str.lower()=="true")).sum()), "naming_ebay": int(g.text.str.lower().str.contains("ebay").sum()), "read": int(g.evidence_id.isin(set(rg.evidence_id)).sum())} for v,g in ch.groupby("video_id")]}
# --- AG in source text
ag = T.str.contains(r"authenticity guarantee|authenticity guaranteed|ebay auth|authenticat", regex=True)
out["authentication_rows"] = {"all": int(ag.sum()), "by_file": D[ag].file.value_counts().to_dict(), "read": int(D[ag].evidence_id.isin(set(rg.evidence_id)).sum())}
# --- Whatnot / TikTok Shop in source text
out["platforms"] = {p: cnt(pat) for p,pat in {"whatnot": r"whatnot", "tiktok_shop": r"tiktok ?shop", "fanatics_live": r"fanatics live", "stockx": r"stockx", "goat": r"\bgoat\b", "tcgplayer": r"tcgplayer|tcg player", "mercari": r"mercari", "vinted": r"vinted", "depop": r"depop", "poshmark": r"poshmark", "facebook_marketplace": r"facebook marketplace|fb marketplace", "discord": r"discord", "purse ?forum": r"purse ?forum", "chrono24": r"chrono24"}.items()}
# --- r/whatnotapp and subreddit counts
rb = D[(D.file=="rd_broad")&(D.unit=="post")]; out["rd_broad_subreddits"] = rb.subreddit.value_counts().to_dict()
# --- score / views lookup for every ID cited in the Stage 2 docs (used by the ledger)
json.dump(out, open(os.path.join(R.HERE, "stage3_recounts.json"), "w"), indent=1, default=str)
print(json.dumps(out, indent=1, default=str)[:12000])
