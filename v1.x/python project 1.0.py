from tkinter import *
import math


master = Tk()


def zeichnen():
    n = 17
    r = 250
    xy = []
    for i in range (0,n):
        xy.append(mx + round (r * math.sin(2 * math.pi / n * i)))
        xy.append(my - round (r * math.cos(2 * math.pi / n * i)))
    print(xy)
    canvas1.create_polygon(xy, fill = 'yellow')
    for k in range (0,n):
        for m in range (0,n):
            canvas1.create_line(xy[2*k],xy[2*k+1],xy[2*m],xy[2*m+1], fill = 'blue')
        



mx = 400
my = 300


canvas1 = Canvas(master, width = 800, height = 600)
canvas1.pack()

button1 = Button(text = 'zeichnen', function = zeichnen())
button1.pack()

edit1 = Entry(master, text = '17')
edit1.pack()
