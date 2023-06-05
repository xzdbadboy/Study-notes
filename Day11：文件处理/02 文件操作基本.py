# 1、打开文件
# windows路径分隔符问题
# 解决方案一：推荐
# open(r'C:\b\n\a\d\d.txt')
# 解决方案二
# open(C:/x/df/er/f.txt)

f = open(r'aaa/a.txt', mode='rt', encoding='utf-8')  # f的值是一种变量，占用的是应用程序的内存空间
# print(f)

# 2、操作文件：读/写文件，应用程序对文件的读写请求都是在向操作系统发送系统调用，然后由操作系统控制硬盘读入内存或者写入硬盘
res = f.read()
print(res)

# 3、关闭文件
f.close()
# del f



