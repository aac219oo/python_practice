print("請輸入5組分數取最高分")

scores = []

for i in range(5):
    while True:
        scoreInput = input(f"請輸入第{i+1}個分數：")

        if not scoreInput:
            print("請輸入分數")
            continue

        if not scoreInput.isdigit():
            print("請輸入整數，不可包含文字或特殊符號！")
            continue

        try:
            score = int(scoreInput)

            if 100 >= score >= 0:
                scores.append(score)
                break
            else:
                raise ValueError("請輸入 0 到 100 之間的整數！")
        
        except ValueError as message:
            print(f"輸入錯誤：{message}")

maxScore = max(scores)
minScore = min(scores)
sumScore = sum(scores)
print("最高分為:", maxScore)
print("最低分為:", minScore)
print("分數總和為:", sumScore)
