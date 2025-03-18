width = int(input("寬："))
calWidth = width//2
for x in range(0, width+1):
    for y in range(0, width+1):
        if (x+y >= calWidth and x-y >= -calWidth and x+y <= calWidth*3 and x-y <= calWidth):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("")
