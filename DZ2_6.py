# 6) *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь
# с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
#     “название”: [“компьютер”, “принтер”, “сканер”],
#     “цена”: [20000, 6000, 2000],
#     “количество”: [5, 2, 7],
#     “ед”: [“шт.”]
# }

print("Здравствуйте, начинающий логистик! Эта программа поможет структурировать данные о товарах на складе.")
q = int(input("Введите длину списка товаров: "))

list = [] # - объявляем итоговый список, в который потом будем собирать все кортежи
i = 0 # - счетчик циклов для операторов

while i != q:
    dict = {} # - объявляем словарь, в который соберем данные о товарах
    i += 1
    infoblock = [] # - список, который позже станет кортежем [№, {словарь}]

    k1 = "наименование"
    print(f"Введите наименование {i} -го товара: ")
    v1 = input().ljust(20) # - форматируем ввод, что б было удобнее смотреть результаты
    dict[k1] = v1 # - добавляем 1 пару "ключ: значение"

    k2 = "цена"
    print(f"Введите цену товара '{v1}', руб: ")
    v2 = input().ljust(20)
    dict[k2] = v2 # - добавляем 2 пару "ключ: значение"

    k3 = "количество"
    print(f"Введите количество товара '{v1}': ")
    v3 = input().ljust(20)
    dict[k3] = v3 # - добавляем 3 пару "ключ: значение"

    k4 = "ед"
    print(f"Введите единицы измерения товара '{v1}'(шт, м, литр, кг, м3): ")
    v4 = input().ljust(20)
    dict[k4] = v4 # - добавляем 4 пару "ключ: значение"

    infoblock.append(i) # - добавляем в список номер
    infoblock.append(dict) # - добавляем в список словарь
    infoblock = tuple(infoblock) # - делаем список кортежем
    list.append(infoblock) # - добавляем кортеж в итоговый список с товарами и данными
print( ) # - отступ, для лучшей читаемости в RUN
print("Список с товарами и данными: ") # - общий список со всеми данными
for el in list: # - выводим список более удобно, построчно
    print(el)
print( ) # - отступ, для лучшей читаемости в RUN
print( )

# Объявление списков с перечнями
list_1 = [] # - список для названий
list_2 = [] # - список для цен
list_3 = [] # - список для количества
list_4 = [] # - список для единиц товара (шт, м, литр, кг, м3)

i = 0 # обнуление счетчика i
while i != q: #Создание списков с перечнями наименований, цен, количеств, единиц измерений
    list_1.append(list[i][1]["наименование"])
    list_2.append(list[i][1]["цена"])
    list_3.append(list[i][1]["количество"])
    list_4.append(list[i][1]["ед"])
    i += 1

result_dict = {} # - создание итогового аналитического словаря

k = "наименование"
v = list_1
result_dict[k] = v

k = "цена"
v = list_2
result_dict[k] = v

k = "количество"
v = list_3
result_dict[k] = v

k = "ед"
v = list_4
result_dict[k] = v
#print(f"Аналитический словарь: {result_dict}") # - словарь в таком виде, как в ДЗ
print( )
for i in result_dict.items(): # - словарь в более читаемом виде
    print('{:12} : {}'.format(i[0], '' .join(i[1])))