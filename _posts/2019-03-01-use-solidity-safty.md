---
title: '使用 Solidity 开发智能合约的安全建议'
subtitle: '智能合约开发学习笔记(2)'
tags: 区块链
author: June
cover: /assets/img/post/2019-03-01/cover.png
reward: 1
layout: post
date: 2019-03-01
---

# 使用 Solidity 开发智能合约的安全建议

## 关于使用Solidity开发的智能合约安全建议

### 外部调用

* 尽量避免外部调用

* 仔细权衡“`send()`”、“`transfer()`”、以及“`call.value()`”
	* 建议尽可能直接使用 `transfer`
	* 一种被称为 push 和 pull的 机制试图来平衡两者， 在 push 部分使用 `send()` 或 `transfer()`，在pull 部分使用 `call.value()()`。（译者注：在需要对外未知地址转账 Ether时使用 `send()` 或 `transfer()`，已知明确内部无恶意代码的地址转账 Ether使用 `call.value()()` ）

* 处理外部调用错误

	Solidity提供了一系列在raw address上执行操作的底层方法，比如： address.call()，address.callcode()， address.delegatecall()和address.send。这些底层方法不会抛出异常(throw)，只是会在遇到错误时返回false。

	如果你选择使用底层方法，一定要检查返回值来对可能的错误进行处理。

* 不要假设你知道外部调用的控制流程
	无论是使用raw calls 或是contract calls，如果这个ExternalContract是不受信任的都应该假设存在恶意代码。外部调用后避免改变状态

* 对于外部合约优先使用 pull 而不是 push

	外部调用可能会失败。为了最小化这些外部调用失败带来的损失，通常好的做法是将外部调用函数与其余代码隔离，最终是由收款发起方负责发起调用该函数。（这种方法同时也避免了造成 gas limit相关问题。）
	
	```js
	// bad
	contract auction {
	    address highestBidder;
	    uint highestBid;

	    function bid() payable {
	        if (msg.value < highestBid) throw;

	        if (highestBidder != 0) {
	            if (!highestBidder.send(highestBid)) { // if this call consistently fails, no one else can bid
	                throw;
	            }
	        }

	       highestBidder = msg.sender;
	       highestBid = msg.value;
	    }
	}

	// good
	contract auction {
	    address highestBidder;
	    uint highestBid;
	    mapping(address => uint) refunds;

	    function bid() payable external {
	        if (msg.value < highestBid) throw;

	        if (highestBidder != 0) {
	            refunds[highestBidder] += highestBid; // record the refund that this user can claim
	        }

	        highestBidder = msg.sender;
	        highestBid = msg.value;
	    }

	    function withdrawRefund() external {
	        uint refund = refunds[msg.sender];
	        refunds[msg.sender] = 0;
	        if (!msg.sender.send(refund)) {
	            refunds[msg.sender] = refund; // reverting state because send failed
	        }
	    }
	}
	```

* 标记不受信任的合约

	当你自己的函数调用外部合约时，你的变量、方法、合约接口命名应该表明和他们可能是不安全的。

* Don't delegatecall to untrusted code

### 使用`assert()`强制不变性

当断言条件不满足时将触发断言保护。断言保护经常需要和其他技术组合使用，比如当断言被触发时先挂起合约然后升级。（否则将一直触发断言，你将陷入僵局）

### 正确使用 `assert()`,`require()`和`revert()`

`require(condition)` 被用来验证用户的输入，如果条件不满足便会抛出异常，应当使用它验证所有用户的输入。 

`assert(condition)` 在条件不满足也会抛出异常，但是最好只用于固定变量：内部错误或你的智能合约陷入无效的状态。


### 小心整数除法的四舍五入

所有整数除数都会四舍五入到最接近的整数。 如果您需要更高精度，请考虑使用乘数，或存储分子和分母。

### 记住Ether可以被强制发送到账户

谨慎编写用来检查账户余额的不变量。

攻击者可以强制发送wei到任何账户，而且这是不能被阻止的（即使让fallback函数throw也不行）

攻击者可以仅仅使用1 wei来创建一个合约，然后调用selfdestruct(victimAddress)。在victimAddress中没有代码被执行，所以这是不能被阻止的。

### 不要假设合约创建时余额为零

攻击者可以在合约创建之前向合约的地址发送wei。合约不能假设它的初始状态包含的余额为零。

### 记住链上的数据是公开的

当开发一个依赖随机数生成器的应用时，正确的顺序应当是（1）玩家提交行动计划，（2）生成随机数，（3）玩家支付

### 权衡Abstract合约和Interfaces

### 在双方或多方参与的智能合约中，参与者可能会“脱机离线”后不再返回

不要让退款和索赔流程依赖于参与方执行的某个特定动作而没有其他途径来获取资金。

### 使Fallback函数尽量简单

谨慎编写fallback函数以免gas不够用。

### 明确标明函数和状态变量的可见性

明确标明函数和状态变量的可见性。函数可以声明为 external，public， internal 或 private。

* private: 修饰的变量和函数，只能在其所在的合约中调用和访问，即使是其子合约也没有权限访问。
* public: 修饰的变量和函数，任何用户或者合约都能调用和访问。可以在内部调用，也可以通过消息调用。对于公共状态变量，将生成一个自动getter函数。
* internal: 和 private 类似，不过， 如果某个合约继承自其父合约，这个合约即可以访问父合约中定义的“内部”函数。
* external: 与 public 类似，只不过这些函数只能在合约之外调用 - 它们不能被合约内的其他函数调用。接收大型数据数组时，有时效率更高。

### Use modifiers only for assertions

仅在断言使用修饰符。不在方法使用。

使用修饰符代替函数（如isowner（））中的条件检查，否则在函数内部使用require或revert。这使得您的智能合约代码更易于阅读和审计。

### 标明 payable 函数和状态变量

Solidity 从 0.4 开始，每个接受 ether 的方法都必须使用 payable 修饰符。

Declare variables and especially function arguments as `address payable`, if you want to call transfer on them. You can use `.transfer(..)` and `.send(..)` on `address payable`, but not on `address`. 

### 将程序锁定到特定的编译器版本

`pragma solidity 0.4.4;`

### 使用时间监测合约的活动

### 区分函数和事件 (Solidity < 0.4.21)

为了防止函数和事件（Event）产生混淆，命名一个事件使用大写并加入前缀（我们建议LOG）。对于函数， 始终以小写字母开头，构造函数除外。

```js
// bad
event Transfer() {}
function transfer() {}

// good
event LogTransfer() {}
function transfer() external {}
```

### 使用Solidity更新的构造器

更合适的构造器/别名:

selfdestruct（旧版本为'suicide）  
keccak256（旧版本为sha3）。   
`require(msg.sender.send(1 ether))` => `msg.sender.transfer(1 ether)`。

### Be aware that 'Built-ins' can be shadowed

### Avoid using tx.origin 

### The 15-second Rule

### Multiple Inheritance Caution

### Use interface type instead of the address for type safety

### Avoid using extcodesize to check for Externally Owned Accounts

## 安全相关的文件和程序


---

### 参考链接

* [以太坊智能合约 —— 最佳安全开发指南](https://github.com/ConsenSys/smart-contract-best-practices/blob/master/README-zh.md)
* [Ethereum Smart Contract Security Best Practices](https://consensys.github.io/smart-contract-best-practices/)
