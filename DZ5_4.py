#  Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

"""
В данной программе использованы 3 функции: 
1. f_info - возвращает информацию о кодировке исходного файла
2. dir_l - покажет содержимое директории, из которой вы откроете данную программу
3. in_f - считает содержимое файла, выведет это содержимое построчно на экран, вернет содержимое файла в виде списка,
элементами которого будут строки и закроет файл.

Перевод слов реализован так: пользователю предлагается самому перевести слова и ввести их вручную, а программа уже 
сама заменит английские слова на русские.

Название конечного файла сгенерируется автоматически. Оно будет состоять из названия исходного файла
с припиской _rus. Например, если имя исходного файла text_4.txt, то конечный файл будет text_4_rus.txt

Конечный файл будет сохранен в ту же директорию, где хранится исходный файл. 

Программа автоматически распознает такие кодировки: utf-8, utf-8-sig, windows-1251 и ascii.

Кодировка конечного файла будет такой же. как и исходного, за исключением кодировки ascii, 
которая будет заменена на utf-8. Вроде все.
"""

import os
from chardet.universaldetector import UniversalDetector


def f_info(f_name):  # функция чтения информации о кодировке
    detector = UniversalDetector()
    with open(f_name, 'rb') as fb:
        for line in fb:
            detector.feed(line)
            if detector.done:
                break
        detector.close()
    # print(detector.result)  # раскомментировать, чтобы посмотреть информацию о файле
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


print("Данная программа откроет файл с английскими строками, заменит английские слова на слова с Вашим вариантом\n"
      "перевода и сохранит новые строки в новом файле с именем 'файл_rus.txt'.\n"
      "Исходные кодировки utf-8 или windows-1251 будут сохранены. Кодировка ascii будет заменена на utf-8.")
dir_l()  # смотрим список файлов, которые можно открыть

try:  # обработка исключения "Такой файл не найден"
    try:  # обработка исключения "Кодировка не распознана"
        file_name = input("Выберете из списка имя текстового файла, который вы хотите открыть: ")  # все жрет, и .py
        new_encoding = f_info(file_name)  # смотрим исходную кодировку входного файла
        new_name = str(file_name).replace(f"{str(file_name)[str(file_name).index('.'):len(str(file_name))]}", "") + \
                   "_rus.txt"  # создаем имя выходного файла
        content_list = in_f(file_name)  # показываем содержимое файла и возвращаем это содержимое списком
        # print(content_list)
        m_str = str(input("Переведите английские слова и введите их перевод через пробел: "))
        m_list = m_str.split()  # преобразуем в список
        # print(m_list)  # раскомментировать, чтобы посмотреть список переведенных слов
        i = -1
        rus_list = []
        for el in content_list:
            i += 1
            s = str(m_list[i]) + el.replace(f"{el[0:el.index(' ')]}", "")
            rus_list.append(s)
        # print(rus_list)  # раскомментировать, чтобы посмотреть итоговый список с переводом
        if new_encoding == "ascii":
            new_encoding = "utf-8"
        fn_obj = open(new_name, "w", encoding=new_encoding)
        for el in rus_list:
            content = fn_obj.write(el)
            fn_obj.write("\n")
        fn_obj.close()
        print()
        print(f"Файл с именем {new_name} создан! ")
        content_list = in_f(new_name)
        dir_l()

    except NameError:
        print("Кодировка файла не распознана, пересохраните файл в одной из кодировок utf-8, windows-1251 или ascii\n"
              "и попробуйте снова")
except FileNotFoundError:
    print("Такой файл не найден")
