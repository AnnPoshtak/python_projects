import random
from turtle import*
import random
pu()
bgcolor("black")
colors = ["crimson","gold","lime green","dodger blue","deep pink","medium purple", "orange","aqua"] # 8
step = 90
step1 = 60
goto(-370,315)
pd()
for j in range (8):
    begin_fill()
    col = random.choice(colors)
    color("white",col)
    colors.remove(col)
    if j == 0:
        forward(50)
    else:
        forward(step)
    rt(60)
    for i in range(2):
        forward(step1)
        right(60)
        forward(step1)
        right(120)
    end_fill()
    lt(60)
color("white")
forward(200)
done()