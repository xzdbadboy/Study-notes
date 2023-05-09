# 1、数字类型
# 1.1整型int
# 作用：记录年龄、身份证号等等
# 定义：
age = 18
# print(type(age))

# 浮点型float
# 作用：记录薪资、体重、身高等
# 定义：
salary = 3.8
height = 1.87
weight = 70.3
# print(type(weight))

# 数字类型的其他使用


# 2、字符串类型str
# 作用：记录描述性质的状态、名字、一段话
# 定义：用引号（'',"",''' ''',""" """）包含的一串字符
info = ''' dsf
        3165asdf
        asdf
        asdf
        asdf
        '''
# print(info)
# XXX #代表访问的变量名字
'xxx'  # 代表的是值

# 其他使用：
# 字符串的嵌套，注意：外层用单引号，内层应该用双引号，反之亦然。
# print("my name is 'egon'")
# print('my name is \'egon\'')  # \表示转义

# 3、列表：索引对应值，索引从0开始，0代表第一个
# 作用：按位置记录多个值，并且可以按照索引取指定位置的值

# 定义：在[]内用逗号分隔开多个任意类型的值，一个值称之为一个元素
# l=[10,3.1,'aaa',['bbb','ccc'],'dddd']
# print(l)
# print(l[3][1])

# info=['egon',18,'male']
# print(info[0])
# print(info[1])
# print(info[2])

# 4、字典类型：key引对应值，其中key通常为字符串类型，所以key对值可以有描述性的功能
# 作用：用来存多个值，每个值都有唯一一个key与之对应，key对值可以有描述性的功能
# 定义：在{}内用逗号分开各多个key：value
# 索引反映的是顺序、位置，对值没有描述
# d={'a':1,'b':2}
# print(type(d))
# print(d['a'])

# info={"nanme":'egon',
#       "age":18,
#       "gender":'male',
#       "salary":19
#       }
# print(info["salary"])

# 其他用途：
# students_info=[
#     第一个信息,
#     第二个信息,
#     第三个信息,
# ]

students_info = [
    {'name': 'egon', 'age': 18, 'gender': 'male'},
    {'name': 'egon1', 'age': 19, 'gender': 'male'},
    {'name': 'egon2', 'age': 18, 'gender': 'male'},
]
print(students_info[1]['age'])

# 六 布尔bool
# 6.1 作用
# 用来记录真假这两种状态
#
# 6.2 定义
# is_ok = True
# is_ok = False
# print(type(is_ok))
# 6.3 使用
# 通常用来当作判断的条件，我们将在if判断中用到它








