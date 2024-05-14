# Вводим число N
N = int(input())

# Создаем пустой список
numbers = []

# Вводим N чисел и добавляем их в список
for _ in range(N):
    numbers.append(int(input()))

# Переворачиваем список
numbers.reverse()

# Выводим перевернутый список
for number in numbers:
    print(number)
