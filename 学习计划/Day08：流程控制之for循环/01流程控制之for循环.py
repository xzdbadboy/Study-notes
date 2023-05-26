"""
1、什么是for循环？
    循环就是重复做某件事，for循环是python提供的第二种循环机制
2、为何要有for循环？
    理论上for循环能做的事情，while循环都可以做
    之所有要有for循环，，一定是for循环在循环取值（遍历取值）比while更简洁

3、如何使用for循环？
    语法：
    for 变量名 in可迭代对象：    # 可迭代对象可以是：列表、字典、字符串、元组、集合
        代码1
        代码2
        代码3
        ...
"""

# 一、语法
# 案例1：列表循环取值
# 简单版：
# for x in ['alex_dsb', 'lxx_dsb', 'egon_nb']:
#     print(x, end=' ')

# 复杂版：
# list1 = ['alex_dsb', 'lxx_dsb', 'egon_nb']
# i = 0
# while i < 3:
#     print(list1[i], end=' ')
#     i += 1

# 案例2：字典循环取值
# 简单版：
# dic = {'k1': 'alex_dsb', 'k2': 'lxx_dsb', 'k3': 'egon_nb'}
# for x in dic:
#     print(x, dic[x])
# 复杂版：while循环可以遍历字典，但是太麻烦了

# 案例3：字符串循环取值
# 简单版
# msg = 'you can you up, no can no bb'
# for k in msg:
#     print(k)

# 二、总结for循环和while循环的异同
# 1、相同之处：都是循环、for循环可以干的事儿，while循环也可以干
# 2、不同之处：
#   while循环称之为条件循环，循环次数取决于条件何时变为False
#   for循环称之为取值循环，循环次数取决于in后面包含的值的个数
# range功能介绍

# for i in range(3):
#     print('------>')

# for+break 同 while+break
# for+else 同 while+else

# 三、 for+continue
# for i in range(6):
#     if i == 4:
#         continue
#     print(i)

# 四、for循环嵌套：外层循环一次，内存循环需要完成的循环完毕
# for i in range(3):
#     print('外层循环--->', 3)
#     for j in range(5):
#         print('内存循环-->', j)
# 补充：终止for循环只有break一种方案
