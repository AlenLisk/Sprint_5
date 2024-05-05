import random


class Helper:
    @staticmethod
    def registration_login(): # генерация логина
        name = 'alena'
        lastname = 'liskovskaya'
        cohort_num = '8'
        domain = '@ya.ru'
        numbers = str(random.randint(100,999))

        email = name + '_' + lastname + '_' + cohort_num + '_' + numbers + domain

        return email

    @staticmethod
    def registration_password(): # генерация пароля от 6 до 10 символов
        symbols_list = [['ABCDEFGHIJKLMNOPQRSTUVWXYZ'], ['abcdefghijklmnopqrstuvwxyz'], ['0123456789'], ['/#@$*=+&%']]
        password = ''
        password_len = random.randint(6, 10)
        for i in range(password_len):
            symbols = symbols_list[random.randint(0, 3)][0]
            password += symbols[random.randint(0, len(symbols) - 1)]

        return password
