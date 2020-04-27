#  Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# 5) Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
# и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

# 6) Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

from abc import ABC, abstractmethod

"""
Вообще было очень интересно и не просто. Я думаю, что можно было как-то сделать сильно проще, методами классов, но
не пришло мне в голову это решение. Зато никто не скажет, что я домашку не старался делать)))
С вами был Даниил Гайворонский, хорошего полета!
"""


def update_warehouse():  # функция обновления содержимого списка товаров "Основного склада"
    p_dict.update({"Товар": printers.p_list})
    p_dict.update({"количество": w_list[0]})
    s_dict.update({"Товар": scanners.s_list})
    s_dict.update({"количество": w_list[1]})
    x_dict.update({"Товар": xeroxs.x_list})
    x_dict.update({"количество": w_list[2]})


def update_warehouse1():  # функция обновления содержимого списка товаров "Бухгалтерии"
    p_dict_1.update({"Товар": printers.p_list})
    p_dict_1.update({"количество": w1_list[0]})
    s_dict_1.update({"Товар": scanners.s_list})
    s_dict_1.update({"количество": w1_list[1]})
    x_dict_1.update({"Товар": xeroxs.x_list})
    x_dict_1.update({"количество": w1_list[2]})


def update_warehouse2():  # функция обновления содержимого списка товаров "Отдел продаж"
    p_dict_2.update({"Товар": printers.p_list})
    p_dict_2.update({"количество": w2_list[0]})
    s_dict_2.update({"Товар": scanners.s_list})
    s_dict_2.update({"количество": w2_list[1]})
    x_dict_2.update({"Товар": xeroxs.x_list})
    x_dict_2.update({"количество": w2_list[2]})


def check_dict(var1, var2, var3, var4, var5, var6, var7):  # функция  для того, чтоб не было в
    # выдаче пустых списков, но как-то не очень она работает. Решил оставить, как решение на будущее,
    # так как очень много времени на нее ушло))
    if var1 > 0 and var2 > 0 and var3 > 0:
        return var4.receive(var5, var6, var7)  # заполняем товарами Основной склад
    elif var1 > 0 and var2 > 0 and var3 == 0:
        return var4.receive(var5, var6)  # заполняем товарами Основной склад
    elif var1 > 0 and var2 == 0 and var3 == 0:
        return var4.receive(var5)  # заполняем товарами Основной склад
    elif var2 > 0 and var1 == 0 and var3 == 0:
        return var4.receive(var6)  # заполняем товарами Основной склад
    elif var3 > 0 and var1 == 0 and var2 == 0:
        return var4.receive(var7)  # заполняем товарами Основной склад
    elif var2 > 0 and var3 > 0 and var1 == 0:
        return var4.receive(var6, var7)  # заполняем товарами Основной склад
    elif var1 > 0 and var3 > 0 and var2 == 0:
        return var4.receive(var5, var7)  # заполняем товарами Основной склад


def check_warehouse():  # функци вывода на экран содержимого всех отделов
    print()
    print(warehouse)
    print(warehouse1)
    print(warehouse2)
    print()


class ExcAnswer:  # класс-родитель обработки исключений для ввода и перемещения количества товаров

    @abstractmethod
    def method(self):
        pass


class ExcAnswer1(ExcAnswer):  # класс обработки исключений для ввода и перемещения количества товаров
    def __init__(self, name):
        self.name = name

    def method(self):
        while True:
            try:
                self.number = int(input(f"Введите количество принимаемой техники вида {self.name}: "))
                if self.number >= 0:
                    return self.number
                else:
                    print("Количество не может быть меньше нуля.")
            except ValueError:
                print("Это не число!")


class ExcAnswer2(ExcAnswer):  # класс обработки исключений для ответа пользователя 248 строки

    def method(self):
        while True:
            try:
                self.number = int(input(f"Введите номер отдела: "))
                if self.number == 1:
                    return self.number
                elif self.number == 2:
                    return self.number
                else:
                    print("Нет отдела с таким номером.")
            except ValueError:
                print("Это не число!")


class Warehouse:  # это класс разных отделов: Основной склад, бухгалтерия, Отдел продаж. Его аргумент - имя
    def __init__(self, name):
        self.name = name
        self.warehouse_list = []

    def receive(self, *equips):  # это метод приема товара. Принимает готовые словари товаров с количеством.
        # Он и добавляет и переопределяет, когда происходит перемещение товаров в другие отделы
        self.equips = equips
        self.warehouse_list = list(equips)

    def name(self):  # метод вывода имени отдела
        return f"{self.name}"  # например "Основной склад" или "Бухгалтерия"

    def __str__(self):  # метод вывода столбиком содержимого склада
        if len(self.warehouse_list) == 0 or self.warehouse_list == False:  # кажется тут я пытался скрыть
            # строки техники с нулевым количеством
            return f"В отделе {self.name} нет товаров."
        elif len(self.warehouse_list) == 1:
            return f"В отделе {self.name} находится такая техника:\n\n{self.warehouse_list[0]}\n"
        elif len(self.warehouse_list) == 2:
            return f"В отделе {self.name} находится такая техника:\n\n{self.warehouse_list[0]}\n" \
                   f"{self.warehouse_list[1]}\n"
        else:
            return f"В отделе {self.name} находится такая техника:\n\n" \
                   f"{self.warehouse_list[0]}\n{self.warehouse_list[1]}\n{self.warehouse_list[2]}\n"  # возвращает имя,


class OfficeEquipment:  # класс-родитель Оргтехника
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand


class Printer(OfficeEquipment):  # класс Принтер
    def __init__(self, name, brand, document_size):
        super().__init__(name, brand)
        self.document_size = document_size
        self.p_list = []
        self.p_list.append(f"{name} {brand}")
        self.p_list.append(f"формат листа бумаги {document_size}")

    def p_list(self):  # метод возврата имени. __str__ применил под построковый вывод оргтехники.
        # Что б не в одну строчку было, а как-то столбиком
        return self.p_list


class Scanner(OfficeEquipment):  # класс Сканер
    def __init__(self, name, brand, resolution):
        super().__init__(name, brand)
        self.resolution = resolution
        self.s_list = []
        self.s_list.append(f"{name} {brand}")
        self.s_list.append(f"разрешение {resolution}")

    def s_list(self):
        return self.s_list


class Xerox(OfficeEquipment):  # класс МФУ
    def __init__(self, name, brand, xerox_speed):
        super().__init__(name, brand, )
        self.xerox_speed = xerox_speed
        self.x_list = []
        self.x_list.append(f"{name} {brand}")
        self.x_list.append(f"скорость копии {xerox_speed}")

    def x_list(self):
        return self.x_list


print("Данная программа представляет собой проект 'Склад оргтехники'. Пользователь принимает товары на склад\n"
      "и может впоследствие переместить его в другое место.\n")
# создаем экземпляры отделов
warehouse = Warehouse("Основной склад")
warehouse1 = Warehouse("Бухгалтерия")
warehouse2 = Warehouse("Отдел продаж")
check_warehouse()  # проверяем товары на всех складах
# объявляем словари оргтехники для товаров на Основном складе
p_dict = {}  # для принтеров
s_dict = {}  # для сканеров
x_dict = {}  # для МФУ(ксероксов)
w_list = []  # создаем словарь значений количеств товаров для расчета перемещений товаров между отделами
# объявляем словари оргтехники для товаров в Бухгалтерии
p_dict_1 = {}
s_dict_1 = {}
x_dict_1 = {}
w1_list = []
# объявляем словари оргтехники для товаров в Отделе продаж
p_dict_2 = {}
s_dict_2 = {}
x_dict_2 = {}
w2_list = []

p_name = "Принтер"  # заполняем аргументы экземпляра принтера
p_brand = "Canon"
document_size = "А4"
printers = Printer(p_name, p_brand, document_size)  # создаем экземпляр класса Принтеры
answer = ExcAnswer1("'принтер'")
p_quantity = answer.method()  # спрашиваем, сколько принтеров нужно принять на склад и обрабатываем исключение
w_list.append(p_quantity)  # вносим значение в список количеств товаров Основного склада.
# Потом с помощью этих значений сможем считать остатки на Основном складе
s_name = "Сканер"  # заполняем аргументы экземпляра сканера
s_brand = "Epson"
resolution = "2400х1200 dpi"
scanners = Scanner(s_name, s_brand, resolution)  # создаем экземпляр класса Сканеры
answer = ExcAnswer1("'сканер'")
s_quantity = answer.method()  # спрашиваем, сколько сканеров нужно принять на склад и обрабатываем исключение
w_list.append(s_quantity)  # вносим значение в список количеств товаров Основного склада

x_name = "МФУ"  # заполняем аргументы экземпляра МФУ
x_brand = "Samsung"
xerox_speed = "16 л/мин"
xeroxs = Xerox(x_name, x_brand, xerox_speed)  # создаем экземпляр класса МФУ
answer = ExcAnswer1("'МФУ'")
x_quantity = answer.method()  # спрашиваем, сколько МФУ нужно принять на склад и обрабатываем исключение
w_list.append(x_quantity)  # вносим значение в список количеств товаров Основного склада
update_warehouse()  # обновляем словарь Основного склада
check_dict(p_quantity, s_quantity, x_quantity, warehouse, p_dict, s_dict, x_dict)  # заводим только те словари склада,
# количество товаров в которых больше нуля. Изначально хотел, чтоб строк с нулевым количеством на складах не было,
# но не везде так получилось.
print()
if p_quantity == 0 and s_quantity == 0 and x_quantity == 0:  # условие дальшейшей работы программы.
    # Если изначально ни одного товара принято не было, то и делать больше нечего.
    print("У вас нет товаров на складе. Программа завершена!")
else:
    check_warehouse()  # проверяем товары на всех складах
    i = 0  # счетчик, который сообщает - первый раз к отделу Бухгалтегии обращаются или нет (нужет для корректного
    # расчета остатков товара)
    j = 0  # счетчик, который сообщает - первый раз к отделу Отдел продаж обращаются или нет (нужет для корректного
    # расчета остатков товара)
    while True:  # цикл, который перемещает товары, пока на Основном складе они не закончатся
        if w_list[0] == 0 and w_list[1] == 0 and w_list[2] == 0:
            print(f"Все, товары в отделе {warehouse.name} закончились. А обратно вам их никто не отдаст!!!")
            break
        else:
            answer = input("Хотите передать товары в другие отделы? да/нет?\n")
            if answer == "да":
                print("Для этого введите номер отдела, в который хотите передать товары:"
                      " 1 - Бухгалтерия, 2 - Отдел продаж: ")
                answer = ExcAnswer2()
                number = answer.method()  # спрашиваем, в какой отдел передать товары и обрабатываем исключение
                if number == 1:
                    print(f"Перемещение из отдела {warehouse.name} в отдел {warehouse1.name}:")
                    while True:
                        answer = ExcAnswer1("'принтер'")
                        p_quantity_1 = answer.method()  # спрашиваем, сколько принтеров нужно принять на склад и
                        # обрабатываем исключение
                        w_list[0] = w_list[0] - p_quantity_1
                        if w_list[0] >= 0 and i == 0:
                            w1_list.append(p_quantity_1)

                            w1_list[0] = w1_list[0]
                            break
                        elif w_list[0] >= 0 and i > 0:
                            w1_list[0] = w1_list[0] + p_quantity_1
                        else:
                            print(f"В отделе {warehouse.name} нет столько принтеров.")
                            w1_list.append(0)
                            w_list[0] = w_list[0] + p_quantity_1
                        break
                    while True:
                        answer = ExcAnswer1("'Сканер'")
                        s_quantity_1 = answer.method()  # спрашиваем, сколько сканеров нужно принять на склад и
                        # обрабатываем исключение
                        w_list[1] = w_list[1] - s_quantity_1  # определяем, сколько вычесть количества с
                        # основного склада и проверяем, хватает ли товара на основном складе
                        if w_list[1] >= 0 and i == 0:  # если первый раз принимаем товар - заполняем список товаров
                            w1_list.append(s_quantity_1)
                            w1_list[1] = w1_list[1]  # добавляем количество поступившего товара
                            break
                        elif w_list[1] >= 0 and i > 0:  # если не первый раз, то какое-то количество уже есть,
                            w1_list[1] = w1_list[1] + s_quantity_1  # и нужно посчитать прибавку
                        else:
                            print(f"В отделе {warehouse.name} нет столько сканеров.")  # если товара больше нет,
                            # то нужно заполнить нулевым количеством, чтоб сохранился список из 3-х индексов
                            # и не ругался код дальше, когда будет сравнение элементов.
                            w1_list.append(0)
                            w_list[1] = w_list[1] + s_quantity_1  # тут мы возвращаем вычет который мы делали
                            # для проверки остатков склада(281 строка), что б все корректно считалось
                        break
                    while True:
                        answer = ExcAnswer1("'МФУ'")
                        x_quantity_1 = answer.method()  # спрашиваем, сколько МФУ нужно принять на склад и
                        # обрабатываем исключение
                        w_list[2] = w_list[2] - x_quantity_1
                        if w_list[2] >= 0 and i == 0:
                            w1_list.append(x_quantity_1)
                            w1_list[2] = w1_list[2]
                            break
                        elif w_list[2] >= 0 and i > 0:
                            w1_list[2] = w1_list[2] + x_quantity_1
                        else:
                            print(f"В отделе {warehouse.name} нет столько МФУ.")
                            w1_list.append(0)
                            w_list[2] = w_list[2] + x_quantity_1
                        break
                    update_warehouse()  # обновляем словарь Основного склада
                    check_dict(w_list[0], w_list[1], w_list[2], warehouse, p_dict, s_dict, x_dict)
                    update_warehouse1()    # обновляем словарь отдела Бухгалтерии
                    check_dict(w1_list[0], w1_list[1], w1_list[2], warehouse1, p_dict_1, s_dict_1, x_dict_1)
                    i += 1
                    check_warehouse()  # смотрим список содежимого на всех складах
                if number == 2:
                    print(f"Перемещение из отдела {warehouse.name} в отдел {warehouse2.name}:")
                    while True:
                        answer = ExcAnswer1("'принтер'")
                        p_quantity_2 = answer.method()  # спрашиваем, сколько принтеров нужно принять на склад и
                        # обрабатываем исключение
                        w_list[0] = w_list[0] - p_quantity_2
                        if w_list[0] >= 0 and j == 0:
                            w2_list.append(p_quantity_2)
                            w2_list[0] = w2_list[0]
                            break
                        elif w_list[0] >= 0 and j > 0:
                            w2_list[0] = w2_list[0] + p_quantity_2
                        else:
                            print(f"В отделе {warehouse.name} нет столько принтеров.")
                            w2_list.append(0)
                            w_list[0] = w_list[0] + p_quantity_2
                        break
                    while True:
                        answer = ExcAnswer1("'Сканер'")
                        s_quantity_2 = answer.method()  # спрашиваем, сколько сканеров нужно принять на склад и
                        # обрабатываем исключение
                        w_list[1] = w_list[1] - s_quantity_2
                        if w_list[1] >= 0 and j == 0:
                            w2_list.append(s_quantity_2)
                            w2_list[1] = w2_list[1]
                            break
                        elif w_list[1] >= 0 and j > 0:
                            w2_list[1] = w2_list[1] + s_quantity_2
                        else:
                            print(f"В отделе {warehouse.name} нет столько сканеров.")
                            w2_list.append(0)
                            w_list[1] = w_list[1] + s_quantity_2
                        break
                    while True:
                        answer = ExcAnswer1("'МФУ'")
                        x_quantity_2 = answer.method()  # спрашиваем, сколько МФУ нужно принять на склад и
                        # обрабатываем исключение
                        w_list[2] = w_list[2] - x_quantity_2
                        if w_list[2] >= 0 and j == 0:
                            w2_list.append(x_quantity_2)
                            w2_list[2] = w2_list[2]
                            break
                        elif w_list[2] >= 0 and j > 0:
                            w2_list[2] = w2_list[2] + x_quantity_2
                        else:
                            print(f"В отделе {warehouse.name} нет столько МФУ.")
                            w2_list.append(0)
                            w_list[2] = w_list[2] + x_quantity_2
                        break
                    update_warehouse()  # обновляем словарь Основного склада
                    check_dict(w_list[0], w_list[1], w_list[2], warehouse, p_dict, s_dict, x_dict)
                    update_warehouse2()  # обновляем словарь Отдела продаж
                    check_dict(w2_list[0], w2_list[1], w2_list[2], warehouse2, p_dict_2, s_dict_2, x_dict_2)
                    j += 1
                    check_warehouse()
            if answer == "нет":
                print("Программа завершена!")
                break
