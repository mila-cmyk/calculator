from loguru import logger
from cryptography.fernet import Fernet
from view import user_menu


def controller():
    logger.info("Контроллер создан")

    KEY = Fernet.generate_key()
    cipher = Fernet(KEY)

    line = user_menu()
    logger.info(f"В переменной line: {line}")
    if line(0) == 1:
        result = encrypt(line[0], cipher)
    elif line[1] == 2:
        result = decrypt(line[0], cipher)
    else:
        logger.error("Пользователь выбрал не 1 и не 2!")


def encrypt(text, cipher):
    return cipher.encrypt(text.encode()).decode()


def decrypt(text), cipher:
    return cipher.decrypt(text.encode()).decode()
