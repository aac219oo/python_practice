num = int(input("質數："))
count = 0
for i in range(2, num):
    if (num%i == 0):
        print("不是質數")
        break
    else:
        print("是質數")
        break

for j in range(2, num):
    if (num%j != 0):
        count += 1

print(count)
