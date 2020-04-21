# 4) Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).  А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов:
# TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать
# текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
import random
import module6_4  # в этой задаче с модулем все норм работает. По крайней мере, я не нашел ошибок.
# Надеюсь, и у Вас не будет.


print(f"Это программа-симулятор дорожного движения в городе!")
i = 0
number = int(input(f"Введите количество шагов цикла городского движения. Возможно, вы станете свидетелем погони: "))
print()
print()
while i < number:
    car1 = module6_4.SportCar("Красная", "Toyota", False, random.randrange(0, 255, 5))
    module6_4.run_car(car1)

    if car1.speed > 150:
        car2 = module6_4.PoliceCar("Белая", "BMW", True, random.randrange(145, 255, 5))
        module6_4.run_car(car2)
    else:
        car2 = module6_4.PoliceCar("Белая", "BMW", True, random.randrange(0, 255, 5))
        module6_4.run_car(car2)

    car3 = module6_4.TownCar("Синий", "Mercedes Benz", False, random.randrange(0, 135, 5))
    module6_4.run_car(car3)

    car4 = module6_4.WorkCar("Черный", "Ford", False, random.randrange(0, 90, 5))
    module6_4.run_car(car4)
    i += 1
print("Не простой был денек!")
