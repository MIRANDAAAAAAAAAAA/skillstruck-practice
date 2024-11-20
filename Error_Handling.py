# Exception Handling:
# try:
#     print(greeting)
# except:
#      print("A problem occured")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # Else 
# greeting = "Hello"

# try:
#     print(greeting)
# except:
# #     print("A problem occurred")
# # else:
# #     print("The code worked without a problem")  
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # Finally

# greeting = "Hello"

# try:
#     print(greeting)
# except:
#     print(A problem has occured")
# else:
#     print("The code worked without a problem")
# finally:
#     print("Your exception handeling is complet")  
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# slices = int(input("Enter the total number of slices of pizza: "))
# people = int(input("Enter the number of people at the party: "))


# try:
    
#     slices_per_person = slices / people
# except:
    
#     print("Your code doesn't account for if a user tries to enter 0 people")
# else:
    
#     print("There is no problem")
#     print(f"Each person gets {slices_per_person:.2f} slices of pizza.")
# finally:
    
#     print("Your exception handling is complete")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# SEEDS_PER_SUNFLOWER = 300

# try:
#     seeds = int(input("Enter the total number of sunflowers: "))

# # total_seeds = sunflowers * SEEDS_PER_SUNFLOWER  
# except:
    
#     print("There is a problem")
# else:
    
#     print("There is no problem")
#     print(f"The farm generates a total of {total_seeds} seeds.")
# finally:
    
#     print("Your exception handling is complete")




# SEEDS_PER_SUNFLOWER = 300
# sunflowers = int(input("Enter the number of sunflowers: "))

# try:
#     total_seeds = sunflowers * SEEDS_PER_SUNFLOWER
# except:
    
#     print("There is a problem")
# else:
    
#     print("There is no problem")
#     print(f"The farm generates a total of {total_seeds} seeds.")
# finally:
   
#     print("Your exception handling is complete")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 import os
os.path.adventure()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
os.path.isfile()
* This function specifies whether the file exists or not. This function returns a boolean True or False.

import os 
cutename = os.path.isfile("C:\\User\owl.png")
print(cutename)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 os.path.isdir()
* This function specifies whether the directory exists or not. This function returns a boolean True or False.

import os 
cutename = os.path.isdir("C:\\Users")
print(cutename)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
os.path.remove()
* This function will remove a file from the directory. In this example, assume the file named owl already exists.

import os 
os.path.remove("C:\\User\owl.png")
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 os.path.basename()
* It is used to return the basename of the file. This function basically return the file name from the path given. 

import os
cutename = os.path.basename("\squirrel\elepthant.png")
print(cutename)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
os.path.dirname()
* This function gives us the directory name where the folder or file is located.
import os
cutename = os.path.dirname("/squirrel/elepthant.png")
print(cutename)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
sys.path()
* When you start a Python file, one of the things it creates automatically is a list that contains all of directories it will use to search for modules when importing. This list is available in a variable named sys.path. Here is an example of printing out sys.path. Note that the empty '' entry means the current directory.

import sys 
sys.path
['',
'C:\\opt\\Python36\\python36.zip',
'C:\\opt\\Python36\\DLLS',
'C:\\opt\\Pyhton36\\lib',
'C:\\opt\\Python36',
'C:\\opt\\NanoDano\\AppData\\Roaming\\Python\\Python36\\site-packages',
'C:\\opt\\Python36\\lib\\site-packages',
'C:\\opt\\Python36\\lib\\site-packages\\win32',
'C:\\opt\\Python36\\lib\\site-packages\\win32\\lib',
'C:\\opt\\Python36\\lib\\site-packages\\Pythonwin']