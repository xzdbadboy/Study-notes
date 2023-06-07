# 指针移动的单位都是以bytes/字节为单位
# 只有一种特殊情况：
#       t模式下的read(n)，n代表的是字符个数


# f.seek(n,模式):n指的是移动的字节个数
# 模式：(0,1,2)

# 0：参照物是文件开头位置
# f.seek(9, 0)
# f.seek(3, 0)  # 3

# 1：参照物是当前指针所在位置
# f.seek(9, 1)
# f.seek(3, 1)  # 12

# 2：参照物是文件末尾位置
# f.seek(-9, 2)  # 3
# f.seek(-3, 2)  # 9

# 强调：只有0模式可以在t下使用，1、2必须在b模式下用

# f.tell() # 获取文件指针当前位置

# 示范

# with open(r'aaa.txt', mode='rb') as f:
#     f.seek(9, 0)
#     f.seek(3, 0)  # 3
#     print(f.tell())
#     res=f.read()
#     print(res.decode('utf-8'))



# with open(r'aaa.txt', mode='rb') as f:
#     f.seek(9, 1)
#     f.seek(3, 1)  # 3
#     print(f.tell())
#     res=f.read()
#     print(res.decode('utf-8'))

# with open(r'aaa.txt', mode='rb') as f:
#     print(len(f.read()))
#     f.seek(-3, 2)
#     print(f.tell())
#     res=f.read()
#     print(res.decode('utf-8'))
#     f.seek(-6, 2)  # 3
#     print(f.tell())
#     res=f.read()
#     print(res.decode('utf-8'))


