# 2) Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def calculation(self, param):  # создаем абстрактный метод расчета количества ткани.
        pass


class Suit(Clothes):  # создаем потомственный класс для костюмов

    def __init__(self, param):
        self.height = param

    @property  # объявляем декоратор, фильтрует рост в заданном диапазоне
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):  # устанавливаем диапазоны роста (1.55 - 1.97)
        if height < 1.55:
            self.__height = 1.55
        elif height > 1.97:
            self.__height = 1.97
        else:
            self.__height = height

    def get_suit_height(self):
        return self.height

    def calculation(self, param):  # переопределяем абстрактный метод расчета расхода ткани для костюма
        return 2 * param + 0.3


class Coat(Clothes):  # создаем потомственный класс для пальто

    def __init__(self, param):
        self.size = param

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):  # устанавливаем диапазоны размеров (44 - 54)
        if size < 44:
            self.__size = 44
        elif size > 54:
            self.__size = 54
        else:
            self.__size = size

    def get_coat_size(self):
        return self.size

    def calculation(self, param):  # переопределяем абстрактный метод расчета расхода ткани для пальто
        self.param = param
        return param/6.5 + 0.5


print("Эта программа посчитает общий расход ткани для пальто и костюма. Для расчета расхода ткани на пальто\n"
      "используется параметр 'размер' в диапазоне 44 - 54, а для расчета расхода на костюм - 'рост', в диапазоне\n"
      "1.55 - 1.97 метра.\n")
suit = Suit(1.50)  # задаем параметр роста костюма, меньше, чем минимальный 1.55, для проверки работы декоратора
print(f"Параметр 'рост' для костюма, в метрах: {suit.get_suit_height()}")
print(f"Нужно ткани для костюма: {suit.calculation(suit.get_suit_height()):.2f}\n")
coat = Coat(55)  # задаем параметр размера пальто, больше, чем максимальный 54, для проверки работы декоратора
result_c = coat.get_coat_size()
print(f"Параметр 'размер' пальто: {coat.get_coat_size()}")
print(f"Нужно ткани для пальто: {coat.calculation(coat.get_coat_size()):.2f}\n")
print(f"Суммарный расход ткани составит "
      f"{(suit.calculation(suit.get_suit_height()) + coat.calculation(coat.get_coat_size())):.2f}")  # общий расход
