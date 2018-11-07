# Solidity

## 智能合约的介绍

### 一个简单的智能合约

#### Storage 存储

    pragma solidity ^0.4.0;
    contract SimpleStorage {
        uint storedData;
        function set(uint x) public {
            storedData = x;
        }
        function get() public view returns (uint) {
            return storedData;
        }
    }

第一行简单地告诉源代码是用的是Solidity版本0.4.0或任何不破坏功能的更新版本（最高版本，但不包括版本0.5.0）。 这是为了确保合约不会突然与新的编译器版本表现不同。 关键字 `pragma`以这种方式调用，编译指示是用来指导编译器如何处理源代码的指令。

合约在Solidity中是代码（其功能）和数据（其状态）的集合，它位于以太坊区块链的特定地址。 `uint storedData`, 声明了一个名为`storedData`的状态变量，类型为`uint`（256位无符号整数）。 您可以将其视为数据库中的单个插槽，可以通过调用管理数据库的代码的函数来查询和更改它。 在这种情况下，函数`set`和`get`可用于修改或检索变量的值。

要访问状态变量，您不需要前缀 `this`。 

这个合约还没有发挥多大的作用（由于以太坊建立的基础设施），除了允许所有人存储任何人都可以访问的单个数字，而没有（可行的）方法来阻止您发布此数字。 当然，任何人都可以使用不同的值再次调用`set`并覆盖您的数字，但该数字仍会存储在区块链的历史记录中。 稍后，我们将看到您如何施加访问限制，以便只有您可以更改数量。

注意
所有标识符（合约名称，函数名称和变量名称）都限制为ASCII字符集。 可以将UTF-8编码数据存储在字符串变量中。

警告
小心使用Unicode文本，因为类似的（或甚至相同的）字符可以有不同的代码点，因此将被编码为不同的字节数组。

#### Subcurrency Example 子货币示例

以下合约将实现最简单的加密货币形式。 可以凭空创造币，但只有创建合约的人才能做到这一点（实施不同的发行方案是微不足道的）。 此外，任何人都可以向对方发币而无需使用用户名和密码进行注册 - 您只需要一个以太坊密钥对。

    pragma solidity ^0.4.21;

    contract Coin {
        // 关键字“public”使这些变量可以从外部读取。
        address public minter;
        mapping (address => uint) public balances;

        // Events事件允许轻客户端有效地对更改做出反应。
        event Sent(address from, address to, uint amount);

        // 这是构造函数，其代码仅在创建合约时运行。
        function Coin() public {
            minter = msg.sender;
        }

        function mint(address receiver, uint amount) public {
            if (msg.sender != minter) return;
            balances[receiver] += amount;
        }

        function send(address receiver, uint amount) public {
            if (balances[msg.sender] < amount) return;
            balances[msg.sender] -= amount;
            balances[receiver] += amount;
            emit Sent(msg.sender, receiver, amount);
        }
    }

本合约介绍了一些新概念，让我们逐一介绍。

`address public minter;` 声明可公开访问的类型为`address`的状态变量。 地址类型是160位值，不允许任何算术运算。 它适用于存储属于外部人员的合约或密钥对的地址。 关键字`public`会自动生成一个函数，允许您从合约外部访问状态变量的当前值。 没有此关键字，其他合约无法访问该变量。 编译器生成的函数代码大致等同于以下内容：

    function minter() returns (address) { return minter; }

添加一个完全相同的函数是行不通的，因为我们会有一个函数和一个具有相同名称的状态变量

下一行，`mapping (address => uint) public balances;`也会创建一个公共状态变量，但它是一种更复杂的数据类型。这个类型把地址映射为无符号整数。 映射可以看作是哈希表，它们被虚拟地初始化，使得每个可能的密钥都存在并被映射到其字节表示全为零的值。 但是，这种类比并不过分，因为既不可能获得映射的所有键列表，也不可能获得所有值的列表。 因此，要么记住（或者保留列表或使用更高级的数据类型）您添加到映射中的内容，或者在不需要这样的上下文中使用它，就像这样。 在这种情况下，`public`关键字创建的getter函数有点复杂。 它大致如下所示：

    function balances(address _account) public view returns (uint) {
        return balances[_account];
    }

如您所见，您可以使用此功能轻松查询单个帐户的余额。

`event Sent(address from, address to, uint amount); `声明一个所谓的“事件”，它在函数`send`的最后一行发出。 用户界面（当然还有服务器应用程序）可以在没有太多成本的情况下监听区块链上发出的事件。 一旦发出，侦听器也将接收来自，`from, to, amount` 的参数，这使得追踪交易变得容易。 为了听取这个事件，你会使用

    Coin.Sent().watch({}, '', function(error, result) {
        if (!error) {
            console.log("Coin transfer: " + result.args.amount +
                " coins were sent from " + result.args.from +
                " to " + result.args.to + ".");
            console.log("Balances now:\n" +
                "Sender: " + Coin.balances.call(result.args.from) +
                "Receiver: " + Coin.balances.call(result.args.to));
        }
    })

请注意函数balances如何从用户界面自动调用

特殊函数`Coin`是在创建合约期间运行的构造函数，之后不能调用。 它永久存储创建合约的人的地址：`msg`（与`tx`和`block`一起）是一个神奇的全局变量，包含一些允许访问区块链的属性。 `msg.sender`始终是当前（外部）函数调用的来源地址。

最后，实际上以合约结束并且可以被用户和合约调用的功能都是`mint` and `send` 。如果`mint`被非合约创建者调用，不会发生任何事情。 另一方面，`send`可以被任何人使用（已经有一些币的人），去发币给其他人。 请注意，如果您使用此合约将币发送到地址，当您在区块链资源管理器中查看该地址时，您将看不到任何内容，因为您发币和更改余额的事实仅存储在此数据存储中 尤其是币的合约。 通过使用事件`events`，创建一个能够追踪你的新币种的交易和余额的“区块链资源管理器”是相对容易的。

### 区块链基础

区块链作为一个概念对程序员来说并不难理解。 原因是大多数复杂性（挖矿，哈希，椭圆曲线加密，点对点网络等）只是提供一系列功能和承诺。 一旦您接受了给定的这些功能，您就不必担心底层技术 - 或者您是否必须知道Amazon的AWS如何在内部运行才能使用它？

#### Transactions 交易

区块链是一个全球共享的交易数据库。 这意味着每个人都可以通过参与网络来读取数据库中的条目。 如果要更改数据库中的某些内容，则要创建一个必须被其他所有人接受的交易。 交易，意味着您要进行的更改（假设您想要同时更改两个值）要么根本没有完成，要么完全应用。 此外，当您的交易应用于数据库时，没有其他交易可以更改它。

例如，假设一个表格列出了电子货币中所有账户的余额。 如果请求从一个帐户转移到另一个帐户，则数据库的交易性质确保如果从一个帐户中减去该金额，则始终将其添加到另一个帐户。 如果由于某种原因，无法将金额添加到目标帐户，则不会修改源帐户。

此外，交易总是由发送者（创建者）以加密方式签名。 这可以直接保护对数据库特定修改的访问。 在电子货币的示例中，简单的检查确保只有持有账户密钥的人才能从中转账。

#### Blocks 区块

一个要克服的主要障碍是，“双花攻击”：如果网络中存在两个想要清算账户的交易，即所谓的冲突，会发生什么？

对此的抽象答案是您不必关心。 交易的顺序会为您排好。交易将打包到“块”中，然后它们将在所有参与的节点中执行和分发。 如果两个交易相互矛盾，那么最终成为第二个的交易将被拒绝并且不会成为该块的一部分。

这些块在时间上形成线性序列，这是“区块链”一词源自的地方。 块以相对规则的间隔添加到链中 - 对于以太坊，大约每17秒完成一次打包。

作为“订单选择机制”（称为“挖矿”）的一部分，可能会发生块不时被回滚，但这仅发生在链的“尖端”处。 顶部添加的块越多，它就越不可能回滚。 因此，您的交易可能会被还原甚至从区块链中删除，但等待的时间越长，它的可能性就越小。

### 以太坊虚拟机

#### 概述

以太坊虚拟机或EVM是以太坊中智能合约的运行环境。 它不仅是沙箱，而且实际上是完全隔离的，这意味着在EVM内部运行的代码无法访问网络，文件系统或其他进程。 智能合约甚至可以限制对其他智能合约的访问。

#### Accounts 帐号

以太坊中有两类账户，它们共用同一个地址空间。外部账户，该类账户被公钥-私钥对控制。合约账户，该类账户被存储在账户中的代码控制。外部账户的地址是由公钥决定的，合约账户的地址是在创建合约时由合约创建者的地址和该地址发出过的交易数量（即所谓的“随机数nonce”）计算得到。

无论帐户是否存储代码，EVM都会平等对待这两种类型。

每个帐户都有一个的键值对存储，将256位字映射到256位字，称为存储。

此外，每个帐户在以太币中都有余额（准确地说是“Wei”），可以通过发送包含以太币的交易来修改。

#### 交易

交易是从一个帐户发送到另一个帐户的消息（可能是相同的或特殊的零帐户，见下文）。 它可以包括二进制数据（其有效载荷）和以太币。

如果目标帐户包含代码，则执行该代码并将有效负载作为输入数据提供。

如果目标帐户是零帐户（地址为0的帐户），则交易会创建一个新的合约。 如前所述，该合约的地址不是零地址，而是从发送方及其发送的交易数量（“nonce”）得出的地址。 合约创建交易的有效载荷被认为是EVM字节码并被执行。 此执行的输出将永久存储为合约代码。 这意味着，为了创建合约，您不会发送合约的实际代码，而是实际上在执行时返回该代码的代码。

注意
在创建合约时，其代码仍为空。 因此，在构造函数执行完毕之前，不应回调构造中的合约。

#### 手续费Gas

在创建时，每笔交易都收取一定数量的手续费，其目的是限制执行交易所需的工作量并支付执行费用。 当EVM执行交易时，根据特定规则逐渐耗尽手续费。

手续费价格是交易创建者设定的价值，他必须从发送账户预先支付`gas_price * gas`。 如果在执行后留下一些手续费，它将以相同的方式退还。

无论执行到什么位置，一旦Gas被耗尽就会触发一个out-of-gas异常。同时，当前调用帧所做的所有状态修改都将被回滚。

#### 存储，内存和堆栈

每个账户都有一块永久的内存区域，被称为存储，其形式为key-value，key和value的长度均为256位。在合约里，不能遍历账户的存储。相对于主存和栈，存储的读操作开销较大，修改存储甚至更多。一个合约只能对它自己的存储进行读写。

第二个内存区被称为主存。合约执行每次消息调用时都有一块新的被清除过的主存。主存可以按字节寻址，但是读写的最小单位为32字节。操作主存的开销随着主存的增长而变大。

EVM不是基于寄存器的，而是基于栈的虚拟机。因此所有的计算都在一个称为栈的区域内执行。栈最大有1024个元素，每个元素有256位。对栈的访问只限于其顶端，允许复制最顶端的16个元素中的一个到栈顶，或者是交换栈顶元素和下面16个元素中的一个。所有其他操作都只能取最顶的一个或几个元素，并把结果压在栈顶。当然可以把栈里的元素放到存储或者主存中。但是无法只访问栈里指定深度的那个元素，在那之前必须把指定深度之上的所有元素都从栈中移除才行。

#### 指令集

EVM的指令集被刻意保持在最小规模，以尽可能避免可能导致共识问题的错误。所有的指令都是针对256位这个基本的数据单位进行的操作，具备常用的算术、位、逻辑和比较操作，也可以进行条件和无条件跳转。此外，合约可以访问当前区块的相关属性，比如它的编号和时间戳。

#### 消息调用

合约可以通过消息调用的方式来调用其他合约，或者发送以太币到非合约账户。消息调用和交易非常类似，它们都有一个源，一个目标，数据负载，以太币，Gas和返回数据。事实上每个交易都可以被认为是一个顶层消息调用，这个消息调用会依次产生更多的消息调用。

一个合约可以决定剩余Gas的分配。比如内部消息调用时使用多少Gas，或者期望保留多少Gas。如果在内部消息调用时发生了out-of-gas异常或者其他异常，合约将会得到通知，一个错误码被压入栈中。这种情况只是内部消息调用的Gas耗尽。在solidity中，这种情况下发起调用的合约默认会触发一个人工异常，这个异常会打印出调用栈。

就像之前说过的，被调用的合约（发起调用的合约也一样）会拥有崭新的主存，并能够访问调用的负载。调用负载被存储在一个单独的被称为calldata的区域。调用执行结束后，返回数据将被存放在调用方预先分配好的一块内存中。调用层数被限制为1024。因此对于更加复杂的操作，我们应该使用循环而不是递归。

#### 代码调用和库

以太坊中存在一种特殊类型的消息调用，被称为callcode。它跟消息调用几乎完全一样，只是加载来自目标地址的代码将在发起调用的合约上下文中运行。这意味着一个合约可以在运行时从另外一个地址动态加载代码。存储，当前地址和余额都指向发起调用的合约，只有代码是从被调用地址获取的。这使得Solidity可以实现“库”。可复用的库代码可以应用在一个合约的存储上，可以用来实现复杂的数据结构，从而使智能合约更加的强大。

#### Logs 日志

可以将数据存储在特殊索引的数据结构中，该数据结构一直映射到块级别。 此功能称为日志，Solidity使用日志来实现事件events。 合约在创建后无法访问日志数据，但可以从区块链外部有效地访问它们。 由于日志数据的某些部分存储在bloom过滤器中，因此可以以高效且加密的方式搜索此数据，因此不下载整个区块链（“轻客户端”）仍然可以找到这些日志。

#### 创建

合约甚至可以使用特殊操作码创建其他合约（即，它们不会简单地调用零地址）。 这些创建调用和普通消息调用之间的唯一区别是执行有效负载数据，结果存储为代码，调用者/创建者接收堆栈上新合约的地址。

#### 自毁

代码从区块链中删除的唯一可能性是当该地址的合约执行`selfdestruct`操作时。 存储在该地址的剩余以太币将发送到指定目标，然后从该状态中删除存储和代码。

警告

即使合约的代码不包含对`selfdestruct`的调用，它仍然可以使用`delegatecall`或`callcode`执行该操作。

注意

旧合约的修改或许不会由以太坊客户端实施。 此外，归档节点可以选择无限期地保留合约存储和代码。

注意

目前无法从状态中删除外部帐户。

<!-- ## 安装Solidity编译器 todo

### Versioning

### Remix

### npm / Node.js

### Docker

### Binary Packages

### Building from Source
#### Clone the Repository
#### Prerequisites - macOS
#### Prerequisites - Windows
#### External Dependencies
#### Command-Line Build

### CMake options

### The version string in detail

### Important information about versioning -->

## 深入了解Solidity

### Solidity源文件的布局

源文件可以包含任意数量的合约定义，包括指令和pragma指令。

#### Pragmas
`pragma`关键字可用于启用某些编译器功能或检查。 pragma指令始终是源文件的本地指令，因此如果要在所有项目中启用它，则必须将pragma添加到所有文件中。 如果导入另一个文件，该文件中的pragma将不会自动应用于导入文件。 

##### Pragma 的版本
todo

#### 导入其他源文件

##### 语法和语义
Solidity支持与JavaScript中可用的导入语句非常相似的语句（来自ES6），尽管Solidity不知道“默认导出”的概念。

在全局级别，您可以使用以下形式的import语句：

    import "filename";

此语句将所有全局符号从“filename”（以及在那里导入的符号）导入当前全局范围（与ES6不同，但向后兼容Solidity）。 建议不要使用这种简单的方式，因为它会以不可预测的方式污染命名空间：如果在“filename”中添加新的顶级项，它们将自动出现在所有从“filename”导入的文件中。 最好明确导入特定符号。

以下示例创建一个新的全局符号`symbolName`，其成员是`“filename”`中的所有全局符号。

    import * as symbolName from "filename";

如果存在命名冲突，您还可以在导入时重命名符号。 此代码创建新的全局符号别名和symbol2，它们分别从“filename”中引用symbol1和symbol2。

    import {symbol1 as alias, symbol2} from "filename";

另一种语法不是ES6的一部分，但可能很方便：

    import "filename" as symbolName;

这相当于`import * as symbolName from "filename"; `。

##### 路径
引入文件路径时要注意，非.打头的路径会被认为是绝对路径，所以要引用同目录下的文件使用

    import “./x” as x

也不要使用下述方式，这样会是在一个全局的目录下

    import “x” as x;

为什么会有这个区别，是因为这取决于编译器，如果解析路径，通常来说目录层级结构并不与我们本地的文件一一对应，它非常有可能是通过ipfs,http，或git建立的一个网络上的虚拟目录。

注意
始终使用导入“./filename.sol”之类的相对导入; 并避免在路径说明符中使用.. 在后一种情况下，最好使用全局路径并设置重映射，如下所述。

#####在实际编译器中使用
调用编译器时，您可以指定如何发现路径的第一个元素以及路径前缀重映射。 例如，您可以设置重映射，以便从您的本地目录/ usr / local / dapp-bin / library中实际读取从虚拟目录github.com/ethereum/dapp-bin/library导入的所有内容。 如果应用多个重映射，则首先尝试具有最长密钥的那个。 不允许使用空前缀。 重映射可以取决于上下文，允许您配置要导入的包，例如，同名库的不同版本。

各编译器提供了文件前缀映射机制。

可以将一个域名下的文件映射到本地，从而从本地的某个文件中读取
提供对同一实现的不同版本的支持（可能某版本的实现前后不兼容，需要区分）
如果前缀相同，取最长，
有一个”fallback-remapping”机制，空串会映射到“/usr/local/include/solidify”

solc编译器

命令行编译器，通过下述命令命名空间映射提供支持

    context:prefix=target

上述的context:和=target是可选的。所有context目录下的以prefix开头的会被替换为target。
举例来说，如果你将github.com/ethereum/dapp-bin拷到本地的/usr/local/dapp-bin，并使用下述方式使用文件

    import “github.com/ethereum/dapp-bin/library/iterable_mapping.sol” as it_mapping;

要编译这个文件，使用下述命令：

    solc github.com/ethereum/dapp-bin=/usr/local/dapp-bin source.sol

另一个更复杂的例子，如果你使用一个更旧版本的dapp-bin，旧版本在/url/local/dapp-bin_old，那么，你可以使用下述命令编译

    solc module1:github.com/ethereum/dapp-bin=/usr/local/dapp-bin  \
            modeule2:github.com/ethereum/dapp-bin=/usr/local/dapp-bin_old \
            source.sol

需要注意的是solc仅仅允许包含实际存在的文件。它必须存在于你重映射后目录里，或其子目录里。如果你想包含直接的绝对路径包含，那么可以将命名空间重映射为=\
备注：如果有多个重映射指向了同一个文件，那么取最长的那个文件。

Remix编译器:

Remix编译器默认会自动映射到github上，然后会自动从网络上检索文件。例如：你可以通过下述方式引入一个迭代包：

    import “github.com/ethereum/dapp-bin/library/iterable_mapping.sol” as it_mapping

备注：未来可能会支持其它的源码方式

#### 注释
todo

### 合约的结构

* 合约类似面向对象语言中的类。
* 支持继承

每个合约中可包含状态变量(State Variables)，函数(Functions),函数修饰符（Function Modifiers）,事件（Events）,结构类型(Structs Types)和枚举类型(Enum Types)。

#### State Variables 状态变量

变量值会永久存储在合约的存储空间

    pragma solidity >=0.4.0 <0.6.0;
    contract SimpleStorage {
        uint storedData; // State variable
        // ...
    }

详情见类型（Types）章节，关于所有支持的类型和变量相关的可见性（Visibility and Accessors）。

#### Functions 函数

智能合约中的一个可执行单元。

    pragma solidity >=0.4.0 <0.6.0;
    contract SimpleAuction {
        function bid() public payable { // Function
            // ...
        }
    }

函数调用可以设置为内部（Internal）的和外部（External）的。同时对于其它合同的不同级别的可见性和访问控制(Visibility and Accessors)。

#### Function Modifiers 函数修饰符

函数修饰符用于增强语义。

    pragma solidity >=0.4.22 <0.6.0;
    contract Purchase {
        address public seller;
        modifier onlySeller() { // Modifier
            require(
                msg.sender == seller,
                "Only seller can call this."
            );
            _;
        }
        function abort() public view onlySeller { // Modifier usage
            // ...
        }
    }

#### Events 事件

事件是以太坊虚拟机(EVM)日志基础设施提供的一个便利接口。用于获取当前发生的事件。

    pragma solidity >=0.4.21 <0.6.0;
    contract SimpleAuction {
        event HighestBidIncreased(address bidder, uint amount); // Event
        function bid() public payable {
            // ...
            emit HighestBidIncreased(msg.sender, msg.value); // Triggering event
        }
    }

关于事件如何声明和使用，详见后面事件相关章节。

#### Struct Types 结构类型

自定义的将几个变量组合在一起形成的类型。详见关于结构体相关章节。

    pragma solidity >=0.4.0 <0.6.0;

    contract Ballot {
        struct Voter { // Struct
            uint weight;
            bool voted;
            address delegate;
            uint vote;
        }
    }

#### Enum Types 枚举类型

特殊的自定义类型，类型的所有值可枚举的情况。详情见后续相关章节。

    pragma solidity >=0.4.0 <0.6.0;

    contract Purchase {
        enum State { Created, Locked, Inactive } // Enum
    }

### Types

由于Solidity是一个静态类型的语言，所以编译时需明确指定变量的类型（包括本地变量或状态变量），Solidity编程语言提供了一些基本类型(elementary types)可以用来组合成复杂类型。

类型可以与不同运算符组合，支持表达式运算，你可以通过表达式的执行顺序(Order of Evaluation of Expressions)来了解执行顺序。

#### Value Types

值类型包含

* 布尔(Booleans)
* 整型(Integer)
* 地址(Address)
* 定长字节数组(fixed byte arrays)
* 有理数和整型(Rational and Integer Literals，String literals)
* 枚举类型(Enums)
* 函数(Function Types)

为什么会叫值类型，是因为上述这些类型在传值时，总是值传递1。比如在函数传参数时，或进行变量赋值时

##### 布尔(Booleans)

bool: The possible values are constants true and false.

Operators:

`!` (logical negation)
`&&` (logical conjunction, “and”)
`||` (logical disjunction, “or”)
`==` (equality)
`!=` (inequality)

运算符&&和||是短路运算符，如f(x)||g(y)，当f(x)为真时，则不会继续执行g(y)。


##### 整型(Integer)

int/uint：变长的有符号或无符号整型。变量支持的步长以8递增，支持从uint8到uint256，以及int8到int256。需要注意的是，uint和int默认代表的是uint256和int256。

Operators:

比较: `<=, <, ==, !=, >=, >` (evaluate to bool)
位运算符: `&, |, ^` (bitwise exclusive or), `~` (bitwise negation)
Shift operators: `<<` (left shift), `>>` (right shift)
数学运算:` +, -,` unary` -, *, /, %` (modulo),` ** `(exponentiation)

Comparisons
The value of a comparison is the one obtained by comparing the integer value.

Bit operations
Bit operations are performed on the two’s complement representation of the number. This means that, for example `~int256(0) == int256(-1)`.

Shifts
The result of a shift operation has the type of the left operand. The expression `x << y` is equivalent to `x * 2**y`, and, for positive integers, `x >> y` is equivalent to `x / 2**y`. For negative `x, x >> y` is equivalent to dividing by a power of `2` while rounding down (towards negative infinity). Shifting by a negative amount throws a runtime exception.

Warning

Before version `0.5.0` a right shift `x >> y` for negative `x` was equivalent to `x / 2**y`, i.e. right shifts used rounding towards zero instead of rounding towards negative infinity.

加法，减法和乘法

Addition, subtraction and multiplication have the usual semantics. They wrap in two’s complement representation, meaning that for example `uint256(0) - uint256(1) == 2**256 - 1`. You have to take these overflows into account when designing safe smart contracts.

The expression -x is equivalent to (T(0) - x) where T is the type of x. This means that -x will not be negative if the type of x is an unsigned integer type. Also, -x can be positive if x is negative. There is another caveat also resulting from two’s complement representation:

    int x = -2**255;
    assert(-x == x);

This means that even if a number is negative, you cannot assume that its negation will be positive.

Division
Since the type of the result of an operation is always the type of one of the operands, division on integers always results in an integer. In Solidity, division rounds towards zero. This mean that `int256(-5) / int256(2) == int256(-2)`.

Note that in contrast, division on literals results in fractional values of arbitrary precision.

Note

Division by zero causes a failing assert.

Modulo
The modulo operation a % n yields the remainder r after the division of the operand a by the operand n, where q = int(a / n) and r = a - (n * q). This means that modulo results in the same sign as its left operand (or zero) and a % n == -(abs(a) % n) holds for negative a:

    int256(5) % int256(2) == int256(1)
    int256(5) % int256(-2) == int256(1)
    int256(-5) % int256(2) == int256(-1)
    int256(-5) % int256(-2) == int256(-1)

Note

Modulo with zero causes a failing assert.

幂

Exponentiation is only available for unsigned types. Please take care that the types you are using are large enough to hold the result and prepare for potential wrapping behaviour.

Note

Note that `0**0` is defined by the EVM as 1.


##### Fixed Point Numbers

Warning

Fixed point numbers are not fully supported by Solidity yet. They can be declared, but cannot be assigned to or from.

fixed / ufixed: Signed and unsigned fixed point number of various sizes. Keywords ufixedMxN and fixedMxN, where M represents the number of bits taken by the type and N represents how many decimal points are available. M must be divisible by 8 and goes from 8 to 256 bits. N must be between 0 and 80, inclusive. ufixed and fixed are aliases for ufixed128x18 and fixed128x18, respectively.

Operators:

Comparisons: `<=, <, ==, !=, >=, >` (evaluate to bool)
Arithmetic operators: `+, -, unary -, *, /, %` (modulo)

Note

The main difference between floating point (float and double in many languages, more precisely IEEE 754 numbers) and fixed point numbers is that the number of bits used for the integer and the fractional part (the part after the decimal dot) is flexible in the former, while it is strictly defined in the latter. Generally, in floating point almost the entire space is used to represent the number, while only a small number of bits define where the decimal point is.

##### 地址(Address)

地址类型有两种形式，大致相同：

address: 保存一个20字节的值（以太坊地址的大小）。
address payable: 与地址相同，but with the additional members transfer and send.
区别是，address payable是您可以发送Ether，而普通地址不能发送Ether。

输入转化次数：

允许从地址到地址的隐式转换，而从地址到地址的转换是不可能的（执行此类转换的唯一方法是使用uint160的中间转换）。

Address literals可以隐式转换为address payable。

Explicit conversions to and from address are allowed for integers, integer literals, bytes20 and contract types with the following caveat: Conversions of the form address payable(x) are not allowed. Instead the result of a conversion of the form address(x) has the type address payable, if x is of integer or fixed bytes type, a literal or a contract with a payable fallback function. If x is a contract without payable fallback function, then address(x) will be of type address. In external function signatures address is used for both the address and the address payable type.
对于整数，整数文字，bytes20和合约类型，允许对地址进行明确的转换，但需要注意以下事项：不允许转换表格地址（x）。 相反，表单地址（x）的转换结果具有应付类型地址，如果x是整数或固定字节类型，文字或具有应付回退函数的合同。 如果x是没有应付回退函数的合约，则地址（x）将是地址类型。 在外部函数签名中，地址用于地址和地址应付类型。

注意

很可能你不需要关心应付地址（address payable）和地址之间的区别，只是到处使用地址。 例如，如果您使用提款模式，您可以（并且应该）将地址本身存储为地址，因为您在msg.sender上调用交易函数，这是一个应付地址（address payable）。

运算符:

`<=, <, ==, !=, >= and >`

警告

如果将使用较大字节大小的类型转换为地址（例如bytes32），则会截断该地址。 要减少编译器强制转换歧义版本0.4.24及更高版本，请在转换中使截断显式化。 以地址0x111122223333444455556666777788889999AAAABBBBCCCCDDDDEEEEFFFFCCCC为例。

您可以使用 address(uint160(bytes20(b))), 这会产生0x111122223333444455556666777788889999aAaa，或者您可以使用 address(uint160(uint256(b))), 这会产生0x777788889999AaAAbBbbCcccddDdeeeEfFFfCcCc。

注意

The distinction between address and address payable was introduced with version 0.5.0. Also starting from that version, contracts do not derive from the address type, but can still be explicitly converted to address or to address payable, if they have a payable fallback function.
应付地址和地址之间的区别是在0.5.0版本中引入的。 同样从该版本开始，合同不是从地址类型派生的，但如果它们具有应付回退功能，则仍然可以显式转换为地址或地址应付款。

地址类型的成员

    balance and transfer

可以使用属性余额查询地址余额，并使用传递函数将以太（以wei为单位）发送到 address payable：

    address payable x = address(0x123);
    address myAddress = address(this);
    if (x.balance < 10 && myAddress.balance >= 10) x.transfer(10);

如果当前合同的余额不够大或者接收帐户拒绝以太转移，则转移功能将失败。传递函数在失败时恢复。

注意

If x is a contract address, its code (more specifically: its Fallback Function, if present) will be executed together with the transfer call (this is a feature of the EVM and cannot be prevented). If that execution runs out of gas or fails in any way, the Ether transfer will be reverted and the current contract will stop with an exception.

send
Send is the low-level counterpart of transfer. If the execution fails, the current contract will not stop with an exception, but send will return false.

Warning

There are some dangers in using send: The transfer fails if the call stack depth is at 1024 (this can always be forced by the caller) and it also fails if the recipient runs out of gas. So in order to make safe Ether transfers, always check the return value of send, use transfer or even better: use a pattern where the recipient withdraws the money.

call, delegatecall and staticcall
In order to interface with contracts that do not adhere to the ABI, or to get more direct control over the encoding, the functions call, delegatecall and staticcall are provided. They all take a single bytes memory argument as input and return the success condition (as a bool) and the returned data (bytes memory). The functions abi.encode, abi.encodePacked, abi.encodeWithSelector and abi.encodeWithSignature can be used to encode structured data.

Example:

如果x是合同地址，则其代码（更具体地说：其后备功能，如果存在）将与转移呼叫一起执行（这是EVM的一项功能，无法阻止）。如果执行耗尽气体或以任何方式失败，则以太网转移将被恢复，当前合同将以例外停止。

发送
发送是转移的低级别对应方。如果执行失败，则当前合同不会因异常而停止，但send将返回false。

警告

使用send会有一些危险：如果调用堆栈深度为1024（这可能始终由调用者强制），则传输失败，如果收件人耗尽了气体，它也会失败。因此，为了进行安全的以太传输，请始终检查发送的返回值，使用传输甚至更好：使用收件人提取资金的模式。

call，delegatecall和staticcall
为了与不遵守ABI的合同接口，或者为了更直接地控制编码，提供了函数call，delegatecall和staticcall。它们都将单字节内存参数作为输入，并返回成功条件（作为bool）和返回的数据（字节内存）。函数abi.encode，abi.encodePacked，abi.encodeWithSelector和abi.encodeWithSignature可用于编码结构化数据。

例：

bytes memory payload = abi.encodeWithSignature("register(string)", "MyName");
(bool success, bytes memory returnData) = address(nameReg).call(payload);
require(success);
Warning

All these functions are low-level functions and should be used with care. Specifically, any unknown contract might be malicious and if you call it, you hand over control to that contract which could in turn call back into your contract, so be prepared for changes to your state variables when the call returns. The regular way to interact with other contracts is to call a function on a contract object (x.f()).

:: note::
Previous versions of Solidity allowed these functions to receive arbitrary arguments and would also handle a first argument of type bytes4 differently. These edge cases were removed in version 0.5.0.
It is possible to adjust the supplied gas with the .gas() modifier:




bytes memory payload = abi.encodeWithSignature（“register（string）”，“MyName”）;
（bool成功，字节存储器返回数据）=地址（nameReg）.call（有效载荷）;
要求（成功）;
警告

所有这些功能都是低级功能，应谨慎使用。具体来说，任何未知的合同都可能是恶意的，如果你调用它，你就可以将控制权移交给合同，而合同又可以回调你的合同，所以在调用返回时准备好改变你的状态变量。与其他契约交互的常规方法是在契约对象（x.f（））上调用函数。

：： 注意：：
以前版本的Solidity允许这些函数接收任意参数，并且还会以不同方式处理bytes4类型的第一个参数。在版本0.5.0中删除了这些边缘情况。
可以使用.gas（）修饰符调整供应的气体：

##### 

##### 定长字节数组(fixed byte arrays)

##### 
#####  

##### 有理数(Rational and Integer Literals)

##### 整型(String literals)
#####  

##### 枚举类型(Enums)
##### 函数(Function Types)


#### Reference Types

复杂类型，占用空间较大的。在拷贝时占用空间较大。所以考虑通过引用传递。常见的引用类型有：

不定长字节数组（bytes）
字符串（string）
数组（Array）
结构体（Struts）

#####  
#####  
#####  
#####  


#### Operators Involving LValues
#####  


#### 
#####  
#####  


#### 
#####  
#####  
#####  


### Units and Globally Available Variables
###
###
###

## Solidity的例子

### 投票

以下合约相当复杂，但展示了很多Solidity的功能。 它是投票合约。 当然，电子投票的主要问题是如何为正确的人分配投票权以及如何防止操纵。 我们不会在这里解决所有问题，但至少我们将展示如何进行授权投票，投票计数是自动的，完全透明的。

这个想法是每次投票创建一个合约，为每个选项提供一个简短的名称。 然后，作为主席的合约的创建者将分别给每个地址分配投票的权力。

然后，地址背后的人可以选择自己投票或将投票委托给他们信任的人。

在投票时间结束时，`winnerProposal（）`将返回投票数最多的提案。

    pragma solidity ^0.4.22;

    /// @title 授权投票 Voting with delegation
    contract Ballot {
        // 这声明了一个新的复杂类型，稍后将用于变量。 
        // 它将代表一个选民。
        struct Voter {
            uint weight; // 权重由授权累积 weight is accumulated by delegation
            bool voted;  // 如果是true，那个人已经投了票
            address delegate; // 被授权的人
            uint vote;   // 投票提案的索引
        }

        // 这是单个提案的类型。
        struct Proposal {
            bytes32 name;   // 简称 (up to 32 bytes)
            uint voteCount; // 累积票数
        }

        address public chairperson;

        // 这声明了一个状态变量，它为每个可能的地址存储一个`Voter`struct。
        mapping(address => Voter) public voters;

        // 一个动态大小的数组，`Proposal`structs。
        Proposal[] public proposals;

        /// 创建一个新的选票以选择一个`proposalNames`。
        constructor(bytes32[] proposalNames) public {
            chairperson = msg.sender;
            voters[chairperson].weight = 1;
       
            // 对于每个提案的提议名称，创建一个新的提案对象并将其添加到数组的末尾。
            for (uint i = 0; i < proposalNames.length; i++) {
                // `Proposal({...})` creates a temporary
                // Proposal object and `proposals.push(...)`
                // appends it to the end of `proposals`.
                proposals.push(Proposal({
                    name: proposalNames[i],
                    voteCount: 0
                }));
            }
        }

        // 赋予“选民voter”投票权。
        // 只能由`主席chairperson`调用。
        function giveRightToVote(address voter) public {
            // 如果`require`的第一个参数得到'false`，则执行终止，并对状态进行回滚，和恢复以太币的余额。 
            // 这曾用于消耗旧EVM版本中的所有gas，但现在不再消耗。 使用`require`检查函数是否被正确调用通常是个好主意。
            // 作为第二个参数，您还可以提供有关错误的解释。
            require(
                msg.sender == chairperson,
                "Only chairperson can give right to vote."
            );
            require(
                !voters[voter].voted,
                "The voter already voted."
            );
            require(voters[voter].weight == 0);
            voters[voter].weight = 1;
        }

        /// 将您的投票分配给选民`to`。
        function delegate(address to) public {
            // 分配参考
            Voter storage sender = voters[msg.sender];
            require(!sender.voted, "You already voted.");

            require(to != msg.sender, "Self-delegation is disallowed.");

            // 只要分配`to`分配，就转发分配。 
            // 一般来说，这种循环非常危险，因为如果它们运行时间太长，它们可能需要比块中可用的gas更多的gas。 在这种情况下，委托将不会被执行，但在其他情况下，这样的循环可能会导致合约完全“卡住”。
            while (voters[to].delegate != address(0)) {
                to = voters[to].delegate;

                // 我们在分配中找到一个循环，这是不被允许的
                require(to != msg.sender, "Found loop in delegation.");
            }

            // 由于`sender`是一个引用，这会修改`votes [msg.sender].voted`
            sender.voted = true;
            sender.delegate = to;
            Voter storage delegate_ = voters[to];
            if (delegate_.voted) {
                // 如果代表已经投票，则直接添加投票数
                proposals[delegate_.vote].voteCount += sender.weight;
            } else {
                // 如果代表尚未投票，请增加权重。
                delegate_.weight += sender.weight;
            }
        }

        /// 将您的投票（包括授权给您的投票）提交给提案`proposals[proposal].name`。
        function vote(uint proposal) public {
            Voter storage sender = voters[msg.sender];
            require(!sender.voted, "Already voted.");
            sender.voted = true;
            sender.vote = proposal;

            // 如果`proposal`超出了数组的范围，它将自动抛出并恢复所有更改。
            proposals[proposal].voteCount += sender.weight;
        }

        /// @dev 计算所有先前投票的获胜提案。
        function winningProposal() public view
                returns (uint winningProposal_)
        {
            uint winningVoteCount = 0;
            for (uint p = 0; p < proposals.length; p++) {
                if (proposals[p].voteCount > winningVoteCount) {
                    winningVoteCount = proposals[p].voteCount;
                    winningProposal_ = p;
                }
            }
        }

        // Calls winningProposal() function to get the index
        // of the winner contained in the proposals array and then
        // returns the name of the winner
        function winnerName() public view
                returns (bytes32 winnerName_)
        {
            winnerName_ = proposals[winningProposal()].name;
        }
    }

#### 完善空间

目前，需要许多交易来将投票权分配给所有参与者。 你能想到一个更好的方法吗？

### 盲拍
#### Simple Open Auction

#### 网购
### Safe Remote Purchase


## 关于安全的考量
###
#### 
#### 
## 使用编译器
###
#### 
#### 
## 合约的元数据
###
#### 
#### 
## 应用二进制接口规范（ABI）
###
#### 
#### 
## 用于（内联）汇编的快乐通用语言
## 风格指导
## 常见模式
## 已知的Bug清单
## 常见问题

