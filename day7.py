def fruit_info(fruit_name,colour="red"):
    print(fruit_name+colour)

fruit_info("apple")
fruit_info("cherry")
fruit_info("straberry")

#keyword arguments
def sample(firstname,lastname):
    print(firstname+lastname)
sample(firstname="mounika",lastname="rathlavath")

#positional arguments
def sample(x,y,z):
    print(x,y,z)
sample(1,2,3)

#arbitary arguments
def sample(*a):
    print(a)
sample(4,5,6)

#return function
def sample():
    print("hello mounika")
    return("execution completed")
print(sample())

#lambda function
f_class=lambda x:"hi"+x

print(f_class("mounika"))






