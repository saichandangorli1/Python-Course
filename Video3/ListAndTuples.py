# Lists in Python
marks1 = 1
marks2 = 2
marks3 = 3
marks4 = 4
marks5 = 5
marks6 = 6
marks7 = 7
marks8 = 8

#instead allocating values to different variable introducing list  

marks = [1,2,3,4,5,6,7,8]
print(marks)
print(type(marks))
students = ["sai",18,"saichandan"]
print(students)
students[0] = "chandan" 
print(students)

#List Slicing

studentsRollNo = [1,2,3,4,5,6]
print(studentsRollNo)
print(studentsRollNo[1:4])
print(studentsRollNo[1:])
print(studentsRollNo[-4:])


#List Methods

list = [10,11,12,13,14]
print(list)
list.append(15)
print(list)
list.sort()
print(list)
list.reverse()
print(list)
list.remove(14)
print(list)
list.pop()
print(list)
list.insert(3,20)
print(list)

#Tuples in Python

tup = (1,2,3,4)
print(tup)
print(type(tup))
print(tup[0])
print(tup[1])
tup[0] = 1 #is not allowed



# Tuple Methods
tup = (1,2,3,4)
print(tup.index(3))
print(tup.count(4))



# Question 1 => Write a program to ask user to enter names of their 3 favorite movies and store then in a list 

list = []
movie = input("enter your 1st favorite movies")
list.append(movie)
movie = input("enter your 2nd favorite movies")
list.append(movie)
movie = input("enter your 3rd favorite movies")
list.append(movie)
print(list)


# Question 2 => Write a program to check if a list contains a palindrome of elements .(hint : use copy(); method)

list = [1,2,3,2,1]
list2 = list.copy()
list2.reverse()
print(list,list2)
if list == list2:
    print(True)
else :
    print(False)


# Question 3 => Write a program to count the number of students with the "A" grade in the following tuple

tup = ("C","A","B","A","A","D")
print("there are",tup.count("A") , "with grade A")

# Question 4 => Write a program to store the above values in a list and sort them from "A" to "D"
list = ["C","A","B","A","A","D"]
list.sort()
print(list)