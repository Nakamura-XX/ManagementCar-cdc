# -------------------------------------------------------------------------------
# Name:        top.py
#
# Purpose:     TOP画面の作成
#
# Author:      Nakamura Akihiro
#
# Created:     2022/10/18
# -------------------------------------------------------------------------------

# ライブラリの宣言
import streamlit as st
import numpy as np
import pandas as pd

# タイトルの記載
st.title("社用車管理アプリ")

# ボタン配置と出力結果(.pyのページ遷移が出来ない為文字で表現)
if st.button("利用状況の確認"):
    st.write("UseSituation.pyに移動")

if st.button("運転日報・実績確認"):
    st.write("DailyReport.pyに移動")

if st.button("予約処理"):
    st.write("準備中です")

if st.button("各種管理"):
    st.write("準備中です")
