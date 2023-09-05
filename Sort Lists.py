# Sort List Alphanumerically
lstSort01 = ["orange", "mango", "kiwi", "pineapple", "banana"]
lstSort01.sort()
print(lstSort01)
lstSort01.sort(reverse=True)
print(lstSort01)

# Error
# lstSort02 = ["Siavash",65,73,"Canada"]
# lstSort02.sort()
# print(lstSort02)

lstSort02 = [2, 65, 73, 1]
lstSort02.sort()
print(lstSort02)
lstSort02.sort(reverse=True)
print(lstSort02)


# Customize Sort Function
def myFunction(n):
    return abs(n - 50)


lstNumber = [22, 105, 65, 73, 2, 3]
lstNumber.sort(key=myFunction)
print(lstNumber)

# Case Insensitive Sort
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
# Case sensitive sorting can give an unexpected result:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# Perform a case-insensitive sort of the list:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)

#Reverse Order
#The reverse() method reverses the current sorting order of the elements.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)