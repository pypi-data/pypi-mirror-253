import sys
from hashlib import md5
from prettytable import PrettyTable

fields = {
    "_all_": "Чтобы отбрабатывать все возможные виды",
    "phone": "Телефонный номер",
    "account.fb.id": "Id Facebook",
    "account.insta.id": "Id Instagram",
    "account.insta.username": "Ник Instagram",
    "account.linkedin.id": "Id Linkedin",
    "account.linkedin.username": "Ник Linkedin",
    "account.ok.id": "Id OK",
    "account.other.password": "Пароль",
    "account.other.username": "Ник",
    "account.skype.id": "Id Skype",
    "account.tg.id": "Id Telegram",
    "account.tg.username": "Ник Telegram",
    "account.twitter.id": "Id Twitter",
    "account.twitter.username": "Ник  Twitter",
    "account.vk.id": "Id VK",
    "account.yandex.id": "Id Yandex",
    "document.passport.number": "Паспорт",
    "account.other.email": "E-mail",
    "organization.name": "Название организации",
    "vehicle.car.regnumber": "Рег.номер авто",
}

if __name__ == "__main__":

    if sys.argv.__len__() == 2:
        command = sys.argv[1]
        table = PrettyTable()
        table.field_names = ["Тип данных", "Обозначение"]
        table.add_rows([[key, value] for key, value in fields.items()])
        if command == "fields":
            print("Наименования полей, используемых в общем проекте:\n")
            print(table)
            print("\nАктуальная информация доступна по ссылке: coming soon")
    elif sys.argv.__len__() == 3:
        command = sys.argv[1]
        value = sys.argv[2]
        if command == "hash":
            try:
                print(md5(value.encode('utf-8')).hexdigest())
            except UnicodeDecodeError:
                print("Не удалось преобразовать значение")
