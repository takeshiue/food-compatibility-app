import pandas as pd

INGREDIENTS = {
    "野菜": [
        "トマト", "きゅうり", "なす", "かぼちゃ", "じゃがいも",
        "たまねぎ", "にんじん", "ピーマン", "ブロッコリー", "ほうれん草"
    ],
    "肉・魚": [
        "鶏肉", "豚肉", "牛肉", "サーモン", "まぐろ",
        "えび", "あさり", "いか", "たこ", "さば"
    ],
    "調味料": [
        "醤油", "味噌", "塩", "砂糖", "酢",
        "みりん", "料理酒", "オリーブオイル", "ごま油", "わさび"
    ],
    "その他": [
        "豆腐", "卵", "チーズ", "米", "パスタ",
        "のり", "わかめ", "きのこ", "こんにゃく", "納豆"
    ]
}

def get_all_ingredients():
    all_ingredients = []
    for category in INGREDIENTS.values():
        all_ingredients.extend(category)
    return sorted(all_ingredients)

def get_ingredients_by_category():
    return INGREDIENTS
