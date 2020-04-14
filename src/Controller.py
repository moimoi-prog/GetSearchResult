class Controller(object):
    def __init__(self, root, model, view):
        self.root = root
        self.model = model
        self.view = view

    # 検索ボタンクリック時起動メソッドを定義
    def call_btn_clicked(self):
        self.model.btn_clicked()
