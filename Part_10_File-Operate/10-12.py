import json
import os

filename = 'json/numbers.json'

size = os.path.getsize(filename)
if size == 0:
    num = input("Please tell me one number your favorite:")
    with open(filename, 'w') as f:
        json.dump(num, f)
        print("Thank you, I'll remember it!")
else:
    with open(filename) as f:
        num = json.load(f)
    print(f"I know your favorite number: {num} .")