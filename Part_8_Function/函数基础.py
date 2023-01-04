def display_message(message):
    """简易函数基础小作业"""
    print(f"Hello, {message}! You look very nice!")

display_message('Bssn520')
print("-------------------------------------------------------")

def favorite_book(title):
    """The favorite book share."""
    print(f"One of my favorite book is {title.title()}")

favorite_book('hello world')
print("-------------------------------------------------------")

def information_pet(pet_kind, pet_name):
    """位置实参：位置对于参数十分重要"""
    print(f"I have one {pet_kind}, it's name is {pet_name.title()}.")

information_pet('dog', 'bangbang')
print("-------------------------------------------------------")

def information_pet(pet_kind, pet_name):
    """关键字实参：位置对于参数不重要"""
    print(f"I have one {pet_kind}, it's name is {pet_name.title()}.")

information_pet(pet_kind='dog', pet_name='bangbang')
print("-------------------------------------------------------")

def information_pet(pet_name, pet_kind='dog'):
    """默认值，未传入对应实参时，使用默认形参, 默认形参应置于非默认形参之后"""
    print(f"I have one {pet_kind}, it's name is {pet_name.title()}.")

information_pet(pet_name='bangbang')