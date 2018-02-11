在pyCharm中导入第三方库之后
直接在
```
himiMacBookPro:pc_ce himi$ which pip
/usr/local/bin/pip
```
出现的是装在这个下面的pip
```
himiMacBookPro:.ssh himi$ /usr/local/bin/pip --version
pip 8.1.1 from /Library/Python/2.7/site-packages/pip-8.1.1-py2.7.egg (python 2.7)
```
这个下面的默认版本就是老版本
而我在pyCharm中看的是9的版本
```
himiMacBookPro:venv himi$ /Users/himi/12_py/pc_ce/venv/bin/pip --version
pip 9.0.1 from /Users/himi/12_py/pc_ce/venv/lib/python3.5/site-packages (python 3.5)
```
所以是要跑去这个项目下的bin里去找
那就有了
执行估计也是要用这个直接路径来执行
否则会使用系统的那个老pip

其实我也不知道pip是个啥
查一下
```
pip 是一个现代的，通用的 Python 包管理工具[1]  。提供了对Python 包的查找、下载、安装、卸载的功能。
官方提供的pip 示例
$ pip install requests
$ pip search xml
$ pip show beautifulsoup4
$ pip uninstall requests
```
嗯,包管理工具
我到现在都不是很理解包管理工具
大概就,随便了

哇接下来下载beautifulsoup4

> https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html

```
$ pip install beautifulsoup4
那么我要
/Users/himi/12_py/pc_ce/venv/bin/pip install beautifulsoup4
绝对路径安装咯只能
我不知道这个要不要求现在路径是什么.....

himiMacBookPro:venv himi$ /Users/himi/12_py/pc_ce/venv/bin/pip install beautifulsoup4
Collecting beautifulsoup4
  Downloading beautifulsoup4-4.6.0-py3-none-any.whl (86kB)
    100% |████████████████████████████████| 92kB 430kB/s
Installing collected packages: beautifulsoup4
Successfully installed beautifulsoup4-4.6.0

哦貌似随便搞一下就好了
```

顺带搜索的时候看到一篇不错的字符集文
> http://blog.csdn.net/idiot_xue/article/details/72626332