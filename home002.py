
#Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.

# num = -0.11111111
num = float(input())
num = abs(num)
# if num < 0:
#     num *= (-1)
# print(num)

sum = 0
if num - int(num) != 0:
    while (num - int(num)) > 0.00000000001: # маленькая дробь вместо нуля из-за особенностей хранения чисел в питоне
        num *= 10 
    num = int(num)

while num > 0:
    sum += num % 10
    num //= 10
print(sum)


# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.

# N = 6
# list = []

# матмодуль
# import math
# for i in range(1, N + 1):
#     list.append(math.factorial(i))

# цикл
# fact = 1
# for i in range(1, N + 1):
#     fact *= i
#     list.append(fact)

# рекурсия
# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return fact(n-1)*n
# for i in range(1, N + 1):
#     list.append(fact(i))

# print(list)


# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ 
# и выведите на экран их сумму.
# (1 + 1/n ) ^n

# n = int(input())
# list = []
# for i in range(1, n + 1):
#     k = round((1 + 1/i)**i, 3)
#     list.append(k)
# print(list)
# sum = 0
# for i in list:
#     sum += i
# print(sum)
