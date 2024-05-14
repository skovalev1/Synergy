# Вводим число N
N = int(input())

# Проверяем, что N удовлетворяет условию задачи
if not 1 <= N <= 10000:
    print("Ошибка: N должно быть в диапазоне от 1 до 10000")
else:
    # Создаем пустой список
    numbers = []

    # Вводим N чисел и добавляем их в список
    for _ in range(N):
        number = int(input())
        # Проверяем, что число удовлетворяет условию задачи
        if abs(number) > 10**5:
            print("Ошибка: число должно быть по модулю не больше 10^5")
            break
        numbers.append(number)
    else:
        # Переворачиваем список
        numbers.reverse()

        # Выводим перевернутый список
        for number in numbers:
            print(number)
