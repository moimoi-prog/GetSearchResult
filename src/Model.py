import configparser as c
import tkinter as tk
import os
import pathlib

# ---------------------------------
# スクレイピング用のモジュールをインポート
# ---------------------------------
# ブラウザ表示用
import urllib
import webbrowser
# HTMLダウンロード用
import requests
# HTML解析用
import bs4

# ---------------------------------
# csv操作用のモジュールをインポート
# ---------------------------------
import csv


class Model(object):
    def __init__(self, root):
        # ---------------------------------
        # 初期設定
        # ---------------------------------
        # configファイルを読み込み
        self.config = c.ConfigParser()
        self.config.read("config.ini")

        # 画面タイトルを取得
        self.title = self.config["DISPLAY_INFO"]["title"]

        # 画面サイズを取得
        self.width = self.config["DISPLAY_INFO"]["width"]
        self.height = self.config["DISPLAY_INFO"]["height"]

        # 表示ページ数を取得
        self.pages = self.config["SETTING"]["pages"]

        # csvファイルのパスを取得する。
        self.output_path = self.config["PATH"]["output_path"]

        # 画面パーツに入力した値を格納する変数を宣言
        self.ent_search_text = tk.StringVar()

    # ボタンクリック時起動メソッド
    def btn_clicked(self):
        # 検索結果のタイトルとURLを格納するリストを生成する
        list_title = []
        list_url = []

        # 検索結果一覧のwebページのHTMLを取得する
        search_result = requests.get("https://www.google.com/search?q={}".format((self.ent_search_text.get()))).content

        # 取得したHTMLを使用してBeautifulSoupオブジェクトを生成する
        result_soup = bs4.BeautifulSoup(search_result, "html.parser")

        print(result_soup.prettify())

        # 検索結果のtitleを含むdivタグのリストを取得
        title_elems = result_soup.select('div[class="kCrYT"] > a > .BNeawe.vvjwJb.AP7Wnd')

        # 検索結果のurlを含むaタグのリストを取得
        url_elems = result_soup.select('div[class="kCrYT"] > a')

        # 指定された件数分検索結果をリストに格納する
        for idx in range(0, min(int(self.pages), len(url_elems))):
            # divタグからタイトルを取得
            title = title_elems[idx].text

            # aタグからurlを取得
            url = urllib.parse.unquote(url_elems[idx].get('href').split('&sa=U&')[0].replace('/url?q=', ''))

            # リストに要素を追加
            list_title.append(title)
            list_url.append(url)

            # ブラウザをインスタンス化
            browser = webbrowser.get()

            # urlを指定してwebページを表示
            browser.open(url)

        result_path = "search_result.csv"
        column_names = ["title", "url"]

        # 検索結果ファイルが存在しない場合、作成する
        if not os.path.exists(result_path):
            with open(result_path, "w") as f:
                # CSVファイルを生成
                writer = csv.DictWriter(f, column_names)

                # ヘッダーを書き込み
                writer.writeheader()

        # csvファイルにデータを書き込む
        with open(result_path, "a") as f:
            # CSVファイルを生成
            writer = csv.DictWriter(f, column_names)

            # 要素を書き込み
            for i in range(0, len(list_title)):
                writer.writerow({"title": list_title[i], "url": list_url[i]})
