# task:1
# 55555
# 4444
# 333
# 22
# 1
rows=5
for i in range(rows,0,-1):
    res=""
    for j in range(1,i+1,1):
        res=res+str(i)+" "
    print(res)
# task:2
# * * * * *
# * * * *
# * * *
# * *
# *
rows=5
for i in range(rows,0,-1):
    res=""
    for j in range(i,0,-1):
        res+="*"+" "
    print(res)
# task:3
# *       *
# *       *
# * * * * *
# *       *
# *       *
rows=5
mid=rows//2+1
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if j==1 or j==rows or  i==mid:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)





        