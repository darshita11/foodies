from turtle import *

tur=Turtle()
tur.speed(100)
win=Screen()
win.bgcolor("black")
r,g,b=255,0,0

for i in range(255*2):
    win.colormode(255)
    if i<255//3:
        g+=3
    elif i<255*2//3:
        r-=3
    elif i<255:
        b+=3
    elif i<255 *4 //3:
        g-=3
    elif i<255*5 //3:
        r+=3
    else:
        b-=3
    tur.fd(10+i)
    tur.rt(91)
    tur.pencolor(r,g,b)
    # tur.hideturtle()
    # win.mainloop()

