from tkinter import*
from tkinter import messagebox
import webbrowser
import time
password = 123
import pyautogui
password1 = ""
tk = Tk()
ent = Entry()
tk.geometry("450x200")
tk.title("Хакери!")
tk.configure(bg="black")
ent.place(x=50,y=50,width=330,height=20)
labelLogin = Label(text="Введіть пароль для входу у систему")
labelLogin.place(x=50,y=10)
labelLogin.configure(bg="black",fg="Lime",font=15)

def login():
    global password
    global password1
    password1 = ""
    password1 = int(ent.get())
    if password != password1:
        messagebox.showinfo("Помилка","Не вірний пароль!")
        ent.delete(0,END)
    else:
        messagebox.showinfo("Пароль","Вірний пароль")
        messagebox.showinfo("Вхід", "Зачекайте! Запускаємо сервера для взлому!")
        ent.place_forget()
        btnLogin.place_forget()
        labelLogin.configure(text="Оберіть одні з функцій для взлому")
        def web():
            webbrowser.open("https://surl.lu/oqefuq")
        btnS = Button(text="Взломати сайт",command = web)
        btnS.place(x=50,y=50,width=150,height=50)
        btnS.configure(bg="Lime")
        def console():
            print("> access granted...")
            time.sleep(5)
            print("> initializing override protocol...")
            time.sleep(5)
            print("> ████████████████████████ 100%")
            time.sleep(5)
            print("> root@mainframe:~$ sudo ./hack_console.sh")
            time.sleep(5)
            print("> 🔓 SYSTEM OVERRIDE SUCCESSFUL")
            time.sleep(5)
            print("> 📡 CONNECTED TO NODE: 192.168.0.13")
            time.sleep(5)
            print("> 💾 DOWNLOADING: secret_data.txt")
            time.sleep(5)
            print("> ✔️ DOWNLOAD COMPLETE")
            time.sleep(5)
            print("> ☠️ WARNING: UNAUTHORIZED ACCESS DETECTED!")
            time.sleep(5)
            print("> 🧠 AI UPLINK ESTABLISHED...")
            messagebox.showinfo("Повідомлення","Консоль взламано!")
        btnConsole = Button(text="Взлом консолі",command = console)
        btnConsole.place(x=250,y=50,width=150,height=50)
        btnConsole.configure(bg="Lime")


        def zgornuty():
            pyautogui.hotkey("win","d")
        btnZgornuty = Button(text="Згорнути всі вікна",command =zgornuty)
        btnZgornuty.place(x=50,y=130,width=150,height=50)
        btnZgornuty.configure(bg="Lime")
        def q():
            messagebox.showwarning("Увага!","Вас викрили!")
            messagebox.showinfo("ХАХАХА","Жартую :)")
        btnQ = Button(text="???",command = q)
        btnQ.place(x=250,y=130,width=150,height=50)
        btnQ.configure(bg="Lime")


btnLogin = Button(text="Увійти",command = login)
btnLogin.place(x=170,y=100,width=100,height=50)
btnLogin.configure(bg="Lime")
tk.mainloop()