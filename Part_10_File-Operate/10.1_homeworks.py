# encoding: utf-8
filename = 'Text_files/Love_python.txt'

# 第一次打印读取整个文件
with open(filename) as file_object:
    content = file_object.read()

print(content.rstrip())
print("-----------------")

# 第二次打印时遍历文件对象
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
        # rstrip()方法清除空行
print("-----------------")

# 第三次打印时将各行存储在一个列表中，再在with代码块外打印它们
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
print("-----------------")

# 用'C++'替换'Python'
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.replace('Python', 'C++')
    print(line.rstrip())
