prompt = "Please input what ingredients you want to add to the pizza:"
print("Enter the 'quit' to exit.")
while True:
    ingredients = input(prompt)
    if ingredients != "quit":
        print(f"OK, the {ingredients.title()} have added.")
    elif ingredients == "quit":
        break
print("-------------------------------------")

prompt = "Please input what ingredients you want to add to the pizza:"
print("Enter the 'quit' to exit.")
active = True
while active:
    ingredients = input(prompt)
    if ingredients != "quit":
        print(f"OK, the {ingredients.title()} have added.")
    else:
        active = False