"""
今日内容
    1、集合类型
        关系运算
        去重（有局限性）
    2、总结与分类
        有序or无序：有序又称之为序列类型


        存一个值or多个值：存一个值成为原子类型，存多个值称为容器类型


        可变or不可变


    3、字符编码（理论多，结论少）
    4、文件处理基本基础
"""
# 1、作用

# friends1 = ["zero","kevin","jason","egon"]
# friends2 = ["Jy","ricky","jason","egon"]
#
# l=[]
# l1=[]
# for x in friends1:
#     if x in friends2:
#         l.append(x)
# print(l)


# 2、定义:在{}内用逗号分隔开多个元素，多个元素满足以下三个条件
# 1.集合内元素必须为不可变元素
# 2.集合内元素无序
# 3.集合内元素没有重复


# 3、类型转换
# l=set('heloooolow')
# print(l)


# 4、内置方法

# -------------------------------关系运算-------------------------------
# friends1 = {"zero", "kevin", "jason", "egon"}
# friends2 = {"Jy", "ricky", "jason", "egon"}

# 4.1 取交集：两者共同的好友
# res = friends1 & friends2
# print(res)
#
# print(friends1.intersection(friends2))

# 4.2 取并/合集：取两者所有的好友
# res1= friends1 | friends2
# print(res1)
#
# print(friends1.union(friends2))
# 4.3 取差集：取friends1独有的好友
# res = friends1 - friends2
# print(res)
#
# print(friends1.difference(friends2))

# 4.4 对称差集：两者独有的好友
# res1= friends1 ^ friends2
# print(res1)
#
# print(friends1.symmetric_difference(friends2))

# 4.5 父子集：包含的关系
# s1 = {1, 2, 3}
# s2 = {1, 2}
# print(s1 > s2)
#
# print(s1.issuperset(s2))
# print(s2.issuperset(s1))

# -------------------------------去重-------------------------------
# 1.只能针对不可变类型去重


# 2.无法保证原来的顺序

# l=[
#     {'name':'lili','age':18,'sex':'male'},
#     {'name':'jack','age':73,'sex':'male'},
#     {'name':'tom','age':20,'sex':'female'},
#     {'name':'lili','age':18,'sex':'male'},
#     {'name':'lili','age':18,'sex':'male'},
# ]
# new_l =[]
# for dic in l:
#     if dic not in new_l:
#         new_l.append(dic)
# print(new_l)

# 其他内置方法

# s = {1, 2, 3, 4}

# 需要掌握的内置方法1： discard
# s.discard(5)   # 删除元素不存在什么都不做
# print(s)
#
# s.remove(5) # 删除元素不存在会报错


# 需要掌握的内置方法2： update
# s.update({4,5,7,8})
# print(s)
#
# s1 = s.difference({3, 4, 5, 6, 7})
# print(s1)
# print(s)
#
# 需要掌握的内置方法3： pop

# 需要掌握的内置方法4： add

# s.isdisjoint()  # 两个集合完全独立、没有共同部分，返回True
