# RANGE REVIEW
->
small = ["yumm", "cool", "Blank", "pink"]

print(small[1:3]) 



for cookies in range(3,98):
    print(cookies)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# STEP
->
small = ["minghao", "jun", "wonwoo", "scoups", "mingyu", "hoshi"]
print(small[0:6:2])
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# REPLACING
->
small =["minghao", "jun", "wonwoo", "scoups", "mingyu", "hoshi"]

small[3] = "the8_my_man"

print(small)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# LENGTH
->
small = ["minghao", "jun", "wonwoo", "scoups", "mingyu", "hoshi"]

print(len(small))

    * you can find out how many iteam are in the list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# SORT
->
small = ["minghao", "jun", "wonwoo", "scoups", "mingyu", "hoshi"]

small.sort()

print(small)

     * It is sourting them in ABC order
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# SORT
->
small = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,]

small.sort()

print(small)

    * This time it put in number and it worked
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# SORT IN REVERSE
->
small = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,]

small.sort(reverse=True)

print(small)

       * This method put them in reverse order
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHECKPOINT
->
activities = ["movies", "skating", "bowling", "laser tag", "escape room", "trampoline park", "library"]

print(activities[0:3])

activities[6] = "water park"

print(activities)

print(len(activities))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# FIND THE LARGEST VALUE (CHALLENGE)
->
my_list = [int(n) for n in input().split()]
biggest = 0
for x in my_list:
	if x > biggest:
		biggest = x

print(biggest)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# GREATER THAN LEFT INDEX (CHALLENGE)
->
my_list = [int(number) for number in input().split()]
current = my_list[0]
for number in my_list:
    if number > current:
        print(number)
    current = number
        



