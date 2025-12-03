import tkinter as tk

def save_text():
    text = entry.get()
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(text)
    label_status.config(text="已成功寫入 output.txt！")

root = tk.Tk()
root.title("檔案寫入範例")

tk.Label(root, text="請輸入文字：").pack()
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

btn = tk.Button(root, text="寫入檔案", command=save_text)
btn.pack(pady=5)

label_status = tk.Label(root, text="")
label_status.pack()

root.mainloop()
