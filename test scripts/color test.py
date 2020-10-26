from tkinter import *
import math


master = Tk()

def getcolor(string):
    if string == 'fc':
        color = editfc.get()
    if string == 'oc':
        color = editoc.get()
    if color[0] == 'r' and not color == 'red':
            print('rgb oc erkannt')
            #color = 'black'
            color = color[color.find('(')+1:color.find(')')]
            rstring = color[:color.find(',')]
            colorrest = color[color.find(',')+1:]
            gstring = colorrest[:colorrest.find(',')]
            bstring = colorrest[colorrest.find(',')+1:]
            rhex = hex(int(rstring))[2:]
            ghex = hex(int(gstring))[2:]
            bhex = hex(int(bstring))[2:]
            if len(rhex) == 1:
                rhex = '0' + rhex
            if len(ghex) == 1:
                ghex = '0' + ghex
            if len(bhex) == 1:
                bhex = '0' + bhex
            color = '#'+rhex+ghex+bhex
    return(color)

def zeichnen():
    fillcolor = getcolor('fc')
    outlinecolor = getcolor('oc')
    canvas1.create_rectangle(20,20,480,180, fill = fillcolor, outline = outlinecolor)
    print('zeichnen abgeschlossen')

def popup(string):
    if string == 'tip':
        msg = 'Es gibt vier Wege der Farbeingabe: \n    (1) Anklicken des Buttons mit der gewünschten Farbe \n    (2) Eingeben von Standardfarben von Python (Bsp: red, yellow, ...) \n    (3) Eingeben von Hexadezimalwerten (Bsp: #ab42cd) \n    (4) Eingeben von RGB-Tripeln (Bsp: rgb(42,69,255) )'
    masterpopup = Tk()
    labelmsg = Label(masterpopup, text = msg, justify = 'left', font = '15')
    labelmsg.pack(padx = 10, pady = 10)
    

canvas1 = Canvas(master, width = 500, height = 200)
canvas1.grid(row = 0, column = 0, rowspan = 1, columnspan = 10)

buttonblackoc = Button(master, text = 'XX', bg = 'black', fg = 'black', command = lambda:(editoc.delete(0,'end'), editoc.insert(10,'black'), zeichnen()))
buttonblackoc.grid(row = 1, column = 0, padx = 0)

buttonblueoc = Button(master, text = 'XX', bg = 'blue', fg = 'blue', command = lambda:(editoc.delete(0,'end'), editoc.insert(10,'blue'), zeichnen()))
buttonblueoc.grid(row = 1, column = 1, padx = 0)

buttonredoc = Button(master, text = 'XX', bg = 'red', fg = 'red', command = lambda:(editoc.delete(0,'end'), editoc.insert(10,'red'), zeichnen()))
buttonredoc.grid(row = 1, column = 2, padx = 0)

buttongreenoc = Button(master, text = 'XX', bg = 'green', fg = 'green', command = lambda:(editoc.delete(0,'end'), editoc.insert(10,'green'), zeichnen()))
buttongreenoc.grid(row = 1, column = 3, padx = 0)

buttonyellowoc = Button(master, text = 'XX', bg = 'yellow', fg = 'yellow', command = lambda:(editoc.delete(0,'end'), editoc.insert(10,'yellow'), zeichnen()))
buttonyellowoc.grid(row = 1, column = 4, padx = 0)

buttonblackfc = Button(master, text = 'XX', bg = 'black', fg = 'black', command = lambda:(editfc.delete(0,'end'), editfc.insert(10,'black'), zeichnen()))
buttonblackfc.grid(row = 1, column = 5, padx = 0)

buttonbluefc = Button(master, text = 'XX', bg = 'blue', fg = 'blue', command = lambda:(editfc.delete(0,'end'), editfc.insert(10,'blue'), zeichnen()))
buttonbluefc.grid(row = 1, column = 6, padx = 0)

buttonredfc = Button(master, text = 'XX', bg = 'red', fg = 'red', command = lambda:(editfc.delete(0,'end'), editfc.insert(10,'red'), zeichnen()))
buttonredfc.grid(row = 1, column = 7, padx = 0)

buttongreenfc = Button(master, text = 'XX', bg = 'green', fg = 'green', command = lambda:(editfc.delete(0,'end'), editfc.insert(10,'green'), zeichnen()))
buttongreenfc.grid(row = 1, column = 8, padx = 0)

buttonyellowoc = Button(master, text = 'XX', bg = 'yellow', fg = 'yellow', command = lambda:(editfc.delete(0,'end'), editfc.insert(10,'yellow'), zeichnen()))
buttonyellowoc.grid(row = 1, column = 9, padx = 0)

labeloc = Label(master, text = 'Randfarbe: ')
labeloc.grid(row = 2, column = 0, columnspan = 2)

editoc = Entry(master)
editoc.grid(row = 2, column = 2, columnspan = 3)
editoc.insert(10,'blue')

labelfc = Label(master, text = 'Füllfarbe: ')
labelfc.grid(row = 2, column = 5, columnspan = 2)

editfc = Entry(master)
editfc.grid(row = 2, column = 7, columnspan = 3)
editfc.insert(10,'yellow')

buttonzeichnen = Button(text = 'zeichnen', command = zeichnen)
buttonzeichnen.grid(row = 3, column = 0)

buttontip = Button(text = '?', command = lambda:popup('tip'))
buttontip.grid(row = 3, column = 5)
zeichnen()
