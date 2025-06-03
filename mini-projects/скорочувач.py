text = str(input("Введіть речення: "))
a =[0]*26
code = 0
index = 0
for k in range(len(text)):
    code = ord(text[k])
    if code>=65 and code<=90:
        index = code - 65
        a[index]+=1
    elif code>=97 and code<=122:
        index = code - 97
        a[index]+=1

for i in range(26):
    if a[i]>0:
        print(chr(i+65),a[i])