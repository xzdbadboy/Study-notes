# 1、通用文件copy工具实现
# import os
#
# while True:
#     source_file = input('请输入源文件地址：').strip()
#     # print(os.path.exists(source_file))
#     if not os.path.exists(source_file):
#         print('文件路径输入错误，请重新输入！')
#         continue
#     dst_file = input('请输入目标文件地址：').strip()
#     with open(source_file, mode='rb') as f_r, open(dst_file, mode='wb') as f_w:
#         for line in f_r:
#             f_w.write(line)
#         print('文件拷贝完成')
#     break

# 2、基于seek控制指针移动，测试r+\w+\a+模式下的读写内容

# r+：可读可写

# with open('test.txt',mode='r+',encoding='utf-8') as f:
#     f.seek(6)
#     res = f.read(4)
#     print(res)
#     f.write('alex')

# w+：可读可写，每次都会清空，无法读取文件中的内容

# with open('test.txt', mode='w+', encoding='utf-8') as f:
#     res = f.read()
#     print(res)

# a+：可读可写，无论是a或者a+模块，追加时都会从末尾追加，指针移动无效

# with open('test.txt', mode='a+', encoding='utf-8') as f:
#     f.seek(6)
#     res = f.read(4)
#     print(res)


# 3、tail -f access.log程序实现

# import time
#
# with open(r'access.log', mode='rb') as f:
#     f.seek(0, 2)
#     while True:
#         line = f.readline()
#         if line:
#             print(line.strip().decode('utf-8'))
#         else:
#             time.sleep(0.2)

# 4、周末作业参考老师在讲解完毕后，练习熟练
# 4.1：编写用户登录接口
# 4.2：编写程序实现用户注册后（注册到文件中），可以登录（登录信息来自文件）


# 方式一
# user_name = input('请输入用户名：').strip()
# user_pwd = input('请输入密码：').strip()
#
# with open('db.txt', mode='a+t', encoding='utf-8') as date:
#     date.seek(0)
#     for line in date:
#         db_user_name, db_user_pwd = line.strip().split(':')
#         if user_name == db_user_name and user_pwd == db_user_pwd:
#             print('longin success!')
#             break
#     else:
#         date.write(user_name + ':' + user_pwd + '\n')
#         print('Account registration successful!')


# 方式二
user_info = {}
with open('db.txt', 'r', encoding='utf-8') as f:
    for line in f:
        db_user_name, db_user_pwd = line.strip().split(':')
        user_info[db_user_name] = db_user_pwd
while True:
    user_name = input('请输入用户名：').strip()
    if user_name not in user_info:
        user_pwd = input('请输入密码：').strip()
        re_user_pwd=input('请再次输入密码：').strip()
        if user_pwd==re_user_pwd:
            with open('db.txt', mode='a+t', encoding='utf-8') as date:
                # date.write(user_name + ':' + user_pwd + '\n')
                date.write(f'{user_name}:{user_pwd}\n')
                print('Account registration successful!')
                break
        else:
            print('两次密码不一致，请重新输入！')
            continue
    else:
        user_pwd = input('请输入密码：').strip()
        if user_pwd == user_info[user_name]:
            print('longin success!')
            break
        else:
            print('账号或密码错误，请重新输入！')
            continue
