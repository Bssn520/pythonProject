#3 line 判断names列表是否为空
names = ['admin', 'motty', 'jesica', 'john', 'jane']
if names:
    for name in names:
        if name == 'admin':
            print("welcome Admin, would you like to see a status report about the system?")
        else:
            print("Hello:"+name)
else:
    print("We must find more users!!!")

"""
names = []
if names:
    for name in names:
        if name == 'admin':
            print("welcome Admin, would you like to see a status report about the system?")
        else:
            print("Hello:"+name)
else:
    print("We must find more users!!!")
"""

"""
创建一个至少包含5个用户名的列表，并将其命名为current_users。

再创建一个包含5个用户名的列表，将其命名为new_users，并确保其中有一两个用户名也包含在列表current_users中。

遍历列表new_users，对于其中的每个用户名，都检查它是否已被使用。如果是这样，就打印一条消息，指出需要输入别的用户名；否则，打印一条消息，指出这个用户名未被使用。

确保比较时不区分大小写；换句话说，如果用户名'John'已被使用，应拒绝用户名'JOHN'。
"""
names_new = ['motty', 'wander', 'wuyifan', 'jack', 'john']
for names_new2 in names_new:
    if names_new2 in names:
        print("sorry,the name:"f"{names_new2}" "is used! Please change one.")
    else:
        print("Successful, the name:"f"{names_new2}"" can be used on the website!")