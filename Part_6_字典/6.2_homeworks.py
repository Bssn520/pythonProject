Bssn = {'name': 'bssn', 'age': 19, 'city': 'zhoukou'}
for information in Bssn:
    print(information + ":" + str(Bssn[information]))

print("-------------------------------------------------------------------")

numbers = {
    'yjh': 4,
    'dwh': 1,
    'ysb': 3,
}
for number in numbers:
    print(number + f":{numbers[number]}")

print("-------------------------------------------------------------------")

dicts = {'list': '列表', 'str': '字符串', 'tuple': '元组', 'dict': '字典', 'int': '整型' }
print('list' + ": " + dicts['list'] )
print('str' + ": " + dicts['str'] )
print('tuple' + ": " + dicts['tuple'] )
print('dict' + ": " + dicts['dict'] )
print('int' + ": " + dicts['int'] )