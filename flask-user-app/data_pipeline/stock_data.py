"""株価データを取得するモジュール"""

import yfinance as yf
from datetime import datetime


def get_stock_price(symbol="AAPL", period="1d", interval="1m"):
    """
    指定された銘柄の株価データを取得

    Args:
        symbol (str): 銘柄コード（デフォルト: AAPL）
        period (str): 取得期間（デフォルト: 1d）
        interval (str): 時間間隔（デフォルト: 1m）

    Returns:
        list: 株価データのリスト
    """
    try:
        # Yahoo Financeから株価データを取得
        stock = yf.Ticker(symbol)
        hist = stock.history(period=period, interval=interval)

        if hist.empty:
            return None

        # 最新のデータを取得
        latest = hist.iloc[-1]

        return [
            {
                "symbol": symbol,
                "price": round(float(latest["Close"]), 2),
                "timestamp": int(datetime.now().timestamp()),
            }
        ]
    except Exception as e:
        print(f"株価データの取得中にエラーが発生しました: {e}")
        return None
