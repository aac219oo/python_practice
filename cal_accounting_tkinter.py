import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# --------------------------
#        主功能邏輯
# --------------------------


def add_expense():
    item = entry_item.get()
    category = category_var.get()
    amount = entry_amount.get()
    payment = payment_var.get()
    date = entry_date.get()

    if not item or not amount:
        messagebox.showwarning("警告", "項目與金額不可為空！")
        return

    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("錯誤", "金額必須為數字！")
        return

    record = f"{date}｜{category}｜{item}｜{payment}｜{amount}\n"

    with open("expenses.txt", "a", encoding="utf-8") as f:
        f.write(record)

    messagebox.showinfo("成功", "已新增開銷紀錄！")
    clear_inputs()
    load_expenses()


def load_expenses():
    text_display.config(state="normal")
    text_display.delete("1.0", tk.END)
    try:
        with open("expenses.txt", "r", encoding="utf-8") as f:
            text_display.insert(tk.END, f.read())
    except FileNotFoundError:
        text_display.insert(tk.END, "尚無資料，請新增記錄。")
    text_display.config(state="disabled")


def clear_inputs():
    entry_item.delete(0, tk.END)
    entry_amount.delete(0, tk.END)
    entry_date.delete(0, tk.END)


def clear_display():
    text_display.config(state="normal")
    text_display.delete("1.0", tk.END)
    text_display.config(state="disabled")

# --------------------------
#        Tkinter 介面
# --------------------------

root = tk.Tk()
root.title("日常開銷紀錄系統")
root.geometry("420x500")

# 標題
label_title = tk.Label(root, text="日常開銷紀錄系統", font=("Arial", 16))
label_title.pack(pady=10)

# 項目名稱
frame_item = tk.Frame(root)
frame_item.pack(pady=5)
tk.Label(frame_item, text="項目：", font=("Arial", 12)).pack(side=tk.LEFT)
entry_item = tk.Entry(frame_item, width=25)
entry_item.pack(side=tk.LEFT)

# 分類
frame_category = tk.Frame(root)
frame_category.pack(pady=5)
tk.Label(frame_category, text="分類：", font=("Arial", 12)).pack(side=tk.LEFT)
category_var = tk.StringVar()
category_choices = [
    "飲食",
    "交通",
    "娛樂",
    "生活用品",
    "醫療",
    "學習",
    "其他",
]
category_var.set(category_choices[0])

option_menu = tk.OptionMenu(frame_category, category_var, *category_choices)
option_menu.config(width=12)
option_menu.pack(side=tk.LEFT)

# 金額
frame_amount = tk.Frame(root)
frame_amount.pack(pady=5)
tk.Label(frame_amount, text="金額：", font=("Arial", 12)).pack(side=tk.LEFT)
entry_amount = tk.Entry(frame_amount, width=25)
entry_amount.pack(side=tk.LEFT)

#支付方式
frame_payment = tk.Frame(root)
frame_payment.pack(pady=5)
tk.Label(frame_payment, text="支付方式：", font=("Arial", 12)).pack(side=tk.LEFT)
payment_var = tk.StringVar()
payment_choices = [
    "現金",
    "信用卡",
    "LinePay",
    "其他",
]
payment_var.set(payment_choices[0])

option_payment_menu = tk.OptionMenu(frame_payment, payment_var, *payment_choices)
option_payment_menu.config(width=12)
option_payment_menu.pack(side=tk.LEFT)


# 日期
frame_date = tk.Frame(root)
frame_date.pack(pady=5)
tk.Label(frame_date, text="日期：", font=("Arial", 12)).pack(side=tk.LEFT)
entry_date = tk.Entry(frame_date, width=25)
entry_date.pack(side=tk.LEFT)
tk.Label(frame_date, text="（可留空）").pack(side=tk.LEFT)

# 功能按鈕
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=15)

btn_add = tk.Button(frame_buttons, text="新增紀錄", width=12, command=add_expense)
btn_add.grid(row=0, column=0, padx=5)

btn_load = tk.Button(frame_buttons, text="讀取紀錄", width=12, command=load_expenses)
btn_load.grid(row=0, column=1, padx=5)

btn_clear = tk.Button(frame_buttons, text="清除輸入", width=12, command=clear_inputs)
btn_clear.grid(row=1, column=0, padx=5, pady=5)

btn_clear_display = tk.Button(frame_buttons, text="清除顯示區", width=12, command=clear_display)
btn_clear_display.grid(row=1, column=1, padx=5, pady=5)

# 顯示區
text_display = tk.Text(root, width=50, height=15, state="disabled")
text_display.pack(pady=10)

# 啟動主畫面
root.mainloop()
