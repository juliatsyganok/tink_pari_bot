def add_pari(user_id, pari):
    message = 'Добавление пари \'' + pari + '\' для пользователя d=' + str(user_id)
    return message

def get_paris(user_id):
    return ['Пари1', 'Пари2', 'Пари3']