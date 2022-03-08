# задача 1

with open(r'new.txt', 'a', encoding='utf-8') as f:
    n = input('Enter data')
    while n != "":
        f.write(n + '\n')
        n = input('Enter data')

# задача 2
with open(r'new.txt', 'r', encoding='utf-8') as f:
    ls = f.readlines()
    print("Общее количество строк ", len(ls))
    n = 0
    for i in ls:
        i = len(i.split())
        n += 1
        print("В", n,"строке", i, "слов")

#  задача 3
with open(r'new.txt', 'r', encoding='utf-8') as f:
    pair = f.readlines()
    result_di = {}
    print("Сотрудники с зарплатой ниже 20 тысяч:")
    for i in pair:
        n = i.split()
        temp_di = {n[0]: n[1]}
        result_di.update(temp_di)
    for i, d in result_di.items():
        d = float(d)
        if d < 20000:
            print(i, d)
    n = 0
    tot_cash = 0
    for i in result_di.values():
        i = float(i)
        tot_cash += i
        n += 1
    med_cash = tot_cash / n
    print("Средний заработок составил:" + "\n",med_cash)

# задача 4
rep_dict = dict(One='Один', Two='Два', Three='Три', Four='Четыре')
with open(r'newTextFile2.txt', 'r', encoding='utf-8') as f:
    ls = f.readlines()
    for line in ls:
        line = line.split()
        line[0] = rep_dict.get(line[0])
        for i in line:
            with open(r'TranslatedFile.txt', 'a', encoding='utf-8') as k:
                k.write(i)
        with open(r'TranslatedFile.txt', 'a', encoding='utf-8') as k:
            k.write('\n')
#
# задача 5
with open(r'task5.txt', 'w', encoding='utf-8') as f:
    f.write(input("Вводите цифры"))

with open(r'task5.txt', 'r', encoding='utf-8') as f:
    ls = f.readline()
    ls = ls.split()
    n = 0
    for i in ls:
        n += int(i)
    print("Сумма чисел равна", n)
#
# задача 6
with open(r'task6.txt', 'r', encoding='utf-8') as f:
    ls = f.readlines()
    new_dict = {}
    my_dict = {}
    for line in ls:
        line = line.split()
        new_dict[line[0]] = line[1:]
    n = 0
    for keys, values in new_dict.items():
        for i in values:
            try:
                i = i.split('(')
                i.pop(1)
                i = [int(x) for x in i]
                n += i[0]
            except IndexError:
                pass
        my_dict[keys] = n
        n = 0
    print(my_dict)
#
# задача 7
with open(r'task7.txt', 'r', encoding='utf-8') as f:
    ls = f.readlines()
    profit_dict = {}
    aveprofit_dict = {}
    for i in ls:
        i = i.split()
        profit_dict[i[0]] = (int(i[2]) - int(i[3]))
    n = 0 # счетчик общей прибыли
    d = 0 # счетчик количества слагаемых
    for values in profit_dict.values():
        if values > 0:
            n += values
            d += 1
    av_profit = n / d
    aveprofit_dict['average profit'] = av_profit
    general_list = [profit_dict, aveprofit_dict]
    import json
    with open(r'jsonTask7.json', 'w', encoding='utf-8') as file:
        json.dump(general_list, file)
