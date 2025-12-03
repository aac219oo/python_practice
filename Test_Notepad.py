import tkinter as tk
from tkinter import filedialog, messagebox

def open_file():
    path = filedialog.askopenfilename()
    if path:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, content)

def save_file():
    path = filedialog.asksaveasfilename(defaultextension=".txt")
    if path:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text_area.get("1.0", tk.END))
        messagebox.showinfo("成功", "檔案已儲存！")

root = tk.Tk()
root.title("簡易記事本")

frame_btn = tk.Frame(root)
frame_btn.pack(pady=5)

tk.Button(frame_btn, text="開啟檔案", width=12, command=open_file).grid(row=0, column=0, padx=5)
tk.Button(frame_btn, text="儲存檔案", width=12, command=save_file).grid(row=0, column=1, padx=5)

text_area = tk.Text(root, width=60, height=18)
text_area.pack()

root.mainloop()
