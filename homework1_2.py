"""
О каждом учащемся класса известны его пол, год рождения, рост и вес.
Определить, сколько в классе мальчиков и сколько девочек.
Найти средний возраст мальчиков и девочек.
Определить, верно ли, что самый высокий мальчик весит больше всех в классе,
а самая маленькая девочка является самой юной среди девочек.
"""

import datetime
now = datetime.datetime.now()
s = [['m', 2008, '170', '68'], ['m', 2009, '180', '70'], ['m', 2007, '170', '68'],
     ['f', 2009, '170', '68'], ['f', 2008, '170', '68']]
def pupils():
    counter_m = 0
    counter_f = 0
    age_sum_boys = 0
    age_sum_girls = 0
    #avg_age_boys = 0
    #avg_age_girls = 0
    for i in range(len(s)):
        if s[i][0] == 'm':
            counter_m += 1
            a = now.year - s[i][1]
            age_sum_boys += a
            avg_age_boys = age_sum_boys / counter_m
    print("Всего мальчиков в классе: ", counter_m)
    print("Средний возраст мальчиков: ", avg_age_boys)
    for i in range(len(s)):
        if s[i][0] == 'f':
            counter_f += 1
            a = now.year - s[i][1]
            age_sum_girls += a
            avg_age_girls = age_sum_girls / counter_f
    print("Всего девочек в классе: ", counter_f)
    print("Средний возраст девочек: ", avg_age_girls)

pupils()
