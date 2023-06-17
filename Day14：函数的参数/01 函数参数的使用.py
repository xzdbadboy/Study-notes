# 一、形参与实参介绍
# 形参：在定义函数阶段定义的参数称之为形式参数，简称形参，相当于变量名
# def func(x, y):
#     print(x, y)


# 实参：在调用函数阶段传入的值称之为实际参数，简称实参，相当于变量值
# func(1, 2)

# 形参与实参的关系：
# 1、在调用阶段，实参（变量值）会绑定给形参（变量名）
# 2、这种绑定关系只能在函数内使用
# 3、实参与形参的绑定关系在函数调用时生效，函数调用结束后解除绑定关系

# 实参是传入的值，但值可以是以下形式
# 形式一：
# func(1,2)

# 形式二：
# a = 1
# b = 2
# func(a, b)

# 形式三：
# func(int('1'), 2)

# 二、形参与实参的具体使用
# 2.1 位置参数：按照从左到右的顺序依次定义的参数称之为位置参数
# 位置形参：在函数定义阶段，按照从左到右的顺序直接定义的”变量名“
#    特点：必须被传值，多一个不行少一个不行


# 位置实参：在函数调用阶段，按照从左到右的顺序依次传入的值
#    特点：按照顺序与形象一一对应


# 2.2 关键字参数
# 关键字实参：在函数调用阶段，按照key=value的形式传入的值
#      特点：指名道姓的给某个形参传值，可以完全不参照顺序
# def func(x, y):
#     print(x, y)

# func(y=2, x=1)

# 混合使用，强调
# 1、位置实参必须放在关键字实参前
# func(2, y=1)
# func(x=2, 1)  # 错误

# 2、不能为同一个形参重复传值
# func(2, y=1, x=3)


# 2.3 默认参数
# 默认形参：在定义函数阶段，就已经被赋值的形参，称之为默认参数
#    特点：在定义阶段就已经被赋值，意味着在调用阶段可以不用为其赋值
# def func(x, y, z=3, i=2):
#     print(x, y, z, i)
#
#
# func(1, 9)
# 位置形参与默认形参混用，强调：
# 1、位置形参必须在默认形参的左边

# 2、默认参数的值是在函数定义阶段被赋值的，准确地说被赋予的是值的内存地址

# 示范1
# m=2
# def func(x,y=m):
#     print(x,y)
#
# m=3333333
# func(1)

# 示范2
# m = [333, ]
#
#
# def func(x, y=m):
#     print(x, y)
#
#
# m.append(3523)
# func(1)

# 3、虽然默认值可以被指定为任意数据类型，但是不推荐使用可变类型
# 函数的定义

# def func1(x, y, z, l=None):
#     if l is None:
#         l = []
#     l.append(x)
#     l.append(y)
#     l.append(z)
#     print(l)
#
#
# new_l = [11, 22]
# func1(1, 2, 3, new_l)

# 2.4 可变长度的参数（*与**的用法）
# 可变长度指的是在调用函数时，传入的值（实参）的个数不固定
# 而实参是用来为形参赋值的，所以对应着，针对溢出的实参必须有对应的形参来接受


# 2.4.1 可变长度的位置参数
# I:*形参名：用来接受溢出的位置实参，溢出的位置实参会被*保存成元组的形式
#        * 后跟的是任意一个名字，但是约定俗成是args

# def func (x,y,*z):
#     print(x,y,z)
#
# func(1,2,3,4,5,6)

# 应用
# def my_sum(*args):
#     res = 0
#     for item in args:
#         res += item
#     return res
#
#
# print(my_sum(2, 4, 3, 53, 324, 2))

# II：*可以用在实参中，实参中带*，先将*后的值打散（类似for循环）成位置实参
# def func(x, y, z):
#     print(x, y, z)
#
#
# func(*[11, 22, 33])

# III：形参和实参中都带*
# def func(x, y, *args):
#     print(x, y, args)
#
#
# func(1, 2, *[3, 4, 5, 6])

# 2.4.2 可变长度的关键字参数
# I:**形参名：用来接受溢出的关键字实参，**会将溢出的关键字实参会保存成字典格式，然后会赋值给紧跟其后的形参名
#        ** 后跟的是任意一个名字，但是约定俗成是kwargs

# def func(x, y, **kwargs):
#     print(x, y, kwargs)
#
#
# func(1, y=2, z=2, a=13, c=4, b=5)


# II：**可以用在实参中（**后跟的只能是字典），实参中带**，先将**后的值打散成关键字实参
# def func(x, y, z):
#     print(x, y, z)
#
#
# func(**{'x': 4, 'y': 2, 'z': 3})


# III：形参和实参中都带**
# def func(x, y, **kwargs):
#     print(x, y, kwargs)
#
#
# func(**{'x': 1, 'y': 2, 'z': 3, 'a': 5})



# 混用*与**
# *args必须在**kwargs之前



# 2.5 命名关键字参数
# 2.6 组合使用
