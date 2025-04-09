'''
images\113-2midterm\forLoopSequence.jpg
第6题
請利用多重迴圈撰寫程式以印出下列三種樣式。(每小題各5分)

(1)
1
12
123
1234
12345
123456

(2) 
1
22
333
4444
55555
666666

(3)
6
55
444
3333
22222
111111
'''

print("(1)")
for i in range(1,7):
    for ii in range(1,7):
        if i >= ii:
            print(ii, end="")
    print("")
print("")
print("(2)")
for i in range(1, 7):
    for ii in range(1, 7):
        for iii in range(1, 7):
            if i == ii:
                if iii <= ii:
                    print(i, end="")
    print("")
print("")
print("(3)")
for i in range(6,0,-1):
    for ii in range(6,0,-1):
        for iii in range(6,0,-1):
            if i == ii:
                if ii <= iii:
                    print(i, end="")
    print("")