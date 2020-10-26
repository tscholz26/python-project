from tkinter import *

master = Tk()

global clickx
global clicky
global currentx
global currenty
global releasex
global releasey
global posx
global posy

posx = 100
posy = 100


def greet():
    print("Greetings!")

def ausgeben(string):
    print(str(string))

def click(eventclick):
    global clickx
    global clicky
    global currentx
    global currenty
    
    clickx = eventclick.x
    clicky = eventclick.y
    currentx = clickx
    currenty = clicky
    
    print("clicked at", clickx, clicky)

def currentpos(eventcurrent):
    global clickx
    global clicky
    global currentx
    global currenty
    global posx
    global posy
    global currentx
    global currenty

    #pos vorher speichern
    currentxalt = currentx
    currentyalt = currenty

    #neue pos
    currentx = eventcurrent.x
    currenty = eventcurrent.y
    
    xdiff = currentxalt - currentx
    ydiff = currentyalt - currenty
    posx = posx - xdiff
    posy = posy - ydiff

    canvas.create_rectangle(currentx, currenty, currentx, currenty)
    
    canvas.create_rectangle(posx-3,posy-3,posx+3,posy+3)

def release(eventrelease):
    global releasex
    releasex = eventrelease.x
    global releasey
    releasey = eventrelease.y
    print("released at", releasex, releasey)


canvas = Canvas(master, height = 400, width = 400)
canvas.pack()

close_button = Button(master, text="Close")
#close_button.grid(column = 1, row = 1)
close_button.pack()

label = Label(master, text = '10.1')
#label.grid(column = 0, row = 1)
label.pack()

canvas.focus_set()

master.bind("<Button-1>", click)
master.bind("<Button1-Motion>", currentpos)
master.bind("<ButtonRelease-1>", release)

canvas.create_rectangle(posx-3,posy-3,posx+3,posy+3)
