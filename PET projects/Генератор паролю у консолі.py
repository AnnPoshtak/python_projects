import random
lettersBig = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lettersLittle = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
number = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','%','&','*','{','~']
number2 = ['1','2','3','4','5','6','7','8','9','0']
long = int(input("Введіть довжину паролю "))
password = [""] * long
password1 = ''
i = 0
total = 0
while i<long:
    password[i] += random.choice(lettersBig)
    total += 1
    if total == long:
        break
    password[i] += random.choice(lettersLittle)
    total += 1
    if total == long:
        break
    password[i] += random.choice(number)
    total += 1
    if total == long:
        break
    password[i] += random.choice(symbols)
    total += 1
    if total == long:
        break
    password[i] += random.choice(number2)
    total += 1
    if total == long:
        break
    i+=1
random.shuffle(password)
i = 0
while i<long:
    password1 += password[i]
    i+=1
print(password1)
