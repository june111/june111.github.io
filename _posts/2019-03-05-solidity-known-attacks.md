---
title: '智能合约的已知的攻击'
subtitle: '智能合约开发学习笔记(3)'
tags: 区块链
author: June
cover: /assets/img/post/2019-03-05/cover.png
reward: 1
layout: post
date: 2019-03-05
---

# 智能合约的已知的攻击

## 竞态

调用外部契约的主要危险之一是它们可以接管控制流，并对调用函数意料之外的数据进行更改。 这类bug有多种形式，导致DAO崩溃的两个主要错误都是这种错误。

### 重入 (Reentrancy)

这个版本的bug被注意到是其可以在第一次调用这个函数完成之前被多次重复调用。对这个函数不断的调用可能会造成极大的破坏。

```js
// INSECURE
mapping (address => uint) private userBalances;

function withdrawBalance() public {
    uint amountToWithdraw = userBalances[msg.sender];
    if (!(msg.sender.call.value(amountToWithdraw)())) { throw; } // At this point, the caller's code is executed, and can call withdrawBalance again
    userBalances[msg.sender] = 0;
}
```
在给出来的例子中，最好的方法是 使用 send() 而不是call.value()()。这将避免多余的代码被执行。

然而，如果你没法完全移除外部调用，另一个简单的方法来阻止这个攻击是确保你在完成你所有内部工作之前不要进行外部调用：将userBalances[msg.sender] 清零。

```js
mapping (address => uint) private userBalances;

function withdrawBalance() public {
    uint amountToWithdraw = userBalances[msg.sender];
    userBalances[msg.sender] = 0;
    if (!(msg.sender.call.value(amountToWithdraw)())) { throw; } // The user's balance is already 0, so future invocations won't withdraw anything
}
```

### 跨函数竞态

攻击者也可以使用两个共享状态变量的不同的函数来进行类似攻击。

```js
// INSECURE
mapping (address => uint) private userBalances;

function transfer(address to, uint amount) {
    if (userBalances[msg.sender] >= amount) {
       userBalances[to] += amount;
       userBalances[msg.sender] -= amount;
    }
}

function withdrawBalance() public {
    uint amountToWithdraw = userBalances[msg.sender];
    if (!(msg.sender.call.value(amountToWithdraw)())) { throw; } // At this point, the caller's code is executed, and can call transfer()
    userBalances[msg.sender] = 0;
}
```
着这个例子中，攻击者在他们外部调用withdrawBalance函数时调用transfer()，如果这个时候withdrawBalance还没有执行到userBalances[msg.sender] = 0;这里，那么他们的余额就没有被清零，那么他们就能够调用transfer()转走代币尽管他们其实已经收到了代币。这个弱点也可以被用到对DAO的攻击。

同样的解决办法也会管用，在执行转账操作之前先清零。也要注意在这个例子中所有函数都是在同一个合约内。然而，如果这些合约共享了状态，同样的bug也可以发生在跨合约调用中。

### 竞态解决办法中的陷阱

由于竞态既可以发生在跨函数调用，也可以发生在跨合约调用，任何只是避免重入的解决办法都是不够的。

作为替代，我们建议首先应该**完成所有内部的工作然后再执行外部调用**。这个规则可以避免竞态发生。然而，你不仅应该避免过早调用外部函数而且应该避免调用那些也调用了外部函数的外部函数。

除了修复bug让重入不可能成功，不受信任的函数也已经被标记出来 。同样的情景： untrustedGetFirstWithdrawalBonus() 调用untrustedWithdraw(), 而后者调用了外部合约，因此在这里untrustedGetFirstWithdrawalBonus() 是不安全的。

另一个经常被提及的解决办法是（译者注：像传统多线程编程中一样）**使用mutex。它会"lock" 当前状态，只有锁的当前拥有者能够更改当前状态**。一个简单的例子如下：
```js
// Note: This is a rudimentary example, and mutexes are particularly useful where there is substantial logic and/or shared state
mapping (address => uint) private balances;
bool private lockBalances;

function deposit() payable public returns (bool) {
    if (!lockBalances) {
        lockBalances = true;
        balances[msg.sender] += msg.value;
        lockBalances = false;
        return true;
    }
    throw;
}

function withdraw(uint amount) payable public returns (bool) {
    if (!lockBalances && amount > 0 && balances[msg.sender] >= amount) {
        lockBalances = true;

        if (msg.sender.call(amount)()) { // Normally insecure, but the mutex saves it
          balances[msg.sender] -= amount;
        }

        lockBalances = false;
        return true;
    }

    throw;
}
```
如果用户试图在第一次调用结束前第二次调用 withdraw()，将会被锁住。 这看上去很有效果，但当你使用多个合约互相交互时问题变得严峻了。

攻击者可以只调用getLock()，然后就不再调用 releaseLock()。如果他们真这样做，那么这个合约将会被永久锁住，任何接下来的操作都不会发生了。如果你使用mutexs来避免竞态，那么一定要确保没有地方能够打断锁的进程或绝不释放锁。（这里还有一个潜在的威胁，比如死锁和活锁。在你决定使用锁之前最好大量阅读相关文献（译者注：这是真的，传统的在多线程环境下对锁的使用一直是个容易犯错的地方））

## 交易顺序依赖(TOD) / 前面的先运行

以上是涉及攻击者在单个交易内执行恶意代码产生竞态的示例。接下来演示在区块链本身运作原理导致的竞态：（同一个block内的）交易顺序很容易受到操纵。

由于交易在短暂的时间内会先存放到mempool中，所以在矿工将其打包进block之前，是可以知道会发生什么动作的。这对于一个去中心化的市场来说是麻烦的，因为可以查看到代币的交易信息，并且可以在它被打包进block之前改变交易顺序。避免这一点很困难，因为它归结为具体的合同本身。例如，在市场上，最好实施批量拍卖（这也可以防止高频交易问题）。 另一种使用预提交方案的方法

## 时间戳依赖

请注意，块的时间戳可以由矿工操纵，并且应考虑时间戳的所有直接和间接使用。

## 整数上溢和下溢

涉及到数量的操作都需要考虑上溢和下溢

考虑如下这个简单的转账操作：
```js
mapping (address => uint256) public balanceOf;

// INSECURE
function transfer(address _to, uint256 _value) {
    /* Check if sender has balance */
    if (balanceOf[msg.sender] < _value)
        throw;
    /* Add and subtract new balances */
    balanceOf[msg.sender] -= _value;
    balanceOf[_to] += _value;
}

// SECURE
function transfer(address _to, uint256 _value) {
    /* Check if sender has balance and for overflows */
    if (balanceOf[msg.sender] < _value || balanceOf[_to] + _value < balanceOf[_to])
        throw;

    /* Add and subtract new balances */
    balanceOf[msg.sender] -= _value;
    balanceOf[_to] += _value;
}
```

## 通过 (Unexpected) revert 发动 DoS

**解决办法：涉及到支付时，优先使用 pull 而不是 push**

## 通过区块 Gas Limit 发动 DoS

一次性向所有人转账，很可能会导致达到以太坊区块gas limit的上限。以太坊规定了每一个区块所能花费的gas limit，如果超过你的交易便会失败。

如果你实在必须通过遍历一个变长数组来进行转账，最好估计完成它们大概需要多少个区块以及多少笔交易。然后你还必须能够追踪得到当前进行到哪以便当操作失败时从那里开始恢复，举个例子：
```js
struct Payee {
    address addr;
    uint256 value;
}
Payee payees[];
uint256 nextPayeeIndex;

function payOut() {
    uint256 i = nextPayeeIndex;
    while (i < payees.length && msg.gas > 200000) {
      payees[i].addr.send(payees[i].value);
      i++;
    }
    nextPayeeIndex = i;
}
```
如上所示，你必须确保在下一次执行payOut()之前另一些正在执行的交易不会发生任何错误。如果必须，请使用上面这种方式来处理。

## 其他漏洞

更多漏洞可到 [Smart Contract Weakness Classification and Test Cases](https://smartcontractsecurity.github.io/SWC-registry/) 进行学习

---

### 参考链接

* [以太坊智能合约 —— 最佳安全开发指南](https://github.com/ConsenSys/smart-contract-best-practices/blob/master/README-zh.md)
* [Ethereum Smart Contract Security Best Practices](https://consensys.github.io/smart-contract-best-practices/)
