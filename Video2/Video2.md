# String

**String is data type that stores a sequence of characters**

## Quick links
- [Basic Operations](#basic-operations)
- [Indexing](#indexing)
- [Rules](#rules)
- [Slicing](#slicing)
- [Slicing (Negative)](#slicing-negative)
- [String Functions](#string-functions)
- [Conditional Statements](#conditional-statements)

### Basic Operations

**1. Concatenation**

```bash
"hello"+"world" => "helloworld"
```

**2.length of str**

```bash
len(str)
```

**3. Escape sequence character**

```bash
\n
```

### Indexing

**S a i c h a n d a n**

**&uarr; &uarr; &uarr; &uarr; &uarr; &uarr; &uarr; &uarr; &uarr; &uarr; &uarr;**

**0 1 2 3 4 5 6 7 8 9**

#### Rules

1. str = "Saichandan"

2. str[0] is 'S',str[1] is 'a'...

3. str[0] = 'C' is not allowed


### Slicing 
**Accessing the parts of string**

str[starting_index : ending_index]

1. str = Sai<span style="color: hotpink;">chan</span>dan
2. str[3 : 6] is "chan"
3. str[ : 6] is same as str[0 : 6]
4. str[1 : ] is same as str[1 : len(str)]

```bash 
print(str[0 : 2])
```


### Slicing (Negative)

**C h a n d a n**

**&uarr; &uarr; &uarr; &uarr; &uarr; &uarr; &uarr; &uarr;**

-7-6-5-4-3-2-1

str = "Chandan"
str[-5 : ] is "Ch" 

```bash
print(str[-7 : -5])
```

### String Functions

```bash
str = "i am a coder."
print(str)
newStr = str.endswith("er.") #returns true if string ends with substr
print(newStr)
newStr = str.capitalize() #capitalize the 1st char
print(newStr)
newStr = str.replace(old , new) #replace all occurrences old with new
print(newStr)
newStr = str.find(word) #returns 1st index of 1st occurrence 
print(newStr)
newStr = str.count("coder") #counts the occurrence of substr in string  
print(newStr)
```


### Conditional Statements

```bash
if-elif-else(SYNTAX)

if(condition):
    pass
elif(condition):
    pass
else:
    pass

```
