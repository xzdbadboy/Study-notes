# 1、作用：按位置存放多个值
# 2、定义
# 3、类型转换：但凡能够被for循环遍历的类型都可以当做参数传给list()转成列表
# res = list('hello')
# print(res)
#
# res1 = list({'k1': 111, 'k2': 222, 'k3': 333})
# print(res1)

# 4、内置方法
# 优先掌握的操作：
# 4.1按索引存取值(正向存取+反向存取)：即可存也可以取
# l = [111, 'juake', 'hello']
# 正向取
# print(l[0])
# 反向取
# print(l[-2])
# 可以取也可以改
# l[0] = 222
# print(l)
# 索引不存在则报错

# 4.2切片(顾头不顾尾，步长)
# l = [111, 'juake', 'hello', 'a', 'b', 'c', 'd', 'e']
# print(l[0:2])
# print(l[0:5:2])
# print(l[:])
# new_l = l[:]  # 切片等于拷贝行为，相当于浅copy
# print(id(l))
# print(id(new_l))
#
# l=l[::-1]
# print(l)

# 4.3长度
# print(len([1,2,3,4]))

# 4.4成员运算in和not in

# 4.5.1追加
# l = [111, 'juake', 'hello']
# l.append(3333)
# print(l)

# 4.5.2插入值
# l = [111, 'juake', 'hello']
# l.insert(0, 'alex')
# print(l)

# 4.5.3 extend
# new_l =[1,2,3]
# l = [111, 'juake', 'hello']
# l.extend(new_l)
# print(l)

# 4.6删除
# 方式一:通用的删除方法，没有返回值
# l = [111, 'juake', 'hello']
# del l[1]
# print(l)

# 方式二：l.pop根据索引删除,会返回删除值
# l = [111, 'juake', 'hello']
# # l.pop()  # 不指定索引，默认删除最后一个
# res=l.pop(1)
# print(res)

# 方式三 l.remove() 根据元素删除，返回None
# l = [111, 'juake', 'hello']
# l.remove('juake')


# 4.7循环
# for x in [1,'aaa','bbb']:
#     print(x)

# 需要掌握的操作
# l= [1,'aaa','bbbb','aaa','aaa','aaa']
# 1、l.count()
# print(l.count('aaa'))

# 2、l.index()
# print(l.index('aaa'))

# 3、l.clear()
# l.clear()
# print(l)

# 4、l.reverse()  不是排序，就是列表倒过来
# l.reverse()
# print(l)

# 5、l.sort() 列表内元素必须是同种类型才可以排序
# l = [11, 2, -3, 9.6, 5]
# l.sort() #默认从小到大排，称之为升序
# l.sort(reverse=True)  # 从大到小排，设置为降序
# print(l)

# 了解：字符串也可以比大小，按照对应位置的字符一次PK
# 字符串的大小是按照ASCII码的先后顺序区别字符的大小，表中排在后面的字符大于前面的

# 了解：列表之间也可以比大小，原理同字符串一样

# 补充
# 1、队列：FIFO,(first in first out,先进先出）
# # 入队操作
# l=[]
# l.append('first')
# l.append('second')
# l.append('third')
# print(l)
#
# # 入队操作
# print(l.pop(0))
# print(l.pop(0))
# print(l.pop(0))
# print(l)

# 2、堆栈：LIFO，后进后出
# 入栈操作
l=[]
l.append('first')
l.append('second')
l.append('third')
print(l)

# 出栈操作
print(l.pop())
print(l.pop())
print(l.pop())
print(l)








