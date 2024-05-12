# Вводим суммы инвестиций
X = float(input("Введите минимальную сумму инвестиций: "))
A = float(input("Введите сумму инвестиций Майкла: "))
B = float(input("Введите сумму инвестиций Ивана: "))

# Определяем, кто может инвестировать
if A >= X and B >= X:
    print(2)
elif A >= X:
    print("Mike")
elif B >= X:
    print("Ivan")
elif A + B >= X:
    print(1)
else:
    print(0)
