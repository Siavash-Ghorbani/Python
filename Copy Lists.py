#Copy a List

#one way is to use the built-in List method copy().
lstListSample = ["apple", "banana", "cherry"]
lstMylist = lstListSample.copy()
print(lstMylist)

#OR
#Another way to make a copy is to use the built-in method list().
lstListSample = ["apple", "banana", "cherry"]
lstMylist = list(lstListSample)
print(lstMylist)

