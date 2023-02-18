import json
import time
def favorite_num():
    """让用户输入喜欢的数字，并存储到json/numbers.json"""
    num = input("Please tell me your favorite number:")
    filename = 'json/numbers.json'
    with open(filename, 'w') as file_object:
        json.dump(num, file_object)
        print("Thanks! I'll remember that.")


def get_num():
    """打印用户输入的数字"""
    filename = 'json/numbers.json'
    with open(filename, 'r') as file_object:
        f_num = json.load(file_object)

        for i in range(3, 0, -1):
            print(f"倒计时还有：{i}秒！")
            time.sleep(1)

        print("I know your favorite number! It's " + str(f_num) + ".")


favorite_num()
get_num()