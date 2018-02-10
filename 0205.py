a = 4
b = 5
t = a
a = b
b = t
print(a,b,t)
# use the 3 jiaoxing

a = "i"
b = 'love'
c = 'nothing'
print(a + b +c)
print(a,b,t)
# ab 被取代掉了

print(a *3)
print(a)
# a没有被*3代替掉 （对的白痴都知道把

str = ' this is python desu'

print(str[1]);
# 这个直接用貌似php没有，php是取数组的时候用，这样的对于字符串应该是要通过某个函数strop？
print(str[1:2]);
print(str[1:3]);
# index的左取，右不取
# php使用函数实现这个功能

url = 'www.google.com'
so = url.split('.')
# 所以这个so得到的是一个数组？？不是，"列表"
print(so)
# ['www', 'google', 'com']

so1 = url.replace('www', 'https://www')
print(url)
print(so1)
# url 没变，给so1了
# www.google.com
# https://www.google.com

a = '       [zhengwen ]  ad df d  dada dad ';
b = a.strip()
print(a)
print(b)
#       [zhengwen ]  ad df d  dada dad
#[zhengwen ]  ad df d  dada dad

a = '&&&&&&&&&[zhengwen ] && ad df d & dada dad &&&';
b = a.strip('&')
print(a)
print(b)
a = '       [zhengwen ]  ad df d  dada dad ';
b = a.strip()
print(a)
print(b)
#&&&&&&&&&[zhengwen ] && ad df d & dada dad &&&
#[zhengwen ] && ad df d & dada dad
#只去头尾

i = input('please enter the thins')
a = '{} behind the clost?'.format(i)
print(a)

# input 是控制栏输入

