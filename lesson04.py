# задача 1
from sys import argv

path, working_hour, st, prem = argv
working_hour, st, prem = map(int, argv[1:])
result = (working_hour * st) + prem
print(result)

# задача 2
ls = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_ls = [ls[el] for el in range(1, len(ls)) if ls[el] > ls[el-1]]
print(new_ls)
#
# задача 3
list = [el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0]
print(list)
#
# задача 4
ls = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [el for el in ls if ls.count(el) == 1]
print(new_list)
#
# задача 5
from functools import reduce
ls = [el for el in range(100, 1001) if el % 2 == 0]
new_ls = reduce(lambda x, y: x * y, ls)
print(new_ls)
#
# задача 6
from sys import argv

path, start_numb = argv
start_numb = int(start_numb)
from itertools import count
from itertools import cycle

ls = []

for el in count(start_numb):
    if el > 10:
        break
    else:
        print(el)
        ls.append(el)
print(ls)
c = 1
for el in cycle(ls):
    if c > 10:
        break
    else:
        print(el)
        c += 1
#
# задача 7
from itertools import count
from math import factorial
n = int(input("Конечное число "))

def gen(n):
    for el in count(1):
        if el > n:
            break
        else:
            yield el
for el in gen(n):
    print(factorial(el))