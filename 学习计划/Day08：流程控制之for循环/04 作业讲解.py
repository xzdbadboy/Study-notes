# 一、for循环
# 1.1 for循环嵌套之打印99乘法表

for x in range(1, 10):
    for y in range(1, x + 1):
        if x == y:
            z = '\n'
            print(y, 'x', x, '=', x * y, end=z)
        else:
            print(y, 'x', x, '=', x * y, end='  ')

# 1.2 for循环嵌套之打印金字塔

"""
    *      
   ***     
  *****
 *******
*********

"""
j = 1
k = '*'
for i in range(1, 6):

    print(k.center(9, ' '))
    k = '*'
    j += 2
    k *= j