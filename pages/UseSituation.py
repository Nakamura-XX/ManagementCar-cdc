# -------------------------------------------------------------------------------
# Name:        Usesituation.py
#
# Purpose:     利用状況の確認画面の作成。
#              カレンダー、車両一覧のDB出力、走行情報が必要。
#
# Author:      Nakamura Akihiro
#
# Created:     2022/10/18
# -------------------------------------------------------------------------------

# ライブラリの宣言
import streamlit as st
import numpy as np
import pandas as pd
import datetime
from PIL import Image

# タイトルの記載
st.title("利用状況の確認")

# 各種関数

# 沖縄県の目的地に関する緯度・経度を生成
def purpose():
    # 沖縄県のランダムな経度・緯度を生成する
    data = {
        "lat": np.random.randn(5) / 100 + 26.2125,
        "lon": np.random.randn(5) / 100 + 127.68111,
    }
    map_data = pd.DataFrame(data)
    # 地図に散布図を描く
    st.map(map_data, zoom=13)


# 走行情報の関数
def root():
    image = Image.open("./img/root.png")
    st.image(image, caption="※ドライブレコーダ搭載時の拡張機能になります")


# 違反情報の関数
def violation():
    image = Image.open("./img/violation.png")
    st.image(image, caption="※ドライブレコーダ搭載時の拡張機能になります")


# カレンダー選択の関数。（対象の日付範囲に合わせて出力結果を出す）
def calendar(start_date, end_date):

    # データの読み込み
    df = pd.read_csv("./csv/利用状況.csv", index_col=None, encoding="shift-jis")

    # Datetime型に統一（end_dateは当日も含める為、1日加算）
    df["available_date"] = pd.to_datetime(df["available_date"], format="%Y/%m/%d")
    start_date = pd.to_datetime(start_date, format="%Y/%m/%d")
    end_date = pd.to_datetime(end_date, format="%Y/%m/%d") + datetime.timedelta(days=1)

    # 日付範囲の絞り込み
    df = df[df["available_date"] >= start_date]
    df = df[df["available_date"] <= end_date]
    st.sidebar.dataframe(df, 600, 400)
    del df


# 各種関数処理の出力

# カレンダーの日付選択をサイドバーに表示
col = st.sidebar.columns(2)
start_date = col[0].date_input("検索開始日")
end_date = col[1].date_input("検索終了日")

if start_date or end_date:
    calendar(start_date, end_date)

# ボタン配置（横並び）
col = st.columns(3)

if col[0].button("目的地情報"):
    purpose()

if col[1].button("走行情報"):
    root()

if col[2].button("違反情報"):
    violation()
