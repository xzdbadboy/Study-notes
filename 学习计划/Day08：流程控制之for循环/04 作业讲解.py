# 一、for循环
# 1.1 for循环嵌套之打印99乘法表

# 方案1
"""
for x in range(1, 10):
    for y in range(1, x + 1):
        if x == y:
            print("%s X %s = %s" % (y, y, y * x))
            # print(y, 'x', x, '=', x * y, end=z)
        else:
            # print(y, 'x', x, '=', x * y, end='  ')
            print("%s X %s = %s" % (y, y, y * x), end='  ')
"""
# 方案2
for x in range(1, 10):
    for y in range(1, x + 1):
        print("%s X %s = %s" % (y, y, y * x), end='  ')
    print()

# 1.2 for循环嵌套之打印金字塔

"""
    *      
   ***     
  *****
 *******
*********

"""

# 方案一

numbers_of_layers = 5
for i in range(1, 2 * numbers_of_layers, 2):
    k = '*' * i
    print(k.center(2 * numbers_of_layers - 1, ' '))

# 方案二

# numbers_of_layers = 4  # 金字塔层数
#
# for current_number_of_layers in range(1, numbers_of_layers + 1):
#     for j in range(numbers_of_layers - current_number_of_layers):
#         print(' ', end='')
#     for k in range(1, current_number_of_layers * 2):
#         print('*', end='')
#     print()
