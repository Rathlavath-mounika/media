# 1)Implement the program to print true when the first and last element in the list was even, else print false.
num=[2,5,7,8,4]
if num[0]%2==0 and num[-1]%2==0:
    print(True)
else:
    print(False)
#2) implement the program to create a function which performs the count method. Without using any methods.
def count_char(text,char):
    count=0
    for c in text:
        if c==char:
            count+=1
    return count
text="banana"
char="a"
print("count:",count_char(text,char))
#3) write a program to print the prime numbers in the new list from the existing list.
def is_prime(n):
    if n <=1:
        return False
    return True
existing_list=[3,4,7,9,11,15,17,21,23,29]
prime_list=[num for num in existing_list if is_prime(num)]
print("prime numbers in the new list:",prime_list)