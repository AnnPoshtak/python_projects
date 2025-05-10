def malui_bagato_symvoliv (shoMaluvaty, skikRaziv) :
     s = ""

     i = 0
     while i < skikRaziv:
         s += shoMaluvaty
         i+=1
     return s;
def zapytaty_masyv () :
    masyv = [0]*8
    i = 0
    while i<20:
        masyv[i]=int(input("Ведіть будь-яке число. 0 - це кінець"))
        if masyv[i] == 0:
            break
        i+=1
    return masyv
def znaidy_naibilshe_chyslo (a):
    m = 0
    i = 0
    while i < len(a):
        if m<a[i]:
            m=a[i]
        i+=1
    return m
def namalui_vidtsentrovanu_fihyrku (a, max):
    i = 0
    while i < len(a):
        print(malui_bagato_symvoliv(" ",(max-a[i])/2),malui_bagato_symvoliv("*",a[i]))
        i+=1
def main():
    a = zapytaty_masyv()
    max = znaidy_naibilshe_chyslo(a)
    namalui_vidtsentrovanu_fihyrku(a, max)
main()