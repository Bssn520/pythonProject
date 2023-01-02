prompt = "Please input the number you like."
prompt += "\nI can return the anwser you it % 10."
prompt += "\n请输入："
number = input(prompt)
number = int(number)
if number % 10 == 0:
    print(f"The number: {number} you like ok.")
else:
    print("No it is not ok.")