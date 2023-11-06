from tkinter import *
from turtle import ScrolledCanvas, RawTurtle, TurtleScreen
import math
root = Tk()
canvas = ScrolledCanvas(root)
canvas.pack(side=LEFT)

screen = TurtleScreen(canvas)
turtle = RawTurtle(canvas)
turtle.up()

def cline(a):
    for i in range(20):
        if i %2==0:
            turtle.down()
        else:
            turtle.up()
        turtle.fd(a/20)

def nangler(n,stx,sty,a,typ):
    turtle.goto(stx,sty)
    turtle.down()
    stxs=100
    stys=150
    canvas.create_oval(stx-5,sty-5,stx+5,sty+5)
    turtle.goto(stx,sty)
    if typ==1:
        for i in range(n):
            turtle.fd(a)
            turtle.lt(360/n)
        x=stx-stxs
        y=sty-stys
        s=math.atan2(stx-stxs,sty-stys)*180/math.pi
        if s>0:
            ang=360-s
        else:ang=s


        
        turtle.lt(ang)
        cline(math.sqrt((stx-stxs)**2+(sty-stys)**2))
        print(ang)
        

nangler(10,100,100,20,1)

screen.mainloop()