import os
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import google.generativeai as genai
import threading

# システム環境変数からAPIキーを取得
gemini_api_key = os.getenv("gemini_api_key")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment.")

# Gemini APIキーを設定
genai.configure(api_key=gemini_api_key)

# モデルの初期化
model = genai.GenerativeModel("gemini-pro")


def generate_diary_entry(title, keywords, text_area):
    """
    題名とキーワードに基づいて日記を生成する関数。
    """
    prompt = f"""
    Create a short diary entry of about 100 characters, written in first-person perspective.
    Use the provided keywords in the diary entry.
    Title: {title}
    Keywords: {', '.join(keywords)}
    Diary:
    """

    try:
        response = model.generate_content(prompt)
        if response.text:
            text_area.config(state="normal")
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, response.text.strip())
            text_area.config(state="disabled")
        else:
            messagebox.showinfo("情報", "生成されたテキストがありません。")
    finally:
        button.config(state="normal")  # ボタンを再び有効化


def generate_diary():
    """
    日記を生成するための処理を呼び出す関数（UIからの呼び出し用）。
    """
    title = title_entry.get()
    keywords_str = keywords_entry.get()
    keywords = [keyword.strip() for keyword in keywords_str.split(",")]
    if not title or not keywords_str:
        messagebox.showerror("エラー", "題名とキーワードを入力してください。")
        return

    button.config(state="disabled")  # ボタンを一時的に無効化
    # スレッドでAPI呼び出しを行う
    threading.Thread(
        target=generate_diary_entry, args=(title, keywords, text_area)
    ).start()


# UIの作成
root = tk.Tk()
root.title("空想日記 powerd by gemini")
root.geometry("600x400")

# スタイル
style = ttk.Style()
style.configure("TButton", padding=5)
style.configure("TLabel", padding=5)
style.configure("TEntry", padding=5)


# 題名ラベルと入力欄
title_label = ttk.Label(root, text="題名:")
title_label.pack(pady=5)
title_entry = ttk.Entry(root, width=50)
title_entry.pack(pady=5)

# キーワードラベルと入力欄
keywords_label = ttk.Label(root, text="キーワード（カンマ区切り）:")
keywords_label.pack(pady=5)
keywords_entry = ttk.Entry(root, width=50)
keywords_entry.pack(pady=5)

# 生成ボタン
button = ttk.Button(root, text="日記を生成", command=generate_diary)
button.pack(pady=10)

# スクロールテキストエリア
text_area = scrolledtext.ScrolledText(
    root, wrap=tk.WORD, width=60, height=10, state="disabled"
)
text_area.pack(pady=10)

root.mainloop()
