import requests
from bs4 import BeautifulSoup

# http://www.python-requests.org/en/master/ 其实官方的例子很直白
# http://docs.python-requests.org/zh_CN/latest/user/quickstart.html

res0 = requests.get('https://bangumi.bilibili.com/22/')
print(res0)
# ↑这个只吐出http status code
# print(res.text)
# ↑这个吐网页渲染后代码
'''
感受:
这个封装太实惠?!!!! 啊我不用一次次一次打curl来测试了不是么!!
不过要说curl的话,curl有curl的必要性,不过这个也是很便利嗯
'''

# 伪装自己是浏览器
# 在resquest里面加head信息

header_try = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

res1 = requests.get('https://bangumi.bilibili.com/22/', headers = header_try)
print(res1)

soup = BeautifulSoup(res1.text, 'html.parser')
# print(soup.prettify())
# ↑这个吐网页渲染后代码的整整齐齐版本!!!非常整齐!!!!!!
'''
虽然还没仔细看bilibili的代码,但是吐出来的内容只有一部分整齐的标题,所以毫无疑问其他部分异步了
那部分估计我就先看chrome的request然后找request单独打?
诶不是把?
你为什么不能帮我都打好?
不是模拟浏览器么??? 内容没有抓啥????

'''

print(soup.find_all('h2'))
# [<h2>最近更新</h2>, <h2>连载动画</h2>, <h2>完结动画</h2>, <h2>资讯</h2>, <h2>官方延伸</h2>]
# 原来返回的是列表

print(soup.find('h2'))
# <h2>最近更新</h2> 只找第一个

html_s = '#bangumi_top > div > div > div > div.topic-preview-list-wrapper > ul > li:nth-child(3) > a > img'
print(soup.selector(html_s))
# TypeError: 'NoneType' object is not callable 果然是没有啊!!!!怎么办!

res2 = requests.get('https://space.bilibili.com/542842/#/', headers = header_try)

print(res2)
# print(res2.content)
# ↑这个不换行啊?
'''
哦,大概是在编码的时候用...也许

>如果你改变了编码，每当你访问 r.text ，Request 都将会使用 r.encoding 的新值。你可能希望在使用特殊逻辑计算出文本的编码的情况下来修改编码。比如 HTTP 和 XML 自身可以指定编码。这样的话，你应该使用 r.content 来找到编码，然后设置 r.encoding 为相应的编码。这样就能使用正确的编码解析 r.text 了。
'''


res3 = requests.get('http://www.dilidili.wang/anime/Samurai/index.html', headers = header_try)
print(res3)
# <Response [502]>  报错类型代码 bad gateway 错误的网关
# 我若是什么搞清楚如何解决这类问题的话就好了 <Response [200]> 有的时候是

