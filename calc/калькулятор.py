from tkinter import*
tk=Tk()
a=0
b=0
s=0
z = 0
ent=Entry(justify="right",font="15")
tk.geometry("300x380")
tk.title("Калькулятор")
ent.place(x=10,y=15,width=280,height=30)

## Кнопки +-*/=С
def click_e():
    global a
    global b
    global s
    global z
    b=ent.get()
    ent.delete(0,END)
    if z=="+":
        s=float(a)+float(b)
        ent.insert(END,s)
    if z=="-":
        s=float(a)-float(b)
        ent.insert(END,s)
    if z=="*":
        s=float(a)*float(b)
        ent.insert(END,s)
    if z=="/":
        if float(b) == 0 :
            ent.insert(END,"На 0 ділити не можна!")
        if b !=0:
            s=float(a)/float(b)
            ent.insert(END, s)


btne = Button(text="=",font="15",command=click_e)
btne.place(x=10,y=50,width=85,height=70)

def c_click():
    global a
    global b
    global s
    ent.delete(0,END)
    a=0
    b=0
    s=0
btnc = Button(text="C",font="15",command=c_click)
btnc.place(x=110,y=50,width=85,height=70)

def click_p():
    global a
    global z
    a = ent.get()
    z="+"
    ent.delete(0,END)
btnp = Button(text="+",font="15",command=click_p)
btnp.place(x=210,y=50,width=85,height=70)

def click_m():
    global a
    global z
    a = ent.get()
    z="-"
    ent.delete(0,END)
btnm = Button(text="-",font="15",command=click_m)
btnm.place(x=210,y=145,width=85,height=70)

def click_po():
    global a
    global z
    a = ent.get()
    z="*"
    ent.delete(0,END)
btnpo = Button(text="*",font="15",command=click_po)
btnpo.place(x=210,y=225,width=85,height=70)

def click_pod():
    global a
    global z
    a = ent.get()
    z="/"
    ent.delete(0,END)
btnpod = Button(text="÷",font="15",command=click_pod)
btnpod.place(x=210,y=305,width=85,height=70)

## Кнопки 123
def click_1():
    ent.insert(END,"1")
btn1 = Button(text="1",font="15",command=click_1)
btn1.place(x=10,y=130,width=50,height=50)
def click_2():
    ent.insert(END,"2")
btn2 = Button(text="2",font="15",command=click_2)
btn2.place(x=80,y=130,width=50,height=50)
def click_3():
    ent.insert(END,"3")
btn3 = Button(text="3",font="15",command=click_3)
btn3.place(x=150,y=130,width=50,height=50)

## Кнопки 456
def click_4():
    ent.insert(END,"4")
btn4 = Button(text="4",font="15",command=click_4)
btn4.place(x=10,y=200,width=50,height=50)

def click_5():
    ent.insert(END,"5")
btn5 = Button(text="5",font="15",command=click_5)
btn5.place(x=80,y=200,width=50,height=50)

def click_6():
    ent.insert(END,"6")
btn6 = Button(text="6",font="15",command=click_6)
btn6.place(x=150,y=200,width=50,height=50)

## Кнопки 789
def click_7():
    ent.insert(END,"7")
btn7 = Button(text="7",font="15",command=click_7)
btn7.place(x=10,y=270,width=50,height=50)
def click_8():
    ent.insert(END,"8")
btn8 = Button(text="8",font="15",command=click_8)
btn8.place(x=80,y=270,width=50,height=50)

def click_9():
    ent.insert(END,"9")
btn9 = Button(text="9",font="15",command=click_9)
btn9.place(x=150,y=270,width=50,height=50)

## Кнопка 0
def click_0():
    ent.insert(END,"0")
btn0 = Button(text="0",font="15",command=click_0)
btn0.place(x=10,y=325,width=190,height=50)


tk.mainloop()