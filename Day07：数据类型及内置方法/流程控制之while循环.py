# 1、循环的语法与基本使用
"""
while 条件:
     代码1
     代码2
     代码3

"""
# count = 0
# while count < 5:
#     print(count)
#     count += 1
# print('顶级代码------>')

# 2、死循环与效率问题
# while True:
#     1+1

# 3、循环的应用
username = 'juake'
userpwd = '123f'

# 两个问题：
# 1、重复代码
# 2、输对了应该不用重复

# count = 0
# while 1:
#     inp_name=input('请输入您的账号：')
#     inp_pwd=input('请输入您的密码：')
#     if inp_name == username and inp_pwd == userpwd:
#         print('登录成功')
#         break
#     elif inp_name != username or inp_pwd != userpwd:
#         count += 1
#         print('账号或密码错误。')
#     elif count == 4:
#         print('输入次数太多，请明天再试')
#         break
# print('真棒')
# count = 0
# while count <3:
#     inp_name=input('请输入您的账号：')
#     inp_pwd=input('请输入您的密码：')
#     count += 1
#     if inp_name == username and inp_pwd == userpwd:
#         print('登录成功')
#         break
#     elif count == 4:
#         print('输入次数太多，请明天再试')
#         break
#     elif inp_name != username or inp_pwd != userpwd:
#         print('账号或密码错误。')
#         print(count)
# print('真棒')

# count = 6
# while count >= -1:
#     inp_name = input('请输入您的账号：')
#     inp_pwd = input('请输入您的密码：')
#     count -= 1
#
#     if inp_name == username and inp_pwd == userpwd:
#         print('登录成功')
#         while True:
#             inp_cmd = input("输入命令的编号>：")
#             if inp_cmd == '':
#                 print('命令不能为空，请重新输入')
#             elif inp_cmd == 'q':
#                 print('终止命令已接受')
#                 break
#             else:
#                 print('命令{y}正在运行'.format(y=inp_cmd))
#         break
#     elif 1 <= count <= 3:
#         print('你还有{x}次输入机会。'.format(x=count))
#     elif count == 0:
#         print('输入次数太多，请明天再试')
#         break
#     elif inp_name != username or inp_pwd != userpwd:
#         print('账号或密码错误。')
# print('真棒')


# 4、退出循环的两种方式
# 方式一：将条件改为False，等到下次循环判断条件时才会生效
# 方式二：break

# 5、while循环嵌套

# 每一次都必须配一个break
"""
while True:
    while True:
        while True:
            break
        break
    break
"""

# 修改条件，直接终止
"""
tag = True
while tag:
    while tag:
        while tag:
            tag =False
"""
# 6、while+continue
# 在continue之后添加同级代码毫无意义，因为永远无法运行
# count = 0
# while count < 6:
#     count += 1
#     if count == 4:
#         continue
#     print(count)
#
# count1 =0
# while count1 < 6:
#     if count1 ==4:
#         count1 += 1
#         continue
#     print(count1)
#     count1 += 1

# 7、while+else
# while True:
#     ..
# else:
#     print('else包含的代码会在while循环结束后，并且while循环在没有被break打断的情况才会运行')

