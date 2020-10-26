from tkinter import *
import time

master = Tk()

def clock():
    t = time.localtime()
    label.config(text = str(t))
    master.after(3000,clock)

def hallo():
    print('Hello World')
    
label = Label(master)
label.pack()

button = Button(master, text = 'Button', command = hallo)
button.pack()

clock()
