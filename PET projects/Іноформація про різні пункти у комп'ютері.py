from tkinter import*
from tkinter import messagebox
tk = Tk()
tk.geometry("250x300")
page = 0
name = ['Bios','Linux','MBR','GPT','File System','Bootloader','Kernel','UEFI']
description = ['BIOS—стара система запуску комп’ютера.\n Працює ще з 1980-х.\nМає простий текстовий інтерфейс, \nпідтримує тільки мишу з клавіатурою,\n завантажує диски\n в режимі MBR (обмеження — до 2 ТБ).','Linux — це операційна система,\n як Windows, але вільна й відкрита.\n Використовується на серверах,\n комп’ютерах, \nтелефонах, навіть в техніці.\n Популярні дистрибутиви — \nUbuntu, Debian, \nArch тощо.','MBR — старий спосіб розмітки диска. \nОбмеження — до 2 ТБ, \nмаксимум 4 основні розділи.\n Часто використовується з BIOS.','GPT— новий стандарт розмітки диска. \nПідтримує великі диски (до 9 зетабайтів),\n багато розділів. \nПрацює з UEFI.','File System — спосіб організації даних \nна диску. \nУ Linux часто використовуються \next4, Btrfs, XFS.\n Це як структура \nполиць у шафі для файлів.','Bootloader (Завантажувач) — програма, \nщо запускає ядро Linux. \nВін зявляється першим після \nBIOS/UEFI й\n дозволяє вибрати систему, \nякщо їх декілька.','Kernel (Ядро) — основна частина Linux, \nщо керує \n"залізом" (процесором, пам’яттю тощо)\n і передає дані між \nпрограмами та обладнанням.','UEFI — новіша заміна BIOS.\n Має сучасний вигляд, \nпідтримує великі диски (GPT),\n працює швидше,\n може використовувати мишу,\n має кращий захист.']
labelName = Label(text=name[0])
labelName.place(x=100,y=10)
labelDe = Label(text=description[0])
labelDe.place(x=10,y=50)
def left():
    global page
    global name
    global description
    page -=1
    if page==-1:
        page=len(name)
    if page == 0:
        labelName.configure(text=name[0])
        labelDe.configure(text=description[0])
    if page == 1:
        labelName.configure(text=name[1])
        labelDe.configure(text=description[1])
    if page == 2:
        labelName.configure(text=name[2])
        labelDe.configure(text=description[2])
    if page == 3:
        labelName.configure(text=name[3])
        labelDe.configure(text=description[3])
    if page == 4:
        labelName.configure(text=name[4])
        labelDe.configure(text=description[4])
    if page == 5:
        labelName.configure(text=name[5])
        labelDe.configure(text=description[5])
    if page == 6:
        labelName.configure(text=name[6])
        labelDe.configure(text=description[6])
    if page == 7:
        labelName.configure(text=name[7])
        labelDe.configure(text=description[7])
btnLeft = Button(text="←", command = left)
btnLeft.place(x=40,y=180,width=80,height=80)

def right():
    global page
    page +=1
    if page == len(description):
        page = 0
    if page == 0:
        labelName.configure(text=name[0])
        labelDe.configure(text=description[0])
    if page == 1:
        labelName.configure(text=name[1])
        labelDe.configure(text=description[1])
    if page == 2:
        labelName.configure(text=name[2])
        labelDe.configure(text=description[2])
    if page == 3:
        labelName.configure(text=name[3])
        labelDe.configure(text=description[3])
    if page == 4:
        labelName.configure(text=name[4])
        labelDe.configure(text=description[4])
    if page == 5:
        labelName.configure(text=name[5])
        labelDe.configure(text=description[5])
    if page == 6:
        labelName.configure(text=name[6])
        labelDe.configure(text=description[6])
    if page == 7:
        labelName.configure(text=name[7])
        labelDe.configure(text=description[7])
btnRight = Button(text="→",command = right)
btnRight.place(x=130,y=180,width=80,height=80)
tk.mainloop()