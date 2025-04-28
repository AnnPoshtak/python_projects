from tkinter import*
import random
pep=0
che=0
gav=0
sik=0
v = 0

tk = Tk()
tk.geometry("500x150")
tk.title("Гра піцерія")
ent = Entry(justify='left', font = "10")
ent.place(x=20, y =20, width = 450, height=30)
ent.insert(END,"            Оберіть мову/choose a language")

def Ua_click ():
    ent.delete(0,END)
    btnUa.place_forget()
    btnEn.place_forget()

    ## варіанти привітання
    pryvit = ["Привіт! Можна мені ", "Доброго дня! Можна мені ", "Салют! Дай мені ", "Здоровенькі були! Дайте мені ",
              "Вітаю! Можна мені "]

    ## Варіань замовлення
    zamovlenia = ["піцу пепероні", "сирну піцу", "гавайську піцу", "сік"]
    ent.insert(END, random.choice(pryvit) + random.choice(zamovlenia))

    ## Кнопки
    def btnPep_click():
        global pep
        ent.delete(0, END)
        ent.insert(END, random.choice(pryvit) + random.choice(zamovlenia))
        pep += 1

    btnPep = Button(text="Пепероні", font="14", command=btnPep_click)
    btnPep.place(x=20, y=70, width=100, height=50)

    def btnChe_click():
        global che
        ent.delete(0, END)
        ent.insert(END, random.choice(pryvit) + random.choice(zamovlenia))
        che += 1

    btnChe = Button(text="Сирна", font="14", command=btnChe_click)
    btnChe.place(x=130, y=70, width=100, height=50)

    def btnGav_click():
        global gav
        ent.delete(0, END)
        ent.insert(END, random.choice(pryvit) + random.choice(zamovlenia))
        gav += 1

    btnGav = Button(text="Гавайська", font="5", command=btnGav_click)
    btnGav.place(x=240, y=70, width=100, height=50)

    def btnSik_click():
        global sik
        ent.delete(0, END)
        ent.insert(END, random.choice(pryvit) + random.choice(zamovlenia))
        sik += 1

    btnSik = Button(text="Сік", font="14", command=btnSik_click)
    btnSik.place(x=350, y=70, width=100, height=50)

    def Finish_click():
        global v
        btnPep.place_forget()
        btnChe.place_forget()
        btnGav.place_forget()
        btnSik.place_forget()
        btnFin.place_forget()
        ent.place_forget()
        v = pep + che + gav + sik
        label1 = Label(tk, text="Результати гри:", font="14")
        label1.place(x=20, y=5)
        label2 = Label(tk, text="Видано пепероні: " + str(pep), font="14")
        label2.place(x=20, y=35)
        label3 = Label(tk, text="Видано сирної: " + str(che), font="14")
        label3.place(x=20, y=65)
        label4 = Label(tk, text="Видано гавайської: " + str(gav), font="14")
        label4.place(x=20, y=95)
        label5 = Label(tk, text="Видано соку: " + str(sik), font="14")
        label5.place(x=20, y=125)
        label6 = Label(tk, text="Всього видано: " + str(v), font="14")
        label6.place(x=250, y=5)

    btnFin = Button(text="стоп", font="5", bg="red", command=Finish_click)
    btnFin.place(x=450, y=110, width=50, height=50)
btnUa = Button(text="Українська",font="14",command=Ua_click)
btnUa.place(x=80, y=70, width=150, height=50)
def en_click ():
    ent.delete(0, END)
    btnUa.place_forget()
    btnEn.place_forget()
    ## варіанти привітання
    pryvit = ["Hi! Can I have ", "Hello! Can I have ", "What's up? Can i get ", "Good morning! Can i get ",
              "Hey there! Can I have "]

    ## Варіань замовлення
    zamovlenia = ["pepperoni", "cheese pizza", "hawaiian pizza", "juice"]
    ent.insert(END, random.choice(pryvit) + random.choice(zamovlenia))

    ## Кнопки
    def btnPep_click():
        global pep
        ent.delete(0, END)
        ent.insert(END, random.choice(pryvit) + random.choice(zamovlenia))
        pep += 1

    btnPep = Button(text="pepperoni", font="14", command=btnPep_click)
    btnPep.place(x=20, y=70, width=100, height=50)

    def btnChe_click():
        global che
        ent.delete(0, END)
        ent.insert(END, random.choice(pryvit) + random.choice(zamovlenia))
        che += 1

    btnChe = Button(text="Cheese", font="14", command=btnChe_click)
    btnChe.place(x=130, y=70, width=100, height=50)

    def btnHaw_click():
        global gav
        ent.delete(0, END)
        ent.insert(END, random.choice(pryvit) + random.choice(zamovlenia))
        gav += 1

    btnHaw = Button(text="Hawaiian", font="5", command=btnHaw_click)
    btnHaw.place(x=240, y=70, width=100, height=50)

    def btnJu_click():
        global sik
        ent.delete(0, END)
        ent.insert(END, random.choice(pryvit) + random.choice(zamovlenia))
        sik += 1

    btnJu = Button(text="juice", font="14", command=btnJu_click)
    btnJu.place(x=350, y=70, width=100, height=50)

    def Finish_click():
        global v
        btnPep.place_forget()
        btnChe.place_forget()
        btnHaw.place_forget()
        btnJu.place_forget()
        btnFin.place_forget()
        ent.place_forget()
        v = pep + che + gav + sik
        label1 = Label(tk, text="The results of the game:", font="14")
        label1.place(x=20, y=5)
        label2 = Label(tk, text="Pepperoni served: " + str(pep), font="14")
        label2.place(x=20, y=35)
        label3 = Label(tk, text="Cheese served: " + str(che), font="14")
        label3.place(x=20, y=65)
        label4 = Label(tk, text="Hawaiian served: " + str(gav), font="14")
        label4.place(x=20, y=95)
        label5 = Label(tk, text="Juice served: " + str(sik), font="14")
        label5.place(x=20, y=125)
        label6 = Label(tk, text="Total served:  " + str(v), font="14")
        label6.place(x=250, y=5)

    btnFin = Button(text="stop", font="5", bg="red", command=Finish_click)
    btnFin.place(x=450, y=110, width=50, height=50)
    tk.mainloop()
btnEn = Button(text="English",font="14",command=en_click)
btnEn.place(x=250, y=70, width=150, height=50)
tk.mainloop()