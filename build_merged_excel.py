import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# ─────────────────────────────────────────────────────────────────────────────
# Merged brand data
# Fields: (rank, brand_jp, brand_en, category, country, ig_account, ig_url, x_account, x_url, notes)
# rank = None for File2-only brands not in File1
# ─────────────────────────────────────────────────────────────────────────────

data = [
    # ── File1 brands (with rank) ─────────────────────────────────────────────
    (2,   "メディヒール",           "Mediheal",                "スキンケア",           "韓国",       "@mediheal_jp",                   "https://www.instagram.com/mediheal_jp",              "@mediheal_jp",        "https://x.com/mediheal_jp",         ""),
    (3,   "CURLYSHYLL",             "Curlyshyll",              "ヘアケア",             "韓国",       "@curlyshyll_jp",                 "https://www.instagram.com/curlyshyll_jp",            None,                  None,                                ""),
    (4,   "COSRX",                  "COSRX",                   "スキンケア",           "韓国",       "@cosrx_jp",                      "https://www.instagram.com/cosrx_jp",                 "@COSRX_JAPAN",        "https://x.com/COSRX_JAPAN",         ""),
    (6,   "celimax",                "celimax",                 "スキンケア",           "韓国",       "@celimax.japan",                 "https://www.instagram.com/celimax.japan",            None,                  None,                                ""),
    (7,   "LEPOREM",                "Leporem",                 "スキンケア",           "韓国",       "@leporem_japan",                 "https://www.instagram.com/leporem_japan",            None,                  None,                                ""),
    (13,  "アレンシア",             "Arencia",                 "スキンケア",           "韓国",       "@arencia_jp",                    "https://www.instagram.com/arencia_jp",               None,                  None,                                ""),
    (14,  "VTコスメティックス",     "VT Cosmetics",            "スキンケア",           "韓国",       "@vtcosmetics_japan",             "https://www.instagram.com/vtcosmetics_japan",        "@vtcosmetics_jp",     "https://x.com/vtcosmetics_jp",      ""),
    (15,  "by TREES",               "by TREES",                "スキンケア",           "韓国",       "@twotreesjp",                    "https://www.instagram.com/twotreesjp",               "@byTREES_jp",         "https://x.com/byTREES_jp",          ""),
    (21,  "ベントン",               "Benton",                  "スキンケア",           "韓国",       "@bentoncosmetic.jp",             "https://www.instagram.com/bentoncosmetic.jp",        None,                  None,                                ""),
    (22,  "Sung Boon Editor",       "Sung Boon Editor",        "メイク",               "韓国",       "@sungbooneditor_global",         "https://www.instagram.com/sungbooneditor_global",    None,                  None,                                ""),
    (23,  "MADAME lash",            "MADAME lash",             "まつ毛・まゆ毛",       "韓国",       "@madamelash_jp",                 "https://www.instagram.com/madamelash_jp",            "@Madame_Lash",        "https://x.com/Madame_Lash",         ""),
    (24,  "メディキューブ",         "Medicube",                "スキンケア",           "韓国",       "@medicube_officialjapan",        "https://www.instagram.com/medicube_officialjapan",   "@medicube_japan",     "https://x.com/medicube_japan",      ""),
    (25,  "no:prob",                "no:prob",                 "スキンケア",           "韓国",       "@noprob_jp",                     "https://www.instagram.com/noprob_jp",                "@NoBoyNoProb",        "https://x.com/NoBoyNoProb",         ""),
    (26,  "AGE20'S",                "AGE20'S",                 "メイク",               "韓国",       "@age20s_jp",                     "https://www.instagram.com/age20s_jp",                None,                  None,                                ""),
    (27,  "Biodance",               "Biodance",                "スキンケア",           "韓国",       "@biodance_japan",                "https://www.instagram.com/biodance_japan",           None,                  None,                                ""),
    (31,  "Néjoo",                  "Nejoo",                   "スキンケア",           "韓国",       "@nejoo__jp",                     "https://www.instagram.com/nejoo__jp",                "@njoo_raw",           "https://x.com/njoo_raw",            ""),
    (32,  "TFIT",                   "TFIT",                    "スキンケア",           "韓国",       "@tfit.japan",                    "https://www.instagram.com/tfit.japan",               "@tfit_universe",      "https://x.com/tfit_universe",       ""),
    (37,  "アイムフロム",           "I'm From",                "スキンケア",           "韓国",       "@imfrom_jp",                     "https://www.instagram.com/imfrom_jp",                "@imfrom_jp",          "https://x.com/imfrom_jp",           ""),
    (38,  "Julie's Lip",            "Julie's Lip",             "リップ",               "韓国",       "@julieslip_official",            "https://www.instagram.com/julieslip_official",       None,                  None,                                ""),
    (39,  "アヌア",                 "Anua",                    "スキンケア",           "韓国",       "@anua.jp",                       "https://www.instagram.com/anua.jp",                  "@anua_official",      "https://x.com/anua_official",       ""),
    (42,  "コスノリ",               "Cosnori",                 "メイク",               "韓国",       "@cosnori_jp",                    "https://www.instagram.com/cosnori_jp",               "@cosnori_jp",         "https://x.com/cosnori_jp",          ""),
    (43,  "アミューズ",             "AMUSE",                   "メイク",               "韓国",       "@amuse.jp",                      "https://www.instagram.com/amuse.jp",                 "@amuse_official",     "https://x.com/amuse_official",      ""),
    (45,  "23yearsold",             "23yearsold",              "スキンケア",           "韓国",       "@23yearsold.jp",                 "https://www.instagram.com/23yearsold.jp",            "@23yo_official",      "https://x.com/23yo_official",       ""),
    (47,  "TOCOBO",                 "TOCOBO",                  "スキンケア",           "韓国",       "@tocobo_jp",                     "https://www.instagram.com/tocobo_jp",                None,                  None,                                ""),
    (48,  "ABOUT TONE",             "About Tone",              "スキンケア/メイク",    "韓国",       "@about___tone_jp",               "https://www.instagram.com/about___tone_jp",          None,                  None,                                ""),
    (49,  "イニスフリー",           "Innisfree",               "スキンケア",           "韓国",       "@innisfreejapan",                "https://www.instagram.com/innisfreejapan",           "@innisfreeJapan",     "https://x.com/innisfreeJapan",      ""),
    (52,  "スキンアンドラブ",       "Skin&Lab",                "スキンケア",           "韓国",       "@skinnlab_japan",                "https://www.instagram.com/skinnlab_japan",           None,                  None,                                ""),
    (54,  "BnD",                    "BnD",                     "スキンケア",           "韓国",       "@bndofficial.jp",                "https://www.instagram.com/bndofficial.jp",           "@BnD_official_jp",    "https://x.com/BnD_official_jp",     ""),
    (55,  "XIXI",                   "XIXI",                    "メイク",               "中国",       "@xixi.tokyo",                    "https://www.instagram.com/xixi.tokyo",               "@xixi_cool",          "https://x.com/xixi_cool",           ""),
    (57,  "UIQ",                    "UIQ",                     "スキンケア",           "韓国",       "@uiq_official",                  "https://www.instagram.com/uiq_official",             "@uiq_japan",          "https://x.com/uiq_japan",           ""),
    (58,  "MAWLAB",                 "MAWLAB",                  "スキンケア",           "韓国",       "@mawlab_",                       "https://www.instagram.com/mawlab_",                  None,                  None,                                ""),
    (61,  "Laka",                   "Laka",                    "メイク",               "韓国",       "@laka.beauty.japan",             "https://www.instagram.com/laka.beauty.japan",        "@BeautySalonLaKa",    "https://x.com/BeautySalonLaKa",     ""),
    (62,  "ブラン",                 "Blanc Nature",            "スキンケア",           "韓国",       "@blanc_official.jp",             "https://www.instagram.com/blanc_official.jp",        "@blancnature_jp",     "https://x.com/blancnature_jp",      ""),
    (63,  "エイプリルスキン",       "April Skin",              "スキンケア/メイク",    "韓国",       None,                             None,                                                 "@aprilskin_japan",    "https://x.com/aprilskin_japan",     ""),
    (72,  "AZTK",                   "AZTK",                    "スキンケア",           "韓国",       "@aztk.official",                 "https://www.instagram.com/aztk.official",            "@azteccbd_japan",     "https://x.com/azteccbd_japan",      ""),
    (74,  "AESTURA",                "AESTURA",                 "スキンケア",           "韓国",       "@aestura_jp",                    "https://www.instagram.com/aestura_jp",               "@Aestura_jp",         "https://x.com/Aestura_jp",          ""),
    (76,  "SKIN1004",               "SKIN1004",                "スキンケア",           "韓国",       "@skin1004_japan",                "https://www.instagram.com/skin1004_japan",           "@skin1004_jp",        "https://x.com/skin1004_jp",         ""),
    (87,  "ララレシピ",             "Lara Recipe",             "スキンケア",           "韓国",       None,                             None,                                                 "@rara_fukinotou",     "https://x.com/rara_fukinotou",      ""),
    (99,  "V.Bio23",                "V.Bio23",                 "スキンケア",           "韓国",       None,                             None,                                                 "@v_rabbit_hole",      "https://x.com/v_rabbit_hole",       ""),
    (102, "ネイチャーリパブリック", "Nature Republic",         "スキンケア",           "韓国",       "@naturerepublic_jp",             "https://www.instagram.com/naturerepublic_jp",        "@Naturerepublic_",    "https://x.com/Naturerepublic_",     ""),
    (103, "ダルバ",                 "d'Alba",                  "スキンケア",           "韓国",       "@dalba_japan",                   "https://www.instagram.com/dalba_japan",              None,                  None,                                ""),
    (104, "セルフュージョンC",      "Cellfusion C",            "スキンケア",           "韓国",       "@cellfusionc_official_jp",       "https://www.instagram.com/cellfusionc_official_jp",  None,                  None,                                ""),
    (106, "SKIN GARDEN",            "Skin Garden",             "スキンケア",           "韓国",       "@skingarden.jp",                 "https://www.instagram.com/skingarden.jp",            None,                  None,                                ""),
    (110, "ラネージュ",             "Laneige",                 "スキンケア/メイク",    "韓国",       "@laneige_jp",                    "https://www.instagram.com/laneige_jp",               "@Laneige_japan",      "https://x.com/Laneige_japan",       ""),
    (116, "EIoM",                   "EIoM",                    "メイク",               "韓国",       "@eiom_jp",                       "https://www.instagram.com/eiom_jp",                  None,                  None,                                ""),
    (117, "ミルクタッチ",           "Milk Touch",              "メイク",               "韓国",       "@milktouch_japan",               "https://www.instagram.com/milktouch_japan",          "@milktouch_jp",       "https://x.com/milktouch_jp",        ""),
    (118, "BAREN",                  "BAREN",                   "スキンケア",           "韓国",       "@bharenn",                       "https://www.instagram.com/bharenn",                  "@barensub11",         "https://x.com/barensub11",          ""),
    (120, "セラディックス",         "Celadix",                 "スキンケア",           "韓国",       "@celladix_jp",                   "https://www.instagram.com/celladix_jp",              None,                  None,                                ""),
    (122, "ペリペラ",               "Peripera",                "メイク",               "韓国",       "@periperajapan",                 "https://www.instagram.com/periperajapan",            "@periperajapan",      "https://x.com/periperajapan",       ""),
    (126, "PERFECT DIARY",          "Perfect Diary",           "メイク",               "中国",       "@perfectdiary_japan",            "https://www.instagram.com/perfectdiary_japan",       "@PerfectDiary_jp",    "https://x.com/PerfectDiary_jp",     ""),
    (128, "ロムアンド",             "rom&nd",                  "メイク",               "韓国",       "@romand_jp",                     "https://www.instagram.com/romand_jp",                "@andbyromand",        "https://x.com/andbyromand",         ""),
    (134, "MilleFée",               "MilleFée",                "メイク",               "韓国",       "@millefee_official",             "https://www.instagram.com/millefee_official",        None,                  None,                                ""),
    (135, "JUDYDOLL",               "Judydoll",                "メイク",               "中国",       "@judydoll_jp",                   "https://www.instagram.com/judydoll_jp",              None,                  None,                                ""),
    (144, "2aN",                    "2aN",                     "スキンケア",           "韓国",       "@2an_official_jp",               "https://www.instagram.com/2an_official_jp",          None,                  None,                                ""),
    (147, "ジョンセンムル",         "Jung Saem Mool",          "メイク",               "韓国",       "@jsmbeauty.jp",                  "https://www.instagram.com/jsmbeauty.jp",             None,                  None,                                ""),
    (148, "Kundal",                 "Kundal",                  "ヘアケア/スキンケア",  "韓国",       "@kundal.japan",                  "https://www.instagram.com/kundal.japan",             None,                  None,                                ""),
    (149, "bring green",            "Bring Green",             "スキンケア",           "韓国",       "@BRINGGREEN_JAPAN",              "https://www.instagram.com/BRINGGREEN_JAPAN",         None,                  None,                                ""),
    (150, "パースピレックス",       "Perspirex",               "デオドラント",         "デンマーク", None,                             None,                                                 None,                  None,                                ""),
    (153, "トゥークールフォースクール", "too cool for school", "メイク",               "韓国",       "@toocoolforschool_official_jp",  "https://www.instagram.com/toocoolforschool_official_jp", None,              None,                                ""),
    (154, "LIALUSTER",              "LIALUSTER",               "スキンケア",           "韓国",       "@lialuster_official",            "https://www.instagram.com/lialuster_official",       None,                  None,                                ""),
    (156, "センテリアン24",         "Centellian24",            "スキンケア",           "韓国",       "@centellian24_japan",            "https://www.instagram.com/centellian24_japan",       None,                  None,                                ""),
    (162, "ドクタージー",           "Dr.G",                    "スキンケア",           "韓国",       "@dr.g_official_jp",              "https://www.instagram.com/dr.g_official_jp",         None,                  None,                                ""),
    (163, "ナンバーズイン",         "Numbuzin",                "スキンケア",           "韓国",       "@numbuzin_official_jp",          "https://www.instagram.com/numbuzin_official_jp",     None,                  None,                                ""),
    (168, "FEG",                    "FEG",                     "まつ毛・まゆ毛",       "韓国",       None,                             None,                                                 None,                  None,                                ""),
    (171, "バイオヒールボ",         "Bioheal BOH",             "スキンケア",           "韓国",       "@bioheal.boh_japan",             "https://www.instagram.com/bioheal.boh_japan",        "@BioHealBohJapan",    "https://x.com/BioHealBohJapan",     ""),
    (172, "refrear",                "refrear",                 "スキンケア",           "韓国",       "@refrear_official",              "https://www.instagram.com/refrear_official",         None,                  None,                                ""),
    (173, "ink.",                   "ink.",                    "メイク",               "韓国",       "@ink.129",                       "https://www.instagram.com/ink.129",                  None,                  None,                                ""),
    (179, "CHPT.⁹",                 "CHPT.9",                  "スキンケア",           "韓国",       None,                             None,                                                 None,                  None,                                ""),
    (182, "Dinto",                  "Dinto",                   "メイク",               "韓国",       "@dinto_cosmetic_jp",             "https://www.instagram.com/dinto_cosmetic_jp",        None,                  None,                                ""),
    (185, "アイムミミ",             "I'm Meme",                "メイク",               "韓国",       "@immeme_japan",                  "https://www.instagram.com/immeme_japan",             None,                  None,                                ""),
    (191, "ザセム",                 "The Saem",                "スキンケア/メイク",    "韓国",       "@thesaem_japan",                 "https://www.instagram.com/thesaem_japan",            None,                  None,                                ""),
    (194, "リトルサイエンティスト", "Little Scientist",        "スキンケア",           "韓国",       "@little_scientist_toitoitoi",    "https://www.instagram.com/little_scientist_toitoitoi", None,                None,                                ""),
    (200, "スキンフード",           "Skinfood",                "スキンケア/メイク",    "韓国",       "@skinfood_japan",                "https://www.instagram.com/skinfood_japan",           None,                  None,                                ""),

    # ── File2-only brands (not in File1, non-lens) ───────────────────────────
    (None, "ティルティル",          "TIRTIR",                  "スキンケア/メイク",    "韓国",       "@tirtir_jp_official",            "https://www.instagram.com/tirtir_jp_official",       "@tirtir_jp",          "https://x.com/tirtir_jp",           ""),
    (None, "バニラコ",              "Banila Co",               "メイク",               "韓国",       "@banilaco_japan",                "https://www.instagram.com/banilaco_japan",           "@Banilaco_Japan",     "https://x.com/Banilaco_Japan",      ""),
    (None, "カラーグラム",          "Colorgram",               "メイク",               "韓国",       "@colorgram_jp",                  "https://www.instagram.com/colorgram_jp",             None,                  None,                                ""),
    (None, "manyo",                 "Manyo Factory",           "スキンケア",           "韓国",       "@manyo.japan",                   "https://www.instagram.com/manyo.japan",              "@manyojapan",         "https://x.com/manyojapan",          ""),
    (None, "FLOWER KNOWS",          "Flower Knows",            "メイク",               "中国",       "@flowerknows_jp",                "https://www.instagram.com/flowerknows_jp",           "@flowerknows_jp",     "https://x.com/flowerknows_jp",      ""),
    (None, "ISOI",                  "ISOI",                    "スキンケア",           "韓国",       "@isoi_japan",                    "https://www.instagram.com/isoi_japan",               "@isoi_jp",            "https://x.com/isoi_jp",             ""),
    (None, "Real Barrier",          "Real Barrier",            "スキンケア",           "韓国",       "@realbarrier_jp_official",       "https://www.instagram.com/realbarrier_jp_official",  None,                  None,                                ""),
    (None, "LUNA",                  "LUNA",                    "メイク",               "韓国",       "@luna_makeup_jp",                "https://www.instagram.com/luna_makeup_jp",           "@luna_makeup_jp",     "https://x.com/luna_makeup_jp",      ""),
    (None, "fwee",                  "fwee",                    "メイク",               "韓国",       None,                             None,                                                 None,                  None,                                ""),
    (None, "isntree",               "isntree",                 "スキンケア",           "韓国",       None,                             None,                                                 None,                  None,                                ""),
    (None, "NESH",                  "NESH",                    "スキンケア",           "韓国",       None,                             None,                                                 None,                  None,                                ""),
    (None, "NDP",                   "NDP",                     "スキンケア",           "韓国",       None,                             None,                                                 None,                  None,                                ""),
    (None, "Barle",                 "Barle",                   "スキンケア",           "韓国",       None,                             None,                                                 None,                  None,                                ""),
    (None, "Brilliet",              "Brilliet",                "スキンケア",           "韓国",       None,                             None,                                                 None,                  None,                                ""),
    (None, "CHASIN' RABBITS",       "Chasin' Rabbits",         "スキンケア",           "韓国",       None,                             None,                                                 None,                  None,                                ""),
    (None, "ENTROPY MAKEUP",        "Entropy Makeup",          "メイク",               "韓国",       None,                             None,                                                 None,                  None,                                ""),
    (None, "FINGER SUIT",           "Finger Suit",             "メイク",               "韓国",       None,                             None,                                                 None,                  None,                                ""),
    (None, "FRANZ",                 "FRANZ",                   "スキンケア",           "韓国",       None,                             None,                                                 None,                  None,                                ""),
    (None, "Furriky",               "Furriky",                 "スキンケア",           "韓国",       None,                             None,                                                 None,                  None,                                ""),
    (None, "GIK",                   "GIK",                     "メイク",               "韓国",       None,                             None,                                                 None,                  None,                                ""),
    (None, "HERRSAINE",             "Herrsaine",               "スキンケア",           "韓国",       None,                             None,                                                 None,                  None,                                ""),
    (None, "Hebestem",              "Hebestem",                "スキンケア",           "韓国",       None,                             None,                                                 None,                  None,                                ""),
    (None, "IZEZE",                 "IZEZE",                   "メイク",               "中国",       None,                             None,                                                 None,                  None,                                ""),
    (None, "It's Skin",             "It's Skin",               "スキンケア",           "韓国",       None,                             None,                                                 None,                  None,                                ""),
    (None, "KISOCARE",              "KISOCARE",                "スキンケア",           "韓国",       None,                             None,                                                 None,                  None,                                ""),
    (None, "Kind Step",             "Kind Step",               "スキンケア",           "韓国",       None,                             None,                                                 None,                  None,                                ""),
    (None, "NIKI PITA",             "NIKI PITA",               "スキンケア",           "韓国",       None,                             None,                                                 None,                  None,                                ""),
    (None, "OIAD",                  "OIAD",                    "スキンケア",           "韓国",       None,                             None,                                                 None,                  None,                                ""),
    (None, "OUKEYA",                "OUKEYA",                  "スキンケア",           "中国",       None,                             None,                                                 None,                  None,                                ""),
    (None, "PHYTOVER",              "PHYTOVER",                "スキンケア",           "韓国",       None,                             None,                                                 None,                  None,                                ""),
    (None, "Slow Humming",          "Slow Humming",            "スキンケア",           "韓国",       None,                             None,                                                 None,                  None,                                ""),
    (None, "TONE fit SUN",          "TONE fit SUN",            "スキンケア",           "韓国",       None,                             None,                                                 None,                  None,                                ""),
    (None, "TONE28",                "TONE28",                  "スキンケア",           "韓国",       None,                             None,                                                 None,                  None,                                ""),
    (None, "VELUS",                 "VELUS",                   "スキンケア",           "韓国",       None,                             None,                                                 None,                  None,                                ""),
    (None, "athe",                  "athe",                    "スキンケア",           "韓国",       None,                             None,                                                 None,                  None,                                ""),
    (None, "efilow",                "efilow",                  "スキンケア",           "韓国",       None,                             None,                                                 None,                  None,                                ""),
    (None, "fremena",               "fremena",                 "スキンケア",           "韓国",       None,                             None,                                                 None,                  None,                                ""),
    (None, "lily eve",              "lily eve",                "メイク",               "韓国",       None,                             None,                                                 None,                  None,                                ""),
    (None, "soaddicted",            "soaddicted",              "メイク",               "韓国",       None,                             None,                                                 None,                  None,                                ""),
    (None, "インセルダーム",        "Inselderm",               "スキンケア",           "韓国",       None,                             None,                                                 None,                  None,                                ""),
    (None, "エリクシール",          "Elixir",                  "スキンケア",           "日本",       None,                             None,                                                 None,                  None,                                "資生堂ブランド"),
    (None, "ヌニ",                  "NUNI",                    "メイク",               "韓国",       None,                             None,                                                 None,                  None,                                ""),
    (None, "マリエラン",            "Mariela'n",               "スキンケア",           "韓国",       None,                             None,                                                 None,                  None,                                ""),
    (None, "ミュード",              "Myude",                   "スキンケア",           "韓国",       None,                             None,                                                 None,                  None,                                ""),
    (None, "リブコイ",              "Livkoi",                  "スキンケア",           "韓国",       None,                             None,                                                 None,                  None,                                ""),
    (None, "リーダース",            "Leaders",                 "スキンケア",           "韓国",       None,                             None,                                                 None,                  None,                                ""),
]

# ─── Build workbook ──────────────────────────────────────────────────────────
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Qoo10 化粧品ブランドSNS"

headers = [
    "Qoo10\n順位", "ブランド名\n（日本語）", "ブランド名\n（英語）",
    "カテゴリ", "原産国",
    "Instagram\nアカウント", "Instagram URL",
    "Twitter/X\nアカウント", "Twitter/X URL",
    "SNS\n状況", "備考"
]

# Styles
border = Border(
    left=Side(style='thin'), right=Side(style='thin'),
    top=Side(style='thin'), bottom=Side(style='thin')
)
header_fill   = PatternFill(start_color="1F3864", end_color="1F3864", fill_type="solid")
green_fill    = PatternFill(start_color="E2EFDA", end_color="E2EFDA", fill_type="solid")
yellow_fill   = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")
red_fill      = PatternFill(start_color="FCE4D6", end_color="FCE4D6", fill_type="solid")

def status_label(ig_url, x_url):
    has_ig = bool(ig_url)
    has_x  = bool(x_url)
    if has_ig and has_x:
        return "両方確認"
    if has_ig:
        return "Instagram\nのみ"
    if has_x:
        return "Twitter/X\nのみ"
    return "未確認"

def row_fill(ig_url, x_url):
    has_ig = bool(ig_url)
    has_x  = bool(x_url)
    if has_ig and has_x:
        return green_fill
    if has_ig or has_x:
        return yellow_fill
    return red_fill

# Header row
for col_idx, header in enumerate(headers, 1):
    cell = ws.cell(row=1, column=col_idx, value=header)
    cell.fill = header_fill
    cell.font = Font(bold=True, color="FFFFFF", size=10)
    cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
    cell.border = border
ws.row_dimensions[1].height = 36

# Data rows
for row_idx, row_data in enumerate(data, 2):
    rank, brand_jp, brand_en, category, country, ig_acc, ig_url, x_acc, x_url, notes = row_data
    fill = row_fill(ig_url, x_url)
    status = status_label(ig_url, x_url)

    values = [
        rank if rank else "－",
        brand_jp, brand_en, category, country,
        ig_acc if ig_acc else "未確認",
        ig_url if ig_url else "未確認",
        x_acc if x_acc else "未確認",
        x_url if x_url else "未確認",
        status,
        notes
    ]
    for col_idx, value in enumerate(values, 1):
        cell = ws.cell(row=row_idx, column=col_idx, value=value)
        cell.fill = fill
        cell.border = border
        cell.alignment = Alignment(vertical='center', wrap_text=True)
        # Hyperlink style for URL columns
        if col_idx in (7, 9) and value not in ("未確認", None):
            cell.font = Font(size=10, color="0563C1", underline="single")
        else:
            cell.font = Font(size=10)
    ws.row_dimensions[row_idx].height = 18

# Column widths
col_widths = [8, 20, 20, 16, 10, 24, 44, 24, 44, 12, 16]
for i, w in enumerate(col_widths, 1):
    ws.column_dimensions[get_column_letter(i)].width = w

# Freeze header + rank/brand columns
ws.freeze_panes = "C2"

# ─── Legend sheet ─────────────────────────────────────────────────────────────
ws2 = wb.create_sheet("凡例")
legend = [
    ("色",        "意味",                              "件数"),
    ("緑",        "Instagram & Twitter/X 両方確認",    str(sum(1 for d in data if d[6] and d[8]))),
    ("黄",        "Instagram または Twitter/X のみ確認", str(sum(1 for d in data if bool(d[6]) != bool(d[8])))),
    ("赤/橙",     "日本公式SNS 未確認",                 str(sum(1 for d in data if not d[6] and not d[8]))),
    ("合計",      "（렌즈ブランド除く）",              str(len(data))),
]
fills_leg = [
    PatternFill(start_color="1F3864", end_color="1F3864", fill_type="solid"),
    green_fill, yellow_fill, red_fill,
    PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid"),
]
fonts_leg = [Font(bold=True, color="FFFFFF", size=11)] + [Font(size=10)] * 4

for r, (col1, col2, col3) in enumerate(legend, 1):
    for c, val in enumerate([col1, col2, col3], 1):
        cell = ws2.cell(row=r, column=c, value=val)
        cell.fill = fills_leg[r - 1]
        cell.font = fonts_leg[r - 1]
        cell.border = border
        cell.alignment = Alignment(horizontal='center', vertical='center')
    ws2.row_dimensions[r].height = 22

for c, w in zip([1, 2, 3], [12, 40, 8]):
    ws2.column_dimensions[get_column_letter(c)].width = w

# ─── Save ─────────────────────────────────────────────────────────────────────
output = "/home/user/mypage/qoo10_beauty_brands_sns_merged.xlsx"
wb.save(output)

total = len(data)
both  = sum(1 for d in data if d[6] and d[8])
one   = sum(1 for d in data if bool(d[6]) != bool(d[8]))
none  = total - both - one
print(f"Saved: {output}")
print(f"Total brands : {total}")
print(f"  両方確認   : {both}")
print(f"  片方のみ   : {one}")
print(f"  未確認     : {none}")
