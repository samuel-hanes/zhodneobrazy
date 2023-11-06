from tkinter import *
from turtle import ScrolledCanvas, RawTurtle, TurtleScreen

root = Tk()
canvas = ScrolledCanvas(root)
canvas.pack(side=LEFT)

screen = TurtleScreen(canvas)
turtle = RawTurtle(canvas)
turtle.down()
turtle.bk(100)

screen.mainloop()