import random
import hashlib

def calculate_compatibility(ingredient1: str, ingredient2: str) -> int:
    """
    2つの食材の相性を計算する
    
    Args:
        ingredient1: 最初の食材
        ingredient2: 2番目の食材
    
    Returns:
        0-100の相性度
    """
    # 食材の組み合わせから一意のハッシュを生成
    combined = f"{ingredient1},{ingredient2}".encode('utf-8')
    hash_value = hashlib.md5(combined).hexdigest()
    
    # ハッシュの最初の4文字を16進数から10進数に変換
    number = int(hash_value[:4], 16)
    
    # 0-100の範囲に変換
    compatibility = number % 101
    
    return compatibility

def get_compatibility_comment(score: int) -> str:
    """
    相性度に基づいてコメントを生成する
    
    Args:
        score: 相性度（0-100）
    
    Returns:
        相性に関するコメント
    """
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
