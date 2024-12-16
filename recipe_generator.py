import os
from openai import OpenAI

# the newest OpenAI model is "gpt-4o" which was released May 13, 2024.
# do not change this unless explicitly requested by the user
MODEL = "gpt-4o"

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def generate_recipe(ingredient1: str, ingredient2: str) -> dict:
    """
    OpenAI APIを使用してレシピを生成する
    
    Args:
        ingredient1: 最初の食材
        ingredient2: 2番目の食材
    
    Returns:
        レシピ情報を含む辞書
    """
    prompt = f"""
    {ingredient1}と{ingredient2}を使用した料理のレシピを考えてください。
    以下のJSON形式で回答してください：
    {{
        "dish_name": "料理名",
        "description": "料理の簡単な説明",
        "ingredients": ["材料リスト"],
        "steps": ["調理手順"],
        "cooking_time": "調理時間（分）",
        "difficulty": "難易度（簡単/普通/難しい）",
        "tips": "調理のコツやポイント"
    }}
    """

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        
        return response.choices[0].message.content
    except Exception as e:
        return {
            "error": f"レシピの生成に失敗しました: {str(e)}",
            "dish_name": "エラー",
            "description": "申し訳ありません。レシピを生成できませんでした。",
            "ingredients": [],
            "steps": [],
            "cooking_time": "N/A",
            "difficulty": "N/A",
            "tips": "N/A"
        }