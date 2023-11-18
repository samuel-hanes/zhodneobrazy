
import math
import turtle
from turtle import RawTurtle, TurtleScreen
import tkinter as tk
from tkinter import *

window = tk.Tk()
window.minsize(width = 1000, height = 800)
canvas = Canvas(window, width = 1000, height = 800,bd=0)
canvas.pack()

screen = TurtleScreen(canvas)
screen.setworldcoordinates(0, 800, 1000, 0)

#screen.setworldcoordinates(-180, -90, 180, 90)
canvas.create_line(0,0,1000,800,fill="red")
canvas.create_line(1000,0,0,800,fill="red")

turtle = RawTurtle(screen)
turtle.goto(0,0)
turtle.goto(1000,800)
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
    stxs=300
    stys=450
    canvas.create_oval(stxs-5,stys-5,stxs+5,stys+5)
    
    if typ==1:
        for i in range(n):
            turtle.fd(a)
            turtle.lt(360/n)
        for i in range(n):
            x=stx-stxs
            y=sty-stys
            s=math.atan2(abs(sty-stys),abs(stx-stxs))*180/math.pi #uhol vypocet od x osi
            print(s)
            if s>0:
                ang=360-s
            else:ang=s
            start=0
            if stxs>stx and stys>sty:
                ang=ang*-1
                start=270
            elif stys>sty:
                ang = ang +180
                start=180
            elif stxs<stx:
                ang = ang*-1+180
                start=90
            
            turtle.lt(ang)
            cline(2*math.sqrt((stx-stxs)**2+(sty-stys)**2))
            arcx,arcy=turtle.pos()
            #canvas.create_arc(arcx+10,arcy+10,arcx-(math.sqrt(2)*10-10),arcy-(math.sqrt(2)*10-10),start=start,style=tk.ARC)
            #canvas.create_rectangle(arcx+10,arcy+10,arcx-(math.sqrt(2)*10-10),arcy-(math.sqrt(2)*10-10))
            #canvas.create_line(arcx-10,arcy-10,arcx,arcy,arcx+10,arcy+10,smooth=1)
            canvas.create_arc(arcx-(math.sqrt(2)*a-a),arcy-(math.sqrt(2)*a-a),arcx+(math.sqrt(2)*a+a),arcy+(math.sqrt(2)*a+a),start=start,style=tk.ARC)
            canvas.create_oval(arcx-1,arcy-1,arcx+1,arcy+1)
            turtle.goto(stx,sty)
            turtle.setheading(0)
            turtle.lt(360/n*i)
            turtle.fd(a)
            turtle.setheading(0)
            stx,sty= turtle.pos()

        print(math.sqrt((stx-stxs)**2+(sty-stys)**2))
        

nangler(10,400,400,20,1)

mainloop()