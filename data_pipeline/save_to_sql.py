"""データをSQLiteに保存する基本的なスクリプト"""

import sqlite3
import pandas as pd
from stock_data import get_stock_price


def save_to_db():
    """株価データをデータベースに保存"""
    # データを取得
    data = get_stock_price()
    if data is None:
        return

    # リストからDataFrameに変換
    df = pd.DataFrame(data)

    # 必要なカラムのみを選択
    df = df[["symbol", "name", "price", "exchange"]]

    # データベースに接続して保存
    conn = sqlite3.connect("data_pipeline/stock_data.db")
    df.to_sql("stock_prices", conn, if_exists="replace", index=False)
    print("データを保存しました")
    conn.close()


if __name__ == "__main__":
    save_to_db()
