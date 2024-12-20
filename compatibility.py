import random
import hashlib

def calculate_compatibility(ingredient1: str, ingredient2: str) -> int:
    combined = f"{ingredient1},{ingredient2}".encode('utf-8')
    hash_value = hashlib.md5(combined).hexdigest()
    number = int(hash_value[:4], 16)
    compatibility = number % 101
    return compatibility

def get_compatibility_comment(score: int) -> str:
    if score >= 90:
        comments = [
            "まさに運命の出会い！この組み合わせは絶品です！",
            "完璧な相性！プロの料理人も驚くような組み合わせです！",
            "これぞ黄金コンビ！素晴らしい相性です！"
        ]
    elif score >= 70:
        comments = [
            "とても相性が良い組み合わせです！",
            "素敵な調和が期待できます！",
            "きっと美味しい料理になるはず！"
        ]
    elif score >= 50:
        comments = [
            "まずまずの相性です！工夫次第で美味しく仕上がります！",
            "基本的な組み合わせですが、安定した味わいが期待できます！",
            "定番の組み合わせ！失敗知らずです！"
        ]
    elif score >= 30:
        comments = [
            "少し意外な組み合わせですが、チャレンジする価値あり！",
            "工夫次第で面白い味わいに！",
            "個性的な組み合わせですが、新しい発見があるかも！"
        ]
    else:
        comments = [
            "珍しい組み合わせ！冒険心のある方におすすめ！",
            "意外性のある組み合わせ！新しいレシピの開拓に！",
            "ユニークな組み合わせ！料理の新境地を開けるかも！"
        ]
    
    return random.choice(comments)
