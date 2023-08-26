print("--------------------------")                   # ------------
print("Welcome to anagram program")                   # Welcome note
print("--------------------------")                   # ------------
str1 = str(input("First String: ")).lower()           # Get First String from user
str2 = str(input("Second String: ")).lower()          # Get Second String from user
intLengthStr1 = len(str1)                             # Extract length of string (integer)
intLengthStr2 = len(str2)                             # Extract length of string (integer)
intReturn = 1                                         # An integer variable to determine whether two inputted string are same or not
if intLengthStr1 == intLengthStr2:                    # Check length of two string
    for elm1 in sorted(str1):
        if intReturn == 0:
            break
        for elm2 in sorted(str2):
            if elm1 == elm2:
                intReturn = 1
                break
            else:
                intReturn = 0
    if intReturn == 1:
        print("The two inputted words are anagram")
    else:
        print("The two inputted words are NOT anagram")
else:                                                 # length of two string are not same
    print("The two inputted words are NOT anagram")   # If length of two string are not equal together my result Certainly FALSE
