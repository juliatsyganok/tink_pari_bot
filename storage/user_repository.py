user_dict = {}

def save_user(name, chat_id):
    user_dict[name] = chat_id

def get_user(name):
    return user_dict[name]