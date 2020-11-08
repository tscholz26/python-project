from tkinter import *
import math, time

master = Tk()
master.title('color gradient test')

global defcolor
defcolor = 'red'

global direction
global colors

direction = [0,0,0]
colors = [255,0,0]

direction[0] = -1
direction[1] = 1
direction[2] = 0

    
def draw():
    color = getcolor()
    canvas1.delete(ALL)
    canvas1.create_rectangle(20,20,380,180, fill = color)

def rgbtohex(color):
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
    colorhex = '#'+rhex+ghex+bhex
    return(colorhex)

def getcolor():
    global defcolor
    global starttime
    global speed
    global direction
    global colors

    speed = scalespeed.get() / 100
    
    for i in range(0,3):
        #print('Speed: ' + str(scalevar))
        colors[i] = round( colors[i] + direction[i] * speed)
        tolerance = speed
        if colors[i] > 255 - tolerance:
            direction[i] = -1
            direction[(i+1)%3] = 1
            direction[(i+2)%3] = 0

        if colors[0] > 255 - tolerance:
            colors[0] = round(255 - tolerance)
            colors[1] = 0
            colors[2] = 0
            print('reset to red')
            
    colorrgb = 'rgb(' + str(colors[0]) + ',' + str(colors[1]) + ',' + str(colors[2]) + ')'
    color = rgbtohex(colorrgb)
    return color


def inffunc():
    time.sleep(0.001)
    master.after(50, lambda:(draw(), inffunc()))

canvas1 = Canvas(master, height = 200, width = 400)
canvas1.grid(row = 0, column = 0, columnspan = 2)

buttonclose = Button(master, text = 'close', command = quit)
buttonclose.grid(row = 1, column = 1)

scalespeed = Scale(master, label = 'Geschwindigkeit Verlauf', from_ = 50, to = 1500, orient = 'horizontal', showvalue = 0, length = 150)
scalespeed.grid(row = 1, column = 0)
scalespeed.set(500)

inffunc()







