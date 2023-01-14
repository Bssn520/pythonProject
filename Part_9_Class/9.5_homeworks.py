from random import randint, choice

class Die:
    """模拟掷骰子，sides为骰子面数"""
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """掷骰子"""
        i = 1
        while i <= 10:
            num = randint(1, self.sides)
            print(f"第{i}次：{num}")
            i +=1

die1 = Die()
die1.roll_die()
print("-----------------")
die2 = Die(10)
die2.roll_die()
print("-----------------")
die3 = Die(20)
die3.roll_die()
print("-----------------")


# lottery analyse
lottery = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'z', 'b', 'y', 'c')
print("You can choose four elements in the list, if them same as the elements on the lottery, "
      "Well, congratulations on winning the lottery.")

ticket = ['3', 'a', 'y', '1', 'z']

i = 1
while True:
    my_ticket = []
    num1 = choice(lottery)
    my_ticket.append(num1)
    num2 = choice(lottery)
    my_ticket.append(num2)
    num3 = choice(lottery)
    my_ticket.append(num3)
    num4 = choice(lottery)
    my_ticket.append(num4)
    i += 1
    if my_ticket == ticket:
        print(f"买了{i}张才中")
        break
    else:
        print(i)
        i += 1