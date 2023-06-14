# 1、编写文件修改功能，调用函数时，传入三个参数（修改的文件路径、要修改的内容、修改后的内容）即可完成文件的修改

import os


def change_file(file_path, old_replace, new_replace):
    with open(file_path, mode='rt', encoding='utf-8') as f, \
            open('.test.txt.swap', mode='w+t', encoding='utf-8') as f1:
        for line in f:
            date = line.replace(old_replace, new_replace)
            f1.write(date)

    os.remove(file_path)
    os.rename('.test.txt.swap', file_path)


# change_file(r'F:\Study\Study-notes\Day：13 函数\test.txt', 'tank3', 'egon')


