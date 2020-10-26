from tkinter import *
import time
import math

master = Tk()
#master.configure(background = 'white')

mx = 400
my = 325
mz = 0
gold = ((math.sqrt(5)-1)/2)
facelist = list()

check1 = IntVar()
check2 = IntVar()
check3 = IntVar()
check4 = IntVar()
check5 = IntVar()
check6 = IntVar()
check7 = IntVar()
check8 = IntVar()
checkrep = IntVar()
checkdeg = IntVar()
checkrad = IntVar()

class object3d:
    name = 'Ikosaeder'
    xyz = []
    xy = []
    sl = 2.5
    ek = IntVar() #anzahl der ecken pro seitenfläche
    a = IntVar()

obj = object3d()

def keplerstern():
    canvas1.delete(ALL)
    obj.name = 'Keplerstern'
    obj.a = 150
    obj.xyz = [mx+obj.a,my,mz, mx,my+obj.a,mz, mx,my,mz+obj.a, mx-obj.a,my,mz, mx,my-obj.a,mz, mx,my,mz-obj.a,
               mx+obj.a,my-obj.a,mz-obj.a, mx-obj.a,my+obj.a,mz-obj.a, mx-obj.a,my-obj.a,mz+obj.a, mx-obj.a,my+obj.a,mz+obj.a, mx+obj.a,my-obj.a,mz+obj.a, mx+obj.a,my+obj.a,mz-obj.a, mx-obj.a,my-obj.a,mz-obj.a, mx+obj.a,my+obj.a,mz+obj.a]
    obj.sl = obj.a * math.sqrt(2)
    #obj.sl = obj.a * 3
    obj.ek = 3
    print(str(obj.name) +' wird geladen')
    labelname.config(text = (obj.name + 'darstellung'))
    master.title('Darstellung eines ' + obj.name + 's in 3D')
    #in startposition drehen für bessere optik
    rotx(40)
    roty(30)
    rotz(30)
    zeichnen()

def oktaeder():
    canvas1.delete(ALL)
    obj.name = 'Oktaeder'
    obj.a = 200
    obj.xyz = [mx+obj.a,my,mz, mx,my+obj.a,mz, mx,my,mz+obj.a, mx-obj.a,my,mz, mx,my-obj.a,mz, mx,my,mz-obj.a]
    obj.sl = math.sqrt(2)*obj.a
    obj.ek = 3
    print(str(obj.name) +' wird geladen')
    labelname.config(text = (obj.name + 'darstellung'))
    master.title('Darstellung eines ' + obj.name + 's in 3D')
    #in startposition drehen für bessere optik
    rotxfunc(1)
    rotyfunc(1)
    zeichnen()
    
def ikosaeder():
    canvas1.delete(ALL)
    obj.name = 'Ikosaeder'
    obj.a = 200
    phi = (gold*obj.a)
    obj.xyz = [mx,my-obj.a,mz+phi, mx,my-obj.a,mz-phi, mx,my+obj.a,mz+phi, mx,my+obj.a,mz-phi, mx+phi,my,mz+obj.a, mx+phi,my,mz-obj.a, mx-phi,my,mz+obj.a, mx-phi,my,mz-obj.a, mx+obj.a,my-phi,mz, mx+obj.a,my+phi,mz, mx-obj.a,my-phi,mz, mx-obj.a,my+phi,mz]
    obj.sl = 2*phi
    obj.ek = 3
    print(str(obj.name) +' wird geladen')
    labelname.config(text = (obj.name + 'darstellung'))
    master.title('Darstellung eines ' + obj.name + 's in 3D')
    #in startposition drehen für bessere optik
    rotxfunc(1)
    rotxfunc(1)
    zeichnen()

def dodekaeder():
    canvas1.delete(ALL)
    obj.name = 'Dodekaeder'
    obj.a = 130
    phi = (gold*obj.a)
    phim = obj.a/gold
    obj.xyz = [mx+obj.a,my+obj.a,mz+obj.a, mx-obj.a,my+obj.a,mz+obj.a, mx+obj.a,my-obj.a,mz+obj.a, mx+obj.a,my+obj.a,mz-obj.a, mx+obj.a,my-obj.a,mz-obj.a, mx-obj.a,my+obj.a,mz-obj.a, mx-obj.a,my-obj.a,mz+obj.a, mx-obj.a,my-obj.a,mz-obj.a, mx+phim,my+phi,mz, mx-phim,my+phi,mz, mx-phim,my-phi,mz, mx+phim,my-phi,mz, mx,my+phim,mz+phi, mx,my+phim,mz-phi, mx,my-phim,mz-phi, mx,my-phim,mz+phi, mx+phi,my,mz+phim, mx+phi,my,mz-phim, mx-phi,my,mz+phim, mx-phi,my,mz-phim]
    obj.sl = 2*phi
    obj.ek = 5
    print(str(obj.name) +' wird geladen')
    labelname.config(text = (obj.name + 'darstellung'))
    master.title('Darstellung eines ' + obj.name + 's in 3D')
    #in startposition drehen für bessere optik
    rotxfunc(1)
    rotxfunc(1)
    rotyfunc(-1)
    zeichnen()

def wuerfel():
    canvas1.delete(ALL)
    obj.name = 'Würfel'
    obj.a = 150
    obj.xyz = [mx-obj.a,my-obj.a,mz-obj.a, mx+obj.a,my+obj.a,mz-obj.a, mx+obj.a,my-obj.a,mz+obj.a, mx-obj.a,my+obj.a,mz+obj.a, mx+obj.a,my-obj.a,mz-obj.a, mx-obj.a,my+obj.a,mz-obj.a, mx-obj.a,my-obj.a,mz+obj.a, mx+obj.a,my+obj.a,mz+obj.a]
    obj.sl = 2*obj.a
    obj.ek = 4
    print(str(obj.name) +' wird geladen')
    labelname.config(text = (obj.name + 'darstellung'))
    master.title('Darstellung eines ' + obj.name + 's in 3D')
    zeichnen()
    
master.title('Darstellung eines ' + obj.name + 's in 3D')
    
def conv32():
    obj.xy = []
    for i in range (0,len(obj.xyz)//3):
        #obj.xy.append(obj.xyz[3*i]+obj.xyz[3*i+2]/2/math.sqrt(2))
        #obj.xy.append(obj.xyz[3*i+1]-obj.xyz[3*i+2]/2/math.sqrt(2))

        #povx = mx
        #povy = my
        #povz = mz - 400
        #distance = math.sqrt((povx-obj.xyz[3*i])**2+(povy-obj.xyz[3*i+1])**2+(povz-obj.xyz[3*i+2])**2)
        
        distance = 3000
        obj.xy.append((obj.xyz[3*i] * distance)/(obj.xyz[3*i+2] + distance))
        obj.xy.append((obj.xyz[3*i+1] * distance)/(obj.xyz[3*i+2] + distance)        )
    return obj.xy

def getdeg():
    if editdeg.get() != '':
        deg = float(editdeg.get())
    else:
        deg = 10
    if checkdeg.get() == 1:
        deg = deg / 180 * math.pi
    return(deg)

def rotxfunc(sgndeg):
    sgndeg2 = sgndeg
    if checkrep.get() == 0:
        rotx(sgndeg)
    else:
        reprotx(sgndeg2)

def rotyfunc(sgndeg):
    sgndeg2 = sgndeg
    if checkrep.get() == 0:
        roty(sgndeg)
    else:
        reproty(sgndeg2)

def rotzfunc(sgndeg):
    sgndeg2 = sgndeg
    if checkrep.get() == 0:
        rotz(sgndeg)
    else:
        reprotz(sgndeg2)

def rotx(sgndeg):
    canvas1.delete(ALL)
    deg = getdeg()*sgndeg
    c = math.cos(deg)
    s = math.sin(deg)
    for p in range(0,len(obj.xyz)//3):
        yalt = obj.xyz[3*p+1]
        zalt = obj.xyz[3*p+2]
        obj.xyz[3*p+1] = ((yalt - my) * c - (zalt - mz) * s) + my
        obj.xyz[3*p+2] = ((yalt - my) * s + (zalt - mz) * c) + mz
    obj.xy = conv32()
    zeichnen()    
    return(obj.xyz)

def roty(sgndeg):
    canvas1.delete(ALL)
    deg = getdeg()*sgndeg
    c = math.cos(deg)
    s = math.sin(deg)
    for p in range(0,len(obj.xyz)//3):
        xalt = obj.xyz[3*p]
        zalt = obj.xyz[3*p+2]
        obj.xyz[3*p] = ((xalt - mx) * c - (zalt - mz) * s) + mx
        obj.xyz[3*p+2] = ((xalt - mx) * s + (zalt - mz) * c) + mz
    obj.xy = conv32()
    zeichnen()
    return(obj.xyz)

def rotz(sgndeg):
    canvas1.delete(ALL)
    deg = getdeg()*sgndeg
    c = math.cos(deg)
    s = math.sin(deg)
    for p in range(0,len(obj.xyz)//3):
        xalt = obj.xyz[3*p]
        yalt = obj.xyz[3*p+1]
        obj.xyz[3*p] = ((xalt - mx) * c - (yalt - my) * s) + mx
        obj.xyz[3*p+1] = ((xalt - mx) * s + (yalt - my) * c) + my
    obj.xy = conv32()
    zeichnen()
    return(obj.xyz)

def reprotx(sgndeg2):
    if checkrep.get() == 1:
        rotx(sgndeg2)
        master.after(100, lambda:reprotx(sgndeg2))

def reproty(sgndeg2):
    if checkrep.get() == 1:
        rotz(sgndeg2)
        master.after(100, lambda:reproty(sgndeg2))
        
def reprotz(sgndeg2):
    if checkrep.get() == 1:
        rotz(sgndeg2)
        master.after(100, lambda:reprotz(sgndeg2))

def getcolor(string):
    if string == 'fc':
        color = editfc.get()
    if string == 'oc':
        color = editoc.get()
    if color[0] == 'r' and not color == 'red':
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

def drawedges():
    canvas1.delete(ALL)
    obj.xy = conv32()
    #print('obj.xyz: ' + str(obj.xyz))
    #print('obj.xy: ' + str(obj.xy))
    for k in range (0,len(obj.xyz)//3):
        for m in range (0,len(obj.xyz)//3):
            abstand = (round(math.sqrt((obj.xyz[3*k]-obj.xyz[3*m])**2+(obj.xyz[3*k+1]-obj.xyz[3*m+1])**2+(obj.xyz[3*k+2]-obj.xyz[3*m+2])**2)))
            #print(abstand)
            if (abs(abstand-obj.sl) < 5):
                canvas1.create_line(obj.xy[2*k],obj.xy[2*k+1],obj.xy[2*m],obj.xy[2*m+1], fill = getcolor('oc'))
                
def drawfaces():
    facelist.clear()
    #zeichnen
    for p in range (0,len(obj.xyz)//3):
        for q in range (0,len(obj.xyz)//3):
            pq = math.sqrt((obj.xyz[3*p]-obj.xyz[3*q])**2+(obj.xyz[3*p+1]-obj.xyz[3*q+1])**2+(obj.xyz[3*p+2]-obj.xyz[3*q+2])**2)
            if (abs(pq-obj.sl) < 10):
                for r in range (0,len(obj.xyz)//3):
                    pr = math.sqrt((obj.xyz[3*p]-obj.xyz[3*r])**2+(obj.xyz[3*p+1]-obj.xyz[3*r+1])**2+(obj.xyz[3*p+2]-obj.xyz[3*r+2])**2)
                    if (abs(pr-obj.sl) < 10):
                        qr = math.sqrt((obj.xyz[3*q]-obj.xyz[3*r])**2+(obj.xyz[3*q+1]-obj.xyz[3*r+1])**2+(obj.xyz[3*q+2]-obj.xyz[3*r+2])**2)
                        if (abs(qr-obj.sl) < 10) or ((obj.ek == 5) and (abs(qr-(2*obj.sl*math.sin(54/180*math.pi))) < 10)):
                            if obj.ek > 3:
                                for s in range (0,len(obj.xyz)//3):
                                    qs = math.sqrt((obj.xyz[3*q]-obj.xyz[3*s])**2+(obj.xyz[3*q+1]-obj.xyz[3*s+1])**2+(obj.xyz[3*q+2]-obj.xyz[3*s+2])**2)
                                    if (abs(qs-obj.sl) < 10):
                                        for t in range (0,len(obj.xyz)//3):
                                            st = math.sqrt((obj.xyz[3*s]-obj.xyz[3*t])**2+(obj.xyz[3*s+1]-obj.xyz[3*t+1])**2+(obj.xyz[3*s+2]-obj.xyz[3*t+2])**2)
                                            if (abs(st-obj.sl) < 10):
                                                rt = math.sqrt((obj.xyz[3*r]-obj.xyz[3*t])**2+(obj.xyz[3*r+1]-obj.xyz[3*t+1])**2+(obj.xyz[3*r+2]-obj.xyz[3*t+2])**2)
                                                if (abs(rt-obj.sl) < 10):
                                                    obj.xy = conv32()
                                                    provebvb()
                                                    canvas1.create_polygon(obj.xy[2*p],obj.xy[2*p+1], obj.xy[2*q],obj.xy[2*q+1], obj.xy[2*s],obj.xy[2*s+1],obj.xy[2*t],obj.xy[2*t+1], obj.xy[2*r],obj.xy[2*r+1], fill = getcolor('fc'), outline = getcolor('oc'))
                                                
                            else:
                                #p,q,r sortieren
                                abc = [p,q,r]
                                for f in range(0,obj.ek):
                                    for g in range(0,obj.ek):
                                        if (abc[f] > abc[g]) and (f < g):
                                            abc[f],abc[g] = abc[g],abc[f]
                                if len(facelist) == 0:
                                    for i in range(0,obj.ek):
                                        facelist.append(abc[i])
                                else:
                                    #prüfen ob p,q,r in liste enthalten ist
                                    add = 1
                                    for i in range(0,len(facelist)//3):
                                        if (facelist[3*i] == abc[0]) and (facelist[3*i+1] == abc[1]) and (facelist[3*i+2] == abc[2]):
                                            add = 0
                                    if add == 1:
                                        #ggf. hinzufügen
                                        for j in range(0,obj.ek):
                                            facelist.append(abc[j])
    if obj.ek == 3:
        #nach mzpolygon sortieren
        for m in range(0,len(facelist)//3):
            for n in range(0,len(facelist)//3):
                mzpolygonm = (obj.xyz[3*facelist[3*m]+2] + obj.xyz[3*facelist[3*m+1]+2] + obj.xyz[3*facelist[3*m+2]+2])/3
                mzpolygonn = (obj.xyz[3*facelist[3*n]+2] + obj.xyz[3*facelist[3*n+1]+2] + obj.xyz[3*facelist[3*n+2]+2])/3
                if (mzpolygonm > mzpolygonn) and (m > n):
                    facelist[3*m],facelist[3*n] = facelist[3*n],facelist[3*m]
                    facelist[3*m+1],facelist[3*n+1] = facelist[3*n+1],facelist[3*m+1]
                    facelist[3*m+2],facelist[3*n+2] = facelist[3*n+2],facelist[3*m+2]

        #Überprüfung    
        #for i in range(0,len(facelist)//3):
        #    mzpolygon = (obj.xyz[3*facelist[3*i]+2] + obj.xyz[3*facelist[3*i+1]+2] + obj.xyz[3*facelist[3*i+2]+2])/3
        #    print('z-Mittelpunkt des Polygons: ',str(round(mzpolygon)))        
                    
        #finales zeichnen
        obj.xy = conv32()
        for i in range(0,len(facelist)//3):
            p = facelist[3*i]
            q = facelist[3*i+1]
            r = facelist[3*i+2]
            provebvb()
            canvas1.create_polygon(obj.xy[2*p],obj.xy[2*p+1], obj.xy[2*q],obj.xy[2*q+1], obj.xy[2*r],obj.xy[2*r+1], fill = getcolor('fc'), outline = getcolor('oc')) 
    
                   
def zeichnen():
    if check1.get() == 1:
        drawedges()
    if check2.get() == 1:
        drawfaces()
        
def provebvb():
    black = 0
    yellow = 0
    if editfc.get() == 'black':
        black = 1
    if editfc.get() == 'yellow':
        yellow = 1
    if editoc.get() == 'black':
        black = 1
    if editoc.get() == 'yellow':
        yellow = 1
    if black + yellow == 2:
        avoidbvb()
            

def avoidbvb():
    popup('bvb')
    editoc.delete(0,'end')
    editoc.insert(10,'rgb(255,0,0)')
    editfc.delete(0,'end')
    editfc.insert(10,'#b0daf0')   

def popup(string):
    if string == 'tip':
        msg = 'Es gibt vier Wege der Farbeingabe: \n    (1) Anklicken des Buttons mit der gewünschten Farbe \n    (2) Eingeben von Standardfarben von Python (Bsp: red, yellow, ...) \n    (3) Eingeben von Hexadezimalwerten (Bsp: #ab42cd) \n    (4) Eingeben von RGB-Tripeln (Bsp: rgb(42,69,255) )'
    if string == 'bvb':
        msg = 'Die Farbkombination schwarz-gelb ist dank \nFabien Streuber und Tristan Scholz verboten \nworden, um den Nutzer zu schützen. Die Farben \nwerden zu einer besseren Kombination geändert.'
    masterpopup = Tk()
    masterpopup.title('Hinweis')
    labelmsg = Label(masterpopup, text = msg, justify = 'left', font = '15')
    labelmsg.pack(padx = 10, pady = 10)

def deselectall():
    cbiko.deselect()
    cbokt.deselect()
    cbkep.deselect()
    cbdod.deselect()
    cbwur.deselect()
    cbz42.deselect()

#canvas1 = Canvas(master, width = 800, height = 600, bg = 'white')
canvas1 = Canvas(master, width = 800, height = 600)
canvas1.grid(row = 0, column = 0, rowspan = 15, columnspan = 17)

labelname = Label(master, text = (obj.name + 'darstellung'), font = 'Verdana 25' )
labelname.grid(row = 0, column = 0, rowspan = 3, columnspan = 10, sticky = NW, padx = 15, pady = 15)

buttonblackoc = Button(master, text = 'XX', bg = 'black', fg = 'black', command = lambda:(editoc.delete(0,'end'), editoc.insert(10,'black'), zeichnen()))
buttonblackoc.grid(row = 15, column = 2, pady = 10)

buttonblueoc = Button(master, text = 'XX', bg = 'blue', fg = 'blue', command = lambda:(editoc.delete(0,'end'), editoc.insert(10,'blue'), zeichnen()))
buttonblueoc.grid(row = 15, column = 3, pady = 10)

buttonredoc = Button(master, text = 'XX', bg = 'red', fg = 'red', command = lambda:(editoc.delete(0,'end'), editoc.insert(10,'red'), zeichnen()))
buttonredoc.grid(row = 15, column = 4, pady = 10)

buttongreenoc = Button(master, text = 'XX', bg = 'green', fg = 'green', command = lambda:(editoc.delete(0,'end'), editoc.insert(10,'green'), zeichnen()))
buttongreenoc.grid(row = 15, column = 5, pady = 10)

buttonyellowoc = Button(master, text = 'XX', bg = 'yellow', fg = 'yellow', command = lambda:(editoc.delete(0,'end'), editoc.insert(10,'yellow'), zeichnen()))
buttonyellowoc.grid(row = 15, column = 6, pady = 10)

buttonblackfc = Button(master, text = 'XX', bg = 'black', fg = 'black', command = lambda:(editfc.delete(0,'end'), editfc.insert(10,'black'), zeichnen()))
buttonblackfc.grid(row = 15, column = 9, pady = 10)

buttonbluefc = Button(master, text = 'XX', bg = 'blue', fg = 'blue', command = lambda:(editfc.delete(0,'end'), editfc.insert(10,'blue'), zeichnen()))
buttonbluefc.grid(row = 15, column = 10, pady = 10)

buttonredfc = Button(master, text = 'XX', bg = 'red', fg = 'red', command = lambda:(editfc.delete(0,'end'), editfc.insert(10,'red'), zeichnen()))
buttonredfc.grid(row = 15, column = 11, pady = 10)

buttongreenfc = Button(master, text = 'XX', bg = 'green', fg = 'green', command = lambda:(editfc.delete(0,'end'), editfc.insert(10,'green'), zeichnen()))
buttongreenfc.grid(row = 15, column = 12, pady = 10)

buttonyellowoc = Button(master, text = 'XX', bg = 'yellow', fg = 'yellow', command = lambda:(editfc.delete(0,'end'), editfc.insert(10,'yellow'), zeichnen()))
buttonyellowoc.grid(row = 15, column = 13, pady = 10)

labeloc = Label(master, text = 'Randfarbe: ', font = '14')
labeloc.grid(row = 16, column = 2, columnspan = 2, pady = 10)

editoc = Entry(master, font = '14', width = 15)
editoc.grid(row = 16, column = 4, columnspan = 3, pady = 10)
editoc.insert(10,'rgb(255,0,0)')

labelfc = Label(master, text = 'Füllfarbe: ', font = '14')
labelfc.grid(row = 16, column = 9, columnspan = 2, pady = 10)

editfc = Entry(master, font = '14', width = 15)
editfc.grid(row = 16, column = 11, columnspan = 2, pady = 10)
editfc.insert(10,'#b0daf0')


cbedges = Checkbutton(master, text = 'Kanten zeichnen', var = check1, command = lambda:(cbfaces.deselect(), cbedges.select(), zeichnen()))
cbedges.grid(row = 0, column = 16, columnspan = 2, padx = 15, pady = 5)

cbfaces = Checkbutton(master, text = 'Flächen zeichnen', var = check2, command = lambda:(cbedges.deselect(), cbfaces.select(), zeichnen()))
cbfaces.grid(row = 1, column = 16, columnspan = 2, padx = 15, pady = 5)

labeldeg = Label(master, text = 'Drehungswinkel:')
labeldeg.grid(row = 3, column = 16, columnspan = 2)

cbdeg = Checkbutton(master, text = 'deg', var = checkdeg)
cbdeg.grid(row = 4, column = 17)
cbdeg.select()

editdeg = Entry(master, width = 8)
editdeg.grid(row = 4, column = 16, columnspan = 1, padx = 15, pady = 5)
editdeg.insert(10,'10')

buttonx = Button(master, text = 'rot x', command = lambda: rotxfunc(1))
buttonx.grid(row = 6, column = 16, padx = 10, pady = 5)

buttony = Button(master, text = 'rot y', command = lambda: rotyfunc(1))
buttony.grid(row = 7, column = 16, padx = 10,  pady = 5)

buttonz = Button(master, text = 'rot z', command = lambda: rotzfunc(1))
buttonz.grid(row = 8, column = 16, padx = 10,  pady = 5)

buttonmx = Button(master, text = 'rot -x', command = lambda: rotxfunc(-1))
buttonmx.grid(row = 6, column = 17, padx = 10,  pady = 5)

buttonmy = Button(master, text = 'rot -y', command = lambda: rotyfunc(-1))
buttonmy.grid(row = 7, column = 17, padx = 10,  pady = 5)

buttonmz = Button(master, text = 'rot -z', command = lambda: rotzfunc(-1))
buttonmz.grid(row = 8, column = 17, padx = 10,   pady = 5)

cbreprot = Checkbutton(master, text = 'weiterdrehen', var = checkrep)
cbreprot.grid(row = 9, column = 16, columnspan = 2, padx = 15, pady = 5)

cbiko = Checkbutton(master, text = 'Ikosaeder zeichnen', justify = 'left', var = check3, command = lambda:(deselectall(), cbiko.select(), ikosaeder()))
cbiko.grid(row = 10, column = 16, columnspan = 2, pady = 5)

cbokt = Checkbutton(master, text = 'Oktaeder zeichnen', justify = 'left', var = check4, command = lambda:(deselectall(), cbokt.select(), oktaeder()))
cbokt.grid(row = 11, column = 16, columnspan = 2, pady = 5)

cbkep = Checkbutton(master, text = 'Keplerstern zeichnen', justify = 'left', var = check5, command = lambda:(deselectall(), cbkep.select(), keplerstern()))
cbkep.grid(row = 12, column = 16, columnspan = 2, pady = 5)

cbdod = Checkbutton(master, text = 'Dodekaeder zeichnen', justify = 'left', var = check6, command = lambda:(deselectall(), cbdod.select(), dodekaeder()))
cbdod.grid(row = 13, column = 16, columnspan = 2, pady = 5)

cbwur = Checkbutton(master, text = 'Würfel zeichnen', justify = 'left', var = check7, command = lambda:(deselectall(), cbwur.select(), wuerfel()))
cbwur.grid(row = 14, column = 16, columnspan = 2, pady = 5)

buttontip = Button(master, text = 'Hinweis zu Farbeingabe', command = lambda:popup('tip'))
buttontip.grid(row = 15, rowspan = 1, column = 16, columnspan = 2)

buttonrefresh = Button(master, text = 'Farben aktualisieren', command = zeichnen)
buttonrefresh.grid(row = 16, column = 16, columnspan = 2, padx = 15, pady = 5)

cbfaces.select()
cbiko.select()
ikosaeder()

