# class Dog:->
# basic class with some objects created using the constructor
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

# minghao = Dog("Minghao", "27", "Male")

# print(minghao)
# ``````````````````````````````````````````````````````
# Adding an Attribute to the Object
# class Dog:->
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

# minghao = Dog("Minghao", "27", "Male")

# minghao.height = 8

# print(minghao.height)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Removing an Attribute to the Object->>
# class Dog:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

# pet = Dog("Minghao", "27", "Male")

# delattr(name)

# print(pet.name)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Modify Object Properties
# class Dog:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

# pet = Dog("Minghao", "27", "Male")

# print(pet.name)

# pet.name = "Jun"

# print(pet.name)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Delete Object Properties
# class Dog:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

# pet = Dog("Minghao", "27", "Male")

# print(pet.name)

# del pet.name

# print(pet.name)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Object Methods
# class Dog:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

#     def greeting(self):
#         print("Good Morning")    



# pet = Dog("Minghao", "27", "Male")

# pet.greeting()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Vacation:

    def __init__(self, place, distance, weather):
        self.place = place
        self.distance = distance
        self.weather = weather
    def tuesday(self):
       print("We will be hiking on Tuesday.")
   
summer = Vacation("Hawaii", 2000, "Sunny")

summer.rating = 10

summer.weather = "rainy"

print(summer)

print(summer.rating)

print(summer.weather)
