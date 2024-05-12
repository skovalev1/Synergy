# Вводим пятизначное число
num = int(input("Введите пятизначное число: "))

# Извлекаем каждую цифру
tens_of_thousands = num // 10000
thousands = (num // 1000) % 10
hundreds = (num // 100) % 10
tens = (num // 10) % 10
units = num % 10

# Вычисляем результат
result = (tens ** units * hundreds) / (tens_of_thousands - thousands)

print(f"Результат: {result}")
