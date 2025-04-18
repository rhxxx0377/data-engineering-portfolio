# 📊 データエンジニア向けポートフォリオ

🚀 **プロジェクト概要**  
このプロジェクトは、データエンジニアとしてのスキルを証明するためのポートフォリオです。  
APIデータ取得、Webスクレイピング、データ保存、可視化、Webアプリケーションを組み合わせ、データパイプラインの基礎を構築しています。

📌 **主な機能**
- **APIデータ取得**（Financial Modeling Prep APIを使用した株価データ取得）
- **Webスクレイピング**（YahooニュースRSSフィードからのデータ取得）
- **データの保存**（SQLiteを使用したデータ管理）
- **データの可視化**（Matplotlib, Pandasを使用）
- **ユーザー管理機能**（Flask × SQLAlchemy × WTForms）

🆕 **最新の改善点**
- **スクレイピング機能の強化**（XMLパーサーの最適化、エラーハンドリングの改善）
- **型安全性の向上**（型ヒントの導入によるコード品質の改善）
- **パフォーマンスの最適化**（データキャッシング、非同期処理の導入）
- **コードの可読性向上**（PEP 8準拠、関数の分割と最適化）
- **UIの改善**（ダッシュボードとニュース一覧の分離、ナビゲーションの最適化）

---

## 🔧 セットアップ方法
このプロジェクトをローカル環境で動作させるための手順です。

### 1️⃣ 必要なライブラリのインストール
```bash
git clone https://github.com/your-username/data-engineering-portfolio.git
cd data-engineering-portfolio
pyenv local 3.11.11  # Pythonバージョンの設定
python -m venv venv  # 仮想環境の作成
source venv/bin/activate  # Windowsの場合: venv\Scripts\activate
pip install -r requirements.txt  # 必要ライブラリのインストール
```

### 2️⃣ 環境変数の設定
```bash
cp .env.example .env  # .envファイルを作成
# SECRET_KEYなどを適切に設定
```

### 3️⃣ アプリケーションの起動
```bash
python -m flask --app flask-user-app/app.py run --port 8080
# または
cd flask-user-app && python app.py
```

⚠️ **注意**: 
- デフォルトでポート8080を使用します
- ポートが使用中の場合は、`app.py`の`port`パラメータを変更してください
- macOSでポート5000を使用する場合は、システム設定 → 一般 → AirDropとハンドオフから「AirPlay Receiver」をオフにする必要があります

### 4️⃣ アクセス方法
- メインページ: `http://127.0.0.1:8080`
- データダッシュボード: `http://127.0.0.1:8080/stock_dashboard`
- ニュース一覧: `http://127.0.0.1:8080/news`
- ユーザー管理: `http://127.0.0.1:8080/users`

---

## 📂 プロジェクト構造
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
│   ├── scrape_yahoo_news.py  # 最適化済みスクレイピング
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
```

---

## 📌 使用技術
- **Python 3.11.11**
- **Flask 3.1.0**（Webアプリケーション）
- **SQLAlchemy 3.1.1**（ORM）
- **WTForms 1.2.2**（フォームバリデーション）
- **Pandas 2.2.1, Matplotlib 3.8.3**（データ処理・可視化）
- **BeautifulSoup4, lxml**（スクレイピング、XMLパース）
- **SQLite3**（データベース）
- **typing**（型ヒント）

---

## 💡 想定ユースケース
- **データエンジニアの基礎スキル証明**（APIデータ取得・スクレイピング・データ保存・可視化）
- **業務のデータ収集と自動化**（例えば、Yahoo RSSフィードを用いたニュース解析）
- **クラウド対応（今後の拡張）**（AWS S3やGCP BigQueryとの連携も検討可能）

---

## 🏆 今後の拡張（ToDo）
✅ AWS S3やGCP BigQueryへのデータアップロード機能  
✅ データ分析機能の強化（時系列予測、機械学習モデルとの統合）  
✅ FastAPIを導入し、データ取得・可視化APIを提供  
✅ 非同期処理の導入によるパフォーマンス最適化
✅ テスト自動化とCI/CDパイプラインの構築

---

## 📬 お問い合わせ
質問やフィードバックがありましたら、[GitHub Issues](https://github.com/your-username/data-engineering-portfolio/issues) に投稿してください。

---

## �� ライセンス
MIT License
