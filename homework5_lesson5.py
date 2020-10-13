"""
    5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from random import randrange as rr

# Программа работает создает файл from_homework5.txt в папке OtherFiles
# Пример построчной записи в файле: 6 8 13 4 3 1
# Открываем файл в кодировке utf-8
with open("OtherFiles/from_homework5.txt", "w+", encoding="utf-8") as f:
    # Так как не сказано, кто должен заносить числа в файл. Либо пользователь, либо программа - я выбрал программу
    # Создаем список чисел и записываем в файл
    f.write(" ".join([str(rr(1, 20)) for _ in range(rr(1, 20))]))

# Открываем файл на чтение и считаем сумму чисел в файле
with open("OtherFiles/from_homework5.txt", "r", encoding="utf-8") as f:
    int_number_list = []
    for line in f.read().splitlines():
        for num in line.split(" "):
            int_number_list.append(int(num))
    f.seek(0)
    print("Числа в файле: ", f.read())
    print("Сумма всех чисел в файле составляет: ", sum(int_number_list))
