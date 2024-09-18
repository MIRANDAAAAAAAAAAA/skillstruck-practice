# members = ["Minghao", "Jun", "Scoups", "Joshua","Wonwoo"]

# print(members)


# members = ["Minghao", "Jun", "Scoups", "Joshua","Wonwoo"]

# print(members[2])


# print(members[2] + " is the best.")

# my_list = [int(n) for n in input("List 9 numbers:").split()]

# print(my_list[4]*100)

# my_list = 


# # clothes = ["shirt", "pants", "hat", "shoes", "socks"]

# # print(clothes[3])

# clothes = ["shirt", "pants", "hat", "shoes", "socks"]

# print(clothes[0])



# clothes = ["shoes", "hat", "socks", "shirt"]

# # if "pants" in clothes:
# # 	print("Yes")

# treat = "I love to eat jelly beans"

# myList = treat.split()

# # print(myList)

# treat = "I love to eat jelly beans"

# myList = treat.split()

# print(myList[2])

# treat = "I love to eat jelly beans"

# myList = treat.split()

# print(myList[2])


# string = ["swim", "run", "slither", "crawl"]

# Ask the user for 5 strings
my_list = input("Enter 5 actions separated by spaces: ").split()

# Check if the user entered exactly 5 items
if len(my_list) == 5:
    # Pull out the first and last item in the list
    first_item = my_list[0]
    last_item = my_list[-1]
    
    # Create a print statement to concatenate the first and last item
    print(f"Some animals {first_item} and some {last_item}")
else:
    print("Please enter exactly 5 actions.")
