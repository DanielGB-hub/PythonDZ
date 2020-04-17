# 7) Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать
# данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

"""
В данной программе использованы 3 функции:
1. f_info - возвращает информацию о кодировке исходного файла
2. dir_l - покажет содержимое директории, из которой вы откроете данную программу
3. in_f - считает содержимое файла, выведет это содержимое построчно на экран, вернет содержимое файла в виде списка,
элементами которого будут строки и закроет файл.
"""
import re
import os
from chardet.universaldetector import UniversalDetector
import json

def f_info(f_name):  # функция чтения информации о кодировке
    detector = UniversalDetector()
    with open(f_name, 'rb') as fb:
        for line in fb:
            detector.feed(line)
            if detector.done:
                break
        detector.close()
    #print(detector.result)  # раскомментировать, чтобы посмотреть информацию о файле
    return detector.result.get('encoding')


def dir_l():  # функция чтения списка файлов в локальной директории
    print("Список файлов в локальной директории: ")
    dir_list = os.listdir(path=".")  # показываем содержимое директории, в которой лежит файл задания
    print(dir_list)


def in_f(f_name):  # функция чтения файла с разной кодировкой и вывода его содержимого
    if f_info(f_name) == "utf-8" or f_info(f_name) == "UTF-8-SIG":
        print(f"Кодировка: {f_info(f_name)}")
        f_obj = open(f_name, "r", encoding="utf-8-sig")
    elif f_info(f_name) == "windows-1251":
        print(f"Кодировка: {f_info(f_name)}")
        f_obj = open(f_name, "r", encoding="windows-1251")
    elif f_info(f_name) == "ascii":
        print(f"Кодировка: {f_info(f_name)}")
        f_obj = open(f_name, "r", encoding="ascii")
    print()
    content_list_def = []
    print("Содержимое файла:\n ")
    content_f = f_obj.readlines()
    for el_f in content_f:  # выводим содержимое построчно
        print(el_f.replace('\n', ''))  # делаем замену, что б строки не выводились через пустые строки
        content_list_def.append(el_f.replace('\n', ''))
    f_obj.close()  # закрываем файл
    print()
    if f_obj.closed == 1:
        print("Файл закрыт")
    return content_list_def  # выводим содержимое в список для последующей обработки


print("Данная программа откроет файл со строками типа : 'Информатика:   100(л)   50(пр)   20(лаб)',\n"
      " посчитает суммарное количество часов каждой дисциплины и выведет на экран результат в виде словаря,\n"
      "например: {'Информатика': 170}")
dir_l()  # смотрим список файлов, которые можно открыть

try:  # обработка исключения "Такой файл не найден"
    try:  # обработка исключения "Кодировка не распознана"
        file_name = input("Выберете из списка имя текстового файла, который вы хотите открыть: ")  # все жрет, и .py
        content_list = in_f(file_name)  # показываем содержимое файла и возвращаем это содержимое списком
        m_list_company = []  # объявляем список в который пойдут названия дисциплин
        m_list_dif = []  # объявляем список в который пойдет прибыль/убыток
        m_list_dif_plus = []  # объявляем список в который пойдет только прибыль
        company_dict = {}  # объявляем итоговый словарь
        list_average_profit = []   # объявляем список средней прибыли
        list_average_profit_2 = []  # как то все через ж
        dict_average_profit = {}  # объявляем словарь средней прибыли
        result_list = []
        result_dict = {}
        dif = 0  # объявляем переменную суммы часов дисциплины
        sum_plus = 0  # объявляем переменную суммарной прибыли только прибыльных компаний
        i = 0  # объявляем счетчик компаний
        try:  # обработка исключения "Содержимое файла не подходит для обратобки"
            for el in content_list:
                text = re.findall(r'[а-яА-ЯёЁ-]{2,}|[a-zA-Z-]{2,}', el)  # находим слова названий
                company = str(text[0]) + " " + str(text[1]) # восстанавливаем названия фирм
                # print(company)  # раскомментить, чтобы построчно вывести список компаний для проверки
                numbers = re.findall(r'\d+', el)  # находим все int числа
                numbers = [int(x) for x in numbers]  # приводим все числа к типу int
                m_list_company.append(company)  # создаем список с названиями компаний
                dif = numbers[0] - numbers[1]  # вычисляем прибыть/убытки
                m_list_dif.append(dif)  # добавляем прибыль/убыток в список
                if dif > 0:  # условие для добавления прибыли в список прибыли
                    m_list_dif_plus.append(dif)  # добавляем прибыль в список прибыли
            sum_plus = sum(m_list_dif_plus)  # суммарная прибыль прибыльных компаний
            average_profit = sum_plus / len(m_list_dif_plus)  # считаем среднюю прибыть прибыльных компаний
            list_average_profit.append("average_profit")
            list_average_profit_2.append(average_profit)
            dict_average_profit = dict(zip(list_average_profit, list_average_profit_2))  # делаем хитрый финт
            company_dict = dict(zip(m_list_company, m_list_dif))  # делаем хитрый финт
            result_list.append(company_dict)
            result_list.append(dict_average_profit)
            print(f"Итоговый список: {result_list}\n")  # аллилуя!
            print("Выгружаем информацию в файл 'text_78.json'...\n")

            with open(   # выводим в json
                    "text_78.json",
                    'w', encoding="utf-8"
            ) as f:
                # s = json.dumps(data,ensure_ascii=False,indent=4)
                for chunk in json.JSONEncoder(ensure_ascii=False, indent=4).iterencode(result_list):
                    f.write(chunk)
            print("Файл 'text_78.json' успешно создан!\n")
            print("Откроем созданный файл 'text_78.json' и проверим его содержимое: ")
            in_f("text_78.json")  # проверяем содержимое файла .json
        except ValueError:
            print("Содержимое файла не подходит для обработки. Пожалуйста, откройте подходящий файл.")
    except NameError:
        print("Кодировка файла не распознана, пересохраните файл в одной из кодировок utf-8, windows-1251 или ascii\n"
              "и попробуйте снова")
except FileNotFoundError:
    print("Такой файл не найден")
