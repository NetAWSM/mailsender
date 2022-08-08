import re
import smtplib
import os
from email.mime.text import MIMEText



def send_email(message):
    sender = "login"
    password = "pass"
    send = input("введите получателя: ")
    server = smtplib.SMTP("domain", 25)

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        server.sendmail(sender, send, msg.as_string())
        # server.sendmail(sender, send, message)

        return "Сообщение отправленно!"
    except Exception as _ex:
        return f"{_ex}\Проверьте Логин или пароль"


def main():
    message = input("Введите свое сообщение: ").encode("cp1251")
    print(send_email(message=message))


if __name__ == "__main__":
    main()
