# Вводим слово
word = input("Введите слово: ")

# Определяем количество гласных и согласных
vowels = "aeiou"
num_vowels = sum(1 for char in word if char in vowels)
num_consonants = len(word) - num_vowels

print(f"Гласных букв: {num_vowels}")
print(f"Согласных букв: {num_consonants}")

# Проверяем наличие каждой гласной
for vowel in vowels:
    print(f"{vowel}: {vowel in word}")
