# Quick Links

- [Dictionary in Python](#dictionary-in-python)
- [Nested Dictionary](#nested-dictionary)
- [Dictionary Methods](#dictionary-methods)
- [Sets in Python](#sets-in-python)
- [Sets Methods](#sets-methods)



# Dictionary in Python

**Dictionaries are used to store data values in <span style="color :blue;">key:value</span> pairs**

**They are unordered , mutable and don't allow duplicate keys**

```bash
dictionary = {
    "name" : "Saichandan",
    "age" : 19,
    "languages" : ["Javascript","Python","C"]
}

```

```bash
print(dictionary)
```

**Output**

```bash
{
    'name': 'Saichandan',
    'age': 19,
    'languages': ['Javascript', 'Python', 'C']
}
```

dictionary[key] = "value"

<br/>

**Dictionaries are mutable so values can be changed**

dictionary["name"] = "chandan" => #override the value

```bash
{
    'name': 'chandan',
    'age': 19,
    'languages': ['Javascript', 'Python', 'C']
}
```

**New key value pairs can be added**

dictionary["name"] = "Saichandan"
dictionary["surname"] = "gorli"

```bash
{
    'name': 'Saichandan',
    'age': 19,
    'languages': ['Javascript', 'Python', 'C'],
    'surname' : "gorli"
}
```

## Nested Dictionary

```bash
resume = {
    "fullname" : "Saichandan",
    "languages" :
{
    "Javascript" : "Experience 2 years",
    "Python" : "Experience 2 years",
    "C" : "Experience 2 years"
    }
}


```

```bash
print(resume)
```

**Output**

```bash
{
    'fullname': 'Saichandan',
     'languages':
    {
    'Javascript': 'Experience 2 years',
    'Python': 'Experience 2 years',
    'C': 'Experience 2 years'}
}

```

## Dictionary Methods

```bash
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

```

**1. Method**

```bash
print(resume.keys()) #returns all keys
```

**1. Output**

```bash
dict_keys(['fullname', 'total experience', 'languages'])
```


**2. Method**

```bash
print(resume.get("languages")) #returns the key according to value
```

**2. Output**

```bash
{'Javascript': 'Experience 2 years', 'Python': 'Experience 2 years', 'C': 'Experience 2 years'}
```

**3. Method**

```bash
print(resume.values()) #returns all values
```

**3. Output**

```bash
dict_values(['Saichandan', '4 years', {'Javascript': 'Experience 2 years', 'Python': 'Experience 2 years', 'C': 'Experience 2 years'}])

```

**4. Method**

```bash
print(resume.items()) #returns all (key , value) pairs as tuple
```

**4. Output**

```bash
dict_items([('fullname', 'Saichandan'), ('total experience', '4 years'), ('languages', {'Javascript': 'Experience 2 years', 'Python': 'Experience 2 years', 'C': 'Experience 2 years'})])

```

**5. Method**

```bash
print(resume.popitem()) #pops the key value pairs
```

**5. Output**

```bash
('languages', {'Javascript': 'Experience 2 years', 'Python': 'Experience 2 years', 'C': 'Experience 2 years'})

```

**6. Method**

```bash

resume.update({"city":"Mahad"}) #insert the specified items to the dictionary
print(resume)

```

**6. Output**

```bash
{'fullname': 'Saichandan', 'total experience': '4 years', 'city': 'Mahad' }
```


# Sets in Python
1. **Set is the collection of the unordered items**

2. **Each element in the set must be unique and immutable**


numbers = {1,2,3,4}
set2 = {1,2,2,2,2}

- repeated elements stored only once ,so it resolved to {1,2}

```bash
null_set = set() #empty set syntax
```


## Sets Methods

```bash
collection3.add(el) # adds an element

collection3.discard(el) #discard or remove the element 

collection3.remove(el) #remove the element

collection3.clear() # empties the set

collection3.copy() # copy the set

collection3.union(collection4) # combines both set values and returns new

collection4.pop() # removes a random value

collection4.intersection(collection3) # combines both set common value and returns new
```