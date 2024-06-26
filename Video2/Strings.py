str = " this is a string."
str2 = 'Chandan'
str3 = """this is triple quote string"""

# to print the sentence in next line use escape sequence character

str4 = "this is another string \nThis is another printed in next line using ESC(escape sequence characters)."
print(str4)



# length of string
print(len(str2))


# print the index of the string
print(str2[0])
print(str2[0 : 4])
print(str2[-7 : -5])


# string functions

str = "i am a coder."
print(str)
newStr = str.endswith("er.") #returns true if string ends with substr
print(newStr)
newStr = str.capitalize() #capitalize the 1st char
print(newStr)
newStr = str.replace("coder" , "Programmer") #replace all occurrences old with new
print(newStr)
newStr = str.find("a") #returns 1st index of 1st occurrence 
print(newStr)
newStr = str.count("coder") #counts the occurrence of substr in string  
print(newStr)


# question 1 => Write a program to input user's first name and print its length

# name = input("Enter your first name : ")
# print("length of your name is : ",len(name))

# question 2 =>  Write a program to find the occurrence of $ in the string
# dollar = input("what is the currency of usa  : ")
# print(dollar.count("$"))


# Conditional Statements
age = input("enter your age : ")
age = int(age)

if (age < 18):
    print("you are not allowed to drive")
elif(age >= 18 and age < 100):
    print("you are allowed to drive")
else:
    print("unfortunately your age is invalid for driving");


# practice question =>
# 1. Write a program to check if a number entered by user is odd or even
# 2. Write a program to find the greatest of 3 number enters by user.
# 3. Write a program to check if a number if multiple of 7 or not 