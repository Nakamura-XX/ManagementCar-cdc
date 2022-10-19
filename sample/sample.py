import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

# タイトルの表示
st.title("Streamlit 超入門")

# テキストを表示
st.write("サンプル機能")

# サイドバー側に表示
text = st.sidebar.text_input("あなたの趣味を教えてください")
condition = st.sidebar.slider("あなたの今日の調子は？", 0, 100, 50)

"あなたの趣味は", text, "です"
"あなたのコンディション", condition

# 2カラムレイアウトを表示
left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラム")

# 拡張表示機能（expander）の追加
expander = st.expander("お問い合わせ")

# お問い合わせ内容の詳細
text_ex = expander.text_input("お問い合わせ内容")
text_ex