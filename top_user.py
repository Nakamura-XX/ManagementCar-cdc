# -------------------------------------------------------------------------------
# Name:        top_user.py
#
# Purpose:     利用者側のTOP画面作成
#
# Author:      Nakamura Akihiro
#
# Created:     2022/10/21
# -------------------------------------------------------------------------------

# ライブラリの宣言
import streamlit as st
import numpy as np
import pandas as pd

# タイトルの記載
st.title("社用車管理アプリ")

# ボタン配置と出力結果(.pyのページ遷移が出来ない為文字で表現)
if st.button("車両予約"):
    st.write("ReservationCar.pyに移動")

if st.button("鍵取り出し"):
    st.write("getAccessKeys.pyに移動")

if st.button("日常点検"):
    st.write("準備中です")

if st.button("各種管理"):
    st.write("準備中です")
