from tkinter import*
tk = Tk()
tk.configure(bg="#c7dfff")
ent = Entry(font="30")
ent.place(x=300, y =70, width=100, height=50)
color = ""

tk.geometry("500x300")
l1 = Label(text="BSOD налаштування",font="50")
l1.place(x=150, y=10)
l2 = Label(text="Введіть колір BSDO(hex):",font="30")
l2.place(x=30, y=80)
l3 = Label(text="*Відразу після натиску на кнопку, відкриється вікно на весь екран.\n Щоб зменшити його варто натиснути кнопку Esc")
l3.place(x=50,y=200)
l1.configure(bg="#c7dfff")
l2.configure(bg="#c7dfff")
l3.configure(bg="#c7dfff")
def start():
    global color
    print("Hello!")
    color = ent.get()
    print(color)
    if color =="":
        color = "#0078d7"
    tk.configure(bg=color)
    l1.place_forget()
    l2.place_forget()
    l3.place_forget()
    ent.place_forget()
    start.place_forget()
    tk.attributes('-fullscreen',True)
    def exit_fullscreen(event=None):
        tk.attributes('-fullscreen', False)
    tk.bind("<Escape>", exit_fullscreen)
start = Button(text="Почати",font="50",command=start)
start.place(x=200,y=150,width=100,height=50)
tk.mainloop()