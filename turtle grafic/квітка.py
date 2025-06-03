from turtle import*
shape("turtle")
colors=["#fa43c0","#ff26ba","#ff03af"]
shapesize(10)
count = 10
color("#fa93d9")
rt(90)
pu()
goto(0,0)
pd()
for i in range(4):
        stamp()
        rt(90)

shapesize(7)
color(colors[0])
for i in range(4):
        stamp()
        rt(90)

shapesize(4)
color(colors[1])
for i in range(4):
        stamp()
        rt(90)

shapesize(1)
color(colors[2])
for i in range(4):
        stamp()
        rt(90)
done()
