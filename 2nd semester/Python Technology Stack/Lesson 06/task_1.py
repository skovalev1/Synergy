# Вводим число N
N = int(input("Введите число N: "))

# Вводим N чисел и подсчитываем количество нулей
count = 0
for i in range(N):
    num = int(input(f"Введите число №{i+1}: "))
    if num == 0:
        count += 1

print(f"Количество нулей: {count}")
