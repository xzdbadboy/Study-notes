# 1、作用
# 2、定义
# msg = 'hello'
# print(type(msg))

# 3、类型转换

# 4、使用：内置方法
# 4.1优先掌握
# 4.1.1、按索引取值(正向取+反向取) ：只能取
# msg = 'hello world'
# # 正向取
# print(msg[0])
# print(msg[5])
# print(msg[6])
# # 反向取
# print(msg[-1])

# 4.1.2、切片：索引的一种拓展应用，从一个大的字符串中拷贝出一个子字符串(顾头不顾尾，步长)
# 顾头不顾尾
# res=msg[0:5]
# print(msg)
# print(res)

# 步长

# res=msg[0:5:2]
# print(res)

# 反向步长

# res=msg[6:0:-1]
# print(res)

# res = [:] # res = msg[0:11]
# print(res)

# res = msg[::-1] # 把字符串倒过来了
# print(res)

# 4.1.3、长度len

# msg = 'hello world'
# print(len(msg))

# 4.1.4、成员运算in和not in

# 4.1.5、移除字符串左右两侧的空白strip
# msg = '   juake     '
# res = msg.strip()  # 默认去掉空格
# print(res)  # 产生了新值
# print(msg)  # 旧值不会改变

# 了解：strip只取两边，不去中间
# msg = '****ju***ake****'
# print(msg.strip('*'))

# msg1='/*-*==*-/*juake*-/()'
# print(msg1.strip('*-/=()'))

# 应用
# inp_user=input('your name--->>:').strip()
# inp_pwd=input('your password--->>:').strip()

# 4.1.6、切分split  (默认分隔符是空格）

# info = 'jauke:18:male'
# lsit1=info.split(':')
# print(lsit1)

# 指定分割次数
# info = 'jauke:18:male'
# lsit1=info.split(':',1)
# print(lsit1)

# 4.1.7、循环
# info = 'jauke:18:male'
# for x in info:
#     print(x)

# 4.2 需要掌握
# 4.2.1 strip lstrip rstrip

# msg = '****ju***ake****'
# print(msg.strip('*'))
# print(msg.lstrip('*'))
# print(msg.rstrip('*'))

# 4.2.2 lower upper

# msg = 'AbbbCCC'
# print(msg.lower())  # 全部改为小写
# print(msg.upper())  # 全部改为大写

# 4.2.3 startswith endswith
# print("juake is good".startswith("juake"))
# print("juake is good".endswith("good"))

# 4.2.4 format
# res='{} {} {}'.format('egon',18,'male')
# print(res)
# res='{1} {0} {1}00
# res='{name} {age} {sex}'.format(sex='male',name='egon',age=18)
# print(res)

# 4.2.5split rsplit:将字符串切成列表
# info = "juake:18:male"
# print(info.split(':', 1))  # ['juake', '18:male']
# print(info.rsplit(':', 1))  # ['juake:18', 'male']

# 4.2.6 join:将列表拼接成字符串
# l = ['juake', '18','male']
# info = ' '.join(l)
# print(info)

# 4.2.7 replace
# msg = 'you can you up no can no bb'
# print(msg.replace('you', 'You'))
# print(msg.replace('you', 'You', 1))

# 4.2.8 isdigit
# 判断字符串是否有纯数字组成
# print('123'.isdigit())
# print('12 3'.isdigit())
# print('12.3'.isdigit())
# print('123sdf'.isdigit())

# 4.3 了解
# 4.3.1 find,rfind,index,rindex,count
# msg = 'hello juake hahahahahha'
# 找得到的情况是一样的
# print(msg.find('e'))  # 返回要查找的字符串在大字符串中的起始索引
# print(msg.find('juake'))  # 返回要查找的字符串在大字符串中的起始索引
# print(msg.index('e'))
# print(msg.index('juake'))
# 找不到的情况find返回（-1），index直接报错
# print(msg.find('x'))  # 找不到返回 -1
# print(msg.index('e')) # 找不到报错
# print(msg.count('a')) # 统计字符出现的次数

# 4.3.2 center,ljust,rjust,zfill
# print('juake'.center(50,'*'))
# print('juake'.ljust(50,'*'))
# print('juake'.rjust(50,'*'))
# print('juake'.zfill(50))

# 4.3.3 expandtabs
# msg = 'hello\tjuake\thahahahahha'
# print(msg.expandtabs(8)) #设置制表符代表的空格数为8

# 4.3.4 captalize,swapcase,title
# print('hello world'.capitalize()) #首字母大写
# print('Hello woRld'.swapcase()) #大小写反转
# print('hello world'.title()) #每个单词的首字母大写

# 4.3.5 is数字系列
# num1 = b'4'  # bytes
# num2 = u'4'  # unicode,python3中无需加u就是unicode
# num3 = '四'  # 中文数字
# num4 = 'Ⅳ'  # 罗马数字

# isdigit 只能识别num1 num2
# print(num1.isdigit())  # True
# print(num2.isdigit())  # True
# print(num3.isdigit())  # False
# print(num4.isdigit())  # False

# isnumberic  可以识别num2 num3 num4
# print(num2.isnumeric())  # True
# print(num2.isnumeric())  # True
# print(num3.isnumeric())  # True

# isdecimal 只能识别num2
# print(num2.isdecimal())  # True
# print(num3.isdecimal())  # False
# print(num4.isdecimal())  # False

# 4.3.6 is其他
# print('hello'.islower())
# print('heLlo'.isupper())
# print('hello world'.istitle())  # 每个单词的首字母大写为True
# print('156sdf'.isalnum())  # 字符串由字母或数字组成为True
# print('hello'.isalpha())  # 字符串由字母组成为True
# print('hello'.isspace())  #  字符串由空格组成为True
# print('hello'.isidentifier()) # 判断名字是否合法
