import tkinter as tk
from tkinter import filedialog, messagebox

# 1. 新增功能：清空文字編輯區
def new_file():
    # "1.0" 代表第一行第0個字元，tk.END 代表最後
    text_area.delete("1.0", tk.END)


# 2. 讀取功能：開啟檔案對話框 -> 讀取檔案 -> 顯示在 Text 區塊
def open_file():
    path = filedialog.askopenfilename(filetypes=[("Text Files",
                                                  "*.txt"), ("All Files",
                                                             "*.*")])
    if path:
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
                text_area.delete("1.0", tk.END)  # 載入前先清空舊內容
                text_area.insert(tk.END, content)
        except Exception as e:
            messagebox.showerror("錯誤", f"無法開啟檔案：\n{e}")


# 3. 儲存功能：開啟存檔對話框 -> 抓取 Text 區塊內容 -> 寫入檔案
def save_file():
    path = filedialog.asksaveasfilename(defaultextension=".txt",
                                        filetypes=[("Text Files", "*.txt"),
                                                   ("All Files", "*.*")])
    if path:
        try:
            with open(path, "w", encoding="utf-8") as f:
                # 抓取編輯區的所有文字
                content = text_area.get("1.0", tk.END)
                f.write(content)
            messagebox.showinfo("成功", "檔案已儲存！")
        except Exception as e:
            messagebox.showerror("錯誤", f"無法儲存檔案：\n{e}")


# --- 主視窗設定 ---
root = tk.Tk()
root.title("Python 簡易記事本")
root.geometry("500x400")

# 上方按鈕區塊 (使用 Grid 排列按鈕)
frame_btn = tk.Frame(root)
frame_btn.pack(pady=10)

btn_new = tk.Button(frame_btn, text="新增", width=10, command=new_file)
btn_open = tk.Button(frame_btn, text="讀取", width=10, command=open_file)
btn_save = tk.Button(frame_btn, text="儲存", width=10, command=save_file)

btn_new.grid(row=0, column=0, padx=5)
btn_open.grid(row=0, column=1, padx=5)
btn_save.grid(row=0, column=2, padx=5)

# 4. 修改功能：Text 元件本身就支援鍵盤輸入與編輯
# expand=True, fill='both' 讓編輯區隨著視窗拉大而延伸
text_area = tk.Text(root, font=("微軟正黑體", 12), undo=True)
text_area.pack(expand=True, fill="both", padx=10, pady=5)

root.mainloop()
