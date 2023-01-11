#9-6
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


class IceCreamStand(Restaurant):
    """模拟冰淇淋的简单尝试"""
    def __init__(self, restaurant_name, cuisine_type='IceCream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['watermelon', 'strawberry', 'blueberry', 'vanilla', ]

    def show_flavors(self):
        for flavor in self.flavors:
            print(f"{flavor.title()} icecream is good.")


IceCreamStand1 = IceCreamStand('中餐馆')
IceCreamStand1.show_flavors()
IceCreamStand1.describe_restaurant()
IceCreamStand1.open_restaurant()
print("------------------------------------------------")


#9-7
class User:
    """简单定义一个User类"""
    def __init__(self):
        """初始化"""
        self.login_attempts = 0

    def increment_login_attempts(self):
        """设置登录尝试次数递增"""
        self.login_attempts +=1

    def reset_login_attempts(self):
        """重置登录尝试次数"""
        self.login_attempts = 0


class Privileges:
    """定义Privileges类，用来存储用户权限"""
    def __init__(self, privileges=['can add post', 'can delete post', 'can invite other user', 'can ban users', ]):
        self.privileges = privileges

    def show_privileges(self):
        """循环打印权限"""
        print("The administrators have these privileges:")
        for privilege in self.privileges:
            print(f"{privilege.title()}")


class Admin(User):
    """创建一个子类"""
    def __init__(self):
        super().__init__()
        # 初始化属性，使其指向Privileges类
        self.privileges = Privileges()

    def show_privileges(self):
        print("The administrators have these privileges:")
        for privilege in self.privileges:
            print(f"{privilege.title()}")


Admin1 = Admin()
# 第一个privileges指Privileges类，第二个指类中的属性
Admin1.privileges.privileges = ['can add post', 'can delete post', 'can invite other user', 'can ban users', 'test']
Admin1.privileges.show_privileges()
print("------------------------------------------------")



