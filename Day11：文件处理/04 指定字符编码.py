
# linux系统默认utf-8
# windows系统默认gkb

with open('c.txt', mode='rt', encoding='utf-8') as f:
    res = f.read()
    print(res)
