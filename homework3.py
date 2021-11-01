"""
Создать класс Car: id, Марка, Модель, Год выпуска, Цвет, Цена, Регистрационный номер.
Функции-члены реализуют запись и считывание полей (проверка корректности), вывода возраста машины.
Создать список объектов. Вывести:
a)	список автомобилей заданной марки;
b)	список автомобилей заданной модели, которые эксплуатируются больше n лет;
"""

import datetime

now = datetime.datetime.now()


class Car:
    car_id = 0

    def __init__(self, brnd='', mod='', yr='', clr='', cst='', regnum=''):
        self.brand = brnd
        self.model = mod
        self.year = yr
        self.color = clr
        self.cost = cst
        self.reg_num = regnum

    def print_info(self):
        print('id: ', self.car_id,
              '\nМарка: ', self.brand,
              '\nМодель: ', self.model,
              '\nГод выпуска: ', self.year,
              '\nЦвет: ', self.color,
              '\nЦена: ', self.cost,
              '\nРегистрационный номер: ', self.reg_num)

    def age_of_car(self):
        a = now.year - int(self.year)
        print('Возраст машины: ', a)


car = Car()
Kol = int(input('Сколько машин добавить в список? '))
for i in range(Kol):
    print("Введите марку автомобиля: ")
    car.brand = input()
    print("Введите модель: ")
    car.model = input()
    print("Введите год выпуска: ")
    car.year = input()
    print("Введите цвет: ")
    car.color = input()
    print("Введите цену: ")
    car.cost = input()
    print("Введите регистрационный номер: ")
    car.reg_num = input()
    print('------------------------------')
    car.print_info()
    car.age_of_car()
    print('===============================')
    car.car_id += 1
