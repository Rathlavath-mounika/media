rows=5
letter=ord('a')
for i in range(1,6):
    line = ""
    for j in range(1,i+1):
        if i==3 and j==2:
            line += "  "
        elif i==4 and (j==2 or j==3):
            line += "  "
        else:
            line += chr(letter) +" "
            letter += 1
    print(line.strip())
    