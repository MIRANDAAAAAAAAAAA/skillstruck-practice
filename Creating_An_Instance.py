Create an Object/Instance:
class Person:


    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

p1 = Person("Minghao", "27", "Male")

print(p1)


```````````````````````````````````````````````````````

Accessing Attributes of an Object:
class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

p1 = Person("minghao", "27", "Male")

print(p1.name)


`````````````````````````````````````````````````````


We can also concatenate different parts of the object like this.:
class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

p1 = Person("minghao", "27", "Male")

print("Person 1: " + p1.name + " " + p1.age + " " + p1.gender)


# ``````````````````````````````````````````````````````


# Another Instance of the Class named Person
class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

p1 = Person("minghao", "27", "Male")
p2 = Person("Jun", "28", "Male")

print("Person 1: " + p1.name + " " + p1.age + " " + p1.gender)
print("Person 2: " + p2.name + " " + p2.age + " " + p2.gender)


# ``````````````````````````````````````````````````````


This will just print them out as a list
class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

p1 = Person("minghao", "27", "Male")
p2 = Person("Jun", "28", "Male")

print(p1.name)
print(p2.gender)
print(p1.age)
print(p2.name)
print(p2.gender)
print(p2.age)


``````````````````````````````````````````````````````


Checkpoint:
class Hat:

    def __init__(self, kind, color, material):
        self.kind = kind
        self.color = color
        self.material = material                       

myObject = Hat(kind, color, material)


# class Pet:

    def __init__(self, cute, demons, small):
        self.cute = cute
        self.demons = demons
        self.small = small

p1 = Pet("Minghao", "27", "Male")
p2 = Pet("Jun", "28", "Male")
p3 = pet("wonwoo", "27", "Male")





class Fruit:

    def __init__(self, shape, kind, size, cute):
        self.shape = shape
        self.kind = kind
        self.size = size
        self.cute = cute

p1 = Fruit("Minghao", "27", "Male", "yes")
p2 = Fruit("Jun", "28", "Male", "yes")
p3 = Fruit("wonwoo", "27", "Male", "maybe")
p4 = Fruit("scoups", "28", "Male", "maybe")


print(p1.kind)       
print(p2.kind)
print(p3.kind) 
print(p4.kind)  