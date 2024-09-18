choice = input("Choose a letter")

my_list = ["red", "orange", "yellow", "green", "blue", "purple", "black", "white", "gray", "pink", "indigo", "brown", "tan", "gold", "silver"]

total = 0

for x in my_list:
    if choice in x:
        total = total + 1

print("There are " + str(total) + " items in the list that have the letter " + choice + " in it.")