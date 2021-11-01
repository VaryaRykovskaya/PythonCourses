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

    # def print_info(self):
    #     print('id: ', self.car_id,
    #           '\nМарка: ', self.brand,
    #           '\nМодель: ', self.model,
    #           '\nГод выпуска: ', self.year,
    #           '\nЦвет: ', self.color,
    #           '\nЦена: ', self.cost,
    #           '\nРегистрационный номер: ', self.reg_num)

    def age_of_car(self):
        a = now.year - int(self.year)
        # print('Возраст машины: ', a)
        return a

    def brand_print(self):
        brnd_frm_keyboard = input("Введите марку авто: ")
        for i in range (len(Spisok_Cars )):
            brand_default = Spisok_Cars[i][1]
            if brnd_frm_keyboard == brand_default:
                print('..........................................................')
                print('id: ', Spisok_Cars[i][0],
                      '\nМарка: ', Spisok_Cars[i][1],
                      '\nМодель: ', Spisok_Cars[i][2],
                      '\nГод выпуска: ', Spisok_Cars[i][3],
                      '\nЦвет: ', Spisok_Cars[i][4],
                      '\nЦена: ', Spisok_Cars[i][5],
                      '\nРегистрационный номер: ', Spisok_Cars[i][6],
                      '\nВозраст машины: ', Spisok_Cars[i][7])
                print('..........................................................')

    def model_year_print(self):
        model_frm_keyboard = input("Введите модель авто: ")
        year_frm_keyboard = int(input("Введите число лет: "))
        for i in range (len(Spisok_Cars)):
            model_default = Spisok_Cars[i][2]
            if (model_frm_keyboard == model_default) and (Spisok_Cars[i][7] > year_frm_keyboard):
                print('*****************************************************************')
                print('id: ', Spisok_Cars[i][0],
                      '\nМарка: ', Spisok_Cars[i][1],
                      '\nМодель: ', Spisok_Cars[i][2],
                      '\nГод выпуска: ', Spisok_Cars[i][3],
                      '\nЦвет: ', Spisok_Cars[i][4],
                      '\nЦена: ', Spisok_Cars[i][5],
                      '\nРегистрационный номер: ', Spisok_Cars[i][6],
                      '\nВозраст машины: ', Spisok_Cars[i][7])
                print('*****************************************************************')


Spisok_Cars = []
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
    print('------------------------------------------------------------')
    vozrast = car.age_of_car()
    Spisok_Cars.append([car.car_id, car.brand, car.model, car.year, car.color, car.cost, car.reg_num, vozrast])
    car.car_id += 1
print('Список всех машин: ', Spisok_Cars)
print('==============================================================')
car.brand_print()
print('==============================================================')
car.model_year_print()


