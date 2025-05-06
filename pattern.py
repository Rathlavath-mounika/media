#Task1: Print the following pattern 
# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5
rows=5
for i in range(1,6):
    for j in range(rows):
        print(i, end=" ")
    print()
# Task2:  Print the following pattern 
# 1 
# 2 2 
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
rows=5
for i in range(1,6):
    for j in range(i):
        print(i, end=" ")
    print()
