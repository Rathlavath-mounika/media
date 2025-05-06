size=5
center =size //2
for i in range(size):
    for j in range(size):
        if i==center and j==center:
            print("*",end="")
        else:
            print("",end="")
    print()
