def sandwich_toppings(*toppings):
    """One * meaning create a 元组"""
    print(f"OK, one {toppings} sandwich .")


sandwich_toppings('chicken', 'eggs','harry potter')
print("---------------------------------------------------------")


def build_profile(first, last, **info):
    """Two ** meaning create a dictionary"""
    print(f"\nHello, {first.title()} {last.title()}, nice to meet you.")
    print(f"Here are some infomation about you:")
    for keys, values in info.items():
        print(f"{keys}:{values}")


build_profile('y', 'jh', age=18, school_site='https://www.haue.edu.cn', future="I don't know. qwq")

