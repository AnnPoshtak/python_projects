import random
words = str(input("Введи слова через пробіл"))
array = words.split()
howMany = int(input("Скільки слів після перемішування ви хочете отримати"))
random.shuffle(array)
for i in range(howMany):
    print(array[i])