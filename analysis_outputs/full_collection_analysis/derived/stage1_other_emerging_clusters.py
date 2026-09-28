"""Cluster the 683 'Other / emerging' TikTok videos by keyword rules over flash_specific_category + flash_topic.
Counting only; rule-based grouping of existing AI labels (so the clusters are AI-coded, rule-grouped)."""
import pandas as pd, re, os, json
from collections import Counter
OUT = os.path.dirname(os.path.abspath(__file__))
oe = pd.read_csv(os.path.join(OUT, "other_emerging_rows.csv"), dtype=str, keep_default_na=False)

RULES = [
 ("Physical media (Blu-ray/DVD/steelbook/VHS/CD/vinyl/books)", r"blu-?ray|dvd|steelbook|physical media|vhs|vinyl|\bcd\b|records|books?\b|manga|comics?"),
 ("Patches, pins, buttons and battle jackets", r"patch|battle (jacket|vest)|morale|pinback|\bpins?\b|button|enamel"),
 ("Automotive: parts, cars, motorcycles", r"auto|car\b|cars\b|engine|motorcycle|vehicle|truck|wheel|tire|dashboard|automobile"),
 ("Vintage and secondhand clothing / thrift", r"vintage (clothing|dress|t-?shirt|shirt|jacket|denim|jeans)|secondhand|thrift|second-hand|used clothing|vintage clothing|vintage dresses|vintage tee"),
 ("Model trains", r"model train|trains?\b|railway|lionel"),
 ("Video games and retro gaming", r"video game|retro gam|console|nintendo|playstation|xbox|gameboy|cartridge"),
 ("Sewing, craft and notions", r"sewing|craft|notions|fabric|yarn|knit|crochet|bead"),
 ("Jewelry and body jewelry", r"jewel|ring\b|necklace|earring|gauge|bracelet|gemstone|diamond|gold\b|silver\b"),
 ("Home, kitchen and decor", r"home|kitchen|decor|furniture|glassware|pyrex|dish|mug|cookware|lamp|rug|antique"),
 ("Beauty, fragrance and personal care", r"beauty|fragrance|perfume|cologne|skincare|makeup|cosmetic|hair"),
 ("Sports memorabilia and equipment", r"memorabilia|jersey|signed|autograph|football|soccer|golf|bike|bicycle|fishing|hunting|sport"),
 ("Music instruments and audio gear", r"guitar|instrument|amplifier|pedal|synth|drum|piano|audio gear|speaker|headphone"),
 ("Reselling / seller how-to / marketplace ops", r"resell|reseller|flipping|sourcing|listing|shipping|seller|sold|store|inventory|marketplace|ebay"),
 ("Pets, plants, food and other lifestyle", r"pet|plant|garden|food|snack|candy|drink|tea|coffee"),
 ("Military, police and collectible memorabilia", r"military|police|challenge coin|badge|militaria|war"),
]
def assign(cat, topic):
    s = (cat + " ; " + topic).lower()
    hits = [name for name, pat in RULES if re.search(pat, s)]
    return hits[0] if hits else "Unassigned (mixed/other)", hits
labels, multi = [], Counter()
for _, r in oe.iterrows():
    first, hits = assign(r["flash_specific_category"], r["flash_topic"])
    labels.append(first)
    for h in hits: multi[h] += 1
oe["cluster_first_match"] = labels
counts = oe["cluster_first_match"].value_counts()
oe.to_csv(os.path.join(OUT, "other_emerging_rows_clustered.csv"), index=False)
counts.to_csv(os.path.join(OUT, "other_emerging_cluster_counts.csv"), header=["videos_first_match"])
print(counts)
print("\nAny-match counts (a video can match several):")
for k, v in multi.most_common(): print(f"  {k}: {v}")
print("\nUnassigned examples (specific_category | topic):")
for _, r in oe[oe.cluster_first_match.str.startswith("Unassigned")].head(60).iterrows():
    print("  ", r["flash_specific_category"], "|", r["flash_topic"][:80])
print("\nBy pull:", oe.groupby(["file","cluster_first_match"]).size().to_string())
