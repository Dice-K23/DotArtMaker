# Python版 ドット絵メーカー（illustrationDot_py）

## 概要
Webブラウザ上でExcel風のドット絵を描けるアプリです。
- 26x30マスのキャンバス
- 色選択・消しゴム・クリア機能
- Flask + HTML/JSで実装

## セットアップ
1. 必要なパッケージをインストール
   ```bash
   pip install flask
   ```
2. サーバー起動
   ```bash
   python app.py
   ```
3. ブラウザで http://localhost:5000 を開く

## ファイル構成
- app.py : Flaskサーバー本体
- templates/index.html : Web UI

## 使い方
- 色ボタンで色を選択
- セルをクリックして塗りつぶし
- 消しゴムボタンで白色に
- クリアボタンで全消去

---
保存・読込などの拡張も可能です。ご相談ください。 