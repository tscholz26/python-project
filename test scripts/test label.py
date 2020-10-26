from tkinter import *

master = Tk()
#self.master = master
master.title("Info python Projekt")

def greet():
    print("Greetings!")

def ausgeben(string):
    print(str(string))

label = Label(master, text = '10.1')
label.pack()

close_button = Button(master, text="Close", command=quit)
close_button.pack()
