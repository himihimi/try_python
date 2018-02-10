#☆ list ☆ = [php] 数字数组Array = Json数字数组
# http://www.runoob.com/python/python-lists.html

list1 = ['什么数据其实都可以,里面也可以放列表', 'aaa一个列表内容不同也可以', '跟json一样貌似最后不要逗号']
print(list1[0])
# print(list1[5])
# IndexError: list index out of range 还以为python很厉害能直接处理index不存在的情况呢

# list1[10] = '我就是要给你赋值'
# IndentationError: unexpected indent ↑上面这个方法貌似不行

list1.insert(10, 'Runoob')
# ↑这个写比现有存在数字大的内容就只是往后面存一位
list1.append('Runoob6')
# ↑直接往后面存一位
list1.insert(0, '7')
# ↑ 在0位置加入这个7,但是0位置不被替代的,往后推一位罢了
print(list1)


# ['7', '什么数据其实都可以,里面也可以放列表', 'aaa一个列表内容不同也可以', '跟json一样貌似最后不要逗号', 'Runoob', 'Runoob6']


#☆ dict ☆ = [php] 数字key值Array = Json key值数组
dict1 = {'name' : 'himi', '噗哈哈' : 'puhaha', 'test': 'tset'}
# php 'name' => 'himi',
# print(dict1[1])
# KeyError: 1 不可以用数字key来取了
print(dict1['name'])
#himi
print(dict1)
#{'name': 'himi', 'test': 'tset', '噗哈哈': 'puhaha'}

dict2 = {
    'name' : {
        'one': 'h',
        'two': 'i',
        '3' : 'm'
    },
    'nick_name' : 'himi'
}
print(dict2)
#{'nick_name': 'himi', 'name': {'two': 'i', 'one': 'h', '3': 'm'}}
print(dict2['name']['3'])
# m
# 嗯就是按照一般的数组操作


#☆ tuple ☆  不可以改的 圆形括号,一般在函数的地方用.
t1 = (1,2,3)
l_t = [('l1','lisht'),('aaa','dadf')]
print(l_t[1])
# 虽然貌似不能直接改,但是可以放在list然后处理的
d_t = dict(l_t)
print(d_t)
# {'l1': 'lisht', 'aaa': 'dadf'} 也可以用list的tuple的写法转dict

#参考 https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/0013868193482529754158abf734c00bba97c87f89a263b000/

#☆ set ☆  不重复集合,无序,去重复,貌似没有key,因为是list转set的,list没有key
l1 = [1, 2, 3]
s = set(l1)
print(s)
# {1, 2, 3} 好比是无key 不重复 数值key数组,用的{}括号

d1 = {'a':'b','v':'z'}
s2 = set(d1)
print(s2)
# {'v', 'a'} 卧槽这个好用诶,这个就是提取key! php中 getKey的作用可以用set来完成,顺带这个key也是unique的所以就ok
# 暂时没看到getValue这个函数在pyhton中怎么实现

# 反正代码就是找既存封装的函数来实现那几个提取来提取去的


# 然后是我很常用的Array的相互加来加去
# php里面就是用用merge,+来加加 他这个有的js的味道的用append
l1 = [1,2,3]
l2 = [3,5,6,7]

d1 = {'a':'aaa','b':'bbb','c':'ccc'}
d2 = {'a':'aaa2','d':'ddd','e':'eee','f':'fff'}

'''
1.append() 
2.extend() 
3.+  
4.+= 
'''

print(l1 + l2)
# [1, 2, 3, 3, 5, 6, 7]
print(l1)
print(l2)
# [1, 2, 3]   [3, 5, 6, 7] l1l2的值是没有变的

l3 = l1.append(l2)
print(l3)
# None
print(l1)
#[1, 2, 3, [3, 5, 6, 7]] 这个改了l1的 并且不返回内容给L3所以l3是none

# print(d1 + d2)
# TypeError: unsupported operand type(s) for +: 'dict' and 'dict' 太惨了 d的函数到时候再去找找用用把