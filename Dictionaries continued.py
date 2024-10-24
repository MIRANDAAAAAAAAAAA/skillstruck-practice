# Dictionary Length
# # ->
# cute = {
#     "minghao": 13,
#     "hoshi": 3,
#     "woonwoo": 56,  
#     "mingyu": 34,
#     "woozi": 25,
#     "vernom": 987,
# }

# print(len(cute))

# &   You can check to see how many items are in the dictionary.  As with Python lists, when counting length we start counting at 1.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Check if Key is in the Dictionary
# ->
# the_classmates = {
#       "minghao": 13,
#     "hoshi": 3,
#     "woonwoo": 56,  
#     "mingyu": 34,
#     "woozi": 25,
#     "vernom": 987,
# }

# if "vernom" in the_classmates:
#     print("vernom is in your dictionary")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 # *You can also use not in to check your dictionary.
#     ^
# classmates = {
#       "minghao": 13,
#     "hoshi": 3,
#     "woonwoo": 56,  
#     "mingyu": 34,
#     "woozi": 25,
#     "vernom": 987,
# }

# if "vernom" in classmates:
#     print("vernom is not in your dictionary")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Converting from a Python list to a dictionary
# ->
# group = ["minghao", "scoups", "hoshi", "mingyu", "vernom"]

# group_dictionary = dict.fromkeys(group, "seventeen")

# print(group_dictionary)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CODE CHECKPOINT
# ->
# coins = {
#    		 "pennies" : 1,
#    		 "nickels": 5,
#   		 "dimes": 10,
#   		 "quarters": 25,
# }

# print(coins)
# coins["silver dollars"] = 10 ;
# coins.pop("pennies")
# print(coins)
# print(len(coins))
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# dictionary = {
# 	1: "bicycle",
# 	2: "soccer balls",
# 	3: "piano books"
# }

# dictionary[4] = input("What do you have 4 of?")
# dictionary[5] = input("What do you have 5 of?")
# dictionary[6] = input("What do you have 6 of?")
						  
# print(dictionary)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# work = {

# 	"Monday": 3,
# 	"Tuesday": 4, 
# 	"Wednesday": 2,
# 	"Thursday": 1, 
# 	"Friday": 1, 
	
# }

# work["Saturday"] = 8
# work.pop("Wednesday")
# print(len(work))

# if "Friday" in work:
# 	print("Friday is in work")

# print(work)