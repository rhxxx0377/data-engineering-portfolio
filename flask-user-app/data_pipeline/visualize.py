"""株価データのグラフを生成するモジュール"""

import os
import matplotlib
import matplotlib.pyplot as plt
import yfinance as yf

matplotlib.use("Agg")  # GUIを使用しないバックエンドを設定


def create_graph(symbol="AAPL", period="1d", interval="1m"):
    """
    株価データのグラフを生成して保存

    Args:
        symbol (str): 銘柄コード（デフォルト: AAPL）
        period (str): 取得期間（デフォルト: 1d）
        interval (str): 時間間隔（デフォルト: 1m）
    """
    try:
        # Yahoo Financeから株価データを取得
        stock = yf.Ticker(symbol)
        hist = stock.history(period=period, interval=interval)

        if hist.empty:
            return

        # グラフを生成
        plt.figure(figsize=(10, 6))
        plt.plot(hist.index, hist["Close"])
        plt.title(f"{symbol} Stock Price")
        plt.xlabel("Time")
        plt.ylabel("Price (USD)")
        plt.grid(True)

        # 現在のファイルのディレクトリを取得
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # staticディレクトリのパスを生成
        base_dir = os.path.dirname(os.path.dirname(current_dir))
        static_dir = os.path.join(base_dir, "flask-user-app/static")

        # staticディレクトリが存在しない場合は作成
        os.makedirs(static_dir, exist_ok=True)

        # グラフを保存
        plt.savefig(os.path.join(static_dir, "stock_price.png"))
        plt.close()
    except Exception as e:
        print(f"グラフの生成中にエラーが発生しました: {e}")
        return None
