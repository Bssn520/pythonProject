#Add username to the Text_files/guest.txt after user input.
name = input("Please tell me your name:")
file_name = "Text_files/guest.txt"

with open(file_name, 'a') as file_object:
    file_object.write(name.title()+"\n")

with open(file_name) as file_object:
    contents = file_object.read()
    print(contents)
print("------------------------------")

file_name = "Text_files/guest_books.txt"

while True:
    name = input("Please tell me your name:")
    print(f"Hello, {name.title()}!")

    with open(file_name, 'a') as file_object:
        file_object.write(name + " Logged the system!\n")