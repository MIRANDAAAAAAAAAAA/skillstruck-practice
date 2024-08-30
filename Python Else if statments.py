
# # Check the conditions and print the appropriate output
# if number <= 50:
#     print("Fewer than average")
# else:
#     print("More than average")


# # Create the variable
# coins = 10

# # Compare the variable and print the appropriate response
# if coins > 20:
#     print("You have more than enough to buy a puppy.")
# elif coins == 20:
#     print("You have exactly enough to buy a puppy.")
# else:
#     print("You do not have enough to buy a puppy.")


# favorite = "pink"

# if favorite == "orange":
#     print("You love tigers")
# elif favorite == "pink":
#     print("You love flamingos")
# elif favorite == "yellow":
#     print("You love toucans")
# else:
#     print("You like a unique animal")


# tokens = 1

# # if tokens >= 5:
# #     print("You have enough tokens for lazer tag")
# # elif tokens == 4:
# #     print("You have enough tokens for mini golf")
# # elif tokens == "3":
# #     print("You have enough tokens for the arcade")
# # else:



# # Take three numbers as input from the user
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))

# # Find and print the smallest number
# if num1 <= num2 and num1 <= num3:
#     print(num1)
# elif num2 <= num1 and num2 <= num3:
#     print(num2)
# else:
#     print(num3)

# # Create a list of 4 strings of the spikiest animals
# animals = [
#     "Porcupine",
#     "Pufferfish",
#     "Hedgehog",
#     "Sea Urchin"
# ]

# # # Create a for loop to iterate through the list
# # for animal in animals:
 
# #     print(animal + " is the spikiest animal ever!")


# sports = ["soccer", "basketball", "volleyball"]

# for x in sports:
#     print("I love to play " + x)


# # windows = [3, 5, 2, 10, 6]
# # for x in windows:
# #     print(x * 2)

# # Take two integers as input from the user
# var1 = int(input("Enter the first number (var1): "))
# var2 = int(input("Enter the second number (var2): "))

# # Ensure var1 is less than var2
# if var1 < var2:
#     # Print all numbers from var1 to var2, inclusive
#     for number in range(var1, var2 + 1):
#         print(number, end=" ")
# else:
#     print("Error: var1 should be less than var2.")

# # Take two integers as input from the user
# start = int(input("Enter the first number (start of the range): "))
# end = int(input("Enter the second number (end of the range): "))

# # Ensure start is less than end
# if start <= end:
#     # Initialize a variable to hold the sum
#     total_sum = 0

#     # Iterate through the range and calculate the sum
#     for number in range(start, end + 1):
#         total_sum += number

#     # Print the total sum
#     print("The sum of the numbers from", start, "to", end, "is", total_sum)
# else:
#     print("Error: The first number should be less than or equal to the second number.")



start = int(input("Enter the first number (start of the range): "))
end = int(input("Enter the second number (end of the range): "))
  
total_sum = 0

for number in range(start, end):
    total_sum += number 

print(total_sum)


