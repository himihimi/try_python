# http://www.runoob.com/python/python-object.html 看这个参考资料的

# 员工的基类
class Employee:
    # 成员变量(错)?? 类变量??? php中的static? [大概]
    emp_count = 0

    # 成员函数

    # 这个init是特殊函数,一定会在生成实例instance的时候被叫上,相当于[构造函数]吧
    # pyhton的构造函数好奇怪啊,要写self,不把self示例放进去就不可以吗嗯??
    def __init__(self, name, salary):
        # 成员变量不要声明的嘛?
        self.name = name
        self.salary = salary

        # ? 是类变量????? 用类名取的?
        Employee.emp_count += 1

    def displayCount(aaa):
        return "Total Employee %d" % Employee.emp_count

# self 不是 python 关键字，我们把他换成 runoob 也是可以正常执行的:
    def displayEmployee(self):
        return "Name : ", self.name, ", Salary: ", self.salary

    def nothingNeedSelf(ppp):
        return '根本没用self还要写在参数里面是不是很烦,这个就是为了让人知道这是成员函数么'

    def needSelfAndOther(ppp, inti):
        ppp.salary = inti
        return ppp.salary
        # return '根本没用self还要写在参数里面是不是很烦,这个就是为了让人知道这是成员函数么'

# 来我们来创建对象!
#himi_no1 = Employee()
#TypeError: __init__() missing 2 required positional arguments: 'name' and 'salary'

himi_no1 = Employee('himi1', '1')

# print(displayCount(himi_no1))
# NameError: name 'displayCount' is not defined

print(himi_no1.displayCount())

print(himi_no1.displayEmployee())
print(himi_no1.needSelfAndOther(2000))
'''
    print(himi_no1.needSelfAndOther(himi_no1, 2000))
TypeError: needSelfAndOther() takes 2 positional arguments but 3 were given
第一个self是不用给的
'''

# 来一个基础继承

class SysEmployee (Employee):

    def sysWorkTime(self):
        self.work_time = 8
    #??? python下面就不需要setter和getter来获取变量了?直接就暴力???不太好吧

himi_sys = SysEmployee('sys', 'ppp')
'''
他的构造,如果写了就不能用不带参数的构造方法,就要放入参数
    himi_sys = SysEmployee()
TypeError: __init__() missing 2 required positional arguments: 'name' and 'salary'
'''
print(himi_sys.displayEmployee())

print(himi_no1.displayCount())
print(himi_sys.displayCount())
'''
Total Employee 2
Total Employee 2
'''
print(himi_no1.emp_count)
print(himi_sys.emp_count)
'''
2
2
好奇怪啊类变量竟然可以用对象instance来取,不应该是类名来取么
python你好任性 
↓类名也能取,服气
'''
print(SysEmployee.emp_count)

himi_sys.sysWorkTime();
print(himi_sys.work_time)
'''
直接用不行,要过一次生成
    print(himi_sys.work_time)
AttributeError: 'SysEmployee' object has no attribute 'work_time'
'''