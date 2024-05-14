# Вводим последовательность чисел и преобразуем их в список
numbers = list(map(int, input().split()))

# Создаем пустое множество для хранения уникальных чисел
seen = set()

# Проходим по всем числам в списке
for number in numbers:
    # Если число уже встречалось ранее
    if number in seen:
        print('YES')
    # Если число встречается впервые
    else:
        print('NO')
        # Добавляем число в множество уникальных чисел
        seen.add(number)