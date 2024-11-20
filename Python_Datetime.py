# Now:
# import datetime

# x = datetime.datetime.now()

# print(x)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Date as a String:

# import datetime

# x = datetime.datetime.now()

# print(x.strftime())
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Today:

# import datetime

# x = datetime.date.today()

# print(x)

# Answer is 2024-10-24

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Local Time:
# import datetime

# x = datetime.datetime.now()

# print(x.strftime("%X"))

# Answer is 13:54:41
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 2 Digit Month:
# import datetime

# x = datetime.datetime.now()

# print(x.strftime("%m"))

# Answer is 10 because that is what month it is 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 2 Digit Day:
# import datetime

# x = datetime.datetime.now()

# print(x.strftime("%d"))

# Answer is 24 because thta is what day it is today
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 4 Digit Year:
# import datetime

# x = datetime.datetime.now()

# print(x.strftime("%Y"))

# Answer is 2024 because it ti the year that it is right now
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Further Date Methods:

# Code            Description            Example

# %a              Weekday short           Thurs

# %A              Weekday long            Thursday

# %b              Month short             Sept

# %B              Month long              September

# %y              2 Digit Year            22

# %M              Minute                  35

# %S              Second                  30
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHECKPOINTS:

# import datetime

# x = datetime.datetime.now()

# print(x)



# import datetime

# x = datetime.datetime.now()

# print(x.strftime("%X"))



# import datetime

# x = datetime.datetime.now()

# print(x.strftime("%M"))



# import datetime

# x = datetime.datetime.now()

# print(x.strftime("%Y"))



# import datetime

# today = datetime.date.today()

# print(today)


# import datetime

# x = datetime.datetime.now()

# print(x.strftime("%A"))
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHALLENGES:

# from datetime import datetime


# birth_month = int(input("Enter your birth month (as a number from 1 to 12): "))


# current_month = datetime.now().month


# if birth_month >= current_month:
#     months_until_birthday = birth_month - current_month
# else:
#     months_until_birthday = (12 - current_month) + birth_month


# if months_until_birthday == 0:
#     print("Your birthday month is this month!")
# else:
#     print(f"Months until your birthday month: {months_until_birthday}")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# import datetime

# x = datetime.datetime.now()

# month = int(x.strftime("%m"))

# day = int(x.strftime("%d"))

# print(datetime.datetime.now())

# print(day)

import datetime

x = datetime.datetime.now()

new_year = datetime.datetime(x.year, 1, 1)

months_passed = x.month - new_year.month
days_passed = x.day - new_year.day

print(f"It has been {months_passed} months and {days_passed} days since your New Year's resolution. How are you doing?")
