"""
О каждом учащемся класса известны его пол, год рождения, рост и вес.
Определить, сколько в классе мальчиков и сколько девочек.
Найти средний возраст мальчиков и девочек.
Определить, верно ли, что самый высокий мальчик весит больше всех в классе,
а самая маленькая девочка является самой юной среди девочек.
"""

import datetime

now = datetime.datetime.now()
s = [['m', 2008, '170', '68'], ['m', 2009, '173', '75'], ['m', 2007, '180', '74'],
     ['f', 2009, '160', '48'], ['f', 2008, '170', '53'],['f', 2009, '165', '50'], ['f', 2008, '167', '51']]


def pupils():
    counter_m = 0
    counter_f = 0
    age_sum_boys = 0
    age_sum_girls = 0
    # avg_age_boys = 0
    # avg_age_girls = 0
    max_height = s[0][2]
    max_weight = s[0][3]
    # max_height_pos = 0
    # max_weight_pos = 0
    min_height = s[0][2]
    max_year = s[0][1]
    # min_height_pos = 0
    # max_year_pos = 0
    for i in range(len(s)):
        if s[i][0] == 'm':
            counter_m += 1
            a = now.year - s[i][1]
            age_sum_boys += a
            avg_age_boys = age_sum_boys / counter_m
            if s[i][2] > max_height:
                max_height = s[i][2]
                max_height_pos = i
            if s[i][3] > max_weight:
                max_weight = s[i][3]
                max_weight_pos = i
    print("Всего мальчиков в классе: ", counter_m)
    print("Средний возраст мальчиков: ", avg_age_boys, "лет")
    if max_height_pos == max_weight_pos:
        print("самый высокий мальчик весит больше всех в классе")
    else:
        print("утверждение 'самый высокий мальчик весит больше всех в классе' - не является верным")

    print("=========================================================================================")

    for i in range(len(s)):
        if s[i][0] == 'f':
            counter_f += 1
            a = now.year - s[i][1]
            age_sum_girls += a
            avg_age_girls = age_sum_girls / counter_f
            if s[i][2] < min_height:
                min_height = s[i][2]
                min_height_pos = i
            if s[i][1] > max_year:
                max_year = s[i][1]
                max_year_pos = i
    print("Всего девочек в классе: ", counter_f)
    print("Средний возраст девочек: ", avg_age_girls, "лет")
    if min_height_pos == max_year_pos:
        print("самая маленькая девочка является самой юной среди девочек")
    else:
        print("утверждение 'самая маленькая девочка является самой юной среди девочек' - не является верным")


pupils()
