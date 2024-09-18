# lasers = [3, 10, 4, 15, 11 ]

# print(lasers[2] * 10)
# print(round(3.14159265,3))

# for x in range(0,10):
#     print(x)

# for x in range(0,10,2):
# #     print(x)

# # goldfish = [4, 8, 1, 3, 10]

# # print(goldfish[2] + 1)

# dessert = 12.4635
# print(round(dessert, 2))


# dessert = 12.4635
# print(round(dessert, 2))


# for x in range(3):
# # 	print(x)

#     for x in range(0, 6, 2):
# 	print(x)

# smells = ["skunk", "lilac", "rain", "ocean", "garbage", "cleaner", "cookies", "roses", "new car", "sweaty feet", "peach"]

# print(smells[0:8:2])





# lasers = [3, 10, 4, 15, 11 ]

# print(lasers[2] * 10)
# print(round(3.14159265,3))

# for x in range(0,10):
#     print(x)

# for x in range(0,10,2):
# # #     print(x)


# my_list = [int(n) for n in input("Enter integers separated by spaces: ").split()]

# product = 1


# for num in my_list:
#     product *= num


# # print(product)


the_list_of_number = [int(n) for n in input().split()]

the_total = 1
for one_number_from_the_list in the_list_of_number:
    the_total = the_total * one_number_from_the_list
print(the_total)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
frogs = [ "Miranda", "Osmari", "Camila", "Yaneli"]

frogs.append("Xuminghao")

print(frogs)

# APPEND
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
frogs = [ "Miranda", "Osmari", "Camila", "Yaneli"]

frogs.extend(["Xuminghao", " Jun", "Scoups", "Vernom", "say_the_name_Seventeen"])

print(frogs)

# EXTEND
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
frogs = ["Food", "Beans", "Carrots", "Rice", "Eggs"]

frogs.extend("Xuminghao")

print(frogs) 

# EXTEND
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
frogs = ["Food", "Beans", "Carrots", "Rice", "Eggs"]

frogs.insert(3, "Xuminghao")

print(frogs)

# INSERT