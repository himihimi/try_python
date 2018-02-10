# so we go to the function

def f1(a, b):
    return a * b

def f2(a, b):
    return '1/2 * a * b'

print(f1(3, 2))
# NameError: name 'f1' is not defined
# 6

print(f2(3, 2))
# 1/2 * a * b

def cN(num):
     hid_n = num.replace(num[5:10], 'saaa')
     return hid_n

print(cN('123'))
# cN(12)  AttributeError: 'int' object has no attribute 'replace'
# saaa1saaa2saaa
# saaa1saaa2saaa3saaa

def checkPass():
    pass_word = input('ppppp')
    res = ''
    if pass_word == 'kikikik':
        res = 'ók'
    else:
        p = 'p'
      #  res = 'dfadfa'
    #UnboundLocalError: local variable 'res' referenced before assignment
    # 说到底还是要声明的，不声明return一定会报错
    # 我还以为python厉害倒直接回个null之类的
    return res
print(checkPass())



