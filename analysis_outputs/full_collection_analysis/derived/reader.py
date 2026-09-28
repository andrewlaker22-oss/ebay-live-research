"""Bounded source-reading helper. Local only, no model calls.
Every row printed through `show()` is appended to reviewed_evidence.csv (the single reviewed-ID register).
The reading budget is the count of UNIQUE evidence IDs in that register. Cap: 1,200 (100 reserved for control)."""
import pandas as pd, os, re, json, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
IDX = os.path.join(HERE, "unified_evidence_index.csv")
REG = os.path.join(HERE, "..", "reviewed_evidence.csv")
CAP = 1200
CONTROL_RESERVE = 100

_idx = None
def idx():
    global _idx
    if _idx is None:
        _idx = pd.read_csv(IDX, dtype=str, keep_default_na=False)
        _idx["dedup_drop"] = _idx["dedup_drop"].isin(["True","true"])
    return _idx

def reg():
    if os.path.exists(REG):
        return pd.read_csv(REG, dtype=str, keep_default_na=False)
    return pd.DataFrame(columns=["evidence_id","file","unit","parent_id","section","read_chars","truncated","note"])

def budget():
    r = reg()
    return r["evidence_id"].nunique()

def labels(s): return [x.strip() for x in s.split(";") if x.strip()]

def role_flags(r):
    f = []
    if r.get("is_owner","").lower()=="true": f.append("OWNER")
    if r.get("is_moderator","").lower()=="true": f.append("MOD")
    if r.get("is_member","").lower()=="true": f.append("member")
    if r.get("is_pinned","").lower()=="true": f.append("pinned")
    if r.get("hearted","").lower()=="true": f.append("hearted")
    if r.get("author","")=="AutoModerator": f.append("BOT")
    return ",".join(f)

def fmt(r, maxchars):
    t = re.sub(r"\s+", " ", r["text"]).strip()
    if r["file"] in ("tt_direct","tt_comm"):
        # hashtags column is a JSON-like list duplicating the caption's #tags; show tag names only
        m = re.search(r"\[\{.*$", t)
        if m:
            names = re.findall(r"'name': '([^']*)'", m.group(0))
            t = t[:m.start()].strip() + " | tags: " + " ".join("#"+n for n in names)
    trunc = len(t) > maxchars
    t = t[:maxchars] + (" [...]" if trunc else "")
    meta = []
    if r["file"] in ("tt_direct","tt_comm"): meta.append(f"views={r.get('views','')} likes={r.get('likes','')} shares={r.get('shares','')}")
    if r["file"] in ("rd_broad","rd_ebay"): meta.append(f"r/{r.get('subreddit','')} score={r.get('score','')} depth={r.get('depth','')} date={r.get('date','')[:10]}")
    if r["file"]=="tt_comments": meta.append(f"likes={r.get('likes','')} date={r.get('date','')[:10]}")
    if r["file"]=="yt_comments": meta.append(f"lane={r.get('lane','')} likes={r.get('likes','')}")
    if r["file"]=="yt_titles": meta.append(f"lane={r.get('lane','')} views={r.get('views','')} date={r.get('date','')} ch={r.get('author','')}")
    if r["file"]=="yt_chat": meta.append(f"stream={r.get('video_id','')} off={r.get('offset','')}")
    rf = role_flags(r)
    if rf: meta.append(rf)
    return f"[{r['file']}|{r['evidence_id']}|{r['unit']}|{' '.join(meta)}|label={r['flash_community']}]\n    {t}", trunc

def show(section, rows, maxchars=350, note=""):
    """Print rows (DataFrame slice of the index) and register them under `section`."""
    r = reg()
    have = set(r["evidence_id"])
    new = []
    out = []
    for _, row in rows.iterrows():
        line, trunc = fmt(row, maxchars)
        out.append(line)
        new.append({"evidence_id": row["evidence_id"], "file": row["file"], "unit": row["unit"], "parent_id": row["parent_id"],
                    "section": section, "read_chars": min(len(row["text"]), maxchars), "truncated": trunc, "note": note})
    n_new_ids = len({x["evidence_id"] for x in new} - have)
    if budget() + n_new_ids > CAP:
        print(f"!! BUDGET: {budget()} + {n_new_ids} new would exceed cap {CAP}. Nothing printed or registered.")
        return
    r = pd.concat([r, pd.DataFrame(new)], ignore_index=True)
    r.to_csv(REG, index=False)
    print("\n".join(out))
    print(f"-- shown {len(out)} rows ({n_new_ids} new IDs); budget used {budget()}/{CAP}")

def sel(file=None, community=None, unit=None, text=None, exclude_reviewed=True, seed=20260928, n=None, sort=None, keep_dups=False):
    d = idx()
    m = pd.Series(True, index=d.index)
    if not keep_dups: m &= ~d["dedup_drop"]
    m &= ~d["unit"].isin(["chat_system","chat_error"])
    if file: m &= d["file"].isin([file] if isinstance(file,str) else file)
    if unit: m &= d["unit"].isin([unit] if isinstance(unit,str) else unit)
    if community: m &= d["flash_community"].apply(lambda s: community in labels(s))
    if text: m &= d["text"].str.contains(text, case=False, regex=True, na=False)
    if exclude_reviewed:
        m &= ~d["evidence_id"].isin(set(reg()["evidence_id"]))
    out = d[m]
    if sort == "views":
        out = out.assign(_v=pd.to_numeric(out["views"], errors="coerce")).sort_values("_v", ascending=False).drop(columns="_v")
    if n is not None and len(out) > n:
        out = out.sample(n=n, random_state=seed)
    return out

def by_ids(ids):
    d = idx(); return d[d["evidence_id"].isin(ids)]

def reddit_thread(post_evidence_id, max_comments=30, seed=20260928):
    """Post + its comments (depth-ordered, capped), keeping parent chain for sampled comments."""
    d = idx()
    post = d[d.evidence_id==post_evidence_id]
    if post.empty: return post
    pid = post.iloc[0]["post_id"]
    comments = d[(d.file==post.iloc[0]["file"]) & (d.unit=="comment") & (d.post_id==pid)]
    if len(comments) > max_comments:
        top = comments[comments.depth=="0"]
        top = top.assign(_s=pd.to_numeric(top.score, errors="coerce")).sort_values("_s", ascending=False).head(max_comments//2)
        rest = comments[~comments.evidence_id.isin(top.evidence_id)].sample(n=max_comments-len(top), random_state=seed)
        comments = pd.concat([top, rest])
        # add immediate parents of sampled replies
        parents = comments["parent_id"].unique()
        pc = d[d.evidence_id.isin(["reddit:"+p if not p.startswith("reddit:") else p for p in parents])]
        comments = pd.concat([comments, pc]).drop_duplicates("evidence_id")
    comments = comments.assign(_d=pd.to_numeric(comments.depth, errors="coerce")).sort_values(["_d"]).drop(columns="_d")
    return pd.concat([post, comments])

def tt_comment_group(video_link):
    d = idx()
    parent = d[(d.file.isin(["tt_direct","tt_comm"])) & (d.link==video_link)]
    comments = d[(d.file=="tt_comments") & (d.parent_id==video_link)]
    return pd.concat([parent, comments])

def yt_comment_group(video_id, n=10):
    d = idx()
    v = d[(d.file=="yt_titles") & (d.video_id==video_id)]
    c = d[(d.file=="yt_comments") & (d.video_id==video_id)].head(n)
    return pd.concat([v, c])

def chat_slice(video_id, n=40, seed=20260928, nonhost_only=False, contiguous=True):
    d = idx()
    c = d[(d.file=="yt_chat") & (d.video_id==video_id) & (d.unit=="chat_message")]
    if nonhost_only:
        c = c[~((c.is_owner.str.lower()=="true") | (c.is_moderator.str.lower()=="true"))]
    c = c.assign(_o=pd.to_numeric(c.offset, errors="coerce")).sort_values("_o").drop(columns="_o")
    if len(c) <= n: return c
    if contiguous:
        random.seed(seed); start = random.randint(0, len(c)-n); return c.iloc[start:start+n]
    return c.sample(n=n, random_state=seed).sort_index()
