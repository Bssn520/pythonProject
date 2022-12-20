name = ['dwh', 'ysb', 'motty']
message1 = f"{name[0].title()}, Would you like to dinner with me?"
message2 = f"{name[1].title()}, Would you like to dinner with me?"
message3 = f"{name[2].title()}, Would you like to dinner with me?"
print(message1)
print(message2)
print(message3)

print("\n--------------------")
print(f"Sorry, {name[2].title()}, because the cocid-19 have to stay home recrntly!")
name.remove('motty')
name.append('yjh')
message4 = f"{name[0].title()}, Would you like to dinner with me?"
message5 = f"{name[1].title()}, Would you like to dinner with me?"
message6 = f"{name[2].title()}, Would you like to dinner with me?"
print(message4)
print(message5)
print(message6)

print("\n--------------------")
print(f"Good news, every one! \nThere is a bigger table and we can invite three people join us!")
dwh2 = input(f"{name[0].title()}"+", who do you want invite:")
ysb2 = input(f"{name[1].title()}"+", who do you want invite:")
yjh2 = input(f"{name[2].title()}"+", who do you want invite:")
name.insert(0, dwh2)
name.insert(3, ysb2)
name.append(yjh2)
print(name)

print("\n--------------------")
i = 1
while i<=4:
    soory  = name.pop()
    i = i+1
    print(soory + ", because of the express, I can't invite you.")

print("\n--------------------")
print(name[0].title() + "you are lucky!")
print(name[1].title() + "you are lucky!")