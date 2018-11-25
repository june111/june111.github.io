---
layout: post
title: '面向对象编程思想(OOP) && JavaScript'
date: 2018-11-05
author: June
cover: 'https://june111.github.io/assets/img/post/2018-11-05/oop.png'
tags: 前端
---

# 面向对象编程思想(OOP) && JavaScript

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-11-05/structure.svg">
![文章结构]({{site.baseurl}}/assets/img/post/2018-11-05/structure.svg)
</a>

## 为什么要理解面向对象编程思想?

为了解决软件开发中的疑难问题，例如代码的维护，需求的变更，人员的流动等，我们需要编写（设计）具有很好的可读性、可维护性和可扩展性的代码。而且需要保证代码具有高内聚低耦合。

下面将简单介绍面向对象的一些基本特性、设计原则，以及设计模式关系。

## 面向对象

### 什么是面向对象

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-11-05/what-is-oop.png">
![生动描述面向对象概念]({{site.baseurl}}/assets/img/post/2018-11-05/what-is-oop.png)
</a>

先上一张图，可以对面向对象有一个大致的了解，那什么是面向对象呢，用java中的一句经典语句来说就是：万事万物皆对象。面向对象的思想主要是以对象为主，将一个问题抽象出具体的对象，并且将抽象出来的对象和对象的属性和方法封装成一个类。

>面向对象是把构成问题事务分解成各个对象，建立对象的目的不是为了完成一个步骤，而是为了描叙某个事物在整个解决问题的步骤中的行为。

### 面向对象和面向过程的区别

知乎上的这个例子挺形象。

>面向对象： 狗.吃(屎)  
>面向过程： 吃.(狗,屎)

分别用这两种思想解决最经典的“把大象放冰箱”的问题：

面向过程的解决方法

1. 开门（冰箱）；
2. 装进（冰箱，大象）；
3. 关门（冰箱）。

面向对象的解决方法

1. 冰箱.开门（）
2. 冰箱.装进（大象）
3. 冰箱.关门（）

可以看出来面向对象和面向过程的侧重点是不同的，面向过程是以动词为主，完成一个事件就是将不同的动作函数按顺序调用。面向对象是以主谓为主。将主谓看成一个一个的对象，然后对象有自己的属性和方法。

|  |面向过程|面向对象|
|:----|:----|:---- |
|关注|关注的是解决问题的步骤|关注的是解决问题所需要的对象(内容、角色),然后根据业务逻辑按一定的规则调用这些对象的相关功能、方法|
|优点|在小型程序中代码量比较少,开发成本低|有弥补了面向过程编程思想的不足|
|缺点|在构建大型项目是,代码逻辑不易捋顺、代码量大、代码编写繁琐,增加开发难度|在小型程序中不如面向过程思想灵活、方便|

### 四大基本特性

* 抽象：提取现实世界中某事物的关键特性，为该事物构建模型的过程。对同一事物在不同的需求下，需要提取的特性可能不一样。得到的抽象模型中一般包含：属性（数据）和操作（行为）。这个抽象模型我们称之为类。对类进行实例化得到对象。

* 封装：封装可以使类具有独立性和隔离性；保证类的高内聚。只暴露给类外部或者子类必须的属性和操作。类封装的实现依赖类的修饰符（public、protected和private等）

* 继承：对现有类的一种复用机制。一个类如果继承现有的类，则这个类将拥有被继承类的所有非私有特性（属性和操作）。这里指的继承包含：类的继承和接口的实现。

* 多态：多态是在继承的基础上实现的。多态的三个要素：继承、重写和父类引用指向子类对象。父类引用指向不同的子类对象时，调用相同的方法，呈现出不同的行为；就是类多态特性。多态可以分成编译时多态和运行时多态。

抽象、封装、继承和多态是面向对象的基础。在面向对象四大基础特性之上，我们在做面向对象编程设计时还需要遵循有一些基本的设计原则。

### 七大设计原则

* SOLID原则（单一职责原则、开放关闭原则、里氏替换原则、接口隔离原则和依赖倒置原则）
* 迪米特法则
* 组合优于继承原则（合成复用原则）

在遵循这些面向对象设计原则基础上，前辈们总结出一些解决不同问题场景的设计模式，以四人帮的gof23最为知名。

### 24种设计模式 (gof23+1)

* 创建型模式：
	* 简单工厂模式（不包含在gof23中）
	* 工厂模式
	* 抽象工厂模式
	* 单例模式
	* 原型模式
	* 创建者模式

* 结构型模式：
	* 组合模式
	* 装饰者模式
	* 外观模式
	* 适配器模式
	* 代理模式
	* 享元模式
	* 桥接模式

* 行为型模式：
	* 观察者模式
	* 策略模式
	* 状态模式
	* 中介模式
	* 模板方法
	* 命令模式
	* 备忘录模式
	* 访问者模式
	* 解释器模式
	* 迭代器模式
	* 职责链模式


## 在JS中用面向对象思想编程

### 封装

在ES6之前，我们可以用原始模式、构造函数模式、Prototype模式来生成实例对象。ES6引入了 Class（类）这个概念，作为对象的模板。通过class关键字，可以定义类。

```js
//定义类
class Point {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }

  toString() {
    return '(' + this.x + ', ' + this.y + ')';
  }
}
```

上面代码定义了一个“类”，可以看到里面有一个constructor方法，这就是构造方法，而this关键字则代表实例对象。

使用的时候，也是直接对类使用new命令，跟构造函数的用法完全一致。

```js
class Bar {
  doStuff() {
    console.log('stuff');
  }
}

var b = new Bar();
b.doStuff() // "stuff"

class Person {
  constructor (name, age) { // 直接写属性
    this.name = name
    this.age = age
  }
  showName () { // 直接可以写方法
    return this.name
  }
  showAge () {
    return this.age
  }
}

// var xiaoming=new Person('小明','16');

```


构造函数的prototype属性，在 ES6 的“类”上面继续存在。事实上，类的所有方法都定义在类的prototype属性上面。

```js
class Point {
  constructor() {
    // ...
  }

  toString() {
    // ...
  }

  toValue() {
    // ...
  }
}

// 等同于

Point.prototype = {
  constructor() {},
  toString() {},
  toValue() {},
};
```

由于类的方法都定义在prototype对象上面，所以类的新方法可以添加在prototype对象上面。Object.assign方法可以很方便地一次向类添加多个方法。

constructor方法是类的默认方法，通过new命令生成对象实例时，自动调用该方法。一个类必须有constructor方法，如果没有显式定义，一个空的constructor方法会被默认添加。

```js
class Point {
  constructor(){
    // ...
  }
}

Object.assign(Point.prototype, {
  toString(){},
  toValue(){}
});
```

另外，类的内部所有定义的方法，都是不可枚举的（non-enumerable）。

注意，定义“类”的方法的时候，前面不需要加上function这个关键字，直接把函数定义放进去了就可以了。另外，方法之间不需要逗号分隔，加了会报错。类必须使用new调用，否则会报错。这是它跟普通构造函数的一个主要区别，后者不用new也可以执行。

关于私有方法和私有属性的问题，介绍一个我觉得比较简单明了的方法：

利用Symbol值的唯一性，将私有方法的名字命名为一个Symbol值。

```js
const bar = Symbol('bar');
const snaf = Symbol('snaf');

export default class myClass{

  // 公有方法
  foo(baz) {
    this[bar](baz);
  }

  // 私有方法
  [bar](baz) {
    return this[snaf] = baz;
  }

  // ...
};
```

上面代码中，bar和snaf都是Symbol值，导致第三方无法获取到它们，因此达到了私有方法和私有属性的效果。

this的指向问题，我觉得使用箭头函数可以比较好得解决。

```js
class Logger {
  constructor() {
    this.printName = (name = 'there') => {
      this.print(`Hello ${name}`);
    };
  }

  // ...
}
```

### 继承

>继承：子类可以使用父类的所有功能，并且对这些功能进行扩展。继承的过程，就是从一般到特殊的过程。

其实继承都是基于封装特性来实现的。

在ES6之前，继承需要考虑原型继承的中间对象，原型对象的构造函数等等。阮一峰把继承分为构造函数的继承和非构造函数的继承，写了8种"继承"的方法。

现在只要用`class`定义对象，用`extends`就可以实现继承。

#### extends

```js
class Point {
}

class ColorPoint extends Point {
}
```
上面代码定义了一个ColorPoint类，该类通过extends关键字，继承了Point类的所有属性和方法。

```js
class ColorPoint extends Point {
  constructor(x, y, color) {
    super(x, y); // 调用父类的constructor(x, y)
    this.color = color;
  }

  toString() {
    return this.color + ' ' + super.toString(); // 调用父类的toString()
  }
}
```
上面代码中，constructor方法和toString方法之中，都出现了super关键字，它在这里表示父类的构造函数，用来新建父类的this对象。

子类必须在constructor方法中调用super方法，否则新建实例时会报错。这是因为子类自己的this对象，必须先通过父类的构造函数完成塑造，得到与父类同样的实例属性和方法，然后再对其进行加工，加上子类自己的实例属性和方法。如果不调用super方法，子类就得不到this对象。

需要注意的地方是，在子类的构造函数中，只有调用super之后，才可以使用this关键字，否则会报错。这是因为子类实例的构建，基于父类实例，只有super方法才能调用父类实例。

```js
class Point {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }
}

class ColorPoint extends Point {
  constructor(x, y, color) {
    this.color = color; // ReferenceError
    super(x, y);
    this.color = color; // 正确
  }
}
```

上面代码中，子类的constructor方法没有调用super之前，就使用this关键字，结果报错，而放在super方法之后就是正确的。

#### Object.getPrototypeOf

`Object.getPrototypeOf` 方法可以用来从子类上获取父类。

```js
Object.getPrototypeOf(ColorPoint) === Point
// true
```

#### 类的-prototype-属性和__proto__属性

大多数浏览器的 ES5 实现之中，每一个对象都有__proto__属性，指向对应的构造函数的prototype属性。Class 作为构造函数的语法糖，同时有prototype属性和__proto__属性，因此同时存在两条继承链。

（1）子类的__proto__属性，表示构造函数的继承，总是指向父类。

（2）子类prototype属性的__proto__属性，表示方法的继承，总是指向父类的prototype属性。

```js
class A {
}

class B extends A {
}

B.__proto__ === A // true
B.prototype.__proto__ === A.prototype // true
```

上面代码中，子类B的__proto__属性指向父类A，子类B的prototype属性的__proto__属性指向父类A的prototype属性。

这两条继承链，可以这样理解：作为一个对象，子类（B）的原型（`__proto__`属性）是父类（A）；作为一个构造函数，子类（B）的原型对象（prototype属性）是父类的原型对象（prototype属性）的实例。

```js
Object.create(A.prototype);
// 等同于
B.prototype.__proto__ = A.prototype;
```

#### Mixin-模式的实现

Mixin 指的是多个对象合成一个新的对象，新对象具有各个组成成员的接口。它的最简单实现如下。

```js
const a = {
  a: 'a'
};
const b = {
  b: 'b'
};
const c = {...a, ...b}; // {a: 'a', b: 'b'}
```

上面代码中，c对象是a对象和b对象的合成，具有两者的接口。

下面是一个更完备的实现，将多个类的接口“混入”（mix in）另一个类。

```js
function mix(...mixins) {
  class Mix {}

  for (let mixin of mixins) {
    copyProperties(Mix.prototype, mixin); // 拷贝实例属性
    copyProperties(Mix.prototype, Reflect.getPrototypeOf(mixin)); // 拷贝原型属性
  }

  return Mix;
}

function copyProperties(target, source) {
  for (let key of Reflect.ownKeys(source)) {
    if ( key !== "constructor"
      && key !== "prototype"
      && key !== "name"
    ) {
      let desc = Object.getOwnPropertyDescriptor(source, key);
      Object.defineProperty(target, key, desc);
    }
  }
}
```

上面代码的mix函数，可以将多个对象合成为一个类。使用的时候，只要继承这个类即可。

```js
class DistributedEdit extends mix(Loggable, Serializable) {
  // ...
}
```


---

觉得文章不错就扫码支持一下呗～

![打赏二维码](https://june111.github.io/assets/img/post/pay-qr.jpg)

参考链接

* [面向对象编程思想（OOP）](https://www.cnblogs.com/xiaosongluffy/p/5072501.html)
* [js:面向对象编程，带你认识封装、继承和多态](https://juejin.im/post/59396c96fe88c2006afc2707)
* [Javascript 面向对象编程（一）：封装](http://www.ruanyifeng.com/blog/2010/05/object-oriented_javascript_encapsulation.html)
* [Javascript面向对象编程（二）：构造函数的继承](http://www.ruanyifeng.com/blog/2010/05/object-oriented_javascript_inheritance.html)
* [Javascript面向对象编程（三）：非构造函数的继承](http://www.ruanyifeng.com/blog/2010/05/object-oriented_javascript_inheritance_continued.html)
* [Class 的基本语法](http://es6.ruanyifeng.com/?search=foreach&x=0&y=0#docs/class)
* [Class 的继承](http://es6.ruanyifeng.com/#docs/class-extends)
* [JS面向对象、继承、ES6中class类](https://www.jianshu.com/p/c384034837cf)
* [MDN JS class](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Classes)
