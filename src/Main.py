import tkinter as tk

from src.Model import Model
from src.View import View
from src.Controller import Controller


class Application(tk.Frame):
    def __init__(self, root):
        # スーパークラスのコンストラクタを呼び出し
        super().__init__(root)

        # モデルをインスタンス化
        self.model = Model(root)

        # ビューをインスタンス化
        self.view = View(root, self.model)

        # コントローラーをインスタンス化
        self.controller = Controller(root, self.model, self.view)

        # Viewにメソッドをセット
        self.view.btn_search["command"] = lambda: self.controller.call_btn_clicked()

        # 画面の設定
        root.geometry(str(self.model.width) + "x" + str(self.model.height))
        root.title(self.model.title)


def main():
    root = tk.Tk()
    window = Application(root)
    window.mainloop()


if __name__ == "__main__":
    main()
