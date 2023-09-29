import re

tel_numb = input("Enter number of home phone: ")
if re.findall("[a-zA-Z!#@%^&*()_+=-]", tel_numb):
    print("Incorrect number. Use only digits!")
elif re.match(r'\d', tel_numb) and len(tel_numb) == 10:
    print(f"{tel_numb} is OK!")
elif len(tel_numb) != 10:
    print("Number must consist of 10 digits!")
