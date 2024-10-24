# list = ["HYUNJIN" for i in range(13)]
# print(list)

# rows = 13
# my_list = [1,2,3,4,5]
# list = [[j for j in my_list] for i in range(rows)]

# print(list)


# rows = 3
# my_rows = [1,2,3,4,5]
# list = [[j for j in my_rows] for i in range(rows)]

# print(list)


# pets = ["dogs", "cats", "frogs", "bear", "fish"]
# print(pets)


# pets = 3
# my_rows = ["dogs", "cats", "frogs", "bear", "fish"]
# list = [[j for j in my_rows] for i in range(pets)]

# print(list)


# CHALLENGES


rows = input("Input a list of weather: ").split()
cols = ["windy", "breezy", "calm"]
list = [[(i + " " + j) for j in cols] for i in rows]

print(list)
