"""
株価データを可視化するモジュール
"""

# 1. 標準ライブラリ
import os
import sqlite3

# 2. サードパーティライブラリ
import matplotlib
import matplotlib.pyplot as plt  # matplotlibの設定前にインポート
import pandas as pd

# matplotlibのバックエンド設定
matplotlib.use("Agg")  # GUIバックエンドを使用しない設定


def create_graph():
    """基本的な棒グラフを作成"""
    # データベースからデータを読み込み
    conn = sqlite3.connect("data_pipeline/stock_data.db")
    df = pd.read_sql("SELECT * FROM stock_prices", conn)
    conn.close()

    # グラフをクリア
    plt.clf()

    # グラフのスタイル設定
    plt.style.use("default")  # seabornの代わりにデフォルトスタイルを使用
    plt.figure(figsize=(8, 4), dpi=100)

    # 棒グラフの作成
    x_pos = 0
    plt.bar(x_pos, df["price"][0], color="skyblue", width=0.4)

    # グラフの装飾
    plt.title("Apple Inc. 株価", fontsize=12, pad=15)
    plt.ylabel("価格 ($)", fontsize=10)
    plt.xticks([x_pos], ["AAPL"], fontsize=10)
    plt.grid(True, alpha=0.3)

    # 価格ラベルの表示
    plt.text(
        x_pos,
        df["price"][0],
        f'${df["price"][0]:.2f}',
        ha="center",
        va="bottom",
        fontsize=10,
    )

    # グラフの保存
    save_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "flask-user-app",
        "static",
        "stock_price.png",
    )
    plt.savefig(save_path, bbox_inches="tight", dpi=100)
    plt.close()  # メモリリーク防止


if __name__ == "__main__":
    create_graph()
