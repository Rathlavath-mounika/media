#take input from the user
num=int(input("enter a number:"))
print(f"factors of {num}are:")
for i in range(1,num+1):
    if num % i ==0:
        print(i)

#print tables from 1 to 5 with even multiplies
for num in range(1,5):
    print(f"\nmultiplication table of {num}:")
    for i in range(2,11,2):
        print(f"{num}*{i}={num*i}")
