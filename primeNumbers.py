num = int(input("質數："))
count = 0
for i in range(2, num):
    if (num%i == 0):
        print("不是質數")
        count += 1
        count = 1
        break
    else:
        print("是質數")
        count += 1
        count = 1
        break


