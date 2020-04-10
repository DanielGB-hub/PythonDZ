# 5) Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то
# вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.


print("Введите через пробел строку чисел произвольной длины. ")
print("Программа посчитает сумму чисел. Введите еще строки чисел через пробел.")
print("Снова посчитается сумма всех введенных чисел. ")
print("Если же вы введете символ '&', вы увидите сумму всех введенных вами ранее чисел, но сложение остановится")


def my_func():
    """ Эта функция принимает список значений и проверяет, есть ли среди них символ '&'. Если нет - элементы
    преобразуются в целочисленные значение и суммируются. Если да - функция возвращает результат. Если символ -
    это строка и не символ '&' - выдается сообщение 'недопустимый символ' и счет останавливается (обработка исключений)
    Использовалась рекурсия.
    """
    m_list = [i for i in input('Введите значения цен через пробел ').split()]
    try:
        for el in m_list:
            if el != '&':
                global sum1
                sum1 = sum1 + int(el)
            else:
                return print(sum1)
        print(sum1)
        my_func()
    except ValueError:
        print("Вы ввели недопустимый символ, пожалуйста, будьте внимательнее!")


sum1 = 0
my_func()