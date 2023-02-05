# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

import random
import math

print('Введите число N: ')
size = int(input())
arr = []
for i in range(size):
    randomNum = random.randint(1, 10)
    arr.append(randomNum)
print(arr)

print('Введите число X: ')
number = int(input())
diff = abs(number - arr[0])
if diff == 0:
    diff = 1
NumberA = -1
NumberB = -1
for i  in range(len(arr)):
    if diff > abs(number - arr[i]):
        if number - arr[i] > 0:
            diff = number - arr[i]
            NumberA = arr[i]
        if number - arr[i] < 0:
            diff = abs(number - arr[i])
            NumberB = arr[i]
    if diff == abs(number - arr[i]):
        if number - arr[i] > 0:
            NumberA = arr[i]
        if number - arr[i] < 0:
            NumberB = arr[i]
if NumberB == -1:
    print('Ближайшее число к искомому: ' + str(NumberA))
elif NumberA == -1:
    print('Ближайшее число к искомому: ' + str(NumberB))
