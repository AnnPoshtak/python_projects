r = int(input("Введи розмір трикутника"))
p=0
s=""
while p<r:
    s+="*"
    p+=1
p=0
while p<r:
    print(s)
    s=s[: -1]
    p+=1
