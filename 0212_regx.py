# 不晓得为啥有点不想写了 嘛就随便试一试把
import re

str = '悲しみの中にーひみーラジャー112121221112222112 klhnglh@dfaklj.com'
print(re.match('com', str))
# None

print(re.match('.*com', str))
# <_sre.SRE_Match object; span=(0, 51), match='悲しみの中にーひみーラジャー112121221112222112 klhnglh@dfaklj.c>
# ?? com 呢?

tel = '+819012345566, +817770000999, +98'
print(re.match('\+.*,', tel))
# <_sre.SRE_Match object; span=(0, 29), match='+819012345566, +817770000999,'>
print(re.match('\+.*', tel))
# <_sre.SRE_Match object; span=(0, 33), match='+819012345566, +817770000999, +98'>


print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配
#(0, 3)
#None


line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!!")
# 正则里面的() 是$1 的概念的利用

'''
re.match与re.search的区别
re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。
'''

# http://www.runoob.com/python/python-reg-expressions.html
# 大概了解了,要用到的时候再细看好了