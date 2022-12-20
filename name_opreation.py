First_name = input("请输入您的姓：")
Last_name= input("请输入您的名字：")
#首字母大写显示
name  = (First_name+" "+Last_name).title().strip()
print(name + ",would you like to learn some python today?")
#全部大写或者小写
name2  = (First_name+" "+Last_name).upper()
name3  = (First_name+" "+Last_name).lower()
print(name2)
print(name3)
#/n /t测试
name4  = (First_name+" "+Last_name).title().strip()
name5  = (First_name+" "+Last_name).title().strip()
print(name4)
print(name5)
