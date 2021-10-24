# По введенному числу (от 0 до 7) напечатать название цифры.
def digits():
    digit = int(input("Введите число от 0 до 7: "))
    if 0 <= digit <= 7:
        if digit == 0:
            print("Ноль")
        if digit == 1:
            print("Один")
        if digit == 2:
            print("Два")
        if digit == 3:
            print("Три")
        if digit == 4:
            print("Четыре")
        if digit == 5:
            print("Пять")
        if digit == 6:
            print("Шесть")
        if digit == 7:
            print("Семь")
    else:
        print("число не соответствует параметрам, проверьте введённое число")

digits()
