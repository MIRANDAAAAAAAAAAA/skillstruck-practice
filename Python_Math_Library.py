# Rounding Up:   Will round the value up to the next whole number no matter what the decimal value. You can think of ceil to mean ceiling

# math.celi()

# import math
# x = math.ceil(3.2)
# print(x)

# Answer was 4
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Rounding Down:   Will round the value down to the next whole number no matter what the decimal value.

# math.floor( )

# import math
# x = math.floor(3.2)
# print(x)

# answer was 3
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# The Value of Pi:   To access the value of pi, you can simply use the following code.

# import math 
# x = math.pi
# print(x)

# Answer was 3.141592653589793
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Square Root:   The following code can help you find the square root using Python code. You can think of sqrt to mean square root.

# import math
# x = math.sqrt(100)
# print(x)

# Answer was 10.2
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Multiply by a Power:  Often in math, finding a value raised to a certain power is important. For example, 3 to the power of 4 is equal to 3 × 3 × 3 × 3 = 81.

# The following code can help you easily multiply a value by any power.

# import math
# x = pow(2, 4)
# print(x)

# Answer was 16
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Give Attribution:   It's important to give proper credit when using outside libraries. This can be done with a comment in your code such as this:

#Math concepts used from the Python Math Library
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# CHALLENGES:  

# import math
# x = math.ceil(3.2)
# print(x)


# import math
# x = math.floor(3.2)
# print(x)


# import math
# x = math.sqrt(100)
# print(x)


# import math
# x = pow(2, 4)
# print(x)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# CHECKPOINTS:

# total = population / bikes
# print(total)



# from math import ceil


people = int(input("Enter the number of people in the town: "))
bikes = int(input("Enter the number of bikes in the town: "))


if bikes > 0:  
    people_per_bike = ceil(people / bikes) 
    print("In this town, for every bike that exists there are {people_per_bike} people.")
else:
    print("There are no bikes in the town.")
    print(people_per_bike)
