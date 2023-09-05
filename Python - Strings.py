#Python - Format - Strings
intAge = 37
intDateOfBirthYear = 1986

strMyText = "I was born in {} and I am {} years old."
print(strMyText.format(intAge,intDateOfBirthYear))

strMyText = "I was born in {1} and I am {0} years old."
print(strMyText.format(intAge,intDateOfBirthYear))

#----------------------------------------------------------
#Python - Escape Characters

#How to add "'" charachter to a string ---> We add bachslash before "'" character
strText01 = "It\'s alright." # OR strText01 = "It""'""s alright."
print(strText01)

#How to add backslash "\" charachter to a string
strText02 = "This will insert one \\ (backslash)."
print(strText02)

#New Line
strText03 = "Hello\nCanada!"
print(strText03)

#Carriage Return
strText04 = "Hello\rWorld!"
print(strText04)

#This example erases one character (backspace):
strText05 = "Hello \bWorld!"
print(strText05)

#A backslash followed by three integers will result in a octal value:
strText06 = "\123\111\101\126\101\123\110"
print(strText06)

#A backslash followed by an 'x' and a hex number represents a hex value:
strText07 = "\x48\x65\x6c\x6c\x6f"
print(strText07)
