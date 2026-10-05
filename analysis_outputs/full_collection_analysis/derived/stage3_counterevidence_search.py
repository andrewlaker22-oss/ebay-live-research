"""Stage 3: code-retrieved counterevidence candidate pools (counting only; nothing is read or registered here).
Runs the searches listed at the end of stage2_provisional.md across all eight files (dedup applied,
system/error chat rows excluded) and reports, per search, total hits, hits already read (in the register)
and unread hits, so that the <=85 remaining reads can be chosen from diverse contexts.
Source text only: the index `text` column holds caption+hashtags (TikTok), title+text (Reddit),
comment text, chat message or title. No Gemini field is searched here."""
import reader as R, pandas as pd, re, json, os, warnings; warnings.filterwarnings("ignore")
d = R.idx(); reg = set(R.reg()["evidence_id"])
base = (~d["dedup_drop"]) & (~d["unit"].isin(["chat_system","chat_error"]))
def labels(s): return [x.strip() for x in s.split(";") if x.strip()]
def hits(mask, name):
    h = d[base & mask]
    out = {"search": name, "hits": len(h), "already_read": int(h.evidence_id.isin(reg).sum()),
           "unread": int((~h.evidence_id.isin(reg)).sum()),
           "by_file": h.file.value_counts().to_dict()}
    print(json.dumps(out)); return h
T = d["text"].str.lower()
S = {}
# 1. community-pull captions naming eBay, by community label
S["comm_captions_ebay"] = hits((d.file=="tt_comm") & T.str.contains("ebay"), "community-pull captions naming eBay (source text)")
print(S["comm_captions_ebay"][["evidence_id","flash_community"]].to_string())
# Sports-Cards-labelled community videos naming eBay (SC-F1 recount)
sc = d[base & (d.file=="tt_comm") & d.flash_community.apply(lambda s: "Sports Cards" in labels(s))]
print("SC-labelled community videos:", len(sc), "naming eBay in caption:", int(sc.text.str.lower().str.contains("ebay").sum()))
for lab in ["TCG/Pokemon","Sneakers/Streetwear","Luxury Fashion","Electronics","Toys/Collectibles"]:
    x = d[base & (d.file=="tt_comm") & d.flash_community.apply(lambda s: lab in labels(s))]
    print(f"  {lab}: {len(x)} community videos, {int(x.text.str.lower().str.contains('ebay').sum())} name eBay in caption")
# 2. eBay Live in source text, all files; split promo-tagged vs not
el = T.str.contains(r"ebay\s*live|ebaylive", regex=True)
S["ebay_live_all"] = hits(el, "eBay Live named in source text, all files")
promo = T.str.contains(r"#ad\b|\bad\b|#ebaypartner|anzeige|#sponsored|paid partnership|#werbung", regex=True)
S["ebay_live_unpaid"] = hits(el & ~promo, "eBay Live named, no promo tag")
print(S["ebay_live_unpaid"][["file","unit"]].value_counts().to_string())
# 3. positive AG rows
ag = T.str.contains(r"authenticity guarantee|authenticity guaranteed|ebay auth|authenticat", regex=True)
pos = T.str.contains(r"\bsaved\b|thank|glad|great|love|worth it|protect|caught|peace of mind|recommend|trust|legit\b|passed|no issues|smooth|happy", regex=True)
S["ag_all"] = hits(ag, "authentication / AG named")
S["ag_positive_words"] = hits(ag & pos, "AG named with positive words")
# 4. UK Panini / Premier League; memorabilia / match-worn
S["panini"] = hits(T.str.contains(r"panini|premier league|\bsticker", regex=True), "Panini / Premier League / stickers")
S["memorabilia"] = hits(T.str.contains(r"memorabilia|match.?worn|game.?worn|signed shirt|jersey|autograph", regex=True), "memorabilia / match-worn / autograph")
# 5. DE-stated rows
S["de"] = hits(T.str.contains(r"germany|deutschland|\bgerman\b|#anzeige|ebay\.de|\bde\b|modellbahn|\bberlin\b|\bmünchen\b|\bmunich\b", regex=True), "DE-market terms")
S["uk"] = hits(T.str.contains(r"\buk\b|ebay\.co\.uk|@ebay uk|britain|london|£", regex=True), "UK-market terms")
# 6. blind box / trains naming eBay or live
bb = T.str.contains(r"blind box|labubu|pop ?mart|sonny angel|smiski|designer toy", regex=True)
tr = T.str.contains(r"model train|lionel|\bho scale|o gauge|n scale|modellbahn|märklin|marklin|kato\b|bachmann|model railroad", regex=True)
S["blindbox_ebay_live"] = hits(bb & T.str.contains(r"ebay|whatnot|\blive\b", regex=True), "blind box rows naming eBay/Whatnot/live")
S["trains_ebay_live"] = hits(tr & T.str.contains(r"ebay|whatnot|\blive\b", regex=True), "train rows naming eBay/Whatnot/live")
# 7. retro_gaming lane comments
S["retro_gaming_comments"] = hits((d.file=="yt_comments") & (d.lane=="retro_gaming"), "YouTube retro_gaming lane comments")
# 8. other TCGs, Fanatics
S["other_tcg"] = hits(T.str.contains(r"one piece|lorcana|yu-?gi-?oh|riftbound|\bmtg\b|magic the gathering", regex=True), "other TCGs named")
S["fanatics"] = hits(T.str.contains(r"fanatics", regex=True), "Fanatics named")
# 9. positive unpaid eBay purchase praise (buyer voice) to oppose 'friction-only' framing
S["ebay_praise"] = hits(T.str.contains(r"ebay", regex=True) & T.str.contains(r"\b(love|great|smooth|no issues|highly recommend|best purchase|so happy|arrived (fast|quickly)|thank you ebay|never had (a|an) (issue|problem))\b", regex=True) & ~promo, "eBay named with buyer-praise phrases, no promo tag")
# 10. whatnot / tiktok shop buyer voice
S["whatnot_buyer"] = hits(T.str.contains("whatnot") & T.str.contains(r"\bi (bought|buy|won|ordered|purchased)\b|as a buyer|my order", regex=True), "Whatnot with first-person buying verbs")
S["live_buyer"] = hits(T.str.contains(r"\blive\b|livestream|stream", regex=True) & T.str.contains(r"\bi (bought|buy|won|ordered|purchased|bid)\b|as a buyer|my order", regex=True), "live/stream with first-person buying verbs")
# 11. coins reproducible pattern
S["coins"] = hits(T.str.contains(r"\bcoins?\b|numismat|bullion|silver eagle|morgan dollar|gold coin|\bpcgs\b|\bngc\b|challenge coin", regex=True), "coins pattern (Stage 2 record)")
# 12. Sports card community captions with 'break' promo per platform
S["break_promo"] = hits(T.str.contains(r"\bbreaks?\b", regex=True) & (d.unit=="video"), "TikTok captions with 'break(s)'")
pd.concat([v.assign(search=k) for k, v in S.items()]).to_csv(os.path.join(R.HERE, "stage3_counterevidence_candidates.csv"), index=False)
print("budget used", R.budget(), "/", R.CAP)
