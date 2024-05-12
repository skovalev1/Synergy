print("Введите стадии развития человека в порядке их происхождения.")
stages = []
for i in range(7):  # У нас есть 7 стадий развития
    stage = input(f"Введите стадию развития №{i+1}: ")
    stages.append(stage)

print("Стадии развития человека:")
print(*stages, sep=' => ')
