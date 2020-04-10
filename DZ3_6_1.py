#  Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.


def int_func(m_word):
    """
    Эта функция проверяет, состоит ли вводимое слово только из маленьких латинских букв (пробелы и любые другие символы
     не пропустит).
    Если да - то возвращает это же слово но с заглавной буквы. Для проверки использовал множества:
    преобразовал слово в множество и сравнил с множеством, где есть все маленькие латинские буквы.
    Если разность множеств > 0, то проверка не пройдена. Цикл while просит ввести слово до тех пор,
    пока оно не удовлетворит условию.

    """
    m_set = set(m_word)
    lat_set = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x',
               'c', 'v', 'b', 'n', 'm'}
    k = (len(m_set - lat_set))  # переменная, которая определяет уникальность символов при вычитании
    if k > 0:
        return k, m_word.title()
    else:
        return k, m_word.title()


""" 
Это первая часть задания. Спрашиваем слово, вызываем функцию, проверяем условие и возвращаем результат
"""
k = 1  # константа для запуска проверки цикла while
while k > 0:
    word = input("Введите слово, написанное маленькими латинскими буквами: ")
    k, f_word = int_func(word)
print(f_word)
