my_list = [[0, 1, 2], [10, 15, 20], [100, 200, 300], [5, 6, 7]]

rows = 4
cols = 3

answer = int(input("What do you want to multiply by?"))

for i in range(rows):
    for j in range(cols): 
        my_list[i][j] = my_list[i][j] * answer

print(my_list)  



# my_list = [[40, 45, 50], [6, 7, 8], [100, 200, 300], [50, 60, 70], [9, 0, 1]]
# rows = 5
# cols = 3


# for i in range(rows):
#     for j in range(cols):
#         my_list[i][j] = my_list[i][j] * 3

# print(my_list)        



# my_list = [[0, 1, 2], [10, 15, 20], [100, 200, 300], [5, 6, 7]]
# multiplier = int(input("Enter a multiplier: "))
# for i in range(len(my_list)):  
#     for j in range(len(my_list[i])): 
#         my_list[i][j] *= multiplier 

# print("Updated 2D list:")
# for row in my_list:
#     print(row)



# # x = int(input("What is the first number?"))
# # y = int(input("What is the second number?"))
# # z = int(input("What is the third number?"))

# # my_list = [[0, 1, x], [10, 15, y], [100, 200, 300], [5, 6, z]]

# # rows = 4
# # cols = 3

# # largest = 0

# # for i in range(rows):
# #     for j in range(cols):
# #         if my_list[i][j] > largest:
# #             largest = my_list[i][j]
# # print(largest)        
