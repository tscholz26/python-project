from tkinter import *

master = Tk()

check1 = IntVar()
check2 = IntVar()
check3 = IntVar()

cbiko = Checkbutton(master, var = check1, text = 'Ikosaeder zeichnen', command = lambda:(cbokt.deselect(), cbkep.deselect()))
cbiko.grid(row = 1, column = 0, columnspan = 1, pady = 15)

cbokt = Checkbutton(master, var = check2, text = 'Oktaeder zeichnen', command = lambda:(cbiko.deselect(), cbkep.deselect()))
cbokt.grid(row = 2, column = 0, columnspan = 1, pady = 15)

cbkep = Checkbutton(master, var = check3, text = 'Keplerstern zeichnen', command = lambda:(cbiko.deselect(), cbokt.deselect()))
cbkep.grid(row = 3, column = 0, columnspan = 1, pady = 15)

cbiko.toggle()

if check1.get() == 1:
	print('erfolg')
