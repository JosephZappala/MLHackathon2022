import turtle 
import tkinter as tk


x = 0
y = 0
width = 0

screen = turtle.Screen()
screen.bgcolor("cyan")
canvas = screen.getcanvas()
button = tk.Button(canvas.master, text="Press me")
canvas.create_window(-200, -200, window=button)


my_lovely_turtle = turtle.Turtle(shape="circle")
my_lovely_turtle.pd()
my_lovely_turtle.width(0)
my_lovely_turtle.shapesize(.1, .1, 12)
my_lovely_turtle.speed(100)
while True:
    my_lovely_turtle.goto(int(x),int(y))
    x += 2
    y += 2
    my_lovely_turtle.width(width)
    width += 1



