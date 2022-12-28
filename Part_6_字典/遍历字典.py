#6.3_homeworks
dicts = {'list': '列表', 'str': '字符串', 'tuple': '元组', 'dict': '字典', 'int': '整型' }
for key, value in dicts.items():
    print(f"\n{key}:{value}")
dicts['class'] = '类'
dicts['object'] = '对象'
for key, value in dicts.items():
    print(f"{key}:{value}")

print("-------------------------------------------------------------------")

river = {
    'nile': 'egypt',
    'long river': 'china',
    'amazon': 'brazil',
}
for key, value in river.items():
    print("\nThe %s runs through %s."%(key.title(), value.title()))
for key in river.keys():
    print(key.title())
for value in river.values():
    print(value.title())

print("-------------------------------------------------------------------")

names = [
    'yjh',
    'ysb',
    'dwh',
    'wtf',
]
favorite_languages = {
    'yjh': 'python',
    'ysb': 'c',
    'dwh': 'ruby',
}
for name in names:
    if name not in favorite_languages.keys():
        print(f"{name.title()} ,please take the poll!")
    else:
        print(f"{name.title()} ,thank you!")