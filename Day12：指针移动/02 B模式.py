"""
t:
    1、读写都是以字符串为单位
    2、只能针对文本文件
    3、必须指定字符编码


"""

# 循环读取文件

# 方式一：自己控制每次读取数据的数据量
with open(r'test.jpg', mode='rb') as f:
    while True:
        res = f.read(1024)
        if len(res) == 0:
            break
        print(len(res))

# 方式二：以行为单位读，当一行内容过长时会导致一次性读入内容的数据量过大
with open(r'a.txt', mode='rt', encoding='utf-8') as f:
   for line in f:
       print(line)