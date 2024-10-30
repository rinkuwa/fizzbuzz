import random
import tkinter as tk

def generate_bingo_card():
    # 各列の範囲からランダムに数字を選び、中央をFREEに設定
    card = [
        random.sample(range(1, 16), 5),      # B列
        random.sample(range(16, 31), 5),     # I列
        random.sample(range(31, 46), 4)[:2] + ["FREE"] + random.sample(range(31, 46), 4)[2:],  # N列
        random.sample(range(46, 61), 5),     # G列
        random.sample(range(61, 76), 5)      # O列
    ]
    return [list(row) for row in zip(*card)]  # 転置して横にする

def toggle_color(i, j, label):
    # クリックでセルの色を切り替え、リーチ・ビンゴをチェック
    clicked_cells[i][j] = not clicked_cells[i][j]
    label.config(bg="blue" if clicked_cells[i][j] else "white")
    check_reach_or_bingo()

def check_reach_or_bingo():
    # 横、縦、斜めでビンゴ/リーチの判定
    reach, bingo = False, False
    for i in range(5):
        if all(clicked_cells[i]): bingo = True
        elif sum(clicked_cells[i]) == 4: reach = True
        if all(row[i] for row in clicked_cells): bingo = True
        elif sum(row[i] for row in clicked_cells) == 4: reach = True

    # 斜めチェック
    if all(clicked_cells[i][i] for i in range(5)) or all(clicked_cells[i][4-i] for i in range(5)):
        bingo = True
    elif sum(clicked_cells[i][i] for i in range(5)) == 4 or sum(clicked_cells[i][4-i] for i in range(5)) == 4:
        reach = True
    
    # 結果表示
    reach_label.config(text="ビンゴ！" if bingo else "リーチ" if reach else "", 
                       fg="red" if bingo else "blue", font=("Helvetica", 24 if bingo else 14))

def display_bingo_card(root, card):
    for widget in root.winfo_children():
        if isinstance(widget, tk.Label) and widget != reach_label:
            widget.destroy()

    for i, row in enumerate(card):
        for j, num in enumerate(row):
            label = tk.Label(root, text=str(num).center(5), borderwidth=2, relief="solid", 
                             width=8, height=4, bg="white")
            label.grid(row=i, column=j, padx=2, pady=2)
            label.bind("<Button-1>", lambda e, i=i, j=j, label=label: toggle_color(i, j, label))

root = tk.Tk()
root.title("Bingo Card")

# 最初のカードと選択状態を表示
bingo_card = generate_bingo_card()
clicked_cells = [[False] * 5 for _ in range(5)]
display_bingo_card(root, bingo_card)

# リーチやビンゴ表示用
reach_label = tk.Label(root, text="", fg="blue", font=("Helvetica", 14))
reach_label.grid(row=6, column=0, columnspan=5, sticky="w", padx=10, pady=10)


root.mainloop()
