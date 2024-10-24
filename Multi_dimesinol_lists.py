# list = [1, 1, 1, 1, 1] 

# list = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4]]


# m = 8
# list = []
# for i in range(m):
#     list.append(0)
# print(list)    






# rows = [ 1, 2, 3, 4, 5]
# cols = ["red", "orange", "yellow", "green"]
# list = []
# for i in rows:
#     col = []
#     for j in cols:
#         col.append(j)
#     list.append(col)
# print(list)    


# rows = [5]
# cols = ["red", "orange", "yellow", "green"]
# list = []
# for i in rows:
#     col = []
#     for j in cols:
#         col.append(j)
#     list.append(col)
# print(list)    





# rows = input("Input a list of weather: ").split()
# cols = ["windy", "breezy", "calm"]
# result = []
# for weather in rows:
#     temp = []
#     for wind in cols:
#         temp.append(f"{weather} {wind}")
#     temp.append(5)
#     result.append(temp)

# print(result)

# n = 5
# list = []
# for i in range(n):
#     list.append(0)
# print(list)




# rows = 5
# cols = 5
# list = []
# for i in range(cols):
#     col = []
#     for j in range(rows):
#         col.append(i)
#     list.append(col)
# print(list)


# rows = input("Input a list of weather: ").split()
# cols = ["windy", "breezy", "calm"]

# first_name = input("Enter first name: ")
# last_name = input("Enter last name: ")
# full_name = first_name + " " + last_name
# result = []
# for weather in rows:
#     temp = []
#     for wind in cols:
#         temp.append(f"{weather} {wind}")
#     temp.append(full_name) 
#     result.append(temp)
# print(result)








# rows = input("Input a list of fruits ").split()
# cols = ["apple", "grape", "peach", "cinnamon", "vanilla"]
# my_list = []
# for i in rows:
#     col = []
#     for j in cols:
#         col.append(i + " " + j)
#     my_list.append(col)
# print(my_list)



## rows = [ 1, 2, 3, 4, 5]
# cols = ["red", "orange", "yellow", "green"]
# list = []
# for i in rows:
#     col = []
#     for j in cols:
#         col.append(j)
#     list.append(col)
# print(list)    



# rows = [int(n) for n in input("Input a list of numbers").split()]

# cols = [2, 5, 10, 100]

# list = []
# for i in rows:
#     col = []
#     for j in cols:
#         col.append(j)
#         list.append(col)
# print(list)        




# Step 1: Define the columns list (values to subtract)
cols = [2, 5, 10, 100]

# Step 2: Get the user's input and convert it into a list of integers
rows = [int(n) for n in input("Input a list of numbers: ").split()]

# Step 3: Create the 2D list where each element is the result of subtracting cols from each row
result = [[row - col for col in cols] for row in rows]

# Step 4: Print the final 2D list
print(result)


# rows = [ int(n)("Input a list of fruits ").split()
# cols = ["apple", "grape", "peach", "cinnamon", "vanilla"]
# my_list = []
# for i in rows:
#     col = []
#     for j in cols:
#         col.append(i + " " + j)
#     my_list.append(col)
# print(my_list)



# rows = [int(n) for n in input("Input a list of numbers").split()]

# cols = [ ]

# list = []
# for i in rows:
#     col = []
#     for j in cols:
#         col.append( )