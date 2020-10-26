from tkinter import *

master = Tk()
#self.master = master
master.title("Info python Projekt")

def greet():
    print("Greetings!")

def ausgeben(string):
    print(str(string))

greet_button = Button(master, text="Greet", command=lambda:[greet,print('hello '),print('world')])
greet_button.pack()

essen_button = Button(master, text='Essen', command = lambda: ausgeben('lecker'))
essen_button.pack()

close_button = Button(master, text="Close", command=quit)
close_button.pack()
        


