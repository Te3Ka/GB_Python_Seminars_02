'''
Задача No11. Решение в группах
Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
то есть выведите такое число n, что φ(n)=A.
Если А не является числом Фибоначчи, выведите число -1.
Input: 5 Output: 6
'''

num = int(input("Введите число Фибоначчи: "))

num1 = 1
num2 = 2
sumFib = num1 + num2
count = 4

if (num == num1):
    print("1 элемент")
elif (num == num2):
    print("2 элемент")
elif (num == sumFib):
    print("3 элемент")
else:
    while (sumFib < num):
        temp = sumFib
        num1 = num2
        num2 = temp
        sumFib = num1 + num2
        count += 1
    if (sumFib == num):
        print(f"Число {num} это {count} элемент последовательности Фибоначчи")
    else:
        print(f"Число {num} не принадлежит последовательности Фибоначчи")