import tkinter as tk
import random

class BingoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bingo")
        self.pre = []
        self.remaining_numbers = list(range(1, 76))  # 1から75の数字のリスト

        # ラベルとボタンを作成
        self.number_label = tk.Label(self.root, text="ビンゴ大会", font=("Helvetica", 24))
        self.number_label.pack(pady=20)

        self.pick_button = tk.Button(self.root, text="数字を引く", font=("Helvetica", 16), command=self.pick_number)
        self.pick_button.pack(pady=20)

        self.history_label = tk.Label(self.root, text="履歴: ", font=("Helvetica", 16))
        self.history_label.pack(pady=20)

    def pick_number(self):
        if self.remaining_numbers:  # まだ残っている数字がある場合
            number = random.choice(self.remaining_numbers)
            self.remaining_numbers.remove(number)  # 重複を避けるために数字を削除
            self.pre.append(number)
            
            # ラベルを更新
            self.number_label.config(text=f"選ばれた数字: {number}")
            self.history_label.config(text=f"履歴: {', '.join(map(str, self.pre))}")
        else:
            # すべての数字が選ばれたらメッセージを表示
            self.number_label.config(text="終了!")

# メインウィンドウを作成
root = tk.Tk()
app = BingoApp(root)

# アプリを実行
root.mainloop()