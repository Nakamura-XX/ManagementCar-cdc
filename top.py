# -------------------------------------------------------------------------------
# Name:        top.py
#
# Purpose:     社用車管理アプリ（管理側）のフロントエンド画面
#
# Author:      Nakamura Akihiro
#
# Created:     2022/11/01
# -------------------------------------------------------------------------------

# ライブラリの宣言
import streamlit as st
import numpy as np
import pandas as pd
import datetime
import math
from PIL import Image

# タイトルの記載
st.title("社用車管理アプリ")

# ボタンのサイズに対するcss設定
button_css = f"""
<style>
  div.stButton > button:first-child  {{
    width: 500px;
    padding: 10px;
    box-sizing: border-box;
    border: 1px solid #68779a;
    background: none;
    cursor: pointer;
  }}
</style>
"""
st.markdown(button_css, unsafe_allow_html=True)

#
# 各種関数
#

# カレンダー選択による範囲の絞り込み関数
def calender_range(df, start_date, end_date):

    # Datetime型に統一（end_dateは当日も含める為、1日加算）
    df["貸渡日時"] = pd.to_datetime(df["貸渡日時"], format="%Y/%m/%d")
    start_date = pd.to_datetime(start_date, format="%Y/%m/%d")
    end_date = pd.to_datetime(end_date, format="%Y/%m/%d") + datetime.timedelta(days=1)

    # 日付範囲の絞り込み
    df = df[df["貸渡日時"] >= start_date]
    df = df[df["貸渡日時"] <= end_date]
    return df


# 稼働率の算出関数
# 必要な機能の要素だけコメントで記載。必要に応じて、関数を分けるなどの変更も実施
def operation(df, start_date, end_date, all_cars):

    # 対象期間の各車両の実働時間(H)を算出

    # 対象期間の各車両の総時間(H)を算出

    # 対象期間の時間(H)による稼働率の計算
    df["稼働率(H)"] = 50

    # 対象期間の各車両の実働時間(日)を算出

    # 対象期間の各車両の総時間(日)を算出

    # 対象期間の時間(日)による稼働率の計算
    df["稼働率(日)"] = 60

    # 対象期間の使用車両台数(台数)を算出
    # （全車両台数は、フロントエンドの入力結果を反映）

    # 対象期間の車両台数による稼働率の計算
    df["稼働率(台数)"] = 70

    return df


# 稼働率の範囲絞り込み関数
def operation_range(df, min_num, max_num):

    # 稼働率範囲の絞り込み(H)
    df = df[df["稼働率(H)"] >= min_num]
    df = df[df["稼働率(H)"] <= max_num]

    # 稼働率範囲の絞り込み(日)
    df = df[df["稼働率(日)"] >= min_num]
    df = df[df["稼働率(日)"] <= max_num]

    # 稼働率範囲の絞り込み(台数)
    df = df[df["稼働率(台数)"] >= min_num]
    df = df[df["稼働率(台数)"] <= max_num]

    return df


#
# 各処理の実行
#

# 対象期間の利用実績出力

# ヘッダーの記載
st.header("利用実績")

# データの読み込み(利用実績)
df = pd.read_csv("./csv/利用実績.csv", index_col=None, encoding="shift-jis")

# カレンダーの日付範囲の選択
col = st.columns(2)
start_date = col[0].date_input("検索開始日")
end_date = col[1].date_input("検索終了日")

# 範囲の絞り込み結果の出力
df = calender_range(df, start_date, end_date)  # 日付範囲の絞り込み
st.dataframe(df, 1200, 400)

# 稼働率の算出

# ヘッダーの記載
st.header("稼働率")

# 稼働率のソート範囲の入力
col = st.columns(2)
min_num = col[0].number_input("稼働率の最小値", min_value=0, max_value=100, value=0, step=5)
max_num = col[1].number_input("稼働率の最大値", min_value=0, max_value=100, value=100, step=5)

# 全保有車両台数の入力
all_cars = st.text_input("現在の保有車両台数")

# 稼働率算出結果の出力
df_operation = operation(df, start_date, end_date, all_cars)
df_operation = operation_range(df, min_num, max_num)
# st.dataframe(df_operation, 1200, 400)  # 稼働率の算出結果の出力
# st.bar_chart(df_operation["稼働率(H)"])  # 算出結果のグラフを出力

# ボタン配置（稼働率種別毎）
button_radio = st.radio("各種稼働率の算出結果", ("稼働率(H)", "稼働率(日)", "稼働率(台数)"))

if button_radio == "稼働率(H)":
    image = Image.open("./img/operation-hours.png")
    st.image(image, caption="対象期間の各車両に対する1時間単位の稼働率")

if button_radio == "稼働率(日)":
    image = Image.open("./img/operation-days.png")
    st.image(image, caption="対象期間の各車両に対する1日単位の稼働率")

if button_radio == "稼働率(台数)":
    image = Image.open("./img/operation-cars.png")
    st.image(image, caption="対象日時の全車両の中から実車を行った台数の稼働率")
