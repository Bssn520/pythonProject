# 10-8 Dogs and Cats
def animals(filename):
    """FileNotFoundError测试"""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
            print(contents)
    except FileNotFoundError:
        # 静默失败将except内容改为 "pass" 即可
        print("File not found!!!")

filename = 'Text_files/love_python.txt'
animals(filename)


def num_words(filename, word):
    """计算一个文本文件中的单词总数及某个单词出现的次数"""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
            words = contents.split()
            print(f"The {filename} flie totla has {len(words)} words.")
            contents = contents.lower()
            num = contents.count(word)
            print(f"单词: {word} 共出现 {num} 次. ")
    except FileNotFoundError:
        print("File not found!!!")


filename = 'Text_files/The Adventures of Ferdinand Count Fathom.txt'
num_words(filename, 'of ')
