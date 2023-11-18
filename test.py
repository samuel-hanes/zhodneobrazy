import turtle
from turtle import RawTurtle, TurtleScreen
import tkinter as tk
from tkinter import *
import math
window = tk.Tk()
window.minsize(width = 720, height = 800)
canvas = Canvas(window, width = 720, height = 800,bd=0)
canvas.pack()

screen = TurtleScreen(canvas)
screen.setworldcoordinates(0, 800, 720, 0)
a=50
arcx,arcy = 500,500
canvas.create_arc(arcx-(math.sqrt(2)*a-a),arcy-(math.sqrt(2)*a-a),arcx+(math.sqrt(2)*a+a),arcy+(math.sqrt(2)*a+a),start=90)
canvas.create_rectangle(arcx+a,arcy+a,arcx-(math.sqrt(2)*a-a),arcy-(math.sqrt(2)*a-a))
canvas.create_oval(arcx-1,arcy-1,arcx+1,arcy+1)
canvas.create_rectangle(300,300,400,400)
canvas.create_arc(300,300,400,400)
#screen.setworldcoordinates(-180, -90, 180, 90)
canvas.create_line(0,0,720,800,fill="red")
canvas.create_line(720,0,0,800,fill="red")
#canvas.create_arc(200, 100, 100, 200,start=90,style=tk.ARC)
quake = RawTurtle(screen)
quake.shape("circle")
quake.color("red")
quake.fd(0)
quake.goto(720,800)



mainloop()