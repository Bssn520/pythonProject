#8.3_homeworks
def city_country(name, coutry):
    information = f"The city {name.title()} lie in {coutry.title()}. It's a beautiful city."
    return information.title()

transfer = city_country('kunming', 'china')
print(transfer)
print("----------------------------")

"""def make_album(singer, name_album, sum=None):
    if sum:
        dictionary = {
            'singer': singer,
            'name_album': name_album,
            'sum': sum,
        }
    else:
        dictionary = {
            'singer': singer,
            'name_album': name_album,
        }
    return dictionary

transfer = make_album('meimei', 'love', 18)
print(transfer)
print("-----------------------------")"""

def make_album():
    while True:
        print(f"\nYou can enter 'quit' to quit the poll at any time.")

        name_album = input(f"Please enter the singer: ")
        if name_album == 'quit':
            break

        singer = input(f"Please enter the name of the album: ")
        if singer == 'quit':
            break

        sum = input(f"Please enter the sum of the album: ")
        if sum == 'quit':
            break

        dictionary = {
            'singer': singer,
            'name_album': name_album,
            'sum': sum,
        }
    return dictionary

transfer = make_album()
print(transfer)