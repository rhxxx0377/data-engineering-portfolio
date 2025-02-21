"""
Financial Modeling Prep APIを使用して株価データを取得するモジュール
"""

import requests
import pandas as pd
from datetime import datetime, timezone, timedelta


def print_debug_info(symbol: str, data: dict, df=None):
    """デバッグ情報を出力

    Args:
        symbol: 企業シンボル
        data: 株価データ
        df: データフレーム
    """
    print(f"\n株価データ for {symbol}:")
    print(data)
    if df is not None:
        print("\n最終的なデータフレーム:")
        print(df[["symbol", "name", "price", "currency", "stockExchange"]])


def fetch_api_data(url: str, params: dict):
    """APIからデータを取得"""
    try:
        print("プロキシ設定を無効化...")
        session = requests.Session()
        session.trust_env = False  # 環境変数のプロキシ設定を無視

        print(f"リクエストURL: {url}")
        print(f"パラメータ: {params}")
        response = session.get(url, params=params, timeout=10)
        print(f"ステータスコード: {response.status_code}")
        return response.json()
    except Exception as e:
        print(f"エラー: {e}")
        return None


def get_stock_price():
    """Appleの株価を取得する基本的な関数"""
    print("株価データの取得を開始...")
    api_key = "hlfUMitfItg2Fb2Yj701XunVr6z5PoWT"
    url = "https://financialmodelingprep.com/api/v3/quote/AAPL"
    params = {"apikey": api_key}

    data = fetch_api_data(url, params)
    if data:
        # 日本時間に変換
        jst = timezone(timedelta(hours=9))
        current_time = datetime.now(jst)

        # データに日本時間のタイムスタンプを追加
        data[0]["timestamp"] = current_time.timestamp()
        return data
    return None


def fetch_companies(query: str, api_key: str) -> list:
    """APIから企業データを取得"""
    base_url = "https://financialmodelingprep.com/api/v3/search"
    params = {
        "query": query,
        "limit": 10,
        "apikey": api_key,
        "exchange": "NYSE,NASDAQ",  # 米国取引所に限定
    }
    response = requests.get(base_url, params=params)
    return response.json()


def search_company(query="AAPL", api_key="YOUR_API_KEY"):
    """企業の株価データを取得"""
    base_url = "https://financialmodelingprep.com/api/v3/search"
    params = {"query": query, "limit": 1, "apikey": api_key}  # シンプルに1社のみ

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        return pd.DataFrame(data)
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return None


def display_company_info(df: pd.DataFrame):
    """企業情報を表示"""
    print("\n企業情報:")
    print(df[["symbol", "name", "currency", "stockExchange"]])


def search_and_display(query: str, api_key: str):
    """企業を検索して結果を表示"""
    df = search_company(query=query, api_key=api_key)
    if df is not None and not df.empty:  # DataFrameの存在とデータの有無を確認
        display_company_info(df)
        return True
    return False


def get_api_key() -> str:
    """APIキーを取得"""
    return "hlfUMitfItg2Fb2Yj701XunVr6z5PoWT"


def display_search_result(query: str, label: str, api_key: str) -> bool:
    """検索結果を表示"""
    print(f"\n{label}:")
    return bool(search_and_display(query, api_key))


def search_by_name_and_code(name: str, code: str, api_key: str):
    """企業を名前と証券コードで検索"""
    if display_search_result(name, f"{name}の検索結果", api_key):
        display_search_result(code, f"証券コード({code})での検索結果", api_key)


def search_toyota_and_code():
    """トヨタの株価を証券コードと社名で検索"""
    search_by_name_and_code("Toyota", "7203", get_api_key())


def test_search():
    """検索機能のテスト実行"""
    search_by_name_and_code("AAPL", "AAPL", get_api_key())


if __name__ == "__main__":
    get_stock_price()
