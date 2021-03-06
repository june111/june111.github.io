---
layout: post
title: '什么是 Dapp'
subtitle: '超长不看版（《Mastering Ethereum》第十二章翻译）'
date: 2019-01-21
author: June
cover: /assets/img/post/2019-01-21/cover.jpg
reward: 1
tags: 区块链
---

# 什么是 Dapp ？

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2019-01-21/structure.svg">
![文章结构]({{site.baseurl}}/assets/img/post/2019-01-21/structure.svg)
</a>

Dapp 就是在应用的组成部分中，大部分或完全的去中心化。
A DApp is an application that is mostly or entirely decentralized.

应用可以去中心化的部分有：

* 后端（程序逻辑）
* 前端
* 数据存储
* 消息通信
* 名称解析

这些部分可以中心化，也可以在某种程度上去中心化。例如前端可以在中心化的服务器上运行，也可以作为手机应用在手机上运行。后端和存储可以位于私有服务器和专有数据库上，也可以使用智能合约和P2P存储。

Dapp的优点

* 弹性
	由于业务逻辑由智能合约控制，因此DApp后端将在区块链平台上完全分发和管理。与部署在中央服务器上的应用程序不同，DApp不会有停机时间，只要平台仍在运行，它就会继续可用。

* 透明度
	DApp的链上特性允许每个人检查代码并更加确定其功能。与DApp的任何交互都将永久存储在区块链中。

* 审查阻力
	只要用户可以访问以太坊节点（必要时运行一个），用户将始终能够与DApp交互而不受任何中央控制的干扰。在网络上部署代码后，任何服务提供商，甚至智能合约的所有者都无法更改代码。

## 后端（智能合约）

在DApp中，智能合约用于存储业务逻辑（程序代码）和应用程序的相关状态。您可以考虑在常规应用程序中替换服务器端（也称为“后端”）组件的智能合约。当然，这是一种过于简单化的做法。其中一个主要区别是智能合约中执行的任何计算都非常昂贵，因此应尽可能保持最小化。因此，确定应用程序的哪些方面需要去中心化非常重要。

以太坊智能合约允许您构建一种架构，其中智能合约网络在彼此之间调用和传递数据，随时读取和写入自己的状态变量，其复杂性仅受gas限制的限制。部署智能合约后，未来许多其他开发人员都可以使用您的业务逻辑。

智能合约架构设计的一个主要考虑因素是部署后无法更改智能合约的代码。如果使用可访问的SELFDESTRUCT操作码对其进行编程，则可以将其删除，但除了完全删除之外，不能以任何方式更改代码。

智能合约架构设计的第二个主要考虑因素是DApp大小。一个非常庞大的单片智能合约可能会花费大量的gas进行部署和使用。因此，某些应用程序可能会选择进行离线计算和外部数据源。但请记住，让DApp的核心业务逻辑依赖于外部数据（例如，来自中央服务器）意味着您的用户必须信任这些外部资源。

## 前端（Web用户界面）

与DApp的业务逻辑（需要开发人员理解EVM和Solidity等新语言）不同，DApp的客户端接口可以使用标准Web技术（HTML，CSS，JavaScript等）。 这允许传统的Web开发人员使用熟悉的工具，库和框架。 与以太坊的交互，例如签名消息，发送交易和管理密钥，通常通过网络浏览器，通过MetaMask等扩展进行。

虽然也可以创建移动DApp，但目前很少有资源可以帮助创建移动DApp前端，这主要是因为缺少可以作为具有密钥管理功能的轻客户端的移动客户端。

前端通常通过web3.js JavaScript库链接到以太坊，该库与前端资源捆绑在一起，并由Web服务器提供给浏览器。

## 数据存储

由于高昂的gas成本和目前较低的gas限制，智能合约不太适合存储或处理大量数据。 因此，大多数DApps利用离线数据存储服务，把数据存在数据存储平台，这意味着他们把数据存在链下。 该数据存储平台可以是中心化的（例如，典型的云数据库），也可以是去中心化的，存储在P2P平台上，例如IPFS或以太坊自己的Swarm平台。

分布式P2P存储非常适合存储和分发大型静态资产，如图像，视频和应用程序前端Web界面（HTML，CSS，JavaScript等）的资源。 我们接下来会看几个选择。

### IPFS

星际文件系统（IPFS）是一种分布式的内容可寻址存储系统，在节点中分布式地存储对象。“内容可寻址”表示对每段内容（文件）进行哈希处理，并使用哈希来标识该文件。然后，您可以通过哈希从IPFS节点检索文件。

IPFS旨在取代HTTP作为交付Web应用程序的首选协议。这些文件不是在单个服务器上存储Web应用程序，而是存储在IPFS上，可以从任何IPFS节点检索。

有关IPFS的更多信息，请访问https://ipfs.io。

### Swarm

Swarm是另一种内容可寻址的P2P存储系统，类似于IPFS。 Swarm由以太坊基金会创建，作为Go-Ethereum工具套件的一部分。与IPFS一样，它允许您存储由Swarm节点传播和复制的文件。您可以通过哈希引用任何Swarm文件来访问它。 Swarm允许您从分布式P2P系统访问网站，而不是中央Web服务器。

Swarm的主页本身存储在Swarm上，可以在Swarm节点或网关上访问：https://swarm-gateways.net/bzz:/theswarm.eth/

## 分布式的消息通信协议

应用程序的另一个主要组件是进程间通信。 这意味着能够在应用程序之间，应用程序的不同实例之间或应用程序的用户之间交换消息。 传统上，这是通过依赖中央服务器来实现的。 但是，基于服务器的协议有很多分布式的替代方案，可以通过P2P网络提供消息传递。最值得注意的DApps P2P消息传递协议是Whisper，它是以太坊基金会Go-Ethereum工具套件的一部分。

DApp的最后一个方面是名称解析。 我们将在本章后面仔细研究以太坊的名称服务; 不过，现在先让我们来看一个例子吧。

## 一个基础的DAPP例子：拍卖DApp

我在原文章的基础上加了些解释，具体到这看————[拍卖DApp：都来拍一个属于自己的ENS吧]()

## 以太坊名称服务（ENS）

您可以设计世界上最好的智能合约，但如果您没有为用户提供良好的界面，他们将无法访问它。

在传统的互联网上，域名系统（DNS）允许我们在浏览器中使用人类可读的名称，同时将这些名称解析为IP地址或其他标识符。在以太坊区块链上，以太坊命名系统（ENS）以分布式的方式解决了同样的问题。

例如，以太坊基金会捐赠地址为0xfB6916095ca1df60&thinsp;bB79Ce92cE3Ea74c37c5d359；在支持ENS的钱包中，它只是ethereum.eth。

ENS不仅仅是一份智能合约;它是一个基本的DApp本身，提供分布式的名称服务。此外，ENS由许多DApps支持，用于注册，管理和注册名称的拍卖。 ENS演示了DApps如何协同工作：它是为其他DApp服务的DApp，由DApps生态系统支持，嵌入在其他DApp中，等等。

在本节中，我们将了解ENS的工作原理。我们将演示如何设置自己的名称并将其链接到钱包或以太坊地址，如何将ENS嵌入到另一个DApp中，以及如何使用ENS命名您的DApp资源以使其更易于使用。


### ENS规范

ENS主要在三个以太坊改进提案中指定：[EIP-137](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-137.md)，其规定了ENS的基本功能; [EIP-162](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-162.md)，描述了.eth的拍卖系统;和[EIP-181](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-181.md)，它规定了地址的反向登记。

ENS遵循“三明治”设计理念：底部是一个非常简单的层，其次是更复杂但可替换的代码层，顶层非常简单，可以将所有资金保存在单独的帐户中。

### 底层：名称所有者和解析器

ENS操作“节点”而不是人类可读的名称：使用“Namehash”算法将人类可读的名称转换为节点。

ENS的基础层是由ERC137定义的一个非常简单的合约（少于50行代码），它只允许节点的所有者设置有关其名称的信息并创建子节点（ENS等效于DNS子域）。

基础层上的唯一功能是使节点所有者能够设置有关其自身节点的信息（特别是解析器，生存时间或转移所有权）以及创建新子节点的所有者。

#### Namehash算法

TODO

#### 如何选择有效的名称

名称由一系列点分隔标签组成。 尽管允许使用大写和小写字母，但所有标签都应遵循UTS＃46规范化过程，即在对标签进行哈希处理之前对其进行折叠处理，因此具有不同大小但拼写相同的名称最终将使用相同的Namehash。

您可以使用任何长度的标签和域，但为了与传统DNS兼容，建议使用以下规则：

* 标签每个不应超过64个字符。

* 完整的ENS名称不得超过255个字符。

* 标签不应以连字符开头或结尾，也不应以数字开头。

#### 根节点所有权

此分层系统的结果之一是它依赖于根节点的所有者，他们能够创建顶级域（top-level domains TLD）。

虽然最终的目标是为新TLD采用分散的决策流程，但在撰写本文时，根节点由7分之4的多重控制控制，由不同国家的人员持有（7个 DNS系统的关键人员）。因此，影响任何改变需要7个关键持有人中的至少有4个人。

目前，这些关键人物的目的和目标是与社区达成共识：

* 在评估系统后，将.eth TLD的临时所有权迁移并升级为更长久的合同。

* 如果社群同意需要，则允许添加新TLD。

* 在同意，测试和实施此类系统时，将根multisig的所有权迁移到更分散的合同。

* 作为处理顶级注册表中的任何错误或漏洞的最后方法。

#### 解析器

基本的ENS合同无法向名称添加元数据; 这就是所谓的“解析合同”的工作。 这些是用户创建的合同，可以回答有关名称的问题，例如Swarm地址与应用程序关联，接收付款到应用程序的地址（以太币或代币），或应用程序的哈希值（验证它的完整性）。

### 中间层：.eth节点

在撰写本文时，唯一可以在智能合约中注册的顶级域名是.eth。

注意
目前正在努力使传统的DNS域名所有者能够获得ENS所有权。 虽然理论上这可能适用于.com，但到目前为止，唯一实现此目的的域名是.xyz，并且只能在Ropsten testnet上使用。

.eth域名通过拍卖系统分发。 没有保留列表或优先级，获取名称的唯一方法是使用系统。 拍卖系统是一段复杂的代码（超过500行）; ENS中的大部分早期开发工作（和缺陷！）都在系统的这一部分。 但是，它也可以更换和升级，不会对资金造成风险。

#### 维克里拍卖

>即次价密封投标拍卖(Second-price sealed-bid auction)。投标者在不知道其他人标价的情况下递出标单，标价最高的人得标，但只需付次高的标价。

名称通过修改后的维克里拍卖分发。在传统的维克里拍卖中，每个投标人都提交密封投标，并且所有投标人同时被公开，此时最高出价者赢得拍卖，但只支付第二高的出价。因此，竞标者被激励不要向他们出价低于名称的真实价值，因为竞标他们的真实价值会增加他们赢得的机会，但不会影响他们最终支付的价格。

在区块链上，需要进行一些更改：

* 为了确保投标人不提交不想支付的投标，他们必须事先锁定等于或高于其投标的价值，以保证投标有效。

* 由于您无法隐藏区块链上的机密信息，因此投标人必须至少执行两笔交易（一个提交-揭示流程 a commit–reveal process），以隐藏其出价的原始值和名称。

* 由于您无法在分布式系统中同时显示所有出价，因此投标人必须自行展示自己的出价;如果他们不这样做，他们就会丧失锁定的资金。如果没有这种罚款，人们可以做出很多出价，并选择仅披露一两个，将密封拍卖变成传统的增加价格拍卖。

因此，拍卖分为四个步骤：

1. 开始拍卖。这是广播注册名称的意图所必需的。这将创建所有拍卖截止日期。这些名称是经过哈希处理的，因此只有在字典中具有该名称的人才能知道哪个拍卖被打开了。这允许一些隐私，这在您创建新项目并且不想共享其详细信息时非常有用。您可以同时打开多个虚拟拍卖，因此如果有人关注您，他们就不能简单地对您打开的所有拍卖进行出价。

2. 密封投标。您必须在竞标截止日期之前执行此操作，方法是将一定数量的以太币发送到符合到秘密消息的散列（其中包括名称的散列，实际的出价金额和盐）。您可以锁定比您实际出价更多的以太，以掩盖您的真实估值。

3. 显示出价。在显示期间，您必须进行显示出价的交易，然后计算出最高出价和第二高出价，并将以太送回给投标失败的人。每次出价都会重新计算当前的赢家;因此，在揭示截止日期到期之前设置的最后一个赢家，会成为总冠军。

4. 之后清理。如果您是赢家，则可以最终确定竞价，以便取消您的出价与第二高出价之间的差额。如果您忘记揭示，您可以进行延迟发布，并收回一些你的出价。

### 顶层：契约

ENS的最高层是另一个超级简单的合同，只有一个目的：持有资金。

当您赢得一个名字时，资金实际上并没有被发送到任何地方，而是在你持有这个名称的期间（至少一年）被锁定了。这有点像保证回购：如果所有者不再需要该名称，他们可以将其卖回给系统，并恢复他们的以太币。

当然，单一合约持有数百万美元的以太币已被证明是非常危险的，因此ENS为每个新名称创建合约。 契约合约非常简单（大约50行代码），它只允许将资金转回单个账户（契约所有者）并由单个实体（注册商合约）调用。 这种方法大大减少了攻击面，因为缺陷可能会使资金面临风险。


### 注册名称

正如我们在维克里拍卖会上看到的那样，在ENS中注册一个名称是一个分为四个步骤的过程。 首先我们对任何可用的名称进行出价，然后我们会在48小时后显示我们的出价以确保名称。

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2019-01-21/ens-flow.png">
![ENS注册时间表是显示注册时间表的图表]({{site.baseurl}}/assets/img/post/2019-01-21/ens-flow.png)
</a>

让我们注册我们的名字！

我们将使用几个可用的用户友好界面中的一个来搜索可用的名称，对名称ethereumbook.eth进行出价，显示出价并保护名称。

ENS有许多基于Web的界面，允许我们与ENS DApp进行交互。 对于这个例子，我们将使用MyCrypto接口和MetaMask作为我们的钱包。

首先，我们需要确保我们想要的名称可用。然后开始拍卖。

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2019-01-21/search-ens-name.png">
![开始拍卖]({{site.baseurl}}/assets/img/post/2019-01-21/search-ens-name.png)
</a>

密封投标。输入真实投标价和伪装投标价，开始一个拍卖。密文可自定义。

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2019-01-21/start-an-auction.png">
![密封投标]({{site.baseurl}}/assets/img/post/2019-01-21/start-an-auction.png)
</a>

确认投标

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2019-01-21/ens-bid.png">
![确认投标]({{site.baseurl}}/assets/img/post/2019-01-21/ens-bid.png)
</a>

注意

如维克里拍卖中所述，您必须在拍卖结束后48小时内公布您的出价，否则您将失去投标中的资金。 我们忘记这样做并且自己失去了0.01 ETH。

截取屏幕截图，保存您的密文（作为出价的备份），并在日历中添加提醒，这样您就不会忘记并丢失资金。

确认付款

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2019-01-21/ens-metamask-bid.png">
![确认付款]({{site.baseurl}}/assets/img/post/2019-01-21/ens-metamask-bid.png)
</a>

如果一切顺利，在以这种方式提交交易后，您可以在48小时内返回并揭示出价，并且您请求的名称将被注册到您的以太坊地址。

### 管理ENS名称

注册ENS名称后，您可以使用其他用户友好界面进行管理：[ENS Manager](https://manager.ens.domains/)。

在那里，在搜索框中输入您要管理的名称。 您需要将您的以太坊钱包（例如，MetaMask）解锁，以便ENS Manager DApp可以代表您管理该名称。

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2019-01-21/ens-man.png">
![管理ENS名称]({{site.baseurl}}/assets/img/post/2019-01-21/ens-man.png)
</a>

在此界面中，我们可以创建子域，设置解析器合约（稍后会详细介绍），并将每个名称连接到相应的资源，例如DApp前端的Swarm地址。

#### 创建ENS子域

首先，让我们为示例Auction DApp创建一个子域（auction.ethereumbook.eth）。 我们将命名子域名拍卖，因此完全限定名称将为auction.ethereumbook.eth。

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2019-01-21/ens_manager_add_subdomain.png">
![创建ENS子域]({{site.baseurl}}/assets/img/post/2019-01-21/ens_manager_add_subdomain.png)
</a>

一旦我们创建了子域，我们就可以在搜索框中输入auction.ethereumbook.eth并对其进行管理，就像我们之前管理域ethereumbook.eth一样。

### ENS解析器

在ENS中，解析名称的过程分为两步：

1. 调用ENS注册表，并在对其进行哈希处理后解析该名称。如果记录存在，注册表将返回其解析程序的地址。

2. 调用解析器，使用合适的方法请求资源。解析器返回所需的结果。

这个两步过程有几个好处。将解析器的功能与命名系统本身分开，为我们提供了更大的灵活性。名称所有者可以使用自定义解析器来解析任何类型或资源，从而扩展了ENS的功能。例如，如果将来您想要将地理位置资源（经度/纬度）链接到ENS名称，则可以创建一个新的解析器来回答地理定位查询。

为方便起见，有一个默认的公共解析器可以解析各种资源，包括地址（用于钱包或合同）和内容（用于DApps的Swarm哈希或合约源代码）。

为auction.ethereumbook.eth设置默认的公共解析器

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2019-01-21/ens-manager-set-default-resolver.png">
![为auction.ethereumbook.eth设置默认的公共解析器]({{site.baseurl}}/assets/img/post/2019-01-21/ens-manager-set-default-resolver.png)
</a>

由于我们想要将Auction DApp链接到Swarm哈希，我们可以使用支持内容解析的公共解析器，如设置auction.ethereumbook.eth的默认公共解析器中所示;我们不需要编写或部署自定义解析程序。

### 将名称解析为Swash哈希（内容）

将auction.ethereumbook.eth的解析器设置为公共解析器后，我们可以将其设置为返回Swarm哈希作为我们名称的内容（请参阅设置'content'以返回auction.ethereumbook.eth）。

设置'content'返回auction.ethereumbook.eth

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2019-01-21/ens-manager-set-content.png">
![设置'content'返回auction.ethereumbook.eth]({{site.baseurl}}/assets/img/post/2019-01-21/ens-manager-set-content.png)
</a>

等待我们的交易确认后，我们应该能够正确解析名称。 在设置名称之前，我们的Auction DApp可以通过其哈希在Swarm网关上找到：

[https://swarm-gateways.net/bzz:/ab164cf37dc10647e43a233486cdeffa8334b026e32a480dd9cbd020c12d4581](https://swarm-gateways.net/bzz:/ab164cf37dc10647e43a233486cdeffa8334b026e32a480dd9cbd020c12d4581)

或者通过在DApp浏览器或Swarm网关中搜索Swarm URL：

bzz://ab164cf37dc10647e43a233486cdeffa8334b026e32a480dd9cbd020c12d4581

现在我们将它附加到一个名称，它更容易：

[http://swarm-gateways.net/bzz:/auction.ethereumbook.eth/](http://swarm-gateways.net/bzz:/auction.ethereumbook.eth/)

我们也可以通过在任何兼容ENS的钱包或DApp浏览器（例如Mist）中搜索“auction.ethereumbook.eth”来找到它。

## App -> DApp

在过去的几个部分中，我们逐渐构建了一个分布式的应用程序。我们从两个智能合约开始，为ERC721进行拍卖。这些合约旨在没有管理或特权账户，因此他们的运作真正达到了去中心化。我们添加了一个用JavaScript实现的前端，它为我们的DApp提供了一个方便且用户友好的界面。拍卖DApp使用分布式存储系统Swarm来存储应用程序资源，例如图像。 DApp还使用分布式通信协议Whisper为每次拍卖提供加密聊天室，而无需任何中央服务器。

我们将整个前端上传到Swarm，以便我们的DApp不依赖任何Web服务器来提供文件。最后，我们使用ENS为DApp分配了一个名称，将其连接到前端的Swarm哈希，以便用户可以使用简单易记的人类可读名称访问它。

拍卖DApp的完整架构

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2019-01-21/auction_dapp_final_architecture.png">
![拍卖DApp的完整架构]({{site.baseurl}}/assets/img/post/2019-01-21/auction_dapp_final_architecture.png)
</a>

## 结论

去中心化的应用程序是以太坊愿景的顶点，正如创始人从最早的设计中所表达的那样。 虽然许多应用程序今天称自己为“DApps”，但大多数应用程序并未完全去中心化。 但是，已经可以构建几乎完全去中心化的应用程序。 随着时间的推移，随着技术的进一步发展，越来越多的应用程序可以去中心化，从而产生更具弹性，审查能力和免费的Web。

---

### 参考链接

* [Decentralized Applications (DApps)](https://github.com/ethereumbook/ethereumbook/blob/04f66ae45cd9405cce04a088556144be11979699/12dapps.asciidoc)
