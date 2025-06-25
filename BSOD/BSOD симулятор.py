from tkinter import*
import random
code = ["CRITICAL_PROCESS_DIED","MEMORY_MANAGEMENT","KERNEL_DATA_INPAGE_ERROR","IRQL_NOT_LESS_OR_EQUAL","TOO_MANY_CATS","GOD_MODE_ACTIVATED","BLUE_SCREEN_OF_APOCALYPSE"]
def exit_fullscreen(event=None):
    tk.attributes('-fullscreen', False)
tk = Tk()
tk.configure(bg="#c7dfff")
ent1 = Entry(font="30")
ent1.place(x=300, y =70, width=100, height=50)
ent2 = Entry()
ent2.place(x=300, y =130, width=100, height=50)
color = ""
time = ""

def BSOD():
    l1.place_forget()
    l2.place_forget()
    l3.place_forget()
    l_time.place_forget()
    ent1.place_forget()
    start.place_forget()
    ent2.place_forget()

    tk.deiconify()
    tk.configure(bg=color)
    tk.attributes('-fullscreen',True)
    tk.bind("<Escape>", exit_fullscreen)
    l_smile = Label(text=":(",font="Arial, 100")
    l_smile.configure(bg=color,fg="white")
    l_smile.place(x=200,y=100)
    l_text = Label(text="Your PC ran into a problem and needs to restart. We're just \n collecting some error info, and then we'll restart for you         ", font="Arial, 30")
    l_text.configure(bg=color,fg="white")
    l_text.place(x=200,y=270)
    l_stop_code = Label(text="Stop code:"+random.choice(code),font="Arial, 20")
    l_stop_code.configure(bg=color, fg="white")
    l_stop_code.place(x=200,y=400)

tk.geometry("500x300")
l1 = Label(text="BSOD налаштування",font="50")
l1.place(x=150, y=10)
l2 = Label(text="Введіть колір BSDO(hex):",font="30")
l2.place(x=30, y=80)
l_time = Label(text="Через скільки секунд \nз'явиться BSOD:",font="30")
l_time.place(x=30,y=130)
l3 = Label(text="*BSOD з'явиться через той час, який ви вказали. Щоб почати відлік натисніть на кнопку.\n Коли час вийде відкриється вікно на весь екран.\n Щоб зменшити його варто натиснути кнопку Esc")
l3.place(x=10,y=250)
l1.configure(bg="#c7dfff")
l2.configure(bg="#c7dfff")
l3.configure(bg="#c7dfff")
l_time.configure(bg="#c7dfff")
def start_bsod():
    global color, time
    color = ent1.get()
    time = ent2.get()
    if color =="":
        color = "#0078d7"
    tk.after(int(time)*1000, BSOD)
    tk.withdraw()

start = Button(text="Почати",font="50",command=start_bsod)
start.place(x=200,y=200,width=100,height=50)
tk.mainloop()