# 1) Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

result_list = [] # создаем пустой список и добавляем в него элементы
result_list.append("cool") # строка
result_list.append(None) # 'NoneType'
result_list.append(False) # булевое
result_list.append(223) # целочисленное
result_list.append(32.2) # с плавающей запятой
result_list.append(4+5j) # комплексное
result_list.append(b'text') # байт
m_ba = bytearray(b"some text") # массив байт
result_list.append(m_ba)
result_list.append([1, 2, 3]) # список
result_list.append({3, "cat", None}) # множества
m_t = tuple("это кортеж") # кортеж
result_list.append(m_t)
m_d = {a: a ** 2 for a in range(7)} # создаем словарь с помощью генератора
result_list.append(m_d)
print(result_list)
print("Убеждаемся, что наш список - действительно список: ")
print(type(result_list))

print("Типы элементов списка: ")

for el in result_list: # перебираем элементы и выводим типы каждого
    print(el)
    print(type(el))

