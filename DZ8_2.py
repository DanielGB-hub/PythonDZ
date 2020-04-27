#  Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно
# обработать эту ситуацию и не завершиться с ошибкой.


class Div_ByNull:
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2

    @staticmethod
    def div_byNull(number_1, number_2):
        try:
            return f"Результат деления: {number_1 / number_2}"
        except:
            return f"Некорректная математическая операция! Делить на ноль нельзя!"


print(f"Эта программа произведет деление одного числа на другое или сообщит об ошибке при делении на ноль.\n")
number_1 = int(input(f"Введите делимое: "))
number_2 = int(input(f"Введите делитель: "))
print(Div_ByNull.div_byNull(number_1, number_2))