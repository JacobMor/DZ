# задание 1
print("Здравствуйте!")
name = input("Как Вас зовут?")
age = input("Введите Ваш возраст")
print("Здравствуйте " + name + "," + age + " лет от роду")

# задание 2
sec_input = int(input("Здравствуйте, задайте количество секунд"))
hour = sec_input // 3600
sec_est = sec_input % 3600
minutes = sec_est // 60
sec = int(sec_input % 60)
print(sec_input, "секунд составляют ", hour, ":", minutes, ":", sec)

# задание 3
n = int(input("Введите число n "))
n = n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n))
print(n)

# задание 4
count = int(input("Введите число"))
max_count = 0
while count / 10 > 0:
    new_count = count % 10
    count = count // 10
    if new_count > max_count:
        max_count = new_count
print("Максимальное число из выборки: ", max_count)

# задание 5
profit = int(input("Ваша выручка составляет: "))
costs = int(input("Издержки составляют: "))
result = profit - costs
if result > 0:
    print("Ваша прибыль составляет :", result)
elif result < 0:
    print("Ваш убыток составляет: ", result)
elif result == 0:
    print("Поздравляю, сработали понолям")

# задание 6

profit = int(input("Ваша выручка составляет: "))
costs = int(input("Издержки составляют: "))
result = profit - costs
if result > 0:
    print("Ваша прибыль составляет :", result)
    profitability = result / profit
    print("Рентабельность выручки составляет: ", '%.2f' % profitability)
    workers = int(input("Давайте расчитаем прибыль на человека, введите количество работников"))
    print("прибыль на человека: ", '%.2f' % (result / workers))
elif result < 0:
    print("Ваш убыток составляет: ", result)
elif result == 0:
    print("Поздравляю, сработали понолям")

# доп. задание 7
first_dist = int(input("Задайте количество километров в первый день"))
final_dist = int(input("Задайте требуемый результат"))
day = 1
print(day, "день: ", first_dist)
while first_dist < final_dist:
    first_dist = first_dist + (first_dist * 10 / 100)
    day = day + 1
    print(day, " день: ", first_dist)
print("Для достижения результата потребуется", day, " дней")
