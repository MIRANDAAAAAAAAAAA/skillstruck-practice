number = int(input("What number do you want to know?"))

print(range(number))
factors = []
for x in range(2, number):
    if number % x == 0: