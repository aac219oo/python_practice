'''
images\113-2midterm\forLoopTriangles.jpg
第1题
請撰寫一程式能以for敘述及*字元,印出下列圖形,高度寬度在10以內。

(1)
**********
*********
********
*******
******
*****
****
***
**
*

(2)
**********
 *********
  ********
   *******
    ******
     *****
      ****
       ***
        **
         *
'''

print("(1)")
for i in range(10):
    for ii in range(10):
        if i <= ii:
            print("*", end="")
    print("")
print("")
print("(2)")
for i in range(10):
    for ii in range(10):
        if i >= ii:
            print(" ", end="")
        else:
            print("*", end="")
    print("")