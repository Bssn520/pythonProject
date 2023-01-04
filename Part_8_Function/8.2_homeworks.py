def make_shirt():
    size = input(f"Please input the size you want: ")
    logo = input(f"Please input what words you want see on the shirt: ")
    print(f"OK, give you the {size.upper()} T-shirt with words: {logo}.")

make_shirt()
print("------------------------------------")

def make_shirt(size='L', logo='I love Python'):
    print(f"OK, give you the {size.upper()} T-shirt with words: {logo}.")

make_shirt()
make_shirt(size='M')
make_shirt(size='s', logo='I love javascript.')