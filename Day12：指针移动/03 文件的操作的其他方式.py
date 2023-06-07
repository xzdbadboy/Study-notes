# 一、读相关
# 1、readline: 一次读一行

# 2、readlines:

# 强调：
# f.read()和f.readlines()都是将内容一次性写入内存，如果内容过大会导致内存溢出，若还想将内容读入内存，必须分多次读入

# 二、写相关操作
# f.writelines():
# with open(r'h.txt', mode='wt', encoding='utf-8') as f:
#     l = ['1111\n', '2222', '3333']
#     # for line in l:
#     #     f.write(line)
#     f.writelines(l)


# with open(r'a.txt', mode='wb') as f:
# l = [
# '1111\n'.encode('utf-8'),
#      '2222'.encode('utf-8'),
#      '3333'.encode('utf-8')
#      ]
# for line in l:
#     f.write(line)

# 补充一：如果是纯英文字符，可以直接加前缀b得到bytes类型
# l = [b'1111aa\n',
#      b'2222bbb',
#      b'3333nnn'
#      ]

# 补充二：
# l = [
#     bytes('上啊', encoding='utf-8'),
#     bytes('冲啊', encoding='utf-8'),
#     bytes('小垃圾们', encoding='utf-8'),
# ]
#
# f.writelines(l)

# 3、flush：
# with open(r'b.txt', mode='wt', encoding='utf-8') as f:
#     f.write('哈哈哈哈')
#     f.flush()

# 4、了解
with open(r'c.txt', mode='wt', encoding='utf-8') as f:
    print(f.readable())
    print(f.writable())
    print(f.encoding)
    print(f.name)