"""Claim support check (beyond ID resolution). For every row cited in claim_ledger.csv, a key phrase taken from the
row's READ WINDOW (the first read_chars characters that were printed and read in this run; see reviewed_evidence.csv)
must be present in that window. A phrase is the specific words that make the row support the claim it is cited for,
not a topic word. Rows whose phrase is missing, or whose window does not carry the support, are flagged per claim.
Also counts distinct authors (TikTok creator handle from the link, Reddit author, YouTube channel, comment or chat
author) behind each claim's cited rows and marks Reddit rows that exist in both Reddit files (shared rows).
Outputs: stage3_claim_support_report.json, and three columns appended to claim_ledger.csv
('Support check', 'Distinct authors behind cited rows', 'Shared Reddit rows cited'). Nothing here reads new rows."""
import os, re, csv, json, sys, pandas as pd
HERE = os.path.dirname(os.path.abspath(__file__))
IDX = pd.read_csv(os.path.join(HERE, "unified_evidence_index.csv"), dtype=str, keep_default_na=False)
REG = pd.read_csv(os.path.join(HERE, "..", "reviewed_evidence.csv"), dtype=str, keep_default_na=False)
READ_CHARS = REG.groupby("evidence_id").read_chars.apply(lambda s: max(int(x) for x in s)).to_dict()
ROW = {r.evidence_id: r for r in IDX.drop_duplicates("evidence_id").itertuples()}
SHARED = set(IDX[IDX.file == "rd_broad"].evidence_id) & set(IDX[IDX.file == "rd_ebay"].evidence_id)
def norm(s): return re.sub(r"\s+", " ", s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')).strip()
def window(eid):
    t = norm(ROW[eid].text); t = re.sub(r"\[\{'id'.*$", "", t).strip()
    return t[:max(READ_CHARS.get(eid, 0), 120)].lower()
def author(eid):
    r = ROW[eid]; f = r.file
    if f in ("tt_direct", "tt_comm"):
        m = re.search(r"@([^/]+)", r.link); return "tiktok:" + (m.group(1) if m else "?")
    if f == "tt_comments": return "tiktok-commenter:" + r.author
    if f in ("rd_broad", "rd_ebay"): return "reddit:" + r.author
    if f == "yt_titles": return "youtube-channel:" + r.author
    if f == "yt_comments": return "youtube-commenter:" + r.author
    if f == "yt_chat": return "chat:" + r.author
    return "?"
# ---- key phrases per cited row, taken from the read windows (cited_rows_read_window.txt). Keys are the abbreviated
# forms used in the ledger builder; matching is by prefix on the ID's platform part.
P = {
 # XC-F1 eBay Live captions (13 tagged, 9 untagged)
 "local_c67838ae": ["ebay live is genuinely my new addiction", "ad"], "local_88af59ae": ["pokémon card shopping on a budget with the help of ebay live"],
 "local_e9c4f012": ["ebay live hat viele verborgene schätze", "#anzeige"], "local_da33bf27": ["tune into ebay live streams all weekend", "#ebaypar"],
 "local_8c6ebc99": ["deal i found on ebay live", "#ebaypartner"], "local_30074f15": ["ebay live found my weakness", "#ad"],
 "local_0f95bced": ["on ebay live", "#ebaypartner"], "local_e7440057": ["i find the sickest pieces on ebay live", "#ebaypartner"],
 "local_c782f692": ["@ebay live is a thrilling and easy way to shop", "#ebaypartner"], "local_627a60aa": ["it all happens on @ebay live", "#ebaypartner"],
 "local_08c305fe": ["ad |", "@ebay uk live"], "local_0a5a262f": ["ebay endless runway live auction", "#ebaypartner"],
 "local_57f2669b": ["hunting for gems on ebay live", "#ebaypartner"],
 "local_f7626202": ["join my new ebaylive with authentic autographs"], "local_63c645f2": ["we're going live on ebay", "first abugkicks live show"],
 "local_e1a367bc": ["#ebaylivestream"], "local_51ab5800": ["ruben is on ebay live with an etb for a penny"],
 "local_447635e8": ["for pricing during whatnot, tiktok and ebay live stream, go to pricehud.com"], "local_ef973161": ["live on ebay", "#ebaylive"],
 "local_8ab883e5": ["pokémon 30th anniversary launch on ebay live"], "local_ae88b484": ["join our insane live ebay events", "ebay.com.au/ebaylive"],
 "local_dc672028": ["ebay live at 7pm tonight", "starting bid £200"],
 "t3_1vub4yy": ["ebay live auctions - absolutely senseless", "silver coin dealer's stream", "quick 10 second reset flash auctions"],
 "t3_1pttt05": ["ebay live auction switcheroo", "he had ripped the box"], "t1_nvjpmsu": ["it auto pays with no options to cancel"],
 "UgzrDtVVH-e2hHYihvR4AaABAg": ["first experience with ebay live", "pre-loaded for a live show"],
 "UgzfGt8L5RoXYTzy7Ul4AaABAg": ["as a buyer who spent $17k on ebay live with seller vookum", "never honored"],
 "t1_p50mp5r": ["sells a lot on ebay live streams and we do well", "(comics)"], "P-F3SpVz-CQ": ["unboxing a preloved chanel bag on ebay live uk"],
 "t1_p56yrbz": ["ebay live will do well for sellers, while it's still highly promoted", "artifical supply/demand"],
 # XC-F2 authentication
 "t3_1todhm0": ["this is how a $1000 purchase from ebay authenticity arrives"], "t3_1r8eukv": ["dark side of ebay's authenticity guarantee"],
 "t3_1u2j162": ["ebay authenticator makes a mistake, costs me a $750 sale"], "t3_1o7ekel": ["magikarp denied by ebay authentication", "gave me refund"],
 "UgySNeVlZQU48YJR_Dd4AaABAg": ["just saved me from a purchase", "two creases that werent on listing"], "t1_niwjhum": ["approved the appeal", "impressed with tim"],
 "t1_ovl1bk3": ["i see ebay authentication sticker", "the authenticator would of flagged it"],
 "t1_ns0iwn6": ["i ended up buying on ebay", "authenticity guaranteed", "aussie dollar"], "t1_ns19b9p": ["i buy all my shoes off ebay", "the ebay authenticate is another plus"],
 "t1_odl74kz": ["their service sucks", "passed it as approved"], "t1_odkd14k": ["ebay has your back"],
 "t3_1s8y9k4": ["99.7% positive feedback", "did not have the \"authenticity guarantee\" badge"], "t3_1q53zhu": ["they failed to authenticate it!? why???"],
 "Ugy-N4vfOHdqoFxnakZ4AaABAg": ["i ordered over 200 pairs the past year", "taking 30 days to ship a shoe after it's authenticated"],
 "t1_p5ij8ks": ["i sold a rolex on ebay", "because they authenticated the watch", "claimed empty box"], "t3_1tz0dbm": ["pull the trigger on a daytona", "found my winner on ebay and read up on their authentication process"],
 "Ugy1zfbMf-NlX2W_69p4AaABAg": ["regularly buying watches on ebay, mostly from japan", "i trust ebay's authentication service"],
 "UgwAqcvWStAcfOH6nl94AaABAg": ["breitling avenger off ebay", "2 lv purses", "ebay authentication is great"],
 "t1_ofgfyui": ["you're on your own in terms of authentication", "purse forum", "japanese seller"], "t1_opkfisj": ["ebay authenticity guaranteed protects you"],
 "t1_p7yaxpk": ["authenticity guarantee programme would be an exception", "selling is definitely not for me"],
 "t3_1qpssd0": ["lv wallet on whatnot", "resold the item on ebay", "counterfeit"], "local_a210513c": ["authenticity guarantee service", "#ebaypartner"],
 "t3_1llzc73": ["bought two gold bars and both were fake", "ebay permanently suspends my account"], "t1_n03y0q8": ["never buy gold from ebay"],
 "t1_n03l086": ["avoid ebay for gold purchases, unless it's an official account from someplace reputable like apmex"],
 "t1_njn42rr": ["i don't trust ebay auth", "failed inspection"], "t1_o65m5pj": ["passed through ebay authentication", "didn't catch a crease"],
 "t1_o64ua2i": ["if the card was authenticated with or without any damaged notice, you wont be able to return it"], "t3_1om25vd": ["sent me a fake card", "beckett"],
 # XC-F3 / SC-F4 Whatnot and live buyers
 "t1_owwn39k": ["did i bid $10 or did it jump to $30", "3-5second sudden death", "loads of seller do 5s or less"],
 "t1_omvn0rt": ["as a buyer i just want to buy stuff and move on", "notifications"], "t1_oeva9nx": ["i buy things to flip from them because many buyers go on \"hype\""],
 "t1_oydr557": ["avoid breaks and impulse buys", "use the app muted"], "t1_oyo6r47": ["paying double market value to have a pack ripped"],
 "t1_p50jtgt": ["the amount of notifications they keep sending for live auctions is becoming infuriating"],
 "t1_oyfrxmd": ["bought probably a 1000 items", "better experience than ebay"], "t1_p4zsiqf": ["this is how most streams work", "you can get some great deals"],
 "t1_oz5yrln": ["filled with counterfeit and fakes"], "t1_p1ynv3d": ["8 of them were scams"],
 "t1_p7hz8rr": ["ebay for singles that you know will sell for close", "whatnot for moving singles faster"], "t1_p7hxipn": ["lucky to have 6 viewers", "95% of my cards @ $1"],
 "t1_p7nasw9": ["gave up on whatnot and list on ebay"], "t1_no39bxl": ["$3 each ($15 total)", "i'd rather just make my money on ebay"],
 "t1_nn69yj9": ["you don't have to have a pre-existing following to do well on whatnot"],
 "t1_omuylg3": ["it's just for liquidation", "i put the good stuff on ebay", "more intelligent clientele"], "t1_nseqlli": ["have you watched any whatnot auctions", "watching different shows"],
 # XC-F5 markets
 "local_061e0f6f": ["vintage designer brands @ebay uk"], "local_e1b518bb": ["#ad", "@ebay uk small businesses"], "local_39bd7ce1": ["#ad", "@ebayau", "authenticity guarantee"],
 "local_4e90086b": ["151 illustration rares on ebay", "australia"], "local_db4809ac": ["finds ehrlich so crazy"], "local_4defa3ab": ["#modellbahn"],
 "local_f59398a7": ["how to- shop on japanese ebay", "authenticating and finding a seller"], "t1_omyw8vx": ["germany", "uk"],
 # SC
 "local_9cc53f16": ["$1,000 sports card negotiation", "#cardshow"], "local_496c6391": ["ebay is now reliable for new folks searching for comps"],
 "local_41e91d56": ["i win a lot of cards under comps"], "local_332a15b5": ["cards you buy can be investments", "#ebay"],
 "t3_1u5s64o": ["psa authentication box arrived empty"], "t3_1uvql6e": ["seller cancels before you can check out"], "t3_1om8vct": ["seller cancelled my yamamoto card"],
 "t3_1o6m3c3": ["fake or ai generated card listed by huge ebay seller"], "t3_1qkscsr": ["exact same slab. which one's fake"], "t3_1thre78": ["don't drink and ebay"],
 "t3_1r1a00m": ["sold a card on ebay to ryan gusto's dad"],
 "local_a45d15cb": ["find your daily breaks located in our tiktok shop"], "local_ddb3b62a": ["find your daily breaks located in our tiktok shop"],
 "local_475e17cc": ["find your daily breaks located in our tiktok shop"], "local_345a885e": ["find your daily breaks located in our tiktok shop"],
 "_rDm8b0LVNQ": ["ebay thursday", "hobby box break"], "iPU9AoWlaBw": ["ebay wednesday", "hobby box break"], "LPZ7wtjacn4": ["ebay sunday", "hobby box break"],
 "EfYNvpJtWmQ": ["hobby box ebay break"], "bElKFZcvfg0": ["ebay-", "case pick your character"], "zlDlWR6W7h0": ["ebay monday", "hobby box break"],
 "sWYyT7Ex69o": ["hobby box ebay break"], "Srwgb5wXrZw": ["ebay live stream", "#boxbreak"], "bPXCFwpSq8c": ["ebay thursday", "hobby box break"], "tSw3RM7K1xM": ["hobby box ebay break"],
 "Zjj_1OX-Gbs": ["$250 hobby boxes vs. $250 retail boxes"], "FaILPcpLD1s": ["mystery packs"], "SzVWf_A4BUo": ["opening high end sports card boxes"],
 "MtNpAZWnn6I": ["$1 sports card boxes"], "xeMKnCDtNhM": ["mystery box from a random ebay seller"], "QyAXNatU8Mo": ["sketchiest sports card mystery boxes on ebay"],
 "local_d1533050": ["@whatnot", "#whatnotpartner"], "local_0f3f1249": ["fake world cup panini boxes", "on ebay"],
 "local_a42343e4": ["ebay authentic explainer - chips tips"], "local_edf5696e": ["authenticity guarantee has been tough lately", "lots of cards failing"],
 # PK
 "local_14590272": ["should i open it? or should i keep it sealed?", "30th celebrations"], "local_4b8b0af8": ["nothing like psa grading to humble you", "250 dollars later"],
 "local_2a99087e": ["costco", "pokémon ascended heroes mini tin"], "local_cbfaedb7": ["massive walmart drop tonight"], "local_de2688c1": ["how to cop every pokemon 30th celebration drop"],
 "local_d780fa1b": ["pokémon scalpers have finally lost"], "local_4e77c895": ["psa's new grading tiers"],
 "local_0bfd1c9e": ["packing a pokemon card order for ebay", "theu move so fast"], "local_53082fbb": ["i sold my 1st edition pikachu on @ebay"],
 "t3_1pbo9ic": ["beware of ebay scammer", "obviously a counterfeit"], "t3_1qd1fa4": ["ebay seller beware", "return request and was denied"],
 "t3_1u15aox": ["seller immediately deleted their account", "given a refund"], "t3_1r3ngpa": ["ebay authenticator says my $1000 card was damaged"],
 "t3_1qvaf6c": ["psa submission lost in usps mail, later resurfaced on ebay"], "t1_njn3ck9": ["we need this for uk"],
 "t1_o64ybsb": ["still be protected by ebays money back guarantee"], "t1_o64htk9": ["ebay is right in that a psa 7 is still technically near mint"],
 "t1_o64o8wg": ["the damage wasn't in the listing photos"], "t1_o9yqku1": ["i rarely ever have this happen with mtg, lorcana, one piece"],
 "tiktok_comment:7686279334882460446": ["exeggutor is already $3 on tcg player"], "tiktok_comment:7686267440066134814": ["your prices are way off"],
 "19bmF518whA:1393": ["whats the price on that one"],
 "t1_oqnhajy": ["one piece cards"], "t1_oony44l": ["long time mtg collector"], "t3_1pcpv9c": ["yu-gi-oh nikes", "ebay has them too with the authenticity guarantee"],
 "UgxYEXDXDWSVi1wR2Jh4AaABAg": ["psa & fanatics"],
 # SN
 "local_13d7da97": ["head over to our ebay shop"], "local_53a90dd5": ["my ebay store just died", "$320 sold overnight"], "local_7551ae4b": ["selling authentic trainers on ebay", "ebay.co.uk"],
 "local_bf98b74d": ["off ebay", "hopefully i can return this junk", "#fakejordans"], "local_3663ef62": ["shop with us on ebay", "#newjersey"],
 "t3_1nzw8nl": ["goat or ebay"], "t1_niwc5vg": ["most ebay sellers also post pics of the shoes you'll actually be getting"],
 "local_9834883a": ["current sneaker rotation"], "local_70b7ebe2": ["10 fire shoes under $100"],
 "UgxbPBFfSv3Tyf-ofop4AaABAg": ["just bought my first ever jordan. i am in uk", "afraid that i received the rep"],
 # LX
 "local_e355b2cc": ["never doubt an ebay find"], "local_0bd4eacd": ["@ebay always has the best finds"], "local_d6e870d2": ["@gucci @ebay seller was aikidoll"],
 "local_71ce9e5c": ["i would suggest checking ebay first", "my list of trusted sellers"], "local_d0324d97": ["#ebayminikelly"], "local_cdcaeca8": ["how to shop on japanese ebay for luxury items"],
 "-TgKIoItPPM": ["lv speedy 25 from japanese ebay"], "8ATRm1Bp1sU": ["from japanese ebay"], "local_5afb86bf": ["#designerbag", "#ebay #mercari"],
 "t3_1sbzdvx": ["new to this thread", "listings on depop and ebay"], "t3_1shwwz7": ["newbie to the second hand luxury bag market", "identical listing photos"],
 "t1_p8kecsh": ["the returns go back through ebay's authenticator"], "local_3e70873d": ["ebay's authentication program is in a class by it self", "qc consigns"],
 "t3_1oe3rv0": ["never sell luxury items on ebay", "louis vuitton bucket hat"], "t1_nkykxsw": ["would also never sell watches"], "t1_nlai4ln": ["worked as ebay customer service", "just don't sell any luxurious stuff"],
 "t1_nkynsy1": ["they all go to an authenticator first which gives me peace of mind"], "t1_p5gv32z": ["i've sold many watches on ebay and never had an issue"],
 "local_0ada9f21": ["mega live alert", "#auction #chanel"], "local_cec361e6": ["pre loved luxury bags", "#tiktokshop"],
 "t3_1vweez9": ["ebay sucks and why is selling watches such a pain", "grailzee, bezel, ebay, chrono24"], "t1_p5gahje": ["ebay's seller protection is basically a myth", "watchexchange"],
 "t1_p5gb6s4": ["it's a jungle out there for buyers too"], "t1_p5gbcao": ["as an inexperienced buyer i would have trouble trusting random sellers on reddit"],
 "t1_oq7fajb": ["which listings they will authenticate"], "t3_1oqfzzy": ["trustworthiness of ebay listings for rolexes", "i am 100% certain this is a fake"],
 "t3_1p7d9qr": ["ebay black friday", "5,000+"], "t1_nqybkth": ["ebay sellers are typically trustworthy in quality and condition besides authenticity?"],
 "local_ac2e94cb": ["my first vintage watch unboxing from ebay"], "local_d21a49d8": ["#watchhospital", "#ebay"], "hWJ0uGyO1Pk": ["omega constellation passed ebay's authentication"],
 "local_d886ed8f": ["most vintage designer clothing isn't even designer", "understand licensing"], "local_43581f51": ["vintage designer purchases from ebay"],
 "local_714e362b": ["expensive men's fragrance from ebay", "#fail"], "local_43dc3f74": ["how to list cologne on ebay"], "urGSyXd0wCo": ["spot fake perfume on ebay"],
 # EL
 "local_71c0aed9": ["kodak easyshare c182 - i got it for $35 on ebay"], "local_ced29739": ["which digicams should you buy in 2026"], "local_c31e3095": ["burned by dishonest japanese ebay film camera sellers"],
 "local_b905f0ac": ["bolo! sony a7riii for $325", "#reseller"], "local_03bf9280": ["$4,134 sold on ebay today", "1950s nikon rangefinder"], "local_27a9e453": ["my ipod collection"],
 "local_58c394ee": ["this is so nostalgic #ipod"], "local_ffb78543": ["40,000 retro games for this price", "#tiktokshopcreatorpicks"], "local_af01bbb0": ["15,000 other games"],
 "local_d1016b2a": ["i hope i didn't get scammed. ps5 from ebay"], "local_6ef354d1": ["bug infested broken xbox off ebay"], "local_ce987d6e": ["nikon coolpix 3600, sourced from ebay"],
 "t3_1wphbkz": ["roach infested", "xbox one x"], "local_dfb628f8": ["refurbished one off of ebay", "missed these console sounds"], "local_2346635f": ["run on ebay", "#digitalcameras"],
 "t3_1r91qdw": ["packaged phone in mayonnaise packets"], "t3_1ojc3n1": ["cpu i purchased from ebay has a warranty void if removed sticker"],
 "t1_nm1ytgc": ["resellers way of weeding out the people"], "local_372655cc": ["20k juegos retros"], "local_1af7f3b9": ["what sold on ebay today"], "local_3cc532cf": ["off ebay, and this one was sold untested", "whether it actually worked"],
 # TY
 "local_d18974a6": ["literally the last one in all az targets", "#popmart"], "local_a379d291": ["disney blind boxes at the drop shop"], "local_0e1abd6b": ["skullpanda", "#popmart"],
 "local_631e6ad9": ["#dababy unboxes #labubu"], "local_3ca5b7c3": ["space molly blind box"], "local_bf4de5e6": ["why did you waste your money", "#overconsumption"],
 "local_4472cc81": ["couldn't justify some of the prices i was seeing on ebay", "mercari through jpfans"], "local_cfb33c9b": ["about 70$ while it goes for 150$ on ebay"],
 "local_9aa09393": ["what did i get from ebay? #transformers"], "local_e46e35fa": ["marketplace for the win", "#toycollector"],
 "t3_1skd4mg": ["bought my dream item from a seller with good reviews", "figure"], "t3_1txny14": ["paper towels as the only packaging material", "anime figures"],
 "t1_opzx1zy": ["replace it with how well the seller packaged the item"], "t1_odxel8c": ["scam, never go off ebay"],
 "local_352f0ba9": ["running 4 trains", "#lionel"], "local_e3650793": ["plano train show", "60+ vendors"], "local_45817e9a": ["rocky mountain train supply"],
 "local_99a07423": ["my first ever n scale locomotive", "doing whatever on ebay importing random stuff"], "local_13a61846": ["kato", "check this out on my shop"],
 "local_667ec305": ["my first ebay purchase, and i'm so happy", "#barbiefashionistas"], "local_1244835c": ["comprar lotes de muñecas en ebay"], "local_7d25e976": ["comprar lego en ebay desde méxico"],
 "local_17dd2552": ["hunting for vintage toys at goodwill to resell on ebay"], "local_3135e0e8": ["rare dr. pepper jellycat"], "local_24b4ad5a": ["don't pass up plush at the thrift stores", "#ebay"],
 "local_11c6d089": ["vintage pins/buttons from ebay"], "local_6db83504": ["4 years of collecting", "#mylittlepony"], "tiktok_comment:7641731808408814367": ["ill take them"],
 "local_7f7b4dda": ["wtf is a labubu"],
 # CN
 "local_6bcfb3ca": ["collects coins", "#policepatch"], "t1_n03q3iy": ["ebay will always 100% honor \"not as described\" returns"], "t3_1ufxb7r": ["8 oz of silver", "fake"],
 "t1_otwj817": ["around april 7, ebay shortened the window", "3 calendar days"], "t3_1qcvle6": ["on a coin i have for sale"],
 "t1_n04bfny": ["sold me a cleaned coin as xf", "ngc", "the seller was able to remove it"], "t1_oygq7h6": ["adjust my coin prices based on what the spot price was of silver"],
 "t1_p515n9w": ["sounds like the home shopping network"], "t1_p56jodo": ["have not won any livestream bids"],
 # AB
 "local_cabc61bd": ["ebay dress haul #vintage#1950s"], "local_9c4a18de": ["#ebayhaul"], "local_0474b192": ["my fave vintage brands to search up! #ebayhaul"],
 "local_8ecc6ac8": ["petit haul vinted"], "local_cff44bce": ["camisetas vintage vendidas en ebay", "#reseller"], "local_13745f76": ["goodwill", "#resellercommunity #ebay"],
 "local_bcddb583": ["how to cop unique pieces on ebay", "#ad"], "local_145097e1": ["ebay/ thrift pickups", "affordable pieces"], "local_6fd13074": ["underrated secondhand and vintage platforms", "#ebay"],
 "local_9520b23f": ["for sale on depop and ebay"], "local_1e0184bc": ["vinted & depop", "#reseller"],
 "local_5cc71701": ["nypd & nyc sheriff patch", "#patchcollector"], "local_dbb48dcc": ["battle jackets"], "local_a203c31d": ["battle vest", "#battlejacketslondon"],
 "local_0089e5d6": ["button press", "hhn trades"], "local_5cdeaba6": ["buttons, buttons, and more buttons", "inventory"], "local_c5f13424": ["hook-backed patches", "#tiktokshopstockup"],
 "local_b441c945": ["lee jeans rider jacket on ebay for $25", "also from @ebay, i found tons of different vintage and antique red wings"], "local_8a4ab98c": ["restock buttons with me! #etsy"],
 "local_e4b6e736": ["4k steelbook", "complete this trilogy"], "local_4492b026": ["over 5000 movies"], "local_4a91348f": ["4k bluray collection"], "local_e4e363d3": ["thrift", "#vhs"],
 "local_8459de44": ["found on ebay and bought instantly"],
 "local_1dd1a5d8": ["i bought the ebay engine"], "local_daced285": ["i bought this motor on ebay 6 years ago", "harley"], "local_fe0afbcf": ["the ol ebay motor was ripping", "#ebaymotors"],
 "local_b80372ee": ["best ya to win an ebay auction every time", "ek civic cluster"], "local_a72c7e8c": ["check out our ebay store link in bio", "#classiccar"],
 "local_a4d89264": ["disponibile per ricambi", "#autodemolizione#ebay#ricambiusati"], "local_21b424cb": ["wholesale of auto parts"], "local_97b9ca83": ["#ebay #reseller #autoparts"],
 "t3_1qjabr7": ["engine from a salvage yard ebay seller", "collections agency"], "t1_o0zedv8": ["who's silly enough to sell engines on ebay too"], "t1_olpp167": ["$2300 is about right"],
 "t3_1wfp5sj": ["demise of ebay live auction", "force feed"], "t1_p9o48gb": ["car crash video streaming", "worst ebay feature yet"], "t1_p9ojy91": ["sports/tcg and memorabilia channels arent going anywhere", "gambling addicts"],
 "t1_p7xb529": ["i hate ebay live"], "t1_ocus8sv": ["even as a high-use seller", "my homepage bombards me with livestreams"], "t1_pa2yhrf": ["i will never try the ebay live auction"],
 "t3_1s5ae92": ["whenever ebay pushes their live auctions", "traffic and sales drop"], "UgxbPcydBm_M7LfisLt4AaABAg": ["it's a notification for ebay live"],
 "wbUy3gK7kFE:690": ["selling on ebay versus whatnot"], "wbUy3gK7kFE:708": ["whatnot shop on vacation mode"], "wbUy3gK7kFE:709": ["busy with a locker"],
 "Eq1xymBqpnk": ["sell on tiktok live or whatnot"], "EtOrAojxRqI": ["tiktok shop livestream seller"], "myCuDV9-2-M": ["$1.5m a month"],
 "d3uHPsnoITc": ["ebay for sellers webinar"], "DjsWZaPwMQs": ["ebay live seller panel"], "y-NqOxTOXP0": ["on ebay live"],
}
def key_for(eid):
    plat, rest = eid.split(":", 1)
    for k in P:
        if plat == "tiktok_video" and k.startswith("local_") and rest.startswith(k): return k
        if plat == "reddit" and rest == k: return k
        if plat == "youtube_comment" and rest == k: return k
        if plat == "youtube_video" and rest == k: return k
        if plat == "youtube_live" and rest == k: return k
        if plat == "tiktok_comment" and eid == k: return k
    return None
# ---- manual flags: rows whose text is in the window but does not carry the support the prose implied
FLAGS = {
 "XC-F1": ["local_e1a367bc: the caption is a hashtag mention (#ebaylivestream) with no announcement; role unknown. Statement corrected: 8 untagged captions are announcements or a tool ad, 1 is a hashtag-only mention.",
           "Repeated creator: local_627a60aa and local_57f2669b are the same partner creator (yulingwu); 13 tagged captions come from 12 creators."],
 "SC-F2": ["Repeated creators: the 4 read TikTok Shop captions are one creator (burtonbreaks); the 10 eBay-break titles come from 4 channels (Bomber Sports Cards 5, Roper's Rips 3, Best Card Breaks 1, SD Breaks 1); the entertainment titles come from 2 channels (TRIKE 3, Wayne Collection 3)."],
 "TY-F1": ["Repeated creator: the two train captions naming eBay (local_99a07423, local_3cc532cf) are from two creators (idktrains, robertscreations); local_13a61846 and local_4defa3ab are also idktrains. Statement corrected to name creators.",
           "local_0e1abd6b is from the handle popmartunboxing.us; whether it is Pop Mart itself is unverified (report §3.6 block 6 corrected)."],
 "TY-H2": ["As TY-F1: eBay is named in captions from two train creators, one of whom (idktrains) also runs a shop."],
 "EL-F2": ["Repeated creator: both what-sold rows are one creator (finestflips)."],
 "AB-PA-F1": ["local_21b424cb ('Wholesale of auto parts for Audi…') does not name eBay in its caption; it sits in the eBay-term pull. It is a parts-seller presence row, not an eBay-store routing row. Statement corrected."],
 "LX-W-F1": ["local_d21a49d8 is hashtags only (#watchhospital … #ebay); 'watch repair' is inferred from the hashtag and handle, not stated. t1_p5gb6s4 and t1_p5gbcao are the same commenter (improvthismoment)."],
 "SN-F1": ["t1_ns0iwn6 and t3_1pcpv9c (cited in PK-F5) are the same person (DeGuyWithDeOpinion): one AU buyer, not two."],
 "AB-TV-F1": ["local_8ecc6ac8 is a Vinted haul in French and does not name eBay; it is cited for the Vinted-alongside-eBay point only. local_bcddb583 carries #AD (promotion)."],
 "CN-F1": ["local_6bcfb3ca asks whether police departments give collectors free coins; 'challenge coin' is inferred from the patch-collector context, not stated."],
}
# ---- run
led = list(csv.DictReader(open(os.path.join(HERE, "..", "claim_ledger.csv"), encoding="utf-8")))
report = {}; new_rows = []
for c in led:
    ids = [i.strip() for i in c["Full evidence IDs (flash_evidence_row_id)"].split(";") if i.strip()]
    cids = [i.strip() for i in c["Counterevidence (IDs)"].split(";") if i.strip() and i.strip() != "none found"]
    missing, nokey, checked = [], [], 0
    for eid in ids + cids:
        k = key_for(eid)
        if k is None: nokey.append(eid); continue
        w = window(eid); checked += 1
        miss = [p for p in P[k] if p.lower() not in w]
        if miss: missing.append({"id": eid, "phrases_not_in_read_window": miss})
    authors = sorted({author(e) for e in ids})
    shared = [e for e in ids + cids if e in SHARED]
    status = "supported" if not missing and not nokey else "FLAGGED"
    if c["Claim ID"] in FLAGS: status = "supported with notes" if status == "supported" else "FLAGGED"
    if not ids: status = "code count (no cited rows)"
    report[c["Claim ID"]] = {"status": status, "rows_checked": checked, "missing": missing, "no_key_phrase": nokey,
                             "distinct_authors": len(authors), "authors": authors, "shared_reddit_rows": shared, "notes": FLAGS.get(c["Claim ID"], [])}
    c["Support check"] = status + (f"; {len(missing)} row(s) missing phrase" if missing else "") + (f"; {len(nokey)} row(s) without key phrase" if nokey else "") + ("; notes: " + " | ".join(FLAGS[c["Claim ID"]]) if c["Claim ID"] in FLAGS else "")
    c["Distinct authors behind cited rows"] = f"{len(authors)} ({', '.join(a.split(':',1)[1] for a in authors)})" if authors else ""
    c["Shared Reddit rows cited"] = "; ".join(shared) if shared else "none"
    new_rows.append(c)
json.dump(report, open(os.path.join(HERE, "stage3_claim_support_report.json"), "w"), indent=1)
with open(os.path.join(HERE, "..", "claim_ledger.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(new_rows[0].keys())); w.writeheader(); w.writerows(new_rows)
tot = len(report); ok = sum(v["status"].startswith("supported") for v in report.values())
print(f"claims {tot}; supported {ok}; flagged {sum(v['status']=='FLAGGED' for v in report.values())}; code-count {sum(v['status'].startswith('code') for v in report.values())}")
for k, v in report.items():
    if v["missing"] or v["no_key_phrase"]:
        print(k, v["status"], json.dumps(v["missing"])[:600], v["no_key_phrase"][:5])
print("shared Reddit rows cited anywhere:", sorted({e for v in report.values() for e in v["shared_reddit_rows"]}))
