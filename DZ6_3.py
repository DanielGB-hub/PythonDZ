#  Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
# с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).


class Worker:

    def __init__(self, name=None, surname=None, position=None, wage=0, bonus=0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


person_1 = Position("Дмитрий", "Донской", "князь", 1000000, 500000)
print(f"Данные о сотруднике 1:\n\n"
      f"Имя:           {person_1.name}\n"
      f"Фамилия:       {person_1.surname}\n"
      f"Должность:     {person_1.position}\n"
      f"Доход:         {person_1._income}\n")

print(f"Имя и фамилия:     {person_1.get_full_name()}\n"
      f"Суммарный доход:   {person_1.get_total_income()}")
