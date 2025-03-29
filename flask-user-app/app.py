"""Flaskによるユーザー管理とデータ表示アプリケーション"""

from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    send_from_directory,
    jsonify,
)
from models import db, User
from forms import UserForm
from data_pipeline.stock_data import get_stock_price
from web_scraping.scrape_yahoo_news import scrape_news
from data_pipeline.visualize import create_graph
import os
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
from flask_compress import Compress
from datetime import datetime

# データベースファイルのパスを設定
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(BASE_DIR, "database.db")

app = Flask(
    __name__,
    static_folder=os.path.join(os.path.dirname(__file__), "static"),
    static_url_path="/static",
)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# 環境変数から SECRET_KEY を取得
load_dotenv()
SECRET_KEY = os.environ.get("SECRET_KEY") or os.urandom(24)
app.config["SECRET_KEY"] = SECRET_KEY

app.config["DEBUG"] = True

db.init_app(app)

csrf = CSRFProtect()
csrf.init_app(app)

# GETリクエストはCSRF保護から除外
app.config["WTF_CSRF_CHECK_DEFAULT"] = False
app.config["WTF_CSRF_METHODS"] = ["POST", "PUT", "PATCH", "DELETE"]

compress = Compress()
compress.init_app(app)


# キャッシュ用の変数
stock_cache = None
news_cache = None
cache_timeout = 300  # 5分


def get_cached_stock_data():
    """株価データをキャッシュから取得"""
    global stock_cache
    if stock_cache is None:
        stock_cache = get_stock_price()
    return stock_cache


def get_cached_news():
    """ニュースをキャッシュから取得"""
    global news_cache
    if news_cache is None:
        news_cache = scrape_news()
    return news_cache


# メインページ（ユーザー登録フォーム）
@app.route("/", methods=["GET", "POST"])
def home():
    form = UserForm()
    if form.validate_on_submit():
        try:
            new_user = User(name=form.name.data, email=form.email.data)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("users"))
        except Exception as e:
            print(f"ユーザー登録エラー: {e}")
            db.session.rollback()
    return render_template("index.html", form=form)


# ユーザー一覧ページ
@app.route("/users")
def users():
    try:
        all_users = User.query.all()
        return render_template("users.html", users=all_users)
    except Exception as e:
        print(f"ユーザー一覧取得エラー: {e}")
        return "データベースエラーが発生しました", 500


# ニュースページ
@app.route("/news")
@csrf.exempt
def news():
    """ニュース一覧"""
    try:
        news_data = get_cached_news()
        return render_template("news.html", news=news_data)
    except Exception as e:
        print(f"ニュース表示エラー: {e}")
        return "ニュースの取得中にエラーが発生しました", 500


# ダッシュボードページ
@app.route("/dashboard", methods=["GET"])
@csrf.exempt
def dashboard():
    """ダッシュボード: 株価とニュースを表示"""
    try:
        # 株価データを取得して保存
        stock_data = get_cached_stock_data()
        if stock_data and stock_data[0]:
            # UNIXタイムスタンプを日時に変換
            timestamp = datetime.fromtimestamp(stock_data[0]["timestamp"])
            # 日本時間で表示
            time_format = "%Y-%m-%d %H:%M:%S JST"
            stock_data[0]["formatted_time"] = timestamp.strftime(time_format)

        if stock_data:
            # グラフを生成
            create_graph()

        # ニュースを取得
        news_data = get_cached_news()

        # テンプレートにデータを渡して表示
        stock = stock_data[0] if stock_data else None
        return render_template("dashboard.html", stock=stock, news=news_data)
    except Exception as e:
        print(f"ダッシュボード表示エラー: {e}")
        return "データの取得中にエラーが発生しました", 500


# stock_dashboardのエイリアス
@app.route("/stock_dashboard", methods=["GET"])
@csrf.exempt
def stock_dashboard():
    """株価データダッシュボードのエイリアス"""
    return dashboard()


# ユーザー削除機能
@app.route("/delete_user/<int:user_id>", methods=["POST"])
def delete_user(user_id):
    try:
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for("users"))
    except Exception as e:
        print(f"ユーザー削除エラー: {e}")
        db.session.rollback()
        return "削除中にエラーが発生しました", 500


# 静的ファイルへのルート
@app.route("/static/<path:filename>")
@csrf.exempt
def serve_static(filename):
    if app.static_folder is None:
        return "静的フォルダが設定されていません", 500
    static_path = os.path.join(app.static_folder, filename)
    if not os.path.exists(static_path):
        print(f"ファイルが見つかりません: {static_path}")
        return "ファイルが見つかりません", 404
    return send_from_directory(app.static_folder, filename)


# 403エラーハンドラー
@app.errorhandler(403)
def forbidden_error(error):
    return (
        jsonify(
            {
                "error": "アクセスが拒否されました",
                "message": "アプリケーションが正常に起動していないか、セッションが期限切れの可能性があります。",
                "status": 403,
            }
        ),
        403,
    )


# ヘルスチェックエンドポイント
@app.route("/health")
def health_check():
    timestamp = datetime.now().isoformat()
    return jsonify({"status": "healthy", "timestamp": timestamp})


# データベースの初期化
def init_db():
    with app.app_context():
        try:
            db.create_all()
            print("データベースを初期化しました")
        except Exception as e:
            print(f"データベース初期化エラー: {e}")


# アプリケーション起動時にDBを初期化
if __name__ == "__main__":
    with app.app_context():
        try:
            db.create_all()
            print("データベースを初期化しました")
        except Exception as e:
            print(f"データベース初期化エラー: {e}")

    # デバッグモードを有効にし、ホストを指定
    app.run(debug=True, host="127.0.0.1", port=5000)
