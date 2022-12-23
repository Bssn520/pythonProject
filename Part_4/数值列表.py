#使用函数range,从第一个值开始，到第二个值停止,如下：只会输出1-10
for num in range(1, 11):
    print(num)


#使用range()创建数字列表:用函数list()将range()生成的结果转化为列表
numbers = list(range(1, 101))
print(numbers)
    #只传入偶数
numbers1 = list(range(2, 101, 2))
print(numbers1)


#传入平方数
squares = []
for x in range(1,101):
    squares.append(x)
    print(f"{squares[-1]}""的平方为" + str(x ** 2))
#squares.append(x ** 2)
print(squares)
#求列表中的最值及总和
print("Squares列表最小值为：" + f"{min(squares)}\n")
print("Squares列表最大值为：" + f"{max(squares)}\n")
print("Squares列表总和为：" + f"{sum(squares)}\n")


#列表解析
squares2 = [x ** 3 for x in range(1,101)]
print(squares2)


#切片（返回列表中任意位置的值）
test = [x for x in range(1,11)]
print("Original list:" + str(test))
#返回索引为1，2，3的值：
print(test[1:4])
#返回索引从7到最后的值：
print(test[7:])
#截取范围内(0-9)每隔特定距离(2)的值
print(test[0:9:2])

#遍历切片
print("This is the first three number in test:")
for test2 in test[0:3]:
    print(test2)

#复制列表
my_food = ['pizza','chick', 'ice cream']
print(my_food)
his_food = my_food[:]
print(his_food)
for my_food_bak in my_food[:]:
    print(my_food_bak)