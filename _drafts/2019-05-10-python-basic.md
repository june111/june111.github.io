---
layout: post
title: 'Python 基础语法'
subtitle: 'codecademy 的 Learn Python 2 笔记'
date: 2019-05-12
author: June
reward: 1
tags: 技术
---

# Python 基础语法

## 基础

### Print Statements

关键字：`print`

```py
print("Hello World!")
```

### 注释

```py
# one line
```

### Variables

* String
* Number
* Boolean
`True` and `False`

```py
# string
string1 = "Hi"

# Multi-line Strings -- use triple quotes
string2 = """A
long
line"""

# integer
int1 = 1

# float
float1 = 1.0

# e indicating the power of 10 => 150
float4 = 1.5e2 
```

### Converting between data types

`str()`, `int()`, `float()`

### Strings 

methods: `len()`, `lower()`, `upper()`, `str()`

```py
# Escaping characters
'There\'s a snake in my boot!'

# Access by Index
fifth_letter = "MONTY"[4]

# using methods
parrot = "norwegian blue"
parrot.lower()
parrot.upper() 
len(parrot)
str(parrot)

# String Formatting with %
# used the % operator to replace the %s placeholders
print "The %s who %s %s!" % ("Knights", "say", "Ni")
```

### DATE AND TIME

```py
from datetime import datetime
now = datetime.now()

current_year = now.year
current_month = now.month
current_day = now.day

print '%02d/%02d/%04d' % (now.month, now.day, now.year)
```

### 算术运算符

加减乘除 `+, -, *, and /`

取余数 `％`

## CONDITIONALS & CONTROL FLOW

### comparators

`<, <=, >, >=`

`==, != `

### Boolean operators

与，或，非  `and, or, not `

优先次序：`not` > `and` > `or`

`()` 优先 

## FUNCTIONS

### Conditional Statement

```py
def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:          
        return -1
    else:
        return 0
```

### Modules

```py
# generic import
import math

# Function Imports
# from module import function
from math import sqrt

# Universal Imports
# from module import *
from math import *
```

### Built-In Functions

`max()`, `min()`, `abs()`, `type()`

```py
maximum = max(1,2,444,22) # 444

minimum = min(222,11,3342) # 11

absolute = abs(-42) # 42

print type(22) # <type 'int'>

def distance_from_zero(n):
  if type(n) == int or type(n) == float:
    return abs(n)
  else:
    return "Nope"

def median(lst):
    sorted_list = sorted(lst)
    if len(sorted_list) % 2 != 0:
        #odd number of elements
        index = len(sorted_list)//2 
        return sorted_list[index]
    elif len(sorted_list) % 2 == 0:
        #even no. of elements
        index_1 = len(sorted_list)/2 - 1
        index_2 = len(sorted_list)/2
        mean = (sorted_list[index_1] + sorted_list[index_2])/2.0
        return mean
```

### Anonymous Functions

```py
lambda x: x % 3 == 0

# Is the same as

def by_three(x):
  return x % 3 == 0
```
 
## LISTS AND DICTIONARIES

### Lists

```py
numbers = [5, 6, 7, 8]
print numbers[1] + numbers[3] # 14

# update
zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
zoo_animals[2] = "hyena" # ["pangolin", "cassowary", "hyena", "tiger"]

# add
# append() takes exactly one argument
zoo_animals.append('dog')
print len(zoo_animals)

# Maintaining Order
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")# Use index() to find "duck"
animals.insert(duck_index, "cobra")

# sort animals into alphabetical order
animals.sort()

# remove
animals.remove("cobra")

# .pop(index)
animals.pop(1) 

# del
del(animals[1])

# List Slicing Syntax
# [start:end:stride]
# we did not modify the original list
l = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print l[2:9:2]
# => [9, 25, 49, 81]

# Reversing a List
letters = ['A', 'B', 'C', 'D', 'E']
print letters[::-1]
# => ['E', 'D', 'C', 'B', 'A']

def double_list(x):
# range() function is just a shortcut for generating a list
  for i in range(0, len(x)):
    x[i] = x[i] * 2
  return x

def remove_duplicates(inputlist):
    if inputlist == []:
        return []
    
    # Sort the input list from low to high    
    inputlist = sorted(inputlist)
    # Initialize the output list, and give it the first value of the now-sorted input list
    outputlist = [inputlist[0]]

    # Go through the values of the sorted list and append to the output list
    # ...any values that are greater than the last value of the output list
    for i in inputlist:
        if i > outputlist[-1]:
            outputlist.append(i)
        
    return outputlist
```
### Building Lists

```py
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50
# => [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]

doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]
# => [6]
```

### Dictionaries

```py
d = {'key1' : 1, 'key2' : 2, 'key3' : 3}
print d['key1'] # 1

# add new key/value pairs
menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair

# remove
# del dict_name[key_name]
del d["key2"]

my_dict = {
  "fish": ["c", "a", "r", "p"],
  "cash": -4483,
  "luck": "good"
}
print my_dict["fish"][0]
```

### Iterators for Dictionaries

`.items()`, `.keys()`, `.values()`

```py
d = {
  "Name": "Guido",
  "Age": 56,
  "BDFL": True
}
print d.items()
# => [('BDFL', True), ('Age', 56), ('Name', 'Guido')]
 
print d.keys()
# => ['Name','Age','BDFL']

print d.values()
# => ['Guido',56,True]
```

## Loops

### For loop

```py
start_list = [1,2,3,4]
for number in start_list:
  print number

d = {"foo" : "bar"}
for key in d: 
  print d[key]  # prints "bar" 

word = "Marble"
for char in word:
  print char, # M a r b l e
  # The , character after our print statement means that our next print statement keeps printing on the same line.
  
choices = ['pizza', 'pasta', 'salad', 'nachos']
for index, item in enumerate(choices):
  print index + 1, item

# zip will create pairs of elements when passed two lists, and will stop at the end of the shorter list.
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
for a, b in zip(list_a, list_b):
  print max(a,b)

# For / else
# the else statement is executed after the for, but only if the for ends normally—that is, not with a break
num = [2,3,4]
for i in num:
  print i
else:
  print "over"

def digit_sum(n):
  total = 0
  string_n = str(n)
  for char in string_n:
    total += int(char)
  return total

def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True 

def censor(text, word):
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result =' '.join(words)

    return result
```

### while 

```py
loop_condition = True

while loop_condition:
  print "I am a loop"
  loop_condition = False

# while/else
# the else block will execute anytime the loop condition is evaluated to False

def factorial(x):
    total = 1
    while x>0:
        total *= x
        x-=1
    return total
```



---


