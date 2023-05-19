



# 需求：
# 1、拷贝一个原列表产生一个新的列表
# 2、想让两个列表完全独立开来，针对的是改操作独立而不是读操作

# 3、如何copy列表
# 3.1 浅copy：是把原列表第一层的内存地址完全copy
# list1 = [
#     'egon',
#     'lxx',
#     [1, 2]
# ]

# list2=list1.copy()
# print(list2)
# print(id(list1))
# print(id(list2))
# 3.2 深copy
import copy
list1 = [
    'egon',
    'lxx',
    [1, 2]
]

list3 =copy.deepcopy(list1)
print(list3)