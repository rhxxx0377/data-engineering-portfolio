"""Yahoo!ニュースの基本的なスクレイピング"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime


def scrape_news():
    """Yahoo!ニュースのRSSフィードから記事を取得"""
    url = "https://news.yahoo.co.jp/rss/topics/top-picks.xml"

    try:
        response = requests.get(url)
        # lxmlパーサーを明示的に指定
        soup = BeautifulSoup(response.text, "lxml-xml")

        articles = []
        # itemタグを探して処理
        for item in soup.select("item"):
            # findではなくselectを使用
            title = item.select_one("title")
            link = item.select_one("link")

            if title and link:
                # 長い行を複数行に分割
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                articles.append(
                    {
                        "title": title.get_text(strip=True),
                        "link": link.get_text(strip=True),
                        "scraped_at": timestamp,
                    }
                )

        if not articles:
            print("ニュース記事が見つかりませんでした")
            return []

        df = pd.DataFrame(articles)
        print("\n取得したニュース:")
        print(df)

        output_path = "web_scraping/scraped_data.csv"
        df.to_csv(output_path, index=False, encoding="utf-8")
        print("\nニュースを保存しました")

        return articles

    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return []


if __name__ == "__main__":
    scrape_news()
