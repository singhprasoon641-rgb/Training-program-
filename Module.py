import math

#square root..............

print(math.sqrt(625))

# factorial..................

fact = math.factorial(6)
print("Factorial of 6:", fact)

# find floor and ceiling.........

floor_val = math.floor(4.7)
ceil_val = math.ceil(4.7)

print("Floor value of 4.7:", floor_val)
print("Ceiling value of 4.7:", ceil_val)

# Compute 5 raised to the power 3.....

result = 5 ** 3
print(result)

# math.fabs..............

import math

value = math.fabs(18)
print(value)

# find value e^3............

value = math.exp(3)
print(value)


# Convert in to degree into radians......

radian = math.radians(180)
print(radian)

# Random module............

import random
print("Random no bw 1 to 10", random.randint(1,10))

print("Random no bw 0 to 1", random.randint())

list=[10,20,30,40]
print("Random choice from list",list,"is",random.choice())

numbers = random.sample(range(1, 21), 4)
print(numbers)








