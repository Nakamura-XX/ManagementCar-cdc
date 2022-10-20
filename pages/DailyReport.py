# -------------------------------------------------------------------------------
# Name:        DailyReport.py
#
# Purpose:     運転日報・実績確認画面の作成。
#
# Author:      Nakamura Akihiro
#
# Created:     2022/10/20
# -------------------------------------------------------------------------------

# ライブラリの宣言
import streamlit as st
import numpy as np
import pandas as pd
import datetime
import math
from PIL import Image

# タイトルの記載
st.title("運転日報の確認")

# 各種関数

# 利用実績の関数（対象範囲の日付の利用実績を表示）
def achievement(start_date, end_date):

    # データの読み込み
    df = pd.read_csv("./csv/利用実績.csv", index_col=None, encoding="shift-jis")

    # Datetime型に統一（end_dateは当日も含める為、1日加算）
    df["available_date"] = pd.to_datetime(df["available_date"], format="%Y/%m/%d")
    start_date = pd.to_datetime(start_date, format="%Y/%m/%d")
    end_date = pd.to_datetime(end_date, format="%Y/%m/%d") + datetime.timedelta(days=1)

    # 日付範囲の絞り込み
    df = df[df["available_date"] >= start_date]
    df = df[df["available_date"] <= end_date]
    st.dataframe(df, 1200, 400)
    del df


# 稼働率の算出関数
def operation(min_num, max_num):

    # データの読み込み
    df = pd.read_csv("./csv/稼働率.csv", index_col=None, encoding="shift-jis")

    # 車両番号と時間から1日の稼働率を算出
    df["operating_rate"] = df["operating_time_minutes"] / 1440 * 100

    # 稼働率範囲の絞り込み
    df = df[df["operating_rate"] >= min_num]
    df = df[df["operating_rate"] <= max_num]

    # 稼働率のカラムを追加した結果を出力
    st.dataframe(df, 1200, 400)
    del df


# 各種関数処理の出力

# カレンダーの日付選択を表示
col = st.sidebar.columns(2)
start_date = col[0].date_input("検索開始日")
end_date = col[1].date_input("検索終了日")

# 稼働率のソート機能ボタンを追加
col = st.sidebar.columns(2)
min_num = col[0].number_input("稼働率の最小値", min_value=0, max_value=100, value=0, step=5)
max_num = col[1].number_input("稼働率の最大値", min_value=0, max_value=100, value=100, step=5)

# ボタン配置（横並び）
col = st.columns(2)

if col[0].button("利用実績の確認"):
    achievement(start_date, end_date)

if col[1].button("稼働率の算出"):
    operation(min_num, max_num)
