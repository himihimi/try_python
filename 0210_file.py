import time
import os

file = open('himi_log.txt', 'a+')
'''
绝对路径 ok
eg:/Users/himi/12_py/pc_ce/README.md
相对路径 OK
eg:README.md
r read | w write | a 追加add | b binary二进制(可添加于其他模式) | + (读写 可以添加)
'''
print("文件名: ", file.name)
# 这到底是,分割参数? 还是python用的,接字符串啊??
print("文件名: " + file.name)

# add ok
file.write(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + " \n");
# 这玩意时间用法和php差不多,弄个对象用用属性
# 配合 tail -f himi_log可以看运行了!!!! 哇我的最传统debug法error_log大法的python版本

content = file.read()
print(content)
# 这玩意没有输出
# 在 write 内容后，直接 read 文件输出会为空，是因为指针已经在内容末尾。
# http://www.runoob.com/python/file-methods.html


#输出当前指针位置
file.seek(os.SEEK_SET);
#设置指针回到文件最初
context = file.read();
print(context);

file.close();

'''
为了保证无论是否出错都能正确地关闭文件，我们可以使用 try ... finally 来实现：

try:
    f = open('/path/to/file', 'r')
    print f.read()
finally:
    if f:
        f.close()
但是每次都这么写实在太繁琐，所以，Python 引入了 with 语句来自动帮我们调用 close() 方法：

with open('/path/to/file', 'r') as f:
    print f.read()
这和前面的 try ... finally 是一样的，但是代码更佳简洁，并且不必调用 f.close() 方法
'''

#↑ 的没有试 就是try catch感觉应该会有用的就先存一下吧