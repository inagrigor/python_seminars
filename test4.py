# Последовательностью Фибоначчи называется последовательность чисел a0 , a1 , ..., an , ..., 
# где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). 
# Требуется найти N-е число Фибоначчи 
# Input: 7 Output: 21 
# Задание необходимо решать через рекурсию 

# n = int(input())
# def fib(n):
#     if n in [1,2]:
#         return 1
#     return fib(n - 1) + fib(n - 2)

# list_1 = []
# for i in range(1,10):
#     list_1.append(fib(i))

#     if n == 0 or n == 1:
#         return 1
#     return fib(n - 1) + fib(n - 2)

# print(fib(n))

# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные. 
# Input: 5 -> 1 3 3 3 4 Output: 1 3 3 3 1
# n = int(input())
# list = list()
# for i in range(n):
#     x = int(input())
#     list.append(x)
    
# max_n = max(list)
# min_n = min(list)
# for i in range(len(list)):
#     if list[i] == max_n:
#         list[i] = min_n
# print(list)

# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым Напоминание: 
# Простое число - это число, которое имеет 2 делителя: 1  и n(само число) 
# Input: 5 Output: yes

# n = int(input())
# def f(n):
#     flag = True
#     i = 2
#     while i < n and flag:
#         if n % i == 0:
#             flag = False
#         i += 1
#     if flag:
#         return 'yes'
#     else:
#         return 'no'
# print(f(n))

# Дано натуральное число N и последовательность из N элементов. 
# Требуется вывести эту последовательность в обратном порядке. 
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
# Input:    2 -> 3 4 
# Output: 4 3

# def F(n):
#     if n == 0:
#         return ''
#     k = int(input())
#     return F(n - 1) + F'{k}'
# #        ' ' + '3'  + ' 4' 
# n = int(input())
# print(F(n))

# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую 
# степень B с помощью рекурсии.
# a = int(input())
# b = int(input())
# def f(a, b):
#     if b == 0:
#         return 1
#     elif b < 0:
#       return 1 /f(a,  - b)
#     else:
#         return a * f(a, b - 1)
# print(f(a, b))

# def f(a, b):
#   if b == 0:
#     return 1
#   return f(a, b - 1) * a

# 8: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# a = int(input())
# b = int(input())
# def sum(a, b):
#     if b == 0:
#         return a
#     else:
#         return 1 + sum(a, b - 1)
# print(sum(a, b))

# def sum_recursive(n):
"""
    Функция sum_recursive вычисляет сумму всех целых чисел от 1 до n включительно.

    Аргументы:
    - n: целое число, для которого вычисляется сумма всех целых чисел от 1 до n.

    Возвращаемое значение:
    - Сумма всех целых чисел от 1 до n.

    Примечание:
    Функция использует рекурсивный подход для вычисления суммы. Базовый случай
    достигается, когда n равно 1, в этом случае возвращается 1. В рекурсивном случае,
    функция вызывает себя для n-1 и прибавляет к этому результату значение n.
    """
    # Базовый случай: если n равно 1, возвращаем 1
    # if n == 1:
    #     return 1
    # Рекурсивный случай: суммируем числа от 1 до n-1 и добавляем n
    # else:
        # Рекурсивно вызываем sum_recursive для n-1 и прибавляем к этому значению n
        # return n + sum_recursive(n - 1)

# Пример использования функции
# result = sum_recursive(5)
# print("Сумма чисел от 1 до 5 равна:", result)

# Даны два массива чисел. Требуется вывести те элементы первого массива 
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. 
# Пользователь вводит  число N - количество элементов в первом массиве, затем 
# N чисел - элементы массива. Затем число M - количество элементов во втором массиве. 
# Затем элементы второго 
# Ввод: 7 
# 3 1 3 4 2 4 12 
# 6 
# 4 15 43 1 15 1 
# Вывод: 3 3 2 12 массива 
# (каждое число вводится с новой строки) 
# n = int(input())
# list1 = list()
# for i in range(n):
#     x = int(input())
#     list1.append(x)


# m = int(input())
# list2 = list()
# for j in range(m):
#     x = int(input())
#     list2.append(x)

# k = 0  
 
# for i in range(n):
#     for j in range(m):
#         if list1[i] == list2[j]:
#              k += 1
#     if k == 0:
#         print(list1[i])
#     k = 0
   
     
# Дан массив, состоящий из целых чисел. 
# Напишите программу, которая в данном массиве определит количество элементов, 
# у которых два соседних и, при этом, оба соседних элемента меньше данного. 
# Сначала вводится число N — количество элементов в массиве  
# Далее записаны N чисел — элементы массива. 
# Массив состоит из целых чисел. 
# Ввод: 5
#  1 2 3 4 5 
#                 Ввод: 5 
#                   1 5 1 5 1 
# Вывод: 0
#                 Вывод:  2

# n = int(input())
# list1 = list()
# for i in range(n):
#     x = int(input())
#     list1.append(x)
# count = 0
# for i in range(1, n-1):
#     # if i - 1 < i and i + 1 < i:
#     if list1[i - 1] < list1[i] > list1[i + 1]:
#         count += 1
        
# print(count)

# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. 
# Вводится список чисел. Все числа списка находятся на разных строках. 
# Ввод: 1 2 3 2 3 
# Вывод: 2
# list = [1, 2, 3, 2, 3 ]
# count = 0

# for i in range(len(list)):
#     for j in range(i + 1, len(list)):
#         if i != j and list[i] == list[j]:
#             count += 1

# print(count)
    
 
# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n 
# (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа. 
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. 
# Программа получает на вход одно натуральное число k, не превосходящее 10^5. Программа должна 
# вывести  все пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо 
# выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только один 
# раз (перестановка чисел новую пару не дает). 
# Ввод:  300
# Вывод: 220 284

# def sum_of_divisors(n):
#     divisors_sum = 0
#     for i in range(1, n):
#         if n % i == 0:
#             divisors_sum += i
#     return divisors_sum

# def find_friend_numbers(k):
#     for n in range(1, k + 1):
#         sum_n = sum_of_divisors(n)
#         if sum_n <= k:  # Проверяем, чтобы сумма делителей n была не больше k
#             sum_m = sum_of_divisors(sum_n)
#             if sum_m == n and n < sum_n:  # Проверяем, что сумма делителей m равна n и m > n, чтобы избежать повторений
#                 print(f"Дружественная пара: ({n}, {sum_n})")

# k = int(input("Введите число k: "))
# find_friend_numbers(k)

# k = int(input())
# list1 = list()

# for i in range(k): #perebiraet vse znacenia ot 0 do k
#     summa = 0
#     for j in range(1, i // 2 + 1): #perebiraet vse vozmojnie deliteli, budem deliti i na j i proveriati delitsea uli net
#         if i % j == 0:
#             summa += j
#     list1.append(tuple([i, summa])) # (5, 1) cislo = 5, deliteli =1; (6,6) - cislo = 6, summa delitelei - 1+2+3
# # print(list1)
# for i in range(len(list1)): 
#     for j in range(i, len(list1)):
#         if i != j and list1[i][0] ==list1[j][1] and list1[i][1] == list1[j][0]:
#             # print(list1[i])
#             print(*list1[i]) # * - raspacovca corteja

# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума).
# На вход подается список с элементами list_1 и границы диапазона в виде чисел min_number, max_number.На входе:


# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = 0
# max_number = 10

# for i in range(len(list_1)):
#     if min_number <=list_1[i] <= max_number:
#         print(i)
        
        
# заполните массив элементами арифметической прогрессии. 
# Её первый элемент a1 , разность d и количество элементов n будет задано автоматически. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# На входе:
# На выходе:
# 2
# 5
# 8
# 11
# a1 = 2
# d = 3
# n = 4
# list1 = []
# for i in range(n):
#     list1.append(a1 + i * d)
# print(list1)
# progression = []  # Создаем пустой массив для хранения элементов прогрессии

# for i in range(n):
#     an = a1 + i * d  # Формула для вычисления n-го члена прогрессии
#     progression.append(an)  # Добавляем вычисленный элемент в массив

# for element in progression:
#     print(element)