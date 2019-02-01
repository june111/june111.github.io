---
layout: post
title: 'Java 基础语法'
subtitle: 'codecademy 的 Learn Java 笔记'
date: 2018-12-16
author: June
cover: /assets/img/post/2018-12-16/java-basis.png
reward: 1
tags: 技术
---

# Java 基础语法

## 基础

### 数据类型

* int（integer 数字）
* boolean（对错）
* char（character 字母）

### 变量

需要明确数据类型

```java
int myNumber = 42;
boolean isFun = true; 
char movieRating = 'A'; 
```

### 代码格式

用空格优化代码格式，看起来更具可读性

### 注释

单行注释
```java
// I'm a single line comment!
```

多行注释
```java
/*

Hello, 
Java! 

*/
```

### 算术运算符

加减乘除 `+, -, *, and /`

取余数 `％`

```java
int sum = 34 + 113;
int difference = 91 - 205;
int product = 2 * 8; 
int quotient = 45 / 3;
int myRemainder = 7 % 5;
```

### 关系运算符

`<, <=, >, >=`

### 比较运算符

`==, != `

## 条件与流程控制

### 布尔运算符 

与，或，非  `&&, ||, ! `

优先次序：`!, &&, ||`

括号内优先

### 条件表达式

if

if/else

if/else if/else

### 三元条件运算符(Ternary Conditional)

```java
char gameResult = (pointsScored > 20) ? 'W' : 'L';
```

### Switch

```java
int restaurantRating = 2;

switch (restaurantRating) {

    case 1: System.out.println("This restaurant is not my favorite.");
      break;

    case 2: System.out.println("This restaurant is good.");
      break;

    default: System.out.println("I've never dined at this restaurant.");
      break;
}
```

## 面向对象 (OPP)

### class, constructor, object
```java
class Dog {

  // instance variables
  int age;
  
  // class constructor
  public Dog(int dogsAge){
    age = dogsAge;
  }

  // main method 
  public static void main(String[] args) {
  // create a Dog object
  Dog spike = new Dog(2);
  }
}
```

### method

关键词 `void` 表示执行方法后，不返回任何值

```java
class Dog {
  
  int age;

  public Dog(int dogsAge) {
    
    age = dogsAge;
    
  }
  
  // 添加 method
  public void bark() {
		
    System.out.println("Woof!");
    
  }
	
  // 添加带参数的 method
  public void run(int feet) {
    
    System.out.println("Your dog ran " + feet + " feet!");

  }

  // return value
  public int getAge() {

    return age;

  }
  
  public static void main(String[] args) {
    
    Dog spike = new Dog(5);
    // 使用 method
    spike.bark();
    spike.run(40);

    // 使用返回值
    int spikeAge = spike.getAge();
    System.out.println(spikeAge);

  }

}
```

### 继承

关键字 `extends`

```java
class Car extends Vehicle {

    int modelYear;

    public Car(int year) {

        modelYear = year;

    }

    //Other methods omitted for brevity...

    public static void main(String[] args){

        Car myFastCar = new Car(2007)
        myFastCar.checkBatteryStatus();

    }
}

class Vehicle {

    public void checkBatteryStatus() {

        System.out.println("The battery is fully charged and ready to go!");

    }
}
```

## 数据结构

### for 循环

1. 初始化计数器
2. 计数器与某个有限值进行比较
3. 每次执行循环，计数器的值都要递增

```java
for (int waterLevel = 0; waterLevel < 7; waterLevel++) {

	System.out.println("The pool's water level is at " + waterLevel + " feet.");

}
```

### 数组
```java
import java.util.ArrayList;

public class Temperatures {
	
  public static void main(String[] args) {

    // create an ArrayList object 
    // 声明一个数组
	ArrayList<Integer> weeklyTemperatures = new ArrayList<Integer>();

	// 在尾部添加数据
    weeklyTemperatures.add(78);
    weeklyTemperatures.add(67);

	// 在指定位置添加数据
    weeklyTemperatures.add(2, 111);

	// 获取数据
    weeklyTemperatures.get(0) 

	// 获取数组的每一个数据
    for (int j = 0; j < weeklyTemperatures.size(); j++) {

      System.out.println( weeklyTemperatures.get(j) );

    }

    // for each 循环，相当于for循环的简写
    // : 可读为 'in'
    for (Integer temperature : weeklyTemperatures) {

      System.out.println(temperature);

    }

  }

}
```

### hashMap

像字典一样，存储键值对

```java
import java.util.HashMap;

public class Restaurant {
  public static void main(String[] args) {

  	// 声明一个HashMap
    HashMap<String, Integer> restaurantMenu = new HashMap<String, Integer>();
    
    // 添加数据
    restaurantMenu.put("Turkey Burger",13);
    restaurantMenu.put("Naan Pizza",11);

	// 获取数据
    System.out.println( restaurantMenu.get("Naan Pizza") );

	// 获取数据的条数
    System.out.println(restaurantMenu.size());


	// 遍历
	// The keySet method of HashMap returns a list of keys.
	for (String item : restaurantMenu.keySet()) {

		System.out.println("A " + item + " costs " + restaurantMenu.get(item) + " dollars.");

	}

  }
}
```

---



