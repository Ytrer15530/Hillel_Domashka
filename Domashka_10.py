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
