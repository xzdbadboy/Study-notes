# 1、接受用户的输入
# python3:input会将用户输入的所有内容都存成字符串类型

# username = input("请输入您的账号：")
# print(username, type(username))


# age = input("请输入您的年龄：")
# print(age, type(age))
# age = int(age)  # int只能将纯数字的字符串转成整型
# print(type(age))
# print(age > 18)


# 在python2中：
# raw_input():用法与Python3的input一模一样
# input()：要求用户必须输入一个明确的数据类型，输入的是什么类型，就存成什么类型

# 2、字符串的格式化输入
# 2.1 %
# 按照位置与%s一一对应，多一个不行，少一个不行
# msg="my name is %s, my age is %s" %('juake','18')
# print(msg)
# %s可以接受任意类型,%d只能接受int
# msg="my name is %(name)s, my age is %(age)s" %{'age':'18','name':'juake'}
# print(msg)

# 2.2 str.format 兼容性好
# msg='我的名字是 {},我的年龄是 {}.'.format('juake',18)
# print(msg)

# msg='我的名字是 {0}{0}{0},我的年龄是 {1}{1}.'.format('juake',18)
# print(msg)

# 打破位置的闲置，按照key=value传值

# msg = "my name is {name}, my age is {age}".format(age=18, name='juake')
# print(msg)

# 2.3 f  python3.5以后才推出
x=input('your name:')
y=input('your age:')
msg=f'我的名字是{x},我的年龄是{y}.'
print(msg)