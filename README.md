# データエンジニアリングポートフォリオ

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-3.1.0-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

[スクリーンショットやデモ画像をここに配置]

Python × データパイプライン × 可視化を組み合わせた、データエンジニアリングのポートフォリオプロジェクトです。

## 機能概要

### 1. データパイプライン
- Financial Modeling Prep APIを使用した株価データの取得
- SQLiteデータベースへのデータ保存
- Matplotlibによるデータの可視化

### 2. Webスクレイピング
- Yahoo!ニュースRSSフィードからの最新ニュース取得
- BeautifulSoupを使用したHTMLパース
- CSVファイルへのデータ保存

### 3. ユーザー管理機能
- Flask × SQLAlchemyによるCRUD操作
- WTFormsを使用したフォームバリデーション
- ユーザー情報のデータベース管理

## 技術スタック

### バックエンド
- Python 3.11.11
- Flask 3.1.0
- SQLAlchemy 3.1.1
- WTForms 1.2.2

### データ処理
- Pandas 2.2.1
- Matplotlib 3.8.3
- BeautifulSoup4
- Requests

### データベース
- SQLite3

## セットアップ手順

1. **環境構築**
```bash
# Pythonバージョンの設定
pyenv local 3.11.11

# 仮想環境の作成と有効化
python -m venv venv
source venv/bin/activate  # Windowsの場合: venv\Scripts\activate

# 依存パッケージのインストール
pip install -r requirements.txt
```

2. **環境変数の設定**
```bash
# .envファイルを作成
cp .env.example .env
# SECRET_KEYを設定
```

3. **アプリケーションの起動**
```bash
python -m flask --app flask-user-app/app.py run
```

## アクセス方法
- メインページ: http://localhost:5000/
- 株価データ: http://localhost:5000/stock-dashboard
- ニュース一覧: http://localhost:5000/news
- ユーザー一覧: http://localhost:5000/users

## プロジェクト構造
```
portfolio-projects/
├── __init__.py         # Pythonパッケージ設定
├── .env.example        # 環境変数の例
├── .gitignore         # Git除外設定
├── .python-version    # pyenvのPythonバージョン設定
├── .zshrc             # Zshシェル設定
├── LICENSE            # MITライセンス
├── README.md          # プロジェクト説明
├── requirements.txt   # 依存パッケージ一覧
├── data_pipeline/     # データ取得・処理関連
│   ├── __init__.py
│   ├── stock_data.py  # 株価データ取得
│   ├── visualize.py   # データ可視化
│   ├── save_to_sql.py # DB保存
│   └── stock_data.db  # SQLiteデータベース
├── web_scraping/      # Webスクレイピング関連
│   ├── __init__.py
│   ├── scrape_yahoo_news.py
│   └── scraped_data.csv
└── flask-user-app/    # Webアプリケーション
    ├── __init__.py
    ├── app.py         # メインアプリケーション
    ├── models.py      # データモデル
    ├── forms.py       # フォーム定義
    ├── database.db    # SQLiteデータベース
    ├── static/        # 静的ファイル
    │   └── stock_price.png
    └── templates/     # HTMLテンプレート
        ├── index.html
        ├── dashboard.html
        ├── news.html
        ├── stock_dashboard.html
        └── users.html

注: venv/ ディレクトリは.gitignoreに含まれており、リポジトリには含まれません

```

## 開発者向け情報
- PEP 8スタイルガイドに準拠
- エラーハンドリングの実装
- CSRFトークンによるセキュリティ対策
- 環境変数による設定管理

## ライセンス
MIT License
