 


 sudo /usr/local/sbin/privoxy /usr/local/etc/privoxy/config

 curl -i ip.cn

 export http_proxy=http://127.0.0.1:8118
 export https_proxy=http://127.0.0.1:8118

 curl -i ip.cn


7. 关闭Privoxy

首先查看privoxy的进程ID：

	ps aux | grep privoxy

返回如下内容：

	root              5730   0.0  0.0  2461516   2484   ??  Ss    2:12下午   0:00.58 ./privoxy /usr/local/etc/privoxy/config

得到进程ID为5730，然后用下面的命令关闭Privoxy：

	sudo kill 5730

或者更简便的方法是根据privoxy进程名来关闭Privoxy：

	sudo killall privoxy

若以上方法都无法关闭Privoxy，请使用Privoxy提供的脚本进行关闭：

	sudo /Applications/Privoxy/stopPrivoxy.sh


[参考链接](https://www.cnblogs.com/DeviLeo/p/6033591.html)