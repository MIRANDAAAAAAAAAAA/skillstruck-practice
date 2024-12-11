frogs = [ "Miranda", "Osmari", "Camila", "Yaneli"]

frogs.append("Xuminghao")

print(frogs)
^
# APPEND
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

frogs = [ "Miranda", "Osmari", "Camila", "Yaneli"]

frogs.extend(["Xuminghao", " Jun", "Scoups", "Vernom", "say_the_name_Seventeen"])

print(frogs)
^
# EXTEND
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

frogs = ["Food", "Beans", "Carrots", "Rice", "Eggs"]

frogs.extend("Xuminghao")

print(frogs)
^
# # EXTEND
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

frogs = ["Food", "Beans", "Carrots", "Rice", "Eggs"]

frogs.insert(3, "Xuminghao")

print(frogs)
^
# INSERT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

flowers = [ "rose", "tulip", "lilac", "sunflower"]

flowers.append("Xuminghao")

print(flowers)

flowers = [ "rose", "tulip", "lilac", "sunflower"]

flowers.extend(["Xuminghao", " Jun", "Scoups", "Vernom", "say_the_name_Seventeen"])

print(flowers)



chickens = ["Clucky", "Barbara", "Nancy", "Fran", "Rhode"]

chickens.extend(["Charlotte", "Crystal"])

print(chickens)



chickens = ["Clucky", "Barbara", "Nancy", "Fran", "Rhode"]

chickens.append("Daphne")

print(chickens)






handkerchief = ["fish", "cake", "bannan", "butter", "pizza"]

handkerchief.extend("handkerchief")

print(handkerchief)











frogs = [spelling = []

print()

frogs.extend("Xuminghao")

print(frogs) 



spelling = ["fish", "cake", "bannan", "butter", "pizza"]

word = input("What word do you want spelled out?")

spelling.("fish")
spelling.("?cake")
spelling.("bannan")

print(word)



def create_word_list(word):

    result = []
    
   
    result.append(word)
    
    
    result.extend(list(word))
    

    result.append(word)
    
    return result


if __name__ == "__main__":
    
    word = input("Enter a word: ")
    
    
    word_list = create_word_list(word)
    print(word_list)





olympics = ["running", "gymnastics", "swimming", "volleyball", "basketball"]

new_olympics = ["karate", "surfing", "baseball", "skateboarding", "sport climbing"]

olympics.extend("pig") 

print(olympics)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# OLYMIPC EVENTS (CHALLENGE)
->
olympics = ["swim","run","high_jump", "archery","karate"]

olympics.extend(["long_jump","vollball","picklball","tennis"])

print(olympics)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# LAST MINUTE TREATS (CHALLENGE)
->
first = input("What other item do you want?")
second = input("What final item do you want?")

treats = ["popcorn", "popsicles", "soda", "chips", "cookies"]

treats.append(first)
treats.append(second)

print(treats)





chickens = ["Clucky", "Barbara", "Nancy", "Fran", "Rhode"]

chickens.append("Daphne")

print(chickens)




chickens = ["Clucky", "Barbara", "Nancy", "Fran", "Rhode"]

chickens.insert(2, "Daphne")

print(chickens)

chickens = ["Clucky","Fran", "Rhode"]

chickens.extend("Fran")

print(chickens)


chickens = ["Clucky", "Barbara", "Nancy", "Fran", "Rhode"]

chickens.extend(["Charlotte", "Crystal"])

print(chickens)