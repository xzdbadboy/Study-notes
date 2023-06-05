# 以t模式为基础进行内存操作


# 1、r（默认的操作模式）：只读模式，当文件不存在时会报错
# inp_username = input('your name:')
# inp_pwd = input('your password:')
#
# with open('user.txt', mode='rt', encoding='utf-8') as f:
#     for line in f:
#         username, password = line.strip().split(':')
#         if inp_username == username and inp_pwd == password:
#             print('login successful')
#             break
#     else:
#         print('账号或密码错误')

# 应用程序  ------>    文件
# 应用程序  ------>    数据库管理软件  ------>    文件

# 2、w：只写模式，当文件不存在时会创建空文件，当文件存在时会清空文件，指针位于开始位置
# with open('d.txt', mode='wt', encoding='utf-8') as f:
#     f.write('haha\n')
#     f.write('haha1\n')
#     f.write('haha2\n')
#     f.write('haha3\n')

# 强调1：
# 在以w模式打开没有关闭的情况下，连续写入，新都内容总是跟在旧内容之后


# 强调2：
# 如果重新以w模式打开文件，则会清空文件内容

# 3、a：只追加写，在文件不存在时会创建空白档，在文件存在时会直接跳到末尾
# with open('e.txt', mode='at', encoding='utf-8') as f:
#     f.write('擦嘞1\n')


# 强调 w 模式与 a 模式的异同：
# 1、相同点：在打开的文件不关闭的情况下，连续地写入，新写的内容总会跟在前写的内容之后
# 2、不同点：以 a 模式重新打开文件，不会清空原文件内容，会将文件指针直接移动到文件末尾，新写的内容永远写在最后

# 注册功能

name = input('your name:')
pwd = input('your password:')
with open('db.txt', mode='at', encoding='utf-8') as f:
    f.write('{}:{}\n'.format(name, pwd))
