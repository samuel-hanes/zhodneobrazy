import turtle
from turtle import RawTurtle, TurtleScreen
import tkinter as tk
from tkinter import *

window = tk.Tk()
window.minsize(width = 720, height = 800)
canvas = Canvas(window, width = 720, height = 800,bd=0)
canvas.pack()

screen = TurtleScreen(canvas)
screen.setworldcoordinates(0, 800, 720, 0)

#screen.setworldcoordinates(-180, -90, 180, 90)
canvas.create_line(0,0,720,800,fill="red")
canvas.create_line(720,0,0,800,fill="red")
quake = RawTurtle(screen)
quake.shape("circle")
quake.color("red")
quake.fd(0)
quake.goto(720,800)



mainloop()