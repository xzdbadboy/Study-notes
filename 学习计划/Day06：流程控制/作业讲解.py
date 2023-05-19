# 作业（必做题）
# 1、使用while循环输出1 2 3 4 5 6     8 9 10

# count = 1
# while count < 11:
#     if count == 7:
#         count += 1
#         continue
#     print(count)
#     count += 1

# 2、求1-100的所有数的和

# count = 1
# sum_count = 0
# while count <= 100:
#     sum_count = sum_count + count
#     count += 1
# print('1-100的所有的数和等于：{x}'.format(x=sum_count))

# 3、输入1-100内的所有奇数
# 4、输入1-100内的所有偶数

# count = 0
# odd_number_sum = 0
# even_number_sum = 0
# while count <= 99:
#     count += 1
#     if count % 2 == 0:
#         even_number_sum = even_number_sum + count
#     else:
#         odd_number_sum = odd_number_sum + count
# print('1-100内的所有奇数的和是:{x}\n1-100内的所有偶数的和是:{y}'.format(x=even_number_sum, y=odd_number_sum))

# 5、求1-2+3-4+5...99的所有数的和

# count =0
# count_sum =0
# while count <= 99:
#     count += 1
#     if count % 2 == 0:
#         count_sum = count_sum - count
#     else:
#         count_sum = count_sum + count
# print('1-2+3-4+5...99的所有数的和是：{x}'.format(x=count_sum))


# 6、用户登录（三次机会重试）

# username = 'juake'
# userpwd = '123'
# count = 0
# while count < 3:
#     inp_name = input('请输入您的账号：')
#     inp_pwd = input('请输入您的密码：')
#     count += 1
#     if inp_name == username and inp_pwd == userpwd:
#         print('登录成功')
#         break
#     elif inp_name != username or inp_pwd != userpwd:
#         print('账号或密码错误')
# print('输入次数太多，请明天再试')

# 7、猜年龄游戏
#    要求：
#    允许用户最多尝试3次，3次都没有猜对的话，就直接退出，如果猜对了，打印恭喜信息并退出

# import random
# random_int = random.randint(1,1000)
# count = 0
# while count < 3:
#     count +=1
#     print('第{x}次尝试'.format(x=count))
#     input_num = int(input('请输入您猜的数字：'))
#     if input_num == random_int:
#         print(f'恭喜您，猜对了，数字就是{random_int}')
#         break
# else:
#     print(random_int)

# 8、猜年龄游戏（选做题）
#    要求：
#    每尝试3次后，如果还没有猜对，就问用户是否还想继续玩，如果回答y或Y，就继续让其猜3次，如果回答n或者N就退出游戏
#    如果猜对了，就直接退出

# v 1.0
# import random
#
# random_int = random.randint(1, 1000)
# count = 0
# while count < 5:
#     count += 1
#     if count == 4:
#         print('还要继续玩吗？是请输入Y or y，退出请输入N or n')
#         input_order = input('请输入：')
#         if input_order == 'Y' or input_order == 'y':
#             count = 0
#             continue
#         elif input_order == 'N' or input_order == 'n':
#             break
#     print('第{x}次尝试'.format(x=count))
#     input_num = int(input('请输入您猜的数字：'))
#     if input_num == random_int:
#         print(f'恭喜您，猜对了，数字就是{random_int}')
#         break

# v1.2
import random

random_int = random.randint(1, 1000)
tag =True
count = 0
while tag:
    count += 1
    if count <=3:
        print('第{x}次尝试'.format(x=count))
        input_num = int(input('请输入您猜的数字：'))
    elif input_num == random_int:
        print(f'恭喜您，猜对了，数字就是{random_int}')
        break
    if count == 4:
        print('还要继续玩吗？是请输入Y or y，退出请输入N or n')
        input_order = input('请输入：')
        if input_order == 'Y' or input_order == 'y':
            count = 0
            continue
        elif input_order == 'N' or input_order == 'n':
            break
        else:
            print('输入错误！')
            input_order = input('请输入：')
            print('请重新输入:{x}'.format(x=input_order))
            continue

