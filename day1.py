details=[{
    "name":"mounika",
    "age":19,
    "citizen":"indian"},{
        "name":"shivaji",
        "age":20,
        "citizenship":"indian"}]
for person in details:
    if person["age"]>19 and person ["citizenship"]=="indian":
        person["eligible"]=True
    
    else:
     person["eligible"]=False
     print("wait for some time")
print(details)

my_tuple=(1,2,5,8,3,9,7,2,5,7,12,65,8)
unique_list=list(set(my_tuple))
print(unique_list)


