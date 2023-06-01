# 1、作用


# 2、定义:{}内用逗号分隔开多个key:value,其中value可以使用任意类型，但是key必须是不可变类型且不可重复
# d={'a1': 111, 'a2': 222}
# print(type(d))

# d={} # 默认定义出来的是空字典
# print(type(d))

# d = dict(x=1, y=2, z=3)
# print(d, type(d))

# 3、数据类型转换
# info = [
#     ['name', 'juake'],
#     ('age', 18),
#     ['gender', 'male']
# ]

# d = {}
# for item in info:
#     d[item[0]] = item[1]
# print(d)

# res = dict(info)
# print(res)

# 造字典的方式:快速初始化字典
# keys = ['name', 'age', 'gender']
# value = None

# d={}
# for k in keys:
#     d[k]=None
# print(d)

# d = {}.fromkeys(keys, None)
# print(d)

# 4、内置方法
# 优先掌握的操作：
# 1、按key存取值：可存可取
# d = {'k1': 111}
# 针对赋值操作：key存在，则修改
# d['k1'] = 2222
# print(d)
# 针对赋值操作：key不存在，则创建新值
# d['k2'] = 333
# print(d)

# 2、长度len
# d = {'k1': 111,'k2':222,'k1':3333,'k2':4444}
# print(d,len(d))

# 3、成员运算in和not in

# 4、删除
# d = {'k1': 1111, 'k2': 2222, 'k3': 33333, 'k4': 4444}
# 4.1 通用删除方法
# del d['k1']
# print(d)

# 4.2 pop删除:根据key删除元素，返回删除key对应的那个value值
# res = d.pop('k1')
# print(res, '\n', d)

# 4.3 popitem删除：随机删除，返回元组（删除的key，删除的value）
# res = d.popitem()
# print(res, '\n', d)

# 5、键keys()，值values()，键值对items()
# d = {'k1': 1111, 'k2': 2222, 'k3': 33333, 'k4': 4444}

# 6、循环
# for k in d.keys():
#     print(k)

# for item in d.items():
#     print(item)

# 其他需要掌握的内置方法
d = {'k1': 1111, 'k2': 2222, 'k3': 33333, 'k4': 4444}

# 1、清空字典
# d.clear()
# print(d)

# d.update()
# d.update({'k5':555,'k2':2121})
# print(d)

# d.get()  根据key取值，容错性好
# print(d['k6'])  # key 不存在则报错

# print(d.get('k1'))
# print(d.get('k5'))  # key不存在不报错，返回None

# d.setdefault()  #如果key有则不添加，返回字典中对应的值；没有则添加
d.setdefault('k7',6232666)
print(d)