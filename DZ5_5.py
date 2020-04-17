# 5) Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

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


print("Данная программа создаст файл в текстовом формате и запишет в него введенные через пробел числа\n"
      "и посчитает их сумму.")
file_name = input("Задайте имя текстового файла: ")
fl_name = str(file_name)  # сохраняем имя файла для последующего вызова функции in_f
f_obj = open(file_name, "w")
while True:
    content = f_obj.write(input("Введите числа через пробел или нажмите enter,\n"
                                "когда строка пуста, чтобы закончить ввод (а можно все подряд вводить, все равно\n"
                                "посчитает сумму чисел в файле): "))
    f_obj.write("\n")
    if not content:
        break
f_obj.close()
print()
print(f"Файл {fl_name} успешно создан/перезаписан!")
content_list = in_f(fl_name)
print()
m_list = []  # объявляем список в который пойдум суммы чисел строк
summ = 0  # суммы чисел строк
result_sum = 0  # итоговая сумма всех чисел всех строк
for el in content_list:
    numbers = re.findall(r'[-]?\d+\.\d+|[-]?\d+', el)  # находим все int и float числа
    numbers = [float(x) for x in numbers]  # приводим все числа к типу float
    summ = sum(numbers)  # вычисляем суммы чисел строк
    m_list.append(summ)  # добавляем суммы чисел строк в список
result_summ = sum(m_list)  # суммируем все суммы чисел строк в итоговую сумму
print(f"Сумма всех чисел в файле равна {result_summ}")
print()
dir_l()  # проверяем список файлов, файл создался
