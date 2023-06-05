# 文件对象又称为文件句柄

with open('a.txt', mode='rt') as f1, open('b.txt', mode='rt') as f2:
    res1 = f1.read()
    res2 = f2.read()
    print(f1)
    print(f2)
    print(res1)
    print(res2)