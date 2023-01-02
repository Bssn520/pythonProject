#删除为特定值的所有列表元素
pets = ['cat', 'dog', 'wolf', 'wox', 'cat', 'fish', ]
print(f"{pets}\n")
while 'cat' in pets:
    pets.remove('cat')
print(pets)
print("-----------------------")

#简易调查交互程序，用字典存储名字及回答
sandwich_orders = ['fish', 'chicken', 'vegetables', 'pastrami', 'pastrami', 'pastrami', ]
finished_sandwiches = []
while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print(f"Your {sandwich_order.title()} sandwich is ok.")
    finished_sandwiches.append(sandwich_order)

for finished_sandwich in finished_sandwiches:
    print(f"The {finished_sandwich} is ok.")
print("------------------------")

print("The pastrami has selled over, please come in advance tomorrow. Thank you.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)
print("------------------------")

places = {}
while True:
    name = input("What is your name: ")
    place = input("Which place you want to have one travel: ")
    places[name] = place
    continue_prompt = input("Would you like to let someone else respond？(yes/no)")
    if continue_prompt == "no":
        break

for name2,place2 in places.items():
    print(f"{name2.title()} want go to {place2.title()} have a travel with npy.")