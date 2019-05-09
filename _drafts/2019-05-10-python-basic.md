---
layout: post
title: 'Python 基础语法'
subtitle: 'codecademy 的 Learn Python 2 笔记'
date: 2019-05-12
author: June
cover: /assets/img/post/2019-05-12/cover.png
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

## FUNCTIONS

```py

```


---


