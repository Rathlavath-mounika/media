#BY Using the While Loop
#Task 1 : Find the second prime of the given number ?
num=int(input("enter a number:"))
count=0
next_num=num+1
while True:
    is_prime=True
    if next_num < 2:
        is_prime=False
    else:
        i=2
        while i*i <=next_num:
            if next_num%i==0:
                is_prime=False
                break
            i+=1
    if is_prime:
        count+=1
        if count==2:
            print("second prime after",num,"is",next_num)
#By using break control statement
#Task 2 : Break the loop if  Condition matches with the given number?
for i in range(1,11):
    if i==5:
        print("match found!breaking the loop.")
        break
    print("current number:",i)   
# By using the continue control statement
#  Task 3 : print the numbers from 1 to 100, but it should not print multiples of 3?
for i in range(1,101):
    if i%3==0:
        continue
    print(i)


