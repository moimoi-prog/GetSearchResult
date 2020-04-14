import tkinter as tk


class View(object):
    def __init__(self, root, model):
        self.root = root
        self.model = model

        # ---------------------------------
        # 画面の部品を生成
        # ---------------------------------
        # 検索欄ラベル
        self.lbl_search = tk.Label(
            root,
            text="word"
        )

        # 検索欄
        self.ent_search = tk.Entry(
            root,
            textvariable=model.ent_search_text,
            width=30
        )

        # 検索ボタン
        self.btn_search = tk.Button(
            root,
            text="search",
            command=lambda: model.btn_clicked()
        )

        # ---------------------------------
        # 画面の部品を配置
        # ---------------------------------
        self.lbl_search.grid(row=0, column=0)
        self.ent_search.grid(row=0, column=1)
        self.btn_search.grid(row=0, column=2)

