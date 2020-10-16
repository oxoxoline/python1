def person_date(*args):
    name = input('Напишите Ваше имя: ')
    surname = input('Напишите Вашу фамилию: ')
    birthday = int(input('В каком году Вы родились: '))
    city = input('В каком городе Вы проживаете: ')
    email = input('Введите Ваш email: ')
    phone_number = int(input('Введите Ваш телефонный номер: '))
    return name, surname, birthday, city, email, phone_number


print(person_date())


def person_date_1(name, surname, birthday, city, email, phone_number):
    return name, surname, birthday, city, email, phone_number


print(person_date_1(name='Вася', surname='Пупкин', birthday=1955, city='Moscow', email='Vasya1955@yandex.ru',
                    phone_number=89997773366))
