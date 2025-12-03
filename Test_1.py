import tkinter as tk
root = tk.Tk()
root.title("grid() 佈局示範")
root.geometry("350x160")
# 標題（跨兩欄）
title = tk.Label(root, text="會員登入系統", font=("Arial", 14))
title.grid(row=0, column=0, columnspan=2, pady=10)
# 帳號欄位
tk.Label(root, text="帳號：").grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_user = tk.Entry(root)
entry_user.grid(row=1, column=1, sticky="w", padx=5, pady=5)
# 密碼欄位
tk.Label(root, text="密碼：").grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_pass = tk.Entry(root, show="*")
entry_pass.grid(row=2, column=1, sticky="w", padx=5, pady=5)
# 按鈕（左右貼齊）
btn_login = tk.Button(root, text="登入")
btn_login.grid(row=3, column=0, sticky="we", padx=5, pady=10)
btn_clear = tk.Button(root, text="清除")
btn_clear.grid(row=3, column=1, sticky="we", padx=5, pady=10)
root.mainloop()
