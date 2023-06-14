"""
1、什么是函数
    函数就相当于具备某个功能的工具
    函数的使用必须遵循一个原则：
        先定义
        后调用

2、为何要用函数
    ①组织结构不够清晰，可读性差
    ②代码冗余
    ③可维护性、扩展性差

3、如何用函数
        先定义
            三种定义方式
        后调用
            三种调用方式
        返回值
            三种返回值的形式

"""

# 1、先定义
# 定义的语法

"""
def 函数名(参数1,参数2,...):
    '''文档描述'''
    函数体
    return 值
"""


# 形式一:无参函数

# def func():
#     print('hahaha')
#
# func()

# 定义函数发生的事情
# 1、申请内存空间保存函数体代码
# 2、将上述内存地址绑定函数名
# 3、定义函数不会执行函数体代码，但是会检测函数体语法


# 调用函数发生的事情
# 1、通过函数名找到函数的内存地址
# 2、然后加括号就是在触发函数体代码的执行
# print(func1)

# 形式二：有参函数
# def func(x, y):
#     print(x, y)

# 形式三：空函数，函数体代码为pass
# def func(x, y):
#     pass

# 三种定义方式各用在何处
# 1、无参函数的应用场景

# def interactive():
#     name = input('username>>:')
#     age = input('userpwd>>:')
#     gander = input('gender>>:')
#     msg = '名字：{}，年龄{}，性别{}'.format(name,age,gander)
#     print(msg)
#
# interactive()

# 2、有参函数的应用场景

# def add(x, y):  # 参数 ---> 原材料
#     res = x + y
#     return res  # 返回值 --->  产品
#
#
# res = add(102, 45)
# print(res)

# 3、空函数的应用场景

# def auth_user():
#     """user authentication function"""
#     pass
#
#
# def download_file():
#     """download file function"""
#     pass
#
#
# def upload_file():
#     """upload file function"""
#     pass
#
#
# def ls():
#     """list contents function"""
#     pass
#
#
# def cd():
#     """change directory"""
#     pass


# 二、调用函数
# 1、语句的形式：只去调用函数，不做其他操作
# add(1,2)

# 2、表达式形式：
# def add(x, y):  # 参数 ---> 原材料
#     res = x + y
#     return res  # 返回值 --->  产品

# 赋值表达式
# res = add(1,2)
# print(res)
# 数学表达式
# res = add(1, 2) * 10
# print(res)

# 3、函数调用可以当做参数
# res = add(add(2, 3), 9)
# print(res)


# 三、函数返回值

# return是函数结束的标志，即函数体代码一旦运行到return会立刻终止函数的运行，并且会将本次return后的值当本次运行的结果返回
# 1、None：函数体内没有return或者return后没有定义值
# 2、返回一个值：return 值

# def func():
#     return 10
# func()

# 3、返回多个值：用逗号分隔开多个值，会被return返回成元祖

def func():
    return 10, 'aa', [1, 23, 3]


res = func()
print(res, type(res))














