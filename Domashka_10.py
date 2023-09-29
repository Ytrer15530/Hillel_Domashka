import re

tel_numb = input("Enter number of home phone: ")
if re.findall("[a-zA-Z!#@%^&*()_+=-]", tel_numb):
    print("Incorrect number. Use only digits!")
elif re.match(r'\d', tel_numb) and len(tel_numb) == 10:
    print(f"{tel_numb} is OK!")
elif len(tel_numb) != 10:
    print("Number must consist of 10 digits!")

ua_tel = input("Enter your number: ")
if re.findall("[a-zA-Z!@#$%^&*()_=]", ua_tel) or 12 > len(ua_tel) > 13:
    print("Incorrect number!")
elif re.match(r"^[+]?\d", ua_tel) and 12 <= len(ua_tel) <= 13:
    print(f"{ua_tel} OK")

email_string = input("Enter email: ")
max_email_len = 30
min_email_len = 10

if re.match(r"^[a-zA-Z\d!#$%^&*()_=+]+@[a-zA-Z\d]+\.[a-zA-Z]{2,}$", email_string) and min_email_len <= len(email_string) <= max_email_len:
    print(f"{email_string} is OK")
elif len(email_string) > max_email_len or len(email_string) < min_email_len:
    print(f"Min email len is {min_email_len} and max is {max_email_len}")
else:
    print("Email incorrect")


FIO = input("Введите ФИО: ")
if re.match(r"^[a-zA-Z]{2,20} [a-zA-Z]{2,20} [a-zA-Z]{2,20}$", FIO):
    print("Все ОК")
else:
    print("Введите правильное ФИО")
