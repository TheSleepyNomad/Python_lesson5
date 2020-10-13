"""
    4. Создать (не программно) текстовый файл со следующим содержимым:
        One — 1
        Two — 2
        Three — 3
        Four — 4
    Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
    При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый
    текстовый файл.
"""
# Словарь числительных.
number_dict = {"One": "Один",
               "Two": "Два",
               "Three": "Три",
               "Four": "Четыре"}

save_strings = []  # Сохраняет в себе строки с переведенными числительными

# Программа работает с файлом from_homework4.txt из папки OtherFiles
# Пример построчной записи в файле: One - 1
# Открываем файл в кодировке utf-8
with open("OtherFiles/from_homework4.txt", "r", encoding="utf-8") as f:
    for line in f.read().splitlines():
        split_line = line.split(" ")
        split_line[0] = number_dict[split_line[0]]
        save_strings.append(" ".join(split_line))

# Программа работает с файлом from_homework4_translate_number.txt из папки OtherFiles
# Пример построчной записи в файле: Один - 1
# Открываем файл в кодировке utf-8, а если его нет, то создаем и записываем переведенные строки в него
with open("OtherFiles/from_homework4_translate_number.txt", "w+", encoding="utf-8") as f:
    for line in save_strings:
        f.writelines(line + "\n")
