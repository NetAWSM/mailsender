import re
import smtplib
import os



def send_email(message):
    sender = "s.nikiforov@fcaudit.ru"
    password = "FZgZCEOa6uIW3kTnfPK2"
    send = input("введите получателя: ")
    server = smtplib.SMTP("mail.fcaudit.ru", 25)

    try:
        server.login(sender, password)
        server.sendmail(sender, send, message)

        return "Сообщение отправленно!"
    except Exception as _ex:
        return f"{_ex}\Проверьте Логин или пароль"


def main():
    message = input("Введите свое сообщение: ").encode("cp1251")
    print(send_email(message=message))


if __name__ == "__main__":
    main()