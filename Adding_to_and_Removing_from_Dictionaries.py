# ADDING ITEMS
# ->
# cute = {
#     "minghao": 8,
#     "vance": 15,
#     "alice": 13
# }

# cute["jun"] = 8

# print(cute)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Keep in mind that you can also create an empty dictionary and add items to that as well.
# cute = {
#      "minghao": 8,
#     "vance": 15,
#     "alice": 13
# }

# print(cute)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# REMOVING ITEMS
# ->
# cute = {
#     "minghao": 8,
#     "vance": 15,
#     "alice": 13
# }

# print(cute)

# cute.pop("vance")

# print(cute)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHECKPOINT
# ->
# friends = { 
#     "Shane" : 10, 
#     "Samantha" : 9, 
#     "Shiloh" : 12, 
#     "Sean" : 11 
# }

# friends["sebastian"] = 8

# print(friends)


# friends = {
#   "Shane" : 10, 
#     "Samantha" : 9, 
#     "Shiloh" : 12, 
#     "Sean" : 11 
# }

# print(friends)

# friends.pop("Shiloh")

# print(friends)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Dictionary of Shapes
# ->
# my_shape = input("What shape do you want to add?")
# my_shape_height = int(input("How tall is your shape?"))

# shapes = {
#     "Triangle": 8,
#     "Circle": 15,
#     "Square": 10,
# 	"Rectangle" : 12,
# }

# shapes[my_shape] = my_shape_height

# print(shapes)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


name = input("Which tree do you want to remove?")
trees = {
	"aspen" : 75,
	"pine" : 82,
	"maple" : 60,
	"oak" : 65,
	"willow" : 80,
	"cottonwood" : 100,	
}

trees.pop(name)
print(trees)