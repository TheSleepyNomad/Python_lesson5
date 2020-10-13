"""
    2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""
# Программа работает с файлом from_homework2.txt из папки OtherFiles
# Пример построчной записи в файле: Hello world
# Открываем файл в кодировке utf-8

with open("OtherFiles/from_homework2.txt", "r", encoding="utf-8") as f:
    count_row = 0 # считает количество строк в файле
    count_word = 0 # считает количество слов в строке
    for el in f.read().splitlines():
        count_row += 1
        print(f"Количество слов в {count_row} строке: {len(el.split(' '))}")
        count_word += len(el.split(" "))
    # Выводим общую информацию на экран
    print("\nКоличество строк в файле: ", count_row)
    print("Количество слов в файле", count_word)
