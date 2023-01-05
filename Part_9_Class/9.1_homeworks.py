class Restaurant:
    """一次模拟餐馆的简单尝试"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """打印餐馆name及菜系"""
        print(f"This is a Chinese Food restaurant, it's name is {self.restaurant_name}.")
        print(f"Cuisine type:{self.cuisine_type}, I believe you will like it.")

    def open_restaurant(self):
        """打印营业状态"""
        print(f"{self.restaurant_name} Opening Now.\tWelcome!\n")


restaurant1 = Restaurant('中餐厅1号店', '豫菜')
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2 = Restaurant('中餐厅2号店', '川菜')
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3 = Restaurant('中餐厅3号店', '鲁菜')
restaurant3.describe_restaurant()
restaurant3.open_restaurant()
print("-----------------------------------------------------------------------------")


class User:
    """简易存储用户信息"""
    def __init__(self, f_name, l_name, **info):
        self.f_name = f_name
        self.l_name = l_name
        self.info = info

    def describe_user(self):
        """将信息存储进字典中，但不知怎样把f_name和l_name存在字典头部qwq"""
        self.info['first_name'] = self.f_name
        self.info['last_name'] = self.l_name
        print("Here are some information about you:")
        for keys, values in self.info.items():
            print(f"{keys.title()}:{str(values).title()}")

    def greet_user(self):
        """简单打印一条问候语"""
        print(f"Hello, {self.f_name.title()} {self.l_name.title()}. Nice to meet you, you look nice!")


user1 = User('y', 'jh', age=18, job='student', game='lol')
user1.greet_user()
user1.describe_user()
