# file = open("report.txt", "a")
# file.write("Quote was said by Gandhi")
# file.close()

# file = open("report.txt", "r")
# print(file.read())
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# file = open("example.txt", "w")
# file.write("Jun is also nice!")
# file.close()m   


# file = open("new_document.txt", "w")


# file = open("porcupine.txt", "w")
# file.write("In short, I love to code!")
# file.close()

# file = open("porcupine.txt", "r")
# print(file.read())

answer = input("What do you want to repalce the text with?")
file = open("report.txt", "w")
file.write(answer)
file.close()

file = open("report.txt", "r")
print(file.read())
