# year = int(input("What year do you want to check?"))

# if year % 4 == 0:
# 	if  == 0:
# 		if  == 0:
# 			print(str(year) + " is a leap year")
# 		else:
# 			print(str(year) + " is not a leap year")
# 	elif 5 < year:

#     else:

		
# else:


year = int(input("What year do you want to check?"))




if year % 4 == 0:
    if str(year)[2:] == "00":
        if year % 400 == 0:
            print(str(year) + " is a leap year")
        else:
            print(str(year) + " is not a leap year")
    else:
        print(str(year) + " is a leap year")
else:
    print(str(year) + " is not a leap year")