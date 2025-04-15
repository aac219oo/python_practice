size = 9  # 行數
for i in range(size):
    for j in range(size):
        if i == 0 or i == size - 1:  # 第一行或最後一行
            print("*", end=" ")
        elif j == 0 or j == 1 or j == size - 2 or j == size - 1:  # 邊緣
            print("*", end=" ") if (i == 1 or i == size - 2) else print(" ", end=" ")
        elif j == i or j == size - 1 - i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()