def show_message(messages):
    """问候语列表操作。"""
    while messages:
        current_message = messages.pop()
        print(current_message.title())
        send_messages.append(current_message)

def send_message(send_messages):
    """检验结果。"""
    print(f"\nOriginal list: {messages}\n")
    print(f"Current list: {send_messages}")

messages = ['hello!', 'welcome!', "you're welcome.", 'nice day.']
send_messages = []
"""切片创建副本[:], 以保留原列表。"""
show_message(messages[:])
send_message(send_messages)