# ベースイメージを指定
FROM tiangolo/uwsgi-nginx-flask:python3.8

# 作業ディレクトリを設定
WORKDIR /app

# ホストのrequirements.txtをコンテナ内にコピー
COPY requirements.txt .

# パッケージをインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのファイルをコンテナ内にコピー
COPY . .

# uWSGIサーバの設定
ENV UWSGI_INI /app/uwsgi.ini

# ポートを公開
EXPOSE 80
EXPOSE 8000