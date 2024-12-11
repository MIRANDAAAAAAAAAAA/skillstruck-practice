Define integer variables
num_apples = 5
num_oranges = 8

# # Define a string variable with two sets of curly brackets
# fruit_string = "I have {} apples and {} oranges."

# # Format and print the string with integer variables
# print(fruit_string.format(num_apples, num_oranges))

# string1.format(trees, bushes)

# Take input from the user as a string
input_number = input("Input: ")

# Convert each character to an integer and calculate the sum of the digits
sum_of_digits = int(input_number[0]) + int(input_number[1]) + int(input_number[2])

# Print the result using the required format
print("The sum of those digits is {}.".format(sum_of_digits))


# Take input from the user as a string
input_number = input("Input: ")

# Convert each character in the string to an integer and calculate the sum of the digits
sum_of_digits = int(input_number[0]) + int(input_number[1]) + int(input_number[2])

# Print the result using the required format
print("The sum of those digits is {}.".format(sum_of_digits))




# Take input from the user as an integer
day_of_year = int(input("Input: "))

# January 1 is a Thursday, which corresponds to day 4
starting_day = 4

# Calculate the day of the week
day_of_week = (starting_day + day_of_year - 1) % 7

# Print the result using the required format
print("The day of the week is the number {}.".format(day_of_week))


# Define integer variables
num_apples = 5
num_oranges = 8

# # Define a string variable with two sets of curly brackets
# fruit_string = "I have {} apples and {} oranges."

# # Format and print the string with integer variables
# print(fruit_string.format(num_apples, num_oranges))

# string1.format(trees, bushes)

# Take input from the user as a string
input_number = input("Input: ")

# Convert each character to an integer and calculate the sum of the digits
sum_of_digits = int(input_number[0]) + int(input_number[1]) + int(input_number[2])

# Print the result using the required format
print("The sum of those digits is {}.".format(sum_of_digits))


# Take input from the user as a string
input_number = input("Input: ")

# Convert each character in the string to an integer and calculate the sum of the digits
sum_of_digits = int(input_number[0]) + int(input_number[1]) + int(input_number[2])

# Print the result using the required format
print("The sum of those digits is {}.".format(sum_of_digits)


num1 = int(input("number of miles your car can drive in a day"))
num2 = int(input("total number of miles to get to your destination"))
total = num2/num1
print("The total number of days you will need to drive there is " + str(total))


# Receive input from the user
number = float(input("Enter a number with a decimal: "))

# Convert the number to a string
number_str = str(number)

# Find the position of the decimal point
decimal_pos = number_str.index('.') + 1

# Extract the first decimal digit
first_decimal_digit = number_str[decimal_pos]

# Print the result with the exact format
print("The first decimal digit is {}".format(first_decimal_digit))
