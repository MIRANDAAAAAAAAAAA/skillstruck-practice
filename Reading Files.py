# Reading Files
# ->
# file = open("example.txt","r")
# print(file.read())
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Closing Files
# ->
# file.close()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# put everything together
# ->
# file = open("example.txt","r")
# print(file.read())
# file.close()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Reading Files
# ->
# file = open("example.txt","r")
# print(file.read())
# file.close()

# &     Create a text file that has a .txt extension and enter in a sentence or two.

# Navigate back to your Python file that has a .py extension.

# Inside your Python file create a variable and assign it to a command to open the text file. Make sure to include the r which means to read!

# In a print statement, read the text file. This should print the contents of the text file to the console.

# (the "r" it means read)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# file = open("red.txt", "r")
# print(file.readline())
# print(file.readline())
# file.close

# file = open("red.txt", "r")
# print(file.read(10))
# print(file.read(10))
# file.close


# file = open("speech.txt" , "r")
# # print(file.read())
# file.close


# 

# file = open("practice.txt" , "r")
# print(file.readlines())
# print(file.readlines())
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

file = open("hello.txt", "r")
print(file.readline())
print(file.readline())
file.close