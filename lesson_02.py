# Задача 1
data = [56, 234, "привет", "как дела", 77, 999, 1]
for objects in data:
    print((objects), type(objects))

# задача 2
data = []
cont = input("Введите информацию, если ввод закончен, введите 'stop'")
while "stop" != cont:
    data.append(cont)
    cont = input("Введите информацию, если ввод закончен, введите 'stop'")
print("Ввод закончен")
print(data)
n = 0
for i in range(int(len(data) / 2)):
    data[n], data[n + 1] = data[n + 1], data[n]
    n += 2
print(data)

# задача 3

months_di = dict(
    [(1, "январь"), (2, "февраль"), (3, "март"), (4, "апрель"), (5, "май"), (6, "июнь"), (7, "июль"), (8, "август"),
     (9, "сентябрь"), (10, "октябрь"), (11, "ноябрь"), (12, "декабрь")])
seasons_di = list(["зима", "весна", "лето", "осень"])
cont = int(input("Введите месяц'число'"))
while months_di.get(cont) is None:
    cont = int(input("неправильное значение, попробуйте снова"))
if cont == 12 or cont == 1 or cont == 2:
    print("Это ", months_di.get(cont)," времени года ", seasons_di[0])
elif cont == 3 or cont == 4 or cont == 5:
    print("Это ", months_di.get(cont), " времени года ", seasons_di[1])
elif cont == 6 or cont == 7 or cont == 8:
    print("Это ", months_di.get(cont), " времени года ", seasons_di[2])
elif cont == 9 or cont == 10 or cont == 11:
    print("Это ", months_di.get(cont), " времени года ", seasons_di[3])

# задача 4
words = input("Введите несколько слов, используя пробел")
words = words.split()
n = 1
for i in words[:]:
    print(n, "", i[0:10])
    n += 1

# задача 5
my_list = [7, 5, 3, 3, 2]
cont = ()
while "stop" != cont:
    cont = input("Введите информацию, если ввод закончен, введите 'stop'")
    if cont == str(cont):
        cont = input("Неправильное значение, введите цифру, если ввод закончен, введите 'stop'")
    my_list.append(int(cont))
    print(sorted(my_list, reverse=True))


