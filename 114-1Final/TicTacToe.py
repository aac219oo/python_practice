import tkinter as tk # 匯入 tkinter 模組
import json # 匯入 json 模組
import os # 匯入 os 模組以檢查檔案是否存在

class TicTacToe:
    def __init__(self, master): # 初始化方法
        self.master = master # 主視窗
        self.master.title("圈圈叉叉")  # 命名應用程式的title
        self.master.geometry("350x350")  # 應用程式的視窗大小
        self.current_player = "×" # 當前玩家
        self.board = [""] * 9  # 3x3 棋盤
        self.scores = {"×": 0, "○": 0, "Draw": 0}  # 初始化分數

        # 從檔案載入分數
        self.load_scores()

        # 建立開始畫面
        self.start_frame = tk.Frame(self.master)
        self.start_frame.pack(expand=True)

        self.start_label = tk.Label(self.start_frame, text="歡迎來到圈圈叉叉~~~", font=("Arial", 16))
        self.start_label.pack(pady=20)

        self.start_button = tk.Button(self.start_frame, text="開始遊戲", command=self.start_game, font=("Arial", 16))
        self.start_button.pack(pady=10)

    def load_scores(self):
        if os.path.exists("scores.json"):
            with open("scores.json", "r") as f:
                self.scores = json.load(f)

    def save_scores(self):
        with open("scores.json", "w") as f:
            json.dump(self.scores, f)

    def start_game(self):
        self.start_frame.pack_forget()  # 隱藏開始畫面
        self.setup_game()

    def setup_game(self):
        # 設定 Grid 的權重
        for i in range(3):
            self.master.grid_columnconfigure(i, weight=1)
            self.master.grid_rowconfigure(i, weight=1)

        # 建立九宮格按鈕
        self.buttons = []
        for r in range(3):
            row_buttons = []
            for c in range(3):
                btn = tk.Button(self.master, command=lambda r=r, c=c: self.make_move(r, c), height=2, width=5, font=("Arial", 60))  # 設定字型大小
                btn.grid(row=r, column=c, sticky="nsew", padx=2, pady=2)
                row_buttons.append(btn)
            self.buttons.append(row_buttons)

        # 顯示目前玩家的標籤
        self.status_label = tk.Label(self.master, text=f"當前玩家: {self.current_player}", font=("Arial", 16))  # 設定字型大小
        self.status_label.grid(row=3, column=0, columnspan=3)

        # 顯示計分板
        self.score_label = tk.Label(self.master, text=self.get_score_text(), font=("Arial", 16))  # 設定字型大小
        self.score_label.grid(row=5, column=0, columnspan=3)

        # 重新開始按鈕
        self.restart_button = tk.Button(self.master, text="重新開始", command=self.restart_game, font=("Arial", 16))  # 設定字型大小
        self.restart_button.grid(row=4, column=0, columnspan=3)
        self.restart_button.grid_remove()  # 隱藏重啟按鈕

    def get_score_text(self):
        return f"計分板 叉叉: {self.scores['×']} 圈圈: {self.scores['○']} 平手: {self.scores['Draw']}"

    def make_move(self, r, c):
        index = r * 3 + c
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.current_player
            self.buttons[r][c].config(text="×" if self.current_player == "×" else "○")
            if self.check_winner():
                self.status_label.config(text=f"{self.current_player} 贏了!")
                self.scores[self.current_player] += 1  # 更新分數
                self.save_scores()  # 保存分數
                self.restart_button.grid()  # 顯示重啟按鈕
            elif "" not in self.board:
                self.status_label.config(text="平局!")
                self.scores["Draw"] += 1  # 更新平局分數
                self.save_scores()  # 保存分數
                self.restart_button.grid()  # 顯示重啟按鈕
            else:
                self.current_player = "○" if self.current_player == "×" else "×"
                self.status_label.config(text=f"當前玩家: {self.current_player}")

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # 行
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # 列
            (0, 4, 8), (2, 4, 6)               # 對角線
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True
        return False

    def restart_game(self):
        self.current_player = "×"
        self.board = [""] * 9
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].config(text="")
        self.status_label.config(text=f"當前玩家: {self.current_player}")
        self.restart_button.grid_remove()  # 隱藏重啟按鈕
        self.score_label.config(text=self.get_score_text())  # 更新記分顯示

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
