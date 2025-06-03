month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
day = int(input("What's the day today?"))
month = int(input("What's the number of month?"))
j = 1
theDayOfYear = 0
for i in range(month-1):
    theDayOfYear += month_days[j]
    j+=1
theDayOfYear+=day
theDayOfYear = str(theDayOfYear)
theDayOfYear += "-й день року"
print("Зараз",theDayOfYear)