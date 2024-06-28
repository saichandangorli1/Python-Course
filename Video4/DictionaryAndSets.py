import datetime

current_year = datetime.datetime.now().year
age = current_year - 2005
dictionary = {
    "name" : "Saichandan",
    "age" : age,
    "languages" : ["Javascript","Python","C"]
    
} 


dictionary["name"] = "chandan"
print(dictionary)

dictionary["name"] = "Saichandan"
dictionary["surname"] = "gorli"
print(dictionary)


# Nested Dictionary

resume = {
    "fullname" : "Saichandan",
    "total experience" : "4 years",
    "languages" :
{ 
    "Javascript" : "Experience 2 years",
    "Python" : "Experience 2 years",
    "C" : "Experience 2 years"
    },
}
# print(resume)


# Dictionary Methods

print(resume.keys()) #returns all keys
print(resume.get("languages")) #returns the key according to value
print(resume.values()) #returns all values
print(resume.items()) #returns all (key , value) pairs as tuple
print(resume.popitem()) #pops the key value pairs
resume.update({"city":"Mahad"}) #insert the specified items to the dictionary
print(resume)

# print(list[resume.items()])



# Sets in Python 

collection = {1,2,3,4,"chandan"}
print(collection)
print(type(collection))
print(len(collection))
collection = {1,2,3,4,4,4,4,4,"chandan"}
print(collection) #sets ignore the multiple or repeated values
print(type(collection)) #sets ignore the multiple or repeated values
print(len(collection)) #sets ignore the multiple or repeated values

# to create empty set

collection2  = set()
print(collection2) 


# # Sets Methods

collection3 = set()
collection4 = {1,2,5,6,7,8,9}


collection3.add(1)
collection3.add(2)
collection3.add(3)
collection3.add(6)
collection3.add(5)
print(collection3)
collection3.remove(2)
print(collection3)
collection3.add(4)
print(collection3)
collection3.pop()
# print(collection3)
# collection3.clear()
print(collection3)
collection3.discard(4)
print(collection3)


# # collection3.add(el) # adds an element
# # collection3.discard(el) #discard or remove the element 
# # collection3.remove(el) #remove the element
# # collection3.clear() # empties the set
# # collection3.copy() # copy the set
# # collection3.union(collection4) # combines both set values and returns new
# # collection4.pop() # removes a random value
# # collection4.intersection(collection3) # combines both set common value and returns new




# Questions 1 => Store following word meanings in a python dictionary : 
# 1.table: "a piece of furniture ","list of facts and figures"
# 2. cat : "a small animal"

dictionary2 = {
    "table":[ "a piece of furniture ","list of facts and figures"],
    "cat" : "a small animal"
}
print(dictionary2)


# Questions 2 => you are given a list of subjects for students .Assume one classroom is required for 1 subject how many classrooms are needed by all students

subjects = {"python","java","C++","python","javascript","java","python","java","C++","C"}
print("classrooms required are:",len(subjects))


# Questions 3 => WAP tp enter marks of 3 subjects from the user and store then in  a dictionary . Start with an empty dictionary and add one by one . use subject name as a key and marks as a value

student ={}
sub1 = input("enter you subject")
marks1 = input("enter you marks")
sub2 = input("enter you subject")
marks2 = input("enter you marks")
sub3 = input("enter you subject")
marks3 = input("enter you marks")

# student.update({sub1 : marks1,})
# student.update({sub2 : marks2,})
# student.update({sub3 : marks3})

student.update({sub1 : marks1,sub2 : marks2,sub3 : marks3})

print(student)

# Questions 4 =>figure out a way to store 9 and 9.0 as a separate value in the set. 

number = {9,9.0}
print(number)
print(type(number))