# # MULTIPLY PARAMETERS IN PYTHON FUNCTON
# # ->
# def fish(first,second):
#     print("Your fist bias was " + first)
#     print("Your bias still now " + second)
    

# fish("minghao", "minghao and jun")
# fish("minghao", "jun and mingaho")
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # Local And Global Scope Variables
# # ->
# cute = " I love minghao "
# def myfunction():
#     bias = "seventeen"
#     print(bias)

# myfunction()

# print(cute)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

choice1 = int(input("What is the first number?"))
choice2 = int(input("What is the second number?"))

def my_function(first, second):
	if first < second :
		print(first)
	else:
		print(second)
		

my_function(choice1,choice2)

# def print_smallest_number(num1, num2):
#     if num1 < num2:
#         print(num1)
#     else:
#         print(num2)

