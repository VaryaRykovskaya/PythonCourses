"""
Сформировать одномерный список целых чисел A, используя генератор случайных чисел (диапазон от 0 до 99).
Размер списка n ввести с клавиатуры.
Найти среднее арифметическое элементов списка.
"""
import random
n = int(input("введите размер списка: "))
spisok = []
for i in range(n):
    a = random.randint(0, 99)
    spisok.append(a)
    s = sum(spisok)
    avg_sum = s/n
print("Список: ", spisok)
print("Среднее арифметическое элементов списка: ", avg_sum)