"""Yahoo!ニュースをスクレイピングするモジュール"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pytz
from typing import Optional, List, Dict


def get_text_safely(element, tag_name: str) -> Optional[str]:
    """要素から安全にテキストを取得"""
    tag = element.find(tag_name)
    return tag.text if tag else None


def scrape_news(url="https://news.yahoo.co.jp/rss/topics/business.xml"):
    """
    Yahoo!ニュースのビジネスニュースRSSフィードを取得

    Args:
        url: スクレイピング対象のRSS URL

    Returns:
        Optional[List[Dict[str, str]]]: ニュース記事のリスト、失敗時はNone
    """
    try:
        response = requests.get(url)
        response.raise_for_status()

        # XMLをパース（lxmlパーサーを使用）
        soup = BeautifulSoup(response.text, "lxml-xml")

        # ニュース記事を取得
        news_list = []
        items = soup.find_all("item")

        # 日本のタイムゾーンを設定
        jst = pytz.timezone("Asia/Tokyo")
        current_time = datetime.now(jst)

        for item in items[:10]:
            title = get_text_safely(item, "title")
            link = get_text_safely(item, "link")
            pub_date = get_text_safely(item, "pubDate")

            if title and link:
                news_list.append(
                    {
                        "title": title,
                        "link": link,
                        "published_at": pub_date,
                        "scraped_at": current_time.strftime("%Y-%m-%d %H:%M:%S JST"),
                    }
                )

        if not news_list:
            print("ニュース記事が見つかりませんでした。")
            return None

        return news_list
    except Exception as e:
        print(f"ニュースの取得中にエラーが発生しました: {e}")
        return None
