"""
    7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""
import json as js

# Программа работает с файлом from_homework7.txt из папки OtherFiles
# Пример построчной записи в файле: Google ООО 125000 12500
# Открываем файл в кодировке utf-8
with open("OtherFiles/from_homework7.txt", "r", encoding="utf-8") as f:
    firm_profit = None  # Прибыль фирмы
    dict_profit_firm = {}  # Фирмы с прибылью
    dict_average_profit = {}  # Средняя прибыль фирм
    dict_loser_firm = {}  # Фирмы с убытком

    # Читаем файл и заполняем dict_profit_firm или dict_loser_firm
    for line in f.read().splitlines():
        split_line = line.split(" ")
        firm_profit = int(split_line[-2]) - int(split_line[-1])  # Считаем прибыль у организации
        if firm_profit >= 0:  # Если у фирмы прибыль то пишем ее в dict_profit_firm, если нет, то в dict_loser_firm
            dict_profit_firm.update({split_line[0]: firm_profit})
        else:
            dict_loser_firm.update({split_line[0]: firm_profit})

    # Считаем среднею прибыль и добавляем ее в словарь dict_average_profit
    list_avarage = []  # Хранит значение прибыли фирм из dict_profit_firm
    for key, value in dict_profit_firm.items():
        list_avarage.append(value)

    avarage_profit = sum(list_avarage) // len(list_avarage)  # Считает значение средней прибыли
    dict_average_profit.update({"average_profit": avarage_profit})

    # Создаем список содержащий словари dict_profit_firm, dict_average_profit, dict_loser_firm
    firm_list = [dict_profit_firm, dict_average_profit, dict_loser_firm]

# Программа читает и записывает данные в файл from_homework7_dump.json из папки OtherFiles
# Открываем файл в кодировке utf-8
with open("OtherFiles/from_homework7_dump.json", "w+", encoding="utf-8") as f_json:
    js.dump(firm_list, f_json)

