import tkinter as tk
from tkinter import messagebox

def load_file():
    try:
        with open("notes.txt", "r", encoding="utf-8") as f:
            content = f.read()
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, content)
    except FileNotFoundError:
        messagebox.showerror("錯誤", "notes.txt 不存在！")

root = tk.Tk()
root.title("檔案讀取範例")

btn = tk.Button(root, text="讀取 notes.txt", command=load_file)
btn.pack(pady=5)

text_area = tk.Text(root, width=50, height=12)
text_area.pack()

root.mainloop()
