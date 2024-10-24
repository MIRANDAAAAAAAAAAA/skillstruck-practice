# file = open("example.txt", "a")
# file.write("This is the new line we added!")


# file.close()
# file = open("example.txt", "r")
# print(file.read())
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# file = open("example.txt", "a")
# file.write("I love programing!")
# file.close()

# file = open("example.txt", "r")
# print(file.read())
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# # Define the file name
# file_name = "programming_love.txt"




# with open(file_name, "a") as file:
#     file.write("I love programming!\n")


# with open(file_name, "r") as file:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# file = open("letter.txt", "a")
# file.write("From your Pen Pal")
# file.close()

# file = open("letter.txt", "r")
# print(file.read())

file = open("report.txt", "a")
file.write("Quote was said by Gandhi")
file.close()

file = open("report.txt", "r")
print(file.read())