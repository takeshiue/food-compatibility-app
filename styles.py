import streamlit as st

def apply_custom_styles():
    """カスタムCSSスタイルを適用する"""
    st.markdown("""
        <style>
        .stApp {
            max-width: 1200px;
            margin: 0 auto;
        }
        
        .ingredient-selector {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        
        .compatibility-result {
            text-align: center;
            padding: 20px;
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin: 20px 0;
        }
        
        .recipe-card {
            background-color: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin: 20px 0;
        }
        
        .header-text {
            color: #FF4B4B;
            font-size: 2.5rem;
            font-weight: bold;
            text-align: center;
            margin-bottom: 30px;
        }
        
        .subheader-text {
            color: #262730;
            font-size: 1.5rem;
            font-weight: bold;
            margin: 20px 0;
        }
        
        .percentage-display {
            font-size: 3rem;
            font-weight: bold;
            color: #FF4B4B;
        }
        </style>
    """, unsafe_allow_html=True)
