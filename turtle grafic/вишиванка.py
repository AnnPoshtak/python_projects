from turtle import*
speed(10)
shape("square")
shapesize(0.5,1,5)
color("red")
pu()
x = -200
y = 0
goto(x,y)
for j in range(3):
    w = 360
    for g in range(4):
        w -= 90
        seth(w)
        rt(45)
        fd(20)
        seth(w)

        for i in range(3):
            fd(20)
            stamp()
            bk(20)
            rt(90)
            fd(20)
            stamp()
            bk(20)
            lt(45)
            fd(15)
            lt(45)
        goto(x,y)
    x += 200
    goto(x,y)


shapesize(1)
color("black")
for i in range(3):
    x -= 200
    goto(x,y)
    stamp()

speed(5)
shape("square")
pu()
goto(-340,150)
width(5)
pd()
## верхні візерунки
for i in range(6):
    pd()
    a = 100
    lt(90)
    forward(a)
    for j in range(5):
        rt(90)
        forward(a)
        a = a-20
    rt(90)
    a = a+20
    forward(a)
    for j in range(5):
        lt(90)
        forward(a)
        a = a+20
    pu()
## нижні візерунки
goto(-340,-250)
pd()
for i in range(6):
    pd()
    a = 100
    lt(90)
    forward(a)
    for j in range(5):
        rt(90)
        forward(a)
        a = a-20
    rt(90)
    a = a+20
    forward(a)
    for j in range(5):
        lt(90)
        forward(a)
        a = a+20
    pu()

done()