# 1、可变不可变类型

# 可变类型：值可变，id不变，证明改的是原值，证明原值是可以被改变的。
# 不可变类型：值改变，id也变了，证明是产生了新的值，压根儿没有改变原值，证明原值是不可以被修改的。

# 2、验证
# 2.1 int是不可改变类型
x = 10
print(id(x))
x = 11  # 产生新值
print(id(x))

# 2.2 float是不可改变类型

xx = 10.3
print(id(xx))
xx = 11.345  # 产生新值
print(id(xx))

# 2.3 str是不可改变类型
xxx = 'asdf'
print(id(xxx))
xxx = 'asd'  # 产生新值
print(id(xxx))

# 小结：int|float|str都被设计成了不可分割的整体，不能够被改变。

# 2.4 list是可变类型

l2 = ['aaa', 'bbb', 'ccc']
print(l2)
print(id(l2))
l2[0] = 'AAA'
print(l2)
print(id(l2))

# 2.5 dict是可变类型
dic = {'xxx': 123, 'yyy': 1258}
print(dic)
print(id(dic))
dic['xxx'] = 685
print(dic)
print(id(dic))

# 2.6 bool不可变

# 关于字典补充：
# 定义：{}内用逗号分隔开多key：value，
#           其中value可以是任意类型
#           但是key必须是不可变类型
dictionary = {
    'k1': 111,
    'k2': 11.1,
    'k3': [11.1, 535],
    'k4': {'name': 'jauke', 'age': 35}
}
print(dictionary)
