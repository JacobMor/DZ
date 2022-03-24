# задача 1
from time import sleep


class TrafficLight:
    __color = {1: 'RED', 2: 'YELLOW', 3: 'GREEN'}

    def running(self):
        while True:
            print(TrafficLight.__color[1])
            time.sleep(7)
            print(TrafficLight.__color[2])
            time.sleep(2)
            print(TrafficLight.__color[3])
            time.sleep(7)


a = TrafficLight()
a.running()
#
# задача 2
class Road:
    __length = int(input('Введите длину дороги в метрах: '))
    __width = int(input('Введите ширину дороги в метрах: '))
    __mass_et = 25
    __thickness = 5

    def asphalt_mass(self):
        return print((self.__length * self.__width * self.__mass_et * self.__thickness) / 1000, 'т.')


a = Road()
a.asphalt_mass()
#
# задача 3
class Worker():
    __income = {}
    name = input('Введите имя')
    surname = input('Введите фамилию')
    __income['wage'] = int(input('Введите зарплату'))
    __income['bonus'] = int(input('Введите бонус'))
    position = 'Слуга народа'


class Position(Worker):

    def get_full_name(self):
        return print(Worker.position, Worker.name, Worker.surname)

    def get_total_income(self):
        self.c = self._Worker__income['wage'] + self._Worker__income['bonus']
        return print(self.c)


a = Position()
a.get_full_name()
a.get_total_income()
#
# задача 4
class Car():
    def __init__(self):
        print('Задаем параметры нового автомобиля')
        self.name = input('Название')
        self.speed = int(input('Скорость='))
        self.color = input('Цвет')
        self.is_police = bool(input('Машина полицейская? Да, если нет- Enter'))

    def show_speed(self):
        if self.speed > 0:
            print('Скорость ', self.speed)
        else:
            print('Стоим')

    def go(self):
        print('Поехали')

    def stop(self):
        print('Остановились')

    def turn(self):
        self.direction = input('Куда поворачиваем?')
        print('Повернули на', self.direction)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости! Ограниение 60')
        else:
            print('Скорость ', self.speed)


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости! Ограниение 40')
        else:
            print('Скорость ', self.speed)


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


a = input('Выберите тип автомобиля. TownCar, SportCar, WorkCar, PoliceCar')
if a == 'TownCar':
    a = TownCar()
elif a == 'SportCar':
    a = SportCar()
elif a == 'WorkCar':
    a = WorkCar()
elif a == 'PoliceCar':
    a = PoliceCar()


a.show_speed()
a.go()
a.stop()
a.turn()
#
# задача 5
class Stationery:
    title = 'Рисуем'
    print(title)

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Рисуем линию ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Рисуем линию карандашом')


class Handle(Stationery):
    def draw(self):
        print('Рисуем жирную линию маркером')


a = Stationery()
a.draw()
a = Pen()
a.draw()
a = Pencil()
a.draw()
a = Handle()
a.draw()
