import random
import time


def run_car(car):  # функция для облегчения кода в цикле ниже
    car.go()
    car.stop()
    car.show_speed()
    if car.speed != 0:
        car.turn(random.randrange(0, 5, 1))
    print()
    print()
    time.sleep(7)


class Car:
    def __init__(self, color, name, is_police, speed): #  описание базового класса
        self.color = color
        self.name = name
        self.is_police = bool(is_police)
        self.speed = int(speed)
        if is_police == True:
            type = "Полиция"
        else:
            type = "Частный автомобиль"
        print(f"{self.color} {self.name}, {type}")

    def show_speed(self):
        print(f"Скорость {self.speed}")

    def go(self):
        if self.speed != 0:
            print("Поехала... Дела, дела.")

    def stop(self):
        if self.speed == 0:
            print("Стоит")

    def turn(self, direction):
        self.direction = int(direction)
        if direction == 1:
            print("Машина повернула налево")
        if direction == 2:
            print("Машина повернула направо")


class SportCar(Car):
    def show_speed(self):
        print(f"Скорость {self.speed} км/ч")
        if self.speed >= 200:
            print("Похоже, удирает от полиции!")
        if 0 < self.speed <= 60:
            print("Едет, будто обычный горожанин, но мы то знаем, что это гонщик!")

    def go(self):
        if 140 >= self.speed > 0:
            print("Ищем приключения")
        if 200 > self.speed > 140:
            print("Уличная гонка! Вперед вперед вперед!!!")
        if self.speed >= 200:
            print("Нашлись приключения!")


class PoliceCar(Car):
    def show_speed(self):
        print(f"Скорость {self.speed}")

    def go(self):
        if self.speed > 140:
            print("Похоже, за кем-то погналась!")
        if 140 > self.speed > 40:
            print("Вызвали в центр, опять гонщики гоняют")
        if 0 < self.speed < 40:
            print("Крадется...")
        if self.speed == 0:
            print("Кофе пьют, небось. На штанишки что б не пролить!")


class TownCar(Car):
    def show_speed(self):
        print(f"Скорость {self.speed}")
        if self.speed > 60:
            print("Превышение ограничения 60 км/ч!")

    def go(self):
        if 60 >= self.speed > 0:
            print("Едем по городу")
        if 80 >= self.speed > 60:
            print("Опаздывает куда-то")
        if self.speed > 80:
            print("Ааа, утюг дома забыл выключить!")


class WorkCar(Car):
    def show_speed(self):
        print(f"Скорость {self.speed}")
        if self.speed > 40:
            print("Превышение ограничения 40 км/ч!")

    def go(self):
        if 40 >= self.speed > 0:
            print("Аккуратно везет груз")
        if 80 >= self.speed > 40:
            print("Еще 3 доставки!")
        if self.speed > 80:
            print("Накладные в офисе остались!!!")
