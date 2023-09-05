
#List Comprehension - Exapmle 01
lstNames = ["Siavash","Mehrzad","Soodabeh","Siamak","Vida","Morteza"]
lstSelected = []

for x in lstNames:
    if "ava" in x:
        lstSelected.append(x)
print(lstSelected)

#List Comprehension - Exapmle 01
#The Syntax
#newlist = [expression for item in iterable if condition == True]
#The return value is a new list, leaving the old list unchanged.
lstFruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in lstFruits if "a" in x]
print(newlist)

newlist = [x for x in lstFruits if x != "apple"]
print(newlist)

#Iterable
newlist = [x for x in range(10)]
print(newlist)
#Accept only numbers lower than 5:
newlist = [x for x in range(10) if x < 5]
print(newlist)

#Expression
#The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:
#Set the values in the new list to upper case:
newlist = [x.upper() for x in lstFruits]
print(newlist)

newlist = ['hello' for x in lstFruits]
print(newlist)

#The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
#Return "orange" instead of "banana":
newlist = [x if x != "banana" else "orange" for x in lstFruits]
print(newlist)
# The expression in the example above says:
# "Return the item if it is not banana, if it is banana return orange".
