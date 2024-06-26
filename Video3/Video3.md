# Quick Links
- (Lists in Python)[#lists-in-python]
- (Note For List)[#note-for-list]
- (List Slicing)[#list-slicing]
- (List Methods)[#list-methods]
- (Tuples in Python)[#tuples-in-python]
- (Note For Tuple)[#note-for-tuple]
- (Tuple Slicing)[#tuple-slicing]
- (Tuple Methods)[#tuple-methods]



# Lists in Python

**A build-in data type that stores set of values**

**it can store elements of different types (integers ,,string ,etc.)**

```bash****
marks = [1,2,3,4,5,6,7,8]

students = ["sai",18,"saichandan"]

students[0] = "chandan" #allowed in python

len(student) #returns length
```

## Note For List

- **Lists are mutable means they are allowed to change value**

- **Strings are immutable means they are not allowed to change value**

## List Slicing

**Similar to String Slicing**

```bash****
list_name[starting_index : ending_index]
```

**Student**

```bash****
studentsRollNo = [1,2,3,4,5,6]
```

1. **studentsRollNo[1:4]** is **[2,3,4]**
2. **studentsRollNo[:4]** is same as **studentsRollNo[0:4]** is **[1,2,3,4]**
3. **studentsRollNo[1:]** is same as **studentsRollNo[1 : len(studentsRollNo)]**
4. **studentsRollNo[-3:]** is same as **studentsRollNo[-3 : len(studentsRollNo)]**


## List Methods

```bash
list = [10,11,12,13,14] 
print(list) => [10, 11, 12, 13, 14] 

list.append(value)
list.append(15)
print(list) => [10, 11, 12, 13, 14, 15] #adds one element at the end

list.sort()
print(list) => [10, 11, 12, 13, 14, 15] #sorts in ascending order 

list.reverse()
print(list) => [15, 14, 13, 12, 11, 10] # reverse the List 

list.remove(value)
list.remove(14)
print(list) => [15, 13, 12, 11, 10] # remove or delete the target value

list.pop()
print(list) => [15, 13, 12, 11] #pops or removes the last element from the list

list.insert(idx,value)
list.insert(3,20)
print(list) => [15, 13, 12, 20, 11] #insert the new element to list


```


## Tuples in Python
**A build-in data type that lets us create immutable sequence of values just like String**

### Syntax

```bash
tup = (1,2,3,4)
print(tup)
print(type(tup))
print(tup[0])
print(tup[1])
# tup[0] = 1 #is not allowed
```

## Note For Tuple

- If we want to pursue the type of tuple as "tuple" , we must declare **(comma => , )** at the end at the variable initialization , else the python compiler will declare it as the respectively data type

- e.g => tup = (1) will declared as int also for all data types until we add a **(comma => , )**
- e.g => tup = (1,) now its data type is "tuple"



## Tuple Slicing


```bash****
tup = (1,2,3,4,5,6)
```

1. **tup[1:4] is [2,3,4]**
2. **tup[:4] is same as tup[0:4] is 1,2,3,4]**
3. **tup[1:] is same as tup[1 : len(tup)]**
4. **tup[-3:] is same as tup[-3 : len(tup)]**


## Tuple Methods

```bash
tup = (1,2,3,4)
print(tup.index(3))
print(tup.count(4))
```