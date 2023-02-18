# 10-6 加法运算
print("请输入两个数字，我会帮你把它们相加.\n你可以随时输入'q'以退出.")

while True:
    first_num = input("Please input the first number:")
    if first_num == 'q':
        break
    try:
        first_num = int(first_num)
    except ValueError:
        print("你输入的好像不是一个数字啊🤔")
    second_num = input("Please input the second number:")
    if second_num == 'q':
        break
    try:
        second_num = int(second_num)
    except ValueError:
        print("你输入的好像不是一个数字啊🤔")
    else:
        anwser = (first_num+second_num)
        print(anwser)
print("---------------------------------------------------")
# Version 2.0
while True:
    try:
        f_num = input("Please input the first number:")
        if f_num == 'q':
            break
        f_num = int(f_num)
        s_num = input("Please input the second number:")
        if s_num == 'q':
            break
        s_num = int(s_num)
    except ValueError:
        print("你输入的好像不是一个数字啊🤔")
    else:
        anwser = f_num + s_num
        print(anwser)
print("--------------------------------------------------")

