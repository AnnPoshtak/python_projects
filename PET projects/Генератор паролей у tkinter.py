from tkinter import*
from tkinter import messagebox
import random
import pyperclip
tk = Tk()
long = 0
test = 0
ent = Entry()
password1 =""
tk.geometry("200x200")
ent.place(x=10,y=10,width=180,height=25)
label1 = Label(text='Скільки символів повинно бути \n у вашому паролі?')
label1.place(x=10,y=40)
def g_click ():
    global long
    global test
    global password1
    if test == 1:
        pyperclip.copy(password1)
        messagebox.showinfo("Ваш парль скопійовано!","Ваш парль скопійовано!")
    long = int(ent.get())
    ent.delete(0, END)
    label1.configure(text="Ваш пароль готовий! \n Ви можете скопіювати його \n у буфер обміну")
    btn.configure(text="Скопіювати \n в буфер")
    lettersBig = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                  "U", "V", "W", "X", "Y", "Z"]
    lettersLittle = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                     "u", "v", "w", "x", "y", "z"]
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbols = ['!', '@', '#', '$', '%', '&', '*', '{', '~']
    password = [""] * long
    i = 0
    total = 0
    while i < long:
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
    random.shuffle(password)
    i = 0
    while i < long:
        password1 += password[i]
        i += 1
    ent.insert(END,password1)
    test+=1

btn = Button(text="Готово!",command=g_click)
btn.place(x=60,y=100,width=80,height=50)

tk.mainloop()