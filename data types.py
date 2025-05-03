# 1.implement the count method on a list by taking input from the user without using the actual method.
user_input=int(input("enter list elements separated by spaces:"))
my_list=user_input.split()
my_list=[int(i)for i in my_list]
target=int(input("enter the element to count:"))
count=0
for item in my_list:
    if item== target:
        count+=1
print(f"the element {target}appears{count}items in the list.")
#2.implement the copy method on a list just as the above condition.
class MyClass:
    def __init__(self,value):
        self.value = value
    def copy(self):
        return MyClass(self.value)
a=MyClass(10)
b=a.copy()
print(a.value)
print(b.value)
print(a is b)



