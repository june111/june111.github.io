

The value of a BigNumber is stored in a decimal floating point format in terms of a coefficient, exponent and sign.

	x = new BigNumber(-123.456);
	x.c                                 // [ 123, 45600000000000 ]  coefficient (i.e. significand)
	x.e                                 // 2                        exponent
	x.s                                 // -1                       sign


参考链接

[bignumber.js](http://www.bootcdn.cn/bignumber.js/readme/)