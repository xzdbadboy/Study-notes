# 基本运算符

# 1、算数运算符

# print(10 / 3)  # 结果带小数
# print(10 // 3)  # 只保留整数部分
# print(10 % 3)  # 取摸、取余数
# print(10 ** 3)  # 取摸、取余数

# 2、比较运算符 >  >=  <=  ==  !=
# print(10 >3)
# print(10 == 10)
# print(10 >= 10)
# print(10 >= 3)

# name=input('your name:')
# print(name=='juake')

# 3、赋值运算符
# 3.1 =：赋值变量的赋值
# 3.2增量赋值
#
# age = 18
# age += 1 # age = age + 1
# print(age)

# 3.3链式赋值
# x = 10
# y = x
# z = y
# z = y = x = 11  # 链式赋值
# print(x, y, z)
# print(id(x), id(y), id(z))

# 3.4交叉赋值
# m = 10
# n = 20
# print(m, n)
# temp = m
# m = n
# n = temp
# print(m, n)
# m, n = n, m # 交叉赋值
# print(m, n)

# 3.5 解压赋值
salaries = [111, 222, 333, 444, 555]
# 把5个月的工资取出来分别赋值给不同的变量名
# mon0 = salaries[0]
# mon1 = salaries[1]
# mon2 = salaries[2]
# mon3 = salaries[3]
# mon4 = salaries[4]

# mon0, mon1, mon2, mon3, mon4 = salaries
#
# print(mon0, mon1, mon2, mon3, mon4)
# 取前三个值
# x, y, z, *_ = salaries # *会将没有对应关系的值存成列表赋值给紧跟其后的变量名，此处为_
# print(x, y, z)
# print(_)

# 取后三个值
# *_, x, y, z = salaries  # *会将没有对应关系的值存成列表赋值给紧跟其后的变量名，此处为_
# print(x, y, z)
# print(_)

# x, *_, y, z = salaries  # *会将没有对应关系的值存成列表赋值给紧跟其后的变量名，此处为_
# print(x, y, z)
# print(_)

# 解压字典默认解压出来的是key
x, y, z = dic = {'a': 1, 'b': 2, 'c': 3}
print(x, y, z)


# 比较运算符
# 逻辑运算符
#   not、and、or
#   区分优先级：not > and > or
# 成员运算符
# in
# 身份运算符
# is
