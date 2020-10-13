"""
    1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
# Программа работает с файлом from_homework1.txt из папки OtherFiles
# Открываем файл в кодировке utf-8

user_text = input("Введите текст для записи в файл: ")  # Сохраняет текст от пользователя
with open("OtherFiles/from_homework1.txt", "w+", encoding="utf-8") as f:
    while user_text:  # Пока в строчке есть любые символы - продолжать запись
        f.write(f"{user_text}\n")
        user_text = input("Введите текст для записи в файл: ")

# Чтение записанного ранее файла
with open("OtherFiles/from_homework1.txt", "r", encoding="utf-8") as f:
    print("Содержимое файла: ")
    for line in f.read().splitlines():
        print(line)
