# 2、写函数，计算传入字符串中【数字】、【字母】、【空格】以及【其他】的个数
# def count(x):
#     dic = {
#         'number': 0,
#         'letters': 0,
#         'black': 0,
#         'other': 0
#     }
#     for line in x:
#         if line.isdigit():  # 判断是否为数字
#             dic['number'] += 1
#         elif line.isalpha():  # 判断是否为字母
#             dic['letters'] += 1
#         elif line.isspace():  # 判断是否为空格
#             dic['black'] += 1
#         else:
#             dic['other'] += 1
#     return dic
#
#
# res = count('asdf *--*561   +*-456`123fasdf')
# print(res)

# 3、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
# def check_length(obj):
#     if len(obj) > 5:
#         print(f'{obj}的长度大于5')
#     else:
#         print('太短了。')
#
#
# check_length('你好啊。！！')

# 4、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者
# def get_odd_element(list_tuple):
#     return list_tuple[1::2]
#
#
# res = get_odd_element([123, 14, 235, 234, 235, 1, 45, 6, 342, 42, 1, 55])
# print(res)

# 5、写函数，检查字典的每一个value的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者
# Ps：字典中的value职能是字符串或列表

def check_dic(dic):
    for key, value in dic.items():
        if len(value) > 2:
            dic[key] = value[:2]
    return dic


dic = {'k1': 'gege', 'k2': [11, 22, 33, 44]}
res = check_dic(dic)
print(res)
