import json
import os

filename = 'json/username.json'
def get_new_username():
    """获取新用户的名字"""
    username = input("Please tell me your name:")
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def get_stored_name():
    """获取已存储的用户名"""
    size= os.path.getsize(filename)
    if size == 0:
        get_new_username()
    else:
        with open(filename, 'r') as f:
            username = json.load(f)
        return username


def greet_user():
    """判断是否为新用户，及打印问候语"""
    username = get_stored_name()
    if username:
        correct = input(f"Are you {username.title()} ?(y/n)")
        if correct == 'y':
            print("Welcome back! " + username.title())
        else:
            username = get_new_username()
            print(f"Hello {username}, I'll remember you.")
    else:
        print(f"Hello {username}, I'll remember you.")


greet_user()

