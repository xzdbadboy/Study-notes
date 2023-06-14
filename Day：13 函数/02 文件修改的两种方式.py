# 方式一：
# 实现思路：将文件内容发一次性全部读入内存,然后在内存中修改完毕后再覆盖写回原文件
# 优点: 在文件修改过程中同一份数据只有一份
# 缺点: 会过多地占用内存
with open('db.txt',mode='rt',encoding='utf-8') as f:
    data=f.read()

with open('db.txt',mode='wt',encoding='utf-8') as f:
    f.write(data.replace('kevin','SB'))

# 方式二：

import os

with open('db.txt',mode='rt',encoding='utf-8') as read_f,\
        open('.db.txt.swap',mode='wt',encoding='utf-8') as wrife_f:
    for line in read_f:
        wrife_f.write(line.replace('SB','kevin'))

os.remove('db.txt')
os.rename('.db.txt.swap','db.txt')