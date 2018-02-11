import random

#target_n = random.randint(0,99) 为毛要随机啦,输入就好了把
target_n = int(input("你要求哪个的因数:"))
res = []
do_flag = 'yes'

def divideAgain(num_devided):
    for i in range(2, num_devided+1):
        if num_devided % i == 0:
            num_devided = int(num_devided / i)
            res.append(i)
            global target_n
            target_n = num_devided
            # print(target_n)
            return
            # 要替换最大值num_devided并且重来
    global do_flag
    do_flag = "no"

# 这的全局变量我会用对象属性来实现(如果直接建立class的话,但是这次就算了)

while do_flag != 'no' :
   # print(target_n)
    divideAgain(target_n)

print('大概是所有因数' , res)
print('不重复因数' , set(res))

'''
写if的时候本来想用三元运算的
http://blog.csdn.net/lanchunhui/article/details/50248327
但是发现貌似还要写几句处理, 所以就没用上
'''