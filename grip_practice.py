import tkinter as tk

root = tk.Tk()
root.geometry("350x140")

# 1. 設定 Grid 的權重 (關鍵步驟)
# range(3) 代表針對第 0, 1, 2 欄/列進行設定
# weight=1 代表該欄/列會隨著視窗變大而分配多餘空間 (達到RWD效果)
for i in range(3):
    root.grid_columnconfigure(i, weight=1)
    root.grid_rowconfigure(i, weight=1)

# 2. 建立九宮格按鈕
# 使用雙層迴圈來佈局 3x3
count = 1
for r in range(3):      # Row 0 到 2
    for c in range(3):  # Column 0 到 2
        btn = tk.Button(root, text=f"{count}")
        
        # sticky='nsew': 讓按鈕向 上下左右(North, South, East, West) 延伸填滿格子
        # padx, pady: 按鈕之間的間距
        btn.grid(row=r, column=c, sticky="nsew", padx=2, pady=2)
        
        count += 1

root.mainloop()