# Вводим числа A и B
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

# Выводим все четные числа на заданном отрезке
for num in range(A, B + 1):
    if num % 2 == 0:
        print(num, end=' ')
