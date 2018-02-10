import random

#target_n = random.randint(0,99) 为毛要随机啦,输入就好了把
target_n = int(input("你要求哪个的因数:"))
target_loop = target_n
res = []
do_flag = 'yes'

def divideAgain(num_devided):
    for i in range(2, num_devided):
        if num_devided % i == 0:
            num_devided = int(num_devided / i)
            res.append(i)
            global target_n
            target_n = num_devided
            return
            # 要替换最大值num_devided并且重来
    global do_flag
    do_flag = "no"

# 这的全局变量我会用对象属性来实现(如果直接建立class的话,但是这次就算了)

while do_flag != 'no' :
    divideAgain(target_n)

print('大概是所有因数' , res)
print('不重复因数' , set(res))
