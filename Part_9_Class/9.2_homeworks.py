class Restaurant:
    """一次模拟餐馆的简单尝试"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """打印餐馆name及菜系"""
        print(f"This is a Chinese Food restaurant, it's name is {self.restaurant_name}.")
        print(f"Cuisine type:{self.cuisine_type}, I believe that you will like it.")

    def open_restaurant(self):
        """打印营业状态"""
        print(f"{self.restaurant_name} Opening Now.\tWelcome!")

    def set_number_served(self, numbers):
        """设置已就餐人数"""
        self.number_served = numbers
        print(f"{numbers} people served.")

    def increment_number_served(self, increment_number):
        """递使人数增"""
        self.number_served += increment_number
        print(f"{self.number_served} person has served!")

restaurant1 = Restaurant('中餐厅1号店', '豫菜')
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant1.set_number_served(18)
restaurant1.increment_number_served(30)
print("----------------------------------------------------------------------")


class User:
    def __init__(self):
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts +=1

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User()
print("Login attempts: " + str(user1.login_attempts))

#循环测试登录次数递增
i=0
while i < 9:
    user1.increment_login_attempts()
    print("Login attempts: " + str(user1.login_attempts))
    i += 1

#重置登录次数
user1.reset_login_attempts()
print("\nLogin attempts after reset: " + str(user1.login_attempts))
