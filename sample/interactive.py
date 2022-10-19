import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

# タイトルの表示
st.title("Streamlit 超入門")

# テキストを表示
st.write("Interactive widgets")

# 画像に対するチェックボックス変更
if st.checkbox("Show Image"):
    img = Image.open("./jpg/sample.jpg")
    st.image(img, caption="sample penguin", use_column_width=True)


# セレクトボックスの操作による変更
option = st.selectbox("あなたが好きな数字を教えてください", list(range(1, 11)))
"あなたの好きな数字は", option, "です。"

# テキストボックスに入力した値を表示
text = st.text_input("あなたの趣味を教えてください")
"あなたの趣味は", text, "です"

# スライダー形式で入力した値を表示（引数：msg,min,max,start_value）
condition = st.slider("あなたの今日の調子は？", 0, 100, 50)
"あなたのコンディション", condition
