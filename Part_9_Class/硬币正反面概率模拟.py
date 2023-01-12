import random
i = 1
zero = 0
one = 0
while i <= 100_000:
    x = random.randint(0, 1)
    if x == 0:
        zero += 1
    else:
        one += 1
    i += 1
    print(f"{x}")
print(f"正面{one}次；")
print(f"反面{zero}次；")

