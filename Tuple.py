# t1=(1,2,3,4,5,6)
# print("first",t1[0], "last",t1[5])
# print("len",len([t1]))

# create a tuple
fruits = ("apple", "banana", "mango", "orange", "grapes")

# use for loop
for fruit in fruits:
    print(fruit)

# create a nested tuple
fruits = (
    ("apple", "banana"),
    ("mango", "orange"),
    ("grapes", "pineapple")
)

# using for loop
for group in fruits:
    for fruit in group:
        print(fruit)
