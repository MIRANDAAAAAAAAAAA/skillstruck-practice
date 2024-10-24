n = int(input("How many keys in dictionary?"))


dictionary = {}
for num in range(n):
    dictionary[num] = num*num
print(dictionary)