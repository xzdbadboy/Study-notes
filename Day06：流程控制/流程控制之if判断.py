"""
语法1：

if 条件：
    代码1
    代码2
    代码3

"""

"""
语法2：

if 条件：
    代码1
    代码2
    代码3
else:
    代码1
    代码2
    代码3

"""

"""
语法3：

if 条件：
    代码1
    代码2
    代码3
elif:
    代码1
    代码2
"""

score = input('请输入您的成绩：')
score = int(score)
if score >= 90:
    print('优秀')
elif 80 <= score < 90:
    print('良好')
elif 70 <= score < 80:
    print('普通')
else:
    print('很差，小垃圾')