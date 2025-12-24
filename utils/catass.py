import random


def get_random_cat():
    # добавляем случайное число, чтобы Telegram не кешировал картинку
    rnd = random.randint(1, 1000000)
    return f"https://cataas.com/cat?rand={rnd}"
    return url 
# cataas возвращает случайного кота сразу картинкой