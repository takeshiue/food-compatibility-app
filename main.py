import streamlit as st
import json
from ingredients_db import get_all_ingredients, get_ingredients_by_category
from compatibility import calculate_compatibility, get_compatibility_comment
from recipe_generator import generate_recipe
from styles import apply_custom_styles

def main():
    # スタイルの適用
    apply_custom_styles()
    
    # アプリケーションのヘッダー
    st.markdown('<h1 class="header-text">🍳 食材相性診断＆レシピ提案</h1>', unsafe_allow_html=True)
    st.markdown("2つの食材を選んで、その相性とレシピの提案を受けてみましょう！")
    
    # サイドバーに説明を追加
    with st.sidebar:
        st.markdown("### 💡 使い方")
        st.markdown("""
        1. 2つの食材を選択
        2. 相性度を確認
        3. AIによるレシピ提案を確認
        """)
        st.markdown("### 🎯 特徴")
        st.markdown("""
        - 食材の相性を％で表示
        - ユニークなコメント付き
        - AIによるオリジナルレシピ提案
        """)
    
    # 食材選択エリア
    st.markdown('<div class="ingredient-selector">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    ingredients_by_category = get_ingredients_by_category()
    
    with col1:
        st.markdown("### 1つ目の食材")
        category1 = st.selectbox(
            "カテゴリー選択 (1)",
            options=list(ingredients_by_category.keys()),
            key="category1"
        )
        ingredient1 = st.selectbox(
            "食材選択 (1)",
            options=ingredients_by_category[category1],
            key="ingredient1"
        )
    
    with col2:
        st.markdown("### 2つ目の食材")
        category2 = st.selectbox(
            "カテゴリー選択 (2)",
            options=list(ingredients_by_category.keys()),
            key="category2"
        )
        ingredient2 = st.selectbox(
            "食材選択 (2)",
            options=ingredients_by_category[category2],
            key="ingredient2"
        )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 診断ボタン
    if st.button("相性を診断する！", type="primary"):
        # 相性度の計算
        compatibility_score = calculate_compatibility(ingredient1, ingredient2)
        comment = get_compatibility_comment(compatibility_score)
        
        # 結果の表示
        st.markdown('<div class="compatibility-result">', unsafe_allow_html=True)
        st.markdown(f'<p class="percentage-display">{compatibility_score}%</p>', unsafe_allow_html=True)
        st.markdown(f"### {comment}")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # レシピの生成と表示
        with st.spinner("AIがレシピを考え中..."):
            recipe_json = generate_recipe(ingredient1, ingredient2)
            recipe = json.loads(recipe_json)
            
            st.markdown('<div class="recipe-card">', unsafe_allow_html=True)
            st.markdown(f"## 🍽️ {recipe['dish_name']}")
            st.markdown(f"### 📝 料理の説明")
            st.write(recipe['description'])
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("### 🕒 調理時間")
                st.write(f"{recipe['cooking_time']}分")
            with col2:
                st.markdown("### 📊 難易度")
                st.write(recipe['difficulty'])
            
            st.markdown("### 🥗 材料")
            for ingredient in recipe['ingredients']:
                st.markdown(f"- {ingredient}")
            
            st.markdown("### 👩‍🍳 調理手順")
            for i, step in enumerate(recipe['steps'], 1):
                st.markdown(f"{i}. {step}")
            
            st.markdown("### 💡 調理のコツ")
            st.write(recipe['tips'])
            st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
