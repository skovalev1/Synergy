# Вводим число N
N = int(input())

# Вводим N чисел и преобразуем их в список
numbers = list(map(int, input().split()))

# Создаем новый список, где на первом месте стоит последний элемент, на втором - первый, на третьем - второй и т. д.
new_numbers = [numbers[-1]] + numbers[:-1]

# Выводим измененный список
for number in new_numbers:
    print(number)
