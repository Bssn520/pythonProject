#老忘了在遍历字典时使用items()方法
james = {
    'school': 'zkyg',
    'habit': 'dog',
}
jane = {
    'school': 'zkeg',
    'habit': 'cat',
}
peoples = [james, jane]

for people in peoples:
    for key, value in people.items():
        print(f"{key}:{value}")
print("-----------------------------------")

cat = {
    'master': 'jane',
    'kinds': 'bosi cat',
}
dog = {
    'master': 'james',
    'kinds': 'labuladuo dog',
}
pets = [cat, dog]
for pet in pets:
    for key,value in pet.items():
        print(f"{key}:{value}")
print("-----------------------------------")

favorite_places = {
    'james': ['zhoukou', 'luoyang', 'russia'],
    'jane': ['UK', 'Japan'],
    'wtf': ['Canda']
}
for key,value in favorite_places.items():
    print(f"{key}:")
    for areas in value:
        print(f"{areas}")
print("-----------------------------------")

cities = {
    'zhoukou': {'country': 'China', 'population': '8.85 million', 'fact': '老子故里'},
    'tokyo': {'country': 'Japan', 'population': '13.96 million', 'fact': '日本首都'},
    'newyork': {'country': 'America', 'population': '8.46 million', 'fact': '漂亮国首都'},
}
for key,value in cities.items():
    print(f"\n{key.title()}:")
    for key1,value1 in value.items():
        print(f"{key1.title()}:{value1.title()}")