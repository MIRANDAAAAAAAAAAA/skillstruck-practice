# my_list = [int(n) for n in input().split()]
# total = 0

# for x in my_list:
#     total = total + x
# #print(len(my_list))	
# average = total/len(my_list)
# #print(average)
# for x in my_list:
#     if x > average:
#         print(x)

letter = input("Choose a letter")

my_list = ["red", "orange", "yellow", "green", "blue", "purple", "black", "white", "gray", "pink", "indigo", "brown", "tan", "gold", "silver"]

total = 0

for x in my_list:
	if letter in x: 
		total = total + x
		
print(total)