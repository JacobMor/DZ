# Задание 1
def my_fn(a, b):
    if b != 0:
        c = a / b
        print(round(c, 2))
    else:
        print("Error")


a = int(input("Введите 1 число"))
b = int(input("Введите 2 число"))
my_fn(a,b)


# задание 2
def user_fn(name, surname, b_date, sity, mail, tel):
    return {"Имя": name, "Фамилия": surname, "Дата рождения": b_date, "Город": sity, "Email": mail, "Телефон": tel}


name = input("Введите имя")
surname = input("Введите фамилию")
b_date = input("Введите дату рождения")
sity = input("Введите город")
mail = input("Введите email")
tel = input("Введите телефон")
d = user_fn(name, surname, b_date, sity, mail, tel)
for i in d:
    print(i, d.get(i))
#
# # задание 3
def my_fn(arg_1, arg_2, arg_3):
    a = [arg_1, arg_2, arg_3]
    a.remove(min(a))
    b = a[0]*a[1]
    return b


arg_1 = int(input("Введите число"))
arg_2 = int(input("Введите число"))
arg_3 = int(input("Введите число"))
print(my_fn(arg_1, arg_2, arg_3))
#
# #  задание 4
def my_func(x, y):
    x = int(x)
    y = int(y)
    m = x ** y
    return round(m, 4)


def my_func2(x, y):
    x = int(x)
    y = int(y)
    n = y + 1
    xx = x
    while n != 0:
        x = x * xx
        n += 1
    res = 1 / x
    return res

x = input("Введите 1 число")
y = input("Введите степень")
print(my_func2(x, y))
# #
# # задача 5
b = 0
n = []
while str not in n:
    n = list(input("Введите числа, для остановки введите букву").split())
    try:
        for i in n:
            b = b + int(i)
            print(b)
    except ValueError:
        print("Конечный результат ", b)
        break

# задача 6
def int_func(n):
    n = str(n.capitalize())
    return n
#
# # задача 7
text = input("Text?").split()
for i in text:
    i = int_func(i)
    print(i)