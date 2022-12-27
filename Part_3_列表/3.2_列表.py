#列表输出第一次接触的编程语言
Language = ['java', 'c', 'python', 'php']
print(Language)
print(Language[0])
print(Language[2])
message = f"The first Program Language I learned is {Language[0].upper()}"
print(message)

print("-----------分割线------------")
name = ['yjh', 'dwh', 'ysb', 'mottry']
hello = "are you SB?"
message2 = f"{name[1].title()}, {hello.title()}"
print(message2)

#添加或者插入元素（append追加或者insert插入特定位置）
print("-----------分割线------------")
friut = ['apple', 'pear', 'banana', 'potato']
print(friut[-1])
friut.append('taozi')
print(friut[-1])

friut.insert(0, 'first_friut')
print(friut[0])

#删除元素(del语句或pop弹出并可赋值)
del friut[0]
print(friut[0])

print(friut[-1])
latest_friut = friut.pop()
#pop()可在圆括号中指定索引
print(friut[-1])
print(latest_friut)

#根据值删除元素
friut.remove('banana')
print(friut)
