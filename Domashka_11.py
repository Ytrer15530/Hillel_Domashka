import re


with open("text.txt", "w", encoding="utf-8") as text:
    text.write(input("Enter text: "))


with open("text.txt", "r", encoding="utf-8") as file:
    with open("7 letters.txt", "w", encoding="utf-8") as letters:
        for line in file:
            words = re.findall(r"\b[a-zA-Z0-9А-Яа-яі]{7,}", line)
            for word in words:
                if len(word) >= 7:
                    letters.write(word + " ")

with open("text.txt", "r", encoding="utf-8") as file:
    text = file.read()
    words = text.split()
    words_count = len(words)
    print(f"Слов в тесте -> {words_count}")
